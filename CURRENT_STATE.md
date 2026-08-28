# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-28T00:35:28Z  
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
- `TSK-0204` — persistent query logging and file query logging explicitly disabled — corrected evidence: `TSK_0204_QUERYLOG_PRIVACY_EVIDENCE_2026-08-27.md`, blob `aa84d93d33d789fe4ff74ea12bcc2e5ffccd5b06`.
- `TSK-0205` — identifiable per-client statistics disabled — evidence: `TSK_0205_CLIENT_STATS_PRIVACY_EVIDENCE_2026-08-27.md`, blob `47fb0e0e6b64ceab965b2ca0ee259b40a98032c6`.
- `TSK-0206` — client-IP anonymisation enabled while query logging/statistics remain disabled — evidence: `TSK_0206_CLIENT_IP_ANONYMIZATION_EVIDENCE_2026-08-27.md`, blob `5905136433d930c2325a877e10a45e8540ac6a80`.
- `TSK-0483` — resolver abuse/amplification protections verified — evidence: `TSK_0483_RESOLVER_ABUSE_PROTECTION_EVIDENCE_2026-08-27.md`, blob `8a6426707fe9c9c8cd08f6b55e25d6b48bb8b28c`.
- `TSK-0407` — exact Quad9 dns10 DoH upstream with ECS disabled verified — evidence: `TSK_0407_QUAD9_DNS10_ECS_EVIDENCE_2026-08-27.md`, blob `7afeca58e9205234a230d2de702b99648b35347d`.
- `TSK-0406` — conservative versioned filtering baseline, narrow exception path and exact rollback verified — policy: `infrastructure/adguard-server/filter-policy-v1.yaml`, blob `333a4ef8cd34719d66056aa608ab19473f839634`; evidence: `TSK_0406_FILTERING_POLICY_EVIDENCE_2026-08-27.md`, blob `bb4514b4af7c1c5e616b7875f98e86962fee0325`.
- `TSK-0202` — secret-safe approved AdGuard settings exported/versioned and proven exactly equal to current live safe settings — artifact: `infrastructure/adguard-server/approved-adguard-config-v1.json`, blob `ea85830b5ef9de7f2772e5467570d52013228b0b`; settings SHA-256 `327c374d46fc40c03a847a57d7078df6035edc71710eb8725ce57c69ac8a93a8`; evidence: `TSK_0202_ADGUARD_CONFIG_EXPORT_EVIDENCE_2026-08-27.md`, blob `d885d3f8e53c052809620958d82eb3114d558b84`.
- `TSK-0429` — privacy-minimal AdGuard backup scope documented and independently verified against current DPIA/retention/live state — policy: `infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md`, blob `e62b48a3e746b1be90881bbffab3b7680384cc16`; evidence: `TSK_0429_PRIVACY_MINIMAL_BACKUP_SCOPE_EVIDENCE_2026-08-27.md`, blob `b77c6d7a2e17adc5e653151b55137467a8c5b62f`.
- `TSK-0430` — encrypted configuration backup created, independently audited and directly decrypted by the authorised owner — evidence: `TSK_0430_ENCRYPTED_CONFIG_BACKUP_EVIDENCE_2026-08-27.md`, blob `de1820cb2a9fc5b175c5e5eb1e18b45e6a430a82`; ciphertext SHA-256 `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`; owner recipient fingerprint `SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`; owner-side decrypted configuration SHA-256 `d8b6eae3b85edbaa1c49e318354389dc616099ecb3d2d90eff3c3dd8c663e1f2`.

### TSK-0204 corrected stable state

Downstream read-only TSK-0202 inspection exposed a previously unverified latent configuration: global `querylog.enabled=false`, but persisted `querylog.file_enabled=true`. Official AdGuard documentation defines these as separate controls. Current AdGuard implementation returns before adding records when global logging is disabled, so no active query-history leakage was evidenced; nevertheless the file-write capability contradicted the frozen project requirement and stale TSK-0204 PASS was correctly reopened.

The canonical control script was hardened to manage the separate persisted scalar while AdGuard is stopped, with a root-only target-local rollback copy, post-restart API readiness polling, exact invariant checks, and a corrected privileged rollback guard. Final script blob: `3018fedb5292c5c302a74ff8b42cada18aec26b5`.

First corrective run `33126239702` / job `98704969927` reached persisted `enabled=false` + `file_enabled=false` but failed on a transient HTTP 404 during immediate post-restart API verification and was not accepted. A separate read-only audit run `33126279381` / job `98705094275` then proved the desired state was stable: both persisted settings false, control API/query-log endpoints HTTP 200, synthetic query not retained, zero query-log items, zero non-empty `querylog.json*` files, and dns10/ECS/anonymisation/statistics/filter invariants preserved.

After hardening rollback and API-readiness handling, final pinned control run `33126344825` / job `98705307945`: **PASS**. It detected `file_enabled=false` already in place, made no second direct YAML edit, cleared historical query-log state, re-proved both persisted controls false, API `enabled=false`, anonymisation enabled, fresh synthetic query retained `false`, query-log item count `0`, no non-empty query-log file, and unchanged upstream/privacy/filter invariants.

ACC-0204 is fully satisfied at the stronger evidence level.

### TSK-0202 accepted stable state

Fresh corrected live export run `33127050108` / job `98707574318`: **PASS**. It asserted the current approved pre-public resolver/privacy/filter/admin/abuse invariants and emitted only a non-sensitive allowlist. Versioned artifact `infrastructure/adguard-server/approved-adguard-config-v1.json` v1.0.0 is blob `ea85830b5ef9de7f2772e5467570d52013228b0b`, and independent audit run `33127141644` / job `98707868115` proved exact live-to-artifact equality at SHA-256 `327c374d46fc40c03a847a57d7078df6035edc71710eb8725ce57c69ac8a93a8`, verified 9 linked evidence blobs, persistent client count `0`, and non-empty query-log file count `0`.

ACC-0202 is fully satisfied. Its `REQ-0022` reference remains unresolved under the owner-deferred UK representative/ICO work and does not authorize real England participant activation.

### TSK-0429 accepted stable state

The exact WBS row defines TSK-0429 as `A3`, `AUTO_ALLOWED`, HIGH, critical path, hard predecessors `TSK-0437` + `TSK-0011`, acceptance `ACC-0429`.

Read-only live scope preflight run `33127459481` / job `98708878287`: **PASS**. It established current root-only config/secret/rollback permissions, logging/statistics/anonymisation state, zero persistent clients/user rules/query-log files, and absence of configured TLS private material.

Policy v1.0.0 at `infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md` defines:

- included data: raw current `AdGuardHome.yaml` + non-secret verification manifest only;
- exclusions: plaintext `admin.env`, stale rollback copies, DNS/query history, client statistics/records, participant/research data, diagnostics, caches/logs/reinstallable binaries, and current-absent TLS private material;
- encryption: confidentiality + integrity/authentication before durable/off-host retention, owner-authorised decryption, secret material separate from archive/Git/logs;
- retention: event-based latest verified + at most one previous verified generation, with immediate plaintext/failed-copy deletion rather than an invented calendar period;
- access: root during execution plus owner/explicit owner-authorised recovery path only;
- location: root-only staging on current West Europe/Netherlands DNS VM; future off-host location remains inside approved Azure/EU boundary and requires actual owner-managed target verification;
- deletion: project-controlled files deleted and absence verified; provider-side deletion verified only when a real provider target exists.

First audit run `33127565783` / job `98709225350` was not accepted because a literal static wording assertion mismatched the policy text; no target mutation occurred. Corrected independent audit run `33127643804` / job `98709483562`: **PASS**, proving policy/source alignment, source blobs, current live assumptions, no policy secret material, no TLS private material, and no query-log files.

ACC-0429 is fully satisfied.

### TSK-0430 accepted stable state

The exact WBS row defines TSK-0430 as `A3`, `AUTO_ALLOWED`, HIGH, critical path, with hard predecessors `TSK-0202`, `TSK-0429`, `TSK-0011`, acceptance `ACC-0430`.

Server-side backup creation run `33128004795` / job `98710652627`: **PASS**. Independent retained-backup audit run `33128142374` / job `98711096972`: **PASS**. The retained root-only encrypted archive was created at `2026-08-27T23:56:12Z`, size `21121` bytes, ciphertext SHA-256 `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`, with no plaintext staging or prohibited query history retained.

On 2026-08-28 the Project Owner executed the repository-pinned owner-side verifier from an owner-controlled workstation. The verifier re-streamed and locally reverified the exact retained ciphertext/sidecar, successfully decrypted it with the owner-held private key, verified package/member and manifest scope, verified the raw configuration checksum without printing configuration contents, and returned `TSK_0430_OWNER_DECRYPTION=PASS`. The owner recipient fingerprint matched `SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`; decrypted configuration SHA-256 was `d8b6eae3b85edbaa1c49e318354389dc616099ecb3d2d90eff3c3dd8c663e1f2`.

No private-key material or passphrase was supplied to GitHub, ChatGPT or project evidence. ACC-0430 is fully satisfied.

### WAITING — TSK-0431

`TSK-0431` — test pilot restore or rebuild procedure: **WAITING on an independent clean recovery target and the owner-managed Azure/TLS inputs required by ACC-0431/REQ-0052; not PASS**.

The exact WBS row is L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0430; TSK-0011`, both satisfied. ACC-0431 requires a functional test target that passes encrypted-DNS and privacy checks with recovery time/issues recorded. REQ-0052 requires a timed clean-server drill covering host baseline, packages, AdGuard, server-managed configuration, firewall/network, endpoint, TLS, filters, privacy, startup, Azure-native backup/restore, verification and health.

CON-0019 and CON-0004 require a fresh owner-provided Ubuntu 24.04 LTS Azure VM and keep Azure VM/control-plane creation/configuration outside project automation. The live `adguardvm` is the current single DNS node and is not an independent clean test target; destructively rebuilding it merely to generate evidence would create avoidable outage/security/privacy risk. In addition, TSK-0441 public DNS and TSK-0442 TLS are not yet PASS, so the encrypted-DNS/TLS portion of the acceptance is not presently available end-to-end.

No Azure control-plane action, new VM creation, or production mutation was performed. Preflight evidence: `TSK_0431_RECOVERY_DRILL_PREFLIGHT_EVIDENCE_2026-08-28.md`, blob `701398159b8b35d5c48ca9b8e3b193acfa038b1e`.

Deterministic resumption condition: an owner-provided reachable fresh Ubuntu 24.04 LTS Azure test target in the approved West Europe boundary is handed off with approved automation access and no participant data; the endpoint/TLS inputs needed for encrypted-DNS verification are available; and an owner-managed Azure-native backup/restore interface or evidence path is available for the REQ-0052 drill. Only then may the timed clean-server restore/rebuild acceptance execute.

### External/provider and legal boundaries

- `TSK-0441` — public `dns.usesafeweb.com` DNS record: no record is claimed created; no authorized DNS-provider account action is currently available through connected tools.
- Azure control-plane provisioning/configuration remains owner-managed; no backup vault/storage account or other Azure control-plane resource is assumed or created by project automation.
- Owner-deferred UK representative/ICO fee planning remains unresolved until 2027-08-27 or earlier explicit reactivation; technical work does not imply validation-readiness legal gate PASS or authorize real England participant activation.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable proof.
- Current contradictory direct evidence reopens stale PASS rather than being ignored.
- No secrets, credentials, password hashes, private keys, unnecessary personal data, or raw DNS query history may be exported to GitHub.
- Public resolver ports remain closed until exact privacy/security/abuse/TLS controls are verified.
- Azure control-plane remains owner-managed; runner autonomy applies to the handed-off VM and repository-authorized tasks.

## Exact next authoritative step

Recompute the authoritative L2 queue with TSK-0431 held WAITING. Do not bypass its clean-target acceptance. Continue the highest-priority eligible task that does not require unavailable Azure control-plane or DNS-provider authority; record any further external boundary truthfully and continue autonomous work where safe.
