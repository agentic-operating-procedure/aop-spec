# AOP-MM Entity Register: The Staged Metamodel's Entities With Stable Identifiers (Specification Scope)

Informative. This document publishes the staged metamodel's entity register (reconciliation point 7) with stable identifiers, transcribed from the programme owner's source documents. It is the citation surface for provenance claims that need to name a metamodel entity.

## 1. The transcription caveat, stated first

The register below records exactly what the local source documents write. The numbering follows the documents' own registers: Stage 02 registers E01 to E14, Stage 04 introduces E15 to E25, and Stage 06 introduces E41 to E60. Stage 03 and Stage 05 deliverables were not present in the transcribed sources, so **E26 to E40 cannot be pinned to names from these sources** and are recorded as unpinned. Earlier working notes had assumed different range boundaries; this document supersedes those assumptions. Where the documents renumber or retire (Stage 04 retires E09 as a composite, splitting it into E15, E17, E18, E19 and the Decision Right family), the register records the retirement.

## 2. Stage 02: Foundation and core conceptual (E01 to E14)

| ID | Entity | Definition (as written) |
|---|---|---|
| AOP-E01 | Agentic Operating Procedure | The persistent identity of an agentic operational specification |
| AOP-E02 | AOP Version | An immutable, identifiable version of an AOP containing its normative specification |
| AOP-E03 | Operational Intent | The declared purpose or intended operational change that the AOP exists to achieve |
| AOP-E04 | Operational Domain | The domain within which the AOP is applicable and governed |
| AOP-E05 | Operational Context | The contextual conditions and relevant information governing applicability and execution |
| AOP-E06 | Operational Trigger | An event, condition or authorised request that initiates consideration or activation of an AOP |
| AOP-E07 | Operational Precondition | A condition that must be satisfied before a defined AOP execution or activity can proceed |
| AOP-E08 | Operational Constraint | A mandatory boundary or restriction governing permitted operational behaviour |
| AOP-E09 | Decision Authority | Retired in Stage 04 as a composite; split into E15, E17, E18, E19 and the Decision Right family |
| AOP-E10 | Operational Outcome | A result or state of affairs that the AOP is intended to achieve |
| AOP-E11 | Outcome Criterion | A defined condition used to determine whether an operational outcome has been achieved acceptably |
| AOP-E12 | AOP Composition | A governed relationship through which one AOP incorporates or delegates part of its operational intent to another AOP |
| AOP-E13 | Source Artefact | An identifiable external operational artefact from which requirements, constraints or other AOP content originate |
| AOP-E14 | Source Traceability | A formal association between an AOP element and the source artefact or element that justifies or informs it |

## 3. Stage 04: Decision and autonomy (E15 to E25)

| ID | Entity | Definition (as written) | Classification |
|---|---|---|---|
| AOP-E15 | Principal | An identifiable human, organisational or non-human actor capable of holding or exercising authority | Identity |
| AOP-E16 | Decision Specification | A normative definition of an operational decision point within an AOP Version | Decision |
| AOP-E17 | Decision Right | An explicit entitlement to make or participate in a defined decision category | Authority |
| AOP-E18 | Authority Grant | A governed assignment of authority to a principal within a defined scope | Authority |
| AOP-E19 | Delegation | A governed transfer or assignment of decision authority from one principal to another | Authority |
| AOP-E20 | Autonomy Allocation | A defined operating mode and discretion boundary assigned to a Decision Specification | Autonomy |
| AOP-E21 | Oversight Control | A defined human oversight or intervention mechanism | Oversight |
| AOP-E22 | Decision Record | A runtime record of a decision occurrence | Runtime |
| AOP-E23 | Decision Assessment | An evaluation of the decision's validity, evidence, confidence, risk or compliance | Assurance |
| AOP-E24 | Decision Intervention | A recorded intervention affecting a decision or its execution | Runtime |
| AOP-E25 | Escalation Rule | A governed rule for transferring a decision or exception to a higher or alternative authority | Governance |

## 4. Unpinned: E26 to E40

The Stage 03 (specification aspects) and Stage 05 (operational logic) deliverables were not present in the transcribed sources. Their entity IDs are reserved; their names are recorded through the aspect register (section 6) where aspects are named. Transcription completes when the Stage 03 and 05 sources are supplied.

## 5. Stage 06: Capability, agent and resource (E41 to E60)

| ID | Entity | Definition (as written) | Classification |
|---|---|---|---|
| AOP-E41 | Capability Requirement | Normative ability required for an activity or execution scope | Requirement |
| AOP-E42 | Agent Capability | Qualified ability attributable to an agent | Capability |
| AOP-E43 | Agent Profile | Declared operational characteristics and qualifications of an agent or agent class | Agent |
| AOP-E44 | Agent Identity | Identity of a distinct execution actor | Agent |
| AOP-E45 | Agent Role | Responsibility assigned to an agent within an execution arrangement | Agent |
| AOP-E46 | Agent Skill Specification | Versioned definition of reusable invocable functionality | Skill |
| AOP-E47 | Skill Invocation | Runtime occurrence of a skill invocation | Runtime |
| AOP-E48 | Tool Specification | Definition of an external operation, service or interface | Resource |
| AOP-E49 | Tool Operation | Defined operation exposed by a tool | Resource |
| AOP-E50 | Knowledge Resource | Governed source or representation of knowledge | Knowledge |
| AOP-E51 | Information Resource | Governed source of data or information | Information |
| AOP-E52 | Capability Qualification | Evidence-backed qualification of a resource for a defined capability | Assurance |
| AOP-E53 | Capability Resolution | Record of matching requirements to eligible resources | Runtime |
| AOP-E54 | Resource Assignment | Binding of a resolved resource to an execution responsibility | Runtime |
| AOP-E55 | Resource Substitution | Governed replacement of a resource | Runtime |
| AOP-E56 | Harness Requirement | Normative requirement placed on an execution environment | Requirement |
| AOP-E57 | Resource Dependency | Dependency between an activity or skill and an execution resource | Requirement |
| AOP-E58 | Resource Binding | Runtime binding of an authorised resource to an execution context | Runtime |
| AOP-E59 | Capability Composition | Relationship between capabilities that compose or depend on one another | Capability |
| AOP-E60 | Resource Compatibility | Assessment of whether a resource is compatible with an AOP requirement or execution environment | Assurance |

## 6. The specification aspects (AS-01 to AS-16)

| Aspect | Name | Note |
|---|---|---|
| AS-01 | Identity and Classification | Transcribed from the Stage 06 source |
| AS-02 | Unnamed in the transcribed sources | The Stage 7 cross-reference jumps AS-01 to AS-03; name completes on transcription |
| AS-03 | Scope and Applicability | Recovered from the Stage 7 cross-reference |
| AS-04 | Operational Context | Transcribed |
| AS-05 | Triggers and Preconditions | Recovered from the Stage 7 cross-reference |
| AS-06 | Outcomes and Objectives | Recovered from the Stage 7 cross-reference |
| AS-07 | Operational Logic | Transcribed |
| AS-08 | Authority and Autonomy | Transcribed |
| AS-09 | Policies and Constraints | Transcribed |
| AS-10 | Capability Requirements | Transcribed |
| AS-11 | Execution and Coordination | Transcribed |
| AS-12 | Exception and Recovery | Transcribed |
| AS-13 | Verification and Assurance | Transcribed |
| AS-14 | Evidence and Auditability | Transcribed |
| AS-15 | Governance and Lifecycle | Transcribed |
| AS-16 | Source Traceability and Transformation | Transcribed |

## 7. Stages 07 to 09 (E61 to E103)

The runtime (E61 to E75), exception and resilience (E76 to E86) and governance and lifecycle (E87 to E103) entities are transcribed in the metamodel mapping document's alignment section, which is their citation surface. This register does not duplicate them.

## 8. How this register is used

A provenance claim, a mapping row, or a reconciliation decision may cite an entity by identifier: for example, "the delegation clause (NM-AUT-9) implements AOP-E19 with attenuation". The register is informative: it names the metamodel's vocabulary; the normative clauses of this specification remain the binding text.
