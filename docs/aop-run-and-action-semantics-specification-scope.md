# AOP Run and Action Semantics: The Run State Machine and the Side-Effecting Action Contract (Specification Scope)

Normative. This document states the run state machine and the contract every side-effecting action carries. It binds implementations where NM-STR-13 states the sequence and leaves behaviour undefined: timeouts, retries, duplicate delivery, concurrency, partial success, compensation and cancellation. RFC 2119 key words apply. Clause identifiers: RA-n.

## 1. The run state machine

RA-1: A run is a state machine with the states: `created`, `matching`, `authorising`, `executing`, `verifying`, `escalated`, `held`, `recovering`, and the terminal states `completed`, `failed`, `cancelled`, `inconclusive`. The record of a run MUST allow a third party to determine which states it entered and in what order.

RA-2: The terminal dispositions are the closed set from NM-STR-14. A run that ends outside them is recorded as `inconclusive`.

RA-3: `held` is a non-terminal state with a cause (enforcement unavailable, emergency stop, budget hold, reconciliation pending) and an owner of the resumption decision (SEC-14, SEC-15). A held run MUST NOT execute; its release path is recorded.

RA-4: Cancellation is a first-class transition from any non-terminal state, recorded with the cancelling role. A cancelled run is not a failed run; its record states how far it proceeded.

## 2. Action identity and the authorization binding

RA-5: Every proposed action carries a canonical form and an action digest: the digest of the canonical serialisation of action name, target, and full parameter payload, computed at proposal time and recomputed at enforcement time.

RA-6: The authority decision is bound to the action digest and the context snapshot reference. A changed digest after authorisation invalidates the decision: the action re-enters authorisation or escalates. Stale authorisation MUST NOT silently authorise a changed action.

RA-7: The credential issued for the action is scoped to the digest (extending SEC-3): a credential authorising one digest does not authorise a re-serialisation with different parameters, even within the same action class.

## 3. Idempotency, retries and duplicate delivery

RA-8: Every side-effecting action declares a retry class: `idempotent` (safe to re-issue; the same digest submitted twice produces the same external state), `reconciling` (a retry requires checking the external system's state first and reconciling), or `manual` (a retry is a human decision).

RA-9: On timeout or transport failure, the runtime's behaviour follows the retry class. It MUST NOT blindly re-issue a `reconciling` or `manual` action. The uncertainty (completed or not) is recorded, and reconciliation or escalation follows.

RA-10: Duplicate delivery is answered by the action digest: a digest already executed within the run returns the recorded outcome and appends no second external effect. A replayed authorisation for an executed digest is answered from the record, not by re-execution.

## 4. Concurrency and partial success

RA-11: Concurrent runs that may touch a shared resource MUST declare the safeguard per resource class: locking, conflict detection, or serialisation. The AOP's Coordination dimension names the shared resources; the harness enforces the declared safeguard.

RA-12: An action that can partially succeed declares so. Partial success routes to the declared behaviour: compensation, reconciliation, or escalation. A partially completed side effect is never recorded as plain success.

RA-13: A compensable action declares its compensation path. Compensation executions are governed actions: they carry their own authority decision, their own record entries, and their own provenance. Where rollback is impossible, the AOP states the residual handling (accept, escalate, or human decision), and the failure to compensate is recorded.

## 4a. The approval object

RA-15: An approval is an object, not an event: it binds the approver's decision to the action digest (RA-5), the context snapshot reference, the triggering rule, the bound AOP version, the target, and an expiry. An approval that has expired, been revoked, or whose bound digest no longer matches the action presented at execution time is invalid; the action re-enters authorisation. There is no approval without a digest.

RA-16: The approver interface carries four outcomes: approve, reject, request changes, defer. Non-response is none of them: it never approves, and it triggers the declared escalation SLA behaviour (routing to a fallback role with the bundle, recorded). An implementation MUST NOT translate silence into approval.

RA-17: Approver eligibility is declared per authority class: who may approve, that the approver is not the requester and not the author of the triggering rule, and how delegation of the approval right works. Approval rights attenuate like any delegated authority (NM-AUT-9).

RA-18: The approval is re-checked at credential issuance and at execution time against its expiry, its revocation state and its digest binding.

RA-19: Oversight quality is measured, not assumed: the harness emits the oversight metrics (approval rate, time-to-approve, override rate), runs injected test escalations (canary bundles whose correct ruling is rejection) and raises a failing-approver alert when an approver approves canaries or rules faster than the declared floor.

## 4b. Parameter-level constraints

RA-20: Every side-effecting action MAY declare a typed parameter schema: required and optional fields with types, bounds, allowed values, units, target scope, prohibited values, and explicit defaults. Defaults are declared, never implicitly supplied by the executor, an adapter, or the downstream tool without appearing in the authorised payload.

RA-21: The enforcement point validates the canonical payload against the declared schema immediately before execution, after all adapter transformations. The authority decision and the approval are bound to the payload digest of the validated canonical form (RA-6).

RA-22: Unknown fields, ambiguous units, type coercions, out-of-range values and invalid targets fail closed or escalate per the risk profile. Where an action declares no parameter schema, the conformance record states it; absence is a declared gap, not an unexamined freedom.

## 5. Degraded modes

RA-14: The failure of a runtime component MUST NOT widen authority (SEC-7). The permitted degraded behaviours are enumerated: hold (SEC-14), continue with read-only diagnostics only, or terminate. Any other degraded behaviour is nonconformant.

## 6. What this contract does not fix

Timeout values, retry counts and backoff are deployment configuration, declared per profile, not per clause. The external systems' exactly-once guarantees are their own; this contract defines what the harness does in a world that cannot provide them.
