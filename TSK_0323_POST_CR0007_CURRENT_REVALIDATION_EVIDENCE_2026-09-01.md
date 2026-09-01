# TSK-0323 — Post-CR-0007 Current Revalidation Evidence

**Task:** `TSK-0323 — Create versioned device and service instruction catalogue`  
**Acceptance / Verification / Evidence:** `ACC-0323 / VER-0323 / EVD-0323`  
**Date:** 2026-09-01  
**Action authority:** A3 / `AUTO_ALLOWED`  
**Disposition:** PASS, subject to guarded runtime reconciliation/read-back

## Current contract

Current WBS authority remains L4 / MEDIUM with sole dependency `TSK-0322`. ACC-0323 requires every instruction to carry platform/version applicability, source reference, last verified date, owner, expected result, fallback and test case, with unsupported states explicit.

The sole current dependency is now current-qualified under `TSK_0322_POST_CR0007_DUAL_MODE_LANGUAGE_ACCEPTANCE_EVIDENCE_2026-09-01.md`.

## Accepted current artifacts

- `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` — version `1.0.1-post-cr0007`, blob `f848372f7820ed9455fe80668e761bec741423ae`.
- `content/TSK-0323/CATALOGUE.json` — schema `usesafeweb.device-service-instructions.v1`, version `1.0.1-post-cr0007`, blob `79753cc4916d38ed8d2f0ed6d01890e62df3fb04`.
- update commit: `ef590194f4942142f82c48230f7dfb711388a0ae`.

The current update is compatibility-only. The 12 device/service instruction records preserve their prior applicability, source-reference sets, owners, expected results, fallbacks, unsupported-state semantics, test IDs and review triggers. Only each record's current verification date was advanced to 2026-09-01 after revalidation.

## Current dual-mode compatibility

The catalogue now explicitly matches DEC-0053 / CR-0006 and DEC-0054 / CR-0007:

- core setup, verification, help, recovery and removal remain usable without SafeWeb login;
- optional parent account/session and lightweight saved-device/dashboard continuity may exist on separately approved product surfaces;
- account/session/saved-device/dashboard presence never produces technical S1 `Verified`;
- logout/account or record deletion is not physical SafeWeb DNS removal;
- browsing/query/activity history, child identity/profile data, broad/raw DNS administration and automatic J0/J1 account linkage remain prohibited;
- platform-owned account prerequisites, where actually required by Apple/Google flows, remain external platform authority and are not SafeWeb account requirements.

The current TSK-0322 guide/policy are pinned by the machine catalogue; the obsolete TSK-0322 blob is no longer authoritative.

## Current first-party source review

Official source review was repeated on 2026-09-01 for the catalogue's current platform families. No reviewed first-party fact required changing any of the 12 instruction semantics. Current source set remains:

- Google Android Private DNS: `https://support.google.com/android/answer/9654714?hl=en`;
- Google Chrome Secure DNS on Android: `https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DAndroid&hl=en`;
- Apple DNS Settings payload: `https://support.apple.com/en-gb/guide/deployment/dep86469ba99/1/web/1.0`;
- Apple profile install/remove guidance: `https://support.apple.com/en-euro/guide/iphone/iph6c493b19/ios` and `https://support.apple.com/guide/personal-safety/review-and-delete-configuration-profiles-ips327569a75/1.0/web/1.0`;
- Apple Screen Time / parental controls: `https://support.apple.com/en-gb/105121`;
- Google Android parental controls: `https://support.google.com/android/answer/16766047?hl=en`;
- Google Family Link supported devices: `https://support.google.com/families/answer/9116646?hl=en`.

Project-owned support matrices and SafeWeb-specific endpoint/state evidence remain authoritative for SafeWeb support claims.

## Deterministic verification

Verifier: `.github/scripts/verify_tsk0323_post_cr0007_compatibility_20260901.py`, corrected blob `5a66a6b05f7358b27c2ffffd8ec365522f9a2450`.  
Workflow: `.github/workflows/verify-tsk0323-post-cr0007-compatibility-20260901.yml`, blob `5894969435f4f103db4767940602c572ffb0f9a2`.  
Successful run/job: `33483472503 / 99778062685` on GitHub-hosted Ubuntu 24.04.

Observed markers:

- `TSK0323_CURRENT_BLOBS=PASS`
- `TSK0323_WBS_CONTRACT=PASS`
- `TSK0323_CURRENT_DEPENDENCY=PASS`
- `TSK0323_RECORD_SEMANTICS=12/12_PASS`
- `TSK0323_DUAL_MODE_SCOPE_FENCE=PASS`
- `TSK0323_PROCEDURE_BODY_UNCHANGED=PASS`
- `TSK0323_LANGUAGE_POLICY_ALIGNMENT=PASS`
- `TSK0323_POST_CR0007_VERIFICATION=PASS`

The first verification attempt `33483389924 / 99777807102` stopped only on a case-sensitive verifier literal (`account` vs `Account`) after all preceding substantive checks passed. No product/runtime mutation resulted from that failure. The verifier was corrected without changing the catalogue; the materially different run above then passed all checks.

## Non-inference fence

This PASS proves the current internal L4 instruction catalogue contract. It does not authorize public publication, production deployment, payment/market activation, real-user processing, human comprehension claims or launch.

**TSK-0323: PASS.**
