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


def blob(path):
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


def require(cond, msg):
    if not cond:
        raise SystemExit(msg)


def section(text, title):
    marker = f'## {title}'
    start = text.find(marker)
    require(start >= 0, f'missing section: {title}')
    end = text.find('\n## ', start + len(marker))
    return text[start:] if end < 0 else text[start:end]


for key, path in [('wbs', WBS), ('runtime', STATE), ('artifact', ART), ('projection', PROJ), ('evidence', EVD)]:
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
for ref in ['REQ-0028', 'REQ-0029', 'CON-0010', 'CON-0017']:
    require(ref in r.get('Requirement_Reference', ''), f'missing WBS ref {ref}')
print('TSK0325_WBS_CONTRACT=PASS')

state = STATE.read_text(encoding='utf-8')
idx = state.find('TSK-0326')
require(idx >= 0, 'TSK-0326 marker absent')
require('NOT_APPLICABLE + PASS' in state[max(0, idx - 500):idx + 1000], 'TSK-0326 exclusion PASS not bound')
require('## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007' in state, 'current TSK-0315 supporting source absent')
require('## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007' not in state, 'current TSK-0325 already reconciled')
print('TSK0325_DEPENDENCY_RUNTIME=PASS')

art = ART.read_text(encoding='utf-8')
ev = EVD.read_text(encoding='utf-8')
proj = json.loads(PROJ.read_text(encoding='utf-8'))
require('Version:** 2.0.0-post-cr0007' in art, 'artifact version mismatch')
require(proj.get('schema') == 'usesafeweb.tsk0325.acceptance-projection.v2', 'projection schema mismatch')
require(proj.get('version') == '2.0.0-post-cr0007', 'projection version mismatch')
paths = {p['id']: p for p in proj.get('required_paths', [])}
tps = {t['id']: t for t in proj.get('touchpoints', [])}
invariants = set(proj.get('mandatory_invariants', []))
require(len(paths) == 8, 'projection path count mismatch')
require(len(tps) == 17, 'projection touchpoint count mismatch')
for p in paths.values():
    require(p.get('heading') in art, f"artifact missing projected path {p.get('id')}")
for i in range(1, 18):
    require(f'`TP-{i:02d}`' in art, f'missing TP-{i:02d}')
require(art.count('| `TP-') == 17, 'artifact touchpoint table count mismatch')
require(all('REQ-0028' in t.get('requirements', []) for t in tps.values()), 'not every touchpoint maps REQ-0028')
require(all({'CON-0010', 'CON-0017'} <= set(t.get('constraints', [])) for t in tps.values()), 'not every touchpoint maps current constraints')
require(all({'INT-0009', 'INT-0010'} <= set(t.get('interfaces', [])) for t in tps.values()), 'not every touchpoint maps interfaces')
print('TSK0325_PATH_TOUCHPOINT_STRUCTURE=PASS')

required_invariants = {
    'full core journey remains usable without login',
    'configuration/account/device record presence never directly establishes Verified',
    'account sign-in does not extend or automatically promote J0/J1',
    'removal withdraws active UseSafeWeb DNS protection claim',
    'dashboard/device record/account deletion is distinct from physical DNS removal',
    'no browsing/query/activity history, child account, or raw DNS administration is introduced',
}
require(required_invariants <= invariants, 'structured lifecycle invariant missing')
removal_terminal = paths['removal'].get('terminal', '').lower()
for token in ['removed', 'claim withdrawn', 'account/device record lifecycle', 'separate']:
    require(token in removal_terminal, f'removal projection missing semantic token: {token}')
resume_terminal = paths['resume'].get('terminal', '').lower()
for token in ['account continuity', 'no automatic j0/j1 promotion', 'reverified']:
    require(token in resume_terminal, f'resume projection missing semantic token: {token}')
tp17 = tps.get('TP-17')
require(tp17 is not None, 'projection TP-17 missing')
require(tp17.get('name') == 'Account/device lifecycle', 'projection TP-17 name mismatch')
require({'TSK-0312', 'TSK-0142'} <= set(tp17.get('dependencies', [])), 'projection TP-17 dependencies incomplete')
print('TSK0325_PROJECTION_LIFECYCLE_CONTRACT=PASS')

binding = section(art, '2. Binding journey rules').lower()
for token in ['full core path', 'without login', 'optional account entry', 'continuity/management', 'no automatic j0/j1', 'stored account/device ownership', 'system verification', 'browsing/query/activity history']:
    require(token in binding, f'binding semantics missing: {token}')

tp17_line = next((line for line in art.splitlines() if line.startswith('| `TP-17` |')), '')
require(tp17_line, 'artifact TP-17 row absent')
tp17_text = tp17_line.lower()
for token in ['account/device lifecycle', 'logout', 'revoke/unlink', 'delete device record', 'delete account', 'distinct', 'physical dns removal', 'tsk-0312', 'tsk-0142']:
    require(token in tp17_text, f'artifact TP-17 semantic token missing: {token}')

path_g = section(art, '10. Path G — Removal and recovery').lower()
for token in ['dashboard record deletion', 'revoke', 'account deletion', 'separate operations', 'must not claim physical dns removal', 'removed', 'reinstall', 'verified']:
    require(token in path_g, f'Path G lifecycle semantic missing: {token}')

overlay = section(art, '12. Optional account/device continuity overlay').lower()
for token in ['tp-08', 'tp-09', 'tp-10', 'tp-11', 'tp-17', 'logout/session expiry', 'account access', 'configured dns', 'device-record deletion', 'account deletion', 'j0/j1 deletion', 'physical dns removal', 'separate', 'stored ownership/history', 'verified']:
    require(token in overlay, f'account overlay semantic missing: {token}')
print('TSK0325_ARTIFACT_LIFECYCLE_STRUCTURE=PASS')

require('Historical TSK-0325 v1.0.0 was accepted' in ev, 'historical impact analysis absent')
require('Analytical result: ACC-0325 PASS candidate.' in ev, 'analytical disposition absent')
require('TSK-0326 NOT_APPLICABLE+PASS' in ev, 'behavioral exclusion boundary absent')
for forbidden in ['TSK-0328 IA PASS', 'TSK-0329 prototype PASS', 'LG-06 is PASS', 'implementation/build is PASS', 'behavioral validation is PASS']:
    require(forbidden not in art and forbidden not in ev, f'downstream PASS inference found: {forbidden}')
print('TSK0325_ANALYTICAL_AND_PASS_FENCES=PASS')
print('TSK0325_CURRENT_SCOPE_RECONCILIATION=PASS')
print('TSK0325_INDEPENDENT_VERIFICATION=PASS')
