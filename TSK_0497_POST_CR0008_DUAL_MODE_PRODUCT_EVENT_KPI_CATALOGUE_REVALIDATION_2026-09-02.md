# TSK-0497 — Post-CR-0008 Dual-Mode Product Event and KPI Catalogue Revalidation

**Task:** TSK-0497 — Define minimal product event and KPI catalogue  
**Acceptance / Verification / Evidence:** ACC-0497 / VER-0497 / EVD-0497  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0497 current PASS pending independent VER-0497 and guarded runtime reconciliation.

## 1. Current authority and revalidation boundary

Current WBS acceptance requires that:

- every approved event has an approved purpose;
- accountless events remain non-identifying;
- any optional-account event uses only the minimum authorised account/device identifiers actually needed for security, lifecycle or product operation;
- DNS/domain browsing history, child-activity timelines, unnecessary identity, content payloads, raw tokens/secrets and invasive attribution remain prohibited;
- retention, access and deletion are explicit.

Current direct dependency is TSK-0230, now current PASS under the post-CR-0008 privacy/data-minimisation/retention/deletion NFR.

The historical TSK-0497 contract remains strong for aggregate-by-design measurement, explicit KPI denominators, no browsing/activity analytics and truthful Protection Map/support metrics. It is stale where it explicitly prohibited all account/login/dashboard events because EXC-0001 was inactive. CR-0006 activated optional parent account/session/minimum ownership persistence/lightweight dashboard/device management while preserving a complete accountless core.

This revalidation does **not** activate telemetry, create a datastore, add a third-party analytics service, approve account-linked behavioral history or define final legal retention. It aligns the L4 KPI catalogue with current TSK-0230 and the already-current L5 TSK-0498 event contract.

## 2. Single event-schema authority — no duplicate analytics contract

For currently approved product analytics/measurement schemas, **TSK-0498 remains the current authoritative L5 event contract**:

- `TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md`;
- version `1.0.1`;
- blob `6b7a5095122c74ed9ec860b74408dab474576659`.

TSK-0497 therefore does not create a second competing event-schema authority. It owns the product/KPI catalogue and consumes the current TSK-0498 allowlist/retention/quality contract.

Current TSK-0498 permits exactly these twelve event names:

1. `journey_started`;
2. `journey_step_entered`;
3. `journey_step_outcome`;
4. `journey_completed`;
5. `protection_state_evaluated`;
6. `protection_verification_outcome`;
7. `self_service_opened`;
8. `self_service_outcome`;
9. `synthetic_service_probe_result`;
10. `recovery_operation_outcome`;
11. `channel_entry`;
12. `cost_period_recorded`.

Unknown event names or fields are rejected before durable storage. Historical TSK-0497 event names that are not present in this current TSK-0498 allowlist remain provenance/decision-intent evidence only and are not independently collection-approved by this L4 document.

## 3. Accountless measurement boundary

The current accountless event architecture is unchanged:

- no stable analytics user ID, account ID, device ID, household ID, advertising ID or fingerprint;
- accountless `journey_session_id` is random, account/device-independent, raw-only and maximum 24 hours;
- sign-in cannot extend or link accountless event history;
- raw accountless journey/protection/self-service/channel events are deleted by the 24-hour bound;
- retained product aggregates are non-linkable and maximum 13 months under the current TSK-0498 contract;
- synthetic reliability raw data contains no user/client identity and expires by 30 days;
- cost analytics remains period/category aggregate and is never joined to a person/session/device/account;
- no DNS qname/domain/URL/browsing/search/child-activity/support-free-text/raw-diagnostic content is an analytics field;
- unknown/high-cardinality fields fail closed rather than being silently retained.

TSK-0230 remains authority for privacy/data-element inventory and deletion requirements. TSK-0498 remains authority for current event schemas and raw/aggregate retention.

## 4. Optional-account event boundary under CR-0006

Optional account/session/dashboard/device-management capability is product scope, but **account identity is not thereby analytics identity**.

### 4.1 Product analytics rule

Product analytics may receive only non-identifying outcome information from an optional-account operation after the owning operational/authentication layer has already performed its authorization/lifecycle work.

By default the analytics payload contains **zero** account/device identifiers. Account email, provider subject, internal parent ID, persistent device ID, AdGuard ClientID, session/token ID, nickname and other ownership keys are prohibited from product analytics and aggregate dimensions.

If a future event truly requires an account/device identifier for security, lifecycle or product operation, that event is an **operational/security event**, not automatically a product-analytics event. It must satisfy the current TSK-0230 inventory and the owning auth/observability/security contract, including purpose, lawful-basis status, source, recipient, exact bounded retention, deletion, access, rights/safeguards and prohibited use.

### 4.2 No implicit new event approval

No new optional-account event name is collection-approved by this revalidation because current TSK-0498 explicitly rejects unknown event names/fields.

Before any new optional-account product event is emitted, governance must update/revalidate the owning event contract and TSK-0230 impact boundary. The new row must define all ACC-0497 event metadata and the implementation must prove the approved schema exactly.

Until then:

- unknown optional-account analytics events are rejected;
- account/session/device operational logs cannot be repurposed as product analytics;
- product KPIs requiring optional-account source events remain **DORMANT / NO CURRENT DATA SOURCE**;
- no account/device identifier may enter an aggregate merely because it existed in an operational transaction.

This is the least-data interpretation of the current WBS phrase allowing only the minimum authorised identifiers where genuinely needed.

## 5. Prohibited event/property classes

Current global prohibitions include:

- DNS query/qname, URL, visited/blocked/allowed/top-domain and browsing/search history;
- child activity/content/message/contact/photo/social history;
- parent/child name, email, phone, exact DOB, school, address, precise/routine location;
- raw IP as analytics data;
- provider subject, persistent account ID/device ID/ClientID as analytics join/dimension;
- raw token, session cookie, authorization header, API credential, private key or profile payload;
- page/screen/click trails, session replay, arbitrary free text, support transcript, disclosure narrative or raw diagnostic payload;
- full referrer URL/arbitrary campaign string;
- daily-active-user/streak/return-frequency/attention-time/addictive-engagement metrics;
- cross-session/cross-device identity graph or anonymous-to-account history join;
- marketing/advertising profile or user-level cost/revenue attribution.

## 6. Current approved event catalogue metadata

The table below is a catalogue view of the currently approved TSK-0498 event schemas. Exact field allowlists remain owned by TSK-0498; this table records the ACC-0497 decision metadata without duplicating those schemas.

| Event | Approved purpose / trigger boundary | Prohibited identity/content | Collection point | Denominator relationship | Retention / deletion | Access / owner |
|---|---|---|---|---|---|---|
| `journey_started` | Count intentional accountless starts | account/device identity, URL/referrer trail, DNS/content data | accountless start transition | denominator for accountless completion/route analysis | TSK-0498 R1 raw <=24h then delete; R2 non-linkable aggregates <=13m | approved analytics processor; Product Analytics/Product |
| `journey_step_entered` | Count entry to decision-critical bounded setup steps | identity, arbitrary page-view trail, content payload | bounded critical step entry | denominator for that exact step outcome | R1/R2 | Product Analytics/UX |
| `journey_step_outcome` | Measure completed/failed/skipped/unsupported/retry for bounded steps | identity, free text, domain/URL/raw error | bounded step outcome | matching step-entry denominator | R1/R2 | Product Analytics/UX |
| `journey_completed` | Count completion of complete accountless core; completion != all layers verified | identity, protection-score inference | accountless completion transition | numerator over `journey_started` | R1/R2 | Product Analytics/Product |
| `protection_state_evaluated` | Measure exact evidence-backed per-layer six-state distribution | overall safety score, identity, DNS history | Protection Map evaluator | valid layer evaluations | R1/R2 | Product Analytics/Product/Privacy |
| `protection_verification_outcome` | Measure technical verifier positive/negative/indeterminate/error truth | DNS qname/raw response, parent-confirmation-as-positive, identity | approved verifier boundary | valid verifier attempts | R1/R2 | Product Analytics/Network Engineering |
| `self_service_opened` | Count approved troubleshooting/recovery topic need | search/free text, transcript, identity | approved self-service route entry | valid journey sessions or exact topic opens, as declared | R1/R2 | Product Analytics/Customer Experience |
| `self_service_outcome` | Measure resolved/unresolved/escalated/abandoned/unknown | transcript/free text/domain/history/identity | self-service route outcome | corresponding topic opens | R1/R2 | Product Analytics/Customer Experience |
| `synthetic_service_probe_result` | Measure public/setup/verification/DNS reliability without observing users | user/client/account/device/domain data | controlled synthetic probe | scheduled probe opportunities | TSK-0498 R3 raw <=30d; non-linkable aggregate <=13m | SRE/Operations |
| `recovery_operation_outcome` | Measure governed recovery result without client/user data | user/account/domain content | governed runbook execution | initiated recovery operations of same type | R3 | SRE/Operations |
| `channel_entry` | Compare privacy-minimal channel source within same short-lived accountless session | full referrer, account/device identity, arbitrary UTM | approved first-party entry | valid channel entries or attributed accountless starts, explicitly named | R1/R2; session link destroyed at aggregation | Product Analytics/Growth |
| `cost_period_recorded` | Provide aggregate period/category cost input | user/session/device/account join, user-level revenue attribution | internal finance measurement boundary | defined decision period | TSK-0498 R4 <=13m measurement copy | Finance/Product Analytics |

Every currently approved event therefore has an approved purpose, trigger/definition boundary, property authority, prohibited fields, collection point, denominator semantics, retention/deletion rule and owner/access boundary.

## 7. Optional-account KPI definitions — dormant until source contract exists

CR-0006 creates legitimate future product questions, but metrics are not evidence until an approved source contract exists.

| KPI | Required future source | Formula / denominator | Window / cohort | Owner | Guardrail | Decision action | Current status |
|---|---|---|---|---|---|---|---|
| Optional sign-in/session success rate | approved future non-identifying auth/session outcome aggregate | successful accepted session operations / all accepted session attempts, failures/blocked/unknown separate | release + bounded reporting window | Product/Security/Analytics | no account/email/provider subject in analytics; provider outage separate from accountless core | investigate auth/provider/session defects without making login mandatory | DORMANT — no current approved TSK-0498 event |
| Owned-device lifecycle operation success rate | approved future non-identifying device lifecycle outcome aggregate | successful register/update/unlink/delete/revoke operations / accepted attempts by bounded operation class | release/window | Product/Platform/Analytics | no account/device/ClientID dimension; ownership enforced before measurement | investigate product/adapter/reconciliation failures | DORMANT |
| Account-deletion terminal-truth rate | approved future deletion/reconciliation aggregate | operations reaching verified terminal deletion/revoke truth / accepted account-deletion attempts | release/window | Product/Privacy/Security | no deleted payload/tombstone profile; account deletion != physical DNS removal | block/repair deletion flow if terminal truth cannot be proven | DORMANT |
| Accountless fallback preservation rate during auth/provider failure | approved synthetic/failure-fixture source | accountless core remains available / scheduled auth/provider/datastore failure fixtures | release/test window | Product/SRE/Security | synthetic/controlled evidence; no real-user identity | treat loss of accountless core as reliability/design defect | DORMANT until source is explicitly bound |

No current KPI value is invented. Activating any row requires an owning approved event/source contract and applicable implementation/privacy/security acceptance.

## 8. Current accountless/product KPI catalogue

The following KPIs consume current TSK-0498 events. Every KPI must record exact event-schema/formula version, numerator, denominator, window, release/cohort, owner, guardrail, decision action and missing-data state.

| KPI | Source | Formula / denominator | Window / cohort | Owner | Guardrail | Decision action |
|---|---|---|---|---|---|---|
| Accountless journey completion rate | `journey_started`, `journey_completed` | completed / valid starts | release/window/cohort | Product Analytics/Product | no inferred abandonment; completion != verified protection | investigate material route/content friction |
| Critical step outcome distribution | `journey_step_entered`, `journey_step_outcome` | each outcome / exact step entries | release/window/cohort/route | Analytics/UX | missing outcome remains missing/abandoned after expiry, not silently failed | target bounded UX/content fixes |
| Protection state distribution | `protection_state_evaluated` | each six-state count / valid layer evaluations | release/window/layer | Analytics/Product/Privacy | S1/S2 remain distinct; no overall safety score | investigate action-needed/not-covered/uncertain clusters |
| Technical verification outcome rate | `protection_verification_outcome` | each result / valid technical attempts | release/window/verifier/scope | Analytics/Network | parent/configuration confirmation cannot become positive | fix verifier/platform compatibility; preserve uncertainty truth |
| Self-service usage rate | `self_service_opened` | opens / declared valid journey denominator | release/window/topic | Analytics/CX | no search/free text | prioritize recurring bounded topics |
| Self-service resolution rate | `self_service_outcome`, `self_service_opened` | reported resolved / corresponding opens; unresolved/escalated/abandoned/unknown separate | release/window/topic | Analytics/CX | absence != resolved; no hidden human completion | improve recurring unresolved routes |
| Synthetic service availability | `synthetic_service_probe_result` | successful scheduled probes / scheduled opportunities, missing probe gaps separate | component/region/version/window | SRE/Operations | synthetic != user availability; no user data | investigate reliability/SLO breach |
| Recovery operation success distribution | `recovery_operation_outcome` | each result / initiated governed recoveries of same type | operation/window/runbook version | SRE/Operations | partial/rollback not mislabeled success | repair runbooks/recovery defect |
| Qualified accountless outcome by channel | `channel_entry`, accountless completion within same R1 session | completed attributed journeys / valid attributed starts or entries, denominator explicitly named | release/window/source class | Analytics/Growth | no full referrer/arbitrary UTM/persistent attribution identity | compare only privacy-minimal channel quality |
| Aggregate cost per approved outcome | `cost_period_recorded` + independently defined aggregate outcome | sourced period cost / valid aggregate denominator | period/category/currency | Finance/Analytics | no per-user attribution; source invoice/ledger required | cost/value review without surveillance |

## 9. Data-quality and reproducibility rules

1. Event absence is not automatically a negative outcome.
2. Delivery loss/schema rejection/session expiry and unknown outcome are separate quality states.
3. Deduplication follows current TSK-0498 `event_id` rules within raw retention.
4. Unknown schema versions/fields/events are rejected before durable storage.
5. Every analysis records event schema, formula/query version, release/cohort/window and source period.
6. Missing/unknown data is shown beside the metric; it is never silently imputed as success.
7. Synthetic/test data cannot enter a real-user cohort.
8. Accountless raw linkage is destroyed by the TSK-0498 R1 boundary and cannot be restored after sign-in.
9. Account/operational logs are not a backdoor analytics store.
10. KPI percentages are not emitted when the required denominator is unavailable; report counts/unknown instead.

## 10. Access and deletion

- Product analytics access is least privilege to the approved event/aggregate boundary only.
- Operational/security account events, if later approved, remain within the owning service/security boundary and do not become product analytics merely because an aggregate is desired.
- TSK-0230 deletion/revocation/account/device/DNS-removal operations remain distinct.
- Account deletion does not retroactively create a right to retain an analytics identity; analytics identity is prohibited by default.
- Aggregate deletion follows TSK-0498 current maximums and REQ-0064 retirement when the decision purpose disappears.
- Any future optional-account event with personal identifiers is blocked from processing until exact purpose/lawful-basis status/recipient/retention/deletion/access/safeguards/prohibited-use fields are approved under TSK-0230.

## 11. Change-control triggers

Reopen affected TSK-0497 proof for:

- any new/changed event/property/dimension;
- TSK-0498 event-name/schema/retention change;
- optional-account product event activation;
- persistent raw event queue/table;
- account/device/person analytics identity or cross-session linkage proposal;
- third-party analytics/session replay/advertising integration;
- DNS/domain/URL/child-activity/arbitrary-text measurement proposal;
- accountless J0/J1 lifetime/linkage change;
- material KPI formula/denominator/window change;
- new real cohort/geography/market or human-assistance measurement;
- current TSK-0230 privacy/data contract change.

## 12. ACC-0497 traceability

Current ACC-0497 is satisfied as follows:

- every currently approved event supports a named approved decision purpose — §§2 and 6;
- accountless events remain non-identifying — §3;
- optional-account events/operations use zero identifiers in product analytics by default and only minimum authorised identifiers in the owning operational/security boundary when actually required — §4;
- DNS/domain browsing history, child activity, unnecessary identity, content payload, raw secrets/tokens and invasive attribution are prohibited — §5;
- event retention/deletion/access are explicit through current TSK-0498/TSK-0230 authority and catalogue metadata — §§3, 6 and 10;
- KPI source/formula/denominator/window/owner/guardrail/action are explicit — §§7–9.

## 13. Non-inference

This is L4 measurement/KPI contract revalidation only. It does not activate telemetry, approve a datastore, approve a new optional-account event name, implement authentication/analytics, create a legal basis, authorize real-user processing, prove KPI values, process participants, publish, activate a market, launch, pass a lifecycle gate or infer any successor PASS.

**TSK-0497 current result candidate: PASS, subject to independent verification, durable evidence publication, guarded runtime reconciliation and exact GitHub read-back.**
