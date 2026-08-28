# TSK-0511 — Android Mapping and Remaining iPhone Verification Evidence

**Task:** TSK-0511 — Verify encrypted DNS resolution from supported devices  
**Acceptance:** ACC-0511  
**Date:** 2026-08-28

## New owner evidence

After TSK-0511 preflight established that the previously tested supported real phone had not yet been identified as iPhone/iOS or Android/Private DNS, the Project Owner explicitly identified that already-tested phone as **Android**.

This owner statement binds the already accepted TSK-0442 and TSK-0514 direct target-device observations to the supported **Android 9+ / native Private DNS / DNS-over-TLS** family defined by TSK-0439.

The already accepted observations therefore provide the following Android-family direct evidence without requiring a duplicate retest solely for platform relabelling:

- the supported Android phone successfully operated through the configured UseSafeWeb encrypted-DNS path;
- the qualifying external cellular test passed with no network-specific failure reported;
- after UseSafeWeb was removed/reset, normal DNS/internet resolution returned.

The production side separately remains proven for the Android DoT endpoint `dns.usesafeweb.com:853` and certificate hostname/listener controls under TSK-0442.

## Remaining supported-family gap

Accepted TSK-0439 scope contains one other supported family: **iPhone/iOS 14+ using a manually installed Apple DNS Settings profile with DNS-over-HTTPS** at:

`https://dns.usesafeweb.com/dns-query`

No durable direct iPhone target-device observation currently proves ACC-0511 for that family. TSK-0511 therefore remains WAITING and is not PASS.

## Prepared iPhone test artifact

A minimal owner-test profile is now versioned at:

`infrastructure/adguard-server/client-profiles/UseSafeWeb-iPhone-DoH.mobileconfig`

Profile blob: `0613cf685b03febd605d2b1d5fd22dff5e396a2a`  
Publication commit: `2697ac13595574025686982675dc28236fe68d68`

The profile contains only the UseSafeWeb encrypted-DNS payload and common profile metadata. Its DNS payload is:

- `PayloadType = com.apple.dnsSettings.managed`
- `DNSProtocol = HTTPS`
- `ServerURL = https://dns.usesafeweb.com/dns-query`
- no client identifier, token, browsing data, match-domain restriction, identity certificate, or fallback-to-plaintext control.

Apple's current Device Management documentation identifies `com.apple.dnsSettings.managed` as the DNS Settings payload type, requires `DNSProtocol`, requires an HTTPS `ServerURL` when the protocol is HTTPS, and states that a manually installed DNS Settings profile applies to cellular networks as well as other networks. Current Apple profile documentation also requires the standard profile envelope (`PayloadType=Configuration`, unique `PayloadIdentifier`/`PayloadUUID`, `PayloadVersion=1`).

Current authoritative Apple references checked 2026-08-28:

- https://developer.apple.com/documentation/devicemanagement/dnssettings
- https://developer.apple.com/documentation/devicemanagement/dnssettings/dnssettings-data.dictionary
- https://developer.apple.com/documentation/devicemanagement/commonpayloadkeys
- https://support.apple.com/en-gb/102400
- https://support.apple.com/en-gb/guide/personal-safety/ips327569a75/1.0/web/1.0

A local standards-library plist parse also accepted the exact profile as a valid property list and confirmed the expected encrypted-DNS keys. This syntax check is supporting preparation evidence only; it does not replace a real iPhone installation/result.

## Deterministic resumption condition

On one representative iPhone running iOS 14 or later:

1. transfer/download the prepared `.mobileconfig` profile to the iPhone;
2. install it through Settings and confirm the UseSafeWeb profile appears under **Settings > General > VPN & Device Management**;
3. with the profile active, confirm normal allowed DNS/internet resolution works on the device;
4. if installation or effective routing fails/appears ambiguous, record only the privacy-safe failure class and treat the state as Action needed/unsupported rather than verified;
5. remove the UseSafeWeb profile and confirm normal DNS/internet resolution returns.

No browsing history, DNS/domain history, screenshot, device identifier, participant identity, or raw query data is required.

When these direct iPhone observations are supplied, evaluate ACC-0511 and recompute the governed L2 queue. TSK-0431 remains a separate WAITING boundary.
