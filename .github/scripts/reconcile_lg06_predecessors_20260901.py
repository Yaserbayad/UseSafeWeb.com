from __future__ import annotations
import datetime as dt
import re
import subprocess
from pathlib import Path

ROOT = Path.cwd()
RUNTIME = ROOT / 'CURRENT_STATE.md'
FINAL_MARKER = ROOT / 'TSK_LG06_PREDECESSOR_REQUALIFICATION_AUTOVERIFY_FINAL_2026-09-01.md'
EVIDENCE = ROOT / 'TSK_LG06_PREDECESSOR_CURRENT_REQUALIFICATION_EVIDENCE_2026-09-01.md'


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def path_commit(path: str) -> str:
    return subprocess.check_output(['git', 'log', '-1', '--format=%H', '--', path], text=True).strip()

subprocess.run(['python3', '.github/scripts/verify_lg06_predecessor_requalification_20260901.py'], check=True)

wbs_blob = blob('Plans/Master/WBS/master-wbs.csv')
assert wbs_blob == 'b57104a71ab814d0f67e7fb8b0fd388d1f6aacfa', wbs_blob

marker = read(FINAL_MARKER)
for required in [
    '**Disposition:** PASS',
    '`d4c1749bcbe074737897f0a9e79181858019af45`',
    '`33492766097`',
    '91 current requirements',
    'zero unresolved critical conflicts',
]:
    assert required in marker, required

state = read(RUNTIME)
assert '## TSK-0321 current accepted stable state — 2026-09-01 — POST-CR-0007' in state
assert '## TSK-0052 / LG-06 CR-0007 auto-authority reconciliation — 2026-09-01' in state
assert 'The stale WBS metadata was reconciled' in state

headings = [
    '## TSK-0145 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0043 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0309 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0628 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
]
for heading in headings:
    assert heading not in state, f'already reconciled: {heading}'
assert not EVIDENCE.exists(), 'evidence file already exists'

matrix_blob = blob('TSK_0145_REQUIREMENT_TO_EVIDENCE_TRACEABILITY_2026-08-28.md')
review_blob = blob('TSK_0043_POST_CR0006_CROSS_FUNCTIONAL_REQUIREMENTS_REVIEW_2026-09-01.md')
baseline_blob = blob('prototype/TSK-0309/BASELINE.md')
baseline_manifest_blob = blob('prototype/TSK-0309/BASELINE_MANIFEST.json')
support_blob = blob('TSK_0628_POST_CR0006_NO_ROUTINE_HUMAN_SUPPORT_OPERATING_MODEL_2026-09-01.md')
access_blob = blob('TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md')
marker_blob = blob('TSK_LG06_PREDECESSOR_REQUALIFICATION_AUTOVERIFY_FINAL_2026-09-01.md')
marker_commit = path_commit('TSK_LG06_PREDECESSOR_REQUALIFICATION_AUTOVERIFY_FINAL_2026-09-01.md')

now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

evidence = f'''# LG-06 predecessor current requalification evidence — 2026-09-01

**Scope:** `TSK-0145`, `TSK-0043`, `TSK-0309`, `TSK-0628` only.  
**Authority:** `DEC-0052 / CR-0005`, `DEC-0053 / CR-0006`, `DEC-0054 / CR-0007`.  
**Current WBS blob:** `{wbs_blob}`.  
**Final source-verification marker:** `{marker_blob}` at commit `{marker_commit}`.  
**Verification run/job:** `33492766097 / 99807875248` — SUCCESS.  
**Reconciliation time:** {now}.

## TSK-0145 — ACC-0145 / VER-0145 / EVD-0145

PASS. The existing derived traceability matrix remains non-authoritative but is current for the ACC-0145 metadata contract. Final verification proved exactly **91** canonical requirements are represented and that each current requirement matches canonical source, priority and verification while rationale, owner, release target, status and implementing-task linkage are populated. Matrix blob: `{matrix_blob}`. No requirement-level PASS is inferred from matrix presence; `REQ-0022` remains separately governed.

## TSK-0043 — ACC-0043 / VER-0043 / EVD-0043

PASS. Current cross-functional review blob `{review_blob}` records **0 unresolved critical requirement conflicts** across dual-mode scope, privacy minimisation, anonymous/persistent-state separation, protection truth, deletion/removal, accessibility, self-service and CR-0007 authority. The two remaining noncritical interpretation controls each have a named owner, control date `2026-09-01`, current disposition and deterministic recheck trigger. No material scope or gate-authority contradiction remains at L4.

## TSK-0309 — ACC-0309 / VER-0309 / EVD-0309

PASS. Current frozen implementation-ready baseline `2.0.0-post-cr0006` (blob `{baseline_blob}`; manifest `{baseline_manifest_blob}`) binds engineering handoff to the accepted dual-mode `prototype/TSK-0333` source. The exact integrated source hashes match current accepted identity. Existing final TSK-0321 target-environment evidence blob `{access_blob}` supplies the required successful 320px/200% reflow, full Chromium regression and current mechanical accessibility review after remediation. The complete accountless core remains usable without login; optional account/session/minimum ownership persistence/lightweight dashboard/device lifecycle and deletion/recovery paths are included. No real-user evidence is claimed before L8.

## TSK-0628 — ACC-0628 / VER-0628 / EVD-0628

PASS. Current dual-mode no-routine-human-support operating model blob `{support_blob}` covers ordinary accountless setup/verification/troubleshooting/recovery/removal plus sign-in/provider, session, dashboard, device-management, account/device lifecycle and deletion/recovery issue classes. Human/operator handling remains exceptional and criterion-driven; account/device ownership never creates technical `Verified`; browsing/query/activity history, raw DNS history, credentials, child identity and broad DNS administration remain excluded. This is L4 operating-model evidence, not real-user supportability proof.

## Boundary

These four PASS decisions repair stale post-CR-0006 evidence only. They do **not** by themselves make `TSK-0052 / LG-06` PASS and do not infer L5 architecture/vendor/privacy/security readiness, L6 implementation, L7 release readiness, legal completion, real-user validation, payment, production activation, publication or launch.
'''
EVIDENCE.write_text(evidence, encoding='utf-8')

appendix = f'''

{headings[0]}

`TSK-0145 — Build requirement-to-evidence traceability matrix`: **PASS** under the current ACC-0145 metadata contract. Final verification run/job `33492766097 / 99807875248` proved all 91 current requirements are represented with canonical source/priority/verification and populated rationale/owner/release-target/status/task linkage. Current matrix blob `{matrix_blob}`; consolidated requalification evidence `TSK_LG06_PREDECESSOR_CURRENT_REQUALIFICATION_EVIDENCE_2026-09-01.md`. The matrix remains derived/non-authoritative and creates no requirement-level PASS.

{headings[1]}

`TSK-0043 — Run cross-functional requirements review and resolve conflicts`: **PASS** under current dual-mode Version-1 authority. Current review blob `{review_blob}` records 0 unresolved critical conflicts; both noncritical interpretation controls have named owners, control date 2026-09-01 and deterministic recheck triggers. Final verification run/job `33492766097 / 99807875248`: PASS. No later gate or implementation state is inferred.

{headings[2]}

`TSK-0309 — Freeze the implementation-ready experience baseline from current internal and automated acceptance evidence`: **PASS** under current `DEC-0052/0053/0054` authority. Baseline `2.0.0-post-cr0006`, blob `{baseline_blob}`, manifest `{baseline_manifest_blob}`, now binds the accepted dual-mode `prototype/TSK-0333` source and current account/session/dashboard/device lifecycle while preserving the complete accountless core. Final TSK-0321 evidence blob `{access_blob}` supplies accepted target-environment responsive/accessibility/regression proof. Final source requalification run/job `33492766097 / 99807875248`: PASS. No real-user evidence or L5/L6/L7 PASS is inferred.

{headings[3]}

`TSK-0628 — Define the no-routine-human-support operating model`: **PASS** under the current dual-mode L4 contract. Current operating-model blob `{support_blob}` covers ordinary accountless plus sign-in/session/dashboard/device-management/account-device deletion/removal/recovery issues with exceptional bounded human routes only. Final verification run/job `33492766097 / 99807875248`: PASS. This does not prove real-user supportability or implement support automation.

### Queue status after LG-06 predecessor requalification

The stale post-CR-0006 predecessor evidence identified on the `TSK-0052 / LG-06` closure is reconciled for TSK-0145, TSK-0043, TSK-0309 and TSK-0628. `TSK-0321` remains current PASS. `TSK-0052 / LG-06` remains **non-PASS** at this checkpoint and must now be independently evaluated against `ACC-0052` and the current LG-06 gate evidence before any L5 unlock.
'''

state = re.sub(r'\*\*Updated:\*\*\s*[^\n]+', f'**Updated:** {now}', state, count=1)
RUNTIME.write_text(state.rstrip() + appendix + '\n', encoding='utf-8')

new_state = read(RUNTIME)
for heading in headings:
    assert new_state.count(heading) == 1, heading
assert '`TSK-0052 / LG-06` remains **non-PASS**' in new_state
print('LG06_PREDECESSOR_STABLE_RECONCILIATION_READY')
