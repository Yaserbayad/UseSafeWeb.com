# TSK-0317 — Current Platform Install / Verification / Removal / Recovery Revalidation — Post-CR-0008

**Task:** TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform  
**Acceptance / Verification / Evidence:** ACC-0317 / VER-0317 / EVD-0317  
**Lifecycle / Priority / Authority:** L4 / HIGH / A4 / AUTO_ALLOWED  
**Version:** 2.0.0-post-cr0008  
**Date:** 2026-09-02 UTC  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE

## 1. Purpose and supersession

This artifact supersedes `TSK_0317_PLATFORM_INSTALL_VERIFICATION_REMOVAL_RECOVERY_DESIGN_CANDIDATE_2026-08-28.md` for current acceptance where that historical candidate:

- described TSK-0317 as `A1 / HUMAN_ONLY` and required a human design disposition, which is superseded by the current CR-0008-normalized WBS contract; and
- used generic parent-facing `UseSafeWeb` wording that is superseded by corrected TSK-0299, where the visible product/brand token is `SafeWeb` / `SafeWeb DNS` and `UseSafeWeb.com` is only a domain/project/technical identifier.

The historical technical platform design remains the substantive baseline where current verification confirms it. This revalidation does not invent a new install mechanism, does not silently automate OS security settings, and does not weaken verification/removal/recovery truth.

## 2. Current canonical contract and eligibility

Read-only current-contract audit run/job `33576145790 / 100080423916` parsed current WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and proved:

- lifecycle `L4`;
- priority `HIGH`;
- AI capability `A4`;
- Action Authority `AUTO_ALLOWED`;
- dependency exactly `TSK-0316`;
- trigger: applicable lifecycle/gate and all hard dependencies satisfied;
- preconditions: canonical state read, current gate/authority confirmed, required inputs/access available, no unresolved safety/privacy blocker;
- `ACC-0317 / VER-0317 / EVD-0317`;
- current ACC-0317: **automatic profile/config is used only where reliable; fallbacks use canonical endpoint/profile guidance; OS asymmetry and limitations are explicit**;
- current verification method requires functional, negative, configuration, security/privacy and rollback checks against acceptance.

The same audit proved current TSK-0316 PASS. Runtime input at eligibility audit: `feb4b34a1860befed1ef52e5ebebb9eda6fd568c`.

No owner action is required for this current bounded design/revalidation task.

## 3. Current predecessor constraints from TSK-0316

TSK-0316 current dual-mode friction acceptance remains binding:

1. the complete setup/verification/Protection Map/help/removal/recovery core must remain usable without login;
2. optional account continuity is non-coercive and does not create extra mandatory platform-setup friction;
3. a valid account/session/device record never substitutes for current technical protection evidence;
4. sign-in must not automatically join/import/promote/extend J0/J1;
5. retries require changed condition/new evidence and ambiguous consequential effects must be reconciled before replay;
6. generic parent-facing naming uses `SafeWeb` / `SafeWeb DNS`; literal technical identifiers remain exact where required;
7. platform/security actions that cannot truthfully be automated remain explicit.

TSK-0317 therefore owns the platform setup path, not account architecture. The same Android/iPhone install, verification, removal and recovery rules apply whether the parent remains accountless or later uses optional account continuity.

## 4. Current external platform-source recheck — 2026-09-02

Current platform facts were rechecked against official sources before revalidation.

### Android

Official Android Help currently documents the system `Private DNS` setting with `Off`, `Automatic`, and `Private DNS provider hostname`, and states that Private DNS protects only DNS questions/answers rather than the rest of device traffic:

- https://support.google.com/android/answer/9654714

Android 9 platform documentation continues to describe Private DNS / DNS-over-TLS behavior for the system resolver:

- https://developer.android.com/about/versions/pie/android-9.0-changes-28

These sources do not establish any browser-based mechanism that silently changes the Android system Private DNS provider hostname. The current manual OS-setting boundary remains valid.

### Apple

Apple's current April 2026 profile-installation guidance confirms that a configuration profile downloaded from a website or email still requires the user to open Settings and explicitly install it. Apple also says an uninstalled downloaded profile is automatically deleted after eight minutes. Current Apple guidance further notes that outside a familiar location, Stolen Device Protection may need to be disabled before profile installation and re-enabled afterward:

- https://support.apple.com/102400

SafeWeb does **not** instruct the parent to weaken Stolen Device Protection merely to obtain a positive SafeWeb state. If the current device/location policy blocks installation, the SafeWeb path remains `Action needed` / `Not covered` / `Status uncertain` as appropriate, with the parent free to retry later under a supported condition.

Apple's current iPhone guide confirms that manually obtained profiles require installation permission, are visible under `Settings > General > VPN & Device Management`, and deleting a profile removes the settings/data associated with that profile:

- https://support.apple.com/guide/iphone/install-or-remove-configuration-profiles-iph6c493b19/ios

Apple Platform Deployment continues to document the DNS Settings payload with encrypted transport `HTTPS` or `TLS`; `Server URL` is used for HTTPS and is required for the HTTPS protocol configuration:

- https://support.apple.com/guide/deployment/dns-settings-payload-settings-dep86469ba99/web

The current SafeWeb design therefore retains an explicitly authorized profile-installation boundary and does not claim silent profile installation/removal.

## 5. Shared invariants

1. **Route, do not ask protocol questions.** The parent never chooses DoH vs DoT as a product decision.
2. **Accountless core remains complete.** Login/account/device registration is never required to configure, verify, troubleshoot, remove or recover SafeWeb DNS.
3. **Optional account is orthogonal continuity.** Account/session/dashboard state never changes the OS setup mechanism and never proves current DNS protection.
4. **Automate only reliable product actions.** Safe routing, copy, delivery of an already verified artifact, controlled verification and state rendering may be automated; security-sensitive OS changes remain explicit.
5. **Verification owns the protection claim.** Configuration presence, profile presence, account ownership, dashboard presence and parent confirmation do not equal `Verified`.
6. **No browsing/query/activity history.** Verification uses approved controlled/synthetic evidence.
7. **Removal/recovery is first-class.** Every supported setup path has a bounded removal/recovery path.
8. **No silent downgrade.** Failure never falls back to plaintext while retaining a SafeWeb protection claim.
9. **No speculative coverage.** Unsupported/managed/conflicting combinations stop with truthful state rather than an improvised client/workaround.
10. **Retry is evidence-driven.** Equivalent failure is not looped; ambiguous consequential state is reconciled before replay.

## 6. Android phone path — current supported baseline

The authoritative internal support matrix remains the owner-frozen TSK-0409 bounded baseline: Android 9+ phones only where the native `Private DNS provider hostname` control is present/usable and the combination has not been excluded by the current support matrix. This task does not broaden that matrix.

### 6.1 Setup

1. Route to Android only when the supported platform band is established with the minimum necessary context.
2. Explain that SafeWeb DNS is an encrypted DNS filtering layer and does not provide complete device safety or replace native parental controls.
3. Guide the parent to the OS `Private DNS` setting and the provider-hostname mode using source-maintained wording rather than an invented universal OEM menu path.
4. Present the exact technical hostname `dns.usesafeweb.com`.
5. Offer `Copy DNS hostname` where useful.
6. Do not append a port or show the Apple DoH URL in the normal Android provider-hostname field.
7. The parent performs the OS-required paste/entry/save action. SafeWeb does not claim to have silently changed the Android system setting.
8. Return to SafeWeb for controlled verification.

### 6.2 Automatic/manual boundary

May be automatic when current evidence supports it:

- supported-platform routing;
- exact hostname display/copy;
- contextual instructions;
- controlled verification attempt;
- evidence-state rendering;
- bounded retry after a changed condition.

Must remain parent/OS controlled under the current baseline:

- opening/changing the Android system Private DNS control;
- selecting provider-hostname mode;
- entering/pasting `dns.usesafeweb.com`;
- saving/applying the OS setting.

### 6.3 Verification

Run the approved controlled verifier automatically where technically feasible; otherwise expose one deliberate `Check protection` / `Recheck` action.

`Verified` requires qualifying current system evidence for the intended resolver/filtering path. Parent confirmation, settings-screen presence, successful hostname resolution, account ownership or dashboard state is insufficient.

A VPN, browser/app custom resolver, network block or other unresolved resolver-path conflict yields the current evidence-matched `Action needed`, `Not covered` or `Status uncertain` state rather than optimistic success.

### 6.4 Removal/recovery

1. Offer `Remove SafeWeb DNS` from help/recovery rather than as normal happy-path friction.
2. Guide the parent to leave the custom SafeWeb provider-hostname mode and return to the appropriate normal platform DNS behavior, normally `Automatic` where that matches the accepted support guidance.
3. Run a neutral/synthetic connectivity check where feasible.
4. Mark the SafeWeb DNS layer `Removed`; do not retain a protection claim.
5. If the intended path fails, removal/reset is the recovery route. Do not silently use plaintext while presenting SafeWeb as active.

## 7. iPhone path — current supported baseline

The authoritative internal support matrix remains the bounded TSK-0409 iPhone baseline using the separately verified SafeWeb encrypted-DNS profile route. This task does not broaden support to iPad, Mac, supervised/managed combinations or other Apple families unless their owning support tasks do so.

### 7.1 Setup

1. Route to the accepted iPhone support band only when current support/applicability is known.
2. Explain that the SafeWeb DNS profile configures an encrypted DNS filtering layer and does not provide complete device safety.
3. Offer only the exact versioned SafeWeb profile artifact after that release artifact has passed its own artifact-level verification. TSK-0317 does not itself fabricate or publish a `.mobileconfig` file.
4. The accepted profile mechanism uses the canonical SafeWeb DoH endpoint `https://dns.usesafeweb.com/dns-query` under its owning technical contract.
5. Profile download/delivery may be automated only for an already verified correct artifact/environment.
6. Installation/authorization remains an explicit iOS/user action in Settings.
7. If Stolen Device Protection/current security policy blocks installation, do not instruct the user to weaken security merely to make SafeWeb green; show a truthful blocked/unsupported/uncertain state and allow later retry under a supported condition.
8. After OS installation, return to SafeWeb and run controlled verification. Profile presence alone is not `Verified`.

### 7.2 Automatic/manual boundary

May be automatic when reliable:

- platform routing;
- delivery of an already verified profile artifact;
- version/applicability check;
- contextual current-source instructions;
- controlled verification attempt;
- evidence-state rendering.

Must remain user/OS controlled:

- approving/installing the profile;
- security-sensitive authorization;
- profile removal.

### 7.3 Verification

Run controlled verification automatically where feasible; otherwise expose one deliberate check/recheck.

Profile presence, successful download, account/session state, dashboard presence or parent confirmation is insufficient for `Verified`.

If VPN, iCloud Private Relay, app/browser custom resolver or another tunnel/resolver path makes the effective route unproven, use the owning uncertainty/not-covered state rather than claiming universal compatibility or incompatibility without exact evidence.

### 7.4 Removal/recovery

1. Identify the exact SafeWeb DNS profile.
2. Guide the parent to remove it using the current iPhone profile-management route.
3. Treat profile removal as removal of the profile-owned SafeWeb DNS configuration; do not claim unrelated account/device data was deleted.
4. Run a neutral/synthetic connectivity check where feasible.
5. Mark SafeWeb DNS `Removed`; no protection claim remains until a supported path is configured and verified again.
6. If the profile route creates material connectivity trouble, explicit profile removal is the safe recovery path; do not invent a hidden alternate resolver while retaining the SafeWeb protection claim.

## 8. Current conflict/negative matrix

| Condition | Required design outcome |
| --- | --- |
| Unsupported OS/device family | `Not covered`; no speculative alternate client. |
| Managed/locked DNS/profile controls | `Not covered` or `Status uncertain` until an exact accepted policy path exists. |
| Captive portal / incomplete ordinary network access | Complete ordinary network access first; no SafeWeb claim until verified. |
| Android intended DoT path blocked | `Action needed` / `Status uncertain`; removal/recovery remains available. |
| Apple intended encrypted-DNS endpoint/profile path blocked | `Action needed` / `Status uncertain`; removal/recovery remains available. |
| VPN changes/owns DNS path | `Status uncertain` / not covered until exact coexistence is accepted. |
| iCloud Private Relay coexistence unproven | `Status uncertain`; no definite compatibility claim without current evidence. |
| Browser/app custom resolver | Affected traffic is outside a universal system-DNS claim unless directly proven. |
| Profile/security policy blocks installation | Do not bypass the security policy merely to obtain success; present truthful blocked/uncertain state. |
| Account/provider outage | Account-only continuity may be unavailable, but accountless setup/verification/help/removal remains available and physical DNS truth is unchanged. |

Adding confirmations or account state cannot convert an unsupported/conflicted platform path into a supported one.

## 9. Canonical fallback policy

`Fallback` means the accepted manual platform guidance or explicit removal/recovery route, not an unreviewed third-party DNS client.

- Android: current native provider-hostname guidance; safe reset to normal platform DNS behavior when the intended route cannot operate.
- iPhone: exact verified profile + manual install/authorization guidance; explicit profile removal when the intended route cannot operate.
- No universal hostname/URL form.
- No silent plaintext fallback under an active SafeWeb protection claim.
- Server-side resolver fallback remains outside this L4 UX task.

## 10. Parent-facing action vocabulary

Use current brand language:

- `Start setup`
- `Copy DNS hostname`
- `Get SafeWeb profile` only when the exact artifact is already verified for the environment
- `Check protection`
- `Try again` only after a changed condition/new evidence
- `Remove SafeWeb DNS`

Use exact technical identifiers literally when technically required: `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query`.

Do not use generic visible-brand copy such as `UseSafeWeb DNS`, `Get UseSafeWeb profile`, or `Turn on UseSafeWeb`. Do not use `Protect this phone in one click`, `Fully protected`, `Works on every Android/iPhone`, `One setting protects every app/network`, or `Install and forget`.

## 11. Accountless / optional-account separation

- Platform setup never requires login.
- Choosing optional account continuity does not change the supported OS mechanism.
- Sign-in does not automatically migrate J0/J1 into account/device state.
- A managed-device record is not a child identity and not current DNS verification.
- Logout/revoke/device-record deletion/account deletion do not remove physical SafeWeb DNS unless the owning removal path actually performs and verifies that operation.
- Removing SafeWeb DNS does not itself delete an account/device record or anonymous state.
- Provider outage blocks account-only functions only; accountless verification/removal remains available.

## 12. Deterministic ACC-0317 assertions

A current verifier must prove all of the following:

1. TSK-0317 is current L4 / HIGH / A4 / AUTO_ALLOWED with sole dependency TSK-0316.
2. Current TSK-0316 is PASS.
3. Automatic profile/config behavior is limited to actions that can be performed reliably without misrepresenting an OS security boundary.
4. Android parent flow uses `dns.usesafeweb.com` as the provider hostname and does not show the Apple DoH URL as the normal Android field.
5. iPhone profile flow uses the owning verified profile artifact and canonical DoH endpoint; TSK-0317 itself does not fabricate/release the profile.
6. Android system setting changes remain parent/OS controlled.
7. Apple profile installation and removal remain explicit user/OS actions.
8. Current official Android guidance still exposes a Private DNS provider-hostname path and warns Private DNS protects DNS only.
9. Current official Apple guidance still requires permission/settings interaction for manually downloaded profiles and supports manual profile removal.
10. Current Apple DNS Settings documentation still supports encrypted HTTPS/TLS configuration semantics.
11. Configuration/profile presence, account ownership, dashboard state and parent confirmation do not equal `Verified`.
12. Controlled/synthetic verification requires no browsing/query/activity history.
13. VPN/Private Relay/custom-resolver/managed/network conflicts bound or demote the claim instead of being hidden.
14. Unsupported combinations stop rather than receiving speculative clients/workarounds.
15. Android removal/recovery ends the SafeWeb DNS claim and returns to normal supported platform DNS behavior.
16. iPhone profile removal ends the SafeWeb DNS claim without pretending account/device/anonymous data was also deleted.
17. No silent plaintext fallback retains a SafeWeb protection claim.
18. Generic parent-facing naming uses `SafeWeb` / `SafeWeb DNS`; exact UseSafeWeb-domain strings appear only as literal technical identifiers.
19. The complete install/verify/remove/recover path remains usable without login.
20. Optional account continuity does not alter OS mechanism, create verification evidence or automatically link J0/J1.
21. Retry occurs only after changed condition/new evidence; ambiguous consequential state is reconciled before replay.
22. No integrated build, release profile, legal/privacy, participant, publication, payment, market, production or launch PASS is inferred.

## 13. Current candidate conclusion

The historical platform mechanics remain substantively valid. Current revalidation requires **no new install technology**. It replaces only stale HUMAN_ONLY procedure and stale generic `UseSafeWeb` parent-facing wording, adds explicit dual-mode account-separation/retry constraints from current TSK-0316, and refreshes current Android/Apple source truth.

**Candidate disposition: ACC-0317 current PASS pending independent VER-0317, EVD-0317 publication, guarded runtime reconciliation and independent read-back.**
