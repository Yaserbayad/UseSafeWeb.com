# TSK-0511 — Supported Device Encrypted-DNS Verification Preflight

**Task:** TSK-0511 — Verify encrypted DNS resolution from supported devices  
**Verification:** VER-0511  
**Evidence:** EVD-0511  
**Acceptance:** ACC-0511  
**Date:** 2026-08-28  
**Runtime authority:** `CURRENT_STATE.md` after TSK-0514 PASS reconciliation

## Authoritative task contract

Current deterministic queue evaluation identifies TSK-0511 as the sole L2 `AUTO_ALLOWED` candidate after TSK-0514 becomes PASS. Its hard predecessors are `TSK-0514; TSK-0202; TSK-0011`, all satisfied in current authority.

ACC-0511 requires: **Each supported device resolves allowed domains over the intended encrypted endpoint; failure modes and removal steps are verified.**

VER-0511 requires the approved checklist/test procedure against the exact artifact/environment with reproducible outputs and reviewer result. EVD-0511 requires artifact/version, exact environment/source, test/review output, date, responsible verifier, and deviations/disposition.

Relevant current requirements include REQ-0065 and REQ-0066. The broader product requirement REQ-0048 also requires DNS setup, verification, removal, bypass/compatibility limitations and recovery to be tested on supported devices/networks.

## Supported-device scope

Accepted TSK-0439 evidence defines exactly two supported Experiment-1 phone configuration families:

1. **iPhone — iOS 14 or later**, using an Apple DNS Settings configuration profile with DoH at `https://dns.usesafeweb.com/dns-query`.
2. **Android — Android 9 or later with a usable native Private DNS provider-hostname control**, using DoT to `dns.usesafeweb.com:853`.

Variants outside those capability boundaries are unsupported unless separately validated.

## Current direct evidence

Current accepted evidence already proves:

- the production certificate/hostname/listener side is valid on both encrypted service ports and weak TLS is rejected (TSK-0442);
- the service supports the frozen iPhone DoH and Android DoT endpoint identities (TSK-0439/TSK-0442);
- one supported real phone successfully operated through UseSafeWeb (TSK-0442 owner observation);
- one qualifying external cellular test passed and normal DNS/internet resolution returned after UseSafeWeb was removed/reset (TSK-0514 owner observation);
- no network-specific failure was reported for that external cellular test.

However, the durable owner observations identify the device only as a **supported real phone**. They do not identify whether it was the iPhone/iOS family or the Android/Private-DNS family. Therefore the existing evidence cannot truthfully be mapped to either family, and it cannot prove ACC-0511's **each supported device** condition for both families.

No inference from likely platform, menu path, transport, or prior conversation is accepted as evidence.

## Stable preflight outcome

**TSK-0511 is not PASS.**

The task is **WAITING on the minimum direct target-device evidence needed to cover both supported families**. This is a target-device evidence boundary, not a server/configuration blocker.

Deterministic resumption condition:

1. Identify the family of the already-tested phone as either **iPhone/iOS** or **Android/Private DNS**. This may reuse the already accepted TSK-0442/TSK-0514 observations for that family; no duplicate test is required solely to relabel the platform.
2. On one representative phone from the **other supported family**, apply the approved UseSafeWeb configuration method and confirm normal allowed DNS/internet resolution works through the configured encrypted-DNS path.
3. Exercise the approved failure/ambiguity handling for that family at least to the point required by the TSK-0439 method: if the encrypted-DNS configuration cannot become effective or routing is ambiguous, the state must fail safely as Action needed/unsupported rather than be treated as verified.
4. Remove/reset UseSafeWeb on that other-family phone and confirm normal DNS/internet resolution returns.
5. Record only platform family, minimum version/capability class, network class, pass/fail outcomes, and any compatibility deviation needed for acceptance. Do not retain browsing history, DNS/domain history, device identifiers, screenshots, or participant data unless separately justified and approved.

If a representative device from the second supported family is unavailable, TSK-0511 remains WAITING unless the Project Owner explicitly changes the supported pilot scope through the governed change process. Such a scope change is not inferred here.

## Boundary

This preflight does not authorize real participant activation, does not alter the separate TSK-0431 recovery WAITING boundary, and does not resolve the owner-deferred UK representative/ICO requirement.
