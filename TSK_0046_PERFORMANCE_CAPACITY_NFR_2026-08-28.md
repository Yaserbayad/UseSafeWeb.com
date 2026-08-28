# TSK-0046 — Performance and Capacity NFRs

**Task:** TSK-0046 — Define performance and capacity NFRs  
**Acceptance:** ACC-0046  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 PERFORMANCE/CAPACITY CONTRACT / LOAD TEST, SCALE PURCHASE OR RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0538 + CON-0018/0021/0023 + current DNS security/privacy/runtime evidence + current host baseline + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and evidence limitation

This contract defines the minimum performance and capacity behavior for the current single-node UseSafeWeb encrypted-DNS service and the future separate web/application runtime if and when that application is legitimately built.

It does **not**:

- authorize real-participant load, Experiment 1 activation or public launch;
- forecast adoption, active users, households or DNS query volume;
- claim a maximum QPS for the current DNS host;
- authorize production stress testing, Azure resizing, HA/multi-node DNS or additional paid infrastructure;
- weaken AdGuard rate limiting, privacy controls, TLS, filtering or administration boundaries to improve benchmark results;
- claim performance for an unbuilt web application.

`RSK-0002` remains OPEN. Real-user completion, comprehension, preference and support burden are not inferred from synthetic performance results.

## 2. Expected pilot load — current truthful state and derivation rule

ACC-0046 requires an expected pilot load. The current canonical project does **not** freeze a numeric future participant/device cohort, and CR-0003/DEC-0050 currently defers real-participant activation. Therefore a made-up future user/device count would violate CON-0021 and the evidence rules.

The correct current load statement is:

- **currently authorized real-participant pilot load: 0 real-participant devices while CR-0003 remains active**;
- **future planned pilot cohort size: UNFROZEN / not currently numerically authorized**;
- the future expected DNS peak becomes numeric only after both the cohort and a privacy-safe per-device workload characterization are approved/evidenced.

When reactivated, define:

- `N_active_peak` = approved maximum simultaneously active supported devices for the pilot window;
- `Q_device_peak` = privacy-safe synthetic characterization of a supported device's peak DNS transaction rate for the approved workload model;
- `Q_pilot_expected = N_active_peak × Q_device_peak`;
- `C_pilot_expected` = approved simultaneous encrypted-DNS transaction/concurrency model if concurrency rather than QPS is the binding resource.

Neither `N_active_peak` nor `Q_device_peak` may be inferred from browsing history, DNS logs or a generic Internet average. The workload characterization must use controlled synthetic/project-owned names and explicit assumptions.

## 3. Engineering safety margin

The initial single-node architecture is accepted only while it retains a **minimum 2× verified capacity margin over the approved expected pilot peak**.

For the applicable release/configuration:

1. a privacy-safe synthetic test must pass at `1.0 × Q_pilot_expected`;
2. the same acceptance invariants must pass at `2.0 × Q_pilot_expected` (the safety-margin point);
3. DoH/DoT correctness, latency and availability targets must remain satisfied at the safety-margin point;
4. privacy/security/filtering/admin/listener invariants must remain unchanged;
5. no production security control may be disabled merely to reach the target load;
6. if 2× cannot be proven safely, the release/pilot load must be reduced or capacity/architecture reviewed before activation.

This **2× rule is a planning and acceptance margin**, not a claim that the host's true maximum is exactly 2× expected load. The maximum sustainable envelope may be higher and should only be recorded after controlled testing.

## 4. Current host baseline — evidence, not capacity proof

Read-only production capture on 2026-08-28 (run `33204389341`, job `98961605638`; evidence `TSK_0046_HOST_CAPACITY_BASELINE_EVIDENCE_2026-08-28.md`) observed:

- 2 logical CPUs, Intel Xeon Platinum 8370C @ 2.80GHz;
- 4,105,707,520 bytes total RAM (~3.82 GiB);
- ~22.2% memory used and ~77.8% available at capture time;
- 30,084,825,088-byte root filesystem (~28.02 GiB), 14% used;
- 1m/5m/15m load 0.00/0.02/0.00;
- AdGuardHome and Nginx active;
- AdGuardHome RSS ~149.7 MiB and CPU snapshot 0.0%;
- Nginx total RSS ~27.4 MiB.

The host was lightly loaded at that instant. **No QPS or concurrency capacity is inferred from this idle baseline.**

## 5. DNS latency/availability/correctness test method

### 5.1 Test inputs

Use only fixed project-owned or otherwise controlled synthetic names/answers designed for testing. Never replay or sample participant/customer DNS traffic.

The test suite must separately cover:

- valid DoH on the approved `/dns-query` path;
- valid DoT on TCP 853;
- controlled allowed-domain behavior;
- controlled blocked-domain behavior;
- TLS hostname/chain validity;
- upstream/filtering correctness;
- removal/recovery checks where the test objective includes client configuration.

### 5.2 Load stages

Once `Q_pilot_expected` is legitimately defined:

1. low-rate functional baseline;
2. `1×` expected peak steady-state;
3. `2×` expected peak safety-margin steady-state;
4. a bounded short burst above 2× only on an isolated/reversible target when useful to locate headroom/bottlenecks.

Each steady-state stage must run long enough to expose stable latency/resource behavior; the implementation test plan must record the exact duration and warm-up rule rather than silently mixing warm-up with measurement.

### 5.3 Measurements

Record only aggregate/synthetic operational data:

- scheduled/attempted/successful/failed synthetic transactions;
- timeout/TLS/protocol/correctness failure counts by controlled error class;
- latency histogram with p50/p95/p99;
- CPU utilization/load;
- memory utilization/pressure;
- disk utilization/free capacity;
- AdGuard/Nginx health;
- exact software/config release under test.

No raw user query/domain/client history is required or permitted.

### 5.4 Performance acceptance

At both 1× and 2× expected peak, the active TSK-0538 provisional DNS targets apply:

- DoH transaction availability >=99.9% over its defined operating window;
- DoT transaction availability >=99.9%;
- synthetic DNS correctness >=99.9%;
- synthetic encrypted-DNS latency p95 <=1.0 s and p99 <=2.0 s;
- TLS validity 100%.

A load-test window is not a 30-day operating window, so it must not falsely claim the 30-day SLO is proven. Instead, every attempted transaction in the bounded test window must be reported and any failure classified; the test is unacceptable if its observed failures/latency would violate the same SLO thresholds or expose a correctness/privacy/security defect.

## 6. Rate-limit and security-control interaction

The current approved production AdGuard configuration includes:

- `ratelimit=20`;
- IPv4 aggregation `/24`;
- IPv6 aggregation `/56`;
- empty rate-limit whitelist;
- `refuse_any=true`.

Those controls are security requirements, not benchmark obstacles.

Therefore:

- never disable/raise rate limiting or add a production whitelist merely to demonstrate high throughput;
- a single test source or shared `/24` hitting the configured limit proves only the source/subnet abuse boundary, **not server saturation**;
- aggregate server-capacity testing above a single-source boundary must use multiple explicitly controlled synthetic source networks/vantage points or an isolated equivalent test target with the same production security semantics;
- if legitimate approved pilot topology would cause many devices behind one NAT `/24` to collide with the current limit, treat that as a product/security compatibility issue requiring evidence-driven review—not as permission to silently weaken the control.

## 7. Future web/application journey performance

This section is **inactive until the web/app exists**. It defines acceptance targets only.

### 7.1 Critical synthetic journey

The future application test must exercise at minimum:

`public/start -> accountless routing -> supported setup guidance -> verification response -> Protection Map -> recovery/removal/help route`

without requiring an account or persistent customer history.

### 7.2 Backend/application service targets

Preserve the TSK-0538 provisional internal targets:

- critical synthetic application transaction availability >=99.9% over rolling 30 days once operational;
- critical-route/dependency response latency p95 <=1.0 s and p99 <=2.0 s over the defined rolling window;
- bounded-cardinality route/status/dependency metrics only; no user identity, raw URL, journey token or DNS/domain labels.

### 7.3 Browser/user-visible targets

Current Google/web.dev Core Web Vitals guidance checked on 2026-08-28 defines the `good` thresholds at the 75th percentile as:

- Largest Contentful Paint (LCP) <=2.5 s;
- Interaction to Next Paint (INP) <=200 ms;
- Cumulative Layout Shift (CLS) <=0.1.

Source: `https://web.dev/articles/vitals` and `https://web.dev/articles/defining-core-web-vitals-thresholds`.

Use these as provisional pre-release targets for the supported web journey, segmented at minimum by mobile/desktop where the measurement method supports it. Before real-user telemetry is authorized, synthetic/lab results may prove implementation quality but **must not be mislabeled as field p75 compliance**.

If privacy-safe aggregate field Web Vitals are later authorized, their event/schema/retention design must comply with TSK-0497/0230 and must not introduce stable user identity or browsing-history telemetry.

## 8. Resource headroom and early capacity-review thresholds

The following are **provisional early-review thresholds**, intentionally lower than the TSK-0538 incident-risk thresholds. Crossing one does not itself prove an outage; it triggers capacity analysis before margin is lost.

Review capacity when any of the following is observed under an approved representative synthetic/operating workload:

1. `Q_pilot_expected` grows above **50% of the last verified sustained capacity envelope**, so the 2× safety margin is no longer proven;
2. CPU is **>=70% for 15 minutes** during representative sustained load;
3. memory utilization/pressure is **>=75% for 15 minutes** during representative sustained load;
4. root/service filesystem is **>=70% used** or shows an evidenced growth trend that would materially erode safe operating margin;
5. p95/p99 DNS or web critical-path latency breaches its active target in two consecutive valid measurement windows under expected legitimate load;
6. transaction failures/correctness errors consume or project exhaustion of the applicable SLO error budget;
7. a verified legitimate client/topology repeatedly collides with rate limiting or other security capacity controls;
8. upstream Quad9 latency/error behavior becomes the measured bottleneck rather than local compute;
9. a material AdGuard/Nginx/kernel/filter-list/application version or topology change invalidates the last capacity evidence;
10. the approved cohort/device concurrency materially increases;
11. a SEV-1/SEV-2 capacity-related incident occurs;
12. a recovery/change cannot preserve the 2× margin without weakening another hard control.

These thresholds are planning triggers, not pages by themselves. TSK-0538 remains authority for operational alert severity.

## 9. Degradation behavior

When load or resource pressure threatens the accepted performance envelope:

1. preserve encrypted DNS correctness, TLS, filtering, privacy and abuse protections before optional features;
2. do not enable query logging/statistics or customer tracking to diagnose normal capacity pressure;
3. stop or defer nonessential administrative mutations/maintenance jobs if they contribute materially to user-facing degradation;
4. preserve truthful TSK-0320 state semantics—uncertain verification cannot be presented as protected;
5. preserve removal/recovery guidance if UseSafeWeb contributes to connectivity loss;
6. for the future web/app, shed/defer noncritical analytics/content refresh/background work before the critical accountless setup/recovery path;
7. do not broaden `/control`, plain DNS, credentials, firewall exposure or logging to recover throughput;
8. if safety/privacy/security controls cannot be preserved within the required performance envelope, reduce supported load/availability claim and escalate rather than fail open.

## 10. Capacity-review decision order

Crossing a trigger starts diagnosis, not automatic scaling.

Decision order:

1. verify the measurement and distinguish monitor/test-source failure from target failure;
2. isolate bottleneck: local CPU/memory/disk, Nginx/TLS, AdGuard/filtering, upstream, network, rate-limit topology, or future application dependency;
3. remove a verified defect/inefficiency only when correctness/security/privacy remain intact;
4. rerun the bounded regression/capacity test;
5. reduce the supported/approved load if the margin still cannot be proven safely;
6. only then evaluate resize/topology/HA if evidence shows real need and the applicable owner/Azure/action authority approves it.

No automatic multi-node/HA purchase is created by this NFR. `CON-0018` remains the single-node baseline until evidence justifies a governed change.

## 11. Revalidation triggers

Reopen affected TSK-0046 evidence when:

- the future pilot cohort/load becomes numerically approved;
- the per-device synthetic workload model changes materially;
- AdGuard/Nginx/kernel/host VM size/filter policy/upstream changes materially;
- the future web/app is implemented or materially changes;
- supported device/network topology changes;
- the current 2× margin is no longer evidenced;
- a capacity/performance incident occurs;
- a security/privacy control materially changes the workload path;
- current Web Vitals definitions/thresholds materially change.

## 12. Testable assertions

A downstream implementation/QA plan must be able to prove at least:

1. no numeric future real-user cohort was invented before authority freezes it;
2. current real-participant load remains zero while CR-0003 defers activation;
3. expected pilot peak is derived from explicit `N_active_peak` and privacy-safe workload characterization;
4. 1× and 2× expected-peak tests are separately measured;
5. DoH and DoT are both exercised;
6. allowed and blocked synthetic correctness are both exercised;
7. p50/p95/p99 and error counts are recorded;
8. host CPU/memory/disk/service health are recorded without user/query telemetry;
9. production abuse/privacy/filtering/TLS controls remain intact during tests;
10. single-source rate limiting is not mislabeled as total host capacity;
11. web/app targets remain inactive until implementation exists;
12. browser targets distinguish lab/synthetic from authorized field evidence;
13. capacity-review triggers are evaluated before incident thresholds become normal operating targets;
14. degradation never weakens encryption/filtering/privacy/admin/firewall boundaries;
15. crossing a trigger causes evidence-driven review rather than automatic HA purchase;
16. exact release/config/environment is bound to every capacity result.

## 13. ACC-0046 traceability

ACC-0046 requires:

> NFRs state expected pilot load, safety margin, DNS latency/availability test method, web journey performance, degradation behavior, and capacity-review trigger.

Coverage:

- **Expected pilot load:** §2 states the exact current authorized load (zero real participants under CR-0003), explicitly records the future numeric cohort as unfrozen, and defines the deterministic future load formula without fabrication.
- **Safety margin:** §3 requires a 2× verified capacity margin over the future approved expected peak.
- **DNS latency/availability test method:** §§5–6 define synthetic inputs, load stages, measurements, SLO binding and security/rate-limit handling.
- **Web journey performance:** §7 defines the future critical journey, TSK-0538 service targets and current Core Web Vitals pre-release targets while distinguishing lab from field evidence.
- **Degradation behavior:** §9 preserves critical service/security/privacy/correctness before optional work and forbids unsafe fallback.
- **Capacity-review trigger:** §§8 and 10 define measurable early thresholds and the evidence-driven decision path.

## Stable task outcome candidate

**TSK-0046 result: PASS candidate for provisional internal L4 performance/capacity-NFR definition only, subject to independent verification, GitHub read-back and runtime reconciliation.**

This result does not authorize real-participant load, production stress testing, infrastructure scaling, HA, web-app implementation, publication or launch.
