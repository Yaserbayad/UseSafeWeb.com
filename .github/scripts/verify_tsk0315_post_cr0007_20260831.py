import csv
import subprocess
from pathlib import Path

EXPECTED = {
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'runtime': '7c6241502cbb361a6cd02bc5d3568b82904b0170',
    'artifact': '97cf09f294c757f80ad5c0fbe6110ed8d471159c',
    'evidence': '5c9c9278349323b67200f084716be8baf9724110',
}
WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
ART = Path('TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md')
EVD = Path('TSK_0315_POST_CR0007_DUAL_MODE_SERVICE_BLUEPRINT_ACCEPTANCE_EVIDENCE_2026-08-31.md')


def blob(path: str) -> str:
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

for key, path in [('wbs',WBS),('runtime',STATE),('artifact',ART),('evidence',EVD)]:
    require(blob(str(path)) == EXPECTED[key], f'unexpected {key} blob')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows.get('TSK-0315')
require(r is not None, 'TSK-0315 missing')
require(r.get('Lifecycle_Stage') == 'L4', 'lifecycle mismatch')
require(r.get('Priority') == 'HIGH', 'priority mismatch')
require(r.get('Dependencies') == 'TSK-0149; TSK-0229; TSK-0142', 'dependency mismatch')
require(r.get('Acceptance_ID') == 'ACC-0315', 'acceptance mismatch')
require(r.get('Verification_ID') == 'VER-0315', 'verification mismatch')
require(r.get('Evidence_ID') == 'EVD-0315', 'evidence mismatch')
require(r.get('Action_Authority') == 'AUTO_ALLOWED', 'authority mismatch')
require(r.get('AI_Capability_A0_A4') == 'A3', 'capability mismatch')
print('TSK0315_WBS_CONTRACT=PASS')

state = STATE.read_text(encoding='utf-8')
for marker in [
    '## TSK-0149 current accepted stable state — 2026-08-31',
    'TSK-0229 current accepted stable state',
    '## TSK-0142 current accepted stable state — 2026-08-31',
]:
    require(marker in state, f'dependency marker absent: {marker}')
require('TSK-0315 current accepted stable state' not in state, 'TSK-0315 already current PASS')
print('TSK0315_DEPENDENCIES_RUNTIME=PASS')

art = ART.read_text(encoding='utf-8')
ev = EVD.read_text(encoding='utf-8')

header = '| Stage | Frontstage — parent experience | Backstage — service/system behavior | Data boundary | Responsible owner | Failure / uncertainty | Recovery / next safe action |'
require(header in art, 'required blueprint mapping columns absent')
for i in range(25):
    require(f'| {i}.' in art, f'missing blueprint stage {i}')
print('TSK0315_STAGE_MAP_25=PASS')

required = [
    'Discover / trust', 'Start core', 'Native safeguard', 'DNS configure', 'DNS verify',
    'Relevant service', 'Protection Map', 'Optional account entry', 'First-session account creation',
    'Signed-in return / session', 'Dashboard empty/list', 'Add/manage device', 'Reverify / reinstall / reconfigure',
    'Replace device', 'Revoke/unlink management', 'Delete dashboard device record', 'Account logout',
    'Account deletion', 'False positive / ordinary help', 'Remove UseSafeWeb protection', 'Post-removal recovery',
    'Provider outage branch', 'Exit / reset / lost state',
    'No automatic J0/J1 linkage', 'no browsing/query/activity history',
    'login is never required for start, native safeguard, DNS setup/verification, service guidance, Protection Map, troubleshooting, removal or recovery',
]
for phrase in required:
    require(phrase in art, f'missing ACC dimension: {phrase}')
print('TSK0315_ACC_SEMANTICS=PASS')

section = art.split('## 9. Deterministic blueprint assertions',1)[1].split('## 10.',1)[0]
for i in range(1,25):
    require(f'{i}.' in section, f'missing assertion {i}')
print('TSK0315_ASSERTIONS_24=PASS')

require('pre-CR-0006 TSK-0315 artifact is accountless-only and is therefore superseded' in ev, 'stale blueprint reconciliation absent')
require('No-linkage compatibility: PASS.' in ev, 'no-linkage analytical result absent')
require('Analytical result: ACC-0315 PASS candidate.' in ev, 'analytical disposition absent')
print('TSK0315_ANALYTICAL_EVIDENCE=PASS')

for forbidden in ['LG-06 is PASS','implementation is PASS','provider acceptance is PASS','legal/privacy compliance is PASS']:
    require(forbidden not in art and forbidden not in ev, f'downstream PASS inference found: {forbidden}')
print('TSK0315_NO_DOWNSTREAM_PASS_INFERENCE=PASS')
print('TSK0315_INDEPENDENT_VERIFICATION=PASS')
