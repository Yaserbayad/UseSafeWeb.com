# TSK-0166 — Pseudonymous Participant Record & Metric Schema Evidence

**Task:** TSK-0166  
**Acceptance:** ACC-0166  
**Verification:** VER-0166  
**Evidence:** EVD-0166  
**Date:** 2026-08-28  
**Outcome:** PASS

## Task contract

The canonical WBS defines TSK-0166, `Create pseudonymous participant record and metric schema`, as L2 / A3 / `AUTO_ALLOWED` / MEDIUM, with hard predecessors TSK-0223 and TSK-0164.

ACC-0166 requires the template to contain participant ID, qualification, device/path, safeguard states, activation, time, assistance, abandonment, comprehension, false positives and 14-day state, with no prohibited fields.

The task is additionally bound by REQ-0013, REQ-0014, REQ-0015, CON-0025, CON-0009, INT-0005 and RSK-0002.

## Direct predecessor reconciliation

Historical/planning PASS labels were not used by themselves to satisfy the dependencies.

### TSK-0164 direct proof

Current durable artifact `EXPERIMENT_01_CONCIERGE_VALIDATION.md`, blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`, directly contains:

- the 20–30 qualified England parent/caregiver cohort;
- qualification criteria and real appropriate configuration actions;
- facilitator intervention rules and the prohibition on silently completing the parent's setup;
- mandatory participant measurements;
- promising decision thresholds;
- strong failure/kill thresholds and privacy/security stop condition;
- Wave A first 10, one controlled refinement, Wave B remaining 10–20;
- aggregate/anonymised decision output and explicit continue/modify/pivot/stop recommendation.

This directly reconstructs ACC-0164 under the current frozen protocol.

### TSK-0223 direct proof

Current durable artifact `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly defines the minimum experiment data and prohibits by default:

- child name/exact DOB;
- school;
- child email/phone;
- contacts/location/messages/photos;
- social usernames;
- browsing-history/domain-history reports.

It also limits GitHub to aggregate/anonymised experiment results. This directly reconstructs ACC-0223 under the current privacy baseline.

## TSK-0166 artifact

Created:

`EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md`

Version: `1.0.0`  
Git blob after read-back: `c7706fceced87c797b8cd92179198754e2b08ffe`

The artifact is explicitly an empty pre-experiment template, not a participant data store. It authorises no recruitment or real-participant processing.

The schema includes controlled fields for:

- opaque pseudonymous participant ID and Wave A/B;
- qualification and non-identifying reason code;
- target life-stage/timing bands, device family and setup path;
- native, DNS and service safeguard states;
- full activation and Protection Map completion;
- activation time;
- active facilitator-assistance minutes/category and a mandatory no-silent-completion control;
- abandonment stage/reason and duplicated-work measurement;
- structured two-gap comprehension;
- false-positive/compatibility category and privacy-safe support-case linkage;
- 14-day follow-up and baseline-protection state/reason.

The schema deliberately avoids uncontrolled narrative/free-text participant fields.

## Privacy and non-goal controls

The artifact explicitly excludes child name, exact DOB, school, child contact details, location, contacts, messages, photos, social usernames/content, browsing history, DNS query/domain history, URLs/top-domain lists, payment/card data, raw diagnostic logs and uncontrolled free-text notes.

Real participant records must not be committed to GitHub. Contact identity/mapping is outside this metric record and remains governed by the separate retention/privacy controls. No collection begins merely because the template exists.

REQ-0014 non-goals are preserved: the schema does not introduce payment testing, paid acquisition, broad DNS feature testing, child accounts or full parental-control scope.

REQ-0015 is directly implemented by mandatory assistance duration/category plus `facilitator_completed_parent_action`, which must remain `no`; a `yes` invalidates the session for normal completion analysis and requires review.

## Independent verification

Repository workflow `.github/workflows/governance-task-row-inspect.yml` was pinned to the read-back schema blob and ran a read-only independent static audit.

- workflow trigger commit: `ea8dc686c31ea1f759d32469def25fab65d64300`;
- run: `33130737625`;
- job: `98719395096`;
- conclusion: **PASS**.

Direct verifier output:

- `TSK_0164_DIRECT_PREDECESSOR_PROOF=PASS`;
- `TSK_0223_DIRECT_PREDECESSOR_PROOF=PASS`;
- `TSK_0166_REQUIRED_FIELD_COUNT=19`;
- `TSK_0166_SCHEMA_FIELD_COUNT=37`;
- `TSK_0166_FORBIDDEN_FIELD_COUNT=0`;
- `TSK_0166_SCHEMA_BLOB=c7706fceced87c797b8cd92179198754e2b08ffe`;
- `TSK_0166_INDEPENDENT_AUDIT=PASS`.

The audit separately parsed schema field names rather than treating the explicit prohibited-field documentation as fields, verified every acceptance-critical field, rejected forbidden field tokens, checked the real-participant/GitHub/gate safeguards, and independently rechecked both predecessor artifacts.

## Acceptance evaluation

| ACC-0166 element | Result | Direct proof |
| --- | --- | --- |
| Participant ID | PASS | `participant_id` |
| Qualification | PASS | qualification result/reason plus bounded qualification route fields |
| Device/path | PASS | `device_family`, `phone_state` |
| Safeguard states | PASS | native, DNS and service state fields |
| Activation | PASS | full activation, Protection Map and incremental safeguard fields |
| Time | PASS | `time_to_full_activation_minutes` |
| Assistance | PASS | active minutes/category + no-silent-completion control |
| Abandonment | PASS | abandoned/stage/reason/duplication fields |
| Comprehension | PASS | two structured coverage-gap checks and aggregate pass field |
| False positives | PASS | structured false-positive/compatibility issue fields without domain history |
| 14-day state | PASS | follow-up/state/reason fields |
| No prohibited fields | PASS | explicit exclusion list plus independent field-token audit returning zero prohibited fields |

## Stable outcome

**TSK-0166: PASS.**

ACC-0166 is fully satisfied with a versioned empty schema, direct predecessor proof and an independent audit. This PASS does not change the still-blocking validation-readiness gate and does not authorise recruitment, real child-linked DNS processing or participant-data collection.
