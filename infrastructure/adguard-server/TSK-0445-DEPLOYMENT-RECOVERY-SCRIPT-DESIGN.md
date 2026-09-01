# TSK-0445 — Production-grade Bash deployment/recovery script design

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Task:** TSK-0445  
**Acceptance:** ACC-0445 / VER-0445 / EVD-0445  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Authority:** DEC-0054 / CR-0007 + DEC-0055 / CR-0008; A3 / AUTO_ALLOWED  
**Status represented:** design PASS CANDIDATE pending independent static acceptance and canonical read-back. This artifact does not execute recovery, mutate a server, measure RTO, or prove target-environment behavior.

## 1. Decision

Implement one auditable direct-host Bash entry point:

`infrastructure/adguard-server/deploy_or_recover.sh`

The script owns deterministic orchestration only. It consumes immutable/versioned repository artifacts plus externally supplied non-secret configuration and secrets, performs idempotent desired-state reconciliation, verifies the resulting target state, and fails closed whenever the safe result is uncertain.

The design is intentionally small: no orchestration platform, no second recovery state store, no generated shell from templates, no interactive wizard, and no generic command execution layer.

## 2. Current authoritative inputs

The implementation must consume current authority rather than historical live state:

- `TSK-0446-RECOVERY-SCOPE-CONTRACT.md` is the recovery/RTO scope contract.
- TSK-0413 bundle version `1.0.0` is the current versioned non-secret DNS desired-state input and must pass its checksum/compatibility verifier before use.
- Current AdGuard compatibility is v0.107.79 / schema 34 until TSK-0412 or later current authority supersedes it.
- Ubuntu Server 24.04 LTS is the supported owner-provided fresh-host baseline.
- `CON-0004` keeps Azure control-plane provisioning owner-managed; this script begins only after VM handoff.
- `REQ-0049` requires idempotency, ambiguity handling, bounded retry, rollback/compensation/reconciliation and final target-state verification for material effects.
- `REQ-0050` prohibits normal browsing-history persistence and restricts exceptional diagnostics to an explicit, bounded, deletion-verified path.
- `INT-0014`, `INT-0018`, `INT-0025`, and `INT-0026` define the runtime/recovery/independent-acceptance handoffs.
- `RSK-0048` remains OPEN until a later independent clean-server recovery proves the script in the target environment and against the accepted RTO.

### 2.1 Stale-helper rule

Existing scripts are reusable only after their behavior is reconciled to the current contract. They are not authority simply because they already exist.

In particular, current repository helpers such as `clean-recovery-drill-runtime.sh` and `create-encrypted-config-backup.sh` contain historical checks that require `statistics.enabled == false`. The current TSK-0446 contract instead requires minimum anonymized aggregate operational statistics with `1d` retention while persistent query/file logging, identifiable client history and browsing/activity history remain prohibited. Therefore `deploy_or_recover.sh` must **not call those helpers as authoritative recovery steps until their relevant behavior is updated/revalidated**. Historical recovery scripts remain evidence/reference, not desired state.

## 3. Files and separation of responsibility

### 3.1 Immutable/versioned code in Git

Allowed:

- `deploy_or_recover.sh`;
- current TSK-0413 bundle and verifier;
- non-secret service/unit/proxy/firewall/config templates;
- current non-secret acceptance definitions;
- optionally small sourced Bash libraries under `infrastructure/adguard-server/lib/` only if code duplication becomes material.

All executable repository files are identified by the exact release commit. The recovery run records that commit and validates required bundle hashes before mutation.

### 3.2 External non-secret configuration

Default path:

`/etc/usesafeweb/recovery.env`

The file is owner/root-managed and is **parsed as data, never sourced as shell code**. Only an explicit key allowlist is accepted. Unknown keys, duplicate keys, malformed lines, shell metacharacter tricks or unsafe paths fail preflight.

Allowed configuration classes include target role/hostname, expected public DNS hostname, protected-input file locations, current release/bundle selector, approved service paths and explicitly bounded operational flags. Values that are fixed by current canonical authority are verified against authority; configuration cannot silently override them.

### 3.3 External secrets

Default root:

`/etc/usesafeweb/secrets/`

Examples are secret/admin credential input and TLS private material or a protected mechanism that obtains it. Secret paths must be absolute, root-owned where applicable, non-symlinked unless explicitly supported, and permission-checked before use. Secret **values are never accepted as CLI arguments**, never written to the action journal, never committed, and never echoed to stdout/stderr.

`umask 077` is set before any temporary or state file is created.

## 4. Command contract

Supported modes are explicit and mutually exclusive:

```text
deploy_or_recover.sh --check
deploy_or_recover.sh --apply
deploy_or_recover.sh --verify
deploy_or_recover.sh --remove
```

Common optional input:

```text
--config /etc/usesafeweb/recovery.env
```

No mode prompts interactively once approved inputs are supplied.

### `--check`

Read-only preflight. Verify OS/architecture, root/sudo capability, target role, repository/release identity, current bundle/checksums, required commands, config syntax/ownership, secret-path existence/permissions without reading secrets into logs, current service/listener/firewall inventory, available disk, network prerequisites and compatibility. It performs no service/config/firewall mutation.

### `--apply`

Run `--check`, acquire the local technical execution lock, snapshot only the current non-secret/project-controlled state needed for compensation, calculate the desired-state plan, apply bounded changes, then run the same verification contract as `--verify`. Success is returned only after verification passes. A verified already-compliant host is a successful no-op.

### `--verify`

Read-only target inspection. Verify exact current safe-state projection, versions, service enable/active state, listener/admin exposure, firewall expectations, upstream/ECS, privacy settings, approved filters/allowlist, TLS/hostname/chain, local and external encrypted-DNS health where the environment permits, restart expectations and prohibited data/secrets checks. It never treats process `active` alone as service acceptance.

### `--remove`

Bounded project-controlled service removal/revocation path. Because it is destructive, it is non-interactive but requires **both** exact target identity validation and an explicit root-owned configuration authorization such as `ALLOW_REMOVE=true`. It removes only project-owned service/config/runtime artifacts enumerated by the implementation contract, preserves unrelated host state, and verifies the removal outcome. It never deletes Azure resources or other owner-managed control-plane objects.

## 5. Script structure

The entry point uses `#!/usr/bin/env bash`, `set -Eeuo pipefail`, `umask 077`, explicit traps and shellcheck-compatible constructs.

Recommended function groups, kept in one file until size/duplication justifies extraction:

1. `main` — argument parsing, mode dispatch, stable exit.
2. `log_*` / `die` — structured privacy-safe messages.
3. `require_*` — OS/arch/tool/privilege/target preflight.
4. `parse_config` — strict allowlisted data parser; no `source`, `eval` or command substitution from config.
5. `validate_secret_paths` — metadata/permission checks without value disclosure.
6. `verify_release_inputs` — release commit, TSK-0413 SHA256SUMS and bundle verifier.
7. `inspect_current_state` — read-only inventory and safe hashes/projections.
8. `build_plan` — compare target to desired state and classify no-op/mutation/unsupported conflict.
9. `capture_rollback_state` — minimum project-controlled non-secret/restorable metadata needed to compensate current run.
10. `apply_host_prerequisites` — required packages/direct-host prerequisites only.
11. `apply_adguard` — pinned compatible install/update path.
12. `apply_dns_config` — safe desired-state merge/atomic replacement.
13. `apply_tls_proxy` — path-restricted encrypted-DNS proxy/TLS state.
14. `apply_firewall` — current host firewall delta only; no Azure NSG/control plane.
15. `apply_services` — daemon reload/enable/start ordering without unsafe public intermediate state.
16. `verify_all` — common final acceptance checks used by `--verify` and post-`--apply`.
17. `rollback_current_run` — bounded compensation from the captured pre-run state when safe.
18. `remove_project_state` — explicit bounded removal mode.

No function accepts arbitrary shell fragments. Commands and paths are fixed or validated against explicit allowlists.

## 6. Input and command-injection controls

- Quote every variable expansion unless an exact Bash array expansion is required.
- Do not use `eval`, `bash -c` with constructed user/config content, dynamically generated shell, unsafe word splitting or glob expansion for input data.
- Represent command arguments as arrays.
- Validate enumerations with `case`; validate hostnames, paths, integers and booleans with strict functions.
- Reject newline/control characters in scalar config values.
- Normalize and compare paths before writes/deletes; destructive operations use fixed project roots and `--` where supported.
- Refuse paths resolving outside approved roots.
- Do not follow an unexpected symlink for config/secrets/state/rollback targets.
- Temporary directories are created with `mktemp -d` under a root-controlled location and removed by trap.
- Downloaded artifacts are HTTPS-only and checksum/version verified before execution/installation.
- Never overwrite an unrecognized AdGuard installation or unrelated service/configuration; fail closed and report the conflict.

## 7. Idempotency and technical concurrency

SERIAL LIGHT governs project orchestration, but the host still needs a technical execution lock. `deploy_or_recover.sh` uses a local root-owned `flock` lock file (for example `/run/lock/usesafeweb-adguard-recovery.lock`) so two host invocations cannot mutate concurrently.

Every mutation follows:

```text
inspect current target -> compare with exact desired state -> no-op or bounded change -> verify final target
```

Required idempotency properties:

- repeated `--check` / `--verify` are read-only;
- repeated `--apply` on an accepted state is a verified no-op;
- package install/version logic refuses an incompatible unknown installation rather than overwriting it;
- service files/configs use content comparison and atomic replacement;
- firewall rules are reconciled to the bounded expected host policy rather than blindly appended;
- repeated secret injection changes no durable non-secret state when the material is unchanged;
- an interrupted prior run is detected through target inspection plus the current-run journal; the script never assumes “previous command probably succeeded.”

The local lock is a runtime safety mechanism, **not** a second Governor checkpoint or persistent project state store.

## 8. Action journal and observability

Use one root-only current-run directory, for example:

`/var/lib/usesafeweb/recovery/runs/<utc>-<random>/`

It may contain only privacy-safe operational metadata:

- mode, UTC start/stop, elapsed seconds;
- release commit and bundle version/hash identity;
- target role/OS/version;
- action IDs and status (`planned`, `attempted`, `verified`, `rolled_back`, `uncertain`);
- non-secret before/after hashes or safe-field projections;
- bounded error class/code;
- final verification summary.

Never record secret values, private keys, password hashes, tokens, raw DNS queries/domains, browsing/activity history, participant data or identifiable per-client history.

Console/journald output uses stable messages such as:

```text
LEVEL=INFO ACTION=verify_bundle RESULT=PASS
LEVEL=ERROR ACTION=apply_tls CLASS=input RESULT=FAIL CODE=21
```

No raw command tracing (`set -x`) is permitted in normal or diagnostic mode because it can expose secrets.

## 9. Error and exit-code contract

The implementation reserves stable classes; exact numeric assignments are frozen with the script tests. Suggested classes:

- `0` — requested mode completed and final verification passed;
- input/config/unsupported-host failure;
- permission/privilege failure;
- dependency/download/checksum/compatibility failure;
- permanent configuration/security/privacy failure;
- transient network/package/service failure after bounded retries;
- verification failure;
- rollback completed after failed apply (overall command still non-zero);
- **uncertain outcome requiring reconciliation before retry**;
- explicitly rejected unsafe remove/retry.

Errors propagate to a single top-level handler. Cleanup traps may remove ephemeral files but must not hide the original failure code or silently “fix” an uncertain material outcome.

## 10. Retry policy

Classify before retry:

| Class | Retry rule |
|---|---|
| malformed input, unsupported OS/version, permission, checksum mismatch, privacy/security invariant failure | no retry; fail closed |
| transient package/download/network/service-start condition with observable non-destructive state | bounded retry with capped backoff and final verification |
| idempotent read/health check | bounded retry permitted |
| ambiguous configuration write, restore, delete, firewall mutation, service migration or other effect whose outcome cannot be proven | **no blind retry**; inspect durable target, reconcile, then continue or fail `uncertain` |

No unbounded loops. The implementation records retry count and cause class without sensitive payloads.

## 11. Atomic change and rollback design

Before a material apply, capture the minimum project-controlled current state required to reverse **this run**, including safe hashes/projections and protected copies of existing project config/service files when applicable. Do not capture browsing/query history as rollback material.

Mutation rules:

1. validate new content completely before replacement;
2. write to a root-only temporary path in the same filesystem when atomic rename is required;
3. set intended owner/mode before exposure;
4. stage services so a partially configured public resolver is not exposed;
5. atomically replace the target where applicable;
6. restart/reload only the affected service;
7. immediately verify the affected invariant;
8. on failure, compensate only actions whose previous state is known and restorable;
9. verify rollback result; if rollback cannot be proven, stop with `uncertain` and keep the affected public service unavailable where safer.

Rollback never means “restore whatever was in an old backup.” A protected raw backup is an input only; current safe-field authority remains TSK-0413/TSK-0446.

## 12. Service safety ordering

The script must avoid an insecure intermediate public state:

1. validate host/release/config/secrets/bundle;
2. keep or place public encrypted-DNS proxy/service unavailable while critical configuration is incomplete;
3. install/reconcile AdGuard and private/admin listeners;
4. apply current privacy/upstream/filter state;
5. restore/obtain TLS protected material and configure the path-restricted proxy;
6. apply/reconcile host firewall;
7. start/reload in dependency order;
8. verify localhost/private state first;
9. verify encrypted external service health and only then declare success.

If a mandatory service remains unavailable or a critical privacy/security state is uncertain, the safe result is **unavailable/degraded**, not an insecure fallback.

## 13. Privacy baseline the script must enforce

Final current state must match TSK-0446/TSK-0413, not older helper assertions:

- persistent raw query logging: off;
- file query logging: off;
- identifiable per-client statistics/history: excluded;
- client-IP anonymization: on wherever records can contain addresses;
- ECS: off;
- upstream: exactly `https://dns10.quad9.net/dns-query` unless later current authority changes it;
- operational statistics: minimum anonymized aggregate statistics with **24-hour / `1d` retention** under current authority;
- browsing/query/activity-history metrics: prohibited;
- exceptional query diagnostics: off by default and only a separately authorized, ticket-linked, time-bounded, access-controlled, deletion-verified operation.

Any existing script/helper that asserts a conflicting historical privacy field must be corrected/revalidated before composition into the recovery path.

## 14. Relationship to existing repository scripts

| Existing artifact | TSK-0445 treatment |
|---|---|
| `install-adguard.sh` | Reuse candidate for pinned v0.107.79 direct-host installation because it already checks Ubuntu 24.04, release SHA, archive safety, service state and refuses unrecognized installations. Revalidate against current TSK-0412/TSK-0413 before final composition. |
| `clean-recovery-drill-runtime.sh` | Historical drill reference only. It demonstrates useful failure-safe and test patterns but currently encodes stale `statistics=false` and target-specific identities; do not call it as production recovery orchestration. |
| `create-encrypted-config-backup.sh` | Historical/current backup implementation reference only until its privacy preflight is reconciled from `statistics=false` to the current TSK-0413 safe projection; do not let it override desired state. |
| `TSK-0446-RECOVERY-SCOPE-CONTRACT.md` | Authoritative recovery/RTO boundary consumed by this design. |
| TSK-0413 recovery bundle | Authoritative non-secret desired-state bundle subject to checksum/compatibility verification. |
| TSK-0518 independent recovery acceptance plan | Downstream QA acceptance map; this design provides the hooks it requires but does not claim those target checks have run. |

The implementation may reuse small verified primitives, but `deploy_or_recover.sh` remains the single production orchestration entry point so error, retry, idempotency, rollback and evidence semantics cannot diverge across several top-level scripts.

## 15. Verification hooks for downstream independent acceptance

The production script must expose enough stable, privacy-safe outputs for independent QA to prove the recovery surface. At minimum:

- `--check` result and exact authority/release/bundle identity;
- `--apply` start/stop timestamps and final verification summary;
- `--verify` machine-readable/stable PASS/FAIL lines for host/version/schema, bundle, listeners/firewall/admin, upstream/ECS, privacy, filter/allowlist, TLS/hostname, encrypted DNS health, service restart and prohibited-data/secret checks;
- explicit no-op evidence on second `--apply`;
- stable error classes for failure-injection assertions;
- rollback/uncertain outcome status;
- `--remove` verification result where that path is in scope.

These hooks map to the TSK-0518 RA-01…RA-20 independent acceptance matrix. **They are hooks, not acceptance evidence.** Actual QA must still execute against the exact clean target and prove the behavior independently.

## 16. RTO instrumentation

The implementation records the TSK-0446 clock exactly:

- clock starts immediately before the first recovery/deployment command after the owner-provided VM handoff prerequisites are proven;
- package installation, protected-input consumption, configuration, firewall, TLS, service and verification time remain inside the clock;
- clock stops only after all applicable final checks and external encrypted-DNS health pass;
- no pause is allowed for an input discovered missing after start;
- UTC start/stop and elapsed seconds are emitted without sensitive data.

The approximate 30-minute target is a later measured acceptance criterion. TSK-0445 does not claim it has been met.

## 17. ShellCheck and static quality contract

Before implementation acceptance:

- `shellcheck` runs with no unwaived error-class finding on `deploy_or_recover.sh` and any sourced project library;
- every disable directive is narrow, adjacent and justified;
- `bash -n` passes;
- a static secret scan shows no credential/private-key material;
- tests cover malformed config, unknown option/key, unsafe path, unsupported host/version, checksum mismatch, missing/unsafe secret metadata, concurrent invocation, no-op second apply, bounded transient retry, ambiguous-effect reconciliation, failed verification, rollback and remove guard;
- test fixtures contain no real secrets or DNS browsing data.

## 18. ACC-0445 mapping

| ACC-0445 requirement | Design evidence | Status |
|---|---|---|
| minimal | One direct-host entry point; no orchestration/microservice/second state system | PASS CANDIDATE |
| auditable | exact release/bundle identity, structured privacy-safe journal, stable actions/errors, final verification | PASS CANDIDATE |
| non-interactive after approved inputs | four explicit modes; root-owned data config and external secret paths; no prompts | PASS CANDIDATE |
| idempotent | inspect/plan/apply/verify loop, no-op accepted state, local lock, reconciliation after interruption | PASS CANDIDATE |
| shellcheck-compatible | strict Bash contract, arrays/quoting, no eval/generated shell, explicit static-quality gate | PASS CANDIDATE |
| secret-safe | no CLI secret values, no sourcing config as shell, root-only external secret paths, `umask 077`, no `set -x`, redacted journal | PASS CANDIDATE |
| immutable code separated from environment secrets/config | Git code/bundle separated from `/etc/usesafeweb/recovery.env` and `/etc/usesafeweb/secrets/` | PASS CANDIDATE |
| logging/errors/retries | structured logs, stable error classes, bounded retry classification, no blind ambiguous retry | PASS CANDIDATE |
| rollback | minimum current-run snapshot, atomic writes, bounded compensation, rollback verification, `uncertain` fail-closed result | PASS CANDIDATE |
| verification hooks | common `--verify` contract plus stable outputs for downstream TSK-0518 independent target acceptance | PASS CANDIDATE |

## 19. Non-inference and next implementation boundary

This design does **not** prove:

- that `deploy_or_recover.sh` exists yet;
- that any current helper is safe to compose without reconciliation;
- that ShellCheck or script tests have passed;
- that a clean Ubuntu server has been deployed/recovered;
- that TLS/firewall/DNS/privacy behavior works on a target;
- that backup/restore works under current TSK-0413 statistics semantics;
- that the ~30-minute RTO has been achieved;
- that RSK-0048 is closed;
- that LG-07 or any later gate is PASS.

The next implementation task(s) must build the script from this contract, reconcile stale helpers before reuse, test it, and then hand the exact candidate to the independent clean-server acceptance defined by TSK-0518/INT-0025.