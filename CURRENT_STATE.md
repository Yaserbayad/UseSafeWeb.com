# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T22:19Z  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`

`CURRENT_STATE.md` owns volatile runtime state only. Planning authority is the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and routed by `Plans/Master/MANIFEST.yaml`; the WBS owns task definitions/dependencies, the relationship index owns traversal, and Layer 5 owns execution/evidence rules.

## Canonical planning authority

**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0001 PUBLISHED AND READ-BACK VERIFIED.**

- Owner freeze `TSK-0017`: PASS.
- Current validated `Plans/` tree after bounded CR-0001: `c42616e92f0624aaf5caf788b2383a1402393dfd`.
- CR-0001 publication commit: `904ca6cb0beca7a868d5ca64729d94f5b4d7217d`.
- CR validation: 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 relationship targets, 0 broken links, 0 generated missing task IDs, 51 checksum entries valid.
- CR-0001 changes only dependency ordering: AdGuard installation precedes live resolver-abuse controls; no scope/status/acceptance/gate/authority decision changed.

## Frozen technical identity

- AdGuard/DNS VM: `srv.UseSafeWeb.com` / `adguardvm`, Ubuntu 24.04 LTS, Azure `westeurope`.
- AdGuard Home: **v0.107.79**.
- Upstream baseline: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard is the filtering layer.
- Client resolver: `dns.usesafeweb.com`.
- DoH contract: `https://dns.usesafeweb.com/dns-query`.
- Android native pilot transport: DoT `dns.usesafeweb.com:853`.

## Persistent autonomous server execution

GitHub is the active execution bridge for eligible AUTO_ALLOWED host work.

- repository-scoped runner `adguardvm`, runner `2.336.0`, account `azureusr`;
- systemd runner service enabled/active and fresh-job verified;
- non-interactive sudo verified;
- ordinary host jobs use trusted `main`, `contents: read`, `persist-credentials: false`, and serialized `usesafeweb-adguard-server` concurrency.

Manual per-command SSH execution is no longer the normal project path.

## Current technical task state

### PASS

- `TSK-0435` — Azure VM handoff. Evidence blob `57de1a4187288870da7655973ac09bf907674d89`.
- `TSK-0437` — host security baseline. Evidence blob `bb9221657a65c254975f61762af73b16a3e50241`.
- `TSK-0438` — domain/control owner condition.
- `TSK-0439` — pilot device DNS methods. Evidence blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0440` — encrypted-DNS hostname/path. Evidence blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.
- `TSK-0203` — install supported AdGuard release. Evidence blob `382b70ca971739712ff8ad5668d03841d5493d62`.
- `TSK-0201` — secure AdGuard administration/change access. Evidence: `TSK_0201_ADGUARD_ADMIN_EVIDENCE_2026-08-27.md`, blob `ae06672e1cebdf87d006b85b80e5a7977f4e69b9`.

### TSK-0201 accepted stable state

Mutation run `33121944276` / job `98690689645`: PASS.  
Independent audit run `33121987585` / job `98690840349`: PASS.

Fresh target evidence:

- authorised admin identity `usesafeweb-admin`; secret remains only in `/var/lib/usesafeweb/adguard/admin.env`, mode `600 root:root`;
- authenticated local `/control/status` HTTP 200;
- unauthenticated `/control/status` HTTP 401;
- administration listener only `127.0.0.1:3000`;
- AdGuard DNS listeners only TCP/UDP `127.0.0.1:53` at this stage;
- UFW still exposes only SSH/TCP 22;
- AdGuard service active/enabled;
- runner service active;
- changes are attributable through the GitHub commit/workflow/run/job chain.

ACC-0201 is fully satisfied.

### Selected next

`TSK-0204` — disable persistent query and file logging: **TODO / selected**.

Prepared canonical implementation `infrastructure/adguard-server/disable-query-logging.sh`, blob `770dcc466d0d0c569aa052105f8ff5c189c8e116`, uses the authenticated local API to preserve unrelated query-log settings while setting `enabled=false`, clearing prior history, issuing a synthetic DNS test, proving the test query is not retained, and checking that no non-empty `querylog.json*` file remains.

### Subsequent current-gate work

- `TSK-0205` — disable/exclude identifiable per-client statistics: waits on TSK-0204 PASS.
- `TSK-0206` — enable IP anonymisation: waits on TSK-0205 PASS.
- `TSK-0483` — resolver abuse/amplification controls: dependency-eligible after TSK-0203 but remains ordered after immediate admin/privacy controls; mandatory before public resolver activation.
- `TSK-0407` — configure Quad9 dns10 / ECS off: execute after immediate privacy controls in current security/privacy ordering.
- `TSK-0429` — privacy-minimal backup scope: independently eligible, lower immediate priority than live resolver privacy/security configuration.

### External provider boundary

- `TSK-0441` — public `dns.usesafeweb.com` record: no record is claimed created; no authorized DNS-provider account action is currently available in the connected execution environment.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable proof.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS query history in GitHub.
- Public resolver ports remain closed until exact privacy/security/abuse/TLS tasks are verified.
- Azure control-plane remains owner-managed; runner autonomy applies to the handed-off VM and repository-authorized tasks.

## Exact next authoritative step

Execute and independently audit `TSK-0204`, persist PASS evidence if the disabled query log survives a synthetic DNS request without retaining a query or non-empty `querylog.json*` file, then recompute eligibility before TSK-0205.
