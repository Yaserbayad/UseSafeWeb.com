# TSK-0431 — Recovery Runner Identity Recheck Evidence

**Task:** TSK-0431 — Test pilot restore or rebuild procedure  
**Acceptance:** ACC-0431  
**Date:** 2026-08-28

## Owner report being verified

The owner reported that the real test VM was complete and registered in GitHub as self-hosted runner `adguartestdvm`.

Because ACC-0431 requires an actual clean test target, runner registration name alone is insufficient. The project therefore performed direct read-only machine/Azure fingerprint verification before any recovery mutation.

## Authoritative WBS boundary

ACC-0431: **Test target becomes functional, passes encrypted DNS and privacy checks, and recovery time/issues are recorded.**

Required access includes Azure, a fresh Ubuntu 24.04 LTS host, Bash, and DNS/TLS/monitoring access. TSK-0431 is `AUTO_ALLOWED`, HIGH priority, critical path, with hard predecessors `TSK-0430; TSK-0011`.

## Dual-runner fingerprint verification

Workflow: `.github/workflows/governance-task-row-inspect.yml`  
Run: `33158855146`

Two simultaneous read-only self-hosted jobs were dispatched so both available registrations could execute independently.

### Job A

Job: `98808136878`  
GitHub runner name: `adguartestdvm`  
Result: **PASS fingerprint capture**

Observed target:

- machine hostname: `adguardvm`;
- Ubuntu 24.04;
- machine-id SHA-256: `e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`;
- Azure VM name: `adguardvm`;
- Azure location: `westeurope`;
- Azure VM ID: `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`;
- AdGuard Home active;
- Nginx active.

### Job B

Job: `98808137226`  
GitHub runner name: `adguardvm`  
Result: **PASS fingerprint capture**

Observed target:

- machine hostname: `adguardvm`;
- Ubuntu 24.04;
- machine-id SHA-256: `e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`;
- Azure VM name: `adguardvm`;
- Azure location: `westeurope`;
- Azure VM ID: `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`;
- AdGuard Home active;
- Nginx active.

## Evidence conclusion

The two GitHub runner registrations are currently different **names for the same Azure production VM**. The identical Azure VM ID is decisive; this is not merely a duplicated hostname or cloned machine-id.

Executing a restore/rebuild through `adguartestdvm` would therefore target production and would violate the clean-test-target acceptance boundary.

No recovery mutation was attempted.

## Stable outcome

**TSK-0431: WAITING.**

Deterministic resolution condition: the GitHub runner intended for recovery must execute on a distinct owner-provided Ubuntu 24.04 LTS West Europe VM and prove a different Azure VM ID/machine fingerprint from production before any restore/rebuild operation starts.
