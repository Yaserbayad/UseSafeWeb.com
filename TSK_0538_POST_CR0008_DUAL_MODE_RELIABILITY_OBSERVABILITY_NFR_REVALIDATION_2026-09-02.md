# TSK-0538 — Post-CR-0008 Dual-Mode Reliability, Observability, Recovery and Service-Level NFR Revalidation

**Task:** TSK-0538 — Define reliability, observability, recovery, and service-level NFRs  
**Acceptance / Verification / Evidence:** ACC-0538 / VER-0538 / EVD-0538  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0538 current PASS pending independent VER-0538 and guarded runtime reconciliation.

## 1. Why current revalidation is required

The accepted 2026-08-28 TSK-0538 contract correctly defines the current single-node encrypted-DNS reliability model and a future **accountless** web/app critical journey. It predates `DEC-0053 / CR-0006`, which activated optional parent authentication/session, minimum parent/device ownership persistence and lightweight dashboard/device management while preserving a complete accountless core.

Current direct predecessor TSK-0484 now defines active security/failure boundaries for authentication, session, ownership, provider, datastore, consequential mutation reconciliation and accountless fallback. ACC-0538 requires a specification of **critical user journeys**, SLI/SLO targets, alerts, recovery objectives, backup/restore behavior and escalation ownership. A reliability contract that omits those now-active optional-account journeys is materially incomplete even though the historical DNS and accountless requirements remain valid.

This is therefore a current dependency-complete revalidation, not a redesign of the DNS service and not an implementation of telemetry.

Current WBS contract:

- lifecycle `L4`;
- priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- dependency exactly `TSK-0484`;
- ACC-0538: specification defines critical user journeys, provisional SLI/SLO targets, alert conditions, recovery objectives, backup scope, restore test, maintenance behavior and escalation ownership;
- VER-0538: independent review against the current source baseline, dependency and acceptance contract;
- EVD-0538: artifact/version, exact source/environment, review output/date/verifier/deviations/disposition.

## 2. Preserved historical reliability baseline

Historical accepted contract:

- `TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_2026-08-28.md`;
- blob `d81537ef3ef66789528336e101d1e05f30030892`.

Historical acceptance evidence:

- `TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_EVIDENCE_2026-08-28.md`;
- blob `bd7a9f0d8a54dd28d423587257f1cd226b3e5dbc`.

The following remain binding unless a later owning task explicitly changes them:

- one lean encrypted-DNS node under the current initial architecture;
- no HA / active-active / new paid monitoring spend merely to satisfy this NFR;
- DNS recovery objective `<=30 minutes` end to end;
- privacy-safe fixed synthetic DNS probes rather than customer/user traffic inspection;
- DoH/DoT/certificate/filter correctness and current host/service health as critical operational signals;
- future web/app bounded route-template rate/error/latency signals once implemented;
- no metric labels containing user ID, IP, journey token, raw URL/query, email, device fingerprint, DNS/domain data or free-text content;
- Nginx access logging, AdGuard query/file logging and identifiable client statistics remain off under their owning privacy contracts;
- symptom-first PAGE/TICKET alerting;
- privacy-minimal recovery material and restore testing;
- no public/customer SLA inferred from provisional internal SLOs.

## 3. Current direct-predecessor reliability boundary

Current TSK-0484 accepted artifact:

- `TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md`;
- blob `285ee390499190137e8aac0fed976975fb79ed80`.

Current TSK-0484 evidence:

- `TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`;
- blob `a7461f68f99ccda5c947a4ee77453817db9db1e5`.

Reliability-relevant current invariants inherited here:

1. accountless core remains independent of optional account/provider availability;
2. authentication never substitutes for authorization;
3. account/device presence never substitutes for technical protection verification;
4. provider/datastore failure fails closed for account authority but must not disable the complete accountless core path;
5. consequential account/device/ClientID/delete/revoke mutations reconcile before replay when outcome is ambiguous;
6. no browsing/query/activity-history observability backdoor is authorized;
7. High/Critical release paths remain blocking until implementation plus target-environment verification succeeds.

TSK-0538 defines the operability requirements that make these conditions observable/recoverable. It does not implement or self-certify TSK-0352 or TSK-0353.

## 4. Current external reliability/observability source review

Current authoritative engineering sources were rechecked on 2026-09-02:

1. Google SRE, *Monitoring Distributed Systems* — `https://sre.google/sre-book/monitoring-distributed-systems/` — user-facing monitoring should distinguish symptoms from causes; the four golden signals are latency, traffic, errors and saturation; black-box monitoring is critical for user-visible behavior.
2. Google SRE Workbook, *Implementing SLOs* — `https://sre.google/workbook/implementing-slos/` — SLOs should be based on specific measurable SLIs and can be centered on critical user journeys; initial SLOs are provisional and should be refined from evidence.
3. OpenTelemetry observability primer — `https://opentelemetry.io/docs/concepts/observability-primer/` — observability relies on emitted telemetry such as traces, metrics and logs.
4. OpenTelemetry signals — `https://opentelemetry.io/docs/concepts/signals/` — metrics, traces and logs are distinct telemetry signals; baggage/context is separate and must not become a sensitive-data transport.
5. OpenTelemetry metrics — `https://opentelemetry.io/docs/concepts/signals/metrics/` — histograms are appropriate for latency/value distributions and high-cardinality attributes such as user IDs/raw URL paths can create unbounded metric cost/state.
6. OpenTelemetry logging specification — `https://opentelemetry.io/docs/specs/otel/logs/` — log correlation can bind structured logs to trace/span context without requiring sensitive business identifiers as metric dimensions.
7. Prometheus metric/label naming — `https://prometheus.io/docs/practices/naming/` — every unique label combination creates a time series; high-cardinality/unbounded labels such as user IDs/email addresses should not be used.

These sources establish engineering direction, not an implementation/vendor decision. OpenTelemetry is the preferred vendor-neutral instrumentation vocabulary if/when the web/app requires cross-component instrumentation, but no collector/backend/APM purchase or deployment is authorized by TSK-0538.

## 5. Current on-call questions

Every approved signal must answer at least one bounded operational question.

### DNS / accountless core

1. Can a supported device reach the approved DoH and DoT endpoints with valid TLS and expected filtering behavior?
2. Can a parent start the accountless journey, reach supported setup, verify protection truthfully, view Protection Map, recover/remove and continue ordinary internet use?
3. Has DNS/service/configuration/network drift invalidated the current protection claim?

### Optional account/session/dashboard

4. Can an explicitly choosing parent establish/refresh a valid optional session without making login mandatory for core value?
5. Can an authenticated parent read only their own lightweight dashboard/device state?
6. Can parent-owned device registration/update/unlink/delete reach one truthful terminal outcome without cross-parent effects?
7. Can logout/revoke/account deletion reach a truthful terminal state without leaving live authorization or falsely implying physical DNS removal?
8. Is an account-only failure caused by our application, the authentication provider, the datastore, authorization, the AdGuard control boundary or verification?
9. During provider/datastore outage, is account authority failing closed **while accountless setup/verify/remove remains usable**?
10. Did an ambiguous consequential mutation reconcile before retry, or is the product incorrectly presenting success?

### Recovery / evidence

11. Can current approved DNS/runtime configuration be rebuilt inside the accepted recovery objective without restoring prohibited history?
12. Can minimum persistent parent/device authority be restored without cross-parent ownership drift or resurrection of deleted/revoked authority?
13. What exact bounded change preceded the regression, and what accepted version/configuration is running now?

A metric/log/trace that answers none of these questions is not justified by this L4 contract.

## 6. Current critical-journey catalogue

| Journey | Mode | Success boundary | Failure boundary / truthful degraded state |
|---|---|---|---|
| DoH transaction | Core | Valid TLS/hostname; approved DoH path; expected controlled DNS result | Connect/TLS/path/timeout/wrong resolver or filtering result |
| DoT transaction | Core | Valid TLS/hostname; approved DoT path; expected controlled DNS result | Connect/TLS/path/timeout/wrong resolver or filtering result |
| Accountless start → supported setup → verification → Protection Map | Core | No login required; each step reaches next valid state; final protection claim has qualifying technical evidence | Unavailable/error/stale state/unsupported path/privacy failure; never force login |
| Accountless recovery/removal | Core | SafeWeb DNS can be removed/recovered and ordinary connectivity restored without stale `protected_verified` | Removal/recovery fails or stale protection claim survives |
| Optional sign-in → session establish/refresh | Account-only | Provider identity accepted only after valid backend verification; server session reaches valid bounded state | Provider/verification/session failure; deny account authority and preserve accountless continuation |
| Dashboard/device read | Account-only | Authenticated parent receives only their minimum owned account/device state | Unauthorized/cross-parent/stale/ambiguous state; no data disclosure |
| Device register/update/unlink/delete | Account-only | Server authorization succeeds; one ownership-correct terminal result; control mutation reconciled | Cross-parent effect, unknown outcome represented as success, orphan ClientID/ownership |
| Logout/session revoke | Account-only | Subsequent use of revoked session/authority fails; accountless core remains usable | Session remains authorized or logout falsely claims DNS removal |
| Account deletion | Account-only | Account-owned persistent authority reaches accepted deletion terminal state; unrelated anonymous/DNS operations remain distinct | Deleted authority is retained/resurrected or account deletion falsely claims physical DNS removal |
| Auth provider failure | Dependency failure | Account-only functions fail closed; accountless core still operates; state clearly identifies bounded account outage | Account access granted without verified provider identity or accountless core unnecessarily blocked |
| Datastore/ownership failure | Dependency failure | Account-only mutation/read fails safely; no cross-parent data; ambiguous writes reconcile before replay | Stale/corrupt/cross-parent state or duplicate mutation presented as success |
| AdGuard control/verification failure | Dependency failure | Account/device control cannot exceed authorized typed operation; protection claim follows fresh verification | Arbitrary control, stale claim, unknown mutation outcome or account state used as protection proof |

Optional-account failure is **not** a SafeWeb-wide outage when the complete accountless safety path remains healthy. Dashboards must make this distinction visible to operators.

## 7. Signal contract

### 7.1 Black-box / synthetic signals

When the applicable runtime exists:

- preserve fixed privacy-safe external DoH/DoT/TLS/filter probes;
- add accountless critical-path synthetic checks from start through truthful terminal state;
- add optional-account synthetic checks only with a dedicated project-owned non-participant test principal and test device records in an approved non-user-data test context;
- exercise sign-in/session, dashboard/device ownership, revoke/delete and provider/datastore failure fixtures without using participant/customer data;
- distinguish target failure from probe/instrumentation failure; missing probes are `unknown/instrumentation_error`, never success.

### 7.2 Metrics

For web/app routes and external dependencies, use bounded RED-style signals when implemented:

- request/operation rate;
- error/outcome rate;
- latency histograms with p50/p95/p99 queryability;
- dependency outcome/latency for auth provider, datastore, AdGuard control and protection-verification dependencies;
- bounded mutation/reconciliation counters by operation class and terminal outcome;
- aggregate authorization-denial/rate-limit counts by operation class, not identity;
- existing host/resource saturation signals for the DNS/runtime host.

Allowed metric dimensions are bounded enums such as:

- route template;
- operation class;
- status class;
- dependency name from a fixed allowlist;
- outcome class;
- platform family where materially needed and bounded.

Never use as metric labels:

- parent/user/account ID;
- email;
- IP address;
- journey/session token;
- Firebase UID or provider subject;
- device ID or `ClientID`;
- raw URL/query string;
- DNS/domain/query data;
- free-text error or user content.

### 7.3 Structured logs

Structured logs are event records, not a second analytics product. When implementation requires diagnostic/security events, use stable event names and allowlisted fields such as:

- request/correlation ID;
- route/operation template;
- bounded dependency name;
- bounded outcome/error class;
- retry/reconciliation attempt count;
- deployment/config version;
- duration;
- trace/span identifiers when tracing is active.

Do **not** log tokens/session cookies, provider credentials, AdGuard credentials, request bodies, DNS/query history, email, unnecessary identity, full URLs, raw ClientID, or persistent journey linkage. Request/correlation IDs are diagnostic fields, not metric labels or durable customer identities.

### 7.4 Traces

Distributed tracing is optional until the runtime actually contains cross-service boundaries where traces answer an operational question that metrics/logs cannot answer cheaply. If enabled:

- use vendor-neutral OpenTelemetry semantics where practical;
- sample/bound volume;
- propagate correlation context only across approved service boundaries;
- keep baggage/attributes allowlisted and free of account identity, tokens, ClientID, DNS/query data and user content;
- tracing failure must not break the product path.

## 8. Provisional current SLIs/SLOs

These are internal engineering targets, not customer promises. They are inactive until the relevant runtime exists and must be recalibrated from evidence without weakening safety/privacy truthfulness.

| SLI | Definition | Provisional internal target |
|---|---|---|
| DoH availability | successful valid external synthetic DoH transactions / scheduled transactions | `>=99.9%` rolling 30 days |
| DoT availability | successful valid external synthetic DoT transactions / scheduled transactions | `>=99.9%` rolling 30 days |
| DNS correctness | correct controlled allow+block checks / scheduled checks | `>=99.9%` rolling 30 days |
| DNS latency | successful external encrypted-DNS transaction duration | p95 `<=1.0s`, p99 `<=2.0s` rolling 24h |
| TLS validity | valid approved hostname/chain/non-expired checks / scheduled checks | `100%` |
| Accountless web critical-path availability | successful synthetic accountless critical transactions / scheduled transactions after app exists | `>=99.9%` rolling 30 days |
| Accountless critical-route latency | successful critical route-template duration after app exists | p95 `<=1.0s`, p99 `<=2.0s` rolling 24h |
| Optional session-establishment availability | successful synthetic sign-in/session establishment / scheduled attempts after optional account exists | `>=99.9%` rolling 30 days; provider-caused user-visible failure counts against this account-only SLI |
| Dashboard/device-read availability | successful authorized synthetic owned-device/account reads / scheduled reads | `>=99.9%` rolling 30 days |
| Account mutation terminal-truth correctness | accepted register/update/unlink/delete/revoke operations that reach one truthful ownership-correct terminal state / accepted test operations | `100%`; ambiguity cannot count as success |
| Authorization isolation | cross-parent negative fixtures with zero unauthorized data/effect / all scheduled cross-parent fixtures | `100%` |
| Accountless fallback during auth/provider failure | synthetic provider-failure tests where account authority fails closed and accountless start/verify/remove remains usable / scheduled provider-failure tests | `100%` |
| Recovery objective attainment | qualifying DNS/runtime recovery tests/incidents restored with all required invariants / qualifying cases | `100%` meet the applicable recovery objective |
| Telemetry critical-path coverage | active critical routes/dependencies with required bounded RED/health instrumentation / active critical routes/dependencies | `100%` before that runtime can satisfy its release gate |

A third-party provider outage is not silently excluded from the **account-only** user-facing SLI merely to make reliability look better. It also does not count as failure of the separate accountless-core SLI if the accountless critical path remains healthy.

## 9. Alert contract

Use two operational severities only:

- **PAGE** — confirmed user-facing critical degradation or active high-impact security/privacy control failure requiring immediate action;
- **TICKET** — actionable degradation/risk requiring correction but not immediate interruption.

### PAGE conditions

Page when any of these occur after the applicable runtime exists:

1. DoH or DoT critical-path synthetic transaction fails on two consecutive scheduled checks, or both transports fail on one independently confirmed check;
2. TLS hostname/chain validation fails on an approved transport;
3. controlled DNS correctness produces a confirmed wrong safety result;
4. accountless critical path fails on two consecutive scheduled checks;
5. optional sign-in/session or dashboard/device critical path is broadly unavailable on two consecutive scheduled checks, while alert context explicitly states whether accountless core is healthy;
6. an ownership/authorization synthetic detects cross-parent data/effect;
7. a deletion/revoke recovery check detects resurrected or still-live authority;
8. active TSK-0484 critical privacy/security invariant fails, such as prohibited query logging/public admin/secret exposure;
9. confirmed recovery is approaching the applicable recovery objective without verified restoration.

### TICKET conditions

Ticket, rather than page solely on cause, for:

- certificate `<=30 days` remaining while still valid;
- certificate renewal/dry-run/deploy-hook failure while current cert is valid;
- sustained CPU/memory/disk pressure without current user-visible failure;
- stale/failed backup or recovery evidence;
- configuration/version drift without current critical-path failure;
- sustained SLO/error-budget burn without immediate broad outage;
- provider/datastore degradation that remains below the page threshold;
- telemetry blind spot / missing-data condition;
- repeated reconciliation/ambiguous-mutation outcomes above the accepted baseline.

Every alert must identify the affected journey, symptom, first diagnostic query/check, current owner and runbook; no participant/DNS-history/secret data may be embedded in alert payloads.

## 10. Recovery and fail-safe objectives

### 10.1 DNS service

Preserve the accepted DNS RTO: **`<=30 minutes` end to end** from confirmed user impact/rebuild start to verified restoration of approved DoH/DoT identity, AdGuard configuration, upstream/filter/privacy/admin/TLS/listener and synthetic-health invariants.

User/query-history RPO remains not applicable by design because such data is prohibited from recovery storage.

### 10.2 Public/accountless web/app runtime

Once implemented, provisional internal RTO is **`<=30 minutes`** from confirmed widespread application outage to verified restoration of the accountless start/setup/verify/Protection-Map/removal critical path. This reuses the current lean recovery envelope as an internal target; it is not a public SLA and does not authorize HA spend.

### 10.3 Authentication-provider outage

SafeWeb cannot promise third-party provider recovery time. The recovery objective is instead deterministic containment and truthful restoration:

- detect and classify the provider failure;
- deny new/ambiguous account authority;
- preserve the complete accountless core path;
- keep existing session behavior within the later approved session contract rather than guessing;
- automatically re-evaluate account-only service after provider recovery;
- restore positive account state only after fresh valid provider/session checks.

No operator may weaken authentication/security to satisfy an availability target.

### 10.4 Persistent parent/device authority

For acknowledged ownership/delete/revoke transitions, **zero security-authority regression is tolerated**: recovery/restore must not expose another parent's device, revive deleted/revoked authorization, or present an ambiguous mutation as completed.

Exact datastore backup-point/RPO mechanics remain owned by later storage/auth architecture, but any chosen mechanism must satisfy this invariant before release. If a restore can roll back a security-relevant authority transition, reconciliation with current authoritative provider/ownership state is mandatory before dashboard/control access resumes.

### 10.5 Ambiguous consequential mutation

A timeout/network failure after a register/update/unlink/delete/revoke/ClientID mutation produces `unknown/reconcile-required`, not automatic replay or success. Retry is authorized only after outcome reconciliation or materially new evidence.

## 11. Backup / restore scope

Preserve the historical privacy-minimal backup contract and extend it only for the newly active minimum persistent authority domain.

### Include only when required for deterministic recovery

- accepted versioned deployment/recovery scripts and non-secret configuration;
- approved DNS/filter/TLS recovery material under its owning protected mechanism;
- minimum persistent parent/device ownership/configuration state once the owning schema/architecture defines it;
- versioned runbooks/verification manifests needed to prove restoration.

### Exclude

- DNS/query/domain/browsing history;
- identifiable AdGuard query logs/statistics;
- J0/J1 transient journey records;
- raw product event streams;
- session cookies/bearer tokens/refresh tokens;
- provider/service-account secrets in ordinary backup artifacts;
- unnecessary identity/content/support transcript data.

### Restore verification

A qualifying current restore test must prove, as applicable:

1. clean/approved target and source/version identity;
2. service/runtime startup;
3. DNS/TLS/filter/privacy/admin invariants;
4. accountless critical path;
5. optional account/session only when approved provider/session dependencies are valid;
6. parent-device ownership isolation;
7. revoked/deleted authority is not resurrected;
8. ambiguous mutations are not silently replayed;
9. prohibited history/tokens/secrets are not restored;
10. synthetic/telemetry health is restored;
11. measured applicable RTO is met;
12. evidence identifies deviations and disposition.

Historical quarterly recovery-rehearsal cadence remains the provisional active-operation minimum for the single-node model and after material changes to recovery/storage/provider topology.

## 12. Maintenance behavior

Preserve the historical daily certificate check, continuous/scheduled critical-path health, weekly drift/security review, monthly consolidated maintenance/capacity/cost/vendor review and quarterly recovery rehearsal once active.

Extend material-change revalidation triggers to include:

- auth provider/project/configuration/session-policy change;
- persistent account/device schema or datastore change;
- ownership/ClientID lifecycle change;
- delete/revoke semantics change;
- critical route/dependency or observability schema change;
- TSK-0484 High/Critical control change;
- restore path or backup scope change.

A material maintenance change is not complete until affected accountless/account/security/privacy/recovery regression evidence passes.

## 13. Incident and escalation ownership

| Incident domain | Primary technical owner | Required boundary |
|---|---|---|
| DNS/platform | SRE/Operations / Network Engineering | Preserve DNS/privacy/TLS/filter invariants |
| Public/accountless web app | Software/Platform + SRE | Restore accountless critical journey truthfully |
| Auth/session/provider | Software/Platform + Security | Fail closed for account authority; preserve accountless core; no provider/security weakening |
| Parent/device ownership/datastore | Software/Platform + Security/Privacy | No cross-parent state; reconcile ambiguity; preserve delete/revoke truth |
| AdGuard control/ClientID | Software/Platform + Network/Security | Typed authorized operation only; no public admin |
| Privacy/security control | Privacy/Security + applicable engineering owner | Technical containment inside authority; no fabricated legal/incident conclusion |
| Azure/control-plane | Existing owner-controlled boundary unless later authority changes | No inferred cloud mutation authority |
| Public/customer communication | Applicable communication authority | Factual verified incident inputs only; no automatic consequential publication |

Every material incident records severity, affected journey, containment, reconciliation/recovery evidence, restored state and proportional regression follow-up before closure.

## 14. Current acceptance assertions

1. Current critical journeys include DNS, complete accountless web/app, optional sign-in/session, dashboard/device ownership, revoke/delete and dependency-failure behavior.
2. Account-only outage and accountless-core outage are measured and reported separately.
3. Provisional SLI/SLOs are user-journey-centered, measurable and explicitly internal/non-public.
4. Historical DNS `<=30-minute` recovery objective is preserved.
5. A provisional `<=30-minute` accountless application recovery objective is defined without authorizing HA spend.
6. Auth-provider recovery time is not fabricated; containment/fail-closed/accountless-fallback/restoration evidence is the operability objective.
7. Persistent account/device recovery cannot resurrect deleted/revoked/cross-parent authority.
8. Consequential ambiguous mutations reconcile before replay and cannot count as success.
9. Metrics use bounded dimensions and never use identity/token/ClientID/raw URL/DNS data as labels.
10. Structured logs use bounded event fields and correlation context without secrets/tokens/DNS history/unnecessary identity.
11. Tracing remains optional/vendor-neutral and cannot become a sensitive-data propagation channel.
12. Alerts are symptom-centered and distinguish PAGE from TICKET.
13. Backup/restore remains privacy-minimal and explicitly excludes J0/J1, DNS history, raw events and bearer/session material.
14. Restore verification covers ownership isolation and non-resurrection of revoked/deleted authority when persistent state exists.
15. Current TSK-0484 security/reliability boundaries are consumed without self-certifying TSK-0352/TSK-0353 implementation.
16. No telemetry backend, monitoring vendor, HA topology, provider activation, datastore implementation, public SLA, participant processing or launch is inferred.

## 15. Candidate disposition

**ACC-0538 current candidate: PASS pending independent current VER-0538.**

The historical TSK-0538 contract remains valid evidence for unchanged DNS/accountless/operability facts. This artifact is the current acceptance candidate because it closes the reliability/observability/recovery gap introduced by the active optional-account/session/ownership/provider/datastore boundary while preserving the lean, privacy-minimal and accountless-first operating model.
