# TSK-0497 — Minimal Product Event and KPI Catalogue

**Task:** TSK-0497 — Define minimal product event and KPI catalogue  
**Acceptance:** ACC-0497  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 MEASUREMENT CONTRACT / TELEMETRY IMPLEMENTATION OR RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** REQ-0060/0061 + CON-0007/0008 + INT-0016/0029 + TSK-0230 + TSK-0229 + TSK-0313/0320 + TSK-0042 + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and evidence limitation

This contract defines the **smallest privacy-safe product measurement vocabulary** needed to understand accountless setup outcomes, truthful Protection Map states, self-service/support friction and removal/recovery without creating user-level behavioral history.

It does not implement telemetry, create a datastore, activate real-user measurement, authorize Experiment 1, prove KPI performance, or claim that representative parents complete or understand the journey successfully.

`RSK-0002` remains OPEN. Real-participant behavioral evidence is deferred under DEC-0050/CR-0003, so every KPI below is a definition/decision instrument only; current values are unknown unless separately evidenced by an authorized dataset.

## 2. Measurement architecture — aggregate by design

The preferred implementation model is **validate -> increment/update approved aggregate -> discard the event payload**.

Requirements:

1. No persistent raw per-user/per-journey event stream.
2. No event history or clickstream inside J0/J1.
3. No stable analytics user ID, device ID, household ID or cross-session identifier.
4. Full `journey_token` is never an analytics property, log field, dimension or join key.
5. An event may use current in-memory/J0/J1 state only long enough to validate the controlled fields and update the approved aggregate; that does not authorize retention of the source payload.
6. Raw event retention after successful aggregate commit: **zero**. The payload is discarded immediately.
7. If a later implementation proves durable event-delivery retry technically necessary, that is a material data-contract change requiring TSK-0230/privacy review before use; this contract does not pre-authorize a durable raw-event queue.
8. Approved aggregates may be retained by release/time window for reproducibility and product decisions only while justified. REQ-0064 requires retirement when unused/unjustified.
9. Dimensions must remain coarse and controlled. If a dimension combination would make a household/journey reasonably identifiable, suppress/drop the dimension rather than retain a high-cardinality record.
10. Synthetic/test events must be explicitly separated from authorized real-operation cohorts so test traffic cannot masquerade as user behavior.

## 3. Global prohibited properties and event classes

No approved event may contain or derive:

- DNS query name, URL, visited domain, top-domain list, browsing history or blocked-domain history;
- child activity, app/content/message/contact/photo/social history;
- child/parent name, email, phone, exact DOB, address, school or precise/routine location;
- IP address as analytics data;
- Apple/Google/service username or account identifier;
- IMEI, serial, advertising ID, hardware/browser fingerprint or stable device/customer ID;
- full journey token, full diagnostic ticket token, credential, secret, private key or profile payload;
- unrestricted free text, support transcript, safeguarding disclosure content or raw diagnostic payload;
- session replay, page-view trail, clickstream, dwell-time, streak, frequency/addictive-engagement metric;
- marketing/advertising profile or cross-session attribution identity;
- account/login/password-reset/dashboard event while EXC-0001 remains inactive.

A new event/property is denied by default until its purpose, exact definition, fields, prohibited fields, collection point, denominator, retention and owner are added through governed review.

## 4. Common controlled dimensions

Only the following common dimensions may be attached where the specific event row permits them:

- `release_id` — exact product/release/schema version, not a user identifier;
- `measurement_window` — governed UTC reporting window identifier;
- `cohort_class` — one of `synthetic`, `authorized_research`, `authorized_operation`; current L4 work uses definitions only and does not activate the latter two;
- `device_family` — `iphone`, `android`, `unsupported_or_unknown`;
- `platform_version_band` — coarse supported routing band or `unknown`, only where necessary;
- `dns_method` — controlled supported mechanism (`ios_doh_profile`, `android_private_dns_dot`, `not_selected`, `unsupported`);
- `state` — one of TSK-0320 S1–S6 semantics or an explicitly mapped internal state;
- `issue_class` / `severity` — controlled TSK-0042 taxonomy only;
- `reason_code` — approved coarse reason enum only, never free text or a domain/service identifier.

Do not attach every dimension to every event. Each event row below is the allowlist.

## 5. Approved event catalogue

All events are **one-shot measurement inputs to aggregates**, not retained user records.

| Event | Purpose | Exact definition / trigger | Allowed properties | Explicit prohibited properties | Collection point | Denominator relationship | Raw retention | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `journey_started` | Count eligible accountless starts | Emit once when the parent intentionally starts the accountless setup flow, after any required privacy/measurement gate permits collection | `release_id`, `measurement_window`, `cohort_class`, optional `device_family` only after known | identity, IP, token, page/referrer trail, marketing ID | Start transition | Denominator for completion/friction metrics | 0 after aggregate commit | Product Analytics |
| `journey_completed` | Measure completion of the defined journey, not protection quality | Emit once when the journey reaches its defined end/Protection Map presentation; mixed S1–S6 states are allowed | `release_id`, `measurement_window`, `cohort_class`, `device_family` | identity, token, elapsed browsing history, overall safety score | Completion transition | Numerator for journey completion rate; denominator for final-map distribution where map shown | 0 after aggregate commit | Product Analytics |
| `journey_reset_or_exit` | Identify explicit restart/exit friction without covert abandonment tracking | Emit only on an explicit reset/start-over/exit action; browser close, inactivity or disappearance is **not** inferred as an event | `release_id`, `measurement_window`, `cohort_class`, optional `device_family`, controlled `reason_code` if product explicitly offers one | free text, inferred reason, click/path history, identity | Explicit reset/exit control | Numerator for explicit reset/exit rate; started journeys denominator | 0 after aggregate commit | Product Analytics / Product |
| `dns_setup_attempted` | Count supported DNS configuration attempts | Emit once per explicit setup attempt for the currently routed supported method | `release_id`, `measurement_window`, `cohort_class`, `device_family`, `platform_version_band`, `dns_method` | profile content, IP, DNS domains, device ID | Internet/DNS setup action | Denominator for DNS verification outcome | 0 after aggregate commit | Product Analytics / Network Engineering |
| `dns_verification_result` | Measure whether current approved verification establishes DNS protection truthfully | Emit on completion of one approved verifier attempt with result `verified`, `failed`, or `uncertain`; parent confirmation cannot create `verified` | `release_id`, `measurement_window`, `cohort_class`, `device_family`, `platform_version_band`, `dns_method`, `result`=`verified|failed|uncertain`, controlled `failure_class` when applicable | test/query domain, raw DNS response, IP, token, profile payload | Approved DNS verifier boundary | Numerator classes over verification attempts; feeds Protection Map Internet state evidence | 0 after aggregate commit | Product Analytics / Network Engineering |
| `dns_removal_recovery_result` | Measure reversible removal and restoration of ordinary DNS behavior | Emit after an explicit UseSafeWeb DNS removal/recovery attempt with `removed_recovered`, `removal_failed`, or `recovery_uncertain` | `release_id`, `measurement_window`, `cohort_class`, `device_family`, `dns_method`, controlled `result`, controlled `reason_code` | ordinary DNS domains used in checks, IP, identity, prior protection history | Removal/recovery verification boundary | Denominator and numerator for recovery success; may support removal reason aggregate | 0 after aggregate commit | Product Analytics / Network Engineering / Support |
| `protection_map_presented` | Measure truthful final state distribution without a safety score | Emit once when the final/current Protection Map is presented; aggregate each layer independently | `release_id`, `measurement_window`, `cohort_class`, `device_family`, `phone_state`=S1–S6, `internet_state`=S1–S6, `services_state`=S1–S6 | overall safe score, domain history, persistent map history, identity, token | Protection Map presentation | Denominator for per-layer state distribution | 0 after aggregate commit | Product Analytics / Product |
| `support_issue_classified` | Measure ordinary support friction by controlled cause/severity | Emit when a support/self-service issue is assigned one TSK-0042 issue class and severity | `release_id`, `measurement_window`, `cohort_class`, `device_family` when relevant, `issue_class`, `severity`, controlled `root_cause_code` only if established | transcript, domain, URL, diagnostic payload, safeguarding disclosure, identity | Self-service/support classifier | Numerator for issue/blocking/unsupported incidence; support cases denominator for support KPIs | 0 after aggregate commit | Product Analytics / Support |
| `self_service_resolution_result` | Measure whether an eligible ordinary issue is resolved without human intervention | Emit once when an eligible issue reaches controlled `resolved`, `not_resolved`, or `unsupported` outcome | `release_id`, `measurement_window`, `cohort_class`, `issue_class`, `result` | identity, transcript, domain, raw diagnostics | End of eligible self-service route | Numerator/denominator for self-service resolution | 0 after aggregate commit | Product Analytics / Support |
| `filtering_false_positive_outcome` | Measure confirmed UseSafeWeb-caused false positives and resolution quality | Emit only after causality is established under TSK-0042 with `confirmed_resolved`, `confirmed_unresolved`, or `not_usesafeweb_caused` | `release_id`, `measurement_window`, `cohort_class`, controlled `result`, coarse `affected_function_class` if approved | affected domain/site/app identity, browsing history, personalized allowlist, user identity | False-positive workflow conclusion | Confirmed cases over applicable activated/verified journeys or support cases as defined by KPI | 0 after aggregate commit | Product Analytics / Network Engineering / Support |
| `exceptional_diagnostic_invoked` | Monitor how often ordinary support requires the separately governed exceptional diagnostic route | Emit only after the incident-specific diagnostic procedure is authorized; count invocation, not content | `release_id`, `measurement_window`, `cohort_class`, broad `issue_class` | incident payload, DNS/query/domain data, ticket token, identity, approver personal details | Diagnostic procedure activation | Numerator over support cases | 0 after aggregate commit; raw diagnostics follow their separate incident retention, never this event | Product Analytics / Privacy / Support |
| `privacy_security_escalation` | Count material privacy/security escalation routes without storing incident facts in analytics | Emit when TSK-0042/incident routing enters the privacy/security escalation path | `release_id`, `measurement_window`, `cohort_class`, broad controlled `incident_class` | affected personal data, secrets, logs, domain/history, narrative | Escalation route entry | Count and optional rate over support cases; incident system remains separate | 0 after aggregate commit | Privacy Engineering / Security / Product Analytics |
| `safeguarding_route_invoked` | Confirm that safeguarding routing occurs without turning disclosures into analytics | Emit only a non-identifying count when the dedicated safeguarding boundary is invoked, if the applicable legal/privacy gate permits this aggregate | `release_id`, `measurement_window`, `cohort_class` only | disclosure content, identity, age, location, narrative, outcome details | Safeguarding route boundary | Count only; no product-performance interpretation | 0 after aggregate commit | Safeguarding / Privacy / Product Analytics |
| `stale_guidance_detected` | Identify instructions that must be reviewed because current platform/service behavior no longer matches them | Emit when an owned instruction is classified stale under TSK-0042 | `release_id`, `measurement_window`, `cohort_class`, controlled `guidance_component`, optional `device_family` | user identity, affected domain/history, free text | Support/content review boundary | Numerator over support cases or reviewed instruction incidents | 0 after aggregate commit | Content / Product Analytics |

### Dormant real-human-assistance measurement

The following measurement is **defined but not active** while real-user/staffed-support authorization is absent:

- `human_assistance_summary`: aggregate count of journeys/issues requiring human intervention and aggregate active assistance minutes by controlled issue class/stage.
- No transcript, identity or free-text notes are authorized by this event definition.
- It may activate only when the applicable research/operation gate authorizes real-user support measurement.

## 6. Explicitly absent events

The following event families are intentionally **not** part of the catalogue:

- `page_viewed`, `screen_viewed`, `button_clicked`, `time_on_page`, `session_duration`, `daily_active_user`, `streak`, return-frequency or engagement-depth events;
- `dns_query`, `domain_blocked`, `domain_allowed`, `top_domain`, `category_browsed`, `child_activity` or equivalent;
- `login`, `logout`, `signup`, `password_reset`, `account_created`, `dashboard_viewed`, `device_added_to_account` while EXC-0001 is inactive;
- persistent `user_id`, analytics cookie, advertising ID, stable journey/session ID or cross-event device fingerprint;
- support transcript/disclosure/diagnostic-content events.

Their absence is a requirement, not a missing analytics feature.

## 7. KPI catalogue

No KPI below has a current observed value under this L4 task. Each calculation must distinguish synthetic, authorized research and authorized operation cohorts.

| KPI | Source events / source | Formula and denominator | Time window / release/cohort | Owner | Guardrail | Decision action |
| --- | --- | --- | --- | --- | --- | --- |
| Journey completion rate | `journey_started`, `journey_completed` | completed journeys / started journeys for the same governed release/cohort; missing completion after browser disappearance is not automatically classified as abandonment | Per governed reporting window + `release_id` + `cohort_class`; optionally coarse device family | Product Analytics / Product | Never optimize by adding surveillance or weakening required safety/privacy steps | Investigate material deterioration; route causes to UX/product/support; do not claim behavioral success until authorized real-user evidence exists |
| Explicit reset/exit rate | `journey_reset_or_exit`, `journey_started` | explicit reset-or-exit actions / started journeys | Same release/window/cohort | Product Analytics / Product | Explicit action only; no inferred abandonment from inactivity/browser close | Review route/content/friction clusters; remove unnecessary steps only when correctness/safety remains intact |
| DNS verified activation rate | `dns_setup_attempted`, `dns_verification_result` | verifier outcomes `verified` / DNS setup attempts for the same supported method/context; also report failed/uncertain separately | Release/window/cohort by supported device family + DNS method | Product Analytics / Network Engineering | Parent confirmation/profile presence never counts as verified; no queried domain retained | Investigate supported-path failures/uncertainty; do not strengthen claims to improve the metric |
| DNS verification failure/uncertainty rate | `dns_verification_result` | (`failed` + `uncertain`) / all verification results | Release/window/cohort, coarse supported context | Product Analytics / Network Engineering | S5 uncertainty remains visible; no fallback fabricated | Open compatibility/reliability/root-cause work; affected path can become Not covered if evidence requires it |
| Protection Map state distribution | `protection_map_presented` | per layer: count of each S1–S6 / maps presented | Release/window/cohort, optionally device family | Product Analytics / Product | No overall safety score; S1 and S2 never merged; mixed states preserved | Investigate high S3/S5 or unsupported patterns; do not cosmetically convert states to positive |
| Support issue incidence | `support_issue_classified`, `journey_started` or applicable completed/activated denominator | classified ordinary support issues / explicitly stated applicable journey denominator; denominator choice must be stored with the aggregate definition | Release/window/cohort + broad issue class | Product Analytics / Support | No transcript/domain/history; multiple issues must not be silently treated as unique users | Prioritize repeated controlled issue classes for product/content fixes |
| Self-service resolution rate | `self_service_resolution_result` | `resolved` / eligible ordinary self-service issues | Release/window/cohort + issue class | Product Analytics / Support | Unsupported cases reported separately; no hidden human completion | Improve product/help for repeated unresolved classes; route EXC-0008 if ordinary issues cannot be productized safely |
| Blocking issue rate | `support_issue_classified` | severity S2 blocking issues / applicable journeys (or support cases when explicitly labelled as support-case rate) | Release/window/cohort | Product Analytics / Support | Denominator label mandatory; no false completion while blocked | Investigate highest-volume blocking classes; pause affected route if safety/reliability warrants |
| Unsupported/conflict rate | `support_issue_classified` and/or final Protection Map states | S4/S5 applicable outcomes / applicable journeys/maps | Release/window/cohort + coarse device/network class only where permitted | Product Analytics / Product / Network Engineering | Unsupported and uncertain remain distinct where decision needs differ | Narrow/support/research platform combinations based on evidence; never invent coexistence |
| DNS removal/recovery success rate | `dns_removal_recovery_result` | `removed_recovered` / all removal/recovery attempts | Release/window/cohort + device family/DNS method | Product Analytics / Network Engineering / Support | Neutral/synthetic recovery checks only; recovery is not UseSafeWeb protection evidence | Fix removal/recovery failures before relying on that platform path |
| Confirmed false-positive incidence | `filtering_false_positive_outcome` | confirmed UseSafeWeb-caused false-positive cases / applicable activated or verified journeys; support-case rate may be reported separately with explicit denominator | Release/window/cohort | Product Analytics / Network Engineering | Never retain affected domain as metric data; never solve by disabling whole baseline | Review filter/list/exception policy and regression test any correction |
| Exceptional diagnostic invocation rate | `exceptional_diagnostic_invoked`, support cases | approved diagnostic invocations / support cases | Release/window/cohort + broad issue class | Product Analytics / Privacy / Support | Invocation count only; diagnostic content stays separate/time-boxed | Reduce recurring diagnostic need through safer product observability/root-cause fixes |
| Privacy/security escalation count/rate | `privacy_security_escalation` | count per window; optional rate = escalations / support cases with denominator explicit | Release/window/cohort + broad incident class | Privacy Engineering / Security | Analytics never stores incident-sensitive facts | Trigger incident/control review; metric cannot close an incident |
| Safeguarding route count | `safeguarding_route_invoked` | non-identifying count only | Reporting window/release/cohort where collection is authorized | Safeguarding / Privacy | No disclosure/outcome data; not a product-success KPI | Check routing/process readiness only; safeguarding case decisions remain outside analytics |
| Stale-guidance incidence | `stale_guidance_detected`, support cases | stale-guidance detections / support cases (or count if denominator unavailable) | Release/window/cohort + controlled guidance component | Content / Product Analytics | No free-text user case retained | Revalidate/update or withdraw stale instruction before continuing to present it as current |
| Human-assistance incidence — dormant | Authorized research/operation human-assistance summary | journeys/issues requiring human help / eligible journeys/issues | Only an explicitly authorized real-user research/operation cohort | Product Research / Support / Product Analytics | Not populated from synthetic work; no transcript/identity | Test EXC-0008/support sustainability assumptions; do not claim current burden while dormant |
| Active assistance minutes — dormant | Authorized human-assistance summary | total active human-assistance minutes / assisted case, also distribution by controlled class/stage | Only authorized real-user cohort | Product Research / Support | Structured duration only; no transcript | Identify productizable support causes and sustainability risk; no current value inferred |

## 8. KPI reproducibility and denominator rules

1. Every aggregate must store its `release_id`, measurement window, cohort class, exact numerator definition and exact denominator definition.
2. A rate with an unavailable denominator is reported as a **count**, not a fabricated percentage.
3. Missing data, instrumentation failure and “event did not occur” are distinct states.
4. Synthetic test data never contributes to real-user performance metrics.
5. Parent confirmation and technical verification are distinct numerator classes.
6. A journey can complete with S3/S4/S5/S6; completion is not equivalent to protection success.
7. A support case may generate several controlled issue categories; “unique users affected” is not calculated without an independently authorized identity-safe method.
8. Release/schema changes that alter event semantics require a versioned break or explicit migration rule before combining time series.
9. A KPI must not be redefined after seeing results merely to improve appearance; changes are versioned and prior periods remain reproducible.

## 9. Aggregate storage and access contract

Approved aggregate records may contain only:

- metric/event aggregate name and schema version;
- UTC reporting window;
- release/cohort class;
- explicitly approved coarse dimensions;
- integer counts, sums or derived rates with numerator/denominator values;
- quality marker such as `complete`, `partial`, `instrumentation_error`, `synthetic_only`;
- decision/evidence version reference.

They must not contain a source event payload or user/journey identifier.

Access is limited to the product/analytics/engineering roles necessary for the stated decision purpose. Export/public reporting must be further aggregated where low counts or dimension combinations could create re-identification risk.

## 10. Collection and retirement gates

Before any event is implemented:

1. its event ID/definition/properties must exactly match this contract or a governed successor;
2. implementation must prove no additional properties are emitted/stored;
3. raw payload is discarded after aggregate update;
4. storage inspection proves no user-level event table/log/backup exists;
5. applicable privacy/legal/participant/release gate permits the cohort being measured;
6. synthetic and real cohorts are technically separated;
7. event owner and KPI consumer still need the event.

Retire an event/aggregate when its decision purpose disappears, its KPI is unused/unactionable, equivalent lower-data evidence exists, or real evidence shows the measurement cost/privacy risk outweighs value. Retirement includes stopping collection and deleting obsolete raw/transient implementation artifacts; governed aggregate evidence may remain only where still required for reproducibility/decisions.

## 11. Change triggers

Reopen TSK-0497 and TSK-0230 impact review before:

- adding any event/property/dimension;
- adding a persistent raw-event queue or event table;
- introducing user/session/device analytics identity;
- adding account/login/dashboard telemetry;
- measuring DNS/domain/URL/child activity;
- adding analytics/session-replay/advertising vendor;
- linking product events to support, DNS, marketing or identity records;
- introducing J1 persistence or changing its schema/TTL;
- activating real participants/operation in a new geography/cohort;
- changing a KPI denominator/decision use materially;
- collecting a dormant human-assistance metric;
- using low-count/high-cardinality aggregates that may become identifying.

## 12. Testable implementation assertions

A later implementation/QA/privacy suite must prove at least:

1. only approved event IDs can be emitted;
2. each event accepts only its allowlisted properties/enums;
3. prohibited properties are rejected, not silently ignored into secondary logs;
4. no DNS/domain/URL/child-activity event exists;
5. no login/account/dashboard event exists while EXC-0001 is inactive;
6. no persistent user/session/device analytics ID exists;
7. full journey tokens never appear in telemetry/logs;
8. raw event payload is absent after aggregate commit;
9. no durable raw-event table/queue/backup exists under this contract;
10. synthetic events cannot enter authorized-research/operation aggregates;
11. S1 verified cannot be generated from parent-confirmed state;
12. Protection Map metrics preserve S1–S6 per layer and no overall safety score;
13. browser close/inactivity is not fabricated as an exit/abandonment event;
14. support analytics contains controlled codes only, no transcripts/free text;
15. false-positive metrics contain no affected domain/site/app identifier;
16. exceptional-diagnostic event contains no diagnostic payload;
17. safeguarding event contains no disclosure/outcome details;
18. every KPI reproduces from stored aggregate numerator/denominator/version metadata;
19. missing/partial/instrumentation-error data is distinguishable from zero;
20. unused/unjustified events can be disabled and retired without breaking the product journey.

## 13. ACC-0497 traceability

ACC-0497 requires every approved event to have purpose, exact definition, properties, prohibited fields, collection point, denominator, retention and owner; it permits minimal accountless journey/device configuration/Protection Map/self-service/support measurement; it requires login/account/dashboard events to remain absent unless EXC-0001 activates; and prohibits DNS/domain history, visited-domain and child-activity events.

- §5 supplies every required metadata dimension for each approved event.
- §7 defines the KPI catalogue and REQ-0060 source/formula/denominator/window/release/cohort/owner/guardrail/decision action dimensions.
- §§2–3 and §9 define aggregate-by-design storage and zero raw-event retention.
- §6 makes account/login/dashboard and browsing/activity event absence explicit.
- §§8, 10–12 make reproducibility, implementation inspection, retirement and future change testable.
- `RSK-0002` and all legal/participant/build/release gates remain open/unmodified.

**TSK-0497 result: PASS candidate for provisional internal L4 measurement-contract definition only, subject to independent verification, GitHub read-back and runtime reconciliation. No telemetry implementation or real-user performance result is claimed.**
