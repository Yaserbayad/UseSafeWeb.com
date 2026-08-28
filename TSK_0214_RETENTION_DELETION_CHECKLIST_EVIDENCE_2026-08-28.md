# TSK-0214 — Retention/Deletion Checklist Evidence

**Task:** TSK-0214  
**Acceptance:** ACC-0214  
**Evidence date:** 2026-08-28  
**Result:** PASS

## Authority and dependency proof

The exact canonical WBS row defines TSK-0214 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard dependencies `TSK-0224; TSK-0166`. ACC-0214 requires a checklist that identifies data locations, deletion dates, owner, verification method, aggregate output, and exception handling.

Historical/planning predecessor labels were not accepted by themselves.

- `TSK-0224` was directly re-proven from current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`: identifiable DNS/domain history is not retained; parent contact details are deleted promptly and no later than 30 days after the participant's follow-up; participant-level pseudonymous metrics are aggregated/anonymised and deleted no later than 90 days after Experiment 1 closes; aggregate/anonymised findings may remain in GitHub.
- Current accepted `TSK-0166` artifact `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md`, blob `c7706fceced87c797b8cd92179198754e2b08ffe`, directly proves that real participant records are not committed to GitHub and that operational identity/contact data remains outside the metric record.

## Accepted artifact

`RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`.

ACC-0214 mapping:

1. **Data locations:** the controlled register covers the participant/contact location, pseudonymous metric store, AdGuard/DNS service, exceptional diagnostic location, and GitHub canonical repository, with a fail-closed rule for any later real location.
2. **Deletion dates:** participant contact deletion is calculated from follow-up completion with a 30-day maximum; participant-level metric deletion is calculated from Experiment-1 close with a 90-day maximum; exceptional diagnostics use the approved end time.
3. **Owner:** each location has a responsible owner and each deletion evidence record carries the responsible owner and verifier.
4. **Verification:** each location has an explicit verification method, plus a structured deletion-evidence record with PASS/FAIL result.
5. **Aggregate output:** the register states which aggregate/anonymised outputs are allowed and explicitly restricts GitHub to aggregate/anonymised findings and non-sensitive evidence.
6. **Exception handling:** only concrete legal/security/provider/technical conditions can defer deletion; the exception must identify authority/reason, restrict access/secondary use, set a deterministic replacement date/condition, assign an owner, verify eventual deletion, and escalate unresolved/high-risk deviations.

## Independent verification

GitHub Actions run `33152847430`, job `98788653014`, completed successfully on the repository-scoped `adguardvm` runner using an exact `main` checkout, `contents: read`, and no persisted checkout credentials.

Audit output:

- `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`
- `TSK_0166_CURRENT_ARTIFACT_BOUNDARY_PROOF=PASS`
- `TSK_0214_ACCEPTANCE_CLASSES=6/6`
- `TSK_0214_ARTIFACT_BLOB=5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`
- `TSK_0214_INDEPENDENT_AUDIT=PASS`

The audit also pinned `VALIDATION_READINESS_GATE.md` to blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1` and `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md` to blob `c7706fceced87c797b8cd92179198754e2b08ffe`.

## Boundary

This PASS verifies a pre-experiment retention/deletion execution checklist only. No participant data was processed or deleted by this verification, no recruitment or child-linked DNS activation is authorised, and the validation-readiness/legal gates remain unchanged.
