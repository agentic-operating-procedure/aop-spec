# AOP Normative Security Clauses (Specification Scope)

Normative. This document states the security clauses that bind every conformant AOP, harness and runtime. The threat model that motivates these clauses is owned by `aop-architecture`; the clauses here are the normative text implementations are built against.

## 1. The central rule

SEC-1: The authority check runs outside the model context. The AOP and its guardrail act as a policy decision point and a policy enforcement point that sit outside the context of the executing agent. The agent can propose actions; it cannot decide whether they are permitted. The agent MUST NOT be able to influence the outcome of the check that governs it.

SEC-2: An agent MUST NOT be able to self-authorise. There is no prompt, context, tool result, or agent-composed argument that grants authority. Authority is granted by the AOP version the run references, evaluated outside the agent.

SEC-3: Every action executes under short-lived credentials scoped to that action class. A credential scoped to one action class MUST NOT authorize another. High-risk actions receive credentials only after a human approval, and the credential is issued after the approval, not before.

SEC-4: The context snapshot available to the agent is scoped to what the case and its authority level require. Context provisioning follows data minimisation; a wider context is not a standing entitlement.

## 2. Fail-closed behaviour

SEC-5: Enforcement fails closed. On an unmatched variant, an unknown condition, an unavailable authority check, or an error in the enforcement path itself, execution does not proceed and the case escalates. Uncertainty routes to a person, never to a guess.

SEC-6: A permitted action within authority executes. A known pattern beyond authority requests approval with an evidence bundle. An unknown condition escalates. There is no fourth path that proceeds without a record.

SEC-7: The failure of an enforcement component MUST NOT widen the agent's effective authority. Degraded enforcement means degraded operation, not degraded governance.

## 3. Evidence integrity

SEC-8: The case record is append-only and tamper-evident. Records are not editable or deletable by the agent, the harness operator, or the AOP author.

SEC-9: The evidence bundle presented for approval carries, at minimum: the proposed action, the triggering rule, that rule's observed provenance, the baseline comparison, and the case context. The approver rules on a case, not on a mystery.

SEC-10: Every decision is replayable from the case record alone. Replay is part of the assurance obligation, not an optional capability.

## 4. The specification surface

SEC-11: The harness is the top-level AOP for its domain. Its boundary conditions (what the agent may do, which tools it may call, which credentials it may hold, how it escalates, how work is verified) are documented as an AOP with the same rigour and the same conformance obligations as any other AOP. A harness that has not been specified as an AOP is a runtime, not a harness.

SEC-12: These clauses bind regardless of executor type. They apply equally to a model-driven agent and a deterministic rules-based executor operating under an AOP.

SEC-13: A conformant implementation MUST satisfy every clause in this document. Conformance is tested by the harness profile owned by `aop-conformance`.
