# Changelog

All notable changes to this repository are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning is semantic: the major version changes when the meaning of a dimension, the authority model, or the permitted-set semantics change, the minor version when substantive normative content is added, and the patch version for corrections that do not change meaning.

## [Unreleased]

## [0.6.0] - 2026-11-05

### Added (Wave H3: CR-021, CR-022, CR-024, CR-025, CR-026)

- Supply-chain attestation: NM-VER-7 (published artefacts bind inputs, builder, toolchain and digest; unsigned-effective is refused) and SK-12 (skill maintainer, dependency lineage, update review).
- Revalidation: NM-VER-8 (the run component matrix; impact-classified gates; no inherited evaluation claims across material changes).
- Workload identity and egress: SEC-16, SEC-17.
- Erasure-compatible evidence: NM-ASR-7 (integrity metadata never erases; tombstone or cryptographic erasure; replay claims narrowed explicitly).
- In-flight migration: RA-23 (linked new run; the original record is never rewritten).
- Schema: `build_attestation`; skill `maintainer` and `dependencies`. Conformance clauses CC-31 to CC-34.

### Dispositions

- Metamodel reconciliation points 3 and 4 closed: the harness relationship (SEC-11, the errata, HM-2's composition rule) and compiled-versus-authored provenance (an authored AOP validates as a document but cannot be operationally authorised without observed, ratified rules).

## [0.5.0] - 2026-11-05

### Added (Wave H2: CR-013, CR-016, CR-017, CR-020, CR-023)

- The approval object: RA-15 to RA-19 (digest and expiry binding, the four-outcome interface where non-response is never approval, approver eligibility and independence, re-check at issuance and execution, oversight metrics and canary detection).
- Parameter-level constraints: RA-20 to RA-22 (typed schemas, canonical payload validation after transformations, fail-closed on tampering).
- Revocation, rollback and compatibility: NM-VER-6.
- Loop hygiene: NM-CTL-6 (case origin, the protected human reservoir) and NM-AUT-10 (ratification requires a human-reviewed corpus).
- Schema: evidence-bundle `action_digest`, `expiry`, `approver_outcome`; AOP `action_schemas` and the `oversight` block.
- Conformance clauses CC-28 to CC-30; validator check CC-29, crediting `target_scope` as a bound form; must-fail fixture parameter-schema-without-bounds.
- Published the metamodel entity register (reconciliation point 7) and the dispositions for points 1, 2, 5 and 7; the context element `key` binding.

## [0.4.0] - 2026-11-04

### Added (Wave H1: CR-011, CR-012, CR-009-3)

- Published the run and action semantics (RA-1 to RA-14): the run state machine, action digests and the authorization binding, idempotency and retry classes, duplicate delivery, concurrency safeguards, partial success and compensation, cancellation, and the enumerated degraded modes.
- Published the evidence and replay semantics (RP-1 to RP-7): the replay levels R1 record verification, R2 decision-trace reconstruction, R3 controlled re-execution; reconstruction never authorises re-execution; R2 from the record alone without trusting the producer.
- Published the cumulative authority clauses: NM-CRD-4 (aggregate limits enforced beside the authority check), NM-AUT-8 (reversibility classes; irreversible never autonomous; compensable declares its path), NM-AUT-9 (delegation attenuation).
- Schema: `reversibility_classes`, `delegation_attenuation`, `aggregate_limits`, `replay_level`.
- Validator check CC-25, including the default-class fall-through: an irreversible action may be neither governed by an autonomous rule nor left to an autonomous default.
- Must-fail fixtures: irreversible-autonomous, compensable-without-path.
- Metamodel reconciliation point 6 settled: named tiers over binary suites; graduated conformance semantics are not adopted.

## [0.3.0] - 2026-11-04

### Added (CR-009 block 1: robustness hardening)

- Trust-classed case facts: NM-CTX-5 (trust class per context element: system-attested, derived, model-asserted, untrusted-content), NM-STR-16 (only system-attested and derived facts are visible to the policy decision point), NM-STR-17 (absent attested facts are unknown and escalate, never default to permitted), with the schema `trust_class` and the validator static check CC-24.
- The ratification gate: NM-AUT-7 (rule status observed, reviewed, ratified; only ratified rules grant authority), NM-STR-18 (minimum support floor), NM-PRV-6 (stitching confidence propagation caps ratification), with validator checks CC-21 and CC-22.
- Accountability and the trust base: NM-GOV-1 (accountable owner required), CC-23 (ratifier differs from preparer), SEC-14 (hold on enforcement unavailability), SEC-15 (emergency stop, owner-gated resumption).
- Must-fail fixtures: unratified-authority, untrusted-authority-basis, variant-below-support, missing-accountable-owner.

### Fixed

- The non-attested-fact check matches element names in both declaration form (`mttr-estimate`) and condition identifier form (`mttr_estimate`).

## [0.2.2] - 2026-11-05

### Added

- Coordination handoffs may carry a kind: approval or informational. An approval handoff routes a decision to the recipient; an informational handoff only informs. The default is approval. Found by the 5G exemplar shadow run, whose comparator was counting shift-log notifications as approver rulings.


## [0.2.1] - 2026-11-04

### Fixed

- The AOP identifier pattern accepts the harness identifier form (HR-) beside the procedure form (AP-), because the harness is the top-level AOP for its domain (SEC-11, NM-ID-2).
- Variant identifiers may carry hyphens.
- Decision rules may carry an optional applies_to action scope, so a rule such as a prohibited escalation threshold governs the actions it names rather than every action on the path.


## [0.2.0] - 2026-11-04

### Added

- Published the process alignment clauses: NM-INT-4 associates the procedure with the OpenDEA Business Process Catalog by reference or declared gap, and NM-INT-5 binds human baseline metrics to canonical performance metrics (dea:metric-*) or declares the gap for lodging as a contribution. The association is by reference and never by copy; inventing an identifier is prohibited.
- Added the optional process_alignment block to the AOP document schema, and the matching semantic checks to the reference validator.
- The specimen AOP now demonstrates both sides of the rule: three canonical metric references and two declared metric gaps, plus a declared process gap for network line fault management.


## [0.1.1] - 2026-11-04

### Fixed

- Guarded the NM-ASR-1 semantic check so it applies only where the document declares a case record with its field list. A non-AOP document validated against another schema was previously diagnosed against AOP-specific checks. No AOP document result changes; the full fixture gate was re-run unchanged.


## [0.1.0] - 2026-11-03

### Normative specification

- Published the eight-dimension normative model as clauses: Intent, Context, Constraints, Authority, Capabilities, Coordination, Control, Assurance, with the decision-rights ladder over the five risk axes.
- Published the network-native procedure structure: variants, decision points, exception edges, rework loops, matching and failure semantics, and runtime binding.
- Published the identifier scheme, the versioning model, and the provenance and lineage requirements, including the three-dimension lifecycle status.
- Published the Agent Skill contract as a normative annex (D-003).
- Published the normative security clauses, including the rule that the authority check runs outside the model context (SEC-1) and the rule that the harness is the top-level AOP for its domain (SEC-11).
- Published the conformance clauses for AOP documents (CC-1 to CC-20).
- Published the metamodel mapping: how the staged metamodel documents (AOP-MM stages 01 to 09) map onto the normative model, with the open reconciliation points surfaced for the programme owner.
- Published the machine-readable schemas: the AOP document schema, the Agent Skill declaration schema, and the approver evidence bundle schema.
- Published the reference validator and the fixture set, and passed the Phase 2 gate: the specimen AOP validates, and every deliberately broken specimen fails with a diagnostic.
[0.1.0]: https://github.com/agentic-operating-procedure/aop-spec/releases/tag/v0.1.0
[0.1.1]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.1.0...v0.1.1
[0.2.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.1.1...v0.2.0
[0.2.1]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.2.0...v0.2.1
[0.2.2]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.2.1...v0.2.2
[Unreleased]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.6.0...HEAD
[0.3.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.2.2...v0.3.0
[0.4.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.3.0...v0.4.0
[0.5.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.4.0...v0.5.0
[0.6.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.5.0...v0.6.0
