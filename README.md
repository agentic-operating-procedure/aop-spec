# AOP Spec

`aop-spec` is the single authority for the normative model of the Agentic Operating Procedure: the eight dimensions, the network-native procedure structure, the identifier and versioning scheme, the machine-readable schema, the Agent Skill contract, the normative security clauses, and the conformance clauses an AOP document must satisfy.

| Field | Value |
|---|---|
| Authority | The normative model: dimensions, structure, identifiers, schema, contracts, conformance clauses |
| Tier | Specification |
| Landing wave | 2 |
| Version | 0.4.0 |
| Status | Stable |
| Licence | MIT |

## What this repository owns

- The eight-dimension normative model: Intent, Context, Constraints, Authority, Capabilities, Coordination, Control, Assurance. All eight are mandatory; an AOP document that omits one is not an AOP.
- The network-native procedure structure: variants, decision points, exception edges, rework loops, and the runtime binding semantics for each.
- The identifier scheme and the versioning and provenance model, including lineage from a source SOP and from the observed cases an AOP was compiled from.
- The machine-readable schema for an AOP document, for an Agent Skill declaration, and for an approver evidence bundle, with a reference validator.
- The normative Agent Skill contract, published as an annex (D-003).
- The normative security clauses, including the rule that the authority check runs outside the model context, and the rule that the harness is the top-level AOP for its domain.
- The conformance clauses for AOP documents.

## What this repository does not own

- The prose rationale for the model, the six-level hierarchy, or the glossary. That is `aop-foundations`.
- The layering, the trust architecture, the pipeline topology, or the threat model. That is `aop-architecture`.
- The change process and the decision records. That is `aop-governance`.
- Implementations of the schema: the linter, the compiler, the SDK. That is `aop-toolkit`.

## How to read this repository

The normative model is stated as clauses with stable identifiers of the form `NM-<area>-<n>`. Conformance clauses use `CC-<n>`. Security clauses use `SEC-<n>`. A clause uses MUST, MUST NOT, SHOULD and MAY in the sense of RFC 2119.

The machine-readable schema is JSON Schema (draft 2020-12). A JSON Schema subset is used, and the reference validator in `validation/` implements exactly that subset with no external dependencies. YAML is an allowed surface syntax that maps onto the same schema; this repository publishes JSON fixtures only.

## Documents

| Document | Scope |
|---|---|
| [The normative model](./docs/aop-normative-model-specification-scope.md) | The eight dimensions as normative clauses, and the decision-rights ladder |
| [Procedure structure](./docs/aop-procedure-structure-specification-scope.md) | Variants, decision points, exception edges, rework loops, runtime binding |
| [Identifiers and versioning](./docs/aop-identifier-and-versioning-specification-scope.md) | Identifier scheme, versioning, provenance and lineage |
| [The Agent Skill contract](./docs/aop-agent-skill-contract-specification-scope.md) | Normative annex: what a skill must declare |
| [Normative security clauses](./docs/aop-normative-security-clauses-specification-scope.md) | Out-of-context authority enforcement, credentials, fail-closed behaviour |
| [Conformance clauses](./docs/aop-conformance-clauses-specification-scope.md) | What a conforming AOP document must satisfy |
| [Run and action semantics](./docs/aop-run-and-action-semantics-specification-scope.md) | The run state machine and the side-effecting action contract |
| [Evidence and replay semantics](./docs/aop-evidence-and-replay-semantics-specification-scope.md) | The replay levels and their provenance floors |
| [Metamodel mapping](./docs/aop-metamodel-mapping-specification-scope.md) | How the staged metamodel maps onto the normative model, and the open reconciliation points |

## Validation

The Phase 2 gate requires that a specimen AOP validates against the schema, and that the validator fails correctly on a deliberately broken specimen.

```
python3 validation/validate.py validation/fixtures/valid/specimen-aop.json
python3 validation/validate.py validation/fixtures/invalid/missing-dimension.json
```

The validator exits 0 on a conformant document and 1 with a diagnostic on a nonconformant one.
