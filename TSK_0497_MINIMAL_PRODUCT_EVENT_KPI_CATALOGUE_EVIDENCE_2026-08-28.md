# TSK-0497 — Minimal Product Event and KPI Catalogue Verification Evidence

**Task:** TSK-0497 — Define minimal product event and KPI catalogue  
**Acceptance:** ACC-0497  
**Verification:** VER-0497 — independent event/KPI/privacy/denominator audit  
**Evidence:** EVD-0497  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- Measurement contract: `TSK_0497_MINIMAL_PRODUCT_EVENT_KPI_CATALOGUE_2026-08-28.md`
- Contract blob: `61bcd78bbe7ac2446c9c79e5e2e0765cb4f66b8c`
- Corrected contract commit: `593d714c06a734aaf0415c11c8e1fefe92dac376`
- Current selection/runtime: `CURRENT_STATE.md` blob at selection read-back `a96d0cf9f08a47892729bddf8e4b7cb291298299`; TSK-0497 selected as L4 / MEDIUM / A3 / AUTO_ALLOWED, hard dependency TSK-0230 PASS.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- TSK-0230 privacy/data NFR blob: `011caaa84dd3dec13bb608be30b15ec92a24f19e`
- TSK-0229 accountless data contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- TSK-0313 Protection Map requirements blob: `521c9cc5073aa289281acade12a66a9e979e197d`
- TSK-0320 protection-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- TSK-0042 support/recovery contract blob: `bf9e1ece69b5ccfc38c1cb44d69de6545b7865dc`
- REQ-0060/0061 current requirement register: each KPI must define source/formula/denominator/time window/release-cohort/owner/guardrail/decision action; browsing/top-domain/visited-domain/child-activity/addictive-engagement metrics are prohibited.
- INT-0016 current interface: approved event schema/retention/quality/telemetry behavior must exclude browsing/activity data and later match actual implementation exactly.

## 2. Authority and eligibility audit

The current queue placed TSK-0497 before equal-priority TSK-0538 by WBS order. TSK-0187 remains representative-parent-evidence-bound and TSK-0140 remains owner-review-bound. TSK-0497 has no preflight flag and its direct dependency TSK-0230 is current PASS.

The work is internal provisional L4 measurement definition only. It does not activate telemetry, a datastore, real participants, accounts, public release or build.

`RSK-0002` remains OPEN and the contract explicitly states that KPI definitions are not observed behavioral results.

**Result: PASS.**

## 3. ACC-0497 approved-event completeness audit

ACC-0497 requires every **approved event** to have:

1. purpose;
2. exact definition;
3. properties;
4. prohibited fields;
5. collection point;
6. denominator relationship;
7. retention;
8. owner.

Section 5 defines exactly 14 approved events in one table with all eight dimensions as dedicated columns:

1. `journey_started`;
2. `journey_completed`;
3. `journey_reset_or_exit`;
4. `dns_setup_attempted`;
5. `dns_verification_result`;
6. `dns_removal_recovery_result`;
7. `protection_map_presented`;
8. `support_issue_classified`;
9. `self_service_resolution_result`;
10. `filtering_false_positive_outcome`;
11. `exceptional_diagnostic_invoked`;
12. `privacy_security_escalation`;
13. `safeguarding_route_invoked`;
14. `stale_guidance_detected`.

Every row gives an exact trigger and uses **raw retention = 0 after aggregate commit**, with the exceptional-diagnostic row correctly separating the event count from the separately governed diagnostic dataset.

The first draft ambiguously described `human_assistance_summary` like an event without the complete eight-field contract. That ambiguity was corrected before verification: the current read-back explicitly says **no human-assistance event is approved** while the relevant real-user/staffed-support gate is inactive. Activation requires reopening this catalogue or an authoritative successor and supplying the complete ACC-0497 metadata before collection.

**Result: PASS.**

## 4. Accountless/minimum-data architecture audit

The measurement architecture is stricter than pseudonymous user analytics:

- validate controlled event -> update approved aggregate -> discard source payload;
- no persistent raw event stream;
- no event history/clickstream in J0/J1;
- no stable analytics user/device/household/session identity;
- full journey token never becomes an event property, dimension, log field or join key;
- raw event retention is zero after aggregate commit;
- a durable retry/event queue is **not** pre-authorized and would require TSK-0230 impact review;
- synthetic and future authorized real cohorts are explicitly separated;
- coarse dimensions must be suppressed if their combination would make a household/journey reasonably identifiable.

This is consistent with TSK-0229's no-linkage/no-clickstream rules and TSK-0230's necessity/no-history/no-cross-session-stitching controls.

**Result: PASS.**

## 5. REQ-0061 prohibited-measurement audit

The contract globally prohibits and explicitly omits:

- DNS query names and query-history events;
- URLs, visited domains, blocked/allowed domain histories and top-domain metrics;
- child activity/content/message/contact/photo/social history;
- page-view/screen-view/button-click trails;
- session duration, daily-active-user, streak, return-frequency and addictive-engagement metrics;
- IP analytics, persistent device/customer/user IDs and advertising/fingerprint identities;
- support transcripts, safeguarding disclosure content and raw diagnostic payloads.

The false-positive metric intentionally excludes the affected domain/site/app identifier; DNS verification excludes the synthetic/query domain and raw DNS response; removal/recovery excludes ordinary DNS domains used for neutral checks.

**Result: PASS.**

## 6. Account/login/dashboard exclusion audit

ACC-0497 requires login/account/dashboard events to remain absent unless EXC-0001 activates.

Section 6 explicitly excludes:

- `login`, `logout`, `signup`, `password_reset`, `account_created`, `dashboard_viewed`, `device_added_to_account`;
- account/user/device analytics identity.

Section 11 makes adding account/login/dashboard telemetry a TSK-0497 + TSK-0230 change trigger.

No EXC-0001 activation or account architecture is inferred.

**Result: PASS.**

## 7. Protection Map evidence-strength audit

The contract consumes TSK-0313/0320 rather than inventing new safety semantics:

- `dns_verification_result` permits `verified` only from the approved technical verifier; parent confirmation cannot generate it;
- `protection_map_presented` preserves Phone/Internet/Services S1–S6 independently;
- no overall safety score is collected;
- mixed states remain measurable rather than normalized green;
- KPI rules keep completion distinct from protection success.

**Result: PASS.**

## 8. Support/safeguarding/diagnostic minimisation audit

The TSK-0042 issue taxonomy and boundaries are preserved:

- support metrics use controlled `issue_class`, severity and root-cause codes only;
- no transcript/free text/domain/history is retained;
- false-positive causality outcome is measured without affected domain identity;
- exceptional diagnostic analytics counts invocation only; diagnostic payload stays in the separately governed temporary incident process;
- privacy/security escalation analytics stores only broad controlled incident class;
- safeguarding analytics, where its applicable gate permits collection, is a non-identifying invocation count only with no disclosure or outcome content;
- real human-assistance measurement remains dormant, with no fabricated current support-burden data.

**Result: PASS.**

## 9. REQ-0060 KPI completeness audit

Section 7 defines 17 KPI/measurement rows. Each row provides:

- source event/source;
- exact formula and denominator rule;
- reporting window and release/cohort dimensions;
- owner;
- guardrail;
- decision action.

The two human-assistance rows are clearly marked **dormant** and source a future governed measurement contract, not a currently approved event or current dataset.

Section 8 adds reproducibility rules:

- numerator/denominator definitions are versioned with the aggregate;
- rates with unavailable denominators are counts rather than fabricated percentages;
- missing data, instrumentation failure and zero are distinct;
- synthetic data cannot enter real-user metrics;
- parent confirmation and technical verification remain distinct;
- schema/semantic changes require versioning before time-series combination.

No invented performance threshold or current KPI value is presented.

**Result: PASS.**

## 10. INT-0016 / aggregate-storage audit

The approved aggregate store may contain only metric/event aggregate name/schema version, UTC window, release/cohort class, approved coarse dimensions, integer counts/sums/rates with numerator and denominator, quality marker and decision/evidence version reference.

It explicitly cannot contain the source event payload or user/journey identifier. Low-count/high-cardinality exports must be further aggregated/suppressed where re-identification risk exists.

Implementation must later prove:

- event allowlists and prohibited-property rejection;
- no user-level event table/log/backup;
- raw payload absent after aggregate commit;
- no persistent identity or journey token in telemetry;
- synthetic/real cohort separation;
- actual runtime/schema/storage equality with the approved contract.

This supplies the INT-0016 event schema/retention/quality behavior needed by downstream engineering without creating an implementation claim.

**Result: PASS.**

## 11. Retirement/change-control audit

The contract applies REQ-0064 by requiring events/aggregates to be retired when the decision purpose disappears, the metric is unused/unactionable, lower-data evidence exists, or measurement privacy cost outweighs value.

Reopening is mandatory for new event/property/dimension, persistent raw queue/table, analytics identity, account telemetry, DNS/domain/activity measurement, third-party analytics/session replay/advertising, cross-system linkage, J1 persistence changes, new real cohort/geography, material denominator change or dormant human-support collection.

**Result: PASS.**

## 12. Verification disposition

**VER-0497 independent audit result: PASS for ACC-0497's provisional internal L4 measurement-contract-definition scope.**

The read-back contract at blob `61bcd78bbe7ac2446c9c79e5e2e0765cb4f66b8c` satisfies every ACC-0497 field for every currently approved event; defines REQ-0060-complete KPIs; excludes account/login/dashboard telemetry while EXC-0001 is inactive; and prohibits DNS/domain/visited-domain/child-activity/addictive-engagement measurement under REQ-0061.

The following remain OPEN/non-PASS and are not converted by this result:

- telemetry/application implementation and runtime verification;
- any durable raw-event/event-delivery store;
- dormant human-assistance measurement;
- real-user KPI values or behavioral conclusions (`RSK-0002`);
- final privacy/legal/participant gates;
- account/dashboard activation;
- build, publication and launch.

**Runtime may move TSK-0497 to PASS only after this evidence file is persisted/read back and a guarded reconciliation verifies the current selection, exact contract/evidence/WBS/runtime preconditions.**
