# TSK-0498 — Privacy-Safe Decision-Linked Event Contract

**Task:** TSK-0498 — Define only decision-linked accountless journey, protection-state, self-service, reliability, channel, and cost events  
**Acceptance:** ACC-0498 / VER-0498 / EVD-0498  
**Lifecycle:** L5 — Architecture, Security, Privacy & Operations  
**Version:** 1.0.1
**Date:** 2026-09-01  
**Status:** CURRENT L5 MEASUREMENT CONTRACT CANDIDATE; implementation and downstream PASS are not inferred  
**Authority:** current owner-frozen CR-0008 modular planning system; current TSK-0229 accountless/no-linkage model; current TSK-0320 protection-state model; REQ-0060/0061/0062; CON-0007/0008/0009; RSK-0049; INT-0016.  

## 1. Decision questions — telemetry exists only to answer these

1. **Journey:** Where do parents start, progress, fail, abandon or complete the accountless core journey, by release/cohort and supported route?
2. **Protection truth:** What evidence-backed Protection Map states are actually produced, and how often does verification resolve to verified, configured-only, action-needed, not-covered, uncertain/error or removed?
3. **Self-service:** Which approved self-service routes are opened and whether the parent reports resolution, no resolution or escalation?
4. **Reliability:** Are the public web/setup and verification/DNS health surfaces available and behaving within their accepted operational thresholds?
5. **Channel:** Which explicitly tagged privacy-minimal acquisition/channel source leads to a completed/qualified accountless journey within the same short-lived journey session?
6. **Cost:** What sourced operating/channel cost belongs to each decision period/category so later KPI calculations can reproduce aggregate cost-per-outcome without user-level financial attribution?

No event may be introduced unless it answers one of these six questions or is required to prove telemetry quality for them. Unused/unjustified events are retired.

## 2. Hard privacy boundary

The event system **must not collect or derive**:

- DNS questions, requested/visited domains, URLs, page contents, browsing history, top domains, search terms or child activity;
- identifiable per-client DNS statistics, client IP as an analytics field, MAC/device hardware IDs, advertising IDs or fingerprinting signals;
- child name/account/profile, messages, contacts, photos, location, social content or any surveillance-like data;
- parent email/account ID/provider subject as an analytics join key;
- free-text support/search/query contents;
- full referrer URLs, arbitrary campaign strings or arbitrary error text;
- secrets, tokens, session cookies, credentials or authorization headers.

**Persistent identity linkage is prohibited.** Optional account identity/device ownership remains operational authorization/persistence context outside this analytics contract and must never be joined into accountless event history. No analytics identifier survives the accountless journey TTL.

## 3. Common event envelope

Every raw event uses an allowlisted schema with these common fields only:

| Field | Rule |
|---|---|
| `event_name` | Stable allowlisted name from this contract. |
| `schema_version` | Exact event-schema version. |
| `event_id` | Random deduplication ID; raw-only; deleted with raw event. Never derived from a person/device/account. |
| `occurred_at` | UTC timestamp for ordering/windowing. |
| `release_id` | Bounded deployed release/build identifier. |
| `surface` | Bounded enum such as `public_web`, `setup_web`, `verification`, `self_service`, `synthetic_probe`, `internal_finance`. |
| `journey_session_id` | Optional random first-party accountless correlation ID used only for journey/channel/self-service correlation; never account/device-derived; maximum life and raw retention **24 hours**; never persisted into aggregate output. |

No event accepts arbitrary extra properties. Unknown fields cause rejection/quarantine and privacy review, not silent storage.

## 4. Retention model

### R1 — Accountless raw event window
Journey, Protection Map, self-service and channel raw events: **maximum 24 hours from the originating journey start**, aligned to the approved anonymous J1 upper bound. The raw record, `event_id`, and `journey_session_id` are then deleted. Sign-in cannot extend this lifetime.

### R2 — Non-linkable aggregates
After aggregation, retain only non-linkable counters by bounded dimensions (`event_name`, approved outcome/state/reason class, approved route/channel class, release/cohort/time bucket). Maximum retention: **13 months**, then delete unless a later approved task establishes a different justified period. Aggregates contain no session/account/device/person identifier and cannot reconstruct a journey.

### R3 — Synthetic reliability telemetry
Synthetic probe events contain no user/client identity and may be retained raw for **30 days** for incident/reliability investigation; non-linkable aggregates may be retained for **13 months**.

### R4 — Cost analytics projection
The measurement copy of sourced cost records is retained for **13 months** for Year-1 decision reproduction. Authoritative accounting/finance-source retention is outside this analytics contract and is not changed here.

Retention is maximum, not minimum. Early deletion is allowed when no longer required for the decision/evidence purpose.

## 5. Approved event catalogue

### A. Accountless journey events

#### `journey_started`
- **Purpose:** denominator for accountless starts and route-level completion/abandonment analysis.
- **Event fields:** common envelope + `route_id` (approved bounded route), `platform_class` (approved coarse supported platform family only), `locale_code` (approved supported locale only), `channel_source_class` if already present from an approved first-party channel entry.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / Product.
- **Denominator:** count of valid deduplicated `journey_started` events in the selected release/cohort/window. Missing/blocked telemetry must be reported separately and never guessed.

#### `journey_step_entered`
- **Purpose:** denominator for each decision-critical setup step and detection of where progression stops.
- **Event fields:** common envelope + `step_id` from frozen bounded step catalogue + `route_id`.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / UX.
- **Denominator:** deduplicated entries to that exact `step_id`; never total page views.

#### `journey_step_outcome`
- **Purpose:** quantify success/failure/skip/unsupported/retry at decision-critical steps.
- **Event fields:** common envelope + `step_id` + `outcome` (`completed`, `failed`, `skipped`, `unsupported`, `retry`) + bounded `reason_code` + `route_id`.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / UX.
- **Denominator:** corresponding valid `journey_step_entered` events for the same step/release/cohort/window. An entered step with no outcome before session expiry is **missing/abandoned**, not silently classified as failure.

#### `journey_completed`
- **Purpose:** numerator for completion of the complete accountless core journey.
- **Event fields:** common envelope + `route_id` + `completion_variant` from approved bounded enum.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / Product.
- **Denominator:** valid `journey_started` events for the same release/cohort/window. Completion does **not** imply every protection layer is verified.

### B. Protection-state events

#### `protection_state_evaluated`
- **Purpose:** measure the truthful Protection Map distribution and detect optimistic-state drift.
- **Event fields:** common envelope + `layer_id` (bounded product layer, not domain) + `state` exactly one of `protected_verified`, `configured_parent_confirmed`, `action_needed`, `not_covered`, `uncertain_error`, `removed` + bounded `reason_code` from the TSK-0320 contract + `verifier_version` where technical verification was attempted + `copy_version`.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / Product / Privacy Engineering.
- **Denominator:** all valid evaluations for the applicable layer/release/cohort/window; state-specific rates must state this denominator explicitly. `configured_parent_confirmed` is never counted as `protected_verified`.

#### `protection_verification_outcome`
- **Purpose:** distinguish technical verification success, negative result and indeterminate/error without collecting DNS activity.
- **Event fields:** common envelope + `layer_id` + `verifier_id`/`verifier_version` + `result` (`positive`, `negative`, `indeterminate`, `error`) + bounded `reason_code` + `duration_bucket_ms` from a fixed bucket set.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / Network Engineering.
- **Denominator:** valid technical verification attempts for the same verifier/scope class/release/window. Parent/configuration confirmation does not create this event and cannot be represented as a positive result.

### C. Self-service events

#### `self_service_opened`
- **Purpose:** identify which approved troubleshooting/recovery topics are needed.
- **Event fields:** common envelope + `topic_id` from an approved bounded catalogue + `entry_surface` + optional bounded `protection_state_at_entry`.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / Customer Experience.
- **Denominator:** valid accountless journey sessions in the selected window for usage rate; for topic outcome rate, the denominator is opens for that exact topic. No search text/free text is recorded.

#### `self_service_outcome`
- **Purpose:** determine whether an opened self-service route was reported resolved, unresolved, abandoned or escalated.
- **Event fields:** common envelope + `topic_id` + `outcome` (`resolved_reported`, `unresolved_reported`, `escalated`, `abandoned`, `unknown`) + bounded `reason_code` where defined.
- **Retention:** R1 raw; R2 aggregate.
- **Owner:** Product Analytics / Customer Experience.
- **Denominator:** corresponding valid `self_service_opened` events. Absence of an outcome is reported as missing/abandoned only after session expiry and is never called resolved.

### D. Reliability events

#### `synthetic_service_probe_result`
- **Purpose:** answer whether approved public/setup/verification/DNS health surfaces are operational without observing user traffic.
- **Event fields:** common envelope without `journey_session_id` + `component` from fixed allowlist + `probe_region` from controlled deployment list + `result` (`success`, `failure`, `timeout`, `degraded`) + bounded `error_class` + `duration_bucket_ms` + `probe_version`.
- **Retention:** R3.
- **Owner:** SRE / Operations.
- **Denominator:** scheduled probe opportunities for the exact component/region/version/window; missing probe executions are counted separately as telemetry gaps, not service successes.

#### `recovery_operation_outcome`
- **Purpose:** measure reliability/recovery actions and whether a verified service state was restored.
- **Event fields:** common envelope without `journey_session_id` + `operation_type` from bounded runbook catalogue + `result` (`success`, `failed`, `partial`, `rolled_back`) + bounded `failure_class` + `duration_bucket_ms` + `runbook_version`.
- **Retention:** R3.
- **Owner:** SRE / Operations.
- **Denominator:** initiated governed recovery operations of the same type/window. Contains no client/user/domain data.

### E. Channel events

#### `channel_entry`
- **Purpose:** compare privacy-minimal qualified accountless journey outcomes by approved channel/source.
- **Event fields:** common envelope + `source_class` from fixed enum (`direct`, `organic_search`, `school_partner`, `referral`, `owned`, `approved_test`, `unknown`) + optional owner-issued bounded `campaign_key`/`partner_key`; no full referrer URL or arbitrary UTM value.
- **Retention:** R1 raw; R2 aggregate. The source may be linked to journey completion only within the same 24-hour `journey_session_id`; that linkage is destroyed at aggregation.
- **Owner:** Product Analytics / Growth.
- **Denominator:** valid `channel_entry` events or valid accountless journey starts attributed within the same session, depending on the KPI; the exact KPI must name which. Reach/impressions are never substituted for qualified journey value.

### F. Cost events

#### `cost_period_recorded`
- **Purpose:** provide reproducible aggregate cost input for operating/channel/unit-economics decisions without per-user attribution.
- **Event fields:** common envelope with `surface=internal_finance` and no journey ID + `period_id` + `cost_category` from bounded catalogue + `provider_or_source_class` + `currency` + `amount_minor_units` + `source_reference` to the authoritative invoice/ledger/evidence + `cost_model_version`.
- **Retention:** R4.
- **Owner:** Project Owner / Finance / Product Analytics.
- **Denominator:** the defined decision period. Any later cost-per-outcome KPI must divide this sourced aggregate by an independently specified aggregate outcome denominator; this event is never joined to a person/session/device/account.

## 6. Explicitly prohibited events and fields

The following are **not approved event concepts**, even if technically easy to collect:

- `domain_visited`, `dns_query`, `top_domain`, `blocked_domain_for_child`, `child_activity`, `time_on_site_child`, `message_viewed`, `location_seen`;
- full URL/referrer, DNS qname, raw IP, account ID/email/provider subject, child ID/name, device serial/MAC, ad ID/fingerprint, precise location, contact/photo/message/social data;
- arbitrary support text, search text, error stack/body/request body in product analytics;
- engagement loops such as streaks, compulsive-return metrics, attention-time optimization or behavioral-ad targeting;
- cross-session/cross-device identity graph, accountless-to-account historical join, or account sign-in used to extend an accountless analytics identifier.

An implementation attempting to emit an unknown event/field fails the schema contract and must be corrected before acceptance.

## 7. KPI/denominator and data-quality rules

1. Every KPI consuming these events must define **source, formula, numerator, denominator, time window, release/cohort, owner, guardrail and decision action** before use.
2. Event absence is not automatically an observed negative outcome. Delivery loss, blocked analytics, session expiry and unknown outcome are explicit missing-data classes.
3. Deduplicate by `event_id` within raw retention; duplicates never increase numerator or denominator.
4. Reject malformed schema versions/unknown fields; record only aggregate telemetry-health counts for rejected events, never the rejected payload.
5. Clock/window calculations use server-received time as a quality cross-check; material client-clock skew is an uncertainty flag.
6. Every analysis records event-schema version, copy/verifier version where relevant, query/formula version and source period.
7. Reproducibility requires the same approved aggregate inputs/formula to reproduce the published result; if not, the affected KPI/gate is invalidated until corrected.
8. Missing data and uncertainty are shown beside the metric; they are never silently imputed as success.
9. Accountless session correlation is strictly ephemeral. At R1 expiry, aggregate first and delete raw linkage; no later re-identification/reconstruction path is approved.
10. A telemetry-quality event may describe schema/delivery health only at aggregate/system level; it may not smuggle prohibited user fields into diagnostics.

## 8. Privacy and observability separation

Product analytics answers the six decision questions above. Operational logs/traces are governed separately and must not be treated as a backdoor analytics store. Structured operational telemetry may use short-lived request correlation required for incident diagnosis, but it must obey its own minimisation/retention/access rules and may not be joined to accountless product analytics or contain prohibited browsing/account/child data.

Reliability is preferentially measured with synthetic probes and aggregate service signals rather than user DNS/request history.

## 9. Change control and retirement

Any request for a new event/property must provide: decision question, exact field allowlist, denominator use, retention, owner, privacy classification, and why existing signals cannot answer it. Expansion involving identity, browsing/activity, child data, arbitrary text or surveillance-like behavior is outside this task and must fail closed pending explicit higher-authority scope/privacy review.

Monthly data-minimisation review must identify unused events/fields/aggregates. An event or field unused for an approved decision/evidence need is disabled and its retained data deleted according to the applicable retention rule.

## 10. Deterministic acceptance assertions

A compliant implementation/test suite must prove at least:

1. Only the twelve event names in this contract are accepted.
2. Unknown fields/events are rejected before durable storage.
3. No approved schema contains domain/URL/DNS-query/child-activity fields.
4. No approved schema contains account/person/device persistent identity or an account join key.
5. `journey_session_id` is random, account/device-independent, maximum 24 hours, and absent from retained aggregates.
6. Sign-in never extends or links accountless event history.
7. Raw journey/protection/self-service/channel records are deleted by the 24-hour bound.
8. Product aggregates are non-linkable and deleted by the 13-month bound.
9. Synthetic reliability raw data contains no user/client identity and expires by 30 days.
10. Parent/configuration confirmation never appears as positive technical verification; protection events preserve all six TSK-0320 states exactly.
11. Every event has purpose, exact fields, retention, owner and denominator semantics.
12. Every KPI reports missing/unknown data and names its source/formula/denominator/window/release-or-cohort/owner/guardrail/action before decision use.
13. Cost records remain aggregate/period based and are never joined to a user/session/device/account.
14. Channel attribution uses only controlled source/campaign/partner codes, no full referrer/arbitrary URL, and loses session linkage after aggregation.
15. Self-service analytics store no free text/search text.
16. Reliability uses synthetic/system signals rather than DNS/user browsing history.
17. Duplicate events cannot inflate counts.
18. Analysis reproduction failure invalidates the affected decision evidence until corrected.
19. Unused/unjustified events/fields are retired and deleted under the retention contract.
20. Literal secrets/tokens/credentials are absent from event schemas and evidence.

## 11. ACC-0498 disposition

`ACC-0498` requires every event to have purpose, fields, retention, owner and denominator, with no domains, browsing, child activity, addictive engagement or persistent identity linkage.

This contract limits measurement to decision-linked accountless journey, protection-state, self-service, synthetic reliability/recovery, privacy-minimal channel, and aggregate cost events; defines an exact allowlist, field/retention/owner/denominator rules, missing-data/reproducibility controls, strict prohibited-data rules, ephemeral-only accountless correlation, aggregate-only long retention and deterministic implementation assertions.

**TSK-0498 result: PASS candidate pending independent verification, GitHub read-back, full master-plan validation and durable runtime reconciliation.**
