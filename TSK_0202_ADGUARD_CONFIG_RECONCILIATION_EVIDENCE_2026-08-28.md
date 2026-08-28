# TSK-0202 — Post-TLS Approved AdGuard Configuration Reconciliation Evidence

**Task:** TSK-0202 — Export and version the approved AdGuard configuration  
**Acceptance:** ACC-0202  
**Date:** 2026-08-28  
**Target:** Azure VM `adguardvm`, West Europe, AdGuard Home v0.107.79

## Reason for reconciliation

TSK-0442 introduced the already-approved same-host TLS-proxy architecture: AdGuard administration remains on `127.0.0.1:3000`, AdGuard plain DNS remains loopback-only, and `http.doh.insecure_enabled=true` is used only as the loopback backend for the path-restricted Nginx `/dns-query` TLS proxy. AdGuard's own shared HTTPS/web-UI TLS listener remains disabled.

The previously accepted TSK-0202 artifact therefore required a fresh secret-safe export and exact live-to-artifact proof.

## Authoritative WBS acceptance

ACC-0202: **Artifact reproduces the approved settings, excludes secrets and query history, and is linked to the deployment evidence.**

## Safe export

Workflow: `.github/workflows/adguard-approved-config-export.yml`  
Run: `33158010249`  
Job: `98805347681`  
Result: **PASS**

The export proved:

- approved invariants: PASS;
- local DoH proxy backend: true;
- AdGuard TLS listener: disabled;
- persistent client count: 0;
- sensitive-field guard: PASS;
- approved settings SHA-256: `fcedf8b67b5d4c43544d5a57b9f74b6a45e6f3be1d778c6fb6183e83802ac49d`.

Versioned artifact: `infrastructure/adguard-server/approved-adguard-config-v1.json`  
Artifact version: `1.1.0`  
Artifact blob: `e9975c4e75c2a68131f049da942468d8d1952d8d`.

## Independent current-state reconciliation

Workflow: `.github/workflows/governance-task-row-inspect.yml`  
Run: `33159129601`  
Job: `98809042724`  
Result: **PASS**

Fresh direct target verification proved:

- production VM identity: PASS;
- approved artifact version `1.1.0`;
- exact live settings equal the artifact;
- live approved settings SHA-256 exactly `fcedf8b67b5d4c43544d5a57b9f74b6a45e6f3be1d778c6fb6183e83802ac49d`;
- `http.address=127.0.0.1:3000`;
- local-only unencrypted DoH backend enabled for the same-host proxy;
- AdGuard native TLS listener remains disabled;
- Quad9 dns10 upstream unchanged and ECS disabled;
- client-IP anonymisation enabled;
- query logging and file query logging disabled;
- statistics disabled;
- no whitelist filters, user rules, or persistent clients;
- active filter remains the approved AdGuard DNS filter;
- secret-key denylist inspection passed;
- no non-empty AdGuard query-log file remains;
- Nginx access logging remains disabled.

Markers: `TSK_0202_LIVE_ARTIFACT_EQUALITY=PASS`, `TSK_0202_SECRET_GUARD=PASS`, `TSK_0202_RECONCILIATION=PASS`.

## Stable outcome

**TSK-0202: PASS.**

ACC-0202 remains fully satisfied against the current post-TLS-proxy server state. This evidence supersedes only the live-equality/version facts of the earlier TSK-0202 evidence; it does not discard still-valid predecessor evidence or change the owner-deferred legal/participant-activation boundary.
