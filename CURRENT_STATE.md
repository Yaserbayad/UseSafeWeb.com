# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T22:27Z  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`

`CURRENT_STATE.md` owns volatile runtime state only. Planning authority remains the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and routed by `Plans/Master/MANIFEST.yaml`; WBS owns task definitions/dependencies, relationship index owns traversal, and Layer 5 owns execution/evidence rules.

## Canonical planning authority

**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0001 PUBLISHED AND READ-BACK VERIFIED.**

- Current validated `Plans/` tree: `c42616e92f0624aaf5caf788b2383a1402393dfd`.
- CR-0001 publication commit: `904ca6cb0beca7a868d5ca64729d94f5b4d7217d`.
- Validation: 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 targets, 0 broken links, 0 generated missing task IDs, 51 checksum entries valid.

## Frozen technical identity

- Target: `srv.UseSafeWeb.com` / `adguardvm`, Ubuntu 24.04 LTS, Azure `westeurope`.
- AdGuard Home: **v0.107.79**.
- Upstream baseline: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard remains the filtering layer.
- Client resolver: `dns.usesafeweb.com`.
- DoH contract: `https://dns.usesafeweb.com/dns-query`.
- Android native pilot transport: DoT `dns.usesafeweb.com:853`.

## Persistent autonomous server execution

GitHub is the active execution bridge for eligible AUTO_ALLOWED host work. Repository-scoped runner `adguardvm` runs as `azureusr` through a persistent systemd service with non-interactive sudo. Ordinary host jobs are restricted to trusted `main`, read-only repository permissions, no persisted checkout credentials, and serialized `usesafeweb-adguard-server` concurrency.

## Current technical task state

### PASS

- `TSK-0435` — Azure VM handoff — evidence blob `57de1a4187288870da7655973ac09bf907674d89`.
- `TSK-0437` — host security baseline — evidence blob `bb9221657a65c254975f61762af73b16a3e50241`.
- `TSK-0438` — domain/control owner condition.
- `TSK-0439` — pilot device DNS methods — evidence blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0440` — encrypted-DNS hostname/path — evidence blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.
- `TSK-0203` — supported AdGuard release installed — evidence blob `382b70ca971739712ff8ad5668d03841d5493d62`.
- `TSK-0201` — restricted authenticated administration/change path — evidence blob `ae06672e1cebdf87d006b85b80e5a7977f4e69b9`.
- `TSK-0204` — persistent query/file logging disabled — evidence blob `79b0e5f4c42eadc8e7ecf7f7598a1b6ad1bcc785`.
- `TSK-0205` — identifiable per-client statistics disabled — evidence: `TSK_0205_CLIENT_STATS_PRIVACY_EVIDENCE_2026-08-27.md`, blob `47fb0e0e6b64ceab965b2ca0ee259b40a98032c6`.

### TSK-0205 accepted stable state

Mutation run `33122472506` / job `98692503341`: PASS.  
Independent audit run `33122513746` / job `98692650302`: PASS.

Direct target evidence:

- statistics API config reports `enabled=false`;
- existing statistics were reset;
- synthetic queries did not create `top_clients` records;
- total stored statistics query count remained `0` in mutation and fresh audit;
- persisted `AdGuardHome.yaml` records `statistics.enabled=false`;
- AdGuard service remained active.

ACC-0205 is fully satisfied.

### Selected next

`TSK-0206` — enable client-IP anonymisation: **TODO / selected**. Current query-log configuration already reports `anonymize_client_ip=false`; the next change must set this flag to true without re-enabling query logging or statistics, persist it, and independently verify the resulting privacy state.

### Subsequent current-gate work

- `TSK-0483` — resolver abuse/amplification controls: dependency-eligible and mandatory before public resolver activation; ordered after immediate privacy controls.
- `TSK-0407` — configure Quad9 dns10 / ECS off: execute after immediate privacy controls, subject to verified predecessor state.
- `TSK-0429` — privacy-minimal backup scope: independently eligible; lower immediate priority than live resolver privacy/security controls.

### External provider boundary

- `TSK-0441` — public `dns.usesafeweb.com` DNS record: no record is claimed created; no authorized DNS-provider account action is currently available through connected tools.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable proof.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS query history in GitHub.
- Public resolver ports remain closed until exact privacy/security/abuse/TLS controls are verified.
- Azure control-plane remains owner-managed; runner autonomy applies to the handed-off VM and repository-authorized tasks.

## Exact next authoritative step

Execute and independently audit TSK-0206 by setting AdGuard Home v0.107.79 query-log `anonymize_client_ip=true` while preserving `enabled=false`, verify persisted configuration and that query logging/statistics remain disabled, then persist evidence and recompute the current LG-03 technical queue.
