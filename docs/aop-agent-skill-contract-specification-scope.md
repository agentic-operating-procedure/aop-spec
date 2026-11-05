# AOP Agent Skill Contract (Normative Annex, Specification Scope)

Normative. This annex is the contract an Agent Skill declaration MUST satisfy to be invocable by a conforming AOP. The annex lives in `aop-spec` by decision D-003.

## 1. What a skill is

A skill is the reusable capability level of the six-level hierarchy. It is atomic, well-scoped, tool-agnostic, composable and independently testable. A skill is not an operating procedure: it provides a capability, it does not state operational intent, and it carries no authority of its own (NM-CAP-3).

## 2. The declaration

SK-1: A skill MUST declare, as machine-readable metadata:

| Field | Requirement |
|---|---|
| `id` | Skill identifier per the identifier scheme (`SK-` form) |
| `name` | Human-readable name |
| `purpose` | One sentence stating what the skill does |
| `inputs` | The declared inputs, each with a type and whether it is required |
| `outputs` | The declared outputs, each with a type |
| `requires` | Credentials, access or context elements the skill needs, per class |
| `must_not` | What the skill MUST NOT do, stated as explicit prohibitions |
| `reporting` | How the skill reports: the events or records it emits |
| `test` | The reference to the independent test that establishes the skill works |

SK-2: A skill declaration that omits any required field is not invocable by a conforming AOP. The omission is a validation failure, not a warning.

## 3. The boundaries

SK-3: A skill MUST NOT carry authority. It MUST NOT contain decision rules with an authority class, MUST NOT grant or widen credentials, and MUST NOT route work to itself outside an AOP's Authority dimension.

SK-4: A skill MUST be tool-agnostic in its declaration: it declares what it needs and does, not which vendor product performs it. A declaration bound to a named vendor product is not conformant.

SK-5: A skill MUST be independently testable: its `test` reference resolves to a test executable without the AOP, the harness, or the agent present.

SK-6: A skill MUST be composable: invoking it MUST NOT depend on hidden state from a prior invocation beyond its declared inputs.

SK-7: A skill MUST be atomic: it does one thing at the scope its `purpose` states. A declaration whose purpose requires "and" between two independent outcomes is not atomic.

## 3a. Supply-chain lineage

SK-12: A skill declaration identifies its maintainer or source, its behaviour-affecting dependencies, and its own immutable version. A skill update is a new version; when an update changes tool access, data access or the behaviour contract, it triggers policy and conformance review before an AOP may invoke it. A skill does not acquire authority through tool access (SK-3 governs at all times).

## 4. Invocation semantics

SK-8: A skill is invoked only by an executor acting under an AOP whose Capabilities dimension enumerates it (NM-CAP-1).

SK-9: On invocation, the executor passes the declared inputs and no more. Context beyond the declared inputs is not passed unless the AOP's Context dimension admits it (NM-CTX-3).

SK-10: The skill reports through its declared `reporting` channel. Reports are evidence and land in the case record; they are not advisory.

SK-11: On failure, a skill returns a failure report through the same channel. It MUST NOT retry outside the AOP's Control dimension, and it MUST NOT escalate on its own; escalation belongs to the AOP's exception edges.

## 5. Relationship to the hierarchy

A skill is invoked by an AOP. An AOP is executed inside a Domain Agent Harness. The harness is the top-level AOP for its domain and governs the skills reachable inside it. The distinction Business Capability is not Agent Skill is not AOP holds: a business capability is an organisational concern, a skill is a reusable unit of execution capability, and an AOP is the operational specification that governs when and under what authority skills are invoked.
