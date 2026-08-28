# TSK-0442 — TLS Certificate Current Partial Evidence

**Task:** TSK-0442 — Issue and install TLS certificate  
**Acceptance:** ACC-0442  
**Date:** 2026-08-28  
**Resolver identity:** `dns.usesafeweb.com`

## Authoritative acceptance contract

ACC-0442 requires all of the following:

1. certificate chain validates on target devices;
2. hostname matches;
3. weak protocols are disabled; and
4. private keys are access-restricted.

TSK-0442 is `AUTO_ALLOWED`, HIGH priority, critical path, with hard predecessors `TSK-0441; TSK-0011`. TSK-0441 is current runtime PASS.

## Completed certificate/server work

The production certificate was issued through Let's Encrypt after a successful HTTP-01 path. Current target verification proves the certificate remains present and valid for `dns.usesafeweb.com`, with more than 30 days remaining and a root-owned mode-0600 private key.

The frozen TSK-0440 architecture requires the AdGuard administration surface to remain non-public. Because AdGuard's native HTTPS listener shares DoH and the web UI, the accepted implementation uses a same-host Nginx TLS proxy restricted to `/dns-query`, while AdGuard administration remains `127.0.0.1:3000` and plain DNS remains loopback-only.

TLS-proxy installation run: `33157853876`  
Job: `98804837297`  
Result: **PASS local install**

That run directly proved:

- production identity guard: PASS;
- pre-change privacy/filter/abuse/admin baseline: PASS;
- loopback DoH backend enabled;
- Nginx encrypted-DNS proxy active;
- local DoH functional;
- local DoT functional;
- public TLS virtual host returns 404 for administration/non-DoH routes;
- TLS 1.0 and TLS 1.1 rejected;
- TLS 1.2 and TLS 1.3 accepted on the HTTPS listener;
- post-change privacy/abuse/filter invariants preserved;
- administration/plain-DNS/privacy/logging boundaries preserved;
- host UFW exposes encrypted DNS 443/853 while plain DNS 53 remains closed.

## Fresh current-state proof

Post-ingress production audit run: `33158990648`  
Job: `98808581681`  
Result: **PASS**

Fresh proof establishes:

- production Azure VM identity: PASS;
- Ubuntu 24.04, AdGuard and Nginx active;
- patch state current;
- Nginx bound on `0.0.0.0:443` and `0.0.0.0:853`;
- admin listener remains `127.0.0.1:3000`;
- plain DNS remains `127.0.0.1:53` TCP/UDP;
- UFW allows 443/853 and does not allow 53;
- path-restricted Nginx configuration valid;
- certificate hostname/key-state check: PASS;
- local TLS on 443/853: PASS;
- local DoH and DoT: PASS;
- public TLS virtual-host non-DoH/admin routes remain 404.

Azure Instance Metadata returned private IP `172.16.0.4` and no `publicIpAddress` value on the VM NIC. Azure control-plane configuration remains owner-managed, so this is recorded as target evidence rather than interpreted as a control-plane decision.

## Owner-reported external condition

The owner reported on 2026-08-28 that Azure inbound TCP 443 and 853 were opened. That current owner instruction is accepted as an instruction/fact report but is not by itself execution proof of the target-device acceptance criterion.

A GitHub-hosted external verification job was attempted in run `33158855146`, but the hosted job terminated without usable test steps/log evidence. Raw outbound network probes from the ChatGPT sandbox were also shown to refuse unrelated public destinations, so those sandbox results are explicitly excluded from acceptance evidence.

## Remaining acceptance gap

No direct current observation yet proves that the certificate chain validates from the actual supported target-device environment(s). Therefore ACC-0442 is not fully proven even though hostname, protocol policy, key restriction, local encrypted-DNS functionality, and server-side exposure are proven.

## Stable outcome

**TSK-0442: WAITING.**

Deterministic resolution condition: obtain direct target-device/external validation of `dns.usesafeweb.com` over the supported encrypted-DNS path, proving trusted certificate-chain/hostname validation while the non-public administration and plain-DNS boundaries remain intact. Only then may TSK-0442 move to PASS and unlock TSK-0443.
