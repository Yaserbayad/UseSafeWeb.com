# TSK-0428 — Azure Region, Recipients, and DNS Data-Path Evidence

**Task:** TSK-0428 — Verify Azure region, recipients, and data path  
**Acceptance:** ACC-0428  
**Verification:** VER-0428  
**Evidence:** EVD-0428  
**Date:** 2026-08-28

## Exact target and authoritative metadata

Fresh assertion-based target verification executed on production host `adguardvm` from workflow source commit `03c749812dca283c25e305e0c53adedce41e5af1`, workflow blob `a460dfc633e799782a7137d34ebcca96bbd69aa6`, runtime-state blob `b286cf2b0cb75c644895661bab624a9af456a251`, and approved-config blob `e9975c4e75c2a68131f049da942468d8d1952d8d`.

Azure Instance Metadata Service was queried from inside the production VM using API version `2025-04-07`. The run asserted Azure environment `AzurePublicCloud`, VM name `adguardvm`, VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`, and Azure location **`westeurope`**.

Current accepted recovery-runner evidence separately identifies the only handed-off recovery target as Azure VM `adguartestdvm`, also in West Europe, with AdGuard/Nginx inactive. There is no accepted or active US DNS node in the governed runtime inventory.

## DNS recipients and path

The live persisted AdGuard configuration directly asserted upstream DNS exactly `https://dns10.quad9.net/dns-query`; bootstrap resolvers exactly Quad9 dns10 addresses `9.9.9.10`, `149.112.112.10`, `2620:fe::10`, `2620:fe::fe:10`; zero fallback/private upstream entries; no upstream file; ECS disabled; loopback-only plain DNS; query/file logging and statistics disabled; IP anonymisation enabled; and zero persistent clients.

Effective Nginx configuration asserted public identity `dns.usesafeweb.com` and exactly two proxy targets, both loopback-only: `http://127.0.0.1:3000` for the DoH HTTP backend and `127.0.0.1:53` for the DoT stream backend. No external application-vendor proxy target is configured. Listener/service checks found the expected DNS host topology and no common application/mail/database or container/mail service participating in the resolver path. A final synthetic allowed-domain query resolved successfully.

Therefore the active child-linked DNS request path is bounded to: **supported device -> UseSafeWeb Azure West Europe DNS endpoint -> same-host Nginx/AdGuard loopback path -> Quad9 dns10 recursive resolver**. Cloudflare authoritative DNS, Let's Encrypt certificate operations, GitHub runner/control tooling, and filter-list distribution are operational/control-plane dependencies but do not receive the child-linked DNS query payload in this resolver path; they are not additional DNS-query processors for ACC-0428.

No CDN, analytics, payment, email, US DNS node, or other application processor was found in the active DNS-query path.

## Deviation and disposition

Initial verifier run `33167781526` was not accepted: Azure IMDS and live AdGuard assertions passed, but the Nginx check incorrectly expected only the DoH loopback proxy and failed when it correctly observed the separate local DoT proxy `127.0.0.1:53`. No product/runtime mutation occurred. The verifier was corrected to require exactly both approved loopback targets and rerun; this evidence is emitted only after the corrected full target audit passes.

## Current-source corroboration

Microsoft documents Azure IMDS as the host-local authoritative metadata service for running Azure VMs and exposes compute `location`/`vmId`. Quad9's current service documentation identifies `dns10.quad9.net`, `https://dns10.quad9.net/dns-query`, and the four bootstrap addresses above as its no-threat-blocking privacy-first service. These source facts were checked on 2026-08-28; the PASS rests on fresh target/runtime evidence.

## Acceptance

- Azure metadata shows West Europe: **PASS**.
- DNS configuration/runtime shows Quad9 dns10 only for recursive resolution/bootstrap: **PASS**.
- No active US DNS node participates: **PASS**.
- No CDN, analytics, payment, email, or other application processor participates in the active child-linked DNS query path: **PASS**.
- Exact environment/artifact and reproducible target assertions retained without participant browsing data: **PASS**.

**Stable outcome: TSK-0428 = PASS.**

This verifies the current DNS data path only. It does not authorize Azure control-plane changes, real-participant activation, web/application deployment, or legal/release-gate bypass.
