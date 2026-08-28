#!/usr/bin/env bash
set -Eeuo pipefail
source /tmp/t0431-summary.env
workflow_blob="$(git hash-object .github/workflows/adguard-clean-recovery-drill.yml)"
state_blob="$(git hash-object CURRENT_STATE.md)"
cat > TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md <<EOF
# TSK-0431 — Project-Controlled Clean Recovery Drill Evidence

**Task:** TSK-0431 — Test pilot restore or rebuild procedure  
**Date:** 2026-08-28  
**Target:** isolated recovery VM \`adguartestdvm\` / runner \`adguartestdvm_correct\`

## Inputs

- Workflow source commit: \`${GITHUB_SHA}\`
- Workflow blob: \`${workflow_blob}\`
- Runtime-state blob at checkout: \`${state_blob}\`
- Owner Azure Backup readiness evidence blob: \`fb846d5ab9a3ed3f4b52976273c92653d73db925\`
- Approved AdGuard configuration artifact blob: \`e9975c4e75c2a68131f049da942468d8d1952d8d\`
- Pinned AdGuard installer blob: \`5891f79b531ac2f0366374a8f4bec8fa560a2496\`
- Pinned admin initializer blob: \`0fa0b3481d9b7173649c72606b40642c278e9c32\`

## Fresh target identity

The drill asserted the corrected independent recovery VM identity before mutation: Azure VM ID \`${recovery_vm_id}\`, location \`${azure_location}\`, Ubuntu 24.04 LTS, and the previously accepted machine-id fingerprint. Production VM \`adguardvm\` was not the execution target.

## Timed rebuild result

Project-controlled clean rebuild elapsed time: **\`${elapsed_seconds}\` seconds**, below the approximately 30-minute recovery target.

The drill reconstructed the service from pinned/versioned project artifacts and fresh local secret generation, then proved:

- approved AdGuard v0.107.79 installation and service startup;
- approved safe configuration reconstruction with Quad9 dns10, ECS off, query/file logging off, statistics off, IP anonymisation on, no persistent clients, conservative filtering enabled;
- admin API loopback-only/authenticated and unauthenticated access denied;
- firewall remained default-deny with public inbound service limited to SSH during the isolated drill;
- local test TLS terminated only on loopback using an ephemeral one-day recovery-test certificate whose private key never left the recovery VM;
- DoH resolution through \`https://dns.usesafeweb.com/dns-query\` semantics on loopback: **PASS**;
- DoT resolution through port 853 semantics on loopback: **PASS**;
- synthetic block -> narrow exception -> exact rules rollback: **PASS**;
- post-test query-log output empty, no non-empty querylog files, statistics disabled with zero top clients/query count: **PASS**;
- AdGuard and Nginx healthy after acceptance checks: **PASS**.

Safe markers: \`approved_config_reconstructed=${approved_config_reconstructed}\`, \`local_doh_encrypted_resolution=${local_doh_encrypted_resolution}\`, \`local_dot_encrypted_resolution=${local_dot_encrypted_resolution}\`, \`filter_block_exception_rollback=${filter_block_exception_rollback}\`, \`privacy_persistence=${privacy_persistence}\`, \`admin_and_firewall_fail_safe=${admin_and_firewall_fail_safe}\`, \`recovery_target_health=${recovery_target_health}\`.

No participant DNS/domain history, participant identity, password, token, private key, certificate private material, or raw query data is stored in this evidence.

## Azure-native boundary

The Project Owner directly reported Azure Backup ready with status Successful and explicitly approved the Azure Backup readiness/setup step as done. That owner-managed prerequisite is recorded separately.

The project-controlled drill **did not execute an Azure control-plane restore**; \`azure_native_restore_exercised=${azure_native_restore_exercised}\`. CON-0004/CON-0019 keep that consequential Azure restore action owner-managed. Therefore the autonomous rebuild/functional/privacy/time portion of TSK-0431 is proven, but the literal REQ-0052 Azure-native *restore* exercise must not be fabricated.

## Stable disposition

**Project-controlled recovery drill: PASS.**  
**TSK-0431 overall: WAITING only on direct owner evidence that an Azure-native restore/recovery-point restore was actually exercised successfully, unless the owner explicitly changes that requirement through governed change control.**

No production service or Azure control-plane resource was mutated by this workflow.
EOF
git config user.name 'UseSafeWeb Recovery Bot'
git config user.email 'actions@users.noreply.github.com'
git add TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md
git commit -m 'evidence: record TSK-0431 clean recovery drill'
git push origin HEAD:main