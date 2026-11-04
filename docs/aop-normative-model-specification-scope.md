# AOP Normative Model: The Eight Dimensions and the Decision-Rights Ladder (Specification Scope)

Normative. This document states the eight dimensions of an Agentic Operating Procedure as clauses. A clause is binding on every AOP document that claims conformance. RFC 2119 key words apply.

## 1. Status of the eight dimensions

NM-MODEL-1: An AOP document MUST populate all eight dimensions: Intent, Context, Constraints, Authority, Capabilities, Coordination, Control, Assurance.

NM-MODEL-2: The eight dimensions MUST appear as top-level members of the AOP document, each carrying a non-empty value.

NM-MODEL-3: An AOP document that omits a dimension is not a degraded AOP. It is not an AOP, and it MUST NOT be published, catalogued or executed as one.

NM-MODEL-4: The content of each dimension is domain-specific. This specification binds the presence, the semantics and the machine-readable shape of each dimension; it does not bind domain content.

## 2. Intent

The operational objective and the desired outcome, stated so that an executor can interpret rather than merely comply.

NM-INT-1: The Intent dimension MUST state the operational objective as a verifiable outcome condition, not as a sequence of activities.

NM-INT-2: The Intent dimension MUST state the scope boundary of the objective: what cases the AOP covers and what cases it does not.

NM-INT-3: Where the AOP was compiled from a source SOP, the Intent dimension MUST carry the intent hypothesis derived from that SOP, so that the claim the observation tested is recoverable.

NM-INT-4: An AOP SHOULD carry a process alignment block associating the procedure with the enterprise process catalog deployed from the OpenDEA Business Process Catalog. The block carries the catalog reference for the process (`processes:process-*`), or an explicit gap declaration where no canonical entry exists, together with the catalog version the reference was resolved against. The association is by reference and never by copy; inventing a process identifier is prohibited. The substrate-side rules are CG-PA-1 to CG-PA-6 in `aop-context-graph`.

NM-INT-5: The process alignment block SHOULD bind each human baseline metric of the Assurance dimension to a canonical performance metric in the OpenDEA metrics catalog (`dea:metric-*`) where one exists. Where no canonical metric exists, the block MUST declare the gap explicitly, and the gap is lodged as a contribution to the metrics catalog through that catalog's own contribution process. An AOP MUST NOT invent a metric identifier.

## 3. Context

The information and environmental state relevant to execution.

NM-CTX-1: The Context dimension MUST enumerate the context elements the executor requires, each with a source and an access rule.

NM-CTX-2: The Context dimension MUST define the context snapshot semantics: what is captured, at what point in the run, and how it is referenced. The snapshot reference uses the `cg://` scheme defined in the identifier scheme.

NM-CTX-3: The Context dimension MUST state the data minimisation rule: the context available to the agent is scoped to what the case and its authority level require. Context engineering doubles as data minimisation.

NM-CTX-5: Every context element MUST declare a trust class: `system-attested` (produced by a system of record), `derived` (deterministically computed from attested facts), `model-asserted` (produced by the executor or another model), or `untrusted-content` (originating outside the estate's control, such as message content). The trust class is the fact's provenance class for enforcement purposes.

NM-CTX-4: The Context dimension MUST NOT admit capture of personal content classes that the observation posture excludes, such as message body content and keystrokes. The work is modelled, not the person.

## 4. Constraints

Policies, rules, boundaries and prohibited actions.

NM-CON-1: The Constraints dimension MUST enumerate the permitted action set as explicit identifiers. An action not in the permitted set is prohibited by default.

NM-CON-2: The Constraints dimension MUST enumerate prohibited actions explicitly where the domain names them, in addition to the default prohibition.

NM-CON-3: The Constraints dimension MUST state the fail-closed rule as a property of execution: on an unknown condition, unmatched variant or unavailable check, execution does not proceed. Uncertainty routes to a person, never to a guess.

NM-CON-4: Every constraint MUST be stated so that a check outside the model context can evaluate it mechanically. A constraint that requires the executor's own judgement to apply is not a constraint; it is a request.

## 5. Authority

Which decisions the agent may take alone, and which require approval.

NM-AUT-1: The Authority dimension MUST express authority as decision rules of the form: condition, consequence, authority class. The rule shape is defined in the procedure structure document.

NM-AUT-2: The Authority dimension MUST classify every decision rule into exactly one authority class:

| Class | Meaning |
|---|---|
| `autonomous` | The agent executes without a human in the loop, within the permitted set and thresholds. |
| `approval-required` | The agent prepares the action and requests human approval with an evidence bundle before dispatch. |
| `prohibited` | The agent does not propose, prepare or execute the action. |

NM-AUT-3: Authority coverage is closed by default. An action class not covered by a decision rule takes the default authority class declared in the Authority dimension; where no default is declared, it is treated as `prohibited`.

NM-AUT-4: The agent MUST NOT have the ability to change its own authority class at run time. The authority class is evaluated by a component outside the model context (SEC-1).

NM-AUT-5: The Authority dimension MUST state the decision-rights ladder position of the AOP as a whole, assessed over the five risk axes:

| Axis | Question |
|---|---|
| Risk | What is the worst credible harm of a wrong decision? |
| Reversibility | Can the decision be undone, and at what cost? |
| Operational impact | How many cases, systems and people does the decision touch? |
| Authority threshold | Above what value, count or class must a human decide? |
| Assurance requirement | What evidence must exist after execution to establish correctness? |

NM-AUT-8: Every action in the permitted set carries a reversibility class: `reversible` (undoable at run time by the same authority), `compensable` (undoable only through a declared compensation path), or `irreversible` (no undo). An `irreversible` action MUST carry the authority class `approval-required` or a stricter restriction; it MUST NOT be `autonomous`. A `compensable` action MUST declare its compensation path. Reversibility classes are declared in the Authority dimension and enforced at run time.

NM-AUT-10: Ratification requires a human-reviewed corpus: rules derived from agent-originated cases, or from corpora whose origin mix is not declared, cannot be ratified. A recompile cannot ratify itself; ratification is a human act on a corpus whose provenance the ratifier has reviewed (NM-AUT-7, NM-CTL-6).

NM-AUT-9: Delegated authority attenuates: a run, agent or sub-agent acting under delegated authority holds no more authority than the delegating AOP grants, and each delegation link in a chain can only narrow it. The Coordination dimension declares delegation links where they exist.

NM-AUT-7: A decision rule carries a status: `observed` (mined, unreviewed), `reviewed` (human-reviewed against the corpus), or `ratified` (ratified by the owner in the governance manifest). Only ratified rules MAY carry the authority classes `autonomous` or `approval-required`. Rules classified `prohibited` need no ratification. Ratification is a human act recorded in the manifest; a recompile cannot ratify itself.

NM-AUT-6: The higher the position of a decision on any risk axis, the higher the minimum authority class it may carry. An AOP MUST NOT classify a decision as `autonomous` where its risk axis values demand `approval-required`. The mapping from axis values to the minimum class is declared in the AOP and validated by the conformance clauses.

## 6. Capabilities

The skills, tools and operational capabilities available.

NM-CAP-1: The Capabilities dimension MUST enumerate the Agent Skills and tools the executor may invoke, by identifier, each resolved through the identifier scheme.

NM-CAP-2: A capability enumerated in the AOP MUST carry the contract declared in the Agent Skill contract annex. A capability that does not declare what it does, what it needs, what it must not do, and how it reports MUST NOT be invoked by a conforming AOP.

NM-CAP-3: A skill carries no authority of its own. Invocation of a skill does not extend the authority granted by the Authority dimension.

NM-CAP-4: The Capabilities dimension MUST state the credential requirement per capability, and each action executes under short-lived credentials scoped to that action class (SEC-3).

## 7. Coordination

How agents, humans and external systems interact.

NM-CRD-1: The Coordination dimension MUST state, for every handoff, who hands off to whom, with what payload, and under what acknowledgement.

NM-CRD-2: The Coordination dimension MUST define the escalation route for each authority class: the target role, the evidence bundle contents, and the expected decision. The evidence bundle contents are fixed by the schema.

NM-CRD-4: The Coordination dimension MAY declare aggregate limits per action class: a maximum count per case, a rate limit, or a blast-radius cap. Where declared, they are enforced at the guardrail beside the authority check (RA-15 in the run and action semantics); exceeding a limit escalates, it never silently proceeds. Where an estate declares none, the conformance record states it.

NM-CRD-3: The Coordination dimension MUST state the interaction contract with external systems: which systems, which operations, and which failure modes route back into the exception edges.

## 8. Control

Monitoring, validation, intervention and exception handling.

NM-CTL-1: The Control dimension MUST state the run-time validation obligations: what is checked after execution, against what expectation, and what happens on a failed check.

NM-CTL-2: The Control dimension MUST bind every exception edge declared in the procedure structure to a handling behaviour: a validated path, a recovery strategy, or an escalation.

NM-CTL-3: The Control dimension MUST state the intervention semantics: how a run is paused, superseded or terminated, and by whom.

NM-CTL-6: Every case carries its origin: `human`, `agent`, or `mixed`. Origin feeds the loop-hygiene obligations: agent-originated cases are excluded from baseline mining by default, a protected human-baseline reservoir is maintained for drift detection, and the origin mix of the corpus is reported with every evaluation claim.

NM-CTL-5: Every side-effecting action MUST carry the action contract of the run and action semantics: a retry class (idempotent, reconciling, manual), partial-success behaviour, and the concurrency safeguard for any shared resource it touches (RA-8 to RA-13).

NM-CTL-4: The Control dimension MUST state the drift obligation: which observed changes in the work trigger reassessment of the AOP, and how the AOP is recalibrated. Execution feeds observation; the loop closes.

## 9. Assurance

The evidence required to establish that execution was correct and that outcomes were achieved.

NM-ASR-1: The Assurance dimension MUST require an append-only, tamper-evident case record per run, containing at minimum: inputs, context snapshot, rule applied, provenance, decision, approver where relevant, and outcome.

NM-ASR-2: The Assurance dimension MUST state the human baseline against which agent performance is compared: the observed human values for the domain metrics, such as cycle time and first-pass resolution.

NM-ASR-3: The Assurance dimension MUST state the replay obligation: every decision in the case record is replayable from the recorded inputs alone.

NM-ASR-5: The case record MUST support the replay levels of the evidence and replay semantics: record verification (R1) always, decision-trace reconstruction (R2) from the record alone, and controlled re-execution (R3) only with its own authorization. Reconstruction never authorises re-execution.

NM-ASR-4: The Assurance dimension MUST NOT permit execution evidence to modify the AOP version that produced it. Recalibration is a new version with its own provenance and its own approval.

## 9a. Accountability

NM-GOV-1: Every AOP document MUST name its accountable owner in the governance block. The accountable owner is the role answerable for the AOP's authority decisions, and the only role that may authorise resumption after an emergency stop (SEC-15). Where the document also names who prepared and who ratified it, the ratifier MUST NOT be the preparer (CC-23).

## 10. What the normative model does not do

The normative model does not fix the layering of the system, the trust boundaries, or the deployment topologies. That is `aop-architecture`. It does not fix how variants are mined or rules are extracted. That is `aop-toolkit`. It binds the shape of the specification and the semantics each part of it carries.
