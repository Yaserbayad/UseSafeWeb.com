# TSK-0408 — UseSafeWeb DNS Identity and Platform Endpoint/Profile Contract

**Task:** TSK-0408 — Define one coherent UseSafeWeb DNS identity and approved platform-specific endpoint/profile mechanisms  
**Acceptance:** ACC-0408  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL L4 DESIGN CONTRACT / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** DEC-0003 AdGuard backend + DEC-0004 encrypted DNS + DEC-0042 accountless-first + DEC-0050/CR-0003 provisional L4 authorization  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.  

## Provisional evidence limitation — RSK-0002 remains OPEN

Real-participant L3 behavioral validation is deferred through 2027-08-27 or earlier explicit owner reactivation. This contract therefore defines a technically coherent provisional platform mechanism from accepted technical evidence and current official platform documentation; it does **not** prove parent comprehension, completion, support burden, persistence, or preference. `RSK-0002` remains OPEN. No synthetic/technical result in this artifact is behavioral-validation evidence, and this artifact does not authorize LG-05/LG-06, implementation/build, public release or launch.

## 1. One product identity, protocol-specific connection forms

UseSafeWeb has one human-facing DNS service identity:

- **Service name:** `UseSafeWeb DNS`
- **Canonical resolver hostname:** `dns.usesafeweb.com`
- **Current accepted DoH endpoint:** `https://dns.usesafeweb.com/dns-query`
- **Current accepted Android native Private DNS / DoT endpoint identity:** hostname `dns.usesafeweb.com`; current service port `853`
- **TLS server identity:** certificate must be valid for `dns.usesafeweb.com` on every supported encrypted transport.

The hostname is a shared service identity, **not a universal setup string**. The correct user input depends on the platform/protocol:

| Platform/mechanism | User/configuration value | Protocol | Do not instruct |
| --- | --- | --- | --- |
| Android native Private DNS provider | `dns.usesafeweb.com` | DNS-over-TLS (DoT) | Do not paste the HTTPS URL or `/dns-query` path into Android Private DNS. |
| iPhone/iPad native DNS configuration profile | Server URL `https://dns.usesafeweb.com/dns-query`; profile uses Apple DNS Settings payload | DNS-over-HTTPS (DoH) | Do not present hostname-only Android instructions as the iOS DoH workflow. |
| Any later explicitly supported DoH-capable client | Full HTTPS endpoint, normally `https://dns.usesafeweb.com/dns-query` | DoH | Do not assume a client accepts a hostname where it requires a URL, or vice versa. |

This protocol-specific separation is mandatory. A future platform cannot be called supported merely because it can resolve the FQDN.

## 2. Current official platform basis

### Android

Google Android Help currently exposes `Private DNS provider hostname` as a native setting and warns that Private DNS secures DNS questions/answers only. Android developer documentation defines the specified-host Private DNS mode as a hostname for a server implementing DNS-over-TLS (RFC 7858), and strict-mode APIs require encrypted queries to that hostname with a valid certificate.

UseSafeWeb therefore treats Android native Private DNS as **DoT by hostname**, not DoH by URL.

### Apple

Apple's DNS Settings payload supports encrypted `HTTPS` and `TLS` protocols. For HTTPS, Apple documents a Server URL beginning with `https://`; Apple identifies the DNS Settings payload as `com.apple.dnsSettings.managed`. Apple also documents that installed configuration profiles can be removed from Settings > General > VPN & Device Management, and removing a profile removes its associated settings.

AdGuard's current Knowledge Base states that Android 9+ supports native DNS-over-TLS by domain name and iOS 14+ supports native DNS-over-TLS and DNS-over-HTTPS via configuration profiles. This is consistent with the current UseSafeWeb accepted Android DoT and iPhone DoH evidence.

## 3. Apple profile identity and naming

For the current UseSafeWeb iPhone/iPad DoH path:

- **Display name:** `UseSafeWeb DNS`
- **Purpose text:** encrypted DNS baseline for the UseSafeWeb first-phone setup; DNS-level protection only; not complete device safety.
- **Protocol:** HTTPS / DoH.
- **Server URL:** `https://dns.usesafeweb.com/dns-query`.
- **Resolver hostname/certificate identity:** `dns.usesafeweb.com`.
- **Payload type:** Apple DNS Settings payload (`com.apple.dnsSettings.managed`) where the profile format requires it.
- **Profile identifier namespace:** production/pilot-facing profile identifiers must be under an explicit UseSafeWeb namespace such as `com.usesafeweb.dns.production`; non-production profiles must use a different environment-qualified identifier.
- **Profile UUID/version:** generated/versioned per profile release; a later update must not silently reuse metadata in a way that obscures which resolver/environment is installed.

The exact generated `.mobileconfig` artifact and signing/distribution method are later implementation/release work; this L4 task does not create or authorize a production profile package.

## 4. Android native Private DNS identity and naming

For the current supported Android native path:

- **User-visible setting:** Android `Private DNS provider hostname`.
- **Value:** `dns.usesafeweb.com`.
- **Transport:** DNS-over-TLS.
- **Current service port:** 853; the Android user instruction remains hostname-only rather than exposing `:853` as a normal input string.
- **Certificate rule:** the TLS connection must authenticate the specified hostname; certificate failure or inability to establish the specified-host private DNS path is not a verified protection state.
- **No UseSafeWeb app/VPN requirement:** the current native baseline does not require installing a UseSafeWeb Android app or creating a persistent account.

## 5. Certificate contract

A supported encrypted endpoint is acceptable only when:

1. the certificate chain is trusted by the target platform;
2. the certificate is valid for `dns.usesafeweb.com`;
3. the certificate is within its validity period;
4. the endpoint serves the intended protocol on the intended transport;
5. renewal/expiry monitoring and recovery remain active before any public operation;
6. non-production endpoints do not silently borrow a production identity/certificate in a way that makes environment evidence ambiguous.

Current runtime evidence already records accepted certificate installation and renewal/expiry/recovery evidence for `dns.usesafeweb.com`; TSK-0408 consumes that evidence but does not replace its acceptance tests.

## 6. Verification-state contract

The product must not equate configuration instructions, parent confirmation, DNS resolution, or an installed profile with universal proof of protection.

Use these states:

- **not_started** — no UseSafeWeb encrypted-DNS configuration asserted.
- **configured_unverified** — the platform configuration appears installed/entered, but no current trustworthy technical verification has completed.
- **verified** — the supported platform path has current evidence that the intended encrypted endpoint is active and the approved synthetic allow/block checks behave as expected, without retaining browsing/query history.
- **failed** — current verification demonstrates the approved path is not functioning.
- **uncertain** — the product cannot safely distinguish active protection from a conflict/bypass/unsupported state.
- **removed** — the UseSafeWeb DNS configuration was removed/reset and normal platform/network DNS behavior is restored.

Verification rules:

1. use synthetic/controlled DNS tests rather than real browsing history;
2. do not persist queried domains, per-user DNS history or a persistent device identity merely to prove protection;
3. keep parent confirmation distinct from system verification;
4. if a browser/VPN/app/network path can bypass or override system DNS and cannot be confidently detected, do not show `verified` for that path; use `uncertain`/Not covered as appropriate;
5. detailed compatibility/bypass handling belongs to the separately governed supported-combination task (TSK-0409), not to a fabricated universal verifier here.

## 7. Removal and recovery

### Android

To remove the custom UseSafeWeb provider, return Android Private DNS from `Private DNS provider hostname` to the device's normal policy, normally `Automatic`; `Off` is a separate user choice and is not the default UseSafeWeb recovery recommendation. After removal, UseSafeWeb must show the DNS layer as `removed`/not protected until reconfigured and verified.

Google's current Android Help documents the three user choices as Off, Automatic, and Private DNS provider hostname.

### iPhone/iPad

A manually installed UseSafeWeb DNS configuration profile must remain user-removable. Apple's current user guidance exposes profiles under Settings > General > VPN & Device Management; removing a profile removes its associated settings. UseSafeWeb instructions must identify the exact UseSafeWeb profile and explain that removing it removes the UseSafeWeb DNS configuration. A restart may be included as troubleshooting when required by the platform guidance/current tested procedure, but it is not a substitute for profile deletion.

### Recovery outcome

Current project evidence already records that external cellular encrypted DNS worked and that normal DNS/internet resolution returned after removing/resetting UseSafeWeb. This design preserves that reversible behavior as a required future regression check.

## 8. Fallback and failure policy

UseSafeWeb must not silently treat an unintended resolver path as protected.

- There is **no client-side universal fallback string** shared between Android DoT and Apple DoH.
- If the intended encrypted path cannot be verified, the user-facing state is `failed` or `uncertain`, not `verified`.
- If the custom configuration causes loss of resolution or a material conflict, the safe recovery path is to remove/reset the UseSafeWeb DNS configuration and restore the platform/network's normal DNS behavior; that recovery ends the UseSafeWeb DNS protection claim.
- Any server-side upstream fallback is a separate resolver/operations decision and must not be invented in this client identity contract. The current canonical upstream remains the approved Quad9 dns10 DoH baseline unless separately changed under authority.
- Captive portal, VPN, browser/app secure-DNS and other bypass/conflict cases are not silently declared solved; they must be explicitly supported or marked unsupported/uncertain under TSK-0409.

## 9. Environment separation

The currently proven controlled pilot endpoint is `dns.usesafeweb.com`. It is not evidence that public production launch is authorized.

Environment rules:

1. `dns.usesafeweb.com` is the canonical pilot/production-facing namespace reserved for the accepted service identity.
2. Test/staging environments must **not** reuse the production/pilot endpoint as if evidence were interchangeable.
3. Any non-production resolver must use an environment-qualified hostname, for example the pattern `dns-<environment>.usesafeweb.com`, plus an environment-qualified Apple profile display/identifier; the exact hostname becomes authoritative only when that environment is actually provisioned and accepted.
4. Test/staging certificates, DNS records, profiles, monitoring and evidence must identify their environment explicitly.
5. Synthetic/non-participant test data only is allowed in non-production under the current CR-0003 boundary.
6. Public instructions must never point users at a non-production endpoint.
7. Promotion of `dns.usesafeweb.com` from controlled pilot use to public production requires the later production/launch gates and fresh endpoint/certificate/compatibility evidence; TSK-0408 does not perform that promotion.

## 10. Naming and instruction invariants

A later implementation/content catalogue must be testable against these invariants:

1. Android native instructions contain `dns.usesafeweb.com`, not the DoH URL.
2. iOS/iPadOS DoH profile uses the full `https://dns.usesafeweb.com/dns-query` Server URL.
3. `dns.usesafeweb.com` certificate identity is valid on each supported encrypted transport.
4. No supported-platform instruction assumes that a hostname, URL, port, profile or FQDN entry mechanism is interchangeable across platforms.
5. Profile/display names identify `UseSafeWeb DNS` and the environment where non-production is involved.
6. `verified` is never derived solely from parent confirmation or profile presence.
7. Removal returns the platform to normal DNS behavior and clears the UseSafeWeb DNS protection claim.
8. A failure/bypass/conflict that cannot be proven safe is `failed`, `uncertain` or unsupported — never silently `verified`.
9. Non-production endpoint/profile/certificate evidence cannot satisfy a production acceptance criterion.
10. No verification mechanism introduces browsing/query history or persistent child/device identity.

## 11. Current source/evidence index

### Canonical UseSafeWeb evidence

- `CURRENT_STATE.md`: current technical identity and accepted task evidence.
- `TSK-0439` accepted pilot device DNS methods — evidence blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0440` accepted encrypted-DNS hostname/path — evidence blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.
- `TSK-0442` TLS certificate acceptance — evidence blob `cb11394af1e80f15d85bda5d9b000bbf0efd6d20`.
- `TSK-0443` certificate renewal/expiry/recovery acceptance — evidence blob `c2f3b3b35c9d8e2ec33f473d72c508ebde30348d`.
- `TSK-0511` supported-device encrypted DNS verification — evidence blob `ecd959f93ab7dff62aba6529ce66b45d59c3ed27`.
- `TSK-0514` external endpoint/removal-recovery completion — evidence blob `c5d004d0e0a8c58d1056b3aaad38034ae4188a68`.
- `TSK-0207` privacy persistence acceptance — evidence blob `1c16db063e2e84d300b547075721d33c2e020e32`.
- `TSK-0407` Quad9 dns10/ECS acceptance — evidence blob `7afeca58e9205234a230d2de702b99648b35347d`.

### Current official platform/product sources checked 2026-08-28

- Google Android Help — Manage advanced network settings / Private DNS: https://support.google.com/android/answer/9654714?hl=en
- Android Developers — DevicePolicyManager Private DNS specified-host mode / RFC 7858: https://developer.android.com/reference/android/app/admin/DevicePolicyManager
- Android Developers — LinkProperties strict-mode/certificate semantics: https://developer.android.com/reference/android/net/LinkProperties
- Apple Platform Deployment — DNS Settings payload: https://support.apple.com/en-gb/guide/deployment/dep86469ba99/1/web/1.0
- Apple Support — Install or remove configuration profiles on iPhone: https://support.apple.com/en-euro/guide/iphone/iph6c493b19/ios
- AdGuard DNS Knowledge Base — AdGuard Home DNS encryption/device configuration: https://adguard-dns.io/kb/adguard-home/encryption/

## 12. ACC-0408 result

ACC-0408 requires hostname/DoH path/profile naming, certificates, verification, removal, fallback, and environment separation to be clear without a false universal FQDN workflow.

This contract supplies all of those elements and explicitly separates Android hostname/DoT from Apple profile/DoH, preserves the accepted `dns.usesafeweb.com` identity, defines certificate and verification truth rules, makes removal/recovery reversible, refuses silent false fallback, separates non-production evidence, and preserves current privacy and CR-0003 boundaries.

**TSK-0408 result: PASS candidate subject to independent verification and runtime read-back.**
