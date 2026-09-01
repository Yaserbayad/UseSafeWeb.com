# TSK-0409 — Supported Device / Network Verification and Bypass Matrix

**Task:** TSK-0409 — freeze supported-device/network verification coverage and explicit unsupported/bypass behavior  
**Acceptance:** ACC-0409 / VER-0409 / EVD-0409  
**Lifecycle:** L4 — Product / Experience definition  
**Version:** 1.0.0  
**Date:** 2026-09-01  
**Authority:** A3 / AUTO_ALLOWED under the current CR-0008 owner-frozen modular Master Planning System.  
**Dependency:** current TSK-0408 PASS.  
**Controls:** REQ-0042; REQ-0043; CON-0002; CON-0003; RSK-0004; INT-0013; current TSK-0320 protection-state contract.

## 1. Frozen invariants

1. The customer-facing service identity remains **UseSafeWeb DNS** and the approved resolver hostname remains **`dns.usesafeweb.com`**. This task does not invent another endpoint, profile URL, browser endpoint, account route, or administrative surface.
2. AdGuard remains the frozen filtering/policy layer. The approved upstream remains exactly **`https://dns10.quad9.net/dns-query` with ECS disabled**. No browser/device route in this matrix changes that server-side invariant.
3. Supported customer setup must use encrypted DNS through an explicitly approved platform mechanism.
4. **Configuration evidence is never technical protection evidence.** Seeing a profile, hostname, ClientID, device record, account ownership record, UI toggle, parent confirmation, or successful setup step may support `configured_parent_confirmed`; none may produce `protected_verified`.
5. `protected_verified` requires current technical evidence that the effective DNS path for the tested scope is UseSafeWeb and that the verification result satisfies the current TSK-0320 verifier contract.
6. When a browser, VPN, Private Relay, application, captive portal, network change, or unknown platform can change the effective resolver and UseSafeWeb cannot prove the current effective DNS path, the product must fail closed to `uncertain_error` or `not_covered`; it must not retain or display `protected_verified` from stale evidence.
7. DNS protection is one protection layer only. It is never presented as complete device, browsing, child, content, emergency, or surveillance coverage.
8. Verification and troubleshooting must not require collection of DNS questions, domains, URLs, browsing history, child activity, or persistent identity linkage.

## 2. Status vocabulary

- **SUPPORTED-L4:** The platform mechanism is current, documented, consistent with TSK-0408 and has a deterministic verification/recovery contract here. This is L4 support-definition evidence only; later implementation/device/runtime acceptance still has its own gates.
- **CONDITIONAL:** The base platform is supported, but a resolver-affecting feature can override/bypass the base path. The combination is supported only after the conflict is removed or current technical verification independently proves the effective path is UseSafeWeb.
- **NOT-COVERED:** The combination has no currently approved/tested UseSafeWeb mechanism. The UI must state that limitation instead of guessing.
- **UNCERTAIN/ERROR:** The mechanism is nominally supported but current technical evidence cannot establish the effective resolver because of error, captive portal, transient network condition, stale evidence, or an unclassified override.

These support labels are not runtime protection states. Runtime user-facing state remains exactly one of the six TSK-0320 states: `protected_verified`, `configured_parent_confirmed`, `action_needed`, `not_covered`, `uncertain_error`, `removed`.

## 3. Frozen support and bypass matrix

| Combination / condition | L4 support status | Approved mechanism / evidence | Required technical verification before `protected_verified` | Conflict / bypass semantics | Recovery / state outcome |
|---|---|---|---|---|---|
| Android supported release, system Private DNS, no known resolver override | SUPPORTED-L4 | Android **Private DNS provider hostname** using `dns.usesafeweb.com` (DoT hostname semantics from TSK-0408). Configuration presence is setup evidence only. | Fresh UseSafeWeb technical verifier result for the current device/network scope. | If effective resolver cannot be proven, do not infer from the Android setting. | Successful config but no technical proof -> `configured_parent_confirmed`; verified effective path -> `protected_verified`; verification failure -> `action_needed` or `uncertain_error` by reason. |
| Android + Chrome Secure DNS set to system/current-provider behavior, no custom non-UseSafeWeb provider | CONDITIONAL | Android base mechanism remains the supported route. Chrome documents browser Secure DNS behavior independently of Android system DNS. | Technical verification must include the browser scope if the user-facing claim covers Chrome. | If Chrome uses a custom other provider or falls outside the proven UseSafeWeb path, system configuration cannot prove Chrome coverage. | Custom/other provider -> `not_covered` for Chrome until switched to the supported system path and reverified; indeterminate browser path -> `uncertain_error`. |
| Android + Chrome custom Secure DNS provider not explicitly approved as UseSafeWeb | NOT-COVERED | No separate Chrome-specific UseSafeWeb endpoint is approved by TSK-0408. | None: do not claim protection for that browser combination. | Browser resolver can differ from Android system resolver. | Explain the conflict; return Chrome to the supported system route, then reverify. Until then -> `not_covered`. |
| Android + app-specific DoH/DoT/custom resolver | NOT-COVERED | No app-specific resolver integration is approved by this task. | None unless a later task explicitly supports and tests that app mechanism. | App-level resolver can bypass system Private DNS assumptions. | `not_covered` for that app; do not downgrade unrelated independently verified layers unless their scope is affected. |
| Android + VPN or DNS-changing security/privacy app | CONDITIONAL | Android base Private DNS remains the supported mechanism only if the effective DNS path is independently proven. | Fresh verification after VPN/app activation and after meaningful VPN configuration changes. | VPN/app policy may replace, intercept, tunnel, or otherwise affect DNS. | Effective UseSafeWeb path proven -> `protected_verified`; known non-UseSafeWeb path -> `not_covered`; indeterminate -> `uncertain_error`. |
| Apple iPhone/iPad supported release, approved UseSafeWeb DoH configuration profile, Private Relay not affecting tested path | SUPPORTED-L4 | TSK-0408 Apple DoH profile/Server-URL mechanism. Profile/configuration presence is not verification. | Fresh technical verification for the current device/network scope. | Any unresolved Private Relay/VPN/browser/app resolver interaction invalidates optimistic inference. | Profile present without proof -> `configured_parent_confirmed`; verified path -> `protected_verified`; failure -> `action_needed`/`uncertain_error`. |
| Apple iPhone/iPad + iCloud Private Relay / Limit IP Address Tracking active on current network | CONDITIONAL | Apple documents Private Relay as a network-specific feature that can be disabled for a specific Wi-Fi/mobile network using Limit IP Address Tracking. | Fresh technical verification is mandatory while the feature is active; if effective UseSafeWeb DNS cannot be proven, no protected claim is allowed. | Private Relay changes the privacy/network path and is treated as a resolver-affecting conflict boundary for UseSafeWeb claims. | Proven UseSafeWeb effective DNS -> `protected_verified`; otherwise `uncertain_error` while diagnosing or `not_covered` when the effective path is known to bypass UseSafeWeb. |
| Apple iPhone/iPad + VPN or app-specific DNS/VPN profile | CONDITIONAL | Base Apple profile is supported only where the effective resolver remains provably UseSafeWeb. | Fresh verification after activation/configuration/network change. | VPN/profile/app can supersede or conflict with the base resolver path. | Proven UseSafeWeb path -> `protected_verified`; known bypass -> `not_covered`; indeterminate -> `uncertain_error`. |
| Firefox with its own DoH provider differing from the system/UseSafeWeb route | NOT-COVERED | No separate Firefox-specific UseSafeWeb DoH endpoint is approved by TSK-0408. Mozilla documents Firefox DoH as an independent resolver choice. | None until Firefox is returned to the supported system path or a later explicit Firefox mechanism is approved/tested. | Firefox DoH can take precedence over a VPN-configured resolver and can bypass DNS filtering supplied by a network/default resolver. | `not_covered` for Firefox; return to supported resolver behavior and reverify. |
| Firefox default/disabled DoH such that it uses the supported OS path | CONDITIONAL | Supported only through the underlying approved Android/Apple/system mechanism; Firefox itself is not a separate UseSafeWeb endpoint. | Browser-scope verification where the product claims Firefox coverage. | Mozilla may alter DoH behavior based on VPN, parental-control, enterprise or network signals; do not infer from browser setting alone. | Verified system/browser path -> inherit applicable verified state; indeterminate -> `uncertain_error`. |
| Any supported device on a captive portal / sign-in network before normal connectivity is established | CONDITIONAL | No special captive-portal bypass is approved. | Reverify only after portal completion and normal connectivity are restored. | Captive-portal interception can make DNS/network tests temporarily non-representative. | During portal/indeterminate state -> `uncertain_error`; after portal completion -> rerun verification before any `protected_verified` state. |
| Wi-Fi <-> cellular switch, SIM/network change, VPN connect/disconnect, profile change, DNS setting change, browser resolver change, or other DNS-affecting transition | CONDITIONAL | Existing approved mechanism may remain configured, but prior effective-path evidence is stale for the changed scope. | Mandatory fresh verification after the material transition. | Stale success may not be carried across a changed DNS path. | While stale -> `uncertain_error` or `configured_parent_confirmed` if configuration remains known; after fresh proof -> recompute state. |
| Unsupported OS/version, unknown browser/app resolver, unclassified network middleware, or mechanism outside this matrix | NOT-COVERED or UNCERTAIN/ERROR | No support may be invented. | No `protected_verified` state until a later approved mechanism and test prove coverage. | Unknown is not success. | Known unsupported -> `not_covered`; potentially supported but evidence unavailable/error -> `uncertain_error`. |
| User intentionally removes the approved UseSafeWeb DNS mechanism | SUPPORTED removal path | Removal follows the current platform-specific removal instructions. | Removal verification must observe the current effective state; configuration disappearance alone does not prove that every possible DNS path changed. | Another UseSafeWeb mechanism may still be active, so a single deleted profile/setting is not global proof. | Verified target mechanism absent and target scope no longer protected -> `removed`; remaining independently verified mechanisms retain their own state. |

## 4. Deterministic state-transition rules

1. **Configure:** approved setting/profile successfully applied -> at most `configured_parent_confirmed`.
2. **Verify positive:** fresh technical evidence proves the effective UseSafeWeb DNS path for the claimed scope -> `protected_verified`.
3. **Verify negative, recoverable:** expected UseSafeWeb path is not effective and a defined corrective action exists -> `action_needed`.
4. **Known unsupported/bypass:** effective resolver is known to be outside the approved/tested UseSafeWeb mechanism -> `not_covered`.
5. **Indeterminate/error/stale:** verifier cannot establish current effective path, a captive portal/transient error exists, or a resolver-affecting transition invalidated prior evidence -> `uncertain_error` unless current configuration-only evidence justifies `configured_parent_confirmed` without implying protection.
6. **Removal:** only evidence-backed removal of the target mechanism/scope -> `removed`; removing an account/device record or receiving parent confirmation does not by itself prove DNS removal.
7. **Reverification:** every material resolver-affecting transition invalidates prior technical-verification freshness for the affected scope. The product recomputes from current evidence rather than carrying forward the old `protected_verified` state.
8. Evidence precedence follows TSK-0320: current qualifying technical evidence outranks configuration/parent confirmation; contradiction or stale evidence can downgrade an earlier optimistic state.

## 5. Verification contract for later implementation/device acceptance

For every combination marked SUPPORTED-L4 or CONDITIONAL, later executable tests must record at least:

- exact OS/browser/VPN/app version and test date;
- network class (Wi-Fi/mobile/other) without collecting browsing history;
- exact approved setup mechanism/config version;
- whether a resolver-affecting browser/VPN/Private-Relay/app feature is active;
- verifier ID/version and bounded result (`positive`, `negative`, `indeterminate`, `error`);
- expected and actual Protection Map state;
- recovery/removal action and post-action reverification where applicable;
- no domain/query/URL/child-activity payload in evidence.

A failed or missing device/runtime test does not get relabeled as supported. It remains explicit `NOT-COVERED` or `UNCERTAIN/ERROR` until corrected and retested.

## 6. Official current-source basis

Current official sources checked on 2026-09-01:

1. Google Android Help — **Manage advanced network settings on your Android phone**: Android exposes Off / Automatic / Private DNS provider hostname; Google states Private DNS protects DNS questions/answers only. https://support.google.com/android/answer/9654714
2. Google Chrome Help — **Manage Chrome safety and security — Android**: Chrome Secure DNS can use the current or another/custom provider and can fall back in automatic mode. https://support.google.com/chrome/answer/10468685
3. Google Android Help — **Log your Android device activity with Advanced Protection**: Google explicitly notes Chrome may use its own internal DNS resolver instead of Android's resolver and instructs switching Chrome Secure DNS off to rely on Android Private DNS for system DNS visibility. https://support.google.com/android/answer/16927813
4. Mozilla Support — **Firefox DNS over HTTPS** and protection-level documentation: Firefox can use its own DoH provider; default behavior can change in response to VPN, parental-control, enterprise or network signals. https://support.mozilla.org/en-US/kb/firefox-dns-over-https and https://support.mozilla.org/en-US/kb/dns-over-https
5. Mozilla Support — **How will DNS work when using the VPN extension?**: Firefox DoH takes priority over the resolver configured in the Mozilla VPN application. https://support.mozilla.org/en-US/kb/how-will-dns-work-when-using-vpn-extension
6. Mozilla Support — **Configure networks to disable DNS over HTTPS**: Mozilla explicitly recognizes that DoH can bypass filtering supplied by the network/default resolver. https://support.mozilla.org/en-US/kb/configuring-networks-disable-dns-over-https
7. Apple Support — **Manage iCloud Private Relay for specific websites, networks or system settings**: Apple documents network-specific Private Relay control through Limit IP Address Tracking on Wi-Fi/mobile networks. https://support.apple.com/en-gb/102022

These sources establish platform behavior and conflict boundaries. They do **not** prove the future UseSafeWeb implementation or any physical device/runtime test result.

## 7. Acceptance assertions for TSK-0409

TSK-0409 is acceptable only if all of the following remain true:

1. Every matrix row has an explicit L4 status and a verification/recovery outcome; no unknown combination is silently called protected.
2. The approved base mechanisms remain Android Private DNS/DoT hostname and Apple DoH profile/Server URL from TSK-0408; no browser-specific endpoint is invented.
3. Private Relay, VPN, Chrome Secure DNS, Firefox DoH, app-specific resolvers, captive portals and DNS-affecting network changes are all explicitly covered by conflict/bypass semantics.
4. No configuration, account, profile, ClientID, parent confirmation, or journey-completion evidence can produce `protected_verified`.
5. All six TSK-0320 protection states remain representable and technical-verification freshness is invalidated by relevant DNS-path changes.
6. No evidence/test requires DNS questions, domains, URLs, browsing history, child activity, or persistent identity linkage.
7. This definition neither changes AdGuard/Quad9/ECS policy nor claims implementation, physical-device acceptance, LG-07, build, production activation, launch, or real-user outcomes.

**TSK-0409 result:** PASS candidate pending independent deterministic verification, full modular-plan validation, GitHub read-back, and durable `CURRENT_STATE.md` reconciliation.