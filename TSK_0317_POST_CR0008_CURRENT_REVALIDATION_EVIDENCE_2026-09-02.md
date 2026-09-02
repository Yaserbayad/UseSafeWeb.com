# TSK-0317 — Current Platform-Path Revalidation Acceptance Evidence

**Task:** TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform  
**Acceptance / Verification / Evidence:** ACC-0317 / VER-0317 / EVD-0317  
**Lifecycle / Priority / Authority:** L4 / HIGH / A4 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject to guarded runtime reconciliation and independent read-back.

## 1. Current artifact

- `TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-cr0008`
- blob `37173d2f9cb970a7b5e6a83af90c8f868f9fbfa8`
- publication commit `2dcaa44f4b0f536729d5f3f6d2ac2c509c35bd3a`

The historical `TSK_0317_PLATFORM_INSTALL_VERIFICATION_REMOVAL_RECOVERY_DESIGN_CANDIDATE_2026-08-28.md`, blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`, remains substantive evidence for compatible Android/iPhone platform mechanics but is superseded for current acceptance where it used stale `A1 / HUMAN_ONLY`, required a human design disposition, and used generic parent-facing `UseSafeWeb` wording.

## 2. Current WBS and eligibility proof

A dedicated read-only current-contract audit, run/job `33576145790 / 100080423916`, parsed current WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and proved:

- lifecycle `L4`;
- priority `HIGH`;
- AI capability `A4`;
- Action Authority `AUTO_ALLOWED`;
- sole hard dependency `TSK-0316`;
- trigger/preconditions permit current execution when hard dependencies and ordinary authority/safety inputs are satisfied;
- `ACC-0317 / VER-0317 / EVD-0317`;
- current ACC-0317: automatic profile/config is used only where reliable; fallbacks use canonical endpoint/profile guidance; OS asymmetry and limitations are explicit;
- current verification contract requires functional, negative, configuration, security/privacy and rollback checks.

The audit also proved current TSK-0316 PASS. No owner decision or human-only act is required for this bounded current design/revalidation.

## 3. Current predecessor semantics

Current TSK-0316 evidence `TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_EVIDENCE_2026-09-02.md`, blob `aaaa68119c21d76bc29d04e54443c23ce808bebc`, remains binding and was independently checked for:

- complete accountless core as the lowest-friction safe path;
- optional account/session/dashboard/device management only after explicit parent choice or already-authenticated account-only use;
- managed-device persistence as minimum bounded continuity rather than a child profile or protection-verification signal;
- consequential and ambiguous effects reconciled before replay rather than blindly retried.

Verifier output: `TSK0317_CURRENT_FRICTION_PREDECESSOR_SEMANTICS=PASS`.

## 4. Current SafeWeb naming and technical endpoint authority

Corrected TSK-0299 evidence `TSK_0299_POST_CR0008_CORRECTED_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `9d48add06fee14aef76f82a876a61cc88ce59440`, proves current visible generic product/feature naming is `SafeWeb` / `SafeWeb DNS`; generic `UseSafeWeb` without `.com` is prohibited as brand copy. Literal domain/endpoint identifiers remain exact where technically required.

Current TSK-0408 evidence `TSK_0408_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `0bbf1d934ecd4a7693baf7de56362391e46dcf55`, preserves:

- canonical resolver hostname `dns.usesafeweb.com`;
- Android native DoT-by-hostname behavior;
- Apple DoH profile/Server-URL behavior;
- truthful verification/removal/fallback rules.

Current TSK-0409 matrix `TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md`, blob `3aa832777276115912e4f3990b30cb541c458f4f`, preserves current support/conflict rules for Android provider-hostname, Apple profile/Server URL, VPN/DNS-changing apps, iCloud Private Relay, app-specific custom resolvers, user removal, and the rule that configuration evidence is never technical protection evidence.

Verifier outputs:

- `TSK0317_CURRENT_SAFEWEB_NAMING_AUTHORITY=PASS`;
- `TSK0317_CURRENT_ENDPOINT_AND_CONFLICT_AUTHORITY=PASS`.

## 5. Current official platform-source recheck

Current platform behavior was source-checked on 2026-09-02 before accepting the design:

### Android

- Android Help — `Manage advanced network settings on your Android phone`: `https://support.google.com/android/answer/9654714` — current help continues to expose Private DNS with a provider-hostname path and states that Private DNS protects DNS questions/answers rather than all device traffic.
- Android Developers — Android 9 behavior changes: `https://developer.android.com/about/versions/pie/android-9.0-changes-28` — documents system Private DNS / DNS-over-TLS behavior.

Current project conclusion: no source establishes a browser mechanism that silently changes the Android system Private DNS provider-hostname setting, so the parent/OS-controlled setting boundary remains correct.

### Apple

- Apple Support — `Install a configuration profile on your iPhone, iPad, or Apple Vision Pro`: `https://support.apple.com/102400` — current April 2026 guidance requires Settings/user installation for manually downloaded profiles; uninstalled downloads are deleted after eight minutes and current Stolen Device Protection policy may affect installation outside a familiar location.
- Apple iPhone User Guide — `Install or remove configuration profiles on iPhone`: `https://support.apple.com/guide/iphone/install-or-remove-configuration-profiles-iph6c493b19/ios` — profile installation requires permission and manual profile removal is exposed in Settings.
- Apple Platform Deployment — `DNS Settings device management payload settings for Apple devices`: `https://support.apple.com/guide/deployment/dns-settings-payload-settings-dep86469ba99/web` — documents encrypted DNS transport configuration including HTTPS/TLS and the Server URL semantics for HTTPS.

Current project conclusion: SafeWeb must not instruct the parent to weaken Stolen Device Protection merely to obtain a positive SafeWeb state. A security-policy block remains a truthful Action-needed / Not-covered / Status-uncertain condition with later supported retry, not a bypass instruction.

Verifier output: `TSK0317_CURRENT_OFFICIAL_SOURCE_BINDINGS=PASS`.

## 6. Final independent VER-0317

Final read-only verifier:

- workflow `.github/workflows/verify-tsk0317-current-revalidation.yml`;
- final workflow blob `b36c1fca1c4ad6f31cf8eb4b55cb25a33c35b6e6`;
- permission `contents: read`;
- GitHub-hosted Ubuntu 24.04;
- successful run/job `33576615158 / 100081874297`;
- conclusion: **SUCCESS**.

Observed final outputs:

- `TSK0317_IMMUTABLE_INPUT_HASHES=PASS`;
- `TSK0317_CURRENT_WBS_CONTRACT=PASS`;
- `TSK0316_CURRENT_PREDECESSOR=PASS`;
- `TSK0317_PROTECTED_RUNTIME_INPUTS=PASS`;
- `HISTORICAL_TSK0317_PROCEDURAL_NAMING_STALENESS=PASS`;
- `TSK0317_CURRENT_FRICTION_PREDECESSOR_SEMANTICS=PASS`;
- `TSK0317_CURRENT_SAFEWEB_NAMING_AUTHORITY=PASS`;
- `TSK0317_CURRENT_ENDPOINT_AND_CONFLICT_AUTHORITY=PASS`;
- `TSK0317_CURRENT_INVARIANTS=PASS`;
- `TSK0317_ANDROID_FUNCTIONAL_NEGATIVE_ROLLBACK_DESIGN=PASS`;
- `TSK0317_APPLE_FUNCTIONAL_NEGATIVE_ROLLBACK_DESIGN=PASS`;
- `TSK0317_CURRENT_OFFICIAL_SOURCE_BINDINGS=PASS`;
- `TSK0317_DUAL_MODE_SEPARATION=PASS`;
- `TSK0317_SAFEWEB_PARENT_FACING_VOCABULARY=PASS`;
- `TSK0317_22_DETERMINISTIC_ASSERTIONS=PASS`;
- `TSK0317_REVALIDATION_SCOPE=PASS`;
- `TSK0317_CURRENT_ACC=PASS`.

## 7. Diagnostic-only failed verifier runs

Three earlier read-only VER-0317 runs are retained as diagnostic evidence only:

1. `33576324000 / 100080973119` failed after immutable/WBS/dependency/protected-state checks because its matcher expected `Ambiguous consequential effects are reconciled before replay`; current TSK-0316 evidence states the same rule as `consequential and ambiguous effects are reconciled before replay rather than blindly retried`.
2. `33576461447 / 100081409912` passed the corrected predecessor semantics and failed because it expected `Browser/app custom encrypted resolver`; current TSK-0409 uses the more exact matrix phrase `Android + app-specific DoH/DoT/custom resolver`.
3. `33576541527 / 100081654136` passed current endpoint/conflict authority and the complete Android design, then failed because its Apple matcher expected a sentence fragment `profile removal remain explicit user/OS actions`; the artifact expresses the requirement structurally under `Must remain user/OS controlled:` with `profile removal` as a bullet.

No failed run mutated governed state or weakened acceptance. The final verifier changed only brittle text predicates to bind the same source-supported semantics.

## 8. Current ACC-0317 proof

1. Automatic profile/config behavior is limited to reliable non-misleading actions — **PASS**.
2. Android uses canonical provider-hostname guidance with `dns.usesafeweb.com`; OS setting mutation remains parent/OS controlled — **PASS**.
3. iPhone uses the owning separately verified profile/DoH route; TSK-0317 does not fabricate/release a profile and installation/removal remains user/OS controlled — **PASS**.
4. Android/Apple mechanism asymmetry and current platform limitations are explicit — **PASS**.
5. Configuration/profile/account/dashboard/parent-confirmation presence never equals `Verified`; controlled evidence owns the claim — **PASS**.
6. VPN, Private Relay, app-specific resolver, managed/security-policy and network conflicts demote/bound the claim rather than being hidden — **PASS**.
7. Removal and recovery are explicit and do not silently preserve a SafeWeb protection claim after the owning mechanism is removed — **PASS**.
8. No silent plaintext downgrade under an active SafeWeb claim — **PASS**.
9. Complete install/verify/remove/recover path remains accountless; optional account continuity is orthogonal and does not create verification evidence or J0/J1 linkage — **PASS**.
10. Generic parent-facing naming uses `SafeWeb` / `SafeWeb DNS`; technical `usesafeweb.com` strings remain literal only as actual identifiers — **PASS**.
11. Retry/replay follows changed-condition/new-evidence and reconciliation rules — **PASS**.
12. No new install technology or downstream lifecycle/gate PASS is inferred — **PASS**.

**TSK-0317 current dependency-complete platform-path revalidation: PASS.**

## 9. Preservation boundary before runtime mutation

Successful VER-0317 recorded current runtime section SHA-256 values:

- corrected TSK-0299: `d570e24eebd814ffd3014a51d4f60f1b7031f07a7e049dd3fb899b4c4ca0fc7c`;
- TSK-0485: `7f968a36ca0831b65f8441bffec6f73f09d6e282338baf8033c152cab56cbf3f`;
- TSK-0318: `71983d6d3689d030cddda123780ee4c5deeddf8bea691938f64d16627ba83d80`;
- TSK-0319: `f736e0301fefbe394a7c061430261e23e9b62ae2004557bf38c6ebfab448baa3`;
- current TSK-0301: `80f664b1d347044b311eab361a837db8e31fbd67c50124e00f309e32dee48785`;
- current TSK-0316: `6a33a6a62d1ce61dfb3a69cc648ae990b55fdbec50771e929b3b0d50b2ae71b9`;
- current TSK-0300: `b86eb69c654c94b4f3b1939fedcc7c23cb0151c87cb443a726f9ed417bdb2255`.

Pre-mutation runtime blob: `feb4b34a1860befed1ef52e5ebebb9eda6fd568c`.

## 10. Non-inference

This is current L4 platform-path design acceptance only. It does not prove integrated implementation/build, release `.mobileconfig`, authentication/provider architecture, persistent schema/storage, legal/privacy completion, representative-parent behavior, participant/publication/payment/market activation, production behavior, LG-06, launch, or any successor PASS.
