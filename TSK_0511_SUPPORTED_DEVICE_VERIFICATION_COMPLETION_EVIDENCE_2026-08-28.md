# TSK-0511 — Supported Device Verification Completion Evidence

**Task:** TSK-0511 — Verify encrypted DNS resolution from supported devices  
**Acceptance:** ACC-0511  
**Date:** 2026-08-28

## Accepted supported-device scope

Accepted TSK-0439 evidence defines exactly two Experiment-1 supported phone families:

1. **Android 9+** with usable native Private DNS provider-hostname control, using DNS-over-TLS to `dns.usesafeweb.com:853`.
2. **iPhone / iOS 14+** using the approved Apple DNS Settings profile, using DNS-over-HTTPS to `https://dns.usesafeweb.com/dns-query`.

ACC-0511 requires each supported device family to resolve allowed domains over the intended encrypted endpoint and requires failure/removal behavior to be verified.

## Android family — accepted direct evidence

On 2026-08-28 the Project Owner explicitly identified the previously tested supported real phone as **Android**. This binds the already accepted TSK-0442 and TSK-0514 owner observations to the Android / native Private DNS / DoT family without requiring a duplicate retest solely for relabelling.

Accepted Android observations:

- the supported Android phone operated successfully through the configured UseSafeWeb encrypted-DNS path;
- the qualifying external cellular test passed with no network-specific failure reported;
- after UseSafeWeb was removed/reset, normal DNS/internet resolution returned.

The production endpoint/listener/certificate side for `dns.usesafeweb.com:853` remains separately proven by accepted TSK-0442 server evidence.

## iPhone family — new direct evidence

A minimal iPhone DoH test profile was versioned at:

`infrastructure/adguard-server/client-profiles/UseSafeWeb-iPhone-DoH.mobileconfig`

Profile blob: `0613cf685b03febd605d2b1d5fd22dff5e396a2a`  
Publication commit: `2697ac13595574025686982675dc28236fe68d68`

The profile configures Apple DNS Settings with:

- `PayloadType = com.apple.dnsSettings.managed`
- `DNSProtocol = HTTPS`
- `ServerURL = https://dns.usesafeweb.com/dns-query`

On 2026-08-28, after being given the governed iPhone test procedure for one representative iPhone running iOS 14 or later, the Project Owner reported exactly:

> iPhone Wi-Fi passed, cellular passed, removal passed.

This is accepted as privacy-minimal direct target-device evidence that, with the approved UseSafeWeb DoH profile active, normal allowed DNS/internet resolution worked on both Wi-Fi and cellular, and that after the UseSafeWeb profile was removed normal DNS/internet resolution returned.

No installation failure, routing ambiguity, or network-specific failure was reported. Therefore the fail-safe branch was not triggered in this successful test; the governed procedure remains explicit that ambiguous/ineffective routing must be classified Action needed/unsupported rather than falsely verified.

## Privacy boundary

No browsing history, DNS/domain history, raw query data, screenshot, device identifier, participant identity, or child-linked data is required or retained for this evidence.

## Acceptance evaluation

- Android supported family: direct encrypted-DNS operation evidence — **PASS**.
- Android removal/recovery — **PASS**.
- iPhone supported family using the approved DoH profile: Wi-Fi resolution — **PASS**.
- iPhone supported family using the approved DoH profile: cellular resolution — **PASS**.
- iPhone removal/recovery — **PASS**.
- No reported network-specific failure or unresolved routing ambiguity remains for the two supported Experiment-1 phone families.

The direct target-device evidence gap identified in `TSK_0511_SUPPORTED_DEVICE_VERIFICATION_PREFLIGHT_2026-08-28.md` and `TSK_0511_ANDROID_MAPPING_IPHONE_REMAINING_EVIDENCE_2026-08-28.md` is resolved.

**Stable outcome: TSK-0511 = PASS.**

This task PASS proves the bounded supported-device encrypted-DNS verification contract only. It does not by itself authorize real-participant activation, launch, legal-gate bypass, or any broader supported-device claim.