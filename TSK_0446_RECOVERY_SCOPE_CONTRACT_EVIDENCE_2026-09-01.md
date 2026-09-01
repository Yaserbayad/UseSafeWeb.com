# TSK-0446 — Recovery scope and RTO contract evidence — 2026-09-01

**Task:** TSK-0446  
**Acceptance:** ACC-0446  
**Verification:** VER-0446  
**Evidence:** EVD-0446  
**Disposition:** PASS at the recovery-contract boundary

## Authoritative outcome

The Version-1 end-to-end recovery scope and approximately-30-minute RTO measurement contract is frozen and independently verified. This PASS accepts the contract required to design/implement recovery; it does **not** claim that a fresh server has already been restored, that the RTO has already been achieved in a target environment, that production is activated, or that LG-07 passes.

## Exact artifact and source

- Contract: `infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md`
- Contract version: `1.0.0`
- Contract Git blob: `18d998e2406e801c7ac08f4daa2e3b763ea9b523`
- Original contract source commit: `18f90a9ef9a27ca2e3ce1917e1d2b35e8b91478c`
- Corrected verifier/source commit independently tested: `6214ac817ed3279561495f73212bd7e2e9acfc6b`
- Verifier: `.github/scripts/verify_tsk0446_recovery_scope_20260901.py`
- Verifier blob at PASS: `42968bfe96ef9d8a7d7f86a4d6767a2df4f754a3`
- Workflow: `.github/workflows/verify-tsk0446-recovery-scope-20260901.yml`
- Workflow blob: `d2a856a180ed2bb6940537ce3d6f37c17be31bd8`

## Dependency and current authority

- `LG-06` is current PASS and unlocks L5.
- TSK-0446 current WBS authority: `L5 / CRITICAL / A3 / AUTO_ALLOWED`.
- Sole current WBS hard dependency: `TSK-0413`.
- TSK-0413 is current PASS with bundle `infrastructure/adguard-server/tsk-0413-bundle-v1/` version `1.0.0` and prior independent run/job `33500597612 / 99832778403`.
- Current owner-approved privacy authority is `DEC-0016`, as reconciled after `APPROVE TSK-0413 RECOMMENDED PRIVACY-FIRST ADGUARD BASELINE`.

## ACC-0446 coverage

Current ACC-0446 requires the contract to cover host/packages, AdGuard, configuration, network/firewall, DNS endpoint, TLS, filter, security, privacy, startup, verification/health, and measurement of actual service restoration within approximately 30 minutes.

The accepted contract explicitly defines:

1. fresh supported Ubuntu 24.04 LTS host assumptions and owner-managed Azure handoff boundary;
2. direct-host package/install behavior and fail-safe unsupported-state handling;
3. AdGuard Home `v0.107.79`, configuration schema `34`, official tag commit `05ba17b282da1c4393d6a4ba4db0cf519194a362`;
4. checksum verification and recovery reconciliation to the exact TSK-0413 safe desired-state projection;
5. private/plain/admin listener and public encrypted-DNS network/firewall boundary;
6. `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query` endpoint identity;
7. protected TLS material and same-host path-restricted reverse-proxy topology, with AdGuard internal TLS disabled;
8. official AdGuard DNS filter only initially, empty versioned allowlist, no stale third-party/user-rule restoration;
9. current privacy baseline: persistent query/file logging off, exceptional diagnostics not enabled by default and at most 24 hours if separately authorised, only minimum anonymized aggregate operational statistics at `1d`, identifiable client history excluded, client-IP anonymization on, ECS off, browsing/query/activity history prohibited;
10. private authenticated administration and secret-safe restore behavior;
11. safe startup/restart/idempotency requirements;
12. external encrypted-DNS, configuration, security/privacy, filter, restart, and health acceptance checks;
13. a precise RTO clock: start immediately before the first recovery/deployment command after owner-handoff prerequisites are established; stop only when all applicable acceptance checks and external encrypted-DNS health pass; no timer pause for a missing input discovered after start; record UTC start/stop and elapsed seconds; above approximately 30 minutes invokes RSK-0048 treatment.

The contract therefore defines how **actual** service restoration is measured against the ~30-minute target. The actual clean-server timed execution is deliberately downstream target-environment evidence and is not invented by this task.

## TSK-0413 privacy-first baseline incorporated

The independent verifier re-read and checked the current TSK-0413 bundle. At PASS it proved:

- bundle version `1.0.0`;
- AdGuard Home `v0.107.79`, schema `34`;
- upstream exactly `https://dns10.quad9.net/dns-query`;
- ECS disabled;
- client-IP anonymization enabled;
- query logging disabled and file logging disabled;
- minimum anonymized aggregate statistics enabled at `1d` retention;
- exactly one initial official AdGuard DNS filter;
- empty whitelist/user rules;
- private non-public admin binding;
- same-host path-restricted public TLS proxy contract.

The contract also explicitly reconciles the older `BACKUP_SCOPE_POLICY.md` live preflight that required `statistics=false`: that older observation is historical and cannot override the current owner-approved DEC-0016/TSK-0413 desired state. A raw protected backup is an input, not desired-state authority.

## Independent verification evidence

- Initial workflow run/job: `33503802182 / 99842993467` — **FAIL**, correctly fail-closed.
- Exact initial deviation: verifier referenced nonexistent WBS column `Layer`, producing `KeyError: 'Layer'`; no product/recovery assertion failed and no PASS/state mutation occurred.
- Canonical WBS header is `Lifecycle_Stage`.
- Corrective commit: `6214ac817ed3279561495f73212bd7e2e9acfc6b`, changing only that parser binding.
- Final workflow run/job: `33504115232 / 99843993787` — **SUCCESS**.
- Final verifier output: `TSK_0446_RECOVERY_SCOPE_CONTRACT_VERIFY=PASS`.
- Final output also records `contract_version=1.0.0`, `dependency=TSK-0413`, `bundle_version=1.0.0`, `adguard_home_version=v0.107.79`, `rto_target=approximately_30_minutes`, `target_timed_drill_claimed=false`.
- Master-plan validator: **PASS** with 641 tasks, 858 dependency edges, 0 broken links, and 0 generated missing task IDs.
- Durable automated marker: `TSK_0446_RECOVERY_SCOPE_CONTRACT_AUTOVERIFY_2026-09-01.md`.
- Marker blob: `f5fe287aac8a40054cc9175b95b85b8f9a63768d`.
- Marker commit/read-back: `e77d287488caba1d279a920e69d0e7a6d404c444` — PASS.

## Verification disposition

`VER-0446` is satisfied against the exact versioned contract/repository environment by deterministic checklist verification, predecessor binding, current-authority checks, the TSK-0413 self-verifier, master-plan validation, diff checks, and an independent GitHub Actions reviewer run. The one implementation defect found was isolated to the verifier's CSV column binding, was corrected from canonical source evidence, and the complete verification was rerun successfully.

## Non-inference / downstream boundary

This evidence does **not** establish:

- a timed clean-server rebuild/restore result;
- actual ~30-minute RTO attainment;
- live deployment of the recovery system;
- Azure control-plane provisioning;
- production/public/user activation;
- TSK-0445, TSK-0447, TSK-0518, LG-07, or any later gate/task PASS.

Those outcomes require their own current dependencies, authority and target evidence.

## Final disposition

**TSK-0446: PASS** at its defined L5 recovery-contract boundary. All current applicable ACC-0446 contract criteria are proven, current TSK-0413 privacy-first authority is incorporated, the verification defect was corrected and rerun to SUCCESS, and the actual clean-server timed restoration remains explicitly downstream evidence rather than an inferred result.
