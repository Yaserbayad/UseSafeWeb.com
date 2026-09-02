# TSK-0308 — Protection-State Copy Correction Revalidation After Current TSK-0300

**Task:** TSK-0308 — Create the shared responsive design system for public and product surfaces  
**Acceptance / Verification / Evidence:** ACC-0308 / VER-0308 / EVD-0308  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent verification, durable evidence publication, guarded runtime reconciliation and exact read-back.

## 1. Revalidation trigger

TSK-0308 reached current PASS earlier on 2026-09-02 using its dual-mode addendum/reference package. A later artifact-specific audit found and corrected a genuine protection-state-copy contradiction in direct predecessor TSK-0300. Current TSK-0300 now binds the current TSK-0320 primary protection-state copy.

Because TSK-0308 directly depends on TSK-0300 and ACC-0308 explicitly requires verification and uncertain states, its accepted current reference was inspected rather than blindly preserved. The inspection found material stale visible copy in `prototype/TSK-0308/dual-mode-reference.html`:

- `You confirmed this is set up`;
- `Verified`;
- `Status uncertain`.

The active `DUAL_MODE_ADDENDUM.md` also used the obsolete shorthand `S1 Verified` without binding the current technical state identifier and primary copy. Historical immutable provenance files are left unchanged; the active addendum/reference are corrected narrowly.

## 2. Current authority and dependency binding

Current canonical inputs:

- WBS `Plans/Master/WBS/master-wbs.csv` — blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship index `Plans/Master/RELATIONSHIP_INDEX.yaml` — blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `CURRENT_STATE.md` — blob `960f8449943552a6c7a8b747b0d9b072f8eaa507`.

Current TSK-0308 remains L4 / HIGH / A3 / AUTO_ALLOWED with hard dependencies exactly `TSK-0309; TSK-0300` and ACC/VER/EVD `ACC-0308 / VER-0308 / EVD-0308`.

Current direct-predecessor binding:

- TSK-0309 dual-mode baseline `prototype/TSK-0309/BASELINE.md` — blob `6302bb2509d04c8269e4df112140d7c416e42eff`;
- corrected TSK-0300 evidence `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md` — blob `a3e39896b67098ced321cb9e4b82c65c440806e4`;
- corrected TSK-0300 runtime commit `93fea25db8c1b6fd70a8fd45e0ff531cf33ea2e1`;
- current TSK-0320 semantic owner `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md` — blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.

## 3. Exact two-file correction

### 3.1 Active dual-mode addendum

Pre-correction addendum blob: `195ace26e6e8586e8e19da85a21d430a4a89a55a`.

Corrected `prototype/TSK-0308/DUAL_MODE_ADDENDUM.md`:

- blob `86461ef4baac27cf4cfd906f7ed464781186e78d`;
- correction commit `f4c479d90299db6fb87ea9b62ea9fcc8f92c6039`;
- version `2.0.1-post-CR0008-copy-refresh`.

The active normative rule now states that identity/session/device ownership never creates technical state `protected/verified` or its primary copy `Protection verified`; visible protection copy follows current TSK-0320/TSK-0300 semantics. DS-01–DS-17 structure, dual-mode scope, privacy, lifecycle separation, responsive/localization/accessibility rules and TSK-0300 token/primitive ownership remain unchanged.

### 3.2 Active rendered dual-mode reference

Pre-correction reference blob: `293945d9e2df823079e8dd73134168773a65a652`.

Corrected `prototype/TSK-0308/dual-mode-reference.html`:

- blob `7e522e23e43d04da3facf53747ad9b245e66ef62`;
- correction commit `6df3d4fa1c839841e651fa3f7c2abd9aabafe089`.

Current rendered evidence-state examples now use:

- `configured/parent-confirmed` → `Setup confirmed` plus `Protection has not yet been technically verified.`;
- `protected/verified` → `Protection verified`;
- `uncertain/error` → `Protection status could not be verified`;
- device-row uncertainty → `Protection verification: Protection status could not be verified`;
- existing `Not covered` remains current.

No account/session/device ownership statement is upgraded into technical verification.

## 4. Explicit preservation boundary

The correction does **not** alter or reopen:

- historical owner-approved candidate `prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md` — `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4`;
- historical `candidate.css` — `de5571379ff240f36b5aecd50f555a07176dbd32`;
- historical reference surface — `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862`;
- design-system map — `cd83279cdf5381cd7dae3feb177439158c1f9197`;
- requirement/interface trace — `5e34ce9c192c6af65ba493cb356adb964c3d30b6`;
- `dual-mode-addendum.css` — `67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8`;
- current shared TSK-0300 tokens — `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- current shared TSK-0300 components — `831e92a74b6dda04252d93242cb33bd491a02381`;
- owner-approved SafeWeb primary wordmark — `f93958e3e4a16f9056693072c1b9b8b31fcda852`;
- DS-01–DS-17 component architecture;
- responsive breakpoints, RTL/LTR behavior, focus/reduced-motion requirements and accessibility model;
- complete accountless core plus optional non-coercive account/session/dashboard/device management;
- lifecycle separation and no-surveillance/no-overall-safety-score boundaries.

The older current revalidation artifact/evidence remain durable provenance for unchanged facts:

- `TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md` — blob `90dce398ae86238abf5cf141acac47d78bf085b8`;
- `TSK_0308_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md` — blob `f280154e45fccbcaab51a2fdca2dd3c33edbb99a`;
- prior final rendered VER run/job `33585488537 / 100108650200`.

They are superseded only for the corrected active protection-state-copy binding and resulting active source hashes.

## 5. Current ACC-0308 verification contract

Independent current VER-0308 must prove:

1. current WBS/graph/runtime identity and exact direct dependencies;
2. corrected current TSK-0300 predecessor evidence/runtime and current TSK-0320 semantic owner;
3. TSK-0309 still requires complete accountless core plus optional account continuity;
4. historical TSK-0308 candidate/CSS/reference/map/trace remain unchanged as compatible provenance;
5. corrected addendum/reference are exactly the new blobs above;
6. current visible state examples use the current primary copy and canonical identifiers, with stale historical primary labels absent from the active reference;
7. DS-14–DS-17 and dual-mode accountless/account/session/device/lifecycle separation remain present;
8. additive CSS still defines no local palette/font fork and continues to consume shared TSK-0300 tokens;
9. reference still imports shared tokens/components, historical candidate CSS, additive CSS and approved SafeWeb identity;
10. browser rendering at 320/768/1024/1440 has no horizontal overflow, preserves accountless primary/optional-account secondary order, provider fallback, identity/protection separation, lifecycle separation, RTL and visible focus, and has no console/page errors;
11. verifier leaves repository source unchanged;
12. no implementation/auth/datastore/legal/privacy/user-validation/publication/payment/market/production/launch/gate/successor PASS is inferred.

## 6. Candidate disposition

The discovered contradiction is narrow but acceptance-relevant. The active TSK-0308 package is corrected without redesigning or replacing the approved responsive design system.

**ACC-0308 current correction candidate: PASS pending independent VER-0308, durable EVD-0308, guarded runtime reconciliation and exact read-back.**
