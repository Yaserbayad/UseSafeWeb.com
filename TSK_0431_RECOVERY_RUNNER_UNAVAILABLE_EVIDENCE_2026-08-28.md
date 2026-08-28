# TSK-0431 — Recovery Runner Availability Evidence

**Task:** TSK-0431 — Test pilot restore or rebuild procedure  
**Date:** 2026-08-28  
**Disposition:** WAITING — recovery target has not been schedulable by the governed GitHub Actions recovery workflow

## Owner-managed Azure prerequisite

The prior Azure Backup readiness condition is resolved by direct Project Owner evidence recorded in `TSK_0431_AZURE_BACKUP_OWNER_EVIDENCE_2026-08-28.md`, blob `fb846d5ab9a3ed3f4b52976273c92653d73db925`: Azure Backup is ready and its status is Successful. No vault/policy/recovery-point details are invented.

## Accepted historical recovery identity

Historical dual-runner fingerprint run `33161281851` proved two simultaneously schedulable, genuinely separate self-hosted runners:

- production runner `adguardvm` on Azure VM `adguardvm`, VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`, machine-id SHA-256 `e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`;
- recovery runner `adguartestdvm_correct` on Azure VM `adguartestdvm`, VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`.

Jobs `98816079276` and `98816079544` began within approximately one second of each other, so the repository is demonstrably capable of concurrent execution on the two runners when both are schedulable. Evidence: `TSK_0431_RECOVERY_RUNNER_CORRECTED_EVIDENCE_2026-08-28.md`, blob `1c8137ae89a5785d12fd1ec5b178488162b5bcd3`.

## Governed recovery implementation

The project prepared a fingerprint-gated clean-server recovery drill using:

- workflow `.github/workflows/adguard-clean-recovery-drill.yml`;
- runtime script `infrastructure/adguard-server/clean-recovery-drill-runtime.sh`, blob `d79c2ee958bfc305a2f973922248c58768cc01f0`;
- evidence publisher `infrastructure/adguard-server/publish-recovery-drill-evidence.sh`, blob `3527130d31969e7c8cb32e8586a715ea81d519f7`.

Before any host mutation, the runtime compares hostname and machine-id SHA-256 against the accepted production and recovery fingerprints. Production matches emit `production_runner_no_mutation=PASS`, sleep for a guard interval, and exit without recovery mutation. Any unexpected machine fails before mutation.

## Initial unavailable-runner attempt — run 33169207187

`recover (a)`, job `98841930651`, ran on `adguardvm`, emitted `production_runner_no_mutation=PASS`, and skipped evidence publication.

`recover (b)`, job `98841930635`, was again scheduled on `adguardvm`, emitted `production_runner_no_mutation=PASS`, and skipped evidence publication.

Final `confirm` job `98842441250` failed because `TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md` did not exist. No recovery PASS was inferred.

## Owner online report and direct retry — run 33170080158

At 2026-08-28T12:09:29Z, the Project Owner reported: `adguartestdvm_correct is online`.

The project immediately retried the unchanged fingerprint-gated recovery mechanics from workflow commit `e370996e6fb8a00f328335c9857cb90cd3ae15dd`, using scheduler labels `[self-hosted, linux, x64]`.

- `recover (a)`, job `98844800335`: GitHub runner `adguardvm`; `production_runner_no_mutation=PASS`; evidence publication skipped.
- `recover (b)`, job `98844800531`: GitHub again selected `adguardvm`; `production_runner_no_mutation=PASS`; evidence publication skipped.
- `confirm`, job `98845306418`: failed because no recovery evidence existed.

This proves that the owner-visible online state did not, by itself, make `adguartestdvm_correct` schedulable for the workflow's default self-hosted/Linux/x64 label set.

## Label-eligibility diagnostic — run 33170275152

To test whether the recovery runner had lost only its OS/architecture labels, scheduling was broadened to the single default selector `[self-hosted]` while retaining the exact same pre-mutation fingerprint guard. Workflow commit: `680038bf112447910fbb6ccee391302ac417e941`.

- `recover (b)`, job `98845453600`: GitHub runner `adguardvm`; `production_runner_no_mutation=PASS`; evidence publication skipped.
- `recover (a)`, job `98845453811`: GitHub runner `adguardvm`; `production_runner_no_mutation=PASS`; evidence publication skipped.
- `confirm`, job `98845963021`: failed because no recovery evidence existed.

Because the historical two-runner probe executed concurrently but both current retry variants serially reused production, the available durable evidence does not support a repository-wide one-job concurrency explanation. It establishes only that `adguartestdvm_correct` was not schedulable by either `[self-hosted, linux, x64]` or `[self-hosted]` during these governed attempts. The underlying runner registration/label/group state must not be guessed.

## What current evidence proves

- Azure Backup readiness: **owner-confirmed Successful**.
- Production `adguardvm` protection during all current recovery attempts: **PASS**; every selected production job exited through the immutable no-mutation guard.
- Historical independent recovery VM identity: still proven.
- Current recovery runner scheduling: **not proven / not schedulable by the tested selectors**, despite the owner-visible online report.
- No project-controlled recovery drill has executed on `adguartestdvm` during these attempts.
- No recovery evidence artifact exists.
- No production DNS, Azure control-plane resource, participant data, secret, or private key was changed or exposed by the failed scheduling attempts.

## Stable disposition and deterministic resumption

**TSK-0431 remains WAITING; not PASS.**

The safest deterministic routing correction is to assign a fresh custom GitHub Actions label to the existing recovery runner, for example `usesafeweb-recovery-v1`, and then route the recovery job to that label while retaining the exact recovery VM fingerprint guard. Do **not** create the custom label `adguartestdvm_correct`: an older stale queued workflow run already requested that string as a label, so assigning it could make stale work unexpectedly eligible.

After the uniquely labelled recovery runner is directly re-proven and the project-controlled clean recovery drill passes, the literal REQ-0052 Azure-native *restore* element still requires direct owner evidence that an Azure recovery-point restore was actually exercised successfully, unless the Project Owner explicitly changes that requirement through governed change control. Backup readiness is not silently converted into restore evidence.
