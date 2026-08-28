# TSK-0431 — Project-Controlled Clean Recovery Drill Evidence

**Task:** TSK-0431 — Test pilot restore or rebuild procedure  
**Date:** 2026-08-28  
**Target:** isolated recovery VM `adguartestdvm` / runner `adguartestdvm_correct`  
**Routing label:** `rec-v1`

## Evidence boundary

This record binds the completed target recovery acceptance to direct GitHub Actions runtime evidence. It does not claim that an Azure control-plane restore was exercised.

Primary recovery run:

- workflow run `33173972042`;
- recovery job `98857724228`;
- workflow source commit `d8111ed4d7d0ef6bd587ef08bd64552874ed24d5`;
- recovery runtime blob `97035f688170322bf22e8f584b514f463861c10b`;
- owner Azure Backup readiness evidence blob `fb846d5ab9a3ed3f4b52976273c92653d73db925`;
- approved AdGuard configuration blob `e9975c4e75c2a68131f049da942468d8d1952d8d`;
- pinned installer blob `5891f79b531ac2f0366374a8f4bec8fa560a2496`;
- pinned admin initializer blob `0fa0b3481d9b7173649c72606b40642c278e9c32`.

The job log directly identified runner `adguartestdvm_correct` and machine `adguartestdvm`. The runtime had already required the accepted machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852` and Azure IMDS identity before any recovery-target mutation.

## Recovery acceptance

The recovery job reached and emitted `TSK_0431_PROJECT_CONTROLLED_DRILL=PASS` after completing its functional, privacy, security and timing assertions.

A separate read-only post-run evidence capture was then executed on the same uniquely routed recovery runner:

- capture run `33174075020`;
- capture job `98858073703`;
- runner `adguartestdvm_correct` / machine `adguartestdvm`;
- accepted machine-id fingerprint rechecked before reading the summary;
- summary content restricted to an explicit privacy-safe allow-list;
- AdGuard and Nginx active state and loopback listeners rechecked after the recovery job.

The captured recovery summary was:

- `azure_location=westeurope`
- `recovery_vm_id=6e92a026-964c-4118-8312-f1d31c6ff4d2`
- `prior_project_state_cleanup=PASS`
- `firewall_public_service_ports=22_only`
- `approved_config_reconstructed=PASS`
- `nginx_local_tls_listeners=PASS`
- `local_doh_encrypted_resolution=PASS`
- `local_dot_encrypted_resolution=PASS`
- `filter_block_exception_rollback=PASS`
- `privacy_persistence=PASS`
- `admin_and_firewall_fail_safe=PASS`
- `elapsed_seconds=12`
- `recovery_target_health=PASS`
- `azure_backup_owner_evidence=PASS`
- `azure_native_restore_exercised=false`
- `project_controlled_rebuild=PASS`
- post-run health recheck: `PASS`

The measured project-controlled recovery path completed in **12 seconds**, below the approximately 30-minute recovery target. The timer included cleanup of prior project-controlled partial application state on the isolated recovery VM.

## Verified behavior

The accepted target evidence proves:

- clean reconstruction of pinned AdGuard Home v0.107.79 and the approved safe configuration;
- Quad9 dns10 upstream, ECS disabled, query/file logging disabled, statistics disabled, client-IP anonymisation enabled and no persistent client records;
- authenticated loopback-only admin path with unauthenticated control access denied;
- default-deny host firewall with only SSH exposed publicly during the isolated drill;
- loopback Nginx TLS endpoints for DoH and DoT;
- local encrypted DoH and DoT resolution success;
- synthetic block -> narrow exception -> exact rule rollback success;
- no persistent query-log output and disabled statistics after the test;
- AdGuard and Nginx healthy after acceptance and again during the separate post-run health recheck.

No participant browsing/domain history, participant identity, password, token, private key, certificate private material or raw DNS query data is stored in this evidence.

## Post-acceptance cleanup deviation

After `TSK_0431_PROJECT_CONTROLLED_DRILL=PASS` had already been emitted, the recovery job returned exit code 1 while deleting `/tmp/t0431-doh.bin`. The DoH verification used root privileges to preserve the root-only `0700` recovery-certificate directory, so that temporary output file was root-owned while the final cleanup command ran as the runner user. This happened **after all recovery acceptance checks and the PASS marker**, and the separate post-run capture subsequently proved the accepted summary and target health remained intact.

This cleanup defect therefore does not invalidate the project-controlled recovery acceptance. It is a workflow hygiene defect, not a failed ACC-0431 functional/privacy/timing criterion. No production mutation occurred.

## Azure-native boundary and stable disposition

The Project Owner previously reported Azure Backup ready with status Successful and approved treating Azure Backup setup/readiness as complete. The project-controlled recovery drill did **not** execute an Azure recovery-point restore: `azure_native_restore_exercised=false`.

**Project-controlled recovery drill: PASS.**  
**TSK-0431 overall: WAITING only on direct owner evidence that an Azure-native recovery-point restore was actually exercised successfully, unless the Project Owner explicitly changes that literal REQ-0052 requirement through governed change control.**
