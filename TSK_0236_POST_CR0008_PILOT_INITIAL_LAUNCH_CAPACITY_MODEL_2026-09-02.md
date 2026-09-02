# TSK-0236 — Post-CR-0008 Pilot / Initial-Launch Capacity Model

**Task:** TSK-0236 — Create pilot and initial-launch capacity model  
**Acceptance / Verification / Evidence:** ACC-0236 / VER-0236 / EVD-0236  
**Lifecycle / Priority / Authority:** L5 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Gate:** contributes to LG-07 Architecture, Security, Privacy and Delivery Readiness  
**Direct predecessors:** TSK-0046 current PASS; TSK-0411 current PASS

## 1. Decision and evidence boundary

Freeze the capacity-planning model below for the current dual-mode Version-1 architecture. The inherited WBS phrase **pilot load** is interpreted under DEC-0054/CR-0007 as the first **bounded live-production validation/ramp envelope after LG-09 PASS and every actually applicable prerequisite passes**. It does not create a separate pilot or staging environment.

This task is a capacity architecture/model decision. It does **not**:

- authorize L6 build before LG-07;
- authorize real users before LG-09 and current applicable legal/privacy/consent conditions;
- resolve the owner-deferred UK representative/ICO/legal condition;
- create or configure Azure control-plane resources;
- purchase, resize, or add infrastructure;
- invent a future user/device/query/request volume;
- convert a point-in-time host snapshot into a throughput claim;
- authorize US infrastructure or a new market;
- weaken encryption, filtering, privacy, authorization, session, CSRF, IDOR, abuse, recovery, or truth-state controls to obtain a larger benchmark.

Current real-user production load before LG-09 is **0**. The future bounded production-validation cohort/load and later UK public-production ramp are **UNFROZEN** until their owning gate/rollout evidence freezes them.

## 2. Authoritative inputs

### 2.1 Current task and governance contract

- Current WBS blob: `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.
- TSK-0236: L5 / MEDIUM / A3 / AUTO_ALLOWED; direct dependencies exactly `TSK-0046; TSK-0411`.
- ACC-0236 requires assumptions/calculations, pilot/launch scenarios, bottlenecks, headroom, alert thresholds, vertical/horizontal scaling options, and a retest/re-architecture trigger.
- VER-0236 is peer/reviewer inspection against the acceptance criteria, source baseline, dependencies, and required evidence.
- EVD-0236 requires artifact/version, exact source/environment, review output/date/verifier, deviations and disposition.
- LG-07 requires evidence-complete architecture/security/privacy/delivery readiness before L6.
- DEC-0055/CR-0008 requires minimum durable evidence sufficient for the actual acceptance boundary.

### 2.2 Performance/capacity NFR predecessor — TSK-0046

Current accepted source:

- `TSK_0046_POST_CR0008_DUAL_MODE_PERFORMANCE_CAPACITY_NFR_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `8e72d542b68de6f7f5c8c375b63b6229c6d15529`
- publication commit `0fbc382c94850fb02376c6f3105a1ea499fa7398`

Binding capacity rules consumed here:

1. every implemented load-bearing critical path needs at least **2× verified capacity margin over the approved expected peak** before that load envelope is treated as proven;
2. DNS, accountless-web, and optional-account workloads are modelled separately;
3. controlled synthetic/project-owned fixtures are used for performance tests; participant/customer DNS traffic and browsing history are prohibited sizing inputs;
4. p50/p95/p99 and explicit success/failure/correctness counts are retained for bounded tests;
5. security/privacy/rate-limit/filtering/authorization invariants remain enabled during capacity testing;
6. degradation preserves encrypted DNS and the accountless core before optional conveniences;
7. expected peak above 50% of the last verified sustained capacity is an early capacity-review trigger;
8. current alert/review triggers include CPU >=70% for 15 minutes, memory >=75% for 15 minutes, relevant filesystem >=70%, repeated latency-target breach, error-budget/correctness pressure, abuse-control collision, dependency bottlenecks, material topology/version change, load-envelope increase, capacity-related SEV-1/2 incident, or inability to preserve the 2× margin.

### 2.3 DNS topology predecessor — TSK-0411

Current accepted source:

- `TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md`
- version `1.0.0`
- blob `8bd206e3832bafc5b8033dddd3e7913a5e01f7b6`
- acceptance source commit `e698ce6cfe7f629dd3d320581ce231ed08190257`

Binding topology rules consumed here:

- one canonical DNS identity: `dns.usesafeweb.com`;
- public DoH: `https://dns.usesafeweb.com/dns-query`;
- public DoT: `dns.usesafeweb.com:853`;
- initial DNS service location: owner-provided Azure West Europe / Netherlands DNS VM;
- AdGuard Home remains the filtering layer; Quad9 dns10 DoH is the sole approved upstream and ECS is disabled;
- public encrypted edge is TCP 443/853 only; UDP/TCP 53 and AdGuard admin 3000 remain non-public;
- web/application VM is outside the ordinary DNS data plane;
- DoT source-identity/rate-control behavior must be proven before production activation;
- no US node is authorized by this model.

### 2.4 Historical host snapshot — context only

`TSK_0046_HOST_CAPACITY_BASELINE_EVIDENCE_2026-08-28.md` is a read-only point-in-time observation, not a capacity benchmark. It recorded:

- 2 logical CPUs;
- about 3.82 GiB total memory, about 22.2% used at capture;
- about 28.02 GiB root filesystem, 14% used at capture;
- AdGuard Home and Nginx active;
- AdGuard Home RSS about 149.7 MiB and Nginx RSS about 27.4 MiB at capture.

These values show only the observed state on 2026-08-28. They establish **no QPS, concurrency, maximum-user, or current-load claim**.

## 3. Capacity model variables and calculations

No numerical user/request forecast is inserted until its owning gate/rollout evidence supplies the input. Every future capacity decision must populate the variables from approved synthetic characterization and bounded rollout evidence, then retain the calculation.

### 3.1 DNS workload

Let:

- `N_dns_active_peak` = approved maximum simultaneously active supported devices in the target rollout envelope;
- `Q_dns_device_peak` = privacy-safe synthetic peak encrypted-DNS transaction rate for one representative supported device profile;
- `Q_dns_expected = N_dns_active_peak * Q_dns_device_peak`;
- `C_dns_expected` = approved expected encrypted-DNS concurrency if concurrency, rather than transaction rate, is the binding resource;
- `Q_dns_accept = 2 * Q_dns_expected`;
- `C_dns_accept = 2 * C_dns_expected`.

A target DNS envelope is capacity-PASS only when the exact production-representative implementation passes at 1× and 2× expected load while preserving TLS, DoH/DoT behavior, filtering correctness, Quad9 dns10/ECS-off, privacy, rate/abuse controls, and bounded latency/error behavior.

### 3.2 Accountless web/application workload

Let:

- `R_accountless_expected` = approved peak request/operation rate for the critical accountless journey;
- `C_accountless_expected` = approved expected concurrent accountless critical transactions;
- `R_accountless_accept = 2 * R_accountless_expected`;
- `C_accountless_accept = 2 * C_accountless_expected`.

The critical journey includes, once implemented, public/start -> accountless routing -> supported setup guidance -> verification response -> Protection Map -> troubleshooting/recovery/removal/help.

The currently accepted engineering thresholds inherited from TSK-0046/TSK-0538 are:

- critical-route p95 <=1.0 s;
- critical-route p99 <=2.0 s;
- accountless critical-path availability >=99.9% once operational.

A bounded load test proves only its tested window; it does not by itself prove a rolling operational SLO.

### 3.3 Optional-account workload

When the optional Version-1 account path exists, keep it separate from the accountless core:

- `R_session_expected` = expected peak sign-in/session establish/refresh operations;
- `R_dashboard_expected` = expected peak authorized dashboard/device reads;
- `R_mutation_expected` = expected peak register/update/unlink/delete/revoke operations;
- `C_account_expected` = expected concurrent account-only critical operations.

For each implemented critical account path, acceptance capacity is at least 2× its approved expected envelope with authorization/privacy/correctness intact. Authentication-provider, datastore, and AdGuard control/verification dependency quotas/latency/error budgets must be measured separately so a dependency bottleneck cannot be mislabeled as local host capacity.

Optional-account/provider failure must not turn a healthy accountless core into a whole-service failure.

### 3.4 Headroom calculation

For each tested critical path:

- `C_verified` = last verified sustained capacity envelope under the current exact release/configuration while all hard controls pass;
- `E_peak` = approved expected peak for that path;
- `Headroom_factor = C_verified / E_peak` where `E_peak > 0`.

Disposition:

- `Headroom_factor >= 2.0`: capacity margin meets the current acceptance rule for that envelope;
- `1.0 <= Headroom_factor < 2.0`: expected load may function but current capacity acceptance **fails**; reduce the supported/ramped load or correct/scale and retest;
- `Headroom_factor < 1.0`: target envelope is unsupported; do not ramp into it;
- no current valid `C_verified`: headroom is **UNPROVEN**, regardless of idle-resource snapshots.

The early review boundary `E_peak > 0.5 * C_verified` is algebraically equivalent to headroom falling below 2× and therefore requires review before expanding the supported envelope.

## 4. Governed scenarios

| Scenario | Lifecycle meaning | Real-user load before entry | Inputs that must be frozen | Capacity acceptance | Result now |
| --- | --- | ---: | --- | --- | --- |
| S0 — Pre-LG-09 | L5-L7 design/build/verification preparation | 0 | Synthetic test definitions only | No real-user capacity claim; prepare repeatable test method and observability | Model ready; throughput/headroom unproven |
| S1 — First bounded live-production validation/ramp (inherited WBS “pilot”) | Production-only first live users after LG-09 and all applicable prerequisites | 0 until activation | bounded device/user cap; per-device DNS synthetic profile; accountless request/concurrency envelope; optional-account envelope if enabled | Pass 1× and >=2× on each applicable critical path; no hard-control regression; alerts/recovery ready | Future conditional; no numeric envelope invented |
| S2 — Initial UK public-production expansion | After required continuation/readiness gates and current checks | only prior authorized production load | observed privacy-safe aggregate peak/trend; proposed public ramp cap; release/topology; support/recovery envelope | Current exact release/config passes >=2× proposed peak or ramp is reduced; no unresolved saturation/security/privacy/recovery blocker | Future conditional; no numeric envelope invented |
| S3 — Evidence-triggered routine scale review | When measured demand/headroom/support/reliability/cost triggers it | current authorized production | current observed aggregate workload, `C_verified`, bottleneck evidence, budget/authority | smallest reversible correction/scale action that restores >=2× margin, then retest | Triggered only by evidence |

No scenario creates a staging gate, public launch permission, legal completion, or a user-volume forecast.

## 5. Expected bottlenecks and required measurements

### 5.1 DNS service path

Potential bottlenecks, in diagnostic order:

1. encrypted edge CPU/TLS handshake/connection/file-descriptor/time-out limits;
2. DoH/DoT request/concurrency limits and per-client/global abuse controls;
3. the TSK-0411 DoT source-identity/rate-control boundary;
4. AdGuard Home CPU/memory/filter-processing behavior;
5. AdGuard rate-limit behavior (`20`, IPv4 `/24`, IPv6 `/56`, empty whitelist, `refuse_any=true`) under legitimate multi-client synthetic topology;
6. loopback/proxy transport behavior;
7. VM network path/NIC/connection capacity;
8. Quad9 dns10/network/upstream latency/error behavior;
9. TLS/certificate failure or renewal fault;
10. OS/service resource pressure.

DNS capacity measurements must use controlled synthetic/project-owned names. Queried domains, browsing history, top-domain analytics, identifiable per-client statistics, or retained raw client IP history are not capacity inputs.

### 5.2 Web/accountless path

Potential bottlenecks once implemented:

- Next.js/runtime CPU/memory/event-loop/process limits;
- TLS/reverse-proxy connection limits;
- content/runtime dependencies;
- server-side verification/AdGuard adapter latency;
- any minimum data store used by the approved design;
- network and external dependency latency;
- logging/telemetry overhead, which must remain privacy-minimal.

### 5.3 Optional-account path

Measure separately:

- Google/Firebase authentication quota/latency/availability;
- session creation/refresh/revocation behavior;
- persistence-store connection/query/write/locking behavior;
- dashboard/device ownership lookup and mutation behavior;
- server-only AdGuard adapter timeouts/retries/reconciliation;
- cross-parent authorization negative fixtures;
- accountless fallback while provider/datastore is unavailable.

A provider quota or outage is a dependency constraint, not evidence that the DNS or accountless host has reached capacity.

## 6. Alert and review thresholds

Capacity evidence and production observability must be able to evaluate at least the following current thresholds once the relevant path exists:

| Signal | Current threshold / condition | Required response |
| --- | --- | --- |
| Expected peak vs verified capacity | expected peak >50% of last verified sustained capacity | capacity review before ramp expansion; restore >=2× margin |
| CPU | >=70% for 15 min under representative sustained workload | diagnose binding process/path; do not scale blindly |
| Memory | >=75% for 15 min | diagnose growth/pressure/leak/cache; preserve safety margin |
| Relevant filesystem | >=70% used or evidenced growth erodes safe margin | identify bounded storage source; do not enable DNS/query history |
| p95/p99 latency | active target breached in two consecutive valid windows under expected legitimate load | investigate bottleneck; hold/reduce ramp until restored |
| Correctness/error budget | correctness/failure behavior consumes or projects exhaustion of applicable budget | hold ramp; repair and retest |
| TLS | any invalid/expired/mismatched supported endpoint certificate | stop affected activation/ramp; recover certificate |
| Abuse controls | legitimate topology repeatedly collides with rate/abuse limit | diagnose topology/edge control; never disable protections merely for throughput |
| Dependency | auth/datastore/AdGuard-control/upstream becomes measured bottleneck | isolate dependency; preserve accountless fallback and truthful state |
| Capacity incident | SEV-1/SEV-2 capacity-related incident | immediate remediation/recovery and full capacity revalidation before expansion |
| Control preservation | 2× cannot be achieved without weakening security/privacy/truth/recovery | reduce supported envelope or re-architect; never waive hard control |

Alert payloads and dashboards must not contain browsing/query history, top-domain views, secrets, raw auth tokens, or unnecessary persistent child/user identifiers.

## 7. Scaling options and authority boundaries

Scaling is evidence-driven. The decision sequence is: validate measurement -> isolate bottleneck -> correct proven inefficiency/defect -> retest -> reduce supported load if margin remains unproven -> scale only when justified.

### 7.1 Vertical options

Potential same-topology vertical actions include:

- increase CPU/memory capability of the DNS VM if CPU/memory is proven binding;
- increase web/app VM capability if the application runtime is proven binding;
- increase filesystem capacity only for legitimate operational/configuration/backup growth, never to retain prohibited DNS/query history;
- tune approved process/socket/connection settings only with before/after evidence and security/recovery review.

**Authority boundary:** CON-0004 keeps Azure control-plane provisioning/configuration owner-managed. This model may identify the required change; project execution must not resize/create/configure Azure resources unless a later explicit owner authority changes that boundary. Any material spend remains separately controlled.

### 7.2 Horizontal options

Horizontal scaling is not the default and is not authorized merely because it is architecturally possible.

Potential future options when evidence requires them:

- multiple same-region DNS nodes behind a production-capable encrypted-DNS edge while preserving one service identity and exact privacy/filter/upstream invariants;
- multiple web/app instances behind the approved application edge if the application becomes locally capacity-bound;
- datastore/read/write scaling only when the approved persistent model and measured workload require it;
- resilience/failover topology only after recovery/RTO and measured incident/capacity evidence justify the added operational/privacy/cost complexity.

Every horizontal change requires renewed testing of abuse/rate-limit behavior, client identity semantics, TLS, DNS correctness, verification truth, recovery/rollback, privacy/data flows, observability, deployment reproducibility, and cost. A new region is a separate architecture/privacy/market decision. **No US node or named-market activation is implied.**

## 8. Retest and re-architecture triggers

Re-run affected capacity verification when any of the following occurs:

1. S1/S2 user/device/request/concurrency cap is first frozen or materially changed;
2. privacy-safe synthetic per-device DNS workload characterization changes materially;
3. optional account/session/dashboard/device-management runtime is implemented or materially changed;
4. authentication-provider/datastore/AdGuard-control quota, latency, reliability, terms, or architecture materially changes;
5. AdGuard/Nginx/kernel/VM size/filter/upstream/edge/topology materially changes;
6. web/application architecture or critical route set changes;
7. supported device/network topology changes;
8. the >=2× verified margin is lost or unproven for the proposed envelope;
9. p95/p99/correctness/availability/resource alert patterns show sustained pressure;
10. a capacity/performance SEV-1/SEV-2 incident occurs;
11. abuse/rate-limit controls repeatedly impair legitimate supported clients;
12. recovery cannot preserve the supported envelope or accepted RTO without weakening a hard control;
13. optional-account load degrades the independently required accountless core;
14. a proposed topology/region/vendor change materially alters privacy/security/data-transfer or recovery assumptions.

**Re-architecture rather than routine scale** is required when the existing topology cannot preserve hard privacy/security/authorization/truth/recovery controls at the needed envelope, when a single-node/recovery design cannot meet accepted objectives despite bounded tuning/vertical options, or when horizontal/region/vendor changes alter trust/data boundaries materially.

## 9. Capacity evidence required before a load claim

A claim that a given envelope is supported requires a versioned result containing:

- exact source commit/release and relevant configuration hashes/versions;
- exact test target/environment and resource shape;
- approved expected envelope and its source;
- synthetic workload definition and fixture source;
- 1× and >=2× workload results;
- p50/p95/p99 where applicable plus attempted/successful/failed/correctness counts;
- CPU/memory/filesystem/network/connection saturation evidence appropriate to the bottleneck;
- TLS/filter/upstream/security/privacy/rate-limit/authorization invariants;
- optional-account and accountless results separated;
- dependency quota/error/latency evidence where applicable;
- alert behavior and recovery/rollback result;
- deviations, supported cap, and disposition.

Until this exists for a concrete envelope, `C_verified` and numeric headroom remain **UNPROVEN**.

## 10. Risk, privacy and legal constraints preserved

- RSK-0001 remains open; this task does not treat the deferred legal/ICO/UK-representation condition as satisfied.
- RSK-0002 remains the accepted integrated-product-first human-validation risk; no behavioral evidence is invented.
- RSK-0006/RSK-0007 capacity/outage/abuse risks remain active and are addressed through synthetic health, alerts, headroom, abuse controls, recovery and evidence-driven scaling.
- CON-0007 and CON-0008 remain hard: persistent identifiable query/file logs and identifiable per-client statistics remain off/excluded except separately authorized time-boxed diagnostics.
- INT-0006 legal/privacy constraints remain inputs; this model creates no unsupported legal conclusion.
- INT-0007 actual data-flow reality remains downstream evidence: implemented behavior must later match the approved inventory/notices/DPIA or block release.

## 11. ACC-0236 trace

| ACC-0236 element | Evidence in this artifact | Disposition |
| --- | --- | --- |
| assumptions / calculations | Sections 1–3; explicit variables, equations, 2× rule and non-inference boundaries | SATISFIED |
| pilot / launch scenarios | Section 4 maps inherited pilot wording to S1 live-production validation/ramp and S2 UK public expansion | SATISFIED |
| bottlenecks | Section 5 separates DNS, accountless web, optional account and dependencies | SATISFIED |
| headroom | Section 3.4 defines `C_verified`, `E_peak`, headroom factor and pass/fail semantics | SATISFIED |
| alert thresholds | Section 6 preserves current quantitative and event thresholds | SATISFIED |
| vertical / horizontal scaling | Section 7 gives bounded options and Azure/material-spend/region authority fences | SATISFIED |
| retest / re-architect trigger | Section 8 defines objective triggers and distinction | SATISFIED |

## 12. Stable task conclusion

**Candidate ACC-0236 disposition: PASS**, subject to VER-0236 read-back/reviewer inspection of this exact artifact.

This PASS, if verified, means the required L5 capacity model exists and is traceable to current predecessors. It does **not** mean production capacity has been load-tested, a numeric live-user envelope is approved, Azure has been scaled, LG-07 has passed, L6 is authorized, legal prerequisites are complete, or production/user activation is permitted.
