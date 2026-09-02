# TSK-0046 — Post-CR-0008 Dual-Mode Performance and Capacity NFR Revalidation

**Task:** TSK-0046 — Define performance and capacity NFRs  
**Acceptance / Verification / Evidence:** ACC-0046 / VER-0046 / EVD-0046  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0046 current PASS pending independent VER-0046 and guarded runtime reconciliation.

## 1. Current contract and why revalidation is required

Current canonical WBS contract:

- lifecycle `L4`;
- priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- direct dependency exactly `TSK-0538`;
- ACC-0046 requires expected pilot load, safety margin, DNS latency/availability test method, web journey performance, degradation behavior and a capacity-review trigger;
- VER-0046 is independent reviewer inspection against the current source baseline, dependency and acceptance contract;
- EVD-0046 requires artifact/version, exact source/environment, review output/date/verifier/deviations/disposition.

Historical accepted TSK-0046 correctly established the capacity-engineering core, but two current-authority changes require revalidation:

1. `DEC-0054 / CR-0007` removed the mandatory separate pilot/staging lifecycle. First real users are live-production users only after `LG-09` and every actually applicable prerequisite passes. The historical `CR-0003` / separate-pilot sequencing is therefore stale.
2. `DEC-0053 / CR-0006` activated optional parent authentication/session, minimum parent/device ownership persistence and lightweight dashboard/device management while preserving a complete accountless core. Current TSK-0538 now defines reliability/SLO boundaries for both accountless and optional-account journeys. The historical web/application capacity model covered the accountless journey only.

This revalidation updates those two semantics without redesigning the DNS service, weakening security/privacy controls, fabricating adoption, authorizing production stress tests, or purchasing/scaling infrastructure.

## 2. Historical TSK-0046 engineering baseline preserved

The following accepted rules remain binding because no current evidence contradicts them:

- minimum **2× verified capacity margin** over the approved expected peak before a load-bearing path is accepted;
- controlled synthetic/project-owned names and fixtures rather than participant/customer DNS traffic for DNS performance testing;
- separately measured p50/p95/p99 latency and explicit success/failure/correctness counts;
- DoH and DoT tested independently with TLS/filtering/correctness intact;
- security/rate-limit/privacy/filtering/admin controls are never disabled merely to improve benchmark results;
- a single test source hitting an abuse/rate-limit boundary is not evidence of total service capacity;
- current host/resource observations are evidence of observed state only, not proof of maximum QPS/concurrency;
- synthetic/lab web results are never mislabeled as field p75 results;
- degradation preserves encryption, filtering, privacy, authorization and truthful protection-state semantics before optional work;
- capacity-review thresholds trigger diagnosis/review before incident thresholds become normal operating targets;
- no automatic HA/multi-node purchase or architecture change is created by this NFR.

Historical artifacts remain provenance:

- `TSK_0046_PERFORMANCE_CAPACITY_NFR_2026-08-28.md` — blob `2c48f975d557b1bb4ba6c58c2a8ad3580b2c7b06`;
- `TSK_0046_PERFORMANCE_CAPACITY_NFR_EVIDENCE_2026-08-28.md` — blob `09d111530c5e9c86feb2cafb54f62fb046a44b6f`;
- `TSK_0046_HOST_CAPACITY_BASELINE_EVIDENCE_2026-08-28.md` remains a historical read-only host snapshot, not current capacity proof.

## 3. Current predecessor binding — TSK-0538

Current predecessor:

- `TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md` — blob `44c9c299465e821e2ffd84a54b77e3e615d61925`;
- current evidence `TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md` — blob `3ba04601ea5574fcd1fb1f58f95922ae94b74ac2`.

Performance/capacity must preserve the current TSK-0538 reliability boundaries:

- DNS DoH/DoT availability target `>=99.9%` rolling 30 days when operational;
- DNS correctness `>=99.9%` rolling 30 days;
- DNS latency p95 `<=1.0s`, p99 `<=2.0s` rolling 24h;
- TLS validity `100%`;
- accountless web critical-path availability `>=99.9%` when the application exists;
- accountless critical-route latency p95 `<=1.0s`, p99 `<=2.0s` when the application exists;
- optional session-establishment availability `>=99.9%` when implemented;
- dashboard/device-read availability `>=99.9%` when implemented;
- account mutation terminal-truth correctness `100%` for accepted test operations;
- authorization isolation `100%` for scheduled cross-parent negative fixtures;
- accountless fallback during auth/provider failure `100%` for scheduled failure fixtures;
- provider/datastore/account-only failure never turns a healthy accountless core into a whole-service outage.

TSK-0046 does not redefine these SLOs. It defines the workload, headroom, performance-test and capacity-review conditions needed to show the implemented system can meet them.

## 4. ACC-0046 “expected pilot load” under current CR-0007 authority

The WBS retains the historical phrase **expected pilot load**. Current CR-0007 authority removes a separate mandatory pilot/staging lifecycle. For ACC-0046 compatibility, that inherited phrase is implemented as the **bounded first live-production validation/ramp load envelope** after `LG-09` and every actually applicable prerequisite passes. It does not create a separate pilot environment or lifecycle.

Current truthful state:

- authorized real-user/live-production validation load before `LG-09 PASS`: **0 real-user devices**;
- first-live-production-validation cohort/device count: **UNFROZEN** until authorized by current gate/rollout evidence;
- no adoption, household, query-volume or account-usage forecast is invented by this task.

### 4.1 DNS load model

When authorized, define:

- `N_dns_active_peak` = approved maximum simultaneously active supported devices in the bounded production-validation/ramp window;
- `Q_dns_device_peak` = privacy-safe synthetic characterization of one supported device’s approved peak encrypted-DNS transaction rate;
- `Q_dns_expected = N_dns_active_peak × Q_dns_device_peak`;
- `C_dns_expected` = approved encrypted-DNS concurrency model if concurrency is the binding resource.

No input may be inferred from browsing history, participant DNS logs or generic Internet averages.

### 4.2 Web/accountless load model

When the web/app exists and live-production validation is authorized, define separately:

- `N_web_active_peak` = approved simultaneously active product users/devices;
- `R_accountless_peak` = privacy-safe synthetic request/operation rate for the accountless critical journey;
- `C_accountless_peak` = expected concurrent accountless critical transactions.

The critical accountless journey remains available without login.

### 4.3 Optional-account load model

When optional account/session/dashboard/device-management implementation exists, define separately:

- `R_session_peak` = synthetic sign-in/session establish/refresh operation rate;
- `R_dashboard_peak` = synthetic authorized dashboard/device-read rate;
- `R_mutation_peak` = synthetic register/update/unlink/delete/revoke operation rate;
- `C_account_peak` = expected concurrent account-only critical operations;
- dependency budgets/quotas for authentication provider, datastore and AdGuard control/verification paths.

Account-only capacity demand must not be blended into DNS/accountless success in a way that hides provider/datastore bottlenecks or makes login mandatory for core value.

## 5. Capacity safety margin

For every implemented load-bearing critical path, current acceptance requires at least a **2× verified margin over the approved expected peak** before the corresponding load envelope is treated as proven.

### DNS

1. pass at `1× Q_dns_expected`;
2. pass at `2× Q_dns_expected`;
3. preserve DoH/DoT/TLS/filtering/correctness/security/privacy/rate-limit invariants;
4. record resource/latency/error behavior at each stage;
5. if 2× cannot be proven safely, reduce supported load or execute governed capacity/architecture review before activation/ramp expansion.

### Web/accountless and optional-account paths

For each implemented critical path:

1. pass functional/authorization/privacy correctness at the approved expected request/concurrency envelope;
2. pass the same invariants at 2× the expected envelope;
3. record route/dependency latency, rate/error/outcome and resource saturation using bounded privacy-safe dimensions;
4. test external dependency failure separately rather than treating a third-party quota/outage as local host saturation;
5. never increase throughput by weakening session, CSRF, ownership, IDOR, rate-limit, privacy or reconciliation controls.

The 2× rule is an acceptance margin, not a claim that any component’s absolute maximum capacity equals exactly 2× expected load.

## 6. DNS latency/availability performance method

Use fixed project-owned/controlled synthetic names and fixtures. Never replay participant/customer DNS traffic.

Minimum coverage:

- valid DoH on the approved path;
- valid DoT on TCP 853;
- controlled allow and block behavior;
- TLS hostname/chain validity;
- filtering/upstream correctness;
- removal/recovery when included in the test objective;
- security/rate-limit interaction under the current accepted abuse-resistance contract.

Load stages once a legitimate expected envelope exists:

1. low-rate functional baseline;
2. 1× expected peak;
3. 2× expected peak;
4. bounded burst above 2× only on an isolated/reversible target when useful for headroom diagnosis.

Record scheduled/attempted/successful/failed synthetic transactions, bounded error classes, p50/p95/p99, CPU/memory/disk/resource pressure, service health, exact release/configuration and test duration/warm-up rule.

A bounded load test does not prove a 30-day SLO. It must report the bounded window truthfully and must fail acceptance if observed behavior violates the active SLO threshold or exposes correctness/security/privacy defects.

## 7. Web journey performance

This section becomes executable only when the relevant application/runtime exists.

### 7.1 Accountless core journey

At minimum test:

`public/start → accountless routing → supported setup guidance → verification response → Protection Map → troubleshooting/recovery/removal/help`

Target the current TSK-0538 critical-route engineering thresholds:

- p95 `<=1.0s`;
- p99 `<=2.0s`;
- accountless critical-path availability `>=99.9%` once operational.

### 7.2 Optional-account journey

Separately exercise:

`optional sign-in → session establish/refresh → owned dashboard/device read → register/update/unlink/delete/revoke → logout/account deletion`

Requirements:

- no account action substitutes for technical protection verification;
- account-only failure fails closed without blocking the accountless core;
- cross-parent negative fixtures remain zero unauthorized disclosure/effect;
- ambiguous consequential mutations reconcile before replay;
- provider/datastore/AdGuard dependency bottlenecks are measured separately;
- optional-account latency is measured p50/p95/p99 in pre-release/load evidence. Until an owning current SLO explicitly freezes a different latency target, use p95 `<=1.0s` and p99 `<=2.0s` as the provisional internal engineering target, without presenting it as a customer SLA.

## 8. Browser-visible performance and current Core Web Vitals

Current first-party web.dev review on 2026-09-02 confirms the Core Web Vitals “good” thresholds remain:

- LCP `<=2.5s`;
- INP `<=200ms`;
- CLS `<=0.1`;
- assessed at the 75th percentile for the majority-user target, segmented across mobile/desktop where applicable.

Sources:

- `https://web.dev/articles/vitals`
- `https://web.dev/articles/defining-core-web-vitals-thresholds`

Current 2026 web.dev guidance also records that Chrome 151 introduced APIs for measuring Core Web Vitals across SPA soft navigations. Adoption into libraries/RUM/CrUX and non-Chromium support remains incomplete as of the August 2026 guidance. Therefore:

- pre-release lab/browser testing must bind exact navigation type and browser/runtime;
- full-page and soft-navigation measurements must not be silently mixed;
- synthetic/lab results do not prove field p75 compliance;
- future privacy-safe field measurement, if authorized, must comply with TSK-0497/TSK-0230 and must not introduce stable user identity, browsing history, raw URLs or content payloads.

Source: `https://web.dev/articles/vitals-spa-faq` (updated 2026-08-11).

## 9. Capacity-review triggers

Preserve the accepted early-review principle: thresholds are deliberately earlier than incident conditions and trigger diagnosis, not automatic scaling.

Review current capacity proof when any applicable condition occurs:

1. approved expected peak exceeds 50% of the last verified sustained capacity envelope;
2. CPU `>=70%` for 15 minutes under representative sustained workload;
3. memory utilization/pressure `>=75%` for 15 minutes;
4. service/root filesystem `>=70%` used or an evidenced growth trend materially erodes safe margin;
5. p95/p99 latency breaches the active target in two consecutive valid windows under expected legitimate load;
6. failures/correctness defects consume or project exhaustion of the applicable error budget;
7. legitimate topology repeatedly collides with current abuse/rate-limit controls;
8. upstream/auth-provider/datastore/AdGuard-control latency, quota or error behavior becomes the measured bottleneck;
9. material AdGuard/Nginx/kernel/filter/application/provider/datastore/topology/version change invalidates prior evidence;
10. approved device/account/concurrency envelope materially increases;
11. a SEV-1/SEV-2 capacity-related incident occurs;
12. recovery/change cannot preserve 2× margin without weakening a hard control;
13. optional-account traffic materially degrades the independently required accountless critical path;
14. accountless fallback under provider/datastore failure cannot meet its current correctness/availability boundary.

TSK-0538 remains authority for alert severity and service-level ownership.

## 10. Degradation behavior

When pressure threatens an accepted envelope:

1. preserve encrypted-DNS correctness, TLS, filtering, privacy and abuse controls;
2. preserve accountless start/setup/verify/recover/remove before optional account conveniences;
3. account-only authority fails closed if auth/provider/datastore/ownership state is unavailable or ambiguous;
4. never weaken authorization/IDOR/session/CSRF/rate limits, reconciliation or protection-state truthfulness to improve throughput;
5. never enable DNS/query/activity-history logging or stable user telemetry as a capacity workaround;
6. shed/defer noncritical analytics/content refresh/background/admin work before critical safety/recovery paths;
7. stop/defer nonessential consequential mutations if their safe reconciliation boundary cannot be maintained;
8. reduce the supported/ramped load claim when hard controls cannot be preserved at the current envelope;
9. do not broaden `/control`, credentials, plain-DNS exposure or firewall surface to recover performance.

Optional-account degradation is not a whole-service outage when accountless core/DNS remain healthy, and must be represented separately.

## 11. Capacity-review decision order

1. verify measurement and distinguish test/monitor failure from target failure;
2. isolate bottleneck: local CPU/memory/disk, Nginx/TLS, AdGuard/filtering, upstream/network, abuse-control topology, application runtime, auth provider, datastore, ownership/reconciliation or verification dependency;
3. correct a proven defect/inefficiency only while correctness/security/privacy remain intact;
4. rerun bounded regression/capacity verification;
5. reduce the supported/ramped load if the 2× margin remains unproven;
6. evaluate routine scaling only within then-current approved architecture/budget/action authority;
7. any architecture/scope/material-spend change follows its governing decision authority rather than being implied by this NFR.

## 12. Revalidation triggers

Reopen affected TSK-0046 proof when:

- first-live-production validation/ramp cohort or load is frozen/changed;
- per-device DNS or web/account workload model changes materially;
- optional account/session/dashboard/device-management runtime is implemented or materially changes;
- auth-provider/datastore quota/latency/reliability constraints materially change;
- AdGuard/Nginx/kernel/VM size/filter/upstream/topology materially changes;
- web/app architecture or critical route set changes;
- supported device/network topology changes;
- the 2× margin is no longer evidenced;
- a capacity/performance incident occurs;
- a security/privacy control materially changes the workload path;
- current Core Web Vitals metrics/thresholds or relevant soft-navigation measurement semantics materially change.

## 13. Testable assertions

A downstream implementation/QA plan must be able to prove at least:

1. no numeric real-user cohort/load is invented before current gate/rollout authority freezes it;
2. no separate mandatory pilot/staging lifecycle is reintroduced;
3. real-user/live-production validation load is zero before LG-09 and applicable prerequisites;
4. DNS, accountless-web and optional-account expected loads are modeled separately;
5. 1× and 2× expected-envelope tests are separately measured;
6. DoH and DoT, controlled allow/block correctness and TLS are tested;
7. p50/p95/p99 plus bounded failures/outcomes/resources are recorded;
8. current abuse/privacy/filtering/TLS/auth/session/ownership controls remain intact;
9. single-source rate limiting is not mislabeled as total service capacity;
10. accountless core remains usable without login;
11. auth/provider/datastore failure does not falsely count as accountless-core failure when the core remains healthy;
12. optional-account failure cannot grant account authority or create cross-parent effects;
13. ambiguous consequential mutations reconcile before replay;
14. browser results distinguish lab/synthetic from field and full-page from soft-navigation measurement where material;
15. crossing a capacity trigger causes evidence-driven diagnosis rather than automatic architecture/spend change;
16. exact release/config/environment/source versions are bound to every capacity result;
17. no browsing/query/activity history or stable unnecessary user identity is introduced for capacity evidence.

## 14. ACC-0046 traceability

ACC-0046 requires:

> NFRs state expected pilot load, safety margin, DNS latency/availability test method, web journey performance, degradation behavior, and capacity-review trigger.

Current coverage:

- **Expected pilot load:** §4 maps the inherited WBS phrase to the current CR-0007 bounded first live-production validation/ramp envelope, records current real-user load as zero before LG-09 and forbids fabricated adoption.
- **Safety margin:** §5 preserves the 2× verified margin and extends it to implemented accountless/account-only critical paths without weakening controls.
- **DNS latency/availability method:** §6 preserves controlled synthetic DoH/DoT/TLS/correctness testing with current TSK-0538 targets and privacy/security invariants.
- **Web journey performance:** §§7–8 cover both the complete accountless core and the optional-account branch and refresh current Core Web Vitals/SPA measurement semantics.
- **Degradation behavior:** §10 explicitly prioritizes DNS/accountless safety paths and fails optional-account authority closed.
- **Capacity-review trigger:** §9 preserves measurable early triggers and adds current provider/datastore/accountless-fallback boundaries.

## 15. Non-inference

This is an L4 NFR-definition revalidation only. It does not authorize or prove:

- LG-06/LG-07/LG-08/LG-09 or live-production activation;
- any real-user cohort/load;
- production stress testing;
- infrastructure resize/HA/new paid monitoring;
- web/app/account/auth implementation;
- provider/datastore architecture approval;
- legal/privacy completion;
- participant processing;
- publication/payment/market activation/launch;
- any successor PASS.

**TSK-0046 current result candidate: PASS, subject to independent verification, durable evidence publication, guarded runtime reconciliation and exact GitHub read-back.**
