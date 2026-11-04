# AOP Evidence and Replay Semantics: Replay Levels and Reproducibility Boundaries (Specification Scope)

Normative. This document states what "replayable" means. NM-ASR-3 requires every decision to be replayable from the case record alone; for nondeterministic executors and changing external systems, replay is a family of guarantees, and conflating them implies reissuing side effects from a record. Clause identifiers: RP-n.

## 1. The replay levels

RP-1: The standard distinguishes three levels, and every replay claim states its level:

| Level | Name | Guarantee |
|---|---|---|
| R1 | Record verification | The record is intact: the chain verifies, the mandatory fields are present, the content digests match |
| R2 | Decision-trace reconstruction | The decision can be re-derived and explained from the recorded inputs: given the context snapshot reference, the bound AOP version, and the rule, the authority decision is reconstructible and checkable |
| R3 | Controlled re-execution | The recorded actions are re-executed in a non-actuating or sandboxed mode for testing or investigation, never to re-produce live side effects |

RP-2: Reconstruction (R2) NEVER authorises re-execution (R3). Reaching R3 requires its own authorization decision, taken under the AOP's authority model as any action is; a record is not an authorization.

RP-3: R2 MUST be achievable from the case record alone, without trusting the harness or agent that produced it. This is the minimum bar for the replay obligation in NM-ASR-3.

## 2. The minimum provenance per level

RP-4: An R2-capable record carries, at minimum: the AOP identifier and version digest, the decision-rule identifier and its condition as evaluated, the context snapshot reference (`cg://`), the action digest (RA-5), the parameter payload (or its digest plus a reference under the retention profile), the authority decision and its class, the approver where relevant, and the outcome disposition.

RP-5: Where a claim needs more than R2, the record states so and names what is missing: executor and model identifiers, prompt or template versions, external response identifiers. A record MUST NOT claim a level it cannot support. After erasure (CR-026), the record states which claims survive and which are withdrawn.

## 3. Verification and third parties

RP-6: Chain verification covers ordering, truncation and deletion: a gap in sequence numbers or a broken hash link is a detected failure, not a shorter history (SEC-8). External anchoring (ARC-TB2) is the deployment obligation that makes wholesale replacement detectable.

RP-7: Verification of a supplied record MUST NOT require trust in the producing agent: the verifier needs the record, the schema, the bound AOP version's rule set, and the digest recomputation. The conformance suite exercises this with an independent verifier path (HAR-12).

## 4. What this document does not fix

The storage of records, the retention periods, and the erasure mechanics are owned by the substrate posture (CG-O6) and CR-026. The sandbox definition for R3 is a deployment profile obligation; the standard requires that it be non-actuating or sandboxed and separately authorized, not what the sandbox looks like.
