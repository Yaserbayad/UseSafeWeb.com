# TSK-0409 — Supported OS/device/network matrix verification evidence

**Task:** TSK-0409 — Freeze supported OS/device/network install, verification, removal, and known-limit matrix  
**Acceptance:** ACC-0409  
**Verification:** VER-0409 independent guarded support/source audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Support matrix: `TSK_0409_SUPPORTED_OS_DEVICE_NETWORK_LIMIT_MATRIX_2026-08-28.md`
- Matrix blob: `09318534ec097849cbe8c7391e2a1acc3ba5a79a`
- Matrix commit: `0eb73aa6e9a0c2d992d23471a197ee9232f0c151`
- TSK-0408 platform contract blob: `52860ce167fc8a31962cd412772e428d280c8184`
- TSK-0511 supported-device evidence blob: `ecd959f93ab7dff62aba6529ce66b45d59c3ed27`
- TSK-0514 external-network/removal evidence blob: `c5d004d0e0a8c58d1056b3aaad38034ae4188a68`
- TSK-0442 TLS/device evidence blob: `cb11394af1e80f15d85bda5d9b000bbf0efd6d20`
- TSK-0320 protection-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Current hard dependency: `TSK-0408 = PASS`.

## Authority/precondition audit

- TSK-0409 is L4 / A3 / AUTO_ALLOWED / HIGH with hard dependency TSK-0408, now runtime PASS.
- ACC-0409 requires a technical support/unsupported matrix and bypass-limit treatment. It does not require representative-parent usability evidence and is executable under DEC-0050/CR-0003.
- The matrix explicitly carries `RSK-0002` and does not claim that setup is behaviorally validated.
- The matrix does not authorize implementation, LG-05/LG-06, participants, legal completion, payment, public release or launch.

## Direct project-evidence audit

### Android accepted family

TSK-0511 directly defines the accepted Android family as Android 9+ phones with usable native Private DNS provider-hostname control using DoT to `dns.usesafeweb.com:853`. It records direct encrypted-DNS operation and removal/recovery, while TSK-0514 separately records an external-cellular PASS. The matrix preserves this family instead of broadening it to tablets, ChromeOS or every Android-derived device.

### iPhone accepted family

TSK-0511 directly defines the accepted Apple family as iPhone/iOS 14+ using the approved Apple DNS Settings DoH profile with Server URL `https://dns.usesafeweb.com/dns-query`. It records direct iPhone Wi-Fi PASS, cellular PASS and removal PASS. The matrix therefore supports iPhone but deliberately leaves iPad/Mac/other Apple families `NOT_YET_SUPPORTED` despite documented technical capability.

### Removal/recovery

TSK-0511 and TSK-0514 directly prove normal DNS/internet recovery after removing/resetting UseSafeWeb. TSK-0408 independently freezes Android return-to-normal-policy and Apple profile-removal semantics. The matrix preserves S6 `Removed` and explicitly withdraws the UseSafeWeb protection claim after removal.

## Current first-party source audit — checked 2026-08-28

### Android Private DNS

Google Android Help documents the current `Off`, `Automatic`, and `Private DNS provider hostname` choices and states Private DNS protects DNS questions/answers only. Android/AOSP documentation identifies Android 9+ as the built-in DNS-over-TLS baseline.

Sources:
- https://support.google.com/android/answer/9654714?hl=en
- https://source.android.com/docs/core/ota/modular-system/dns-resolver

**Disposition:** supports the Android 9+ hostname/DoT baseline; does not justify universal app/network coverage.

### Android VPN DNS override capability

Android Developers documents `VpnService.Builder.addDnsServer`, allowing a VPN to provide DNS servers for the VPN connection.

Source:
- https://developer.android.com/reference/android/net/VpnService.Builder

**Disposition:** an active VPN can materially alter the DNS path. The matrix correctly treats generic VPN coexistence as conflict/uncertain unless an exact configuration is directly tested.

### Chrome Secure DNS

Google Chrome Help documents Android Chrome `Use secure DNS`, including the ability to select the current or another/custom provider.

Source:
- https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DAndroid&hl=en

**Disposition:** a browser-specific custom DNS provider can create a resolver path that cannot be inferred from Android system Private DNS alone. The matrix correctly refuses a universal browser-coverage claim.

### Apple encrypted DNS profile

Apple Developer documentation identifies the DNS Settings payload, HTTPS Server URL semantics, and states that locally installed DNS settings apply to all networks while managed deployments can differ.

Sources:
- https://developer.apple.com/documentation/devicemanagement/dnssettings
- https://developer.apple.com/documentation/devicemanagement/networkdnssettings

**Disposition:** supports the current iPhone manual-profile/DoH mechanism and the managed-device exception. It does not turn untested iPad/Mac families into UseSafeWeb-supported devices.

### Apple profile installation/removal

Apple Support currently requires explicit Settings installation for manually downloaded profiles and states that deleting a profile deletes its associated settings. Apple also documents an interaction with Stolen Device Protection for profile installation outside a familiar location.

Sources:
- https://support.apple.com/en-gb/102400
- https://support.apple.com/en-gb/guide/iphone/iph6c493b19/ios

**Disposition:** supports explicit user authorization and removal/recovery rules. The matrix correctly refuses silent install and refuses to instruct users to weaken unrelated security merely to produce a green state.

### iCloud Private Relay

Apple Platform Security states that Private Relay primarily protects Safari browsing and also includes DNS name-resolution requests, with DNS records protected through the relay architecture.

Source:
- https://support.apple.com/en-gb/guide/security/secad8ce3233/web

**Disposition:** this is material contrary evidence against assuming the UseSafeWeb DNS profile controls every Safari/DNS request while Private Relay is active. Current UseSafeWeb evidence does not establish the exact coexistence result, so the matrix correctly freezes it as conflict/uncertain rather than claiming either guaranteed compatibility or guaranteed incompatibility.

### Apple VPN DNS routing

Apple Network Extension documentation states that tunnel DNS settings can select resolver domains and that a tunnel can become the default resolver path.

Sources:
- https://developer.apple.com/documentation/networkextension/nednssettings/matchdomains
- https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/dnssettings

**Disposition:** supports the Apple VPN conflict boundary; no generic VPN coexistence claim is justified.

## ACC-0409 clause audit

ACC-0409 requires: `Every supported combination has a tested mechanism or explicit unsupported status; Private Relay/VPN/app/browser/network bypass limits are covered.`

### Supported combinations — PASS

The matrix defines only two supported phone families:

1. Android 9+ phone with usable native Private DNS provider-hostname control, using the already accepted DoT path.
2. iPhone/iOS 14+ with the approved manually installed Apple DNS Settings DoH profile.

Both consume direct project evidence. No additional device family is silently promoted.

### Explicit unsupported/not-yet-supported status — PASS

The matrix explicitly classifies Android below 9, Android devices without usable Private DNS, Android tablets/ChromeOS/other derived devices, iOS below 14, iPad/Mac/other Apple families, managed/supervised device variants, captive portals, unusual enterprise/managed networks, IPv6-only/NAT64-only environments and untested app/browser/VPN paths.

### Private Relay limit — PASS

Private Relay coexistence is explicitly `CONFLICT`/S5 because Apple confirms it includes DNS name resolution but UseSafeWeb has no direct coexistence evidence. The artifact correctly refuses to claim either guaranteed bypass or guaranteed compatibility.

### VPN limit — PASS

Android and Apple first-party APIs both establish that VPN/tunnel configurations can control DNS. Generic VPN coexistence is therefore not accepted as supported without exact testing.

### App/browser bypass limit — PASS

Chrome Android's custom Secure DNS control is directly documented. The matrix also conservatively classifies any app/browser with an independent encrypted resolver as not-yet-supported for that traffic until exact testing exists.

### Network limits — PASS

The matrix covers external cellular, ordinary Wi-Fi, captive portals, DoT/DoH transport blocking, enterprise-managed networks and IPv6-only/NAT64 uncertainty. It does not pretend that ordinary internet access proves the UseSafeWeb encrypted path; current verification remains mandatory.

### Install, verification and removal — PASS

Each supported family has the exact platform-specific install value/mechanism, current-verifier requirement, and tested removal/recovery path. Android hostname entry is kept distinct from Apple full DoH Server URL/profile; configuration presence never equals S1.

## Adversarial findings and unresolved uncertainty

1. **No universal Android Wi-Fi evidence.** Android's platform family is supported, but the project does not have evidence that every Wi-Fi permits DoT TCP 853. The matrix correctly makes network support verification-gated.
2. **No iPad/Mac acceptance evidence.** Apple capability documentation is not equivalent to UseSafeWeb product acceptance. These families remain not-yet-supported.
3. **Private Relay coexistence is genuinely unresolved.** Apple documents Private Relay DNS handling, but current sources do not establish the exact precedence/coexistence outcome with this UseSafeWeb profile. S5 is therefore the correct stable result.
4. **Named VPN products are untested.** APIs prove the possibility of DNS override, not the behavior of every VPN. The matrix does not generalize beyond that evidence.
5. **Chrome automatic mode is not a universal browser-coverage proof.** Only explicit custom-provider conflict is directly clear; automatic/current-provider behavior still does not justify an all-browser guarantee from system-state evidence alone.
6. **IPv6-only/NAT64 is untested.** Current runtime records an A-only resolver hostname and no direct acceptance evidence for an IPv6-only/NAT64 path; the matrix correctly refuses support.
7. **Profile-install security friction can change.** Apple's 2026 profile-install guidance includes Stolen Device Protection interaction. The product must follow current Apple guidance rather than hard-coding a security-weakening workaround.
8. **Behavioral evidence is still missing.** None of the technical support classifications proves parent comprehension or usability. `RSK-0002` remains OPEN.

## Stable verification decision

The durable matrix directly satisfies ACC-0409, is conservative relative to direct target evidence, and incorporates current first-party contrary evidence capable of invalidating universal support claims. Untested combinations are explicitly fenced rather than inferred.

**Stable outcome: TSK-0409 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the L4 queue. Do not assume a human-only detailed-install task is executable merely because its dependency is ready; apply Action Authority before selection. Continue only with the highest-priority dependency-ready AUTO_ALLOWED provisional-L4 task whose acceptance does not require real-participant evidence.
