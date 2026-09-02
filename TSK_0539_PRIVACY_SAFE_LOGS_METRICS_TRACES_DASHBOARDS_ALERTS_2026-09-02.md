# TSK-0539 — Privacy-Safe Logs, Metrics, Traces, Dashboards and Alerts

**Version:** 1.0.0  
**Date:** 2026-09-02  
**Lifecycle / priority:** L5 / MEDIUM  
**Task:** TSK-0539 — Design privacy-safe logs, metrics, traces, dashboards, and alerts  
**Acceptance / verification / evidence:** ACC-0539 / VER-0539 / EVD-0539  
**Hard dependencies:** TSK-0538; TSK-0239  
**Action authority:** A3 / AUTO_ALLOWED  
**Current authority:** DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008; DEC-0056/CR-0009

## 1. Decision and design boundary

This artifact defines the **logical observability contract** for the current dual-mode Version-1 architecture: accountless core plus optional parent account/session, minimum parent/device ownership persistence and lightweight dashboard/device management.

It consumes the current accepted reliability contract and security/privacy control matrix:

- `TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md`, blob `44c9c299465e821e2ffd84a54b77e3e615d61925`;
- `TSK_0239_SECURITY_PRIVACY_CONTROL_IMPLEMENTATION_VERIFICATION_MATRIX_2026-09-02.md`, blob `674c21b4c169da4fb496617164ad68cfc6527fb4`, accepted by GitHub Actions run `33621524294`.

The design is vendor-neutral. It does **not** select or purchase a collector, APM, metrics backend, log backend, alerting vendor, HA topology or paid service. OpenTelemetry is only the preferred neutral vocabulary when cross-component tracing/instrumentation is justified. Physical repository/config paths are assigned by TSK-0048 and implemented/tested in L6/L7.

Under DEC-0056/CR-0009, legal/regulatory/compliance conclusions remain owner-external/not AI-verified. This task still fully owns the technical privacy engineering boundary: minimised fields, no-history controls, bounded retention, access, cardinality, alert payloads and implementation verification.

## 2. Operational questions every signal must answer

A signal is permitted only if it answers at least one of these bounded questions:

**Core / DNS**

1. Can supported clients reach the approved DoH/DoT endpoints with valid TLS and correct controlled filtering behavior?
2. Is the complete accountless start → setup → verification → Protection Map → removal/recovery path working without login?
3. Has DNS/service/configuration/network drift invalidated a current protection claim?

**Optional account / ownership**

4. Can a parent establish/refresh a valid optional session while the accountless core remains independent?
5. Can an authenticated parent read only their own account/device state?
6. Do device/register/update/unlink/delete/revoke operations reach one ownership-correct truthful terminal state?
7. During provider/datastore failure, does account authority fail closed while accountless setup/verify/remove remains usable?
8. Did an ambiguous consequential mutation reconcile before retry or success presentation?

**Security / privacy / recovery**

9. Is a High/Critical control currently violating authz, ClientID isolation, secret, no-history, supply-chain, DNS abuse, protection-truth or recovery invariants?
10. Can the current service/configuration be restored inside the accepted recovery objective without restoring prohibited history or revoked authority?
11. What bounded release/configuration change preceded a regression?
12. Is telemetry itself missing, leaking, over-retaining or becoming high-cardinality?

Telemetry that answers none of these questions is prohibited noise.

## 3. Telemetry privacy classes and retention

The design uses four explicit data classes. Implementations may retain **less**, never more, without a new accepted change.

| Class | Permitted content | Maximum retention | Access | Hard exclusions |
|---|---|---:|---|---|
| `R0_FORBIDDEN` | DNS/query/domain/URL history; request/response bodies; credentials; tokens; cookies; Firebase UID/provider subject; email; raw IP; raw ClientID; device/account/user identity; free text | `0` — do not collect | none | must be rejected/redacted before telemetry emission |
| `R1_DIAGNOSTIC` | structured bounded operational events; random request/correlation ID; trace/span IDs; route template; operation/dependency/outcome class; retry count; duration; release/config version | `<=24h` | SRE + Security, least privilege | no persistent identity linkage; correlation IDs are diagnostic only and expire with the record |
| `R2_OPERATIONAL_AGGREGATE` | bounded metrics, histograms, synthetic probe outcomes, alert-state aggregates with no identifiers | `<=30d` | SRE + QA + Security read access as needed | no identity, raw URL, DNS/domain/query, ClientID, free text or request ID labels |
| `R3_ACCEPTANCE_EVIDENCE` | release/test/run metadata, aggregate pass/fail result, artifact/config version/hash, verifier/run reference | project evidence retention | governed project evidence readers | never embed raw R0/R1 telemetry content in durable evidence |

Retention clocks are based on ingestion time. Expiry must be automatic. A telemetry backend that cannot enforce these limits is not acceptable without a specific evidence-backed alternative. Backup/export behavior must preserve the same class and expiry; `R0_FORBIDDEN` never becomes recoverable data.

## 4. Field and cardinality contract

### 4.1 Structured operational log allowlist

Permitted fields are limited to:

- `event` — stable allowlisted event name;
- `timestamp`;
- `severity` — `debug|info|warn|error`;
- `request_id` / `correlation_id` — random diagnostic ID, R1 only;
- `trace_id` / `span_id` — only when tracing is enabled, R1 only;
- `service` — bounded service enum;
- `route_template` — normalized template, never raw URL;
- `operation_class` — bounded enum;
- `dependency` — `auth_provider|datastore|adguard_control|protection_verify|dns_upstream|none` or later accepted fixed enum;
- `outcome_class` — bounded enum such as `success|rejected|timeout|dependency_error|ambiguous|reconciled|instrumentation_error`;
- `error_class` — stable bounded machine class, never free-text exception content;
- `status_class` — `2xx|3xx|4xx|5xx|none`;
- `attempt` / `retry_count` / `reconciliation_state` — bounded values;
- `duration_ms`;
- `release_id` / `config_version` — non-secret bounded version identifiers;
- `platform_family` only where a supported-device distinction is operationally necessary and remains a fixed low-cardinality enum.

Unknown fields fail telemetry schema validation; they are not silently accepted.

### 4.2 Explicitly prohibited fields

Never emit to logs, metrics, traces, dashboards or alert payloads:

- DNS question/domain/query data, browsing/activity history or top-domain data;
- raw URL, query string, Host/Referer values containing user-controlled destinations, request/response body or arbitrary headers;
- parent/user/account ID, email, phone, Firebase UID/provider subject or child identity;
- IP address, device fingerprint, device ID, raw AdGuard `ClientID`, MAC/hostname;
- password, token, cookie, authorization header, API key, private key, provider credential or AdGuard administrative credential;
- free-text support input, exception string/stack carrying user data, arbitrary third-party response body;
- persistent analytics identifier or linkage between anonymous accountless state and later sign-in.

### 4.3 Metric-label allowlist

Metric labels must come from small fixed enums only:

- `journey`;
- `mode=core|account_only|dependency_failure`;
- `route_template` from a reviewed finite route table;
- `operation_class`;
- `dependency`;
- `outcome_class`;
- `status_class`;
- `transport=doh|dot` where relevant;
- `platform_family` only for a finite supported-device matrix.

Never use request/correlation ID, trace/span ID, identity, ClientID, raw URL, DNS/domain/query, error text or timestamp as a metric label. CI must fail when a metric definition introduces an unbounded label source.

## 5. Stable operational event catalogue

These are **operational diagnostic events**, not product analytics. They do not replace the accepted TSK-0498 decision-linked product event contract.

| Event | Purpose | Required bounded fields | Severity | Retention |
|---|---|---|---|---|
| `ops_http_request_outcome` | locate a specific failed/degraded normalized route request | request_id, route_template, mode, status_class, outcome_class, duration_ms, release_id | info/warn/error by outcome | R1 |
| `ops_dependency_call_outcome` | explain auth/datastore/AdGuard/verify/upstream dependency failure | request_id, dependency, operation_class, outcome_class, error_class, duration_ms, attempt | warn/error on failure | R1 |
| `ops_session_operation_outcome` | diagnose establish/refresh/revoke/logout failure without identity | request_id, operation_class, outcome_class, error_class, duration_ms | info/warn/error | R1 |
| `ops_authorization_denied` | detect bounded authorization/IDOR pressure without target identity | request_id, operation_class, reason_class, route_template | warn | R1 |
| `ops_device_mutation_outcome` | diagnose ownership/device/ClientID lifecycle terminal state | request_id, operation_class, outcome_class, reconciliation_state, attempt | info/warn/error | R1 |
| `ops_reconciliation_outcome` | prove ambiguous effects were classified/reconciled before replay | request_id, operation_class, dependency, reconciliation_state, attempt, outcome_class | warn/error until resolved | R1 |
| `ops_protection_verification_outcome` | diagnose technical protection proof without DNS/domain/device identity | request_id, transport/platform_family if bounded, outcome_class, error_class, config_version | info/warn/error | R1 |
| `ops_synthetic_probe_outcome` | distinguish target health from probe/instrumentation health | journey, mode, outcome_class, error_class, duration_ms, release_id | info/warn/error | R1 raw; R2 aggregate |
| `ops_recovery_operation_outcome` | verify recovery/rollback step and invariant result | operation_class, outcome_class, error_class, duration_ms, release_id, config_version | info/warn/error | R1 raw; R3 result only |
| `ops_security_control_violation` | emit only a bounded confirmed control-class violation | control_class, outcome_class, route_template or dependency if applicable, release_id | error | R1; R3 incident result only |
| `ops_telemetry_guard_violation` | detect unknown field, forbidden field, cardinality/retention/access drift | guard_class, signal_class, outcome_class, release_id | error | R1; R3 result only |

Production `debug` remains off by default. Enabling diagnostic detail must be time-boxed, field-allowlisted and unable to enable R0 collection.

## 6. Metric catalogue

All latency metrics are histograms. Operational decisions use p50/p95/p99; no average-only latency gate is permitted.

| Metric family | Type | Bounded labels | Operational question |
|---|---|---|---|
| `synthetic_probe_total` | counter | journey, mode, outcome_class, transport/platform_family when bounded | are critical synthetic journeys succeeding? |
| `synthetic_probe_duration_seconds` | histogram | journey, mode, transport/platform_family when bounded | are critical synthetic journeys slow? |
| `http_requests_total` | counter | route_template, mode, status_class, outcome_class | where are user-facing errors occurring? |
| `http_request_duration_seconds` | histogram | route_template, mode, status_class | which normalized routes are slow? |
| `dependency_requests_total` | counter | dependency, operation_class, outcome_class | which external/internal dependency is failing? |
| `dependency_duration_seconds` | histogram | dependency, operation_class, outcome_class | which dependency is slow? |
| `authorization_denials_total` | counter | operation_class, reason_class | is authorization denial/abuse changing without identity tracking? |
| `mutation_terminal_outcomes_total` | counter | operation_class, outcome_class | are consequential mutations reaching truthful terminal state? |
| `reconciliation_pending` | gauge | dependency, operation_class | are ambiguous mutations awaiting reconciliation? |
| `reconciliation_outcomes_total` | counter | dependency, operation_class, outcome_class | do reconciliation paths converge safely? |
| `protection_verification_total` | counter | mode, transport/platform_family where bounded, outcome_class | is protection technical verification succeeding truthfully? |
| `tls_valid` | gauge 0/1 | transport | is approved TLS currently valid? |
| `tls_days_remaining` | gauge | transport | is certificate renewal becoming actionable? |
| `dns_correctness_total` | counter | transport, outcome_class | do controlled allow/block synthetic checks remain correct? |
| `runtime_resource_utilization` | gauge | resource_class | is host/runtime utilization elevated? dashboard only unless user symptom exists |
| `runtime_resource_saturation` | gauge | resource_class | is host/runtime capacity saturated? |
| `runtime_resource_errors_total` | counter | resource_class, outcome_class | are resource errors increasing? |
| `telemetry_signal_present` | gauge 0/1 | signal_class, journey | is a required telemetry source blind/missing? |
| `telemetry_schema_rejections_total` | counter | signal_class, guard_class | is instrumentation trying to emit forbidden/unknown/high-cardinality data? |

## 7. SLI → signal / collection / retention / alert / runbook matrix

Each current TSK-0538 SLI is mapped below. `PAGE`/`TICKET` thresholds are inherited from the current TSK-0538 alert contract; an SLI that is not yet implemented remains `inactive/not_applicable_to_runtime`, never green by absence.

| SLI | Signals | Logical collection point | Fields / labels | Retention | Access | Alert threshold | Runbook | Privacy review |
|---|---|---|---|---|---|---|---|---|
| DoH availability | synthetic_probe_total + duration | external fixed synthetic probe → approved DoH endpoint | journey=doh, transport=doh, outcome_class | R1 raw / R2 aggregate | SRE/QA | PAGE after 2 consecutive failed checks; TICKET on sustained SLO burn | RB-01 DNS critical path | PR-01,02,03,04 |
| DoT availability | synthetic_probe_total + duration | external fixed synthetic probe → approved DoT endpoint | journey=dot, transport=dot, outcome_class | R1/R2 | SRE/QA | same as DoH | RB-01 | PR-01,02,03,04 |
| DNS correctness | dns_correctness_total + synthetic result | fixed non-user controlled allow/block probe | transport,outcome_class | R1/R2 | SRE/QA/Security | PAGE on confirmed wrong safety result | RB-01 | PR-01,03,06 |
| DNS latency | synthetic_probe_duration_seconds histogram | same external fixed probe | journey,transport | R2 | SRE/QA | TICKET on sustained p95/p99/SLO burn; PAGE only with critical-path failure | RB-01 | PR-02,03 |
| TLS validity | tls_valid + tls_days_remaining | certificate/TLS synthetic check | transport only | R2 | SRE | PAGE on invalid hostname/chain; TICKET at <=30 days or renewal failure while valid | RB-08 TLS/DNS/config drift | PR-02,03 |
| Accountless web critical-path availability | synthetic_probe_total | project-owned synthetic accountless transaction | journey=accountless_core,mode=core,outcome_class | R1/R2 | SRE/QA | PAGE after 2 consecutive failed checks | RB-02 Accountless critical path | PR-01,02,03,06 |
| Accountless critical-route latency | http/synthetic duration histograms | normalized route middleware + synthetic runner | route_template,mode=core,status_class | R2 | SRE/QA | TICKET sustained p95/p99/SLO burn; PAGE only with broad user failure | RB-02 | PR-02,03 |
| Optional session-establishment availability | synthetic + session/dependency outcomes | project-owned non-participant test principal; auth boundary | journey=session_establish,mode=account_only,dependency,outcome_class | R1/R2 | SRE/Security | PAGE after 2 consecutive broad failures, with accountless-core status included | RB-03 Account/session/provider | PR-01,02,03,06 |
| Dashboard/device-read availability | synthetic + http outcomes | owned synthetic test records through authorization boundary | journey=dashboard_read,mode=account_only,outcome_class | R1/R2 | SRE/QA/Security | PAGE after 2 consecutive broad failures; any cross-parent result uses RB-04 | RB-03 / RB-04 | PR-01,02,03,06 |
| Account mutation terminal-truth correctness | mutation/reconciliation counters + R1 events | mutation service + datastore/AdGuard reconciliation boundary | operation_class,outcome_class,reconciliation_state | R1/R2 | SRE/Security | PAGE on false-success/cross-owner terminal state; TICKET on repeated ambiguity | RB-06 Mutation/reconciliation | PR-01,02,03 |
| Authorization isolation | scheduled negative synthetic + authorization denial/violation | server authz boundary using synthetic Parent-A/B fixtures | operation_class,reason_class,outcome_class | R1/R2/R3 result | Security/QA | PAGE on any cross-parent data/effect | RB-04 Ownership/IDOR/ClientID | PR-01,02,03,06 |
| Accountless fallback during auth/provider failure | paired failure-injection synthetic | auth-provider fixture + accountless critical runner | dependency=auth_provider,mode,outcome_class | R1/R2/R3 result | SRE/QA/Security | PAGE if account authority fails open or accountless core becomes unavailable | RB-03 | PR-01,02,03,06 |
| Recovery objective attainment | recovery outcome + synthetic post-restore verification | approved recovery workflow/clean-server acceptance | operation_class,outcome_class,duration,release/config version | R1 + R3 result | SRE/QA/Security | PAGE when confirmed recovery approaches objective without verified restoration; TICKET on stale evidence | RB-08 | PR-01,03,04 |
| Telemetry critical-path coverage | telemetry_signal_present + schema guard | instrumentation self-check/CI/runtime | signal_class,journey | R2/R3 result | SRE/QA/Security | TICKET on blind spot; blocks release if required critical-path coverage <100% | RB-09 Telemetry integrity | PR-01,02,04,05 |

## 8. Threat → telemetry / alert / runbook matrix

This matrix covers every TM-01..TM-30 row accepted in TSK-0239. Telemetry detects symptoms/control violations; it does not replace the negative/runtime tests named by TSK-0239.

| Threat | Primary signals / collection point | Allowed fields | Retention/access | Alert | Runbook | Privacy review |
|---|---|---|---|---|---|---|
| TM-01 XSS | CSP/security-header test result; normalized 5xx/error-class at web boundary | route_template,error_class,release_id | R1 SRE/Security; R3 test result | PAGE on confirmed active exploit/control failure; otherwise TICKET | RB-05 Privacy/security control | PR-01,03 |
| TM-02 CSRF | rejected state-change outcome at server mutation boundary | operation_class,reason_class,route_template | R1 Security/SRE | PAGE on successful forged mutation; TICKET on abnormal rejected trend | RB-05 | PR-01,02,03 |
| TM-03 session theft/fixation/replay | session outcome + revoked/expired/replay rejection | operation_class,outcome_class,error_class | R1 Security/SRE | PAGE on accepted invalid/revoked session; TICKET on rejection trend | RB-03 | PR-01,03 |
| TM-04 provider identity/account takeover | provider/session failure + auth-abuse aggregate | dependency,operation_class,outcome_class,error_class | R1/R2 Security/SRE | PAGE on accepted invalid identity/systemic takeover evidence; TICKET degradation | RB-03 | PR-01,02,03 |
| TM-05 IDOR/cross-parent | scheduled Parent-A/B negative fixture + confirmed authz violation | operation_class,outcome_class,release_id; no parent IDs | R1/R3 Security/QA | PAGE on any cross-parent data/effect | RB-04 | PR-01,03,06 |
| TM-06 ClientID authorization confusion | ClientID lifecycle negative fixture + mismatch/orphan aggregate | operation_class,outcome_class,reconciliation_state; never raw ClientID | R1/R2 Security/SRE | PAGE on unauthorized target effect; TICKET orphan/mismatch trend | RB-04 / RB-06 | PR-01,02,03 |
| TM-07 auth-provider fail-open / mandatory-login drift | provider failure + paired accountless synthetic | dependency,mode,outcome_class | R1/R2 SRE/Security | PAGE on fail-open or accountless-core loss | RB-03 | PR-01,02,03,06 |
| TM-08 datastore partial write/concurrency corruption | mutation + reconciliation signals | dependency=datastore,operation_class,outcome_class,reconciliation_state | R1/R2 SRE/Security | PAGE on cross-owner/false success; TICKET pending ambiguity | RB-06 | PR-01,02,03 |
| TM-09 exposed AdGuard admin/generic proxy/secret | exposure/secret/config checks + bounded admin rejection | control_class,dependency=adguard_control,outcome_class,release_id | R1/R3 Security | PAGE on confirmed exposure | RB-05 | PR-01,03,05 |
| TM-10 resolver abuse/amplification/resource/cost exhaustion | aggregate request/resource/saturation/cost guard | transport,resource_class,outcome_class | R2 SRE/Security | PAGE on user-impacting saturation/active abuse; TICKET sustained pressure | RB-07 Abuse/saturation | PR-02,03 |
| TM-11 web/API/DoH flood or malformed expensive input | RED/USE + rate-limit/schema rejection | route_template,operation_class,outcome_class,resource_class | R1/R2 SRE/Security | PAGE user-visible critical degradation; TICKET non-impacting sustained abuse | RB-07 | PR-01,02,03 |
| TM-12 dependency/action supply-chain compromise | CI/provenance/lock/advisory test result | control_class,outcome_class,release_id | R3 Security/DevSecOps | PAGE on protected release/control compromise | RB-05 / release recovery | PR-03,05 |
| TM-13 CI workflow injection/overprivileged token | CI permission/secret-boundary verification + audit result | control_class,outcome_class,release_id | R3 Security/DevSecOps | PAGE on protected-secret/write/deploy authority escape | RB-05 | PR-03,05 |
| TM-14 production/admin secret leakage | secret scanner + runtime privilege/config audit | control_class,outcome_class,release_id | R1/R3 Security | PAGE on confirmed secret exposure | RB-05 | PR-01,03,05 |
| TM-15 deletion/revoke/restore resurrects access | recovery/deletion fixture + reconciliation outcome | operation_class,outcome_class,reconciliation_state | R1/R3 Security/QA | PAGE on live/resurrected revoked authority | RB-06 / RB-08 | PR-01,03,06 |
| TM-16 telemetry/logging/backups create history/secrets/PII | telemetry schema guard + config/log/cache/backup privacy inspection | guard_class,signal_class,outcome_class | R1/R3 Security/Privacy Engineering | PAGE on active prohibited collection/secret; TICKET drift before collection | RB-09 / RB-05 | PR-01,03,04,05 |
| TM-17 anonymous J0/J1 enumeration/replay/tamper | anonymous-state rejection aggregate | operation_class,outcome_class,error_class | R1/R2 Security/SRE | PAGE on cross-session disclosure/control; TICKET abnormal rejection trend | RB-05 | PR-01,02,03 |
| TM-18 forged config/verification false protected state | protection verification invariant + synthetic fixture | outcome_class,config_version,platform_family | R1/R3 Security/QA | PAGE on false `protected_verified` | RB-02 / RB-05 | PR-01,03,06 |
| TM-19 VPN/Private Relay/custom DNS bypass | supported-device/network synthetic matrix | platform_family,outcome_class,transport | R1/R2/R3 QA/SRE | PAGE only on false protection claim; TICKET support/drift issue | RB-02 | PR-02,03,06 |
| TM-20 upstream DNS/provider outage/misroute | fixed synthetic resolution + dependency health | dependency=dns_upstream,transport,outcome_class | R1/R2 SRE | PAGE on critical-path impact/incorrect resolver; TICKET degradation | RB-01 | PR-01,02,03 |
| TM-21 SQL/NoSQL/command/path/control injection | validation-rejection aggregate + security test result | route_template,operation_class,error_class | R1/R3 Security | PAGE on successful arbitrary operation; TICKET attack/rejection trend | RB-05 | PR-01,02,03 |
| TM-22 auth/setup/recovery/verification brute force | bounded rate/rejection metrics | operation_class,outcome_class,reason_class | R1/R2 Security/SRE | PAGE if availability/control compromised; TICKET sustained abuse | RB-07 / RB-03 | PR-01,02,03 |
| TM-23 AI/operator privilege exceeds authority | governed mutation audit + authority-negative test | operation_class,control_class,outcome_class,release_id | R3 Governance/Security | PAGE on consequential authority escape | RB-05 / governance recovery | PR-03,05 |
| TM-24 stale/tampered safeguard/setup guidance | content source/version freshness check + failure report | control_class,outcome_class,release_id | R2/R3 Product/QA | TICKET stale guidance; PAGE only if active dangerous false claim | RB-02 / content correction | PR-02,03 |
| TM-25 duplicate/reordered/replayed device mutation | idempotency/version/reconciliation signals | operation_class,outcome_class,reconciliation_state,attempt | R1/R2 SRE/Security | PAGE on cross-owner/false success; TICKET repeated conflict | RB-06 | PR-01,02,03 |
| TM-26 backup/export/restore exposure or stale authority | backup schema/access/restore verification | control_class,operation_class,outcome_class,config_version | R3 Security/SRE | PAGE on prohibited content or resurrected authority; TICKET stale evidence | RB-08 / RB-05 | PR-03,04,05 |
| TM-27 domain/DNS/TLS compromise or expiry | DNS/TLS external synthetic + expiry metric | transport,outcome_class | R2 SRE/Security | PAGE on invalid/compromised endpoint; TICKET <=30d/renewal issue while valid | RB-08 | PR-02,03 |
| TM-28 clickjacking/cross-origin embedding | header/security test + rejected mutation aggregate | route_template,operation_class,outcome_class | R1/R3 Security | PAGE on successful state-changing exploit; TICKET control drift | RB-05 | PR-01,02,03 |
| TM-29 error/debug disclosure | error-response/log privacy test + telemetry guard | route_template,error_class,guard_class,outcome_class | R1/R3 Security | PAGE on secret/sensitive disclosure; TICKET debug/config drift | RB-05 / RB-09 | PR-01,03,05 |
| TM-30 account/config presence falsely treated as protection | Protection Map state invariant + technical verification synthetic | outcome_class,platform_family,config_version | R1/R3 QA/Security | PAGE on false `protected_verified` | RB-02 | PR-01,03,06 |

## 9. Runbook catalogue

Every alert must link to one of these runbook contracts. L6/L7 may split them into separate files but cannot remove required fields.

| Runbook | Trigger / first query | Immediate safe action | Escalation / closure evidence |
|---|---|---|---|
| `RB-01 DNS critical path` | confirm external DoH/DoT/TLS/correctness synthetic and target-vs-probe classification | preserve privacy logging-off state; roll back only to accepted DNS/config version; do not enable query history | SRE; closure requires fresh synthetic correctness + TLS + health evidence |
| `RB-02 Accountless critical path / protection truth` | compare accountless synthetic, normalized route RED, technical protection verification | keep core available without login; downgrade stale/unsupported protection truth | Product/SRE/QA/Security as relevant; closure requires fresh end-to-end accountless + truth-state verification |
| `RB-03 Account/session/provider` | compare session synthetic, provider dependency outcome and separate accountless health | fail account authority closed; preserve accountless continuation; never weaken auth for SLO | Identity/SRE/Security; closure requires fresh provider/session checks and accountless independence proof |
| `RB-04 Ownership / IDOR / ClientID` | run Parent-A/B and ClientID isolation check; inspect bounded authz/mismatch signals | block affected operation/session/control path; do not expose target identifiers in telemetry | Security/Backend; closure requires zero cross-parent effect and fresh isolation regression |
| `RB-05 Privacy/security control incident` | identify control_class, release/config change and current active exposure | stop prohibited collection/exposure; revoke/rotate secrets where applicable; restrict compromised surface | Security/Privacy Engineering; closure requires corrected config/code, secret-safe evidence and negative tests |
| `RB-06 Mutation / reconciliation integrity` | inspect operation_class, dependency, ambiguous/pending counts and exact durable state | stop blind replay; reconcile authoritative datastore/AdGuard/session state to one safe outcome | Backend/SRE/Security; closure requires deterministic terminal-state proof |
| `RB-07 Abuse / saturation` | compare user symptom, rate, latency, resource saturation and bounded abuse class | apply accepted rate/cap/circuit/load-shed control; avoid identity/history collection | SRE/Security; closure requires user-path recovery + bounded resource evidence |
| `RB-08 Recovery / TLS / DNS / config drift` | compare current release/config, restore evidence, TLS/DNS endpoint checks | rollback/restore only approved version; never restore prohibited history/revoked authority | SRE/QA/Security; closure requires clean recovery verification and accepted RTO evidence |
| `RB-09 Telemetry integrity / blind spot` | inspect telemetry_signal_present/schema rejection/retention/access guard | treat missing signal as unknown, never success; stop invalid signal pipeline | SRE/Security/Privacy Engineering; closure requires schema, field, cardinality, retention and alert-delivery verification |

Alert payloads carry only: severity, affected journey/control class, symptom/outcome, bounded release/config identifier, dashboard/runbook link and non-sensitive correlation to the incident record. No R0 data is allowed in notifications.

## 10. Dashboard contract

Four logical dashboards are sufficient for Version 1. Additional dashboards require a concrete operational question.

### D1 — Core Protection Health

- DoH/DoT availability, correctness and latency;
- TLS validity/days remaining;
- accountless critical-path availability/latency;
- protection-verification truthful outcome rate;
- current release/config version;
- separate `unknown/instrumentation_error` state.

### D2 — Optional Account Health

- session-establishment and dashboard-read availability/latency;
- auth-provider/datastore dependency outcomes;
- mutation terminal outcomes and reconciliation pending;
- authorization-denial aggregate;
- **always show accountless-core health beside account-only health** so provider failure is not mislabeled as total outage.

### D3 — Security / Privacy Controls

- current synthetic negative-test status by control class;
- telemetry schema/field/cardinality/retention guard status;
- secret/config exposure scan status;
- cross-parent/ClientID isolation fixtures;
- no-history configuration checks;
- supply-chain/CI protected-boundary verification result.

No user/device/client/domain drill-down exists.

### D4 — Recovery / Capacity

- last qualifying recovery/restore result and duration;
- backup/recovery evidence freshness;
- aggregate host/runtime utilization/saturation/errors;
- certificate/DNS/config drift;
- error-budget/SLO burn where applicable;
- no automatic HA/spend inference.

## 11. Tracing contract

Tracing is **disabled by default until a cross-component latency/failure question cannot be answered adequately by metrics + structured logs**. If later enabled inside the approved architecture:

- use OpenTelemetry-compatible trace/span semantics where practical;
- successful-request sampling is capped at `<=1%` initially; implementations may use less;
- R1 retention is `<=24h`;
- error traces are still subject to the same strict field allowlist—sampling more errors never authorizes sensitive fields;
- context may include random request/trace identifiers, normalized route/operation/dependency/outcome, duration, release/config version only;
- baggage must not carry identity, token, ClientID, DNS/domain/query or user content;
- tracing/export failure must not fail the product request path;
- any backend/vendor selection remains a separate implementation/resource decision.

## 12. Alert routing and anti-noise rules

Only two severities exist:

- `PAGE`: confirmed user-facing critical degradation or active High/Critical security/privacy control violation requiring immediate response;
- `TICKET`: actionable degradation, blind spot or drift that does not require immediate interruption.

Rules:

1. alerts are symptom/control-violation based; CPU/memory alone never page;
2. every alert has threshold/duration from TSK-0538 or an explicit invariant (for example cross-parent effect = one failure); no guessed threshold is introduced merely to create an alert;
3. every alert links to a runbook and identifies first diagnostic query/check;
4. duplicate events collapse by fixed alert key such as `journey+control_class+outcome_class`, never identity;
5. missing telemetry is `unknown/blind`, never healthy;
6. alert payloads contain no R0/R1 identifiers except an internal non-sensitive incident/correlation reference where needed;
7. actual delivery channel implementation/test is owned downstream (TSK-0541); this design does not claim Telegram/email delivery exists.

## 13. Privacy review gates

Each implemented signal must pass all applicable reviews before release:

- `PR-01 FIELD_ALLOWLIST` — every emitted field is explicitly allowed; unknown field fails closed/quarantines telemetry emission;
- `PR-02 CARDINALITY` — every metric label has a finite enumerated source and a bounded series estimate; identity/raw path/error text prohibited;
- `PR-03 NO_HISTORY_NO_SECRET` — sample output contains no DNS/domain/query/browsing data, identity, ClientID, credential, token, request body or free text;
- `PR-04 RETENTION` — automatic expiry/export/backup behavior proves R1 <=24h and R2 <=30d; R0 absent;
- `PR-05 ACCESS` — telemetry readers/writers/exporters are least privilege; access changes/revocation are auditable without telemetry content;
- `PR-06 SYNTHETIC_FIXTURES` — optional-account/device/network probes use project-owned non-participant fixtures and never real child/customer browsing data.

A privacy-review failure blocks that signal and any gate that requires it. It does not authorize widening collection to diagnose the failure.

## 14. Implementation and verification obligations

TSK-0539 is a design task. Downstream implementation must prove, in the target/approved test environment:

1. stable structured event schemas and random correlation propagation work end to end;
2. actual sample output contains no R0 data or unknown fields;
3. RED metrics exist for every active critical web/app route and external dependency, with histograms and bounded labels;
4. DNS/core synthetic probes preserve current query-history-off policy;
5. every current TSK-0538 SLI has a working signal or explicit inactive/not-yet-runtime state;
6. every current TSK-0239 High/Critical control has its planned detection/test signal and cannot be marked closed by telemetry alone;
7. tracing, if enabled, has no broken required context and no forbidden baggage/attributes;
8. retention and access enforcement pass negative tests;
9. every alert is test-fired once after implementation, reaches the approved downstream channel, links to the correct runbook and carries no sensitive payload;
10. induced failures are diagnosable from approved telemetry without needing forbidden browsing/query/identity collection;
11. instrumentation/export failure cannot break the core product path;
12. dashboards cannot drill into user/device/client/domain history.

## 15. Acceptance disposition

`ACC-0539` is satisfied at the **L5 observability-design boundary** when independent review verifies that:

- every current TSK-0538 SLI is mapped to signals, logical collection point, fields/labels, retention, access, alert threshold, runbook and privacy review;
- every TSK-0239 TM-01..TM-30 High/Critical control is mapped to a bounded detection/test signal, retention/access, alert/runbook and privacy guard;
- log fields and metric dimensions are allowlisted and bounded;
- correlation IDs exist only as short-lived diagnostics and never metric labels or durable customer identity;
- R0 forbidden data cannot enter telemetry by design;
- R1/R2 retention is explicit and bounded;
- dashboards separate account-only failure from accountless-core health and expose no user/device/client/domain drill-down;
- tracing is optional, bounded and vendor-neutral;
- PAGE/TICKET alerts are symptom/control-violation based and runbook-linked;
- no monitoring vendor, paid service, implementation, target-environment success, legal conclusion or downstream gate PASS is inferred.

**Non-inference:** TSK-0539 PASS would establish only the logical privacy-safe telemetry/alert design. It does not implement instrumentation, deploy a backend/collector, enable tracing, test notification delivery, prove production SLOs, close TSK-0239 security controls, make TSK-0049/TSK-0237/TSK-0048/LG-07 PASS, authorize L6 build, or establish production/legal readiness.
