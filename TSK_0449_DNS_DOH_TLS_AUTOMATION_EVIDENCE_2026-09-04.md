# TSK-0449 DNS, DoH endpoint, and certificate automation evidence

**Date:** 2026-09-04
**Task:** TSK-0449 — Implement environment DNS, DoH endpoint, and certificate automation
**Acceptance:** ACC-0449
**Verification:** VER-0449
**Evidence:** EVD-0449
**Source commit:** `064ee110cd6d90136ea37df574baaef848b82d8a`
**Verifier blob:** `456b7835a8631ebb57859e00c8604590e110ba1c`
**Verifier SHA-256:** `d7867094fc0213107e634b8ed9e6a31cddb0cd43db9e651bc8b2aa6cd8f8a779`
**GitHub Actions run / attempt:** `33850683968 / 1`
**Target:** repository-scoped self-hosted runner on `adguardvm`, Ubuntu 24.04 LTS, Azure West Europe.

## Result

**PASS.** The existing approved DNS/DoH/TLS automation was verified without changing DNS records, Azure resources, Nginx configuration, firewall state, certificate lineage, public activation, or any participant-facing state.

- Target verification confirmed `dns.usesafeweb.com` resolves directly to the handed-off Azure resolver without persisting the address, and the target is in the approved West Europe region.
- Local target verification passed trusted TLS hostname/chain checks on encrypted-DNS listeners, TLS protocol checks, DoH response validation, negative wrong-hostname/path/admin checks, and the non-public plaintext-DNS boundary.
- A separate GitHub-hosted verifier independently passed public DNS resolution, public DoH TLS/hostname validation on TCP 443, DoH response validation, and negative public-admin/wrong-route/wrong-hostname checks.
- `certbot.timer` is enabled/active; the existing root-owned deploy hook is present/executable; the approved Certbot renewal rehearsal passed with `--dry-run --no-random-sleep-on-renew`.
- The production certificate full-chain hash was identical before and after the renewal rehearsal; no production certificate was replaced by this task.
- The daily expiry monitor retains the approved 30-day threshold and owner issue route; the emergency replacement/rollback runbook remains present.
- Private-key contents were never read; ownership/permission checks passed, and versioned DNS/TLS artifacts contain no detected secret material.
- No CI/ephemeral resolver endpoint is provisioned yet (TSK-0450 is downstream); persistent staging was not triggered. No new CI/staging/public DNS endpoint was provisioned.

## Sanitized evidence integrity

- Target transcript SHA-256: `76616a30656d6cacb53dd5ac8be85b07e40529e2f3f0b804777cf88b8789694c`
- Independent external transcript SHA-256: `048c6b1ce4231a64489e8dcb19bb27cf0482a77d66f88b681e1de2e5882193a9`
- Evidence contains no IP address, private key, ACME credential, registrar/API credential, raw DNS response/query history, or participant/client identifier.

## Authority and non-inference

This evidence uses the existing canonical `DNS_ENDPOINT_DECISION.md`, `TLS_CERTIFICATE_RENEWAL_RUNBOOK.md`, and `certificate-expiry-monitor.yml`; it creates no second DNS/certificate authority. REQ-0049/REQ-0050, CON-0004/CON-0005, INT-0014, and RSK-0048 remain controlling. This PASS proves only TSK-0449. It does not pass or alter TSK-0455, TSK-0456, TSK-0457 or TSK-0492; deploy a new environment; change DNS records; issue/replace a production certificate; distribute profiles/certificates; revoke service; process participants; enable telemetry; authorize public/market activation; make payment; or satisfy launch gates.
