#!/usr/bin/env python3
"""AOP reference validator.

Validates an AOP document against schema/aop-document.schema.json using a
documented subset of JSON Schema draft 2020-12, plus the normative semantic
checks that a schema cannot express (frequency summation, permitted-set
coverage). Implements the Phase 2 gate: a specimen AOP validates, and a
deliberately broken specimen fails with a diagnostic.

Supported schema keywords: type (including type unions), required,
properties, additionalProperties (false only), enum, const, pattern,
minLength, minimum, maximum, minItems, maxItems, items, $ref (local
#/$defs/...), $defs.

Usage:
    python3 validation/validate.py <aop-document.json> [--schema schema/aop-document.schema.json]

Exit codes: 0 conformant, 1 nonconformant, 2 usage or I/O error.
"""

import json
import re
import sys
from pathlib import Path

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "schema" / "aop-document.schema.json"


class Diagnostics:
    def __init__(self):
        self.errors = []

    def add(self, path, message):
        self.errors.append("%s: %s" % (path if path else "$", message))

    def ok(self):
        return not self.errors


def resolve_ref(schema_root, ref):
    if not ref.startswith("#/"):
        raise ValueError("only local $ref values are supported: %s" % ref)
    node = schema_root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def validate(instance, schema, schema_root, path, diag):
    """Validate one instance against one schema node."""
    if "$ref" in schema:
        validate(instance, resolve_ref(schema_root, schema["$ref"]), schema_root, path, diag)
        return

    # type
    expected = schema.get("type")
    if expected is not None:
        types = expected if isinstance(expected, list) else [expected]
        checks = {
            "object": lambda v: isinstance(v, dict),
            "array": lambda v: isinstance(v, list),
            "string": lambda v: isinstance(v, str),
            "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
            "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
            "boolean": lambda v: isinstance(v, bool),
            "null": lambda v: v is None,
        }
        if not any(checks[t](instance) for t in types):
            diag.add(path, "expected type %s, got %s" % (expected, type(instance).__name__))
            return

    # enum and const
    if "enum" in schema and instance not in schema["enum"]:
        diag.add(path, "value %r is not one of %r" % (instance, schema["enum"]))
    if "const" in schema and instance != schema["const"]:
        diag.add(path, "value %r does not equal the required constant %r" % (instance, schema["const"]))

    # string checks
    if isinstance(instance, str):
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            diag.add(path, "value %r does not match pattern %r" % (instance, schema["pattern"]))
        if "minLength" in schema and len(instance) < schema["minLength"]:
            diag.add(path, "string shorter than minLength %d" % schema["minLength"])

    # numeric checks
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            diag.add(path, "value %r below minimum %r" % (instance, schema["minimum"]))
        if "maximum" in schema and instance > schema["maximum"]:
            diag.add(path, "value %r above maximum %r" % (instance, schema["maximum"]))

    # object checks
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                diag.add(path, "missing required member %r" % key)
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in props:
                    diag.add(path, "member %r is not an allowed property" % key)
        for key, subschema in props.items():
            if key in instance:
                validate(instance[key], subschema, schema_root,
                         "%s/%s" % (path, key) if path else key, diag)

    # array checks
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            diag.add(path, "array has fewer than %d items" % schema["minItems"])
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            diag.add(path, "array has more than %d items" % schema["maxItems"])
        if "items" in schema:
            for index, item in enumerate(instance):
                validate(item, schema["items"], schema_root, "%s[%d]" % (path, index), diag)


def normative_checks(doc, diag):
    """Semantic checks the JSON Schema subset cannot express."""
    structure = doc.get("structure", {})
    variants = structure.get("variants", [])

    # NM-STR-3: variant frequencies sum to at most 1.0.
    total = sum(v.get("frequency", 0) for v in variants)
    if total > 1.0:
        diag.add("$", "variant frequencies sum to %s, above the 1.0 ceiling (NM-STR-3)" % total)

    # NM-AUT-3 / CC-7: every permitted action is covered by a decision rule
    # or by the declared default authority class.
    permitted = doc.get("constraints", {}).get("permitted_actions", [])
    thens = " ".join(
        rule.get("then", "")
        for v in variants
        for rule in v.get("decision_rules", [])
    )
    has_default = "default_authority_class" in doc.get("authority", {})
    for action in permitted:
        if action.lower() not in thens.lower() and not has_default:
            diag.add("$", "permitted action %r is covered by neither a decision rule nor a declared default authority class (NM-AUT-3, CC-7)" % action)

    # NM-STR-9: no variant may be marked as matched on unknown context; the
    # fail-closed const in the schema covers the declarative part. Here we
    # check exception edges that escalate carry a target role (NM-STR-6).
    for index, edge in enumerate(structure.get("exception_edges", [])):
        if edge.get("behaviour") == "escalate" and not edge.get("target_role"):
            diag.add("$", "exception edge %d escalates without a target role (NM-STR-6)" % index)

    # NM-ASR-1: case record carries the seven mandatory fields.
    fields = doc.get("assurance", {}).get("case_record", {}).get("fields", [])
    required_fields = {"inputs", "context snapshot", "rule", "provenance", "decision", "approver", "outcome"}
    missing = {f for f in required_fields if not any(f in field.lower() for field in fields)}
    if missing:
        diag.add("$", "case record fields missing mandatory members: %s (NM-ASR-1)" % ", ".join(sorted(missing)))


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    document_path = Path(argv[1])
    schema_path = Path(argv[3]) if len(argv) > 3 and argv[2] == "--schema" else DEFAULT_SCHEMA

    try:
        doc = json.loads(document_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print("cannot read document: %s" % exc, file=sys.stderr)
        return 2
    try:
        schema = json.loads(schema_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print("cannot read schema: %s" % exc, file=sys.stderr)
        return 2

    diag = Diagnostics()
    validate(doc, schema, schema, "", diag)
    if diag.ok():
        normative_checks(doc, diag)

    if diag.ok():
        print("CONFORMANT: %s satisfies the AOP document schema and the normative semantic checks." % document_path.name)
        return 0

    print("NONCONFORMANT: %s failed with %d diagnostic(s):" % (document_path.name, len(diag.errors)))
    for error in diag.errors:
        print("  - %s" % error)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
