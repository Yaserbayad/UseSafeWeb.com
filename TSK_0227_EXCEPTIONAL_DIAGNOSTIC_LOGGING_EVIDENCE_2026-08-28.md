# TSK-0227 — Exceptional Diagnostic Logging Procedure Evidence

**Task:** TSK-0227  
**Acceptance:** ACC-0227  
**Evidence date:** 2026-08-28  
**Result:** PASS

## Authority and dependency proof

The exact canonical WBS row defines TSK-0227 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0224`. ACC-0227 requires a runbook containing an incident/ticket ID, necessity, exact fields, approver, start/end, access, user notice where applicable, and deletion verification.

The predecessor planning label was not accepted by itself. Current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly re-proves the Experiment-1 retention baseline: identifiable DNS/domain history is not retained; contact data has the current follow-up deletion bound; participant-level metrics have the current post-close deletion bound; and only aggregate/anonymised findings may persist in GitHub.

## Accepted artifact

`EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md`, blob `f9e1bb52582a69bc385aa69c93d02febb7b5cffa`.

ACC-0227 mapping:

1. **Incident/ticket identity:** a unique non-personal incident/ticket ID is mandatory before collection.
2. **Necessity:** lower-data checks must be exhausted/documented and necessity for temporary diagnostic data must be explicit.
3. **Field and scope minimisation:** exact collected fields are allowlisted; scope is restricted to the smallest affected client/device/test cohort; synthetic and aggregate methods are preferred first.
4. **Approval and access:** an approver and explicit authorised-access list are required before activation.
5. **Bounded time:** UTC start and end are selected before collection, the collection stops no later than the approved end time, and extension requires a new approval record.
6. **User notice:** applicability is decided and the notice/reference or reason for non-applicability is recorded.
7. **Baseline restoration:** exceptional collection must be disabled and the privacy-minimal baseline restored and verified at resolution/end time.
8. **Deletion:** temporary diagnostic data and copies/exports must be deleted; indefinite logging and reuse for analytics/profiling/marketing are prohibited.
9. **Deletion verification:** deletion owner, method, time, verifier, locations checked, and PASS/FAIL are recorded; a deletion-verification failure escalates rather than closing silently.

## Independent verification

GitHub Actions run `33153403025`, job `98790453195`, completed successfully on the repository-scoped `adguardvm` runner using an exact `main` checkout, `contents: read`, and no persisted checkout credentials.

Audit output:

- `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`
- `TSK_0227_ACCEPTANCE_CLASSES=9/9`
- `TSK_0227_ARTIFACT_BLOB=f9e1bb52582a69bc385aa69c93d02febb7b5cffa`
- `TSK_0227_INDEPENDENT_AUDIT=PASS`

## Boundary

This PASS verifies the pre-experiment exceptional-diagnostic procedure only. No exceptional logging was enabled, no participant data was collected, and no validation-readiness, recruitment, provider, or legal gate was changed.
