# TSK-0431 — Recovery Runner Availability Evidence

**Task:** TSK-0431 — Test pilot restore or rebuild procedure  
**Date:** 2026-08-28  
**Disposition:** WAITING — recovery target was not available to the governed GitHub Actions execution attempt

## Owner-managed Azure prerequisite

The prior Azure Backup readiness condition is resolved by direct Project Owner evidence recorded in `TSK_0431_AZURE_BACKUP_OWNER_EVIDENCE_2026-08-28.md`, blob `fb846d5ab9a3ed3f4b52976273c92653d73db925`: Azure Backup is ready and its status is Successful. No vault/policy/recovery-point details are invented.

## Governed recovery execution attempt

The project prepared a fingerprint-gated clean-server recovery drill using:

- workflow `.github/workflows/adguard-clean-recovery-drill.yml`, wrapper blob `fe30ebba36fe710d6d8131002307f664bcd99d2a`;
- runtime script `infrastructure/adguard-server/clean-recovery-drill-runtime.sh`, blob `d79c2ee958bfc305a2f973922248c58768cc01f0`;
- evidence publisher `infrastructure/adguard-server/publish-recovery-drill-evidence.sh`, blob `3527130d31969e7c8cb32e8586a715ea81d519f7`;
- workflow run `33169207187`.

The wrapper intentionally scheduled two common-label self-hosted jobs so that production could not be mistaken for the recovery VM. Before any host mutation, the runtime script compares hostname and machine-id SHA-256 against the accepted production and recovery fingerprints.

### Job evidence

`recover (a)`, job `98841930651`:

- GitHub identified runner name and machine name as `adguardvm`;
- the immutable production guard matched;
- output: `production_runner_no_mutation=PASS`;
- it exited successfully;
- evidence publication was skipped.

`recover (b)`, job `98841930635`:

- after the first job released the available runner, GitHub again scheduled the job on runner name/machine name `adguardvm`;
- the immutable production guard matched again;
- output: `production_runner_no_mutation=PASS`;
- it exited successfully;
- evidence publication was skipped.

The final `confirm` job `98842441250` failed because `TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md` did not exist. This is the correct fail-closed result: no recovery PASS was inferred.

## What this proves

- Production `adguardvm` was protected from recovery mutation on both scheduling attempts: **PASS**.
- The accepted independent recovery VM identity remains the previously proven Azure VM `adguartestdvm`, VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`.
- The recovery runner `adguartestdvm_correct` was **not available to receive this governed run**. The available GitHub evidence does not establish whether the cause is an offline runner service, disconnected runner, VM availability state, or another runner-registration/scheduling condition; no cause is invented.
- No recovery mutation was performed on the recovery VM during this attempt.
- No production DNS, Azure control-plane resource, participant data, secret, or private key was changed or exposed by this failed scheduling attempt.

## Stable disposition

**TSK-0431 remains WAITING; not PASS.**

The immediate deterministic resumption condition is to make the already-registered recovery runner `adguartestdvm_correct` available to GitHub Actions again. The fingerprint-gated project-controlled drill can then be rerun without changing production or Azure control-plane resources.

After that drill passes, the literal REQ-0052 Azure-native *restore* element still requires direct owner evidence that an Azure recovery-point restore was actually exercised successfully, unless the Project Owner explicitly changes that requirement through governed change control. The current statement that Azure Backup is ready/successful proves backup readiness, not an actual restore event.
