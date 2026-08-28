# TSK-0514 — External Endpoint and Target-Device Verification Preflight Evidence

**Task:** TSK-0514 — Verify the endpoint from external networks and target devices  
**Acceptance:** ACC-0514  
**Date:** 2026-08-28

## Authoritative contract

The canonical WBS defines TSK-0514 as L2 / A3 / `AUTO_ALLOWED` / HIGH, with hard predecessors `TSK-0442; TSK-0443`, both now current PASS.

ACC-0514 requires: **All target tests pass; network-specific failures are recorded; removing profile/config restores normal DNS behaviour.**

Referenced requirements/constraints establish:

- `REQ-0065`: `dns.usesafeweb.com` must be configurable on supported client devices using the approved encrypted-DNS method;
- `REQ-0066`: the DNS service must be verified from at least one network outside Azure and the operator's normal network before pilot approval;
- `REQ-0069`: onboarding must include exact device settings for each supported setup method and a removal/recovery path that restores normal DNS behavior;
- `CON-0023`: test evidence must remain privacy-minimised and reproducible without unnecessary browsing/content capture;
- `CON-0029`: protection must not be inferred merely from configuration presence; effective behavior must be verified;
- `VER-0514`: target-system external observation is required on the actual supported client/network path with privacy-safe evidence.

Contract inspection workflow: `.github/workflows/governance-task-row-inspect.yml`  
Commit: `a7cf226a57dcc07d3c6cc226ccfb1c821a69a2a9`  
Run: `33162389253`  
Job: `98819702034`  
Result: **PASS authority inspection**.

## Current valid predecessor/device evidence

Current accepted evidence already proves:

- `TSK-0442`: real-phone encrypted-DNS/TLS operation was directly observed by the Project Owner and the server-side certificate/hostname/protocol/private-key controls were freshly verified;
- `TSK-0443`: certificate renewal/expiry monitoring is operational and current;
- Android baseline uses native Private DNS / DoT `dns.usesafeweb.com` on supported Android 9+ devices;
- iPhone baseline uses the approved DoH profile with `https://dns.usesafeweb.com/dns-query` on supported iOS 14+ devices.

The owner's earlier statement that a real-phone test was done and working is preserved and is not being discarded or needlessly repeated.

## Remaining direct-observation gap

The existing phone observation did **not** explicitly establish the two additional facts required for ACC-0514/REQ-0066/REQ-0069:

1. the supported phone was verified while connected through a network outside Azure **and** outside the operator's normal network; and
2. removing/resetting the UseSafeWeb DNS profile/configuration restored normal DNS behavior afterward.

No durable evidence currently identifies the earlier phone test network as satisfying REQ-0066, and no earlier evidence states that the profile/private-DNS configuration was removed/reset and normal DNS behavior was restored.

The independent recovery VM `adguartestdvm_correct` cannot itself satisfy REQ-0066 because it is an Azure VM rather than the required external supported client/network path.

No browsing history, domain history, DNS query history, device identifier, participant identity, screenshot, or other personal content is required to close this evidence gap. A privacy-safe owner observation consisting only of platform/network class and pass/fail outcomes is sufficient.

## Stable outcome

**TSK-0514: WAITING.**

Deterministic resolution condition: on the already-supported real phone, verify UseSafeWeb encrypted DNS while using at least one network outside Azure and outside the operator's normal network (cellular data is normally the simplest qualifying path when the normal network is home/work Wi-Fi), record whether the test passes or any network-specific failure occurs, then remove/reset the UseSafeWeb DNS configuration and confirm normal DNS/internet resolution is restored. No ordinary browsing-history capture is needed.

After that owner observation is supplied, ACC-0514 can be evaluated for PASS and the L2 queue must be recomputed.
