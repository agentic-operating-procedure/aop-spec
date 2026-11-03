# AOP Conformance Clauses for AOP Documents (Specification Scope)

Normative. These clauses state what a conformant AOP document must satisfy. The test fixtures and the certification process that operationalise them are owned by `aop-conformance`. Clause identifiers here are the normative references those profiles cite.

## 1. Completeness

CC-1: The document populates all eight dimensions with non-empty, schema-valid content (NM-MODEL-1 to NM-MODEL-3).

CC-2: Every context element declared in the Context dimension carries a source and an access rule (NM-CTX-1).

CC-3: The permitted action set is explicit, and every action referenced anywhere in the document is either in the permitted set or explicitly prohibited (NM-CON-1, NM-CON-2).

## 2. Decision specificity

CC-4: Every decision rule has a machine-evaluable condition, a stated consequence, and exactly one authority class (NM-STR-4, NM-AUT-2).

CC-5: Every threshold in a decision rule is a value, not a prose adjective (NM-STR-5).

CC-6: Every decision rule carries observed provenance: the case count and path frequency at minimum (NM-PRV-3).

## 3. Authority coverage

CC-7: The union of decision rules, plus the declared default authority class, covers every action in the permitted set. Actions outside that union are prohibited by default and are treated as such (NM-AUT-3).

CC-8: No decision rule classified `autonomous` contradicts the minimum authority class derived from the declared risk-axis assessment (NM-AUT-6).

CC-9: No construct in the document grants the agent the ability to alter its own authority at run time (NM-AUT-4, SEC-1, SEC-2).

## 4. Structure

CC-10: The procedure structure is declared as variants with frequency, trigger, steps and provenance; variant frequencies sum to at most 1.0 (NM-STR-1 to NM-STR-3).

CC-11: Every exception edge declares its raising condition, handling behaviour and target role where the behaviour is an escalation (NM-STR-6).

CC-12: Every rework loop declares its return condition, iteration bound, and bound-exceeded behaviour (NM-STR-7).

## 5. Provenance and versioning

CC-13: The document carries a provenance block with source, observed case count, variant count and last recalibration (NM-PRV-1).

CC-14: The identifier and version follow the identifier scheme, and lifecycle status is carried on the three separate status dimensions (NM-ID-1 to NM-ID-4, NM-VER-4).

CC-15: Where the AOP was compiled from a source SOP, the SOP identifier and version are recorded and the intent hypothesis is recoverable (NM-PRV-2, NM-INT-3).

## 6. Capabilities and security

CC-16: Every capability invoked carries a complete Agent Skill declaration per the contract annex (SK-2), and no skill carries authority (SK-3).

CC-17: The document states the credential requirement per capability, and no credential scope exceeds the action class it is declared for (NM-CAP-4, SEC-3).

CC-18: The document states the fail-closed rule and does not construct any execution path that proceeds on an unknown condition without escalation (NM-CON-3, SEC-5).

## 7. Assurance

CC-19: The document requires an append-only case record with the mandatory fields, a stated human baseline, and the replay obligation (NM-ASR-1 to NM-ASR-3).

CC-20: No construct in the document permits execution evidence to modify the producing AOP version (NM-ASR-4).

## 8. What conformance does not mean

A conformant document is not a certified one until it passes the conformance profile administered by `aop-conformance`, and conformance does not establish that the AOP works. That claim is Demonstrated-level authority, established by `aop-evaluation` and `aop-examples`, not by this specification.
