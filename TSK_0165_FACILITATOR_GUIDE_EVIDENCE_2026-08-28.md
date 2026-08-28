# TSK-0165 — Facilitator Guide and Intervention Taxonomy Evidence

**Task:** TSK-0165  
**Acceptance:** ACC-0165  
**Evidence date:** 2026-08-28  
**Result:** PASS

## Authority and predecessor proof

The canonical WBS defines TSK-0165 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessors `TSK-0166; TSK-0228`. ACC-0165 requires the guide to preserve the hypothesis, record intervention duration/reason, distinguish safety correction from usability help, and prevent silent facilitator completion.

Both hard predecessors were confirmed as current runtime PASS from `CURRENT_STATE.md`, not merely planning labels:

- `TSK-0166` — accepted participant record/metric schema, artifact blob `c7706fceced87c797b8cd92179198754e2b08ffe`.
- `TSK-0228` — accepted child-safety escalation boundary, artifact blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`.

## Accepted artifact

`EXPERIMENT_01_FACILITATOR_GUIDE.md`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`.

The guide is aligned to current `EXPERIMENT_01_CONCIERGE_VALIDATION.md`, blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`, and the accepted participant schema.

ACC-0165 mapping:

1. **Hypothesis preserved:** the guide reproduces the frozen Experiment-1 hypothesis and prohibits changing the hypothesis, activation definition, or thresholds during a wave except for an immediate safety/privacy stop.
2. **Duration and reason recorded:** every intervention is timed/classified and the mandatory record includes observed block/reason, start/end markers, active assistance minutes, action, outcome, and whether the facilitator performed the user's action.
3. **Safety correction distinguished from usability help:** taxonomy codes separate wording/navigation/technical/compatibility assistance from `S1` safety/privacy correction and `G1` safeguarding escalation; the guide explicitly states the analytical consequences of each class.
4. **No silent facilitator completion:** the parent performs the real actions; facilitator takeover is explicitly recorded as substantial assistance and cannot be counted as silent self-service success. Off-camera/behind-the-scenes completion recorded as parent success is expressly prohibited.

The guide also retains the accepted privacy boundary by excluding child browsing/domain history, child name, exact DOB, messages, contacts, photos, location, and unnecessary identifiers from intervention records.

## Independent verification

GitHub Actions run `33153850640`, job `98791885998`, completed successfully on the repository-scoped `adguardvm` runner using an exact `main` checkout, `contents: read`, and no persisted checkout credentials.

Audit output:

- `TSK_0166_RUNTIME_PREDECESSOR=PASS`
- `TSK_0228_RUNTIME_PREDECESSOR=PASS`
- `TSK_0165_PROTOCOL_ALIGNMENT=PASS`
- `TSK_0165_SCHEMA_ALIGNMENT=PASS`
- `TSK_0165_ACCEPTANCE_CLASSES=4/4`
- `TSK_0165_ARTIFACT_BLOB=7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`
- `TSK_0165_INDEPENDENT_AUDIT=PASS`

## Boundary

This PASS verifies a pre-experiment facilitator protocol artifact only. It does not authorise recruitment, participant processing, live facilitation, child-linked DNS activation, or passage of the validation-readiness/legal/provider gates.
