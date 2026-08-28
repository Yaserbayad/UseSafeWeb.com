# TSK-0431 — Corrected Recovery Runner Identity Evidence

**Task:** TSK-0431 — Test pilot restore or rebuild procedure  
**Acceptance:** ACC-0431  
**Date:** 2026-08-28

## Owner change being verified

The Project Owner reported that the recovery runner was corrected and is now registered in GitHub as `adguartestdvm_correct`.

TSK-0431 requires a genuinely independent clean Ubuntu 24.04 LTS Azure recovery target before any rebuild/restore mutation. Runner name alone is not sufficient, so the project executed two simultaneous read-only self-hosted jobs to force both available runners to identify their underlying machines.

## Dual-runner fingerprint verification

Workflow: `.github/workflows/governance-task-row-inspect.yml`  
Commit: `95207081ba80db3ea2bb122246ccf5797da9a6b3`  
Run: `33161281851`  
Result: **PASS**

### Production runner

Job: `98816079276`  
Runner: `adguardvm`

Observed:

- machine hostname: `adguardvm`;
- Ubuntu 24.04;
- machine-id SHA-256: `e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`;
- Azure VM name: `adguardvm`;
- Azure region: `westeurope`;
- Azure VM ID: `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`;
- AdGuard Home: active;
- Nginx: active.

### Corrected recovery runner

Job: `98816079544`  
Runner: `adguartestdvm_correct`

Observed:

- machine hostname: `adguartestdvm`;
- Ubuntu 24.04;
- machine-id SHA-256: `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`;
- Azure VM name: `adguartestdvm`;
- Azure region: `westeurope`;
- Azure VM ID: `6e92a026-964c-4118-8312-f1d31c6ff4d2`;
- AdGuard Home: inactive;
- Nginx: inactive.

The Azure VM IDs and machine-id hashes are different. The corrected runner is therefore a genuinely separate clean Ubuntu 24.04 LTS West Europe VM and is suitable as the recovery test host subject to the remaining recovery-contract inputs.

## Remaining authoritative recovery condition

Authoritative contract inspection run `33161362741` / job `98816346637` confirms:

- ACC-0431 requires the test target to become functional, pass encrypted-DNS and privacy checks, with recovery time/issues recorded;
- REQ-0052 requires the timed clean-server drill to include host baseline, packages, AdGuard, server-managed configuration recovery, firewall/network, endpoint, TLS, filters, privacy, startup, **Azure-native backup/restore**, verification, and health;
- CON-0004 and CON-0019 keep Azure control-plane provisioning/configuration owner-managed.

No Azure control-plane connector is available to project automation, and no current durable evidence identifies an owner-managed Azure-native backup/restore interface or restoration step for this test VM.

## Stable outcome

**TSK-0431: WAITING.**

The prior machine-identity blocker is resolved. The deterministic remaining resolution condition is: the owner identifies/provides the Azure-native backup/restore path or evidence needed by REQ-0052. After that, the project may execute the timed clean-server recovery drill on `adguartestdvm_correct` and must not use production `adguardvm` as the destructive recovery target.
