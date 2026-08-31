# TSK-0328 — Deterministic Verification Evidence

**Task:** TSK-0328 — Define information architecture and navigation model  
**Acceptance:** ACC-0328  
**Verification:** VER-0328  
**Evidence:** EVD-0328 deterministic post-CR-0007 verification  
**Date:** 2026-08-31  
**Final deterministic result:** PASS

## 1. Exact verified inputs

- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Relationship graph: `Plans/Master/RELATIONSHIP_INDEX.yaml`, blob `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-reconciliation runtime: `CURRENT_STATE.md`, blob `cd65636a10e0d0f6c72f5062a269cba69279399d`.
- Current TSK-0315 service blueprint: `TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md`, blob `97cf09f294c757f80ad5c0fbe6110ed8d471159c`.
- Current TSK-0325 parent journey: `prototype/TSK-0325/SERVICE_BLUEPRINT.md`, blob `7763a6d16760d85df3ad23789f764d3e431849ef`.
- Current TSK-0312 account/session requirements: `TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md`, blob `8dd71bccbd24ac5f62d5c536e644e7d9209b5832`.
- Current TSK-0142 dashboard/device-management requirements: `TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_REQUIREMENTS_2026-08-31.md`, blob `77b432e9d06741d0d303de2c2a2524e804cdcf5e`.
- Normative IA: `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md`, version `2.0.0-post-cr0007`, blob `527436958a1cd75fc91057410f4347ad56a3f53a`.
- Structured acceptance projection: `prototype/TSK-0328/ACCEPTANCE_MATRIX.json`, blob `d3b345a982f98bc7bdb32bc105fda4ac5659e9ab`.
- Analytical evidence: `TSK_0328_POST_CR0007_INFORMATION_ARCHITECTURE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `4f2f62fc06dd4ab037f443480fd67191bc213713`.
- Independent verifier: `.github/scripts/verify_tsk0328_post_cr0007_structured_20260831.py`, blob `0e0aca9aed951a90e9decc3da4e77d5a034b2623`.
- Verification workflow: `.github/workflows/verify-tsk0328-post-cr0007-structured-20260831.yml`, blob `9647ee6b2822c4b753a6814bf0286f8b7a9a2542`.

## 2. Deterministic execution

- GitHub Actions run: `33408013645`.
- Job: `99540324630`.
- Runner: `adguardvm`.
- Head commit: `c1e41529da468b6772b5a3c41276864a067ad026`.
- Conclusion: **SUCCESS**.

Observed deterministic PASS markers:

- `TSK0328_WBS_CONTRACT=PASS`
- `TSK0328_GRAPH_CONTRACT=PASS`
- `TSK0328_DEPENDENCY_RUNTIME=PASS`
- `TSK0328_PROJECTION_CONTRACT=PASS`
- `TSK0328_ARTIFACT_STRUCTURE=PASS`
- `TSK0328_ANALYTICAL_AND_PASS_FENCES=PASS`
- `TSK0328_CURRENT_SCOPE_RECONCILIATION=PASS`
- `TSK0328_INDEPENDENT_VERIFICATION=PASS`

The workflow also completed `git diff --check` and the clean-working-tree assertion without failure.

## 3. What was proven

The exact persisted TSK-0328 v2 artifact and projection satisfy current ACC-0328 by proving all of the following:

- a complete normal accountless core route exists and finishes without login;
- Start setup remains available irrespective of sign-in state;
- optional Google-sign-in/account continuity is represented without becoming a core gate;
- provider/sign-in error and session-expiry/revocation states preserve accountless core availability;
- signed-in return, dashboard empty/list, device detail and bounded device-management routes are represented;
- unsupported, failed-verification, false-positive, resume/lost-state, removal/recovery and support paths remain available and truthful;
- every logical screen has a documented user goal and current requirement trace;
- account/device/dashboard presence cannot create technical `Verified` evidence;
- logout, revoke/unlink, dashboard-record deletion, account deletion, J0/J1 deletion and physical DNS removal remain distinct operations;
- no browsing/query/activity history, child account/profile, raw AdGuard administration, broad per-domain control or mandatory-login route was introduced;
- English/Turkish/Arabic+RTL capability is represented without inferring non-UK market activation.

## 4. Historical impact and technical-verification disposition

The historical TSK-0328 v1.0.0 accountless-only artifact remains useful only for still-compatible public/setup structure. Its explicit exclusion of Login/Account/Dashboard cannot satisfy current CR-0006 scope and current ACC-0328.

The rebuilt v2 artifact was independently verified against structured semantic obligations rather than incidental wording. The final verifier passed on its first execution; no verifier correction or product-design change was needed after deterministic execution began.

## 5. Non-inference boundary

This evidence proves **TSK-0328 only**. It does not infer or approve:

- TSK-0329 interaction/prototype PASS;
- Google/Firebase vendor/privacy/security/provider architecture;
- persistent account/device schema, storage, retention, backup or authorization implementation;
- implementation/build/deployment/production behavior;
- real-user behavioral validation;
- LG-06 or any later gate PASS.

`RSK-0002` remains OPEN/non-blocking before L8.

## 6. Disposition

`ACC-0328 / VER-0328 / EVD-0328`: **PASS**, subject only to successful guarded runtime reconciliation and read-back of `CURRENT_STATE.md`.

No successor or gate becomes PASS automatically from this evidence.
