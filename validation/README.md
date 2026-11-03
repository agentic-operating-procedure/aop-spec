# Validation

The reference validator implements the Phase 2 gate: a specimen AOP validates against the schema, and deliberately broken specimens fail with a diagnostic.

## Running

```
python3 validation/validate.py validation/fixtures/valid/specimen-aop.json
python3 validation/validate.py validation/fixtures/invalid/missing-dimension.json
```

Exit codes: 0 conformant, 1 nonconformant, 2 usage or I/O error.

## Scope of the implementation

- Schema: `schema/aop-document.schema.json`, using a documented subset of JSON Schema draft 2020-12: type (including type unions), required, properties, additionalProperties (false only), enum, const, pattern, minLength, minimum, maximum, minItems, maxItems, items, local `$ref`, `$defs`.
- Normative semantic checks the schema subset cannot express: variant frequency summation (NM-STR-3), authority coverage of the permitted set (NM-AUT-3, CC-7), escalation edges carrying a target role (NM-STR-6), and the case record field floor (NM-ASR-1).
- Dependencies: none. The validator is standard library only, so the gate can be re-run anywhere Python 3 runs.

## Fixtures

| Fixture | Expected | What it proves |
|---|---|---|
| `valid/specimen-aop.json` | pass | A complete fault management AOP, compiled from 12,417 observed cases, validates end to end |
| `invalid/missing-dimension.json` | fail | An AOP missing a dimension is not an AOP (NM-MODEL-1) |
| `invalid/unknown-authority-class.json` | fail | Authority classes are a closed enumeration (NM-AUT-2) |
| `invalid/bad-identifier.json` | fail | Identifiers follow the identifier scheme (NM-ID-2) |
| `invalid/frequency-sum-exceeds-one.json` | fail | Variant frequencies sum to at most 1.0 (NM-STR-3) |
| `invalid/fail-closed-disabled.json` | fail | The fail-closed rule cannot be switched off (NM-CON-3) |

The invalid fixtures are each generated from the valid specimen with exactly one defect, so a pass by the validator on an invalid fixture indicates a hole in the checks, not a marginal document.
