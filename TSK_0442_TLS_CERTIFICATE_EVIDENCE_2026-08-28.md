# TSK-0442 — TLS Certificate Acceptance Evidence

**Task:** TSK-0442 — Issue and install TLS certificate  
**Acceptance:** ACC-0442  
**Date:** 2026-08-28  
**Resolver identity:** `dns.usesafeweb.com`

## Acceptance contract

ACC-0442 requires all of the following:

1. certificate chain validates on target devices;
2. hostname matches;
3. weak protocols are disabled; and
4. private keys are access-restricted.

TSK-0442 is L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0441; TSK-0011`, both satisfied.

## Owner-observed target-device validation

On 2026-08-28 the Project Owner reported, immediately after performing the requested real-phone validation, that **the real phone test is done and is working**.

This is accepted as direct human observation of the target-device side of ACC-0442: the supported real phone accepted and operated through the configured encrypted-DNS endpoint rather than failing certificate/hostname trust validation.

No participant identity, browsing history, DNS history, screenshot, device identifier or other personal data is required or retained for this acceptance evidence.

## Fresh server-side revalidation

Workflow: `.github/workflows/governance-task-row-inspect.yml`  
Commit: `5601ec4951583ef0fa7a5c95fb4c4fb135928b84`  
Run: `33160416730`  
Job: `98813254928`  
Result: **PASS**

Fresh direct production verification proved:

- exact production Azure VM identity: PASS;
- current WBS acceptance contract loaded from the canonical WBS;
- AdGuard Home and Nginx active;
- Nginx configuration valid;
- certificate hostname `dns.usesafeweb.com` matches;
- certificate remains valid for more than 30 days;
- private key remains root-owned mode `0600`;
- local certificate-chain/hostname verification succeeds on both 443 and 853;
- TLS 1.0 rejected;
- TLS 1.1 rejected;
- TLS 1.2 accepted;
- administration remains bound only to `127.0.0.1:3000`;
- plain DNS remains loopback-only on TCP/UDP 53;
- encrypted DNS listeners remain on TCP 443 and 853;
- public TLS virtual host returns 404 for `/` and `/control/status`, preserving the non-public admin boundary;
- UFW allows 443/853 while plain DNS 53 is not allowed.

Markers:

- `HOSTNAME_KEY_VALIDITY=PASS`
- `TLS_PROTOCOL_POLICY=PASS`
- `LISTENER_ADMIN_BOUNDARY=PASS`
- `PUBLIC_ROUTE_AND_FIREWALL_BOUNDARY=PASS`
- `TSK_0442_SERVER_SIDE_REVALIDATION=PASS`

## Evidence synthesis

- Target-device certificate-chain usability: **PASS — owner direct real-phone observation**.
- Hostname match: **PASS — fresh server verification**.
- Weak protocols disabled: **PASS — fresh server verification**.
- Private-key access restriction: **PASS — fresh server verification**.

The earlier partial evidence `TSK_0442_TLS_CERTIFICATE_PARTIAL_EVIDENCE_2026-08-28.md` remains useful historical proof of issuance and implementation. This file supersedes its WAITING conclusion because the previously missing target-device observation is now supplied by the Project Owner and the server-side controls have been freshly revalidated.

## Stable outcome

**TSK-0442: PASS.**

ACC-0442 is fully satisfied. This certificate/TLS PASS does not by itself authorize participant recruitment/activation or bypass later service-readiness/legal gates. It unlocks dependency evaluation for TSK-0443 and any other task whose hard dependency is TSK-0442.