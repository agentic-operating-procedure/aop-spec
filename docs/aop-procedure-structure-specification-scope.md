# AOP Procedure Structure: Variants, Decision Points, Exception Edges, Rework Loops, Runtime Binding (Specification Scope)

Normative. This document states the network-native procedure structure of an AOP. An AOP is not a linear document. The linear corridor is a special case that happens to have one variant and no exception edges, and it is precisely the case this structure was built to escape.

## 1. The structure

NM-STR-1: An AOP document MUST declare its procedure structure as a set of variants. Each variant is an observed path through the work.

NM-STR-2: Each variant MUST carry:

| Field | Meaning |
|---|---|
| `id` | Variant identifier, unique within the AOP |
| `name` | Human-readable name |
| `frequency` | Observed relative frequency across compiled cases, in `[0, 1]` |
| `trigger` | The condition under which this variant is the matched path |
| `steps` | The ordered steps of the path |
| `decision_rules` | The decision rules evaluated on this path |
| `provenance` | The observed cases this variant was compiled from |

NM-STR-3: The sum of variant frequencies MUST be at most 1.0. Variants do not double-count cases.

NM-STR-4: A decision rule MUST have the shape:

```
if:      <condition over context elements, machine-evaluable>
then:    <consequence: an action, a route, or an escalation>
authority: autonomous | approval-required | prohibited
```

NM-STR-5: Every threshold that appears in a decision rule condition MUST be stated as a value, not as a prose adjective. Where the SOP said a word such as "severe", the AOP states the threshold at which humans actually escalate, with its observed provenance.

NM-STR-6: An exception edge MUST declare the condition that raises it, the handling behaviour (execute per validated path, recover, or escalate), and the target role where the behaviour is an escalation. The exception class, severity and recoverability are declared per the exception model.

NM-STR-7: A rework loop MUST declare the condition that returns the work to a prior step, the bound on iterations, and the behaviour on exceeding the bound. An unbounded loop is not a rework loop; it is a defect.

## 2. Matching and failure semantics

NM-STR-8: At run time the executor MUST match the context snapshot to a variant before acting. Matching selects an observed path, not a happy path.

NM-STR-9: On no matching variant, execution MUST fail closed: no action is taken, the case is escalated, and the miss is recorded as an observation that feeds the next compile.

NM-STR-10: A variant whose steps deviate from the AOP's own constraints MUST NOT be matched. A path observed in the work is not thereby authorised; the governance bounds attach at compile time and bind at run time.

## 3. Runtime binding

NM-STR-11: A run MUST reference exactly one immutable AOP version. The version is resolved before the run starts and does not change during the run.

NM-STR-12: Every action taken under a matched variant MUST be attributable, in the case record, to the variant, the decision rule, and the provenance of that rule.

NM-STR-13: The runtime sequence for a matched variant is: snapshot the case context, match the variant, check authority for the proposed action, execute or escalate, record, emit. The emit returns execution evidence to the substrate as new observation.

NM-STR-14: The run outcome MUST be recorded using the outcome dispositions: `achieved`, `partially_achieved`, `not_achieved`, `accepted_with_deviation`, `inconclusive`. An outcome that does not fit a disposition is recorded as `inconclusive` and escalates.

## 4. The special case of linearity

NM-STR-15: An AOP with exactly one variant at frequency 1.0 and no exception edges is conformant. It is the degenerate case, and the provenance MUST show it was measured, not assumed. A documented path asserted without observed coverage does not satisfy NM-STR-2.

## 5. What this structure does not fix

The structure does not fix the graph substrate the variants are mined from, the entity model of observed work, or the mining method. The Context Graph of Work and its entity model are owned by `aop-context-graph`; the miners and the compiler by `aop-toolkit`. This specification binds what a compiled AOP must look like and how it binds to a run.
