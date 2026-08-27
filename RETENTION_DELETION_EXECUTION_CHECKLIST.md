# UseSafeWeb — Experiment-1 Retention and Deletion Execution Checklist

**Task:** TSK-0214  
**Gate:** LG-03 Validation Readiness  
**Status:** operational checklist  
**Reviewed:** 2026-08-27

## Purpose

Turn the frozen Experiment-1 retention policy into an executable, verifiable deletion process. This checklist does not authorise participant activation; it is preparation for a future LG-03/LG-04-authorised experiment.

## Frozen retention baseline

- **Identifiable DNS/domain history:** not retained as an Experiment-1 product/research record.
- **Exceptional diagnostic data:** only when genuinely necessary under `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md`; delete after resolution or the approved diagnostic window and verify deletion.
- **Parent contact details for 14-day follow-up:** retain only through the follow-up; delete promptly afterward and no later than **30 days after that participant's follow-up**.
- **Pseudonymous participant-level experiment metrics:** retain through experiment analysis/decision; then aggregate/anonymise and delete participant-level records no later than **90 days after Experiment 1 closes**.
- **Canonical GitHub:** aggregate/anonymised findings only; no participant identities or child browsing/domain history.

## Data-location register

Before recruitment, complete one row for every actual location that can hold Experiment-1 data. A location not listed here must not be used until it is added and reviewed.

| Data location / system | Data class allowed | Responsible owner | Deletion trigger | Exact deletion due date | Deletion method | Verification method | Aggregate output allowed? | Current status |
|---|---|---|---|---|---|---|---|---|
| Participant/contact record location | Parent contact + pseudonymous participant ID only as required for follow-up | Project Owner / Research | Participant's 14-day follow-up completed | **Calculate and record:** follow-up date + 30 days maximum | Delete participant contact fields/record as designed | Query/export or UI/API read-back proving record/fields absent | No identifiable contact output | Not active before participant gate |
| Pseudonymous experiment metric store | Minimum fields defined in `EXPERIMENT_01_CONCIERGE_VALIDATION.md` | Product/Research | Experiment analysis/decision completed | **Calculate and record:** Experiment-1 close date + 90 days maximum | Aggregate/anonymise required results, then delete participant-level rows | Re-query/export proving participant IDs/rows absent; verify aggregate contains no re-identifying fields | Yes — aggregate/anonymised only | Not active before participant gate |
| AdGuard/DNS service | No persistent identifiable DNS/domain history for experiment research/product use | Network/Operations | Continuous control | N/A — prohibited from persistent retention | Keep query/file logs and identifiable client statistics disabled/excluded per deployed acceptance | Configuration inspection + targeted test; any exceptional log uses TSK-0227 | Aggregate only if separately approved and non-identifying | Deployment verification pending |
| Exceptional diagnostic location | Only exact fields approved by TSK-0227 | Incident owner | Fault resolved or approved diagnostic end time | Exact approved UTC end time from diagnostic ticket | Delete dataset and copies/exports | TSK-0227 recorded deletion verification | Non-sensitive incident conclusion only | Used only by exception |
| GitHub canonical repository | Aggregate/anonymised findings, procedures, non-sensitive evidence | Project Governance | Continuous control | N/A — prohibited data must never be committed | Prevent/remove prohibited content; incident handling if exposure occurs | Repository inspection / secret-data review | Yes — aggregate/anonymised only | Active |

Add actual infrastructure/provider locations after deployment and before they hold participant data. Do not assume a provider location from the design alone.

## Participant-level execution checklist

For each participant:

- [ ] Record pseudonymous participant ID; do not use child name or exact DOB as the identifier.
- [ ] Record the actual 14-day follow-up completion date.
- [ ] Calculate and record the **contact deletion due date** (no later than follow-up completion + 30 days).
- [ ] Delete contact details when follow-up no longer requires them; do not wait until the maximum if earlier deletion is practical.
- [ ] Verify deletion from every registered contact-data location and any export/copy.
- [ ] Record deletion UTC, verifier, locations checked, PASS/FAIL and deviation disposition.

## Experiment-close execution checklist

- [ ] Record the authoritative Experiment-1 close date.
- [ ] Record the analysis/decision completion date.
- [ ] Produce only the aggregate/anonymised decision output required by the protocol.
- [ ] Review the aggregate for identifiers, small-cell/re-identification risk and prohibited child browsing/domain data before GitHub publication.
- [ ] Calculate and record the participant-metric deletion due date (no later than Experiment-1 close + 90 days).
- [ ] Delete participant-level pseudonymous rows from every registered metric-data location by the due date.
- [ ] Delete obsolete exports/backups/copies where the project controls them; document provider/system constraints instead of assuming deletion.
- [ ] Verify participant-level deletion and record evidence.
- [ ] Confirm GitHub contains only aggregate/anonymised findings.

## Deletion evidence record

```text
Deletion event ID:
Data class:
Location/system:
Responsible owner:
Trigger date:
Required deletion due date:
Actual deletion UTC:
Deletion method:
Copies/exports checked:
Verification method:
Verification result: PASS/FAIL
Verifier:
Aggregate/anonymised output reference (if any):
Exception/deviation reference (if any):
Disposition:
```

Do not put participant identifiers, contact details, raw DNS/query data, credentials, tokens or private keys in the GitHub evidence record.

## Exception handling

An exception never silently changes the frozen retention rule.

If deletion cannot occur on schedule because of a concrete security incident, legal preservation obligation, provider limitation, or verified technical failure:

1. open a non-sensitive exception/deviation record before the due date where possible;
2. identify the exact affected data and location without copying the data into GitHub;
3. record the authority/reason for temporary retention;
4. restrict access and prohibit secondary use;
5. set the earliest defensible replacement deletion date or deterministic condition;
6. assign an owner;
7. verify deletion when the condition ends;
8. escalate any unresolved or high-risk deviation to the Project Owner/privacy authority.

A convenience, analytics idea, future product possibility, or indefinite troubleshooting need is not an acceptable retention exception.

## Canonical baseline used

- `VALIDATION_READINESS_GATE.md` §§4, 6 and 8.
- `PILOT_PRIVACY_NOTICE.md` retention and DNS-processing sections.
- `EXPERIMENT_01_CONCIERGE_VALIDATION.md` minimum dataset and aggregate-output rules.
- `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md` for temporary diagnostic data.
- Frozen WBS ACC-0214 / REQ-0018 / REQ-0019 / CON-0007 / CON-0008.

## Acceptance result

This checklist identifies the controlled data locations, responsible owners, exact due-date rules and per-event due-date fields, deletion methods, verification methods, permitted aggregate output, and fail-closed exception handling required by ACC-0214.
