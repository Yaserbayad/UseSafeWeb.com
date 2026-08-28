from pathlib import Path
from datetime import datetime, timezone
import re

p = Path('CURRENT_STATE.md')
s = p.read_text()

s, n = re.subn(
    r'\*\*Updated:\*\* [^\n]+',
    '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') + '  ',
    s,
    count=1,
)
assert n == 1

old = "Current recovery-attempt evidence from run `33169207187` shows both common-label jobs were scheduled on production runner `adguardvm`; neither reached `adguartestdvm_correct`. Therefore the recovery VM identity remains historically proven, but the recovery runner is currently treated as unavailable to GitHub Actions until directly re-proven. Evidence: `TSK_0431_RECOVERY_RUNNER_UNAVAILABLE_EVIDENCE_2026-08-28.md`."
new = "The Project Owner subsequently reported `adguartestdvm_correct` online, but direct retry run `33170080158` still scheduled both `[self-hosted, linux, x64]` jobs on production `adguardvm`, and label-diagnostic run `33170275152` still scheduled both broadened `[self-hosted]` jobs on production. Every production job emitted `production_runner_no_mutation=PASS`; no recovery evidence was published. Historical recovery identity remains proven, but present schedulability is not. Evidence: `TSK_0431_RECOVERY_RUNNER_UNAVAILABLE_EVIDENCE_2026-08-28.md`, blob `2f90a355fb696ca75cfec176d56d72e68dcb92f3`."
assert s.count(old) == 1
s = s.replace(old, new, 1)

start = s.index('### WAITING — TSK-0431')
end = s.index('### TSK-0514 accepted stable state', start)
replacement = '''### WAITING — TSK-0431

`TSK-0431` — test pilot restore or rebuild procedure: **WAITING on deterministic recovery-runner routing and, after the project-controlled drill passes, direct owner evidence for the literal Azure-native restore element of REQ-0052; not PASS**.

The exact WBS row is L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0430; TSK-0011`, both satisfied. ACC-0431 requires a functional test target that passes encrypted-DNS and privacy checks with recovery time/issues recorded. REQ-0052 requires a timed clean-server drill covering host baseline, packages, AdGuard, server-managed configuration recovery, firewall/network, endpoint, TLS, filters, privacy, startup, Azure-native backup/restore, verification and health.

Azure Backup readiness is resolved. On 2026-08-28 the Project Owner directly reported Azure Backup ready with status **Successful** and explicitly approved treating Azure Backup setup/readiness as done. Durable owner evidence: `TSK_0431_AZURE_BACKUP_OWNER_EVIDENCE_2026-08-28.md`, blob `fb846d5ab9a3ed3f4b52976273c92653d73db925`. This is not silently converted into proof that an Azure recovery-point restore was executed.

The independent recovery target identity remains the previously proven Azure VM `adguartestdvm`, West Europe, Ubuntu 24.04, Azure VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`. Production remains VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`.

At 2026-08-28T12:09:29Z the Project Owner reported `adguartestdvm_correct is online`. The project immediately retried the fingerprint-gated recovery workflow. Run `33170080158` used `[self-hosted, linux, x64]`; jobs `98844800335` and `98844800531` both ran on `adguardvm`, emitted `production_runner_no_mutation=PASS`, skipped recovery evidence publication, and confirm job `98845306418` failed closed. A materially different label diagnostic then broadened selection to `[self-hosted]`: run `33170275152`, jobs `98845453600` and `98845453811`, again both ran on `adguardvm`, emitted the same no-mutation marker, skipped publication, and confirm job `98845963021` failed closed.

Historical run `33161281851` had executed production and `adguartestdvm_correct` concurrently, so current evidence does not support a repository-wide single-job-concurrency explanation. The owner-visible online state therefore does not by itself prove current schedulability, and the exact registration/label/group cause must not be guessed.

Evidence: `TSK_0431_RECOVERY_RUNNER_UNAVAILABLE_EVIDENCE_2026-08-28.md`, blob `2f90a355fb696ca75cfec176d56d72e68dcb92f3`.

Deterministic resumption condition:

1. in GitHub repository Settings > Actions > Runners, open `adguartestdvm_correct` and assign a fresh custom label `usesafeweb-recovery-v1`;
2. do not assign the label `adguartestdvm_correct`, because stale queued run `33168596672` already requests that label and could become unexpectedly eligible;
3. route the current recovery workflow to `usesafeweb-recovery-v1` while retaining the exact recovery VM fingerprint guard;
4. require the clean recovery drill to prove encrypted DoH/DoT, filtering/rollback, privacy, admin/firewall, health and <30-minute recovery evidence;
5. after the project-controlled drill passes, provide direct owner evidence that an Azure-native recovery-point restore was actually exercised successfully, unless the owner explicitly changes that literal REQ-0052 requirement through governed change control.

No recovery PASS is inferred from an online indicator or Azure Backup readiness alone.

'''
s = s[:start] + replacement + s[end:]

old = '- Azure control-plane provisioning/configuration remains owner-managed. Azure Backup readiness is owner-confirmed Successful. TSK-0431 is now immediately WAITING on `adguartestdvm_correct` becoming available to GitHub Actions; after the project-controlled drill passes, the literal Azure-native restore element of REQ-0052 still requires direct owner restore evidence unless changed by governed owner decision.'
new = '- Azure control-plane provisioning/configuration remains owner-managed. Azure Backup readiness is owner-confirmed Successful. TSK-0431 is now WAITING on deterministic GitHub Actions routing to the historically proven recovery runner; direct retries after the owner online report still selected production only. A fresh custom recovery label is required before another recovery attempt. After the project-controlled drill passes, the literal Azure-native restore element of REQ-0052 still requires direct owner restore evidence unless changed by governed owner decision.'
assert s.count(old) == 1
s = s.replace(old, new, 1)

old = '- `TSK-0431` — make recovery runner `adguartestdvm_correct` available to GitHub Actions; then rerun the fingerprint-gated recovery drill. Azure Backup readiness itself is already owner-confirmed Successful.'
new = '- `TSK-0431` — assign fresh custom runner label `usesafeweb-recovery-v1` to `adguartestdvm_correct`, then route the fingerprint-gated recovery drill to that unique label. Azure Backup readiness itself is already owner-confirmed Successful.'
assert s.count(old) == 1
s = s.replace(old, new, 1)

old = 'No ordinary L2 work may progress until a dependency/gate condition changes. TSK-0431 next requires `adguartestdvm_correct` to become available to GitHub Actions so the already-prepared fingerprint-gated clean recovery drill can execute on the isolated recovery VM. After that drill passes, do not infer the literal Azure-native restore element from backup readiness; require direct owner restore evidence or an explicit governed owner change to REQ-0052. Do not bypass participant-activation, legal, Azure control-plane, provider, recovery, privacy or validation gates.'
new = 'No ordinary L2 work may progress until a dependency/gate condition changes. TSK-0431 next requires the Project Owner to assign the fresh custom GitHub Actions label `usesafeweb-recovery-v1` to existing runner `adguartestdvm_correct`; do not use `adguartestdvm_correct` itself as the label because stale run `33168596672` already requests it. After the label is assigned, route the prepared fingerprint-gated clean recovery drill to that unique label and independently re-prove the recovery VM fingerprint before mutation. After that drill passes, do not infer the literal Azure-native restore element from backup readiness; require direct owner restore evidence or an explicit governed owner change to REQ-0052. Do not bypass participant-activation, legal, Azure control-plane, provider, recovery, privacy or validation gates.'
assert s.count(old) == 1
s = s.replace(old, new, 1)

p.write_text(s)
