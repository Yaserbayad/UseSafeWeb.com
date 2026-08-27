# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T22:12Z  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`

`CURRENT_STATE.md` owns volatile runtime state only. Planning authority is the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and routed by `Plans/Master/MANIFEST.yaml`; the WBS owns task definitions/dependencies, the relationship index owns traversal, and Layer 5 owns execution/evidence rules.

## Canonical planning authority

**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0001 PUBLISHED AND READ-BACK VERIFIED.**

- Owner freeze: `TSK-0017` PASS.
- Original frozen publication commit: `fce408f34470c0a0883ab978685b5265fdec4b97`.
- Original frozen `Plans/` tree: `e6c78a67a191e04ea85fbb68caf18b854067c3de`.
- Post-freeze `CR-0001`: reversed the impossible TSK-0203/TSK-0483 dependency ordering without changing task scope/status/acceptance/gates/authority.
- CR-0001 publication commit: `904ca6cb0beca7a868d5ca64729d94f5b4d7217d`.
- Current validated `Plans/` tree: `c42616e92f0624aaf5caf788b2383a1402393dfd`.
- CR validation: PASS — 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 relationship targets, 0 broken links, 0 generated missing task IDs, 51 checksum entries valid.

## Frozen technical identity

- Domain: `UseSafeWeb.com`.
- AdGuard/DNS VM: `srv.UseSafeWeb.com` / `adguardvm`, Ubuntu 24.04 LTS, Azure `westeurope`.
- Backend: AdGuard Home.
- Current supported installed release: **v0.107.79**.
- Upstream baseline: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard remains the filtering layer.
- Client resolver identity: `dns.usesafeweb.com`.
- DoH endpoint contract: `https://dns.usesafeweb.com/dns-query`.
- Android native pilot transport: DoT to `dns.usesafeweb.com:853`.

## Persistent autonomous server execution

GitHub is the active execution bridge for eligible host-side AUTO_ALLOWED work on `adguardvm`.

- repository-scoped self-hosted runner `adguardvm`, runner `2.336.0`, account `azureusr`;
- non-interactive sudo: PASS;
- persistent systemd runner service: enabled/active and fresh-job verified;
- ordinary host jobs use trusted `main` push triggers, `contents: read`, `persist-credentials: false`, and serialized `usesafeweb-adguard-server` concurrency.

This replaces manual per-command SSH execution for ordinary eligible server work.

## Current technical task state

### PASS

- `TSK-0435` — Azure VM handoff. Evidence blob `57de1a4187288870da7655973ac09bf907674d89`.
- `TSK-0437` — host security baseline. Evidence blob `bb9221657a65c254975f61762af73b16a3e50241`.
- `TSK-0438` — domain/control owner condition.
- `TSK-0439` — pilot device DNS methods. Evidence blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0440` — encrypted-DNS hostname/path. Evidence blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.
- `TSK-0203` — install supported AdGuard release. Evidence: `TSK_0203_ADGUARD_INSTALL_EVIDENCE_2026-08-27.md`, blob `382b70ca971739712ff8ad5668d03841d5493d62`.

### TSK-0203 accepted stable state

Official source/release:

- AdGuard Home **v0.107.79**, official `AdguardTeam/AdGuardHome` release;
- pinned Linux amd64 release asset SHA-256 `c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f`;
- official release `checksums.txt` independently agreed with that digest.

Mutation run `33121330758` / job `98688639507`: PASS.
Independent fresh audit run `33121382223` / job `98688809908`: PASS.

Fresh target audit proved:

- installed version `AdGuard Home, version v0.107.79`;
- installed binary SHA-256 `7e247573e63ce771a5925d16ca4ca9344e6e888673244289dc302f0fdfdfbf4e`;
- `AdGuardHome.service` enabled and active with ExecStart `/opt/AdGuardHome/AdGuardHome -s run`;
- local setup endpoint reachable on TCP 3000 (HTTP 302);
- no AdGuard listener yet on 53/80/443/853;
- UFW remains default-deny inbound/default-allow outbound and only SSH/TCP 22 is allowed inbound;
- persistent runner service remained active;
- `FRESH_INSTALL_AUDIT=PASS`.

ACC-0203 is fully satisfied.

### Newly eligible / ordered next

1. `TSK-0201` — secure AdGuard administration and change access: **TODO / selected next**. The initial setup listener exists but remains firewall-blocked; complete authenticated initialization locally and establish a restricted attributable admin/change path before any public resolver port is opened.
2. `TSK-0204` — disable persistent query and file logging: eligible after TSK-0203 + existing TSK-0200 PASS.
3. `TSK-0483` — resolver abuse/amplification protections: now dependency-eligible after CR-0001 + TSK-0203, but configure only after the resolver/configuration surface is initialized; still mandatory before public resolver activation.
4. `TSK-0407` — configure Quad9 dns10 / ECS off: dependency-eligible if its frozen TSK-0405 predecessor remains PASS; execute after admin initialization and privacy controls in current security/privacy ordering.
5. `TSK-0429` — define privacy-minimal backup scope: independently eligible after TSK-0437; lower immediate priority than securing/configuring the live resolver target.

### WAITING external provider action

- `TSK-0441` — public `dns.usesafeweb.com` record: no record is claimed created; current execution environment still lacks an authorized DNS-provider account action.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable evidence.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS query history in GitHub.
- Public resolver ports remain closed until their exact configuration/security/privacy/abuse/TLS tasks are verified.
- Azure control-plane remains owner-managed; GitHub runner autonomy applies to the handed-off VM host and repository-authorized tasks.

## Exact next authoritative step

Execute `TSK-0201`: use the versioned AdGuard Home setup/control interface locally on `adguardvm` to complete initialization, create an authenticated non-public administration path with credentials stored only in a root-restricted server location, verify unauthenticated access is denied after setup, verify the admin/change path is attributable and not publicly allowed by UFW, persist evidence, then recompute eligibility before applying query/statistics/privacy/upstream/abuse configuration.
