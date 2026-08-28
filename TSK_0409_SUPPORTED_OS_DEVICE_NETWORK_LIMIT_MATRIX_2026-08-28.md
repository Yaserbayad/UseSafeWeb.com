# TSK-0409 — Supported OS, Device, Network and Known-Limit Matrix

**Task:** TSK-0409 — Freeze supported OS/device/network install, verification, removal, and known-limit matrix  
**Acceptance:** ACC-0409  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 SUPPORT CONTRACT / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0408 DNS identity/platform contract + TSK-0511 supported-device evidence + TSK-0514 external-network/removal evidence + TSK-0320 protection-state contract + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

This matrix freezes the strongest **technical support boundary currently justified by direct project evidence and current first-party platform documentation**. It is not representative-parent usability evidence and does not prove that setup is easy, understood, preferred, or low-support. `RSK-0002` remains OPEN.

The matrix deliberately marks untested device/network combinations `NOT_YET_SUPPORTED` or `UNCERTAIN` instead of extrapolating from one tested phone. It does not make LG-05/LG-06 PASS and does not authorize implementation/build, participant processing, legal completion, payment, public release or launch.

## 1. Support-state vocabulary

| Status | Meaning | Protection-state consequence |
| --- | --- | --- |
| `SUPPORTED` | The platform family/mechanism is in the current UseSafeWeb support baseline and the exact current path can reach and pass the approved verifier. | May reach TSK-0320 S1 `Verified` only after current verification succeeds. |
| `CONDITIONAL` | The platform mechanism is supported in principle, but current network/device context must pass an explicit check before UseSafeWeb can rely on it. | S2/S3/S5 until the condition is resolved; never infer S1. |
| `NOT_YET_SUPPORTED` | Platform capability may exist, but current project evidence does not directly justify support for this combination. | TSK-0320 S4 `Not covered` or S5 where the exact state is uncertain. |
| `UNSUPPORTED` | The current baseline lacks the required native capability/mechanism or the product explicitly excludes the path. | S4 `Not covered`. |
| `CONFLICT` | Another resolver/tunnel/network control can override or bypass the intended UseSafeWeb DNS path and the project cannot currently prove coexistence. | S5 `Status uncertain` unless the exact conflict is directly tested and resolved. |

A supported **platform family** is not a promise that every OEM build, browser, VPN, app or network is supported. `Verified` is granted only to the current tuple actually proven by the verifier.

## 2. Current frozen platform baseline

### Android phone baseline

| Dimension | Current status | Install/configuration | Verification | Removal/recovery | Known limit |
| --- | --- | --- | --- | --- | --- |
| Android phone, Android 9+, `Private DNS provider hostname` present and usable | `SUPPORTED` | Enter hostname `dns.usesafeweb.com`; Android native path is DoT, not DoH URL entry. | Current approved synthetic/technical verification must succeed; configuration presence alone is insufficient. | Return Private DNS from custom provider to normal platform policy, normally `Automatic`; current project evidence proves normal DNS/internet recovery after reset/removal. | OEM/settings wording can vary; if the setting is unavailable or locked, this self-service path is not supported. |
| Android below 9 | `UNSUPPORTED` | No current UseSafeWeb native baseline. | None. | No UseSafeWeb configuration should be introduced. | Android 9 is the current minimum native DoT baseline. |
| Android 9+ device where Private DNS hostname control is absent, broken, disabled by policy, or cannot authenticate `dns.usesafeweb.com` | `NOT_YET_SUPPORTED` | Do not improvise another client/app/VPN workflow. | Must not show Verified. | Restore normal device DNS policy if a partial configuration exists. | Manufacturer/management policy can differ. |
| Android tablet, ChromeOS or other non-phone Android-derived device | `NOT_YET_SUPPORTED` | No public UseSafeWeb instruction yet. | No support claim until direct device-family test. | N/A until supported. | Technical similarity to Android phones is not acceptance evidence. |

Google currently exposes `Private DNS provider hostname` in Android network settings and states that Private DNS protects DNS questions/answers only. Android/AOSP documentation states Android 9+ has built-in DNS-over-TLS support. Current UseSafeWeb direct evidence establishes the accepted Android phone family and removal/recovery.

### Apple phone baseline

| Dimension | Current status | Install/configuration | Verification | Removal/recovery | Known limit |
| --- | --- | --- | --- | --- | --- |
| iPhone, iOS 14+, approved manually installed UseSafeWeb DNS Settings profile | `SUPPORTED` | Apple DNS Settings profile using HTTPS/DoH Server URL `https://dns.usesafeweb.com/dns-query`. | Current approved synthetic/technical verification must succeed; profile presence alone is insufficient. | Remove the UseSafeWeb profile from Settings > General > VPN & Device Management; direct project evidence proves normal DNS/internet recovery. | Manual profile install requires explicit user/OS authorization. |
| iPhone/iOS below 14 | `UNSUPPORTED` | No current UseSafeWeb native encrypted-DNS profile baseline. | None. | No UseSafeWeb profile should be introduced. | Current project baseline starts at iOS 14+. |
| iPad/iPadOS, Mac, Apple Vision Pro or other Apple device family | `NOT_YET_SUPPORTED` | No public UseSafeWeb instruction yet. | No support claim until direct device-family test. | N/A until supported. | Apple documents encrypted DNS capability on additional families, but UseSafeWeb has only direct iPhone acceptance evidence. |
| Supervised/managed iPhone where policy/MDM controls DNS/profile behavior | `NOT_YET_SUPPORTED` | Do not assume the normal manual profile path. | Must not show Verified without exact managed-device test. | Follow the managing authority's profile-removal policy. | Apple documents different behavior for managed versus local installation. |

Apple documents `com.apple.dnsSettings.managed`, HTTPS Server URL semantics, and that manually installed DNS settings apply to all networks. Current UseSafeWeb evidence directly proves one representative iPhone path on Wi-Fi and cellular plus profile removal/recovery.

## 3. Network support matrix

| Network/context | Android 9+ phone | iPhone iOS 14+ | Frozen rule |
| --- | --- | --- | --- |
| Qualifying external cellular network | `SUPPORTED` when current verification passes | `SUPPORTED` when current verification passes | Direct UseSafeWeb evidence: Android external-cellular PASS; iPhone cellular PASS. |
| Ordinary Wi-Fi with unrestricted required encrypted-DNS connectivity | `CONDITIONAL` | `SUPPORTED`/`CONDITIONAL` | iPhone Wi-Fi is directly proven. Android family support is valid only when the current verifier succeeds; no claim that every Wi-Fi permits TCP 853. |
| Captive portal / pre-authentication network | `NOT_YET_SUPPORTED` | `NOT_YET_SUPPORTED` | Complete captive-portal access first using normal network behavior; do not claim protection until the intended encrypted path can be verified. No current project captive-portal test exists. |
| Network blocking DoT TCP 853 | `CONFLICT` | N/A to Apple DoH path | Android UseSafeWeb DoT cannot be considered active when the intended transport is unreachable. Show Action needed/Uncertain and offer removal/recovery, never silent plain-DNS fallback under the UseSafeWeb protection claim. |
| Network blocking HTTPS/DoH to `dns.usesafeweb.com:443` | N/A to Android DoT path | `CONFLICT` | iPhone DoH cannot be considered active when the intended endpoint is unreachable. Show Action needed/Uncertain and offer removal/recovery. |
| IPv6-only/NAT64-only or unusual translation environment | `NOT_YET_SUPPORTED` | `NOT_YET_SUPPORTED` | Current public resolver evidence is A-only and there is no direct UseSafeWeb acceptance test for an IPv6-only/NAT64 environment. Do not extrapolate. |
| Enterprise/managed network enforcing its own DNS/VPN/security policy | `NOT_YET_SUPPORTED` | `NOT_YET_SUPPORTED` | Self-service support requires exact policy-compatible testing and authorization; do not bypass organizational controls. |

A network is never declared supported solely because ordinary web access works. The intended UseSafeWeb encrypted path must itself pass the current verifier.

## 4. VPN conflict matrix

### Android

Android's official `VpnService.Builder` lets a VPN set DNS servers for the VPN connection. Therefore an active VPN can materially change the resolver path.

- Generic active VPN: `CONFLICT` / S5 until the exact VPN configuration is tested.
- VPN explicitly setting non-UseSafeWeb DNS: UseSafeWeb system-DNS coverage for tunneled traffic is `NOT_YET_SUPPORTED`/not covered.
- VPN without custom DNS: still `CONDITIONAL`; do not assume coexistence from absence of a visible custom DNS field.
- Always-on/managed VPN: `NOT_YET_SUPPORTED` unless a separate exact integration test proves the UseSafeWeb path.

UseSafeWeb must not ask a user to disable a required employer/school/security VPN merely to obtain a green state. The correct product state is uncertainty/not-covered unless an approved coexistence path exists.

### Apple

Apple's Network Extension documentation allows tunnel DNS settings and split/default DNS routing. Therefore VPNs can also alter the DNS resolver path on Apple devices.

- Generic active VPN: `CONFLICT` / S5 until exact coexistence is tested.
- VPN whose tunnel DNS becomes default: UseSafeWeb profile coverage cannot be presumed.
- Managed VPN: `NOT_YET_SUPPORTED` under the self-service baseline.

No current UseSafeWeb project evidence proves compatibility with any named third-party VPN product.

## 5. Apple iCloud Private Relay boundary

Apple states that iCloud Private Relay primarily protects Safari browsing and also includes DNS name-resolution requests, with DNS records encrypted through the relay architecture.

Current UseSafeWeb evidence has **not** directly tested coexistence between the UseSafeWeb DNS Settings profile and iCloud Private Relay.

Therefore:

- iCloud Private Relay enabled: `CONFLICT` / S5 for any claim that UseSafeWeb is controlling the relevant Safari/DNS path.
- Do not show S1 `Verified` merely because the UseSafeWeb profile is installed while Private Relay is active.
- Do not claim that Private Relay definitely disables or definitely preserves UseSafeWeb; current evidence does not establish that exact coexistence outcome.
- A future direct test may narrow this rule for a specific iOS/version/profile configuration.

This is an uncertainty boundary, not an instruction to disable a privacy feature.

## 6. Browser/app encrypted-DNS and resolver-bypass boundary

### Chrome on Android

Google Chrome currently exposes `Use secure DNS` and allows selecting the current or another/custom provider. Therefore a browser-specific DNS provider can create a resolver path that is not safely inferred from the Android system Private DNS setting.

- Chrome explicitly configured to a different custom Secure DNS provider: `CONFLICT` / browser traffic not covered by the system UseSafeWeb verification claim.
- Chrome automatic/current-provider mode: `CONDITIONAL`; current UseSafeWeb evidence does not independently prove every Chrome resolver mode, so system S1 must not be rewritten as a universal browser guarantee.

### Any platform/app

Any app/browser that implements its own DNS-over-HTTPS, DNS-over-TLS, DNS-over-QUIC, VPN tunnel, proxy resolver or hard-coded resolver is `NOT_YET_SUPPORTED` for that traffic unless the exact behavior is directly tested.

UseSafeWeb DNS is therefore a DNS-layer protection mechanism, not a guarantee that every app/request on a device can never bypass DNS filtering.

## 7. Apple profile-installation constraints

Apple currently requires an explicit Settings installation step for a manually downloaded configuration profile. Apple also documents that profile installation can interact with Stolen Device Protection outside a familiar location.

Frozen UseSafeWeb rule:

- manual profile installation remains an explicit user/OS action;
- UseSafeWeb must not claim silent install;
- if current iOS security policy blocks profile installation, show Action needed/Not covered for the current attempt rather than instructing the user to weaken an unrelated device-security feature merely to make UseSafeWeb pass;
- the product may point to current Apple guidance, but any future instruction to change security settings requires its own reviewed UX/security decision.

## 8. Verification matrix

| Condition | Allowed state |
| --- | --- |
| Exact supported platform/mechanism + current verifier succeeds + no known conflict | TSK-0320 S1 `Verified` |
| User entered/installed configuration but verifier has not succeeded | S2 only where parent confirmation is appropriate, otherwise configured-unverified internal state; never S1 |
| Supported path fails with a known repair | S3 `Action needed` |
| Unsupported/unaccepted platform family | S4 `Not covered` |
| VPN/Private Relay/browser/app/network conflict cannot be resolved confidently | S5 `Status uncertain` |
| UseSafeWeb DNS configuration removed/reset | S6 `Removed` |

Verification uses controlled/synthetic tests only. It does not require browsing/query history, persistent identity or a child/device profile.

## 9. Removal/recovery matrix

### Android

1. Leave `Private DNS provider hostname` mode for the UseSafeWeb hostname.
2. Restore the platform's normal policy, normally `Automatic` unless the user independently chooses another setting.
3. Confirm normal DNS/internet recovery using neutral/synthetic checks.
4. Mark UseSafeWeb DNS S6 `Removed`; do not retain a protection claim.

Direct project evidence proves normal DNS/internet recovery after Android removal/reset.

### iPhone

1. Identify the exact UseSafeWeb DNS profile.
2. Remove it under Settings > General > VPN & Device Management.
3. Apple states that deleting a profile deletes its associated settings.
4. Confirm normal DNS/internet recovery with neutral/synthetic checks.
5. Mark UseSafeWeb DNS S6 `Removed`.

Direct project evidence proves iPhone removal/recovery. Apple first-party guidance independently supports the profile-removal semantics.

## 10. Release/support review triggers

The matrix must be re-audited before expanding a support claim when any of these change:

- new Android/iOS major release or material Settings/profile behavior change;
- new supported device family (tablet/iPad/Mac/etc.);
- new Apple profile format/signing/distribution method;
- new browser/app resolver behavior relied upon by the product;
- VPN/Private Relay coexistence support claim;
- resolver endpoint, certificate, transport or port change;
- addition of AAAA/IPv6-native service support;
- material network-path change;
- current verification method changes;
- direct evidence contradicts any current supported/unsupported classification.

Contradictory target evidence reopens the affected support row; it is not averaged away.

## 11. Testable acceptance assertions

A later implementation/QA suite must prove:

1. Android instructions are shown only to Android 9+ phones with usable Private DNS hostname capability.
2. Android input is `dns.usesafeweb.com`, never the DoH URL.
3. iPhone instructions are shown only to current accepted iOS 14+ profile-capable paths.
4. iPhone profile uses `https://dns.usesafeweb.com/dns-query`.
5. iPad/Mac/other untested families are not silently treated as supported.
6. Profile/provider presence alone never produces S1.
7. External cellular support remains subject to current verification even though the family-level path has direct evidence.
8. Android Wi-Fi does not receive a universal network-support promise; TCP 853 reachability/current verification is required.
9. A VPN conflict demotes the result to S5 unless the exact coexistence path is directly proven.
10. iCloud Private Relay coexistence is not represented as proven either way.
11. Chrome/other app custom resolver paths are not included in a universal system-DNS coverage claim.
12. Captive-portal, enterprise-managed and IPv6-only/NAT64-only combinations remain unsupported/not-yet-supported until directly tested.
13. Android removal restores normal DNS policy and clears the UseSafeWeb protection claim.
14. iPhone profile removal clears the UseSafeWeb profile settings and the UseSafeWeb protection claim.
15. No unsupported combination is made to appear supported by adding more confirmations.
16. No verification test stores real-user browsing/query history or persistent device identity.
17. A material OS/network/resolver change triggers re-verification/review rather than preserving stale S1.

## 12. Current evidence/source index

### Canonical UseSafeWeb evidence

- `TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md` — blob `52860ce167fc8a31962cd412772e428d280c8184`.
- `TSK_0511_SUPPORTED_DEVICE_VERIFICATION_COMPLETION_EVIDENCE_2026-08-28.md` — blob `ecd959f93ab7dff62aba6529ce66b45d59c3ed27`.
- `TSK_0514_EXTERNAL_ENDPOINT_COMPLETION_EVIDENCE_2026-08-28.md` — blob `c5d004d0e0a8c58d1056b3aaad38034ae4188a68`.
- `TSK_0442_TLS_CERTIFICATE_EVIDENCE_2026-08-28.md` — blob `cb11394af1e80f15d85bda5d9b000bbf0efd6d20`.
- `CURRENT_STATE.md` — current runtime/frozen endpoint identity and A-only public-DNS evidence.

### Current first-party platform sources checked 2026-08-28

- Google Android Help — Private DNS: https://support.google.com/android/answer/9654714?hl=en
- Android Open Source Project — Android 9+ DNS-over-TLS / DNS Resolver: https://source.android.com/docs/core/ota/modular-system/dns-resolver
- Android Developers — VPN DNS servers: https://developer.android.com/reference/android/net/VpnService.Builder
- Google Chrome Help — Secure DNS on Android: https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DAndroid&hl=en
- Apple Developer — DNS Settings payload: https://developer.apple.com/documentation/devicemanagement/dnssettings
- Apple Developer — NetworkDNSSettings/local installs: https://developer.apple.com/documentation/devicemanagement/networkdnssettings
- Apple Support — install configuration profile: https://support.apple.com/en-gb/102400
- Apple Support — remove configuration profiles: https://support.apple.com/en-gb/guide/iphone/iph6c493b19/ios
- Apple Platform Security — iCloud Private Relay security: https://support.apple.com/en-gb/guide/security/secad8ce3233/web
- Apple Developer — VPN/tunnel DNS routing: https://developer.apple.com/documentation/networkextension/nednssettings/matchdomains

## 13. ACC-0409 result

ACC-0409 requires every supported combination to have a tested mechanism or explicit unsupported status and requires Private Relay/VPN/app/browser/network bypass limits to be covered.

This matrix supplies explicit supported, conditional, conflict, not-yet-supported and unsupported classifications; binds Android/iPhone support to the exact TSK-0408 mechanisms; incorporates current direct Android/iPhone and external-network/removal evidence; and explicitly covers Private Relay, VPN DNS, browser/app Secure DNS, captive portals, managed networks, blocked transport, IPv6-only/NAT64 uncertainty and removal/recovery.

**TSK-0409 result: PASS candidate subject to independent verification and runtime read-back.**
