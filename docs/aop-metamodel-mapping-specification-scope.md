# AOP Metamodel Mapping: The Staged Metamodel Against the Normative Model (Specification Scope)

Informative. This document maps the staged metamodel documents supplied by the programme owner (the AOP-MM stages 01 to 09) onto the normative model ratified for this estate. It records where the two align, where the metamodel goes further, and the reconciliation points that remain open. Per the governance model, reconciliation decisions are change requests against this repository, decided by the programme owner; this document surfaces them, it does not settle them.

## 1. The two sources

The ratified normative model (the eight dimensions, the network-native structure, the identifier and versioning scheme) is the document-level contract: what an AOP document must contain and how it binds a run.

The staged metamodel is the semantic model underneath: a register of 103 entities (AOP-E01 to AOP-E103) across nine stages, each stage owning one semantic area and declaring entities, relationships, invariants, design decisions and conformance levels L0 to L4.

| Stage | Area | Entity range |
|---|---|---|
| 01 | Foundation | E01 to E08 |
| 02 | Core conceptual | E09 to E20 |
| 03 | Specification aspects (AS-01 to AS-16) | E21 to E32 |
| 04 | Decision and autonomy | E33 to E44 |
| 05 | Operational logic | E45 to E52 |
| 06 | Capability, agent, resource | E53 to E60 |
| 07 | Execution, coordination and runtime semantics | E61 to E75 |
| 08 | Exception, recovery and resilience semantics | E76 to E86 |
| 09 | Governance, assurance and lifecycle semantics | E87 to E103 |

## 2. Alignment: where the metamodel and the normative model agree

- **Authority is bounded and externally enforced.** The metamodel's decision and autonomy stage and the normative Authority dimension state the same thing: authority is per decision, bounded by the specification, and enforced outside the executor.
- **A run references one immutable AOP version.** Metamodel invariant S07-D02 and NM-STR-11 agree.
- **Normative change produces a new version.** Metamodel invariant S09-C11 and NM-VER-2 agree.
- **Evidence does not rewrite the specification.** The Stage 09 learning feedback rule and NM-ASR-4 agree.
- **Approval, release and operational authorisation are distinct.** Stage 09's three-dimension lifecycle status and NM-VER-4 to NM-VER-5 agree.

## 3. Coverage: which metamodel material the normative model absorbs

| Metamodel material | Where it lands in this estate |
|---|---|
| Eight-dimension content requirements | The normative model clauses (this repository) |
| 16 specification aspects (AS-01 to AS-16) | Mapped onto the eight dimensions in section 4; a finer decomposition that informs clause-level checks |
| Decision and autonomy entities (E33 to E44) | The Authority dimension, the decision-rule shape (NM-STR-4) and the authority classes (NM-AUT-2) |
| Runtime entities (E61 to E75): AOP Run, Execution Context, Agent Session, Activity Instance, Coordination Arrangement, Runtime Event, Execution State, Synchronisation Point, Human Interaction Request, Runtime Handoff, Runtime Assurance Record, Runtime Failure, Runtime Recovery, Runtime Evidence Record, Run Outcome | `aop-architecture` (layer and pipeline semantics) and `aop-reference-harness` (runtime implementation); the run outcome dispositions are normative here (NM-STR-14) |
| Exception, recovery and resilience entities (E76 to E86) | Exception edges and the Control dimension here; the recovery state machines belong to `aop-architecture` (trust architecture) and `aop-context-graph` (observed exceptions) |
| Governance, assurance and lifecycle entities (E87 to E103) | The identifier and versioning document (lifecycle status), `aop-governance` (the estate's own change model) and `aop-registry` (release and publication) |
| 14 foundational principles (AOP-P01 to P14) | `aop-foundations`, as the discipline's principle set |
| Stage 10 (transformation, migration and AOP engineering semantics) | `aop-toolkit` (SOP intake and translation) and `aop-adoption` (the migration playbook) |

## 4. The 16 aspects mapped to the eight dimensions

| Aspect (Stage 03) | Dimension |
|---|---|
| AS-01 Operational Intent | Intent |
| AS-02 Outcome and Success Criteria | Intent |
| AS-03 Scope and Applicability | Intent |
| AS-04 Operational Context | Context |
| AS-05 Data and Information Requirements | Context |
| AS-06 Operational Logic | Control |
| AS-07 Procedure Structure | Control |
| AS-08 Authority and Autonomy | Authority |
| AS-09 Decision Rules and Thresholds | Authority |
| AS-10 Constraints and Prohibitions | Constraints |
| AS-11 Capability Requirements | Capabilities |
| AS-12 Agent and Role Assignment | Coordination |
| AS-13 Interaction and Handoff | Coordination |
| AS-14 Exception and Recovery | Control |
| AS-15 Evidence and Assurance | Assurance |
| AS-16 Source Traceability and Transformation | Assurance (provenance) |

The mapping is informative. It shows the eight dimensions are a coarser but complete decomposition of the same surface: every aspect lands on exactly one primary dimension, and the conformance clauses test the aspects through the dimensions.

## 5. Open reconciliation points

These are surfaced for the programme owner. Each is a candidate change request; none is decided here.

1. **Hierarchy and metamodel levels.** The ratified six-level conceptual hierarchy (discipline, AOP, skill, harness, agent, agentic operations) does not appear in the metamodel documents, which use a four-level scope (metamodel, AOP specifications, operationalisation, runtime). The two are complementary views, but the mapping between the six levels and the four levels should be stated once, normatively, to prevent drift.
2. **Dimension count in source documents.** The executive summary lists six dimensions; the framing paper and the introduction list eight. The ratified eight is normative here; the source inconsistency should be closed by a note in `aop-foundations` or an erratum in the source documents.
3. **Harness-AOP relationship.** The framing paper states the harness is the top-level AOP for its domain; the introduction says an AOP is not a harness. The ratified position (SEC-11) adopts the top-level-AOP statement. The metamodel's Stage 01 decision that the Agent Harness is not part of the AOP is consistent with this and should be cited.
4. **Compiled versus authored provenance.** The framing paper requires compilation from observation; the introduction permits authoring through the six-stage procedural engineering process without observation. The normative model adopts compiled provenance for authority-bearing rules (NM-PRV-3) while permitting authored intent hypotheses (NM-INT-3). Whether an entirely authored AOP can conform, and under which profile, is open.
5. **Runtime vocabulary adoption.** The metamodel's runtime entities (E61 to E75) are richer than the runtime sequence in NM-STR-13. Adopting the entity names into the schema and the harness profile is proposed for the Wave 4 repos.
6. **Conformance levels.** RESOLVED 2026-11-05: the estate keeps binary suites and expresses graduation as named tiers over cumulative suite supersets (Validated, Enforced, Adversarially Tested, Assured). The metamodel's per-stage L0 to L4 cross-map informatively to those tiers; the mapping is stated in the certification process document. Graduated conformance semantics are not adopted.
7. **Entity register publication.** The 103-entity register currently exists only in the owner's source documents. Publishing it in this repository or in `aop-context-graph`, with stable identifiers, is proposed so that provenance claims can cite it.

## 6. Why this mapping exists

The estate's authority depends on traceability: every normative claim should reach the source it came from. This document is that trace for the metamodel. It keeps the staged metamodel from becoming a second, drifting source of truth by stating explicitly which material has been absorbed, where it landed, and what remains open.
