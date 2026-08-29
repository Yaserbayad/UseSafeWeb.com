# TSK-0323 — Versioned Device and Service Instruction Catalogue

**Version:** 1.0.0  
**Status:** internal L4 implementation-facing content contract  
**Owner:** Content  
**Action authority:** A3 / AUTO_ALLOWED  
**Current sequencing:** DEC-0052 / CR-0005  
**Last source review:** 2026-08-29  
**Publication authority:** none

## 1. Purpose and authority

This is the current implementation-facing instruction registry for the bounded SafeWeb first-phone experience. It turns the accepted source-backed TSK-0307 catalogue, TSK-0317 platform design, TSK-0409 support matrix, TSK-0143 native-safeguard routing, TSK-0144 one-service routing, TSK-0320 protection-state semantics, and TSK-0322 product-language policy into versioned instruction records that engineering and QA can consume without guessing.

TSK-0307 remains predecessor/source evidence; this TSK-0323 catalogue is the current mutable implementation-facing catalogue. A downstream surface must reference an instruction ID/version instead of copying technical semantics into a second authority.

Visible product identity is **SafeWeb**. `UseSafeWeb.com` remains the domain/project/technical identifier. Technical endpoint strings remain exact: Android `dns.usesafeweb.com`; iPhone DoH `https://dns.usesafeweb.com/dns-query`.

DEC-0052 / CR-0005 applies: no pre-product parent/user/participant evidence is claimed or required. Technical/source/device/browser/accessibility verification remains mandatory through L7; real-user validation begins only at the controlled L8 integrated-product pilot.

## 2. Catalogue-wide rules

1. **Applicability is exact.** Platform/device/version/network/account/management conditions are part of the instruction, not optional notes.
2. **Unsupported means stop.** Never improvise another DNS client, VPN, account workaround, service, or platform path to make a journey look complete.
3. **Verification truth is preserved.** Configuration presence or parent confirmation never becomes S1 `Verified`; use S2/S3/S4/S5/S6 exactly as owned by TSK-0320/0322.
4. **Accountless by default.** SafeWeb never collects Apple/Google/provider credentials, child browsing/DNS history, or a persistent child/device profile for these instructions.
5. **OS/security authority remains external.** SafeWeb may route, explain, copy values, deliver an already-approved profile artifact, and run approved checks; OS/profile/account/security authorization remains with the user/platform.
6. **Review is event-driven.** A source/platform/service/endpoint/support/state/security/privacy contradiction immediately sets the affected record to `REVIEW_REQUIRED`; stale positive instructions do not remain active.
7. **Localization cannot strengthen claims.** English is semantic baseline; Turkish/Arabic/RTL variants bind to the same instruction ID/version and evidence strength. `SafeWeb` and technical endpoints remain LTR/untranslated.
8. **No named external service is currently hard-coded.** The service layer supports zero or one service only when a separately current approved named-service instruction exists. Until then, the correct service outcome is skip/Not covered/uncertain.

## 3. Current external source set rechecked 2026-08-29

| Source ID | First-party source | Current fact relied upon |
| --- | --- | --- |
| `ANDROID-PRIVATE-DNS` | Google Android Help — `https://support.google.com/android/answer/9654714?hl=en` | Android exposes Private DNS with `Automatic` and `Private DNS provider hostname`; UI can vary by device/version; Private DNS protects DNS questions/answers only. |
| `CHROME-SECURE-DNS` | Google Chrome Help — `https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DAndroid&hl=en` | Chrome can use automatic or another/custom Secure DNS provider; browser-specific resolver behavior can conflict with a system-DNS coverage assumption. |
| `APPLE-DNS-SETTINGS` | Apple Platform Deployment — `https://support.apple.com/en-gb/guide/deployment/dep86469ba99/1/web/1.0` | DNS Settings payload supports HTTPS/TLS; HTTPS uses a Server URL beginning with `https://`. |
| `APPLE-PROFILE-INSTALL` | Apple iPhone User Guide — `https://support.apple.com/en-euro/guide/iphone/iph6c493b19/ios` | Downloaded configuration profiles require user permission to install; installed profiles are visible under VPN & Device Management. |
| `APPLE-PROFILE-REMOVE` | Apple Support — `https://support.apple.com/guide/personal-safety/review-and-delete-configuration-profiles-ips327569a75/1.0/web/1.0` | Removing a profile removes its associated settings; managed/school/business profiles require management-authority caution. |
| `APPLE-SCREEN-TIME` | Apple Support UK — `https://support.apple.com/en-gb/105121` | Screen Time / Content & Privacy Restrictions provide current iPhone parental-control capabilities; Family context and settings can vary. |
| `ANDROID-PARENTAL-CONTROLS` | Google Android Help — `https://support.google.com/android/answer/16766047?hl=en` | Current Android 17+ can expose on-device parental controls; Family Link is another supported Android parental-control route where applicable. |
| `FAMILY-LINK-DEVICES` | Google For Families — `https://support.google.com/families/answer/9116646?hl=en` | Family Link supervision works on supported Android devices; most supervision tools do not work on iPhone/iPad. |

Project-owned source truth remains stronger for SafeWeb-specific endpoints, tested support, state semantics and recovery evidence.

## 4. Registry

Every active record below contains the ACC-0323 fields: applicability, source, last verification, owner, expected result, fallback and test case. `Review trigger` and `unsupported state` are additionally mandatory governance fields.

| ID | Version | Purpose | Applicability | Sources | Owner | Last verified | Expected result | Fallback | Unsupported / uncertain state | Test case |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DEV-AND-DNS-SETUP` | 1.0.0 | Configure SafeWeb DNS | Android phone 9+; Private DNS provider-hostname control present/usable; no known policy block | TSK-0307; TSK-0317; TSK-0409; ANDROID-PRIVATE-DNS | Content + Network Engineering | 2026-08-29 | `dns.usesafeweb.com` saved in provider-hostname mode; return for technical check; no S1 yet | Restore normal Private DNS policy, normally `Automatic`, if setup breaks connectivity | Missing/locked/broken control → S4/S5; never invent VPN/client route | `TC-0323-AND-SETUP-01` |
| `DEV-AND-DNS-VERIFY` | 1.0.0 | Verify Android DNS path | Current supported Android DNS tuple after setup | TSK-0307; TSK-0409; TSK-0320/0322; CHROME-SECURE-DNS | Network Engineering + Content | 2026-08-29 | S1 only when approved technical check confirms intended encrypted DNS path and no known conflict invalidates it | S3 if a known repair exists; S5 if conflict/evidence is inconclusive | VPN/custom browser/app resolver/network block/unproven tuple → S5/S4 | `TC-0323-AND-VERIFY-01` |
| `DEV-AND-DNS-REMOVE` | 1.0.0 | Remove/recover Android DNS | Supported Android path with SafeWeb provider configured or partial setup | TSK-0307; TSK-0317; TSK-0409; ANDROID-PRIVATE-DNS | Content + Network Engineering | 2026-08-29 | Custom SafeWeb provider removed; normal platform DNS policy restored; SafeWeb DNS state S6 | Neutral connectivity check; if still broken, show non-SafeWeb network troubleshooting without preserving a protection claim | No silent plaintext fallback while retaining S1/protection wording | `TC-0323-AND-REMOVE-01` |
| `DEV-IOS-DNS-SETUP` | 1.0.0 | Configure SafeWeb DNS | iPhone iOS 14+; exact separately verified SafeWeb DNS profile; local/manual install allowed; not managed-blocked | TSK-0307; TSK-0317; TSK-0409; APPLE-DNS-SETTINGS; APPLE-PROFILE-INSTALL | Content + Network Engineering | 2026-08-29 | User explicitly approves exact profile using `https://dns.usesafeweb.com/dns-query`; return for technical check; no S1 from presence | Remove exact profile if installation/configuration causes material connectivity problem | iPad/Mac/other unaccepted family, managed/supervised restriction, unavailable exact profile → S4/S5 | `TC-0323-IOS-SETUP-01` |
| `DEV-IOS-DNS-VERIFY` | 1.0.0 | Verify iPhone DNS path | Current supported iPhone DNS tuple after exact profile installation | TSK-0307; TSK-0409; TSK-0320/0322 | Network Engineering + Content | 2026-08-29 | S1 only after approved technical verification of intended path | S3 for known repair; S5 for unresolved conflict | VPN/Private Relay/custom resolver/network conflict or profile-only evidence → S5; never infer S1 | `TC-0323-IOS-VERIFY-01` |
| `DEV-IOS-DNS-REMOVE` | 1.0.0 | Remove/recover iPhone DNS | Supported iPhone path with exact SafeWeb profile installed | TSK-0307; TSK-0317; TSK-0409; APPLE-PROFILE-REMOVE | Content + Network Engineering | 2026-08-29 | Exact SafeWeb profile and its settings removed; SafeWeb DNS state S6; neutral connectivity restored/checked | If device is managed, follow managing authority rather than bypassing controls | Unknown/managed profile ownership → stop and use management-authority guidance/S5 | `TC-0323-IOS-REMOVE-01` |
| `DEV-COMMON-CONFLICT` | 1.0.0 | Represent DNS conflict truthfully | Any supported-family attempt with VPN, Private Relay, browser/app resolver, blocked encrypted-DNS transport, captive portal, managed network or unproven tuple | TSK-0409; TSK-0320/0322; CHROME-SECURE-DNS | Content + Network Engineering | 2026-08-29 | S3 only for a proven repair; otherwise S5/S4 with one safe next action | Removal/recovery or current official guidance; continue independent layers only if their own requirements pass | Never ask user to weaken required employer/school/security controls merely to obtain green status | `TC-0323-CONFLICT-01` |
| `DEV-COMMON-NOT-COVERED` | 1.0.0 | Stop unsupported device/network paths | Any platform/device/network/profile combination outside current TSK-0409 support | TSK-0409; TSK-0320/0322 | Content | 2026-08-29 | S4 `Not covered` with concise reason; no speculative setup | Current official platform guidance may be linked for understanding only; no SafeWeb support claim | Unsupported/not-yet-supported remains S4/S5 until direct current evidence changes support matrix | `TC-0323-NOTCOVERED-01` |
| `DEV-COMMON-RECOVERY` | 1.0.0 | Safe connectivity recovery | Supported DNS path where SafeWeb configuration materially breaks intended resolution | TSK-0317; TSK-0319; TSK-0409 | Content + Network Engineering | 2026-08-29 | Exact SafeWeb configuration removed/reset; neutral connectivity check; S6 if removed | Platform normal DNS behavior; no alternate unreviewed resolver/client | If neutral connectivity remains broken, SafeWeb cannot claim recovery cause; route to ordinary network help/S5 | `TC-0323-RECOVERY-01` |
| `DEV-IOS-NATIVE` | 1.0.0 | Route iPhone native safeguard | Current supported iPhone branch; Screen Time/Content & Privacy Restrictions relevant; parent can use Apple-owned flow | TSK-0143; TSK-0320/0322; APPLE-SCREEN-TIME | Content | 2026-08-29 | Already configured → S2 and skip duplicate work; needs setup → Apple current flow then S2 on parent confirmation; no S1 technical claim | If prerequisite/account/family state is missing, route to Apple-owned setup without collecting credentials | Managed/restricted/unmatched/stale path → S4/S5; Family Link is not treated as equivalent iPhone supervision | `TC-0323-IOS-NATIVE-01` |
| `DEV-AND-NATIVE` | 1.0.0 | Route Android native safeguard | Current supported Android phone; exact approved parental-control mechanism applicable to device/version/account state | TSK-0143; TSK-0320/0322; ANDROID-PARENTAL-CONTROLS; FAMILY-LINK-DEVICES | Content | 2026-08-29 | Already configured → S2/skip; Android 17+ on-device route only when actually applicable; Family Link only where current prerequisites apply; no S1 technical claim | Use Google-owned flow for required account/supervision setup; SafeWeb never collects credentials | Unknown OEM/managed/unmatched/stale path → S4/S5; do not infer Android 17+ from UI appearance | `TC-0323-AND-NATIVE-01` |
| `SVC-ONE-RELEVANT` | 1.0.0 | Route zero-or-one external service safeguard | Only when a separately current approved named-service record exists and parent declares that service relevant | TSK-0144; TSK-0320/0322; current provider source required per named record | Content | 2026-08-29 | Zero services is valid; one applicable service may be guided; completion is S2 parent-confirmed unless a future separately approved verifier exists | No relevant/current supported named service → skip/S4; stale/ambiguous provider rule → S5 | **No named external service is currently hard-coded by this catalogue.** A named service is unsupported until a current provider-specific record satisfies all TSK-0144 fields. | `TC-0323-SVC-ROUTE-01` |

## 5. Instruction procedures

### `DEV-AND-DNS-SETUP`
1. Confirm the branch is a supported Android phone and the provider-hostname control is usable.
2. Open Android **Private DNS** using current device wording/search when necessary.
3. Choose **Private DNS provider hostname**.
4. Enter exactly `dns.usesafeweb.com` — no `https://` prefix and no `:853` suffix.
5. Save using the OS action.
6. Return to SafeWeb and run the approved technical check.
7. Do not label the result `Verified` until that check succeeds.

### `DEV-AND-DNS-REMOVE`
1. Open Android Private DNS.
2. Leave the custom SafeWeb provider-hostname mode.
3. Restore the normal platform policy, normally **Automatic**, unless the user independently chooses another non-SafeWeb policy.
4. Run a neutral connectivity check where available.
5. Set SafeWeb DNS to S6 `Removed`; withdraw the active protection claim.

### `DEV-IOS-DNS-SETUP`
1. Confirm the branch is an accepted iPhone/iOS 14+ path and that the exact profile artifact/version for the environment has separately passed its artifact verification.
2. Deliver only that exact profile artifact.
3. Let iOS display the profile contents and request explicit installation permission.
4. The profile uses the approved DoH endpoint `https://dns.usesafeweb.com/dns-query`.
5. Complete the iOS-owned installation flow; SafeWeb must not claim silent/background installation.
6. Return to SafeWeb and run the approved technical check.
7. Profile presence alone is not S1.

### `DEV-IOS-DNS-REMOVE`
1. Open **Settings → General → VPN & Device Management** using current Apple wording.
2. Identify the exact SafeWeb profile.
3. Remove that profile and follow the OS prompts.
4. Run a neutral connectivity check where available.
5. Set SafeWeb DNS to S6 `Removed`; withdraw the active protection claim.
6. If the profile/device is managed by school/business/another authority, stop and follow that authority instead of bypassing policy.

### `DEV-IOS-NATIVE`
1. If the relevant Apple native safeguard is already configured, do not make the parent redo it; record only S2 parent confirmation unless contrary evidence exists.
2. If setup is needed, route to Apple's current Screen Time / Content & Privacy Restrictions flow; do not duplicate Apple credentials or account data in SafeWeb.
3. If the state is unknown, show a concise current-source check route and retain S5 until resolved.
4. If management/account/family prerequisites prevent the approved path, use S4/S5 rather than a workaround.

### `DEV-AND-NATIVE`
1. If an approved relevant Android native safeguard is already configured, skip duplicate setup and use S2 parent confirmation.
2. Use Android 17+ on-device parental controls only when the exact device actually supports that current route.
3. Use Family Link only when the exact Android/account prerequisites make it the approved route.
4. Keep Google credential/account actions inside Google-owned surfaces; SafeWeb does not collect them.
5. Unknown/managed/unmatched device states remain S4/S5 rather than guessed OEM instructions.

### `SVC-ONE-RELEVANT`
1. Build the selectable set only from separately current, approved named-service instruction records.
2. Ask only which one currently supported service is actually used/planned, if any; zero is valid.
3. Never infer service use from DNS/browsing/app history, popularity, age, advertising data or a persistent child profile.
4. Present at most one service instruction.
5. Parent completion is S2 unless a future separately approved technical verifier exists.
6. If no current named-service record qualifies, show no setup instruction; use skip/S4/S5 as appropriate.

## 6. Explicit unsupported states

The following are not silently supported by v1.0.0:

- Android below 9 for SafeWeb native encrypted DNS;
- Android tablet, ChromeOS, unaccepted Android-derived family, or Android phone without usable provider-hostname control;
- iPhone below iOS 14 for the current DNS-profile baseline;
- iPad, Mac, Apple Vision Pro or other unaccepted Apple family for the current SafeWeb public DNS path;
- managed/supervised device paths without exact accepted management-compatible evidence;
- captive-portal, enterprise-managed, IPv6-only/NAT64-only combinations without exact accepted evidence;
- any VPN/Private Relay/browser/app custom-resolver coexistence not directly accepted for the exact tuple;
- any named external service without a current provider-specific SafeWeb instruction record;
- any stale instruction after a review trigger fires.

Unsupported paths render S4 `Not covered` when clearly outside support; ambiguous/conflicting/stale paths render S5 `Status uncertain`.

## 7. Review, expiry and deprecation

There is no arbitrary date-only expiry that can preserve contradicted guidance. Each record becomes `REVIEW_REQUIRED` immediately on the earliest material trigger:

- OS/platform/vendor major or settings-path change;
- endpoint/profile/certificate/transport/support-matrix change;
- provider age/account/control-policy change;
- current target evidence contradicts the instruction;
- source URL/text no longer supports the relied-upon fact;
- security/privacy/safeguarding decision changes the safe recommendation;
- protection-state semantics or visible product terminology changes;
- localization reveals a material applicability difference rather than a translation-only change.

Versioning:
- **MAJOR:** applicability/state/fallback semantics or public interaction changes incompatibly;
- **MINOR:** new supported instruction/service/device record without invalidating existing semantics;
- **PATCH:** source/copy clarification that does not change applicability, expected result, fallback or state meaning.

Deprecated records remain traceable in history/evidence but are removed from the active selector. They are never silently deleted from audit history or shown as current.

## 8. Test cases

| Test | Scenario | Required result |
| --- | --- | --- |
| `TC-0323-AND-SETUP-01` | Supported Android phone with usable Private DNS | Shows hostname only; OS action remains user-controlled; no S1 until verifier succeeds. |
| `TC-0323-AND-VERIFY-01` | Android configured but Chrome custom Secure DNS/VPN conflict exists | Does not preserve universal S1; renders S5/S4 or bounded state per current evidence. |
| `TC-0323-AND-REMOVE-01` | Remove SafeWeb Android provider | Returns normal DNS policy; S6; no residual protection claim. |
| `TC-0323-IOS-SETUP-01` | Supported iPhone with exact approved profile | Explicit iOS approval; exact DoH endpoint; no silent install/no S1 from presence. |
| `TC-0323-IOS-VERIFY-01` | Profile present but Private Relay/VPN coexistence unproven | S5; no compatibility/incompatibility claim beyond evidence. |
| `TC-0323-IOS-REMOVE-01` | Remove exact SafeWeb profile | Associated SafeWeb settings removed; S6; management boundary respected. |
| `TC-0323-CONFLICT-01` | Required encrypted-DNS transport blocked | S3 only with proven repair, otherwise S5; removal/recovery offered; no silent plaintext protection claim. |
| `TC-0323-NOTCOVERED-01` | iPad/Android tablet/unaccepted managed device | S4/S5; no guessed setup path. |
| `TC-0323-RECOVERY-01` | SafeWeb config causes name-resolution failure | Exact configuration removed/reset; neutral connectivity check; protection claim withdrawn. |
| `TC-0323-IOS-NATIVE-01` | Screen Time already configured vs needs setup vs blocked | Already configured skips duplicate work/S2; setup uses Apple-owned current path; blocked/unmatched → S4/S5. |
| `TC-0323-AND-NATIVE-01` | Android 17+ route vs Family Link vs unknown OEM | Exact applicable route only; no credentials collected; unknown/unmatched → S4/S5; positive state S2 only. |
| `TC-0323-SVC-ROUTE-01` | No approved named service; none relevant; one future approved relevant service | Current v1 yields zero-service/Not covered as appropriate; never invents a named service; maximum one branch. |

## 9. Engineering and QA handoff

For INT-0009/INT-0010, implementation must bind rendered setup/help/status content to the instruction ID and version. QA can objectively assert applicability, exact technical value, expected state, fallback, unsupported behavior and review metadata without subjective reconstruction.

No instruction adds a mandatory SafeWeb account, persistent dashboard, browsing-history collection, child identity record, or credentials. The catalogue does not authorize implementation/publication/launch by itself.
