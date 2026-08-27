# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T22:57:55Z  
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
- `TSK-0206` — client-IP anonymisation enabled while query logging/statistics remain disabled — evidence: `TSK_0206_CLIENT_IP_ANONYMIZATION_EVIDENCE_2026-08-27.md`, blob `5905136433d930c2325a877e10a45e8540ac6a80`.
- `TSK-0483` — resolver abuse/amplification protections verified — evidence: `TSK_0483_RESOLVER_ABUSE_PROTECTION_EVIDENCE_2026-08-27.md`, blob `8a6426707fe9c9c8cd08f6b55e25d6b48bb8b28c`.
- `TSK-0407` — exact Quad9 dns10 DoH upstream with ECS disabled verified — evidence: `TSK_0407_QUAD9_DNS10_ECS_EVIDENCE_2026-08-27.md`, blob `7afeca58e9205234a230d2de702b99648b35347d`.

### TSK-0206 accepted stable state

Initial mutation run `33122650943` / job `98693120873` was **not** accepted as completion: the API mutation succeeded, but the persisted-state verifier checked the wrong YAML section and the workflow failed.

The verifier was corrected and read back before retry. Corrected mutation run `33123662351` / job `98696491164`: **PASS**.  
Independent audit run `33123701221` / job `98696614657`: **PASS**.

Direct target evidence:

- query-log API config reports `enabled=false` and `anonymize_client_ip=true`;
- statistics API config reports `enabled=false`;
- persisted `AdGuardHome.yaml` records `querylog.enabled=false`, `dns.anonymize_client_ip=true`, and `statistics.enabled=false`;
- fresh synthetic DNS activity created no retained query-log item;
- `top_clients` remained empty and stored statistics query count remained `0`;
- no non-empty `querylog.json*` file existed;
- AdGuard service remained active.

ACC-0206 is fully satisfied. Evidence contains no participant IP, browsing history, credential, token, private key, or raw DNS query history.

### TSK-0483 accepted stable state

The canonical WBS row was read directly from `Plans/Master/WBS/master-wbs.csv`: `A3`, `AUTO_ALLOWED`, hard predecessors `TSK-0203`, `TSK-0436`, `TSK-0011`, acceptance `ACC-0483`.

Predecessors were reconciled before target testing: TSK-0203 is direct runtime PASS; TSK-0436 is explicit `NOT_APPLICABLE+PASS` for the owner-managed Azure control-plane boundary; TSK-0011's publication/read-back condition is satisfied by the owner-frozen planning tree and verified CR-0001 publication/read-back state.

No resolver mutation was required. Current AdGuard controls already satisfied ACC-0483. Final acceptance run `33124114154` / job `98697977476`: **PASS**.

Direct target evidence:

- `ratelimit=20`, IPv4 `/24`, IPv6 `/56`, zero rate-limit whitelist entries;
- `refuse_any=true`;
- no public wildcard DNS bind and no non-loopback IPv4 bind;
- UFW active with default incoming deny and no current DNS/DoT allow-rule mention;
- 8/8 low-rate synthetic pilot requests received responses;
- synthetic `ANY` request returned rcode `4` with response/query size ratio `1.00`;
- 80-request burst sent in approximately 0.6 ms received 20 responses and dropped 60;
- query logging remained disabled, client-IP anonymisation remained enabled, and statistics remained disabled.

ACC-0483 is fully satisfied for the current pre-public target. This PASS does not authorize opening resolver ports, widening bind addresses, changing Azure NSG rules, or public launch; any later exposure change must preserve and re-verify the controls under the applicable downstream task/gate.

### TSK-0407 accepted stable state

The canonical WBS row was read directly from `Plans/Master/WBS/master-wbs.csv`: `A3`, `AUTO_ALLOWED`, HIGH priority, critical path, hard predecessors `TSK-0203`, `TSK-0405`, `TSK-0011`, acceptance `ACC-0407`.

No resolver mutation was required. Read-only preflight run `33124332533` / job `98698691502`: **PASS**. A first independent audit run `33124383023` / job `98698868690` was not accepted because its verifier compared AdGuard's normalized explicit `:443` test result literally against the configured default-port URL. The verifier was corrected without changing resolver state. Corrected independent audit run `33124417228` / job `98698974470`: **PASS**.

Direct target evidence:

- runtime API upstream is exactly `https://dns10.quad9.net/dns-query` and no other upstream is configured;
- upstream file is empty and fallback count is zero;
- ECS is disabled and no dns11/dns12 ECS endpoint is present;
- AdGuard's built-in upstream test for dns10 returns `OK` (reported as equivalent normalized `https://dns10.quad9.net:443/dns-query`);
- persisted `AdGuardHome.yaml` matches the exact dns10/ECS-off runtime state;
- fresh randomized synthetic resolution succeeded with `rcode=0`;
- query logging remained disabled, client-IP anonymisation remained enabled, and statistics remained disabled.

Current Quad9 documentation still identifies dns10 as the no-ECS service. Quad9 changed dns10's DNSSEC behavior effective 15 June 2026 so it now validates DNSSEC; current project requirements require exact dns10 + ECS-off and do not require DNSSEC validation to be disabled, so no requirement conflict was found.

ACC-0407 is fully satisfied.

### Selected next

`TSK-0406` — configure sensible baseline filtering policy: **TODO / selected**.

Deterministic selection evidence:

- queue-delta inspection after TSK-0407 found `TSK-0406` as the only direct successor newly unlocked by TSK-0407;
- exact WBS row: `A3`, `AUTO_ALLOWED`, HIGH, critical path, `ACC-0406`;
- hard predecessors: `TSK-0407` (runtime PASS) and `TSK-0011` (publication/read-back condition satisfied);
- `ACC-0406` requires a documented policy rationale, low-risk allowlist/exception path, no unsupported complete-safety promise, and versioned configuration;
- independently eligible `TSK-0429` is also HIGH/critical-path, but TSK-0406 precedes it in the current WBS/dependency sequence and is therefore selected first.

### Subsequent eligible current-gate work

- `TSK-0429` — define privacy-minimal backup scope: eligible after TSK-0406 unless a newly verified higher-priority safety/security/gate constraint intervenes.

### External provider boundary

- `TSK-0441` — public `dns.usesafeweb.com` DNS record: no record is claimed created; no authorized DNS-provider account action is currently available through connected tools.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable proof.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS query history in GitHub.
- Public resolver ports remain closed until exact privacy/security/abuse/TLS controls are verified.
- Azure control-plane remains owner-managed; runner autonomy applies to the handed-off VM and repository-authorized tasks.

## Exact next authoritative step

Begin `TSK-0406`. Read its linked requirements/constraint/interface/risk plus the current live AdGuard filtering configuration and any existing versioned filter-policy artifact. Detect existing policy state before mutation. Then establish the conservative baseline rationale, allowlist/exception path, claims boundary, and versioned configuration; run allowed/blocked and rollback checks with privacy-safe synthetic domains; persist/read back evidence and runtime state before selecting later work.
