# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T23:23:30Z  
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
- `TSK-0205` — identifiable per-client statistics disabled — evidence: `TSK_0205_CLIENT_STATS_PRIVACY_EVIDENCE_2026-08-27.md`, blob `47fb0e0e6b64ceab965b2ca0ee259b40a98032c6`.
- `TSK-0206` — client-IP anonymisation enabled while query logging/statistics remain disabled — evidence: `TSK_0206_CLIENT_IP_ANONYMIZATION_EVIDENCE_2026-08-27.md`, blob `5905136433d930c2325a877e10a45e8540ac6a80`.
- `TSK-0483` — resolver abuse/amplification protections verified — evidence: `TSK_0483_RESOLVER_ABUSE_PROTECTION_EVIDENCE_2026-08-27.md`, blob `8a6426707fe9c9c8cd08f6b55e25d6b48bb8b28c`.
- `TSK-0407` — exact Quad9 dns10 DoH upstream with ECS disabled verified — evidence: `TSK_0407_QUAD9_DNS10_ECS_EVIDENCE_2026-08-27.md`, blob `7afeca58e9205234a230d2de702b99648b35347d`.
- `TSK-0406` — conservative versioned filtering baseline, narrow exception path and exact rollback verified — policy: `infrastructure/adguard-server/filter-policy-v1.yaml`, blob `333a4ef8cd34719d66056aa608ab19473f839634`; evidence: `TSK_0406_FILTERING_POLICY_EVIDENCE_2026-08-27.md`, blob `bb4514b4af7c1c5e616b7875f98e86962fee0325`.

### Reopened TODO — TSK-0204

`TSK-0204` — disable persistent query and file logging: **TODO / reopened on contradictory current target evidence**.

The earlier PASS remains valid evidence that global query logging was disabled, prior history was cleared, fresh synthetic queries were not retained, and no non-empty `querylog.json*` file existed. However, its mutation/audit checked only `querylog.enabled=false` and file absence; neither verified the separate persisted `querylog.file_enabled` setting.

During the read-only TSK-0202 safe export, corrected run `33126066177` / job `98704396731` directly read current `AdGuardHome.yaml` and found:

- `querylog.enabled=false`;
- `querylog.file_enabled=true`;
- no persistent clients;
- no secrets or query history were exported.

Current official AdGuard documentation defines `querylog.enabled` as query-log status and `querylog.file_enabled` separately as whether query logs are written to a file. The current implementation returns before adding a query-log record when global logging is disabled, so this is not evidence of current query-history leakage. It is nevertheless contrary to the frozen project configuration requirement that persistent query **and file** logging be off, and ACC-0204 requires configuration inspection showing query/file logging disabled. Therefore the historical TSK-0204 PASS is stale for the complete current acceptance contract and is reopened rather than silently relied upon.

### Blocked by reopened predecessor

`TSK-0202` — export and version the approved AdGuard configuration: **BLOCKED** solely on the reopened hard predecessor `TSK-0204`.

The read-only safe-export verifier itself succeeded after one linter-only correction and produced no target mutation. No versioned approved-settings artifact has been created and no TSK-0202 PASS is claimed. TSK-0202 must resume only after TSK-0204 is corrected, independently verified, evidenced and republished as PASS.

### TSK-0406 accepted stable state

The canonical WBS defines TSK-0406 as `A3`, `AUTO_ALLOWED`, HIGH priority, critical path, hard predecessors `TSK-0407` + `TSK-0011`, acceptance `ACC-0406`.

The read-only baseline inspection found filtering already enabled with exactly one active maintained list: AdGuard DNS filter (`filter_1.txt`, 178285 rules at inspection), while AdAway remained configured but disabled. There were zero whitelist filters and zero user rules, `blocking_mode=default`, and normal `example.com` resolution worked. Existing dns10/ECS-off and privacy controls remained intact.

Policy v1.0.0 was created and read back at `infrastructure/adguard-server/filter-policy-v1.yaml`. It records the one-list conservative rationale, the existing privacy-safe false-positive intake as the exception path, a narrow reversible allow-rule mechanism, exact rollback, the Protection Claims Checklist as the claims boundary, explicit no-complete-safety wording, and governed change control.

First acceptance run `33125650171` / job `98703037668` was **not accepted**: after submitting a temporary randomized `.invalid` block rule, the immediate `check_host` observation had not yet converged. A pre-armed restore trap executed. Mandatory recovery audit run `33125686361` / job `98703159125`: **PASS**, directly proving API and persisted user rules returned to zero, list state was unchanged, privacy/upstream invariants were preserved, and normal resolution remained functional.

The verifier was then materially corrected to poll for observed rule-engine convergence while keeping rollback armed until restoration itself was observed. Corrected acceptance run `33125736588` / job `98703328392`: **PASS**.

Direct acceptance evidence:

- baseline randomized `.invalid` name: `NotFilteredNotFound`;
- temporary exact block: `FilteredBlackList`, convergence on poll attempt 2;
- matching narrow allow exception: `NotFilteredWhiteList`, convergence on poll attempt 2;
- exact restoration of the pre-test empty rule set: `NotFilteredNotFound`, convergence on poll attempt 3;
- API user-rule set restored exactly to `[]`;
- filter-list enabled/disabled state and whitelist state unchanged;
- persisted policy still matches v1 with zero user rules;
- dns10 upstream, ECS-off, query-log-off, anonymisation-on and statistics-off invariants preserved;
- direct post-rollback `example.com` resolution returned 2 answers.

No permanent resolver filtering mutation was required. The temporary synthetic rules were completely rolled back. ACC-0406 is fully satisfied.

### Subsequent eligible current-gate work

- `TSK-0429` — define privacy-minimal backup scope: independently eligible, but current safety/privacy blocker priority requires resolving reopened TSK-0204 first.

### External/provider and legal boundaries

- `TSK-0441` — public `dns.usesafeweb.com` DNS record: no record is claimed created; no authorized DNS-provider account action is currently available through connected tools.
- Owner-deferred UK representative/ICO fee planning remains unresolved until 2027-08-27 or earlier explicit reactivation; technical work does not imply validation-readiness legal gate PASS or authorize real England participant activation.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable proof.
- Current contradictory direct evidence reopens stale PASS rather than being ignored.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS query history in GitHub.
- Public resolver ports remain closed until exact privacy/security/abuse/TLS controls are verified.
- Azure control-plane remains owner-managed; runner autonomy applies to the handed-off VM and repository-authorized tasks.

## Exact next authoritative step

Correct reopened `TSK-0204` under its existing `A3/AUTO_ALLOWED` authority. Preserve global logging disabled, stop AdGuard before any direct YAML edit that is required because the current query-log API does not expose `file_enabled`, set only `querylog.file_enabled=false`, retain a root-only rollback copy on the target until verification succeeds, restart service, clear any historical query-log file, and independently prove both `enabled=false` and `file_enabled=false`, no retained synthetic query, no non-empty query-log file, service health, and unchanged dns10/ECS/statistics/anonymisation/filter-policy invariants. Persist/read back corrected evidence and runtime PASS before resuming TSK-0202.
