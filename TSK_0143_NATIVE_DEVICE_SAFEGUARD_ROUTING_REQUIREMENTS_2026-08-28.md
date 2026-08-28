# TSK-0143 — Native-Device Safeguard Routing Requirements

**Task:** TSK-0143 — Specify native-device safeguard routing requirements  
**Acceptance:** ACC-0143  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 ROUTING CONTRACT / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** DEC-0009 native-safeguards-first baseline + TSK-0141 minimum scope + TSK-0315 service blueprint + TSK-0316 friction budget + TSK-0320 truth-state contract + TSK-0409 supported-device matrix + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

The project has **not** behaviorally validated which native-control route parents understand best, how often controls are already configured, or whether native-first reduces rather than adds work. `UPA-003` and `RSK-0002` remain OPEN. This contract therefore freezes routing/truth/staleness requirements only; it does not claim that the route is easy, preferred, valuable or user-tested.

This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real participants, legal completion, payment, public release or launch.

## 1. What “native-device safeguard” means in the current product

Canonical UseSafeWeb authority freezes the user-visible shape as **native safeguards first → AdGuard baseline → one relevant service → truthful Protection Map**. The product is explicitly not a full parental-control or surveillance suite.

For TSK-0143, **native-device safeguard** means the current device-platform parental-control/safety mechanisms supplied by the phone ecosystem and relevant to the minimum first-phone setup. The currently source-supported mechanism families are:

- **Apple/iPhone:** Apple Screen Time / Family Sharing parental controls, including Content & Privacy Restrictions and related built-in age/content controls.
- **Android phone:** Google/Android parental controls. Depending on the actual supported Android version/device state, this can mean Google Family Link supervision and, on current Android 17+ where available, Android's on-device parental-controls PIN path.

This task does **not** freeze an exhaustive list of settings inside those systems. Exact instruction items, version applicability and screenshots belong to the source-backed instruction catalogue. The routing contract only determines which mechanism family/state to present and what truth the product may claim.

UseSafeWeb must not require location tracking, message reading, photo/contact inspection or equivalent surveillance merely to satisfy this native-safeguard step. Native ecosystems may offer broader features; UseSafeWeb's active minimum remains simple guardrails consistent with the non-surveillance product boundary.

## 2. Platform-routing decision tree

### 2.1 First route by supported phone family

1. **Supported iPhone path:** route only when the current TSK-0409 iPhone support condition is met.
2. **Supported Android-phone path:** route only when the current TSK-0409 Android-phone support condition is met.
3. **Unsupported/not-yet-supported device family:** do not improvise a native-control workflow. Show the appropriate TSK-0320 S4 `Not covered` or S5 `Status uncertain` state and a concise explanation.

Native-safeguard routing does not expand the DNS supported-device matrix. A device can be unsupported for UseSafeWeb DNS even if its vendor has parental controls, and vice versa.

### 2.2 Then route by current native-control state

For the chosen phone family, use exactly one of these routing states:

| Route state | Evidence/input | Product action | Protection Map state |
| --- | --- | --- | --- |
| `NATIVE_ALREADY_CONFIGURED_CONFIRMED` | Parent states the relevant approved native safeguard is already configured; no current contrary evidence. | Skip duplicate setup. Show only the minimum check/description needed to confirm the intended control category. | TSK-0320 S2 `Set up — parent confirmed` unless a later approved system verifier exists. |
| `NATIVE_NEEDS_SETUP` | Relevant approved native safeguard is absent/not completed, or parent says it is not configured. | Present the current source-backed platform instruction. | S3 `Action needed` until parent completes/confirms or an approved verifier succeeds. |
| `NATIVE_UNKNOWN` | Parent does not know and UseSafeWeb has no safe verifier. | Give a short “check this setting” route; do not force the full setup before the state is known. | S5 `Status uncertain` until resolved; may become S2/S3/S4. |
| `NATIVE_NOT_APPLICABLE` | Current approved rules say the particular safeguard does not apply to this branch. | Skip without replacement work. Explain why no step is required. | S4 `Not covered`/not-applicable semantics; never manufacture a positive state. |
| `NATIVE_UNSUPPORTED_OR_BLOCKED` | Device/version/account/management policy prevents the approved route or current instruction does not match observed UI/behavior. | Stop the native branch; show current-source help or unsupported state. | S4 if clearly unsupported, S5 if the state is ambiguous/conflicting. |
| `NATIVE_REMOVED_OR_DISABLED` | Parent reports an applicable safeguard was intentionally disabled/removed after setup. | Explain consequence and offer reconfiguration if appropriate. | S6 `Removed` in the current journey, or S3 when reconfiguration starts. |

No route state is inferred from the mere presence of an Apple/Google account, an installed Family Link app, a Screen Time menu, or an earlier session.

## 3. iPhone native-control route

### Current mechanism family

Apple's current UK guidance identifies Screen Time / Family Sharing as the built-in parental-control system for a child's iPhone. It includes Content & Privacy Restrictions and controls for web content, app/media ratings, purchases/downloads and other device settings. Current Apple guidance also says Family Sharing/child-account context is used for managing a child's controls and that some age-appropriate settings can be enabled by default depending on age/region.

### Routing requirements

1. **Already configured:** if the parent says the relevant approved Screen Time/content restrictions are already set, skip duplicate setup and record only S2 parent-confirmed state. Do not ask the parent to toggle settings off/on just to generate evidence.
2. **Needs setup:** show the current approved Apple instruction bundle only. Use Apple's current terminology and navigation; do not generalize from an old iOS screenshot/path.
3. **Family/child-account prerequisite absent:** do not collect the child's Apple Account credentials, birth date or family details inside UseSafeWeb. If the current Apple route requires Family Sharing/child-account setup, direct the parent to the current Apple flow and let Apple collect/manage its own account data. Until completed, keep S3/S5 as appropriate.
4. **Managed/supervised device or policy-restricted settings:** use S4/S5; do not advise bypassing school/employer/MDM controls.
5. **Family Link on iPhone is not an equivalent native-control substitute:** Google currently states most Family Link supervision tools do not work on iPhone/iPad. Do not route an iPhone parent to Android-style Family Link supervision as if it provided equivalent device control.
6. **No system-verification claim:** UseSafeWeb currently has no approved technical verifier for Apple Screen Time/content-control state. Positive state is parent-confirmed S2, not S1.

## 4. Android native-control route

### Current mechanism families

Google currently documents:

- Family Link supervision for Android devices and Google child/teen accounts;
- Android parental controls for screen time, apps/content and related controls;
- a newer on-device parental-controls PIN route on Android 17+ where supported, with the option to use/switch to Family Link for account-managed controls.

Family Link's supported supervision capability is materially different from iPhone/iPad, where Google states most supervision tools do not work.

### Routing requirements

1. **Prefer the already-correct native method:** if the parent already uses an approved Android parental-control route and the relevant minimum safeguard is set, skip reconfiguration and retain S2 parent-confirmed state.
2. **Android 17+ on-device controls:** they may be offered only when the device actually exposes the current on-device parental-controls path and the approved instruction catalogue marks it applicable. Do not infer Android 17+ merely from UI appearance.
3. **Family Link route:** it may be used for a supported Android phone when the current account/device prerequisites are satisfied and the approved instruction catalogue says it is the appropriate route. UseSafeWeb never collects the child's Google credentials.
4. **Older or variant Android UI:** if current authoritative instructions cannot map the observed device state confidently, do not improvise OEM-specific steps; route to S5/S4 and source-backed help.
5. **Managed device / policy restriction:** do not bypass organizational/guardian/device-owner controls; use S4/S5.
6. **No system-verification claim:** UseSafeWeb currently has no approved technical verifier for Family Link/on-device parental-control configuration. Positive state is parent-confirmed S2, not S1.
7. **Avoid surveillance scope:** Family Link features such as location or activity visibility are not mandatory UseSafeWeb native-safeguard requirements merely because the platform offers them.

## 5. Minimum interaction/routing inputs

TSK-0316 requires every retained interaction to have a current reason. Therefore the native route may use only inputs that change the branch:

1. supported device family — only when it cannot be safely derived/confirmed;
2. minimum OS/support band — only when current native-control applicability differs;
3. `already configured / needs setup / not sure` — one compact state question if UseSafeWeb cannot determine the state;
4. native-control mechanism choice **only if more than one approved route genuinely applies** to the exact Android configuration.

Do not ask for:

- parent or child name;
- exact DOB/age solely for UseSafeWeb routing when a coarse already-established first-phone context is enough;
- Apple/Google credentials;
- location, contacts, photos, messages or browsing history;
- a second confirmation after a prior answer already determines the same state;
- an arbitrary control choice when current platform rules determine the route.

If a platform itself requires identity/age/account data, that interaction occurs inside the platform's own flow and is not copied into UseSafeWeb state.

## 6. Already-configured handling

“Already configured” is a first-class success-shortening route, not an exception.

Requirements:

1. never make the parent redo a correctly configured safeguard merely for funnel consistency;
2. ask at most the minimum necessary confirmation of the approved control category;
3. do not inspect or collect screenshots/settings dumps by default;
4. do not call it `Verified` without an approved technical verifier;
5. retain a concise `Change/check this in Apple/Google settings` link so the parent can review it voluntarily;
6. if the parent reports a configuration but also reports contradictory behavior, route to S5 rather than preserving S2;
7. if later current-source guidance shows the old setting no longer provides the intended safeguard, reclassify to S3/S5 and explain the change.

## 7. Unsupported / unavailable / conflict paths

A native route is not safely executable when:

- the phone family/version is outside the approved support catalogue;
- the required native control is absent or materially different from current guidance;
- device management/ownership policy prevents the change;
- the required Apple/Google account/family prerequisite cannot be completed by the authorized parent;
- observed settings contradict the current instruction and no current source resolves the difference;
- the platform has materially changed and the instruction's last-verified baseline is stale.

The product must then:

1. stop the affected native setup branch;
2. use S4 when the path is clearly unsupported/not applicable;
3. use S5 when the state cannot be determined safely;
4. continue other independent safe layers only when their own support requirements are satisfied;
5. never create a fake alternative safeguard merely to make the Protection Map look complete.

## 8. Parent confirmation versus system verification

For the current native-control layer:

- parent completion/confirmation → S2 only;
- UseSafeWeb must not use the words `Verified`, `UseSafeWeb confirmed`, or equivalent system-evidence language;
- a future verifier can promote S2→S1 only after its own technical/security/privacy/accuracy acceptance is approved;
- a native-control setting is not inferred from UseSafeWeb DNS success;
- DNS verification is not evidence that Apple Screen Time/Family Link/on-device parental controls are configured.

This separation is mandatory even if combining the states would simplify UI.

## 9. Stale-guidance and source-version rules

Every native instruction used by the product must be versioned with:

- platform/mechanism;
- applicability/minimum version or state;
- official source URL;
- source title;
- last verified date;
- UseSafeWeb content version;
- expected user-visible result;
- fallback/unsupported result;
- owning task/content owner;
- review trigger.

Re-review is mandatory when:

- Apple/Google changes the documented menu path, default, prerequisite or supported device family;
- a major OS release changes the control model;
- Family Link or Screen Time capability/applicability materially changes;
- current user/target-device evidence contradicts the instruction;
- platform guidance becomes unavailable/redirected in a way that makes applicability uncertain;
- a security/privacy/safeguarding concern changes what UseSafeWeb should recommend.

Until re-verified, affected guidance is not silently reused. Use S5 or S4 and present a current-source fallback rather than stale instructions.

## 10. Platform-source facts checked 2026-08-28

### Apple

Current Apple UK guidance confirms:

- Screen Time/Family Sharing provides child parental controls;
- Content & Privacy Restrictions can manage web content, app/media restrictions, purchases/downloads and other settings;
- child controls and available defaults can vary by age/country/region;
- Screen Time passcode protects chosen settings;
- current settings/navigation can change and therefore must remain source/version owned.

Sources:
- https://support.apple.com/en-gb/guide/iphone/iph00ba7d632/ios
- https://support.apple.com/en-gb/105121
- https://support.apple.com/en-gb/126533

### Google / Android

Current Google guidance confirms:

- Android devices can use parental controls and Family Link;
- Family Link supervision works on supported Android devices but most supervision tools do not work on iPhone/iPad;
- Android 17+ currently exposes an on-device parental-controls PIN path where supported and can transition to Family Link;
- Family Link offers broader controls than UseSafeWeb needs; platform capability does not itself expand UseSafeWeb's non-surveillance scope.

Sources:
- https://support.google.com/android/answer/16766047
- https://support.google.com/families/answer/9116646?hl=en
- https://support.google.com/families/answer/9037996?hl=en
- https://support.google.com/families/answer/9055704?hl=en

## 11. Testable acceptance assertions

A later prototype/content/QA audit must prove:

1. iPhone routes to current Apple native parental controls, not Android Family Link supervision.
2. Android routes only to an approved current Android native-control mechanism for the exact device/account/version state.
3. Unsupported/not-yet-supported device states stop the affected native branch rather than receiving guessed instructions.
4. `Already configured` skips duplicate setup.
5. Parent-confirmed native state is S2 and never S1.
6. `Not sure` does not default to positive state; it routes through a minimal check or S5.
7. Managed/policy-restricted devices are not instructed to bypass their management authority.
8. UseSafeWeb does not collect Apple/Google credentials or duplicate platform account data.
9. UseSafeWeb does not require location/messages/photos/contacts/activity surveillance to satisfy the native step.
10. Exact native-control setting lists come only from the versioned instruction catalogue, not hard-coded unsourced assumptions.
11. Stale/unmatched guidance becomes S5/S4 until reverified.
12. Every instruction carries source, applicability and last-verified metadata.
13. A source/platform change triggers review before a continuing support claim.
14. Native-control completion is independent from DNS verification.
15. A platform prerequisite failure does not fabricate an alternative task merely to produce completion.
16. The route remains optional/skippable when the approved safeguard is already correctly present or genuinely not applicable.

## 12. ACC-0143 result

ACC-0143 requires supported platform states, already-configured handling, parent confirmation, unsupported paths, stale guidance and verification limitations.

This contract defines all six areas, binds them to the frozen native-first/minimum-scope/product-truth decisions, avoids inventing an exhaustive parental-control feature suite, and uses current Apple/Google platform evidence only to select source-backed mechanism families and constraints.

**TSK-0143 result: PASS candidate subject to independent verification and runtime read-back.**
