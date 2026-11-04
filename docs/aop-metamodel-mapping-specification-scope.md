# AOP Metamodel Mapping: The Staged Metamodel Against the Normative Model (Specification Scope)

Informative. This document maps the staged metamodel documents supplied by the programme owner (the AOP-MM stages 01 to 09) onto the normative model ratified for this estate. It records where the two align, where the metamodel goes further, and the reconciliation points that remain open. Per the governance model, reconciliation decisions are change requests against this repository, decided by the programme owner; this document surfaces them, it does not settle them.

## 1. The two sources

The ratified normative model (the eight dimensions, the network-native structure, the identifier and versioning scheme) is the document-level contract: what an AOP document must contain and how it binds a run.

The staged metamodel is the semantic model underneath: a register of 103 entities (AOP-E01 to AOP-E103) across nine stages, each stage owning one semantic area and declaring entities, relationships, invariants, design decisions and conformance levels L0 to L4.

| Stage | Area | Entity range (per the documents' own registers) |
|---|---|---|
| 01 to 02 | Foundation and core conceptual | E01 to E14 |
| 03 | Specification aspects (AS-01 to AS-16) | E26 to E40 reserved; unpinned in the transcribed sources |
| 04 | Decision and autonomy | E15 to E25 |
| 05 | Operational logic | within E26 to E40; unpinned in the transcribed sources |
| 06 | Capability, agent, resource | E41 to E60 |
| 07 | Execution, coordination and runtime semantics | E61 to E75 |
| 08 | Exception, recovery and resilience semantics | E76 to E86 |
| 09 | Governance, assurance and lifecycle semantics | E87 to E103 |

An earlier version of this table assumed different range boundaries; the documents' own registers supersede that assumption. The authoritative entity register with names and definitions is the metamodel entity register document.

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

## 5. Reconciliation points and their dispositions

The dispositions below were settled by the programme owner through CR-009-9, CR-015 and CR-010 (2026-11-04 and 2026-11-05). This section records the final state; the reasoning for each is in the linked artefacts.

1. **Hierarchy and metamodel levels. RESOLVED (CR-010, 2026-11-05).** The six-level conceptual hierarchy and the four-level metamodel scope are complementary views with one normative mapping: the metamodel frames the six levels (its Level 1 the metamodel itself, its Level 4 the runtime the six levels operationalise through). The conceptual hierarchy document and the glossary carry the mapping vocabulary; this section records the disposition.
2. **Dimension count in source documents. RESOLVED (CR-010, 2026-11-05).** The ratified eight is normative; the six-dimension source wording is marked superseded by the source errata document in `aop-foundations`.
3. **Harness-AOP relationship.** The framing paper states the harness is the top-level AOP for its domain; the introduction says an AOP is not a harness. The ratified position (SEC-11) adopts the top-level-AOP statement. The metamodel's Stage 01 decision that the Agent Harness is not part of the AOP is consistent with this and should be cited.
4. **Compiled versus authored provenance.** The framing paper requires compilation from observation; the introduction permits authoring through the six-stage procedural engineering process without observation. The normative model adopts compiled provenance for authority-bearing rules (NM-PRV-3) while permitting authored intent hypotheses (NM-INT-3). Whether an entirely authored AOP can conform, and under which profile, is open.
5. **Runtime vocabulary adoption. RESOLVED IN PART (2026-11-05).** The run state machine and action contract (RA-1 to RA-14) adopt the runtime semantics normatively; the run outcome dispositions and the recovery model were already absorbed. The full E61 to E75 entity naming remains available through the register for provenance citations rather than duplicated into the schema.
6. **Conformance levels.** RESOLVED 2026-11-05: the estate keeps binary suites and expresses graduation as named tiers over cumulative suite supersets (Validated, Enforced, Adversarially Tested, Assured). The metamodel's per-stage L0 to L4 cross-map informatively to those tiers; the mapping is stated in the certification process document. Graduated conformance semantics are not adopted.
7. **Entity register publication. RESOLVED (CR-010, 2026-11-05).** Published as the metamodel entity register document in this repository, with the transcription caveat recorded: E26 to E40 are unpinned pending the Stage 03 and 05 sources.

## 6. Why this mapping exists

The estate's authority depends on traceability: every normative claim should reach the source it came from. This document is that trace for the metamodel. It keeps the staged metamodel from becoming a second, drifting source of truth by stating explicitly which material has been absorbed, where it landed, and what remains open.
