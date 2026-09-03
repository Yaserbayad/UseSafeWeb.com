# TSK-0417 — Vendor removal/revocation source research — 2026-09-03

## Disposition

Source/vendor research only. `TSK-0417` is not PASS and no live-device, service-revocation, profile-removal, certificate-removal, deployment, participant, telemetry, activation, market, launch, `TSK-0374 PASS`, or `TSK-0499 PASS` action is authorized or inferred.

## Canonical implementation surface

Current source identifies the concrete profile platform as Apple iPhone/iOS:

- `website/src/lib/ios-doh-profile.ts`, current `main` blob `9a342cce55a7a0c4769e61861e9d81d5837f3141`.
  - payload type `com.apple.dnsSettings.managed`;
  - DoH server URL `https://dns.usesafeweb.com/dns-query`;
  - profile identifier `com.usesafeweb.profile.doh`;
  - DNS payload identifier `com.usesafeweb.profile.doh.dns`;
  - no `PayloadCertificateUUID`, ClientID, authorization token, identity certificate, or other per-device service credential.
- `website/src/app/api/ios-doh-profile/route.ts`, current `main` blob `53b67ea8bbc03f29dc732591150a25ae748a7071`.
  - delivery is disabled unless explicitly enabled;
  - server-owned UUID metadata and exact SHA-256 binding are required;
  - route contains no per-device revocation handle or credential.
- `website/tests/contract/tsk0360.test.mjs` is the existing profile-generation/delivery contract suite.
- `website/src/lib/core-state-machine.ts`, current `main` blob `8bebd5f429cdaf03c416c9c64e93fc7ed804ee6a`, currently permits `recover:REMOVE_CONFIGURATION -> removed` directly.
- `website/src/app/[locale]/recover/page.tsx`, current `main` blob `259bdc82727af6371dd260ad311361bb4e48eb5d`, currently emits `REMOVE_CONFIGURATION` directly after presenting the versioned removal instruction.
- `website/src/content/instruction-bindings.json`, current `main` blob `32441b56f5b2daf2c9924584685fd35fb416438e`, states that iPhone profile removal removes profile-owned DNS configuration but does not delete a SafeWeb account/device record or anonymous web state.

The current source therefore has a concrete Apple profile-cleanup surface but no concrete service-side revocation API or credential to call. TSK-0417 source work must not invent such an external interface.

## Current official Apple documentation verified 2026-09-03

1. Apple Developer — DNSSettings
   https://developer.apple.com/documentation/devicemanagement/dnssettings
   - `com.apple.dnsSettings.managed` is the encrypted-DNS profile payload.
   - Apple currently documents manual install support on iOS.
   - Apple marks this payload deprecated for iOS 27+ and points to the declarative `com.apple.configuration.network.dns-settings` configuration. Deprecation is not treated here as removal of current source support.

2. Apple Developer — DNSSettings.DNSSettings
   https://developer.apple.com/documentation/devicemanagement/dnssettings/dnssettings-data.dictionary
   - `DNSProtocol` supports HTTPS/TLS.
   - `PayloadCertificateUUID` is optional and would reference an identity certificate if used.
   - Current SafeWeb source does not use that property, so there is no certificate cleanup surface in the present profile artifact.

3. Apple Support — Install or remove configuration profiles on iPhone
   https://support.apple.com/guide/iphone/iph6c493b19/ios
   - Installed profiles are visible in Settings > General > VPN & Device Management.
   - Deleting a profile also deletes the settings, apps, and data associated with that profile.

4. Apple Support — Review and delete configuration profiles
   https://support.apple.com/guide/personal-safety/review-and-delete-configuration-profiles-ips327569a75/1.0/web/1.0
   - Removing an iPhone/iPad profile removes the profile's settings and information.
   - Apple directs the user to Settings > General > VPN & Device Management, select the profile, Delete Profile, and then restart the device.

## TSK-0417 source implication

Apple owns the device/profile-removal mechanism. The UseSafeWeb acceptance contract separately requires service removal/revocation to be proven before profile/certificate cleanup. Because current source exposes no service-side revocation API/credential, the safe source checkpoint is a sequencing/evidence guard in the existing core state machine: direct profile cleanup from recovery must be rejected; only explicit qualifying `REVOKED` evidence may advance to a profile-cleanup phase. This records ordering without fabricating how a future target executor obtains revocation evidence.

The isolated RED contract is `website/tests/contract/tsk0417.test.mjs`. It is intentionally expected to fail against the current direct-removal behavior before the minimal source change is applied.
