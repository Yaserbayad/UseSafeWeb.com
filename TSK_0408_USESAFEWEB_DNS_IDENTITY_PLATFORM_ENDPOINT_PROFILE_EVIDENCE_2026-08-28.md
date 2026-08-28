# TSK-0408 — UseSafeWeb DNS identity/platform mechanism verification evidence

**Task:** TSK-0408 — Define one coherent UseSafeWeb DNS identity and approved platform-specific endpoint/profile mechanisms  
**Acceptance:** ACC-0408  
**Verification:** VER-0408 independent guarded technical/source audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back  

## Exact evidence index

- Contract: `TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md`
- Corrected contract blob: `52860ce167fc8a31962cd412772e428d280c8184`
- Corrected contract commit: `73fd41fabf81f282af00dfc6974ed55a3f77bd92`
- Runtime blob before TSK-0408 reconciliation: `b9b2ca4d20ba2be8627f27b5f05c4cb37b069094`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Decision/trigger register blob: `577732f6fc5168b392224063a312c28f5495a3bd`
- Risk register blob: `d15165b0e06f559fc7281fab12873d0cb32144d9`
- Verification/evidence register blob: `7a2b4fbc4cd533a638ae47df84cf0761accfa251`
- Current hard dependency: `TSK-0146 = PASS` in authoritative runtime.

## Current canonical technical facts consumed

The current runtime records the accepted controlled-pilot identity and evidence:

- resolver hostname `dns.usesafeweb.com`;
- DoH endpoint `https://dns.usesafeweb.com/dns-query`;
- Android native pilot transport DoT to `dns.usesafeweb.com:853`;
- `TSK-0439` supported pilot-device DNS methods PASS;
- `TSK-0440` hostname/path PASS;
- `TSK-0442` certificate PASS;
- `TSK-0443` renewal/expiry/recovery PASS;
- `TSK-0511` supported Android/iPhone encrypted-DNS verification PASS;
- `TSK-0514` external endpoint plus removal/recovery PASS;
- `TSK-0207` privacy persistence PASS;
- `TSK-0407` exact Quad9 dns10/ECS-off upstream PASS.

This audit consumes those accepted facts; it does not re-label them as public-production evidence.

## Current authoritative external-source verification

Sources were checked on 2026-08-28.

### Google Android Help

Source: `https://support.google.com/android/answer/9654714?hl=en`

Observed current guidance:

- Private DNS options are `Off`, `Automatic`, and `Private DNS provider hostname`.
- Google states that Private DNS secures DNS questions/answers only, not all device traffic/safety.

Disposition: supports hostname-only Android user input and the contract's DNS-only protection limitation.

### Android Developers — DevicePolicyManager

Source: `https://developer.android.com/reference/android/app/admin/DevicePolicyManager`

Observed current API contract for `setGlobalPrivateDnsModeSpecifiedHost`:

- `privateDnsHost` is the hostname of a server implementing DNS-over-TLS (RFC 7858);
- Android performs a resolver connectivity/validity check and can return host-not-serving when the hostname does not implement DoT;
- VPN coexistence can create reachability constraints.

Disposition: directly disproves a universal instruction that would paste the UseSafeWeb DoH URL into Android native Private DNS. Android's native specified-host mechanism is DoT by hostname.

### Android Developers — LinkProperties

Source: `https://developer.android.com/reference/android/net/LinkProperties`

Observed current API contract:

- a non-null `getPrivateDnsServerName()` indicates strict Private DNS mode;
- DNS queries should be encrypted to that hostname;
- queries should only be sent if the hostname's certificate is valid.

Disposition: supports the contract's hostname/certificate identity rule and its refusal to show verified state on certificate/strict-mode failure.

### Apple Platform Deployment — DNS Settings payload

Source: `https://support.apple.com/en-gb/guide/deployment/dep86469ba99/1/web/1.0`

Observed current payload semantics:

- supported payload identifier is `com.apple.dnsSettings.managed`;
- encrypted Protocol options are `HTTPS` or `TLS`;
- HTTPS uses a Server URL beginning with `https://` and the Apple table states this URL is required when Protocol is HTTPS.

Important limitation: the cited Apple page is a device-management payload reference and lists device-enrollment deployment channels. It is authoritative for the DNS payload field/protocol semantics, but by itself is not proof of the exact manual consumer-profile distribution workflow. The current project has separate accepted iPhone profile/device evidence, and the exact generated `.mobileconfig`/distribution method remains later implementation/release evidence.

Disposition: supports the contract's iOS DoH Server URL semantics while preserving the manual-profile implementation caveat.

### Apple Support — configuration profile removal

Source: `https://support.apple.com/en-gb/guide/personal-safety/ips327569a75/1.0/web/1.0`

Observed current user guidance:

- installed profiles are found under Settings > General > VPN & Device Management;
- deleting a profile removes its settings/information;
- Apple includes restart after deletion in the cited safety workflow.

Disposition: supports the reversible profile-removal contract. Restart remains troubleshooting/current-platform procedure, not a substitute for profile deletion.

### AdGuard DNS Knowledge Base — AdGuard Home encryption

Source: `https://adguard-dns.io/kb/adguard-home/encryption/`

Observed current product guidance:

- Android 9+ supports native DNS-over-TLS by entering a domain name in Private DNS;
- iOS 14+ supports native DoT/DoH through configuration profiles and AdGuard Home can generate those profiles.

Disposition: corroborates the platform split already proven in the current UseSafeWeb controlled-pilot evidence.

## ACC-0408 audit

ACC-0408 requires: `Hostname/DoH path/profile naming, certificates, verification, removal, fallback, and environment separation are clear; no false universal FQDN workflow.`

### Hostname and DoH path — PASS

The contract fixes one service identity `dns.usesafeweb.com` while explicitly separating:

- Android native Private DNS: hostname `dns.usesafeweb.com`, DoT;
- iPhone/iPad DoH profile: full Server URL `https://dns.usesafeweb.com/dns-query`.

It explicitly prohibits treating hostname, HTTPS URL/path, port and profile mechanism as interchangeable.

### Profile naming — PASS

The corrected contract separates controlled-pilot, test/staging and future-production profile metadata. A newly generated pilot profile uses pilot-qualified metadata; `com.usesafeweb.dns.production` is reserved for a later production profile and cannot prove production/public authorization. The contract does not retroactively rewrite accepted historical test-profile evidence.

### Certificates — PASS

The contract requires a trusted in-date certificate for `dns.usesafeweb.com` on every supported encrypted transport, preserves existing certificate/renewal evidence, and forbids non-production certificate evidence from silently satisfying production acceptance.

### Verification truth — PASS

The contract defines `not_started`, `configured_unverified`, `verified`, `failed`, `uncertain`, and `removed`, with parent confirmation/profile presence kept distinct from technical verification. Synthetic controlled DNS checks are required; browsing/query history and persistent device identity are prohibited as verification evidence.

### Removal/recovery — PASS

Android returns from the custom provider to normal platform policy, normally `Automatic`, and iPhone/iPad removes the UseSafeWeb profile through the platform profile-management path. In both cases the UseSafeWeb DNS protection claim ends until reconfigured and reverified. This is consistent with accepted TSK-0514 recovery evidence.

### Fallback/failure — PASS

The contract explicitly refuses a universal Android/iOS fallback string, refuses silent protected state on an unintended resolver, separates any server-side upstream fallback from this client-identity task, and assigns bypass/conflict expansion to TSK-0409 rather than fabricating coverage here.

### Environment separation — PASS

The contract distinguishes the currently accepted controlled-pilot endpoint from public production authorization, requires environment-qualified test/staging resolver/profile metadata, reserves future production profile metadata for later gates, and prevents non-production evidence from satisfying production acceptance.

### No false universal FQDN workflow — PASS

Current Android and Apple evidence actively contradicts a universal setup mechanism: Android's native field consumes a DoT provider hostname, while Apple HTTPS DNS payload semantics consume an HTTPS Server URL. The contract states this difference as a testable invariant.

## Adversarial findings and unresolved uncertainty

1. **Behavioral evidence remains absent.** `RSK-0002` remains OPEN under DEC-0050/CR-0003. This technical contract does not prove parents understand or successfully complete the flows.
2. **Android UI paths vary.** Google explicitly notes settings can vary by device/manufacturer/version. The contract therefore freezes the semantic setting/value, not one universal navigation path.
3. **Apple manual-profile implementation still needs artifact-level verification.** Apple's authoritative payload reference checked here is device-management-oriented. The project has accepted iPhone profile evidence and AdGuard corroboration, but any generated release `.mobileconfig`, signing/distribution mechanism, payload scope and current OS behavior must be tested directly before release.
4. **Bypass/conflict behavior remains separate.** VPN, app/browser secure DNS, captive portals and network-specific conflicts are not declared solved; TSK-0409 owns the supported-combination/bypass matrix.
5. **Non-production examples are naming rules, not deployed facts.** No `dns-<environment>.usesafeweb.com` endpoint is claimed to exist until separately provisioned and verified.
6. **Public production remains unauthorized.** The accepted controlled-pilot identity and this L4 design do not satisfy production or launch gates.

No contrary current source or canonical evidence was found requiring reversal of the Android DoT-hostname / Apple DoH-profile split or the accepted `dns.usesafeweb.com` service identity.

## Stable verification decision

All clauses of ACC-0408 are directly covered by the corrected durable contract and are consistent with current accepted UseSafeWeb technical evidence and current authoritative platform documentation. The environment-profile ambiguity identified during review was corrected before this decision.

**Stable outcome: TSK-0408 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

Do not assume the next task from the pre-TSK-0408 queue. Runtime reconciliation must add TSK-0408 to the stable PASS set, derive the dependency-ready L4 queue again, exclude HUMAN_ONLY/HUMAN_APPROVAL_REQUIRED and real-user-evidence-bound tasks, then select by current project priority and WBS order.
