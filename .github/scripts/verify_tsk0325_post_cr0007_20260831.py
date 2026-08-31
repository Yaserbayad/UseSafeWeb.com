import csv
import json
import subprocess
from pathlib import Path

EXPECTED = {
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'runtime': '6feab0d1991035304293c25c0af1398e75ff91f7',
    'artifact': '7763a6d16760d85df3ad23789f764d3e431849ef',
    'projection': '9826c7ab39e087002c6e0a51d7353e52ca6cc34b',
    'evidence': '36d838ad4e9de2f705005a16930d72a768727d68',
}
WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
ART = Path('prototype/TSK-0325/SERVICE_BLUEPRINT.md')
PROJ = Path('prototype/TSK-0325/ACCEPTANCE_MATRIX.json')
EVD = Path('TSK_0325_POST_CR0007_PARENT_JOURNEY_SERVICE_BLUEPRINT_EVIDENCE_2026-08-31.md')


def blob(path: str) -> str:
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

for key, path in [('wbs',WBS),('runtime',STATE),('artifact',ART),('projection',PROJ),('evidence',EVD)]:
    require(blob(str(path)) == EXPECTED[key], f'unexpected {key} blob')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows.get('TSK-0325')
require(r is not None, 'TSK-0325 missing')
require(r.get('Lifecycle_Stage') == 'L4', 'lifecycle mismatch')
require(r.get('Priority') == 'MEDIUM', 'priority mismatch')
require(r.get('Dependencies') == 'TSK-0326', 'dependency mismatch')
require(r.get('Acceptance_ID') == 'ACC-0325', 'acceptance mismatch')
require(r.get('Verification_ID') == 'VER-0325', 'verification mismatch')
require(r.get('Evidence_ID') == 'EVD-0325', 'evidence mismatch')
require(r.get('Action_Authority') == 'AUTO_ALLOWED', 'authority mismatch')
require(r.get('AI_Capability_A0_A4') == 'A3', 'capability mismatch')
for ref in ['REQ-0028','REQ-0029','CON-0010','CON-0017']:
    require(ref in r.get('Requirement_Reference',''), f'missing WBS ref {ref}')
print('TSK0325_WBS_CONTRACT=PASS')

state = STATE.read_text(encoding='utf-8')
idx = state.find('TSK-0326')
require(idx >= 0, 'TSK-0326 marker absent')
window = state[max(0,idx-500):idx+1000]
require('NOT_APPLICABLE + PASS' in window, 'TSK-0326 exclusion PASS not bound near marker')
require('## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007' in state, 'current TSK-0315 supporting source absent')
require('## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007' not in state, 'current TSK-0325 already reconciled')
print('TSK0325_DEPENDENCY_RUNTIME=PASS')

art = ART.read_text(encoding='utf-8')
ev = EVD.read_text(encoding='utf-8')
proj = json.loads(PROJ.read_text(encoding='utf-8'))

require('Version:** 2.0.0-post-cr0007' in art, 'artifact version mismatch')
required_headings = [
    'Path A — Normal supported accountless setup',
    'Path B — Already configured',
    'Path C — Unsupported / not covered',
    'Path D — Failed activation / verification failure',
    'Path E — False positive / legitimate content blocked',
    'Path F — Resume after interruption',
    'Path G — Removal and recovery',
    'Path H — Support / help',
]
for heading in required_headings:
    require(heading in art, f'missing required path {heading}')
print('TSK0325_REQUIRED_PATHS_8=PASS')

for i in range(1,18):
    require(f'`TP-{i:02d}`' in art, f'missing TP-{i:02d}')
require(art.count('| `TP-') == 17, 'touchpoint table does not contain exactly 17 rows')
for trace in ['REQ-0028','REQ-0029','CON-0010','CON-0017','INT-0009','INT-0010']:
    require(trace in art, f'missing trace {trace}')
print('TSK0325_TOUCHPOINTS_17_TRACE=PASS')

require(proj.get('schema') == 'usesafeweb.tsk0325.acceptance-projection.v2', 'projection schema mismatch')
require(proj.get('version') == '2.0.0-post-cr0007', 'projection version mismatch')
require(len(proj.get('required_paths',[])) == 8, 'projection path count mismatch')
require(len(proj.get('touchpoints',[])) == 17, 'projection touchpoint count mismatch')
require(all('REQ-0028' in t.get('requirements',[]) for t in proj['touchpoints']), 'not every touchpoint maps REQ-0028')
require(all('CON-0010' in t.get('constraints',[]) and 'CON-0017' in t.get('constraints',[]) for t in proj['touchpoints']), 'not every touchpoint maps current constraints')
require(all('INT-0009' in t.get('interfaces',[]) and 'INT-0010' in t.get('interfaces',[]) for t in proj['touchpoints']), 'not every touchpoint maps interfaces')
print('TSK0325_PROJECTION_CONSISTENCY=PASS')

for phrase in [
    'The full core path remains usable without login',
    'Optional account entry is continuity/management only',
    'No automatic J0/J1-to-account/device join, promotion or expiry extension is authorized',
    'stored account/device ownership never becomes system verification',
    'TP-08 → TP-09 → TP-10 → TP-11 / TP-17',
    'logout, revoke/unlink, device-record deletion, account deletion and physical DNS removal remain distinct operations',
    'Browsing/query/activity history, child accounts/profiles and raw/unrestricted AdGuard administration remain excluded',
]:
    require(phrase in art, f'missing current-scope invariant: {phrase}')
print('TSK0325_CURRENT_SCOPE_RECONCILIATION=PASS')

require('Historical TSK-0325 v1.0.0 was accepted' in ev, 'historical impact analysis absent')
require('Analytical result: ACC-0325 PASS candidate.' in ev, 'analytical disposition absent')
require('TSK-0326 NOT_APPLICABLE+PASS' in ev, 'behavioral exclusion evidence boundary absent')
for forbidden in ['TSK-0328 IA PASS','TSK-0329 prototype PASS','LG-06 is PASS','implementation/build is PASS','behavioral validation is PASS']:
    require(forbidden not in art and forbidden not in ev, f'downstream PASS inference found: {forbidden}')
print('TSK0325_ANALYTICAL_AND_PASS_FENCES=PASS')
print('TSK0325_INDEPENDENT_VERIFICATION=PASS')
