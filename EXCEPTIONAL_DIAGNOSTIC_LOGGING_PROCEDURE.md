# UseSafeWeb — Exceptional Diagnostic Logging Procedure

**Task:** TSK-0227  
**Gate:** LG-03 Validation Readiness  
**Status:** operational runbook  
**Reviewed:** 2026-08-27

## Default rule

Persistent identifiable DNS/query logging remains **OFF**. File query logging remains **OFF**. Identifiable per-client statistics remain **OFF/excluded** unless separately justified and approved. This procedure is only for a specific fault that cannot be diagnosed with lower-data methods.

Diagnostic collection must be necessary, minimal, explicitly time-bounded, access-restricted, and deleted after the fault is resolved or the approved diagnostic window ends. Raw diagnostic data must not be committed to GitHub.

## Before enabling exceptional logging

Create one diagnostic record containing every field below. If a required field cannot be completed, do not enable the collection.

| Required field | Required content |
|---|---|
| Incident / ticket ID | Unique non-personal identifier linking the diagnostic action to a concrete fault. |
| Problem statement | What is failing and what lower-data checks have already been attempted. |
| Necessity | Why the remaining question cannot reasonably be answered without the proposed temporary data. |
| Exact fields | Explicit allowlist of fields to be collected; unspecified fields are prohibited. |
| Data subjects / scope | Smallest affected device/client/test scope; do not broaden to unrelated users. |
| Start time | UTC start time. |
| End time | UTC stop time chosen before collection begins; collection must stop no later than this time unless a new approval record is created. |
| Storage location | Approved restricted diagnostic location; never GitHub. |
| Access list | Named roles/people authorised to access the temporary data. |
| Approver | Project Owner or explicitly delegated incident/privacy authority who reviewed necessity and scope. |
| User notice | Whether a parent/user notice is required or appropriate for the diagnostic action; record the notice or the reason it is not applicable. |
| Deletion owner | Person responsible for deletion. |
| Deletion verification method | How deletion from the collection location and any diagnostic copy will be checked. |

## Data minimisation order

Use the first method that can answer the diagnostic question:

1. service health/configuration/status without request data;
2. synthetic test traffic created specifically for diagnosis;
3. aggregated/non-identifying operational counters;
4. anonymised/coarsened network diagnostics;
5. only if still necessary, the minimum temporary identifiable/request-level fields explicitly approved above.

Do not collect child browsing/domain history merely because it is convenient. Do not enable a broad query log to investigate an unrelated application, TLS, DNS reachability, certificate, capacity, or configuration problem when a narrower test can answer it.

## Activation procedure

1. Confirm the ticket record is complete and approved.
2. Capture the current logging/privacy configuration needed to restore the baseline, without recording secrets.
3. Configure only the approved fields/scope and the shortest practical collection window.
4. Verify access restrictions before producing diagnostic data.
5. Record the actual UTC start time.
6. Re-check that no raw log path, token, credential, private key, ClientID-as-behavioral identifier, or child browsing history is being sent to GitHub/telemetry outside the approved diagnostic location.
7. Diagnose the concrete fault; stop early when sufficient evidence exists.

## Stop and deletion procedure

At fault resolution or the approved end time, whichever comes first:

1. disable the exceptional collection;
2. restore and verify the privacy-minimal baseline configuration;
3. record the actual UTC stop time;
4. retain only the minimum non-sensitive incident conclusion needed for operations;
5. delete the temporary diagnostic dataset and any diagnostic copies/exports;
6. perform the predefined deletion verification;
7. record deletion time, verifier, locations checked, and PASS/FAIL;
8. if deletion verification fails, treat it as an incident and escalate to the Project Owner/privacy authority rather than marking the diagnostic action closed.

## Diagnostic record template

```text
Incident/ticket ID:
Problem statement:
Lower-data checks attempted:
Necessity for temporary logging:
Approved fields:
Affected scope:
Approved UTC start:
Approved UTC end:
Storage location:
Authorised access:
Approver:
User notice required/applicable?:
Notice/reference or non-applicability reason:
Deletion owner:
Deletion verification method:

Actual UTC start:
Actual UTC stop:
Finding (non-sensitive):
Baseline restored and verified: PASS/FAIL
Temporary data deleted: PASS/FAIL
Deletion verification UTC:
Deletion verifier:
Locations checked:
Residual deviation / disposition:
```

## Hard prohibitions

- no indefinite or open-ended exceptional logging;
- no silent expansion beyond the approved fields, users, devices or time window;
- no GitHub commit of raw diagnostic/query data;
- no reuse of temporary diagnostic data for analytics, product metrics, profiling, marketing or behavioral monitoring;
- no claim that deletion occurred without a recorded verification result;
- no automatic extension after the approved end time.

## Canonical baseline used

- `VALIDATION_READINESS_GATE.md` §§6 and 8 — diagnostic logging only when genuinely necessary, time-boxed and deleted after resolution.
- `PILOT_PRIVACY_NOTICE.md` — parent/child transparency for exceptional diagnostics.
- `EXPERIMENT_01_CONCIERGE_VALIDATION.md` — no child browsing history except the readiness gate's minimum exceptional procedure.
- Frozen WBS ACC-0227 and REQ-0018 / REQ-0019 / CON-0007 / CON-0008.

## Acceptance result

This runbook requires an incident/ticket ID, necessity, exact fields, approver, start/end times, restricted access, user notice decision, deletion owner, and explicit deletion verification before closure. It keeps exceptional collection bounded by the frozen privacy-minimal baseline.
