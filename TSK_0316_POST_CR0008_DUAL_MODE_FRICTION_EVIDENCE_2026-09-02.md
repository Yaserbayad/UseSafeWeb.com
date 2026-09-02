# TSK-0316 — Post-CR-0008 Dual-Mode Friction Acceptance Evidence

**Task:** TSK-0316 — Define a friction budget and challenge every click, field, choice, confirmation, account, and manual step  
**Acceptance / Verification / Evidence:** ACC-0316 / VER-0316 / EVD-0316  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject to guarded runtime reconciliation and independent read-back.

## 1. Current artifact

- `TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_BUDGET_2026-09-02.md`
- version `2.0.0-post-cr0008`
- blob `27f1b6de7924ceba713f9aed9ffc90df9a31efe5`
- publication commit `8af4b735cd0e9013c21cf8faa1b63d6f1a99015c`

The historical `TSK_0316_FRICTION_BUDGET_AND_INTERACTION_CHALLENGE_2026-08-28.md`, blob `07df8b1909809a069e3ddba1ff10b688d2f5a5e0`, remains traceable for compatible design-minimisation concepts but is superseded for current acceptance because it did not budget the CR-0006 optional parent-account/session/dashboard/device-management lifecycle.

## 2. Current WBS and predecessor proof

Independent VER-0316 parsed current WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and proved:

- L4 / HIGH / A3 / `AUTO_ALLOWED`;
- hard dependency exactly `TSK-0315`;
- `ACC-0316 / VER-0316 / EVD-0316`;
- ACC-0316 still requires every retained interaction to have a decision/technical/safety reason, removable steps to be removed, platform constraints to be explicit, and unsupported one-click claims to be absent.

Current dependency TSK-0315 is durable PASS under its dual-mode post-CR-0007 blueprint. Current blueprint input:

- `TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md`;
- blob `97cf09f294c757f80ad5c0fbe6110ed8d471159c`.

Verifier outputs:

- `TSK0316_CURRENT_WBS_CONTRACT=PASS`;
- `TSK0315_CURRENT_PREDECESSOR=PASS`;
- `CURRENT_DUAL_MODE_BLUEPRINT_INPUT=PASS`;
- `HISTORICAL_TSK0316_CR0006_STALENESS=PASS`.

## 3. Independent VER-0316

Successful read-only verifier:

- workflow `.github/workflows/verify-tsk0316-post-cr0008.yml`;
- workflow blob `c4948995ad5fde72c827d588132ec5aa7ff1dd09`;
- permissions: `contents: read`;
- GitHub-hosted Ubuntu 24.04;
- run/job `33574008442 / 100073872441`;
- conclusion: **SUCCESS**.

Observed verification outputs:

- `TSK0316_DUAL_MODE_INVARIANTS_AND_BUDGET_CLASSES=PASS`;
- `TSK0316_ZERO_BUDGET_REMOVALS=PASS`;
- `TSK0316_ALL_25_BLUEPRINT_STAGES_CHALLENGED=PASS`;
- `TSK0316_ACCOUNTLESS_AND_OPTIONAL_ACCOUNT_FRICTION=PASS`;
- `TSK0316_FIELD_CONFIRMATION_PRIVACY_BUDGET=PASS`;
- `TSK0316_PLATFORM_AND_ONE_CLICK_TRUTH=PASS`;
- `TSK0316_RETRY_AND_AMBIGUOUS_EFFECT_POLICY=PASS`;
- `TSK0316_26_DETERMINISTIC_ASSERTIONS=PASS`;
- `TSK0316_SAFEWEB_NAMING=PASS`;
- `TSK0316_NON_INFERENCE=PASS`;
- `TSK0316_CURRENT_ACC=PASS`.

## 4. Accepted friction model

The accepted current contract proves that:

1. the complete accountless core remains the lowest-friction safe path and can finish/exit without login;
2. optional parent account/sign-in/session/dashboard/device management occurs only after explicit parent choice or already-authenticated account-only use;
3. successful sign-in does not implicitly link/import/promote/extend J0/J1 and does not automatically create a managed-device record;
4. valid sessions suppress redundant sign-in;
5. dashboard list/empty is output, not mandatory form friction;
6. managed-device persistence is minimum bounded continuity and is not a child profile or protection-verification signal;
7. logout, unlink/revoke, device-record deletion, account deletion, anonymous reset and physical SafeWeb DNS removal are distinct operations;
8. consequential and ambiguous effects are reconciled before replay rather than blindly retried;
9. identity/contact/analytics/marketing/browsing-history/raw-DNS-admin fields have zero default budget unless an owning current requirement proves necessity;
10. platform/security actions and evidence interactions are preserved where they cannot truthfully be automated away;
11. generic parent-facing naming is `SafeWeb` / `SafeWeb DNS`, while exact `UseSafeWeb.com` or `dns.usesafeweb.com` appears only when it is the actual technical identifier;
12. one-click, complete-safety and silent-install claims remain prohibited when the underlying platform operation requires more.

## 5. Preservation boundary before runtime mutation

VER-0316 independently hashed the exact current runtime sections that must remain unchanged:

- corrected TSK-0299 section SHA-256 `d570e24eebd814ffd3014a51d4f60f1b7031f07a7e049dd3fb899b4c4ca0fc7c`;
- TSK-0485 section SHA-256 `7f968a36ca0831b65f8441bffec6f73f09d6e282338baf8033c152cab56cbf3f`;
- TSK-0318 section SHA-256 `71983d6d3689d030cddda123780ee4c5deeddf8bea691938f64d16627ba83d80`;
- TSK-0319 section SHA-256 `f736e0301fefbe394a7c061430261e23e9b62ae2004557bf38c6ebfab448baa3`;
- current TSK-0301 section SHA-256 `80f664b1d347044b311eab361a837db8e31fbd67c50124e00f309e32dee48785`.

Pre-mutation runtime blob: `077e6c61df6284441d447c4a796185adb5f3e65b`.

## 6. Current acceptance conclusion

ACC-0316 is proven under current dual-mode scope and current predecessor evidence.

**TSK-0316 post-CR-0008 dual-mode friction requalification: PASS.**

This is L4 friction-design acceptance only. It does not prove real-parent usability, provider/auth architecture, persistent schema/storage, implementation/build, legal/privacy completion, publication, payment, production behavior, LG-06, launch, or any successor PASS.
