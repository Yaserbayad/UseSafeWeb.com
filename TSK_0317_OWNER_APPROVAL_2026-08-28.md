# TSK-0317 — Project Owner Approval Evidence

**Task:** `TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform`  
**Candidate:** `TSK_0317_PLATFORM_INSTALL_VERIFICATION_REMOVAL_RECOVERY_DESIGN_CANDIDATE_2026-08-28.md`  
**Exact candidate blob:** `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`  
**Decision authority:** Project Owner / HUMAN_ONLY disposition  
**Decision date:** 2026-08-28  
**Disposition:** **APPROVE**

## Owner decision

In the governed continuation immediately following presentation of the exact TSK-0317 candidate blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`, the Project Owner explicitly replied:

> Approved

This is recorded as explicit approval of the exact candidate identified by the immediately preceding authoritative decision request. No change request or rejection accompanied the approval.

## Scope of approval

The approval accepts the candidate as the TSK-0317 provisional internal L4 design baseline, including its acceptance assertions and its preserved boundaries:

- current supported design is limited to accepted Android 9+ phone and iPhone/iOS 14+ paths;
- Android uses the native DoT hostname `dns.usesafeweb.com` and iPhone uses the approved DoH profile/Server URL mechanism;
- no silent web-based Android system-DNS mutation or silent Apple profile authorization is claimed;
- configuration presence or parent confirmation is not system verification;
- unresolved VPN, Private Relay, browser/app custom resolver, managed-device, blocked-network and unaccepted-platform conditions remain truthful uncertainty/not-covered conditions;
- fallback means canonical manual guidance or safe removal/recovery, not an improvised resolver/client or silent plaintext path while retaining a UseSafeWeb protection claim;
- verification remains controlled/synthetic and privacy-minimal;
- the design remains accountless and reversible.

## Non-expansion boundary

This approval does **not** authorize implementation/build, generation or public distribution of a production `.mobileconfig`, production/public application deployment, participant processing, legal completion, payment activation, publication or launch. It does not make behavioral validation true; `RSK-0002` remains OPEN; `REQ-0022` remains unresolved; LG-03/LG-04/LG-05/LG-06 remain non-PASS; account/dashboard scope remains deferred under EXC-0001.

## Evidence role

This file is durable evidence of the HUMAN_ONLY disposition required before TSK-0317 can be accepted. It does not itself prove ACC-0317; independent acceptance verification against the unchanged candidate and current authority is still required before runtime PASS reconciliation.