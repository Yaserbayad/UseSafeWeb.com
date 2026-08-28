from pathlib import Path
from datetime import datetime, timezone
import re

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')

s, n = re.subn(
    r'\*\*Updated:\*\* [^\n]+',
    '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') + '  ',
    s,
    count=1,
)
assert n == 1

old_runner_line = "- recovery runner `adguartestdvm_correct`: Azure VM `adguartestdvm`, VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`, Ubuntu 24.04, West Europe, AdGuard/Nginx inactive."
new_runner_line = "- recovery runner `adguartestdvm_correct`: Azure VM `adguartestdvm`, VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`, Ubuntu 24.04, West Europe; owner-provided custom label `rec-v1`; AdGuard/Nginx active after the accepted project-controlled recovery drill and post-run health recheck."
assert s.count(old_runner_line) == 1
s = s.replace(old_runner_line, new_runner_line, 1)

old_sched = "The Project Owner subsequently reported `adguartestdvm_correct` online, but direct retry run `33170080158` still scheduled both `[self-hosted, linux, x64]` jobs on production `adguardvm`, and label-diagnostic run `33170275152` still scheduled both broadened `[self-hosted]` jobs on production. Every production job emitted `production_runner_no_mutation=PASS`; no recovery evidence was published. Historical recovery identity remains proven, but present schedulability is not. Evidence: `TSK_0431_RECOVERY_RUNNER_UNAVAILABLE_EVIDENCE_2026-08-28.md`, blob `2f90a355fb696ca75cfec176d56d72e68dcb92f3`."
new_sched = "The Project Owner then assigned the fresh custom runner label `rec-v1` and confirmed the recovery runner online. Direct GitHub Actions execution subsequently proved deterministic routing to runner `adguartestdvm_correct` / machine `adguartestdvm`. Project-controlled recovery run `33173972042` / job `98857724228` reached `TSK_0431_PROJECT_CONTROLLED_DRILL=PASS`; read-only capture run `33174075020` / job `98858073703` re-proved the accepted recovery fingerprint, privacy-safe PASS summary and post-run AdGuard/Nginx health. Durable evidence: `TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md`, blob `2df5c05767fe326e38c609d37888f672dcb9dd48`."
assert s.count(old_sched) == 1
s = s.replace(old_sched, new_sched, 1)

start = s.index('### WAITING — TSK-0431')
end = s.index('### TSK-0514 accepted stable state', start)
replacement = '''### WAITING — TSK-0431

`TSK-0431` — test pilot restore or rebuild procedure: **WAITING only on direct owner evidence for the literal Azure-native recovery-point restore element of REQ-0052; project-controlled rebuild/functional/privacy/timing acceptance is PASS; overall task is not PASS**.

The exact WBS row remains L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0430; TSK-0011`, both satisfied. ACC-0431 requires a functional test target that passes encrypted-DNS and privacy checks with recovery time/issues recorded. REQ-0052 additionally requires the Azure-native backup/restore element.

Azure Backup readiness remains owner-confirmed **Successful** through `TSK_0431_AZURE_BACKUP_OWNER_EVIDENCE_2026-08-28.md`, blob `fb846d5ab9a3ed3f4b52976273c92653d73db925`. Backup readiness is not converted into restore evidence.

The Project Owner supplied the custom GitHub Actions label `rec-v1` for existing runner `adguartestdvm_correct` and reported it online. That routing boundary is now directly proven. Recovery run `33173972042` / job `98857724228` executed on runner `adguartestdvm_correct`, machine `adguartestdvm`, after the exact accepted recovery fingerprint and Azure VM identity gates. The drill rebuilt the project-controlled application state and emitted `TSK_0431_PROJECT_CONTROLLED_DRILL=PASS` after all acceptance checks.

Read-only capture run `33174075020` / job `98858073703` then re-proved the same recovery fingerprint and captured only the allow-listed privacy-safe summary: approved configuration reconstruction PASS; loopback Nginx TLS listeners PASS; local DoH PASS; local DoT PASS; block/exception/exact rollback PASS; privacy persistence PASS; admin/firewall fail-safe PASS; recovery target health PASS; project-controlled rebuild PASS; elapsed time **12 seconds**; post-run health recheck PASS. Evidence: `TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md`, blob `2df5c05767fe326e38c609d37888f672dcb9dd48`, publication commit `c356384aeafe70f5c74c8eb3966a810c4947673b`.

The recovery job's GitHub conclusion was failure only because a root-owned temporary DoH output file could not be removed by the non-root final cleanup command **after** `TSK_0431_PROJECT_CONTROLLED_DRILL=PASS` had already been emitted. The separate post-run health/summary capture proved this post-acceptance cleanup deviation did not invalidate the recovery criteria. No production service or Azure control-plane resource was mutated by the recovery drill.

Current unresolved literal requirement: `azure_native_restore_exercised=false`. TSK-0431 therefore remains WAITING, not PASS, until the Project Owner provides direct evidence that an Azure-native recovery-point restore was actually exercised successfully, or explicitly changes REQ-0052 through governed change control.

Deterministic resumption condition:

1. Project Owner exercises the approved Azure-native recovery-point restore path under the owner-managed Azure control-plane boundary without overwriting production;
2. provide direct, privacy-safe evidence of successful restore execution (for example target, recovery point timestamp/status and successful restore outcome, without unnecessary subscription/account identifiers);
3. reconcile that evidence against REQ-0052 and ACC-0431 before any overall TSK-0431 PASS decision.

'''
s = s[:start] + replacement + s[end:]

s, n = re.subn(
    r'^- Azure control-plane provisioning/configuration remains owner-managed\..*$',
    '- Azure control-plane provisioning/configuration remains owner-managed. Azure Backup readiness is owner-confirmed Successful and deterministic `rec-v1` recovery-runner routing plus the project-controlled clean rebuild are now proven. TSK-0431 remains WAITING solely on direct owner evidence that the literal Azure-native recovery-point restore was actually exercised successfully, unless changed by governed owner decision.',
    s,
    count=1,
    flags=re.M,
)
assert n == 1

old_boundary = '- `TSK-0431` — assign fresh custom runner label `usesafeweb-recovery-v1` to `adguartestdvm_correct`, then route the fingerprint-gated recovery drill to that unique label. Azure Backup readiness itself is already owner-confirmed Successful.'
new_boundary = '- `TSK-0431` — project-controlled recovery drill is PASS with deterministic `rec-v1` routing and 12-second recovery evidence; overall task remains WAITING only on direct owner evidence of a successful Azure-native recovery-point restore.'
assert s.count(old_boundary) == 1
s = s.replace(old_boundary, new_boundary, 1)

old_next = 'No ordinary L2 work may progress until a dependency/gate condition changes. TSK-0431 next requires the Project Owner to assign the fresh custom GitHub Actions label `usesafeweb-recovery-v1` to existing runner `adguartestdvm_correct`; do not use `adguartestdvm_correct` itself as the label because stale run `33168596672` already requests it. After the label is assigned, route the prepared fingerprint-gated clean recovery drill to that unique label and independently re-prove the recovery VM fingerprint before mutation. After that drill passes, do not infer the literal Azure-native restore element from backup readiness; require direct owner restore evidence or an explicit governed owner change to REQ-0052. Do not bypass participant-activation, legal, Azure control-plane, provider, recovery, privacy or validation gates.'
new_next = 'No ordinary L2 work may progress until a dependency/gate condition changes. The runner-routing and project-controlled rebuild portions of TSK-0431 are satisfied. The exact next authoritative step is owner-managed Azure-native recovery-point restore execution and direct successful-restore evidence; do not restore/overwrite production, do not infer restore success from backup readiness, and do not bypass participant-activation, legal, Azure control-plane, provider, recovery, privacy or validation gates.'
assert s.count(old_next) == 1
s = s.replace(old_next, new_next, 1)

p.write_text(s, encoding='utf-8')
