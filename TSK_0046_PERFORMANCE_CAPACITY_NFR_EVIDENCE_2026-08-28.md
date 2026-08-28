# TSK-0046 — Performance and Capacity NFR Verification Evidence

**Task:** TSK-0046 — Define performance and capacity NFRs  
**Acceptance:** ACC-0046  
**Verification:** VER-0046 — independent load-model/performance/capacity/privacy audit  
**Evidence:** EVD-0046  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- Performance/capacity contract: `TSK_0046_PERFORMANCE_CAPACITY_NFR_2026-08-28.md`
- Contract blob: `2c48f975d557b1bb4ba6c58c2a8ad3580b2c7b06`
- Contract creation commit: `76a13870227b4a036003988ba141aea473d6f29a`
- Current selected runtime before execution: `CURRENT_STATE.md` blob `6928e90935f892587a40d3b4586e3e2f86e29e3e`; TSK-0046 selected as L4 / MEDIUM / A3 / AUTO_ALLOWED with hard dependency TSK-0538 current PASS.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`; WBS owns ACC-0046 and the dependency/action-authority definition while `CURRENT_STATE.md` owns volatile execution state.
- Host baseline evidence: `TSK_0046_HOST_CAPACITY_BASELINE_EVIDENCE_2026-08-28.md`, blob `f43d237b3f6a7135aa498ce4627f8cd7ca59682e`; read-only host capture run `33204389341`, job `98961605638`.
- Current approved AdGuard configuration: `infrastructure/adguard-server/approved-adguard-config-v1.json`, blob `e9975c4e75c2a68131f049da942468d8d1952d8d`.
- Direct predecessor TSK-0538 remains current PASS and owns the provisional service-level targets/alert/recovery framework.
- Current Google/web.dev Core Web Vitals guidance checked 2026-08-28: `https://web.dev/articles/vitals` and `https://web.dev/articles/defining-core-web-vitals-thresholds`; good thresholds remain p75 LCP <=2.5s, INP <=200ms, CLS <=0.1.

## 2. Eligibility and authority audit

The post-TSK-0044 derived queue contained three candidates: TSK-0187 with real/behavior-evidence preflight, unflagged TSK-0046, and TSK-0140 with owner-review preflight. The corrected guarded selector verified the WBS definition/edge and the live TSK-0538 PASS from `CURRENT_STATE.md`, then selected TSK-0046 successfully.

An earlier selector attempt incorrectly treated the WBS frozen `Execution_State` column as live runtime truth and failed before mutation. Canonical `CURRENT_STATE_INTERFACE.md` and Layer 5 establish that volatile execution state is owned by repository `CURRENT_STATE.md`, while WBS owns task/dependency definitions. The selector was corrected accordingly; no planning file was mutated.

**Result: PASS.**

## 3. ACC-0046 expected-pilot-load audit

ACC-0046 requires the NFR to state expected pilot load. Higher-authority project constraints simultaneously prohibit fabrication and CR-0003/DEC-0050 currently defer real-participant activation.

The contract therefore does not invent a future participant or device count. It states the complete current truth:

- currently authorized real-participant pilot load = **0 real-participant devices while CR-0003 remains active**;
- future planned numeric cohort = **UNFROZEN / not currently numerically authorized**;
- before reactivation, expected DNS peak must become numeric from the approved `N_active_peak` and a privacy-safe measured/synthetic `Q_device_peak` using `Q_pilot_expected = N_active_peak × Q_device_peak`.

Repository searches for a frozen numeric pilot sample/cohort in the current planning material did not return an authoritative numeric value, and the PKG-03/lifecycle package summaries route detailed execution facts to the WBS/registers rather than declaring a current numeric cohort.

This is the only acceptance interpretation compatible with both ACC-0046 and the higher-authority no-fabrication/gate rules. **TSK-0046 PASS does not mean a future numeric pilot size has been approved.** The contract explicitly reopens when that cohort/load becomes numeric.

**Result: PASS for the current provisional L4 definition scope.**

## 4. Host-baseline grounding audit

The read-only production capture was deliberately separated from repository publication and used `contents: read` only on the accepted `adguardvm` machine identity. It observed:

- 2 logical CPUs;
- ~3.82 GiB RAM with ~77.8% available at capture;
- ~28.02 GiB root filesystem with 14% used;
- near-zero instantaneous load;
- AdGuardHome/Nginx active;
- AdGuardHome ~149.7 MiB RSS and Nginx ~27.4 MiB RSS.

The contract correctly labels this a point-in-time idle/resource baseline and explicitly refuses to infer QPS or maximum capacity from it.

No DNS/domain/query/client/user data was read.

**Result: PASS.**

## 5. Safety-margin audit

The contract defines a **2× verified capacity margin over the future approved expected peak**. This is an internal provisional acceptance design choice, not a statement that the host is already proven to have that capacity and not a public SLA.

It requires separate 1× and 2× synthetic acceptance stages and keeps correctness, latency, availability, privacy, filtering, TLS, administration and abuse controls intact at the safety-margin point. If the 2× margin cannot be proven safely, supported/approved load must be reduced or architecture/capacity reviewed before activation.

This preserves CON-0018's lean single-node/no-HA baseline while making the safety margin measurable.

**Result: PASS.**

## 6. DNS latency/availability test-method audit

Sections 5–6 define a reproducible privacy-safe method:

- fixed controlled/project-owned synthetic inputs only;
- separate DoH and DoT paths;
- allowed and blocked correctness;
- TLS/hostname/chain and upstream/filtering behavior;
- staged baseline -> 1× expected -> 2× expected -> optional isolated bounded burst;
- p50/p95/p99, transaction failure classes and CPU/memory/disk/service health;
- exact release/configuration binding;
- no raw user query/domain/client history.

The contract correctly carries forward TSK-0538's p95 <=1s / p99 <=2s and availability/correctness targets while explicitly refusing to claim that a bounded load-test window proves a 30-day SLO.

**Result: PASS.**

## 7. Abuse-control/capacity distinction audit

The contract preserves the approved `ratelimit=20`, IPv4 `/24`, IPv6 `/56`, empty whitelist and `refuse_any=true` controls.

It explicitly prevents a common benchmarking error:

- a single test source reaching the rate limit demonstrates the source/subnet protection boundary, not server capacity;
- production controls may not be disabled/raised or whitelisted merely to inflate benchmark throughput;
- aggregate capacity above one-source constraints must use multiple controlled synthetic vantage points or an isolated equivalent environment with production security semantics;
- a future legitimate NAT/topology collision becomes a security/product compatibility review rather than an automatic rate-limit weakening.

**Result: PASS.**

## 8. Web-journey performance audit

The web/application section is explicitly dormant until implementation exists.

It nevertheless makes ACC-0046 measurable by defining:

- the critical synthetic journey from public/start through accountless routing/setup/verification/Protection Map/recovery;
- TSK-0538 service targets for backend availability/latency;
- current Core Web Vitals pre-release targets: p75 LCP <=2.5s, INP <=200ms, CLS <=0.1;
- mobile/desktop segmentation where supported;
- a strict distinction between synthetic/lab evidence and authorized field p75 evidence;
- any later privacy-safe field telemetry remains governed by TSK-0497/0230 without stable identity/browsing-history telemetry.

Current web.dev guidance also notes that SPA soft-navigation measurement support is evolving in 2026, so the contract appropriately uses current thresholds without hard-coding one future SPA telemetry implementation.

**Result: PASS.**

## 9. Capacity-review-trigger audit

Section 8 defines early-review triggers below incident thresholds:

- expected peak >50% of last verified sustained envelope (2× margin no longer proven);
- CPU >=70% for 15m under representative sustained load;
- memory >=75% for 15m;
- filesystem >=70% or evidenced growth eroding margin;
- consecutive p95/p99 target breaches;
- SLO error-budget consumption/projected exhaustion;
- verified legitimate rate-limit/security-control collision;
- measured upstream bottleneck;
- material software/filter/topology change;
- material cohort/concurrency growth;
- SEV-1/SEV-2 capacity incident;
- inability to preserve 2× margin without weakening a hard control.

These are explicitly planning-review triggers, not page alerts. TSK-0538 remains alert/severity authority.

**Result: PASS.**

## 10. Degradation-behavior audit

Section 9 prioritizes encrypted DNS correctness, TLS, filtering, privacy and abuse protection ahead of optional work; forbids enabling logs/tracking or broadening `/control`, plain DNS, credentials/firewall exposure; preserves truthful Protection Map state and recovery/removal guidance; and requires reducing supported load/claim rather than weakening hard controls.

The future web/app must shed noncritical analytics/content/background work before the critical setup/recovery path.

**Result: PASS.**

## 11. Scale-decision audit

Crossing a capacity trigger does **not** automatically authorize scaling. Section 10 requires measurement verification, bottleneck isolation, safe defect/efficiency correction, rerun, possible supported-load reduction, and only then an owner-authorized resize/topology/HA evaluation if evidence proves need.

This preserves CON-0018 and the Azure owner boundary.

**Result: PASS.**

## 12. Verification disposition

**VER-0046 independent audit result: PASS for ACC-0046's provisional internal L4 performance/capacity-NFR-definition scope.**

The read-back contract at blob `2c48f975d557b1bb4ba6c58c2a8ad3580b2c7b06` covers every ACC-0046 domain: expected pilot load, safety margin, DNS latency/availability test method, future web journey performance, degradation behavior and measurable capacity-review triggers.

The following remain OPEN/non-PASS and are not converted by this result:

- a future numeric real-participant cohort/load;
- any synthetic maximum-capacity or QPS result;
- production stress testing;
- future web/app implementation or field performance evidence;
- infrastructure scaling or HA;
- `DVR-0230-01`, `DVR-0484-01`, `GAP-0484-02`;
- real-user/behavioral evidence (`RSK-0002`);
- final legal/privacy/participant gates;
- build/publication/launch.

**Runtime may move TSK-0046 to PASS only after this evidence file is persisted/read back and a guarded reconciliation verifies the current selection, exact contract/evidence/baseline/runtime preconditions.**
