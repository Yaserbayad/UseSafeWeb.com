# TSK-0322 — Post-CR-0007 Dual-Mode Language Acceptance Evidence

**Task:** `TSK-0322`  
**Acceptance / Verification / Evidence:** `ACC-0322 / VER-0322 / EVD-0322`  
**Date:** 2026-09-01  
**Authority:** `DEC-0053 / CR-0006`, `DEC-0054 / CR-0007`  
**Action authority:** A4 / `AUTO_ALLOWED`  
**Disposition:** PASS, subject to guarded runtime reconciliation/read-back

## Changed-scope correction

The historical TSK-0322 language guide was stale because QA assertion 10 said no claim could imply an account/dashboard/activity-history product existed. CR-0006 subsequently approved an optional parent account/session, minimum saved-device ownership persistence and lightweight dashboard/device management while preserving an accountless core. Activity history remains prohibited.

The current guide and machine policy were therefore updated without changing upstream brand or protection-state semantics:

- `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md`, version `2.0.0-post-cr0007`, blob `9344140b48ec99e0bd14639ac6640b581ee66d9f`;
- `content/TSK-0322/POLICY.json`, schema `usesafeweb.product-language-policy.v2`, version `2.0.0-post-cr0007`, blob `b4d8d144a8aac26114848542729bf2ac4aeee8d6`.

Current rules preserve visible brand `SafeWeb`, accountless core setup/verification/help/recovery/removal, and exact technical endpoint strings. They permit ordinary optional-account/dashboard copy inside the frozen DEC-0053 scope while prohibiting mandatory login for core value, browsing/query/activity history, child accounts/profiles, broad/raw DNS administration, automatic J0/J1-to-account linkage, and technical verification inferred from account/device/dashboard presence. Lifecycle copy keeps logout, account deletion, saved-record deletion, revoke/unlink, anonymous-state deletion and physical SafeWeb DNS removal distinct; unknown destructive results remain uncertain and never imply automatic replay or success.

## Deterministic verification

Verifier: `.github/scripts/verify_tsk0322_dual_mode_policy_20260901.py`, blob `641387eb4d8685ccd4d25438adb58d158886f59f`.  
Workflow: `.github/workflows/verify-tsk0322-dual-mode-policy-20260901.yml`, blob `32fbb526422b619279ef9ac49bb51fc32b14a706`.  
Run/job: `33479775242 / 99766584019`.  
Runner: self-hosted `adguardvm`.  
Conclusion: **SUCCESS**.

Observed markers:
- `TSK0322_CURRENT_BLOBS=PASS`
- `TSK0322_WBS_CONTRACT=PASS`
- `TSK0322_CURRENT_PREDECESSOR_CONTEXT=PASS`
- `TSK0322_GUIDE_SEMANTICS=PASS`
- `TSK0322_MACHINE_POLICY=PASS`
- `TSK0322_IDENTITY_ENDPOINT_FENCE=PASS`
- `TSK0322_DUAL_MODE_VERIFICATION=PASS`

An earlier run `33479719170 / 99766406951` failed only because the verifier expected the literal phrase `canonical state labels` instead of the WBS's actual state-language wording; current source blobs passed before that assertion. The corrected semantic check passed without changing product/content artifacts.

## Disposition

Current TSK-0322 satisfies its language/claims/terminology acceptance against current TSK-0327, corrected TSK-0333 and owner-approved SafeWeb identity. It makes no real-user comprehension, legal, publication, implementation, market or launch claim.

**ACC-0322 = PASS. VER-0322 = PASS. EVD-0322 = SATISFIED.**
