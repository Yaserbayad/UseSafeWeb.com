import re
import subprocess
from pathlib import Path

STATE = Path('CURRENT_STATE.md')
EXPECTED_RUNTIME = 'bc95bd395097ace6ab93e368d10812aeeef5fc0f'
EXPECTED_ARTIFACT = '77b432e9d06741d0d303de2c2a2524e804cdcf5e'
EXPECTED_ANALYTICAL = '6cad75df075d9444abf67fa564452dc32a0692f3'
EXPECTED_DETERMINISTIC = 'dd6a3d5360d002fd1f89b23e569f36a90742b649'


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

require(blob('CURRENT_STATE.md') == EXPECTED_RUNTIME, 'runtime baseline changed before reconciliation')
require(blob('TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_REQUIREMENTS_2026-08-31.md') == EXPECTED_ARTIFACT, 'artifact blob mismatch')
require(blob('TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_ACCEPTANCE_EVIDENCE_2026-08-31.md') == EXPECTED_ANALYTICAL, 'analytical evidence blob mismatch')
require(blob('TSK_0142_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md') == EXPECTED_DETERMINISTIC, 'deterministic evidence blob mismatch')

text = STATE.read_text(encoding='utf-8')
require('## TSK-0312 current accepted stable state — 2026-08-31' in text, 'TSK-0312 current PASS marker absent')
require('### TSK-0041 accepted stable state' in text, 'TSK-0041 accepted marker absent')
require('## TSK-0142 current accepted stable state — 2026-08-31' not in text, 'TSK-0142 already reconciled')

text, count = re.subn(r'^\*\*Updated:\*\* .*$', '**Updated:** 2026-08-31T14:12:00Z', text, count=1, flags=re.MULTILINE)
require(count == 1, 'Updated marker not replaced exactly once')

section = r'''

## TSK-0142 current accepted stable state — 2026-08-31

`TSK-0142 — Specify lightweight parent dashboard and device-management requirements`: **PASS** under current `ACC-0142 / VER-0142 / EVD-0142`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, priority MEDIUM, hard dependencies `TSK-0312; TSK-0041`, A3 / `AUTO_ALLOWED`; the WBS planning/execution snapshot is not runtime proof.
- `TSK-0312` is current PASS under the post-CR-0007 runtime state. `TSK-0041` remains accepted and compatible for the DNS activation/verification/removal/privacy facts consumed by this task; CR-0006/CR-0007 did not weaken those technical truth requirements.
- Requirements artifact: `TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_REQUIREMENTS_2026-08-31.md`, version `1.0.0`, blob `77b432e9d06741d0d303de2c2a2524e804cdcf5e`, publication commit `9c8ffc1c933c67861f7549c6caee12f77af0ad7a`.
- Analytical acceptance evidence: `TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `6cad75df075d9444abf67fa564452dc32a0692f3`, publication commit `911a4f1c19771b42a77009e4b8f257f8e311775e`.
- Deterministic verification evidence: `TSK_0142_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `dd6a3d5360d002fd1f89b23e569f36a90742b649`, publication commit `404dd4d1bb9c0d270b343bb07d2ddfba8023fb61`.
- Independent verifier run/job `33401200803 / 99517634917` on self-hosted `adguardvm`: WBS contract, both dependency markers, all ACC-0142 semantics, 20 deterministic/synthetic test cases, scope fences, analytical evidence and no-downstream-PASS inference all PASS; repository diff/clean checks passed.
- Accepted dashboard boundary: optional authenticated parent continuity/device management with minimum device list/nickname, add/setup/verify/reinstall/replace/revoke/remove flows, truthful Protection Map/evidence states, curated controls, privacy-minimal help and account lifecycle handling.
- Account/device persistence does not create technical protection evidence. Stored ownership, dashboard presence or historical setup cannot create S1; current qualifying technical evidence remains required under the owning verifier contracts, and stale/contradictory evidence must downgrade the displayed state.
- Browsing/query/activity history, child behavioral profiles, raw/unrestricted AdGuard administration, broad per-domain allow/block controls, customer query logs, mandatory login for core value and safety paywalls remain excluded.
- J0/J1 remains separate from the optional persistent account/device domain. No automatic anonymous-state promotion/linkage is authorized; any future explicit transfer remains owned by a separately approved downstream data-flow contract.
- This PASS is requirements-level only. It does not infer provider/vendor, persistent schema/storage, authz/security architecture, implementation/build, legal/privacy compliance, real-user evidence, LG-06 or any later gate PASS.
- `RSK-0002` remains OPEN and non-blocking before L8 under current sequencing.

### Queue status after TSK-0142 acceptance

TSK-0142 may satisfy its outgoing hard-dependency edges. Recompute the current L4 queue from WBS dependencies, relationship graph, runtime evidence, gates/constraints and Action Authority before selecting any successor; do not infer the next task from numbering or prior conversation.
'''

STATE.write_text(text.rstrip() + section + '\n', encoding='utf-8')
out = STATE.read_text(encoding='utf-8')
require('## TSK-0142 current accepted stable state — 2026-08-31' in out, 'TSK-0142 section missing after transform')
require('Independent verifier run/job `33401200803 / 99517634917`' in out, 'verifier binding missing after transform')
require('LG-06 or any later gate PASS' in out, 'downstream PASS fence missing after transform')
print('TSK0142_RUNTIME_TRANSFORM=PASS')
