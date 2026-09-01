# TSK-0446 — End-to-end AdGuard recovery scope and RTO contract

**Task:** TSK-0446  
**Acceptance:** ACC-0446  
**Contract version:** 1.0.0  
**Date:** 2026-09-01  
**Owner:** Cloud / Platform Engineering  
**Authority:** A3 / AUTO_ALLOWED  
**Status:** candidate frozen contract pending independent repository verification

## 1. Decision and authority

This contract freezes the current end-to-end recovery boundary for the single UseSafeWeb AdGuard/DNS node. It does not perform a restore, deploy production, create Azure resources, or claim a measured recovery result.

The current governing inputs are:

- current WBS `TSK-0446 / ACC-0446 / VER-0446 / EVD-0446`;
- current `LG-06` PASS, which unlocks L5 execution;
- current `TSK-0413` PASS and the versioned recovery-consumable bundle at `infrastructure/adguard-server/tsk-0413-bundle-v1/`, version `1.0.0`;
- `DEC-0016` owner-approved privacy-first DNS baseline;
- `REQ-0049` through `REQ-0054`, `CON-0004`, `CON-0005`, `RSK-0048`, and interfaces `INT-0014`, `INT-0018`, `INT-0025`, and `INT-0026`.

If any later source conflicts with this contract, the higher/current authority wins and recovery fails closed until the contract is reverified.

## 2. Recovery objective

From an owner-provided, reachable, supported **fresh Ubuntu 24.04 LTS** DNS VM handoff, restore a verified operational UseSafeWeb DNS service by deterministic direct-host automation, using the current versioned non-secret desired state plus protected runtime/secret inputs, while preserving the approved privacy, security, filter, endpoint, and administration boundaries.

The target is approximately **30 minutes** from recovery execution start to externally verified service restoration. This is the accepted design/RTO target, not evidence that a clean-server recovery has already achieved it.

## 3. RTO measurement contract

### Start

The RTO clock starts immediately before the first recovery/deployment command is executed on the owner-provided fresh VM, after these owner-handoff prerequisites have been objectively established:

1. the VM is reachable through the approved administration/deployment path;
2. Ubuntu 24.04 LTS is present and supported;
3. required root/sudo execution authority is available without exposing credentials in Git or logs;
4. the exact repository/release commit and TSK-0413 bundle are available;
5. required protected secret/recovery inputs have been supplied through the approved external mechanism.

Azure VM creation, subscription/resource-group setup, region selection, network-resource creation, and other Azure control-plane provisioning are outside the recovery clock because `CON-0004` makes those owner-managed pre-handoff acts.

### Stop

The clock stops only when all applicable acceptance checks below pass on the rebuilt service and the external encrypted-DNS health probe succeeds. A process merely starting, a package install finishing, or a backup restoring does not stop the clock.

### Timing rules

- Package downloads, AdGuard installation, configuration application, firewall/service setup, protected-input consumption, certificate/TLS restoration, filter activation, restarts, and verification time are inside the clock once recovery starts.
- The timer is not paused for a missing input discovered after start; that is a recovery failure/deviation.
- Record UTC start, UTC stop, elapsed seconds, release commit, bundle version, exact target identity, and every material deviation.
- A result above approximately 30 minutes is not silently accepted; it triggers `RSK-0048` treatment and remains a failed/conditional recovery result until disposition is recorded.
- **No timed clean-server drill is claimed by TSK-0446.** Actual timing is proved only by the downstream target-environment recovery acceptance/drill.

## 4. Required recovery inputs

### Versioned, non-secret inputs from Git

- exact approved recovery/deployment scripts under `/infrastructure/adguard-server`;
- TSK-0413 bundle version `1.0.0`, including `SHA256SUMS`, `bundle.json`, `AdGuardHome.public-fragment.yaml`, endpoint contract, filter reference, allowlist, compatibility declaration, and `verify_bundle.py`;
- exact release/repository commit identifier;
- current non-secret firewall/network/service expectations and test definitions.

### Protected inputs outside Git

- administrator authentication material or protected input required to recreate it;
- any secret-bearing server-managed configuration approved for recovery;
- TLS private key/certificate material or protected certificate-recovery mechanism used by the current same-host encrypted-DNS proxy design;
- any owner-managed Azure-native backup/snapshot reference required by the applicable recovery path;
- deployment access credentials/keys.

No password, password hash export, private key, certificate private material, bearer/API token, participant record, raw DNS query history, browsing/activity history, or identifiable client-history dataset may be committed to Git or emitted in workflow logs/evidence.

## 5. Clean-server assumptions

The supported primary recovery target is a fresh owner-provided Ubuntu 24.04 LTS VM for the DNS role. Recovery automation may assume only:

- supported Ubuntu 24.04 LTS and working base networking/DNS sufficient to fetch approved packages/repository assets;
- owner-authorised root/sudo access;
- owner-managed Azure handoff already completed;
- protected inputs are accessible through the approved external mechanism.

It must not assume AdGuard Home, filters, reverse proxy/TLS state, firewall rules, local secrets, application directories, or prior recovery artifacts already exist.

The implementation is **direct-host by default**. Docker/orchestration is excluded unless a later verified component requires it and authority explicitly reopens that design.

## 6. End-to-end recovery scope

A compliant recovery must cover and verify every applicable area below.

### Host and packages

- verify Ubuntu 24.04 LTS and expected DNS-node role;
- install only required, approved packages by deterministic/idempotent direct-host steps;
- fail safely on unsupported OS/version or package failure;
- record exact installed AdGuard version and recovery release commit.

### AdGuard Home

- install **AdGuard Home v0.107.79** and require configuration schema `34` for the current bundle;
- bind recovery compatibility to official tag commit `05ba17b282da1c4393d6a4ba4db0cf519194a362` as recorded by TSK-0413;
- fail closed rather than silently consuming the bundle with another AdGuard/schema version.

### Configuration and protected state

- verify TSK-0413 `SHA256SUMS` before consumption and run its `verify_bundle.py`;
- never treat a raw server backup as current desired-state authority;
- if a protected raw/server-managed configuration is restored, merge/overlay only through the approved recovery procedure so the **final safe-field projection matches the current TSK-0413 bundle**;
- inject secret-bearing fields from the external protected mechanism; never synthesize or restore them from Git;
- after merge, independently verify safe fields before public service exposure.

### Network and firewall

- keep AdGuard plain DNS and administration listeners loopback/private according to the current bundle;
- expose only the encrypted-DNS service surface required by the current endpoint contract;
- administration remains non-public and authenticated;
- no Azure control-plane firewall/NSG/resource creation is performed by this recovery contract; actual owner-provided exposure is inspected and must match the service boundary before acceptance.

### DNS endpoint and encrypted protocols

- preserve service identity `UseSafeWeb DNS`;
- preserve `dns.usesafeweb.com` and DoH `https://dns.usesafeweb.com/dns-query`;
- preserve Android Private DNS / DoT hostname semantics for `dns.usesafeweb.com`;
- keep the public resolver path direct to the approved Azure DNS node, not the website CDN/admin surface;
- external verification must prove resolution and encrypted endpoint health, not only localhost process health.

### TLS

- current TSK-0413 endpoint contract uses a **same-host path-restricted reverse proxy** for public encrypted-DNS TLS termination while AdGuard internal TLS remains disabled;
- recover/obtain certificate/private material only through the protected external mechanism;
- verify trusted certificate chain, hostname/SAN for `dns.usesafeweb.com`, validity, and encrypted endpoint behavior;
- never commit or log TLS private material;
- admin UI must not become public as a side effect of TLS recovery.

### Filters and allowlist

- restore exactly the current TSK-0413 filtering baseline: one initial active official `AdGuard DNS filter` (`filter_1.txt`);
- initial versioned allowlist is empty;
- do not restore dormant/historical third-party lists or stale user rules;
- later exceptions must remain evidence-bound, documented, reversible, and separately versioned.

### Privacy

Final recovery state must match current `DEC-0016` and TSK-0413:

- persistent raw query logging: **off**;
- file query logging: **off**;
- exceptional operational query diagnostics: not enabled by default; if separately authorised later, maximum 24 hours and deleted after use;
- operational statistics: only minimum anonymized aggregate statistics, enabled with **24-hour / `1d` retention** in the current TSK-0413 bundle;
- identifiable per-client statistics/history: excluded;
- client-IP anonymization: **on** wherever records can contain it;
- ECS: **off**;
- browsing/query/activity-history metrics: prohibited;
- no recovery source may reintroduce raw query history, participant data, client history, or other prohibited telemetry.

### Security and administration

- AdGuard administration stays at `127.0.0.1:3000`, non-public and authenticated;
- administrator credentials come only from the external secret/recovery mechanism;
- file permissions, service ownership, secret paths, and process exposure must be rechecked after restore;
- checksums/version mismatches, secret leakage, unexpected listeners, or public admin access fail recovery acceptance.

### Startup and service management

- AdGuard and the encrypted-DNS proxy/TLS components required by the approved topology must be enabled/recoverable for host restart as designed;
- service-start ordering and restart behavior must not create a public partially configured/unsafe service window;
- repeat execution must be idempotent or detect existing accepted state before mutation.

### Verification and health

At minimum, downstream clean-server acceptance must prove:

1. host/version/schema identity;
2. bundle checksum and compatibility;
3. final safe configuration projection;
4. listener/firewall/admin exposure;
5. upstream exactly `https://dns10.quad9.net/dns-query` and ECS off;
6. approved filter/allowlist state;
7. privacy invariants above;
8. TLS certificate/hostname/chain and encrypted endpoint behavior;
9. successful allowed-domain resolution and expected blocked-domain behavior using the privacy-safe regression set;
10. external DoH health and applicable DoT/private-DNS health;
11. restart/startup recovery;
12. no prohibited secrets/history in Git, logs, evidence, or recovered query-history paths;
13. exact elapsed RTO measurement and deviations.

A backup restore, process `active` state, or localhost-only DNS response is insufficient by itself.

## 7. Backup/restore and stale-state reconciliation

`BACKUP_SCOPE_POLICY.md` is useful for encryption, access, retention, location, deletion, and prohibited-data boundaries, but its recorded historical live preflight required `statistics=false` before the 2026-09-01 owner approval. That historical live setting does **not** override current `DEC-0016` or the accepted TSK-0413 desired state.

Therefore:

- a protected raw configuration backup is an input, not desired-state authority;
- query logs, raw DNS/domain history, identifiable client statistics/history, participant data, and stale diagnostic artifacts remain excluded from recovery;
- final recovered non-secret settings must be reconciled to TSK-0413, including the current anonymized aggregate `1d` statistics setting;
- any later backup-creation workflow that still requires `statistics=false` must be revalidated/reconciled before being used against the new desired state;
- Azure-native backup/restore remains owner-managed at the control plane but must be included in downstream end-to-end recovery acceptance when an applicable owner-managed backup target is supplied;
- backup success alone never proves end-to-end recovery.

This is a current-authority reconciliation inside TSK-0446; it does not mark TSK-0429 or TSK-0430 PASS and does not mutate their WBS state.

## 8. Failure-safe behavior and rollback

Recovery must leave the service **disabled/not accepted** when any critical condition is uncertain or failed, including:

- unsupported Ubuntu/AdGuard/schema;
- bundle checksum/version failure;
- missing protected input after recovery start;
- secret/private-key leakage;
- unexpected public listener/admin exposure;
- privacy invariant failure;
- filter/upstream/ECS mismatch;
- TLS/hostname failure;
- external DNS health failure;
- incomplete/ambiguous destructive or restore result.

Do not blindly replay an ambiguous non-idempotent restore. Inspect durable/target outcome first. Use a known-good protected backup/manual emergency runbook only if it preserves current privacy/security invariants; otherwise keep the service unavailable/uncertain until corrected and retested.

## 9. Required recovery outputs/evidence

Each actual clean-server recovery acceptance must retain privacy-safe evidence containing:

- exact Git/source commit and recovery-system version;
- TSK-0413 bundle version and checksum identity;
- target role/OS/region evidence without secrets;
- installed AdGuard version/schema;
- safe configuration projection and invariant test results;
- network/listener/firewall and admin-exposure results;
- TLS/endpoint and external DNS health results;
- filter/allowlist results;
- restart/idempotency/failure-injection results as applicable;
- UTC start/stop, elapsed seconds, ~30-minute target result;
- deviations, rollback/retry disposition, verifier, run/job identifiers.

Evidence must never include raw DNS queries, browsing/activity history, participant data, plaintext credentials, password hashes, tokens, or private keys.

## 10. Explicit exclusions

TSK-0446 does not:

- create/configure Azure VMs, subscriptions, resource groups, NSGs, vaults, storage accounts, or other Azure control-plane resources;
- change public DNS records or activate production/user traffic;
- perform the actual clean-server timed recovery drill;
- authorise real participants or market activation;
- restore browsing/query/activity history or identifiable client history;
- add Docker/orchestration;
- expand AdGuard into broad customer DNS administration;
- make the optional Version-1 account capability mandatory for core DNS use.

## 11. Acceptance mapping

| ACC-0446 area | Contract coverage |
|---|---|
| host/packages | Sections 5–6 |
| AdGuard | exact v0.107.79/schema 34 compatibility and fail-closed install |
| configuration | TSK-0413 checksum/merge/final safe-field projection |
| network/firewall | private plain/admin listeners; encrypted public surface only; actual exposure verification |
| DNS endpoint | `dns.usesafeweb.com`, DoH `/dns-query`, applicable DoT/private-DNS health |
| TLS | protected external key/cert input; same-host path-restricted proxy; hostname/chain validation |
| filter | official AdGuard DNS filter only; versioned empty initial allowlist |
| security | secret-safe inputs, private authenticated admin, version/listener/permission checks |
| privacy | DEC-0016 + TSK-0413 querylog/statistics/anonymization/ECS/history invariants |
| startup | safe service ordering, restart behavior, idempotent/detect-existing execution |
| verification/health | exact configuration + functional/negative/external health/restart evidence |
| ~30-minute restoration | precise start/stop clock, no timer pausing after start, elapsed result required downstream |

## 12. Disposition

This artifact freezes the **measurement and recovery contract** required by TSK-0446. It deliberately separates contract acceptance from the later clean-server target-environment drill. Passing TSK-0446 therefore means the end-to-end scope, inputs, outputs, safety boundaries, verification set, and ~30-minute measurement rule are complete and reproducible; it does **not** mean a fresh server has already been restored inside 30 minutes.
