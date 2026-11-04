# Changelog

All notable changes to this repository are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning is semantic: the major version changes when the meaning of a dimension, the authority model, or the permitted-set semantics change, the minor version when substantive normative content is added, and the patch version for corrections that do not change meaning.

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

[Unreleased]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.5.0...HEAD
[v0.5.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/agentic-operating-procedure/aop-spec/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/agentic-operating-procedure/aop-spec/releases/tag/v0.1.0
