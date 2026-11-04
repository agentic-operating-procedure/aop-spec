# AOP Identifiers and Versioning: Identifier Scheme, Versioning, Provenance and Lineage (Specification Scope)

Normative. This document states the identifier scheme for AOP artefacts and the versioning and provenance model. A published AOP that cannot be traced to the observations it was compiled from is not conformant.

## 1. Identifier scheme

NM-ID-1: Every governed artefact class carries an identifier of the form:

```
<domain>/<artefact-id>@v<major>.<minor>.<patch>
```

NM-ID-2: The artefact classes and their identifier prefixes are:

| Class | Prefix pattern | Example |
|---|---|---|
| AOP document | `AP-` followed by uppercase alphanumeric | `fault-management/AP-LINE-001@v0.47.0` |
| Agent Skill | `SK-` followed by uppercase alphanumeric | `fault-management/SK-CORRELATE-ALARMS@v1.3.0` |
| Domain Agent Harness | `HR-` followed by uppercase alphanumeric | `fault-management/HR-LINE-001@v2.1.0` |
| AOP Release | the AOP identifier plus a release tag | `fault-management/AP-LINE-001@v0.47.0+r2` |

NM-ID-3: The domain segment is the organisational or operational domain that owns the artefact. It MUST NOT name a vendor, a model or a tool.

NM-ID-4: Identifiers are immutable. A change to the content of an artefact produces a new version, never an edit in place.

NM-ID-5: Context snapshots are referenced by the `cg://` scheme:

```
cg://case/<case-id>@<timestamp>
```

The reference resolves in the Context Graph of Work and pins the exact observed state the decision was made against.

## 2. Versioning model

NM-VER-1: An AOP version is semantic: the major version changes when the meaning of a dimension, the authority model, or the permitted set changes; the minor version when the procedure structure changes (variants, rules, thresholds, exception edges); the patch version for corrections that do not change meaning or structure.

NM-VER-2: A normative change to an AOP produces a new AOP version. Runtime evidence MUST NOT directly modify an approved version (NM-ASR-4).

NM-VER-3: A run references exactly one AOP version (NM-STR-11). The harness MUST record that version in the case record.

NM-VER-4: Lifecycle status is carried on three separate dimensions, and MUST NOT be collapsed into one status field:

| Dimension | Values |
|---|---|
| Specification status | `draft`, `under-review`, `under-assessment`, `approved`, `rejected`, `withdrawn` |
| Release status | `not-released`, `released`, `withdrawn-from-distribution` |
| Operational applicability | `not-effective`, `effective`, `restricted`, `suspended`, `superseded`, `retired` |

NM-VER-5: Approval, release and operational authorisation are distinct events. An approved AOP version is not automatically released; a released version is not automatically effective in an operational scope. Operational authorisation is granted per scope and can be restricted, suspended, reinstated, superseded or retired independently of approval.

## 2a. Revocation, rollback and compatibility

NM-VER-6: Suspension and revocation operate per scope and never mutate historical records (extending NM-VER-5). The registry resolves the revocation state of a ref, and a run MUST consult it before binding: a revoked version holds at the enforcement point, and an action already in flight follows its declared active-run behaviour per action class (stop, continue under pinned prior authorisation, or safe hold). Rollback selects a prior verified version with a recorded reason; it does not implicitly restore withdrawn credentials or obsolete policy. Compatibility rules for schema evolution and dependency resolution are declared by the registry profile; a historical case remains interpretable after a schema change through the version binding in its record.

## 3. Provenance and lineage

NM-PRV-1: A compiled AOP MUST carry a provenance block containing at minimum:

```
source:         <context-graph reference the compile was taken from>
derived_from:
  observed_cases:   <count of cases compiled from>
  variants:         <count of variants mined>
  last_recalibrated: <timestamp of the last recalibration>
```

NM-PRV-2: Where an AOP was compiled from a source SOP, the provenance MUST record the SOP identifier and version, and the Intent dimension carries the intent hypothesis the observation tested.

NM-PRV-3: Every decision rule MUST carry the provenance of the observations that yielded it: the case count and the path frequency at minimum. A rule without observed provenance is an assertion, and an AOP carrying one is not conformant (CC-6).

NM-PRV-4: A published AOP MUST be traceable, through its provenance chain, from the published version back to the observed cases it was compiled from. This is the obligation the registry publishes against.

NM-PRV-5: Governance events on an AOP version (approval, publication, operational authorisation, suspension, retirement) MUST reference the evidence records that support them, distinct from the runtime evidence of execution.

## 4. What this scheme does not fix

The scheme does not fix the registry that resolves identifiers, the storage of provenance chains, or the publication workflow. Those are owned by `aop-registry`. It binds the shape of identifiers, the meaning of versions, and the minimum provenance a conformant AOP carries.
