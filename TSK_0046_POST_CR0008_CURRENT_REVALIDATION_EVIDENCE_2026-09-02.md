# TSK-0046 — Post-CR-0008 Current Revalidation Evidence

**Task:** TSK-0046 — Define performance and capacity NFRs  
**Acceptance / Verification / Evidence:** ACC-0046 / VER-0046 / EVD-0046  
**Date:** 2026-09-02 UTC  
**Disposition:** **PASS** for the current L4 performance/capacity-NFR definition only.

## 1. Current authority and eligibility

Canonical inputs independently audited:

- WBS `Plans/Master/WBS/master-wbs.csv` — blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship graph `Plans/Master/RELATIONSHIP_INDEX.yaml` — blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `CURRENT_STATE.md` — blob `b0e320a862eaf83b3fea11e565b42621608578eb`.

Exact current WBS row proves:

- lifecycle `L4`;
- priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- dependency exactly `TSK-0538`;
- ACC/VER/EVD exactly `ACC-0046 / VER-0046 / EVD-0046`.

Read-only current-contract audit run/job `33581119932 / 100095430473`: **SUCCESS**. It proved current WBS/dependency authority, current TSK-0538 PASS, historical engineering-core reuse, stale historical CR-0003/pilot sequencing, current dual-mode reliability input and current CR-0006/CR-0007 scope.

## 2. Current accepted candidate artifact

Current artifact:

- `TSK_0046_POST_CR0008_DUAL_MODE_PERFORMANCE_CAPACITY_NFR_REVALIDATION_2026-09-02.md`;
- version `2.0.0-post-CR0008`;
- blob `8e72d542b68de6f7f5c8c375b63b6229c6d15529`;
- publication commit `0fbc382c94850fb02376c6f3105a1ea499fa7398`.

Historical compatible proof retained:

- `TSK_0046_PERFORMANCE_CAPACITY_NFR_2026-08-28.md` — blob `2c48f975d557b1bb4ba6c58c2a8ad3580b2c7b06`;
- `TSK_0046_PERFORMANCE_CAPACITY_NFR_EVIDENCE_2026-08-28.md` — blob `09d111530c5e9c86feb2cafb54f62fb046a44b6f`.

The current artifact preserves the accepted 2× verified capacity margin, controlled synthetic DoH/DoT/TLS/filter correctness method, p50/p95/p99 evidence, hard security/privacy/rate-limit invariants, degradation rules and early capacity-review triggers. It supersedes only stale separate-pilot/CR-0003 sequencing and accountless-only future-web capacity scope.

## 3. Current predecessor proof

Current direct predecessor TSK-0538 is current PASS:

- artifact `TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md` — blob `44c9c299465e821e2ffd84a54b77e3e615d61925`;
- evidence `TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md` — blob `3ba04601ea5574fcd1fb1f58f95922ae94b74ac2`.

TSK-0046 binds current DNS/accountless plus optional session/dashboard/device/provider/datastore reliability boundaries without redefining TSK-0538 service-level ownership.

## 4. Current external source review

First-party web.dev sources were reviewed on 2026-09-02:

- `https://web.dev/articles/vitals`;
- `https://web.dev/articles/defining-core-web-vitals-thresholds`;
- `https://web.dev/articles/vitals-spa-faq`.

The current artifact records the still-current Core Web Vitals good thresholds LCP `<=2.5s`, INP `<=200ms`, CLS `<=0.1` at the 75th percentile and the August 2026 soft-navigation measurement caveat. These references are engineering inputs only; no field/RUM compliance or browser-universal soft-navigation support is inferred.

## 5. Independent VER-0046

Final verifier:

- script `.github/scripts/verify_tsk0046_current_revalidation_v3.py` — blob `340ed4864cf6c63f8c163bb5852a9f16f7de4aa3`;
- workflow `.github/workflows/verify-tsk0046-current-revalidation-v3.yml` — blob `22707f3ee628c2421a5707fdc7ec09b365309d98`;
- GitHub-hosted Ubuntu 24.04 runner;
- workflow permissions: `contents: read`;
- run/job `33581514882 / 100096620942`: **SUCCESS**.

Terminal evidence markers:

- `TSK0046_V3_INPUT_HASHES=PASS`;
- `TSK0046_V3_WBS=PASS`;
- `TSK0046_V3_PREDECESSOR=PASS`;
- `TSK0046_V3_LOAD_SCOPE=PASS`;
- `TSK0046_V3_MARGIN_DNS=PASS`;
- `TSK0046_V3_DUAL_MODE_PERFORMANCE=PASS`;
- `TSK0046_V3_WEB_PERF=PASS`;
- `TSK0046_V3_TRIGGERS_DEGRADATION=PASS`;
- `TSK0046_V3_RECONCILIATION=PASS`;
- `TSK0046_V3_NON_INFERENCE=PASS`;
- `TSK0046_CURRENT_ACC=PASS`;
- `TSK0046_CURRENT_VER=PASS`;
- `TSK0046_CURRENT_EVD_READY=PASS`;
- `TSK0046_CURRENT_REVALIDATION=PASS`.

Earlier verifier runs are retained as diagnostic-only failures:

- v1 run/job `33581329346 / 100096056039` failed after preceding substantive checks because it searched for contiguous prose `controlled block` while the artifact correctly states `controlled allow and block behavior`;
- v2 run/job `33581430881 / 100096368646` failed after authority/WBS/predecessor/load-scope checks because it required the literal phrase `hard control` inside the safety-margin section even though that section structurally preserves correctness/security/privacy/rate-limit invariants.

Neither diagnostic run mutated governed state or changed the accepted candidate. The v3 verifier uses section-level semantic concepts with explicit missing-concept diagnostics rather than brittle exact-prose matching.

## 6. ACC-0046 disposition

ACC-0046 requires expected pilot load, safety margin, DNS latency/availability test method, web journey performance, degradation behavior and a capacity-review trigger.

Current proof:

- the inherited `expected pilot load` phrase is reconciled to the bounded first live-production validation/ramp envelope after LG-09, with current real-user load truthfully `0` and future cohort/load `UNFROZEN`;
- DNS, accountless-web and optional-account load models are distinct and privacy-safe;
- 2× verified capacity margin is retained for every implemented load-bearing critical path;
- DNS methodology covers DoH/DoT/TLS/allow+block correctness, controlled synthetic inputs, latency/error/resource evidence and rate-limit interaction;
- web performance covers the complete accountless core plus the optional account/session/dashboard/device lifecycle and current browser-performance inputs;
- degradation preserves DNS/accountless safety, authentication/authorization/privacy/reconciliation hard controls and truthful protection states;
- capacity-review triggers are measurable and precede unsafe normalization of incident conditions.

**ACC-0046 = PASS.**  
**VER-0046 = PASS.**  
**EVD-0046 = SATISFIED.**  
**TSK-0046 current dependency-complete revalidation = PASS.**

## 7. Non-inference

This evidence does not authorize or prove live-production activation, any real-user cohort/load, production stress testing, infrastructure resize/HA/new paid monitoring, web/app/account/auth implementation, provider/datastore architecture approval, legal/privacy completion, participant processing, publication/payment/market activation/launch, or any successor PASS.
