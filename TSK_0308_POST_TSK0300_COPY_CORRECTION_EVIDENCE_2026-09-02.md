# TSK-0308 — Protection-State Copy Correction Evidence After Current TSK-0300

**Task / Acceptance / Verification / Evidence:** TSK-0308 / ACC-0308 / VER-0308 / EVD-0308  
**Date:** 2026-09-02 UTC  
**Result:** PASS candidate for guarded runtime reconciliation; no successor or lifecycle-gate PASS inferred.

## 1. Immutable evidence index

- Canonical WBS blob: `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.
- Canonical relationship-index blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-reconciliation runtime blob: `960f8449943552a6c7a8b747b0d9b072f8eaa507`.
- Correction artifact: `TSK_0308_POST_TSK0300_COPY_CORRECTION_REVALIDATION_2026-09-02.md`, blob `76d652481a993469aaf175c08893e829ee01dad7`, publication commit `51d039c9d97f2ff48a048201ef9b23673021ebfa`.
- Corrected active addendum: `prototype/TSK-0308/DUAL_MODE_ADDENDUM.md`, blob `86461ef4baac27cf4cfd906f7ed464781186e78d`, correction commit `f4c479d90299db6fb87ea9b62ea9fcc8f92c6039`.
- Corrected active rendered reference: `prototype/TSK-0308/dual-mode-reference.html`, blob `7e522e23e43d04da3facf53747ad9b245e66ef62`, correction commit `6df3d4fa1c839841e651fa3f7c2abd9aabafe089`.
- Current corrected TSK-0300 evidence: `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md`, blob `a3e39896b67098ced321cb9e4b82c65c440806e4`; runtime reacceptance commit `93fea25db8c1b6fd70a8fd45e0ff531cf33ea2e1`.
- Current TSK-0320 state/copy authority: `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md`, blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.
- Current TSK-0309 baseline: `prototype/TSK-0309/BASELINE.md`, blob `6302bb2509d04c8269e4df112140d7c416e42eff`.
- Structural verifier: `.github/scripts/verify_tsk0308_post_copy_correction.py`, blob `3c364d588fd4d89407c2db8223cf4fe34f0b865f`.
- Read-only workflow: `.github/workflows/verify-tsk0308-post-copy-correction.yml`, blob `f35da0b77340e68b3247eb1a547c11ba02a6faa4`.
- Diagnostic PR `#49`, branch `diag/tsk0308-post-copy-correction`; PR changes only a trigger file.
- Independent run/job: `33593810379 / 100133049388`, conclusion **SUCCESS**.

## 2. Current contract and predecessor verification

The independent verifier reparsed the canonical WBS and proved:

- TSK-0308 is L4 / HIGH / A3 / `AUTO_ALLOWED`;
- direct dependencies are exactly `TSK-0309; TSK-0300`;
- `ACC-0308 / VER-0308 / EVD-0308` binding is unchanged;
- current acceptance still requires content/error/loading/verification/uncertain/recovery states, shared tokens, accessibility, localization and implementation guidance.

Runtime parsing independently proved durable PASS for both direct predecessors and additionally bound TSK-0300 to its corrected evidence/run/current runtime section rather than preserving the superseded visible-copy assumption. Markers:

- `TSK0308_COPY_WBS=PASS`
- `TSK0308_COPY_CURRENT_PREDECESSORS=PASS`
- `TSK0308_COPY_TSK0300_CORRECTED_BINDING=PASS`
- `TSK0308_COPY_TSK0309=PASS`
- `TSK0308_COPY_TSK0320=PASS`

**Result: PASS.**

## 3. Historical/provenance preservation

The correction retained untouched:

- historical candidate `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4`;
- historical CSS `de5571379ff240f36b5aecd50f555a07176dbd32`;
- historical reference `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862`;
- design map `cd83279cdf5381cd7dae3feb177439158c1f9197`;
- requirement/interface trace `5e34ce9c192c6af65ba493cb356adb964c3d30b6`;
- historical acceptance evidence `343961f30bc46a20762ad2b0108a4afe9593e5a3`;
- dual-mode additive CSS `67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8`;
- shared TSK-0300 tokens `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- shared TSK-0300 components `831e92a74b6dda04252d93242cb33bd491a02381`;
- SafeWeb primary wordmark `f93958e3e4a16f9056693072c1b9b8b31fcda852`.

The prior current evidence blob `f280154e45fccbcaab51a2fdca2dd3c33edbb99a` and prior final rendered run/job `33585488537 / 100108650200` remain compatible provenance for unchanged responsive/component/account/lifecycle mechanics. Markers:

- `TSK0308_COPY_HISTORICAL_PROVENANCE=PASS`
- `TSK0308_COPY_PRIOR_CURRENT_MECHANICS=PASS`
- `TSK0308_COPY_NO_TOKEN_BRAND_FORK=PASS`
- `TSK0308_COPY_PRESERVATION_FENCE=PASS`

**Result: PASS.**

## 4. Corrected current state semantics

The active addendum now explicitly states that signed-in/session/device-ownership state never creates technical `protected/verified` or its primary user-facing copy `Protection verified`, and that visible protection copy follows current TSK-0320/TSK-0300 semantics.

The active rendered reference now uses:

- `configured/parent-confirmed` → `Setup confirmed` and `Protection has not yet been technically verified.`;
- `protected/verified` → `Protection verified`;
- `uncertain/error` → `Protection status could not be verified`;
- current `Not covered` for the second device;
- device uncertainty copy `Protection verification: Protection status could not be verified`.

The active reference no longer renders `You confirmed this is set up`, `Verified` as the primary state label, or `Status uncertain`. Static markers:

- `TSK0308_COPY_ADDENDUM=PASS`
- `TSK0308_COPY_ACTIVE_STATE_REFERENCE=PASS`
- `TSK0308_COPY_REFERENCE_STRUCTURE=PASS`
- `TSK0308_COPY_ACC_STRUCTURAL=PASS`
- `TSK0308_POST_COPY_CORRECTION_STATIC=PASS`

**Result: PASS.**

## 5. Fresh rendered verification

Read-only GitHub-hosted run/job `33593810379 / 100133049388` completed **SUCCESS** on Ubuntu 24.04 with Playwright `1.62.0` and Chrome for Testing / Chromium `151.0.7922.34` (revision `1234`).

Rendered checks passed at all target widths:

- `TSK0308_COPY_VIEWPORT_320=PASS`
- `TSK0308_COPY_VIEWPORT_768=PASS`
- `TSK0308_COPY_VIEWPORT_1024=PASS`
- `TSK0308_COPY_VIEWPORT_1440=PASS`

Cross-viewport acceptance markers:

- `TSK0308_COPY_BROWSER_NO_OVERFLOW=PASS`
- `TSK0308_COPY_BROWSER_ACCOUNTLESS_PRIMARY=PASS`
- `TSK0308_COPY_BROWSER_OPTIONAL_ACCOUNT_SECONDARY=PASS`
- `TSK0308_COPY_BROWSER_CURRENT_STATE_COPY=PASS`
- `TSK0308_COPY_BROWSER_PROVIDER_FALLBACK=PASS`
- `TSK0308_COPY_BROWSER_IDENTITY_PROTECTION_SEPARATION=PASS`
- `TSK0308_COPY_BROWSER_LIFECYCLE_SEPARATION=PASS`
- `TSK0308_COPY_BROWSER_RTL=PASS`
- `TSK0308_COPY_BROWSER_FOCUS=PASS`
- `TSK0308_COPY_BROWSER_CONSOLE=PASS`
- `TSK0308_COPY_RENDERED_ACCEPTANCE=PASS`
- `TSK0308_COPY_SOURCE_UNCHANGED=PASS`

The browser verifier proved no horizontal overflow, primary accountless/secondary optional-account action hierarchy, account-provider fallback, current evidence-state copy/IDs, identity/protection separation, lifecycle separation, RTL layout, visible focus, no console/page errors, no unexpected external requests, and no tracked source mutation during verification.

**Result: PASS.**

## 6. Disposition

**ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED** for the corrected current L4 shared responsive design-system acceptance boundary, pending guarded runtime synchronization and exact read-back.

No authentication/session/datastore implementation, legal/privacy completion, real-user processing, participant/publication/payment/market/production/launch action, lifecycle-gate PASS or successor PASS is inferred.
