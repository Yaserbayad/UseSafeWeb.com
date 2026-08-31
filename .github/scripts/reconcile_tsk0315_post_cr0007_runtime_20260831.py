import re
import subprocess
from pathlib import Path

STATE = Path('CURRENT_STATE.md')
EXPECTED_RUNTIME = '7c6241502cbb361a6cd02bc5d3568b82904b0170'
EXPECTED_ARTIFACT = '97cf09f294c757f80ad5c0fbe6110ed8d471159c'
EXPECTED_ANALYTICAL = '5c9c9278349323b67200f084716be8baf9724110'
EXPECTED_DETERMINISTIC = 'f458ade10b26d686cf45b5c839d2acc39fac1568'


def blob(path: str) -> str:
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

require(blob('CURRENT_STATE.md') == EXPECTED_RUNTIME, 'runtime baseline changed before reconciliation')
require(blob('TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md') == EXPECTED_ARTIFACT, 'blueprint blob mismatch')
require(blob('TSK_0315_POST_CR0007_DUAL_MODE_SERVICE_BLUEPRINT_ACCEPTANCE_EVIDENCE_2026-08-31.md') == EXPECTED_ANALYTICAL, 'analytical blob mismatch')
require(blob('TSK_0315_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md') == EXPECTED_DETERMINISTIC, 'deterministic blob mismatch')
text = STATE.read_text(encoding='utf-8')
for marker in ['## TSK-0149 current accepted stable state — 2026-08-31','TSK-0229 current accepted stable state','## TSK-0142 current accepted stable state — 2026-08-31']:
    require(marker in text, f'dependency marker absent: {marker}')
require('TSK-0315 current accepted stable state' not in text, 'TSK-0315 already current PASS')
text, count = re.subn(r'^\*\*Updated:\*\* .*$', '**Updated:** 2026-08-31T14:28:00Z', text, count=1, flags=re.MULTILINE)
require(count == 1, 'Updated marker not replaced exactly once')
section = r'''

## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0315 — Create the dual-mode end-to-end service blueprint for accountless core and optional parent-account lifecycle`: **PASS** under current `ACC-0315 / VER-0315 / EVD-0315`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, priority HIGH, hard dependencies `TSK-0149; TSK-0229; TSK-0142`, A3 / `AUTO_ALLOWED`; the WBS planning/execution snapshot is not runtime proof.
- All three hard dependencies are current durable PASS: post-CR-0007 TSK-0149 outcome split, post-CR-0006 TSK-0229 accountless/persistent separation, and current TSK-0142 dashboard/device-management requirements.
- Current blueprint: `TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md`, version `2.0.0-post-cr0007`, blob `97cf09f294c757f80ad5c0fbe6110ed8d471159c`, publication commit `90bd9e6a4e4891d67e350db6a4001848e7610703`.
- Analytical acceptance evidence: `TSK_0315_POST_CR0007_DUAL_MODE_SERVICE_BLUEPRINT_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `5c9c9278349323b67200f084716be8baf9724110`, publication commit `b7bee6f7453d0ccb68f9cb6c0034d9296cbf5a5c`.
- Deterministic verification evidence: `TSK_0315_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `f458ade10b26d686cf45b5c839d2acc39fac1568`, publication commit `9a6e32f7774f4f0bead70d0e3f6cdd301f1cd425`.
- Independent verifier run/job `33402665013 / 99522523592` on self-hosted `adguardvm`: WBS contract, all dependency markers, 25-stage mapping, all ACC semantics, 24 deterministic assertions, analytical evidence and no-downstream-PASS inference all PASS; repository diff/clean checks passed.
- The historical accountless-only `TSK_0315_ACCOUNTLESS_END_TO_END_SERVICE_BLUEPRINT_2026-08-28.md` is superseded for current acceptance where it excludes the now-authorized optional account/dashboard scope.
- Accepted current blueprint preserves a complete login-free core and maps optional Google account entry/creation/return/session, dashboard/device lifecycle, provider outage, false-positive support, reinstall/reconfigure, replace, revoke/unlink, device-record/account deletion, physical DNS removal/recovery and exit.
- Every mapped stage includes frontstage, backstage, data boundary, responsible owner, failure/uncertainty and recovery. No automatic J0/J1 linkage or browsing/query/activity history is authorized.
- Account/device ownership or stored history never substitutes for current technical protection verification; account/device/J0-J1 deletion and physical DNS removal remain separate operations.
- This PASS is service-design only. It does not infer current IA/navigation, provider/security architecture, persistent schema/storage, implementation/build, legal/privacy compliance, real-user evidence, LG-06 or any later gate PASS.
- `RSK-0002` remains OPEN/non-blocking before L8 under current sequencing.

### Queue status after TSK-0315 acceptance

TSK-0315 may now satisfy its outgoing hard-dependency edges. Recompute the current L4 queue from WBS dependencies, relationship graph, runtime evidence, gates/constraints and Action Authority; stale pre-CR-0006 PASS evidence must not satisfy a changed successor acceptance.
'''
out = text.rstrip() + section.rstrip() + '\n'
require(not out.endswith('\n\n'), 'blank line at EOF would be created')
STATE.write_text(out, encoding='utf-8')
out = STATE.read_text(encoding='utf-8')
require('## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007' in out, 'TSK-0315 section missing')
require('Independent verifier run/job `33402665013 / 99522523592`' in out, 'verifier binding missing')
require(not out.endswith('\n\n'), 'blank line at EOF after write')
print('TSK0315_RUNTIME_TRANSFORM=PASS')
print('TSK0315_EOF_GUARD=PASS')
