# TSK-0437 — Post-TLS Host Security Revalidation Evidence

**Task:** TSK-0437 — Apply host security baseline  
**Acceptance:** ACC-0437  
**Date:** 2026-08-28  
**Target:** Azure VM `adguardvm`, West Europe, Ubuntu 24.04 LTS

## Acceptance contract

ACC-0437 requires only required ports/services exposed, restricted administration, current patches, and captured baseline evidence.

## Reopened current-patch condition

A post-TLS reconciliation audit detected five newly installable Ubuntu Python 3.12 package updates. The historical PASS could not remain current until that drift was repaired.

Patch repair workflow: `.github/workflows/governance-task-row-inspect.yml`  
Run: `33158277980`  
Job: `98806231226`  
Result: **PASS**

The job upgraded exactly five packages from Ubuntu noble-updates, then proved:

- `NO_PENDING_UPGRADES=PASS`;
- `REBOOT_REQUIRED=NO`;
- AdGuard Home and Nginx remained active;
- `TSK_0437_PATCH_REPAIR=PASS`.

## Post-TLS production audit

Run: `33158990648`  
Job: `98808581681`  
Result: **PASS**

Fresh target evidence proved:

- exact production Azure VM identity and West Europe region;
- Ubuntu 24.04 baseline;
- AdGuard Home and Nginx active; Nginx enabled;
- no pending installable package update and no reboot requirement;
- Nginx listeners on `0.0.0.0:443` and `0.0.0.0:853`;
- AdGuard administration remains `127.0.0.1:3000` only;
- AdGuard plain DNS remains `127.0.0.1:53` TCP/UDP only;
- UFW active with deny-incoming/allow-outgoing defaults;
- UFW allows SSH 22, ACME HTTP-01 80, DoH TLS 443, and DoT TLS 853; it does not allow plain DNS 53;
- path-restricted Nginx configuration valid;
- certificate hostname and private-key permissions valid;
- local TLS 443/853, local DoH, and local DoT functional;
- `/control/status` and `/` return 404 through the public TLS virtual host, preserving the non-public administration boundary.

Marker: `PRODUCTION_POST_INGRESS_AUDIT=PASS`.

## Independent reconciliation

Run: `33159129601`  
Job: `98809042724`  
Result: **PASS**

It independently re-proved:

- current patch/service baseline;
- effective SSH hardening;
- current UFW allow-set exactly `22/tcp,80/tcp,443/tcp,853/tcp`;
- externally bound TCP listener ports exactly `22,443,853`;
- privacy/key/logging boundary;
- no non-empty AdGuard query-log file;
- marker `TSK_0437_POST_TLS_PATCH_REVALIDATION=PASS`.

## Stable outcome

**TSK-0437: PASS.**

The current TLS-proxy service exposure is intentional downstream service exposure and remains within ACC-0437 because only required encrypted-DNS/ACME/SSH ports are allowed, administration stays restricted, plain DNS stays non-public, and current patch state is directly re-proven.
