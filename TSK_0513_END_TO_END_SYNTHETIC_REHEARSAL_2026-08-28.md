# TSK-0513 — End-to-End Synthetic Rehearsal

**Task:** TSK-0513 — Run end-to-end synthetic rehearsal  
**Lifecycle:** L2 / Pre-Experiment  
**Date:** 2026-08-28  
**Scope:** synthetic/internal/non-participant only  
**Gate state:** G-02 / LG-03 = DEFER  
**Recruitment authorized:** NO

## 1. Purpose and boundary

This rehearsal exercises the approved Experiment-1 operating path with **synthetic data only**. It does not contact, recruit, schedule, activate, observe, or process a real participant. It does not create a real child-linked DNS record or participant metric record.

The synthetic fixture is `fixtures/experiment1/TSK_0513_SYNTHETIC_REHEARSAL_FIXTURE_V1.json`, blob `8189de9d6f5fa554ff23fb127f95604c8fc381a5`. All identifiers beginning `SYN-` are fabricated test identifiers with no mapping to a person.

The fixture's `activated_verified` and similar values are **synthetic state values used to test the workflow/schema**. They are not a claim that a new participant/device was activated during this rehearsal. Technical feasibility is bound separately to already accepted current evidence (TSK-0511, TSK-0512, TSK-0207, TSK-0428, TSK-0431 and TSK-0510).

## 2. Authority and accepted inputs

- Experiment protocol: `EXPERIMENT_01_CONCIERGE_VALIDATION.md`, blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`.
- Participant schema: `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md`, blob `c7706fceced87c797b8cd92179198754e2b08ffe`.
- Qualification screener: `EXPERIMENT_01_QUALIFICATION_SCREENER.md`, blob `d35d3e0abfc3882d648df3c0c7458e216853b592`.
- Facilitator guide: `EXPERIMENT_01_FACILITATOR_GUIDE.md`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`.
- Support/false-positive intake: `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`, blob `9fab42f97e3e96023de89a8ed266acc21c0f06ab`.
- Retention/deletion checklist: `RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`.
- Participant communication templates: `EXPERIMENT_01_PARTICIPANT_COMMUNICATION_TEMPLATES.md`, blob `1dd5aa88f200174d88d1422bbe0c11f7fc5ecbe8`.
- TSK-0167 evidence: `TSK_0167_PARTICIPANT_COMMUNICATION_TEMPLATES_EVIDENCE_2026-08-28.md`, blob `06506a61d8065bfa812f6df49006d840ef2339ff`.
- Pilot technical acceptance: `TSK_0510_PILOT_TECHNICAL_ACCEPTANCE_REPORT_2026-08-28.md`, blob `fbc41f65ec56e7e9ea8873e9a995b66ae9e8f2c9`.
- Owner gate decision: `TSK_0027_G02_LG03_OWNER_DEFER_DECISION_EVIDENCE_2026-08-28.md`, blob `1c12e4f4e31962735dd3a3a8bd94ccbfa8308e92`.

## 3. Main synthetic end-to-end path

| Step | Synthetic action | Expected control/result | Rehearsal result |
| ---: | --- | --- | --- |
| 1 | Generate invitation | Voluntary; no payment ask; privacy-minimal qualification summary; contacts remain release-blocked | PASS — generated only, not sent |
| 2 | Run qualification logic | Caregiver responsible; first-phone stage; approved timing; Android/iPhone; willing real changes; non-surveillance fit; no child name/exact DOB | PASS — synthetic fixture qualifies |
| 3 | Generate scheduling confirmation | What-to-prepare instructions; no credentials sent; voluntary cancel/reschedule/withdraw route | PASS — generated only, not sent |
| 4 | Generate reminder | Repeats minimum preparation/support/privacy boundaries | PASS — generated only, not sent |
| 5 | Open synthetic session | Tests journey, not parent; participant tries first; bounded help recorded; no complete-safety claim | PASS |
| 6 | Minimal synthetic intake | Uses only allowed structured fields; no prohibited free text or identity fields | PASS |
| 7 | Produce Phone → Internet → Service plan | Preserves approved three-layer sequence and avoids broad product scope | PASS |
| 8 | Native safeguard step | Synthetic `completed_during_session`; facilitator does not perform user's action | PASS |
| 9 | Baseline protection step | Synthetic `activated_verified` schema state; feasibility bound to already accepted TSK-0511/0512/0207/0428 evidence rather than a new participant action | PASS |
| 10 | Relevant service safeguard | `none_applicable` is used; no artificial substitute task is invented | PASS |
| 11 | Protection Map | Reaches approved state model and keeps verified vs parent-confirmed distinction | PASS |
| 12 | Coverage-gap comprehension | Two material gaps marked understood using structured yes/no results; no verbatim personal explanation retained | PASS |
| 13 | Assistance accounting | One synthetic U2 navigation intervention; 2 active minutes; parent retains action; facilitator-completed-action = no | PASS |
| 14 | Session close | Full activation derived from applicable synthetic states; no payment ask | PASS |
| 15 | 14-day follow-up | Synthetic follow-up complete; baseline state = active; communication generated only; no browsing/domain history requested | PASS |
| 16 | Retention/deletion logic | Contact/metric deletion rules are represented without storing a real contact or identity | PASS |

## 4. Synthetic support / false-positive branch

Fixture `SYN-SUP-001` tests the approved support path without a real domain/query history:

1. category = `FALSE-POSITIVE`, severity = `S3`;
2. symptom is a generic synthetic supported-path block, not a domain/URL/history record;
3. evidence binds to the accepted synthetic filtering exception/rollback behavior already proven by TSK-0512;
4. action is a narrow synthetic exception/retest/exact-rollback path rather than blanket filtering disablement;
5. active assistance minutes are recorded;
6. no exceptional diagnostic logging is invoked;
7. outcome/protection state and closure are recorded.

**Branch result: PASS.** No raw DNS/query data or participant browsing evidence is created.

## 5. Synthetic withdrawal/removal branch

Fixture `SYN-E1-003` tests the withdrawal route:

- withdrawal acknowledgment generated but not sent;
- no further participation is required;
- removal/recovery semantics bind to accepted TSK-0514 evidence rather than touching a real participant device;
- contact deletion is triggered promptly when no longer needed and remains bounded by the approved maximum;
- no participant data is written to GitHub.

**Branch result: PASS.**

## 6. Synthetic safeguarding boundary

Fixture `SYN-SAFE-001` contains no real disclosure. It tests only the routing rule:

- category becomes `SAFEGUARDING`;
- ordinary product-support investigation stops;
- the path routes to `CHILD_SAFETY_ESCALATION_PROCEDURE.md`;
- product support does not investigate or collect personal disclosure details.

**Boundary result: PASS.**

## 7. Prohibited-data audit

The synthetic fixture intentionally contains **none** of the following real-person data classes:

- child or parent name;
- exact date of birth;
- school;
- email address or phone number;
- precise/routine location;
- contacts/address book;
- messages/message content;
- photos/images;
- social usernames/content;
- browsing history, DNS query history, visited-domain history, URLs, top-domain lists or per-domain activity;
- payment/card data;
- credentials, passwords, authentication codes, tokens or private keys;
- raw diagnostic logs.

The only participant IDs are explicit synthetic values (`SYN-*`) with no identity mapping.

**Prohibited-data result: PASS.**

## 8. Technical evidence binding

This rehearsal does not repeat or weaken the accepted technical verification. It uses the following current PASS evidence as the technical feasibility boundary:

- TSK-0511 — supported-device encrypted DNS;
- TSK-0512 — filtering, narrow exception and exact rollback;
- TSK-0207 — privacy persistence/no prohibited history;
- TSK-0428 — Azure region/data path;
- TSK-0431 — recovery/rebuild + owner Azure restore evidence;
- TSK-0510 — compiled technical acceptance.

No new production mutation or real device action is needed for the synthetic process rehearsal.

## 9. Blockers and deviations

### Rehearsal-execution blockers

**None.** Every rehearsed step and branch completes using synthetic data and accepted preparation/technical evidence.

### Real-participant gate blockers intentionally preserved

1. final LIA/DPIA approval remains deferred/open;
2. final participant-facing notice/contact release remains deferred/open;
3. ICO/UK-representation position remains deferred/open;
4. participant-facing communication templates still contain unresolved release contacts and are not released.

These are **not accepted as cleared for G-03/LG-04 or real-participant use**. They are explicitly dispositioned by the Project Owner's TSK-0027 decision as **G-02/LG-03 = DEFER** and by CR-0002 as conditionally bypassed only for qualifying internal/synthetic/preparatory work through 2027-08-27.

Therefore the rehearsal does not hide an unresolved blocker and does not reinterpret DEFER as PASS.

## 10. ACC-0513 evaluation

ACC-0513 requires:

> Every step completes with synthetic data; no prohibited data is captured; blockers are fixed or explicitly accepted before G-03.

Evaluation:

- every main-path step completes with synthetic data: **PASS**;
- support/false-positive, withdrawal/removal and safeguarding-boundary branches complete synthetically: **PASS**;
- prohibited-data capture audit: **PASS**;
- no rehearsal-execution blocker remains;
- real-participant legal/contact blockers are explicitly dispositioned as **DEFER / unresolved before any G-03/LG-04 real-participant authorization**, not silently accepted as cleared.

**TSK-0513 acceptance disposition: PASS candidate, subject to independent machine audit and durable read-back.**

## 11. Gate effect

A successful TSK-0513 synthetic rehearsal does **not** change the current gate outcome:

- G-02 / LG-03 = **DEFER**;
- recruitment = **NOT AUTHORIZED**;
- real-participant processing = **NOT AUTHORIZED**;
- participant-facing templates = **NOT RELEASED**.

Any later gate decision must use the then-current legal/privacy/contact and technical evidence rather than inheriting synthetic-rehearsal PASS as participant authorization.
