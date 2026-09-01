from __future__ import annotations
import csv, json, re, subprocess
from pathlib import Path

ROOT = Path.cwd()

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')

def git_blob(path: str) -> str:
    return subprocess.check_output(['git','hash-object',path], text=True).strip()

def md_rows(text: str, prefix: str):
    out=[]
    for line in text.splitlines():
        if line.startswith(prefix):
            out.append([c.strip() for c in line.strip().strip('|').split('|')])
    return out

# Canonical WBS task contracts.
wbs_path='Plans/Master/WBS/master-wbs.csv'
with open(wbs_path, newline='', encoding='utf-8-sig') as f:
    rows=list(csv.DictReader(f))

def task_row(task_id: str):
    matches=[r for r in rows if task_id in r.values()]
    assert len(matches)==1, (task_id, len(matches))
    return matches[0]

def flat(r):
    return ' | '.join(str(v) for v in r.values() if v is not None)

for tid in ['TSK-0145','TSK-0043','TSK-0309','TSK-0628','TSK-0052']:
    r=task_row(tid)
    print('TASK', tid, flat(r))

assert 'revised dual-mode prototype' in flat(task_row('TSK-0309'))
assert 'optional parent account' in flat(task_row('TSK-0309'))
assert 'dashboard/device-management' in flat(task_row('TSK-0309'))
assert 'sign-in/session' in flat(task_row('TSK-0628'))
assert 'dashboard/device-management' in flat(task_row('TSK-0628'))
assert 'account/device deletion/removal' in flat(task_row('TSK-0628'))
assert 'AUTO_ALLOWED' in flat(task_row('TSK-0052'))
assert re.search(r'\bA4\b', flat(task_row('TSK-0052')))

# Traceability: current requirement set must be exactly represented by matrix rows,
# and fields owned by the canonical requirement register must still match.
req_rows=md_rows(read('Plans/Master/Registers/REQUIREMENTS.md'), '| REQ-')
mx_rows=md_rows(read('TSK_0145_REQUIREMENT_TO_EVIDENCE_TRACEABILITY_2026-08-28.md'), '| REQ-')
req={r[0]:r for r in req_rows}
mx={r[0]:r for r in mx_rows}
assert len(req)==91, len(req)
assert set(req)==set(mx), (set(req)-set(mx), set(mx)-set(req))
for rid, rr in req.items():
    mr=mx[rid]
    # requirement register: id, priority, package, text, implementing tasks, verification, source
    # matrix: id, source, rationale, priority, acceptance test, owner, release target, status, tasks, evidence
    assert mr[1] == rr[6], (rid, 'source', mr[1], rr[6])
    assert mr[3] == rr[1], (rid, 'priority', mr[3], rr[1])
    assert mr[4] == rr[5], (rid, 'verification', mr[4], rr[5])
    assert mr[2] and mr[5] and mr[6] and mr[7] and mr[8], (rid, 'required traceability field empty')

req11=' | '.join(req['REQ-0011'])
assert 'optional parent account' in req11
assert 'fully usable accountless core' in req11
print('TRACEABILITY_REQUIREMENTS', len(req), 'PASS')

# Current dual-mode baseline and source identity.
baseline=read('prototype/TSK-0309/BASELINE.md')
manifest=json.loads(read('prototype/TSK-0309/BASELINE_MANIFEST.json'))
assert manifest['version']=='2.0.0-post-cr0006'
assert manifest['representative_source']=='prototype/TSK-0333'
assert manifest['mode_contract']['accountless_core_usable_without_login'] is True
assert manifest['mode_contract']['optional_parent_account'] is True
assert manifest['mode_contract']['mandatory_login_for_core_value'] is False
assert 'prototype/TSK-0333/' in baseline
assert 'optional parent Google sign-in/account/session continuity' in baseline

expected={
 'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
 'prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212',
 'prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8',
 'prototype/TSK-0333/prototype.css':'385dc5269de79b7baca9aa597b9ecf4cca8a95f2',
}
for p,sha in expected.items():
    actual=git_blob(p)
    assert actual==sha,(p,actual,sha)
    assert manifest['artifacts'][{'index.html':'index','model.mjs':'model','app.mjs':'app','prototype.css':'styles'}[Path(p).name]]['git_blob']==sha
print('TSK0309_SOURCE_IDENTITY PASS')

access=read('TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md')
for phrase in ['focused 320 px / 200% text proof: **PASS**','Full current SafeWeb TSK-0333 Chromium regression: **PASS**','Full post-CR-0007 TSK-0321 mechanical accessibility suite: **PASS**','Product source identity remained unchanged during the review: **PASS**']:
    assert phrase in access, phrase
print('TSK0309_ACCEPTED_TEST_EVIDENCE PASS')

support=read('TSK_0628_POST_CR0006_NO_ROUTINE_HUMAN_SUPPORT_OPERATING_MODEL_2026-09-01.md')
for phrase in ['Sign-in / provider return','Session expiry / revocation / logout','Dashboard access','Add / save / manage device','Device replacement / revoke / record deletion','Account deletion','Removal / recovery','human escalation is exceptional']:
    assert phrase in support, phrase
for forbidden in ['routine human support a dependency','account presence/device ownership never creates `Verified` protection state']:
    assert forbidden in support, forbidden
print('TSK0628_DUAL_MODE_SUPPORT_MODEL PASS')

changes=read('Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md')
assert '| CR-0006 |' in changes and '| CR-0007 |' in changes
assert 'ACTIVATED_V1_SCOPE' in changes
print('CURRENT_CHANGE_AUTHORITY PASS')

print('LG06_PREDECESSOR_REQUALIFICATION_BASELINE PASS')
