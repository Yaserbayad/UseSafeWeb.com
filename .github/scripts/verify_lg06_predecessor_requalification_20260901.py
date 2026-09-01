from __future__ import annotations
import csv, json, re, subprocess
from pathlib import Path
ROOT=Path.cwd()
def read(path): return (ROOT/path).read_text(encoding='utf-8')
def git_blob(path): return subprocess.check_output(['git','hash-object',path],text=True).strip()
def md_rows(text,prefix): return [[c.strip() for c in l.strip().strip('|').split('|')] for l in text.splitlines() if l.startswith(prefix)]
with open('Plans/Master/WBS/master-wbs.csv',newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
def task_row(t):
    m=[r for r in rows if t in r.values()]; assert len(m)==1,(t,len(m)); return m[0]
def flat(r): return ' | '.join(str(v) for v in r.values() if v is not None)
for t in ['TSK-0145','TSK-0043','TSK-0309','TSK-0628','TSK-0052']: print('TASK',t,flat(task_row(t)))
r=flat(task_row('TSK-0309')); assert all(x in r for x in ['revised dual-mode prototype','optional parent account','lightweight dashboard','deletion/recovery'])
r=flat(task_row('TSK-0628')); assert all(x in r for x in ['sign-in/session','dashboard/device-management','account/device deletion/removal'])
r=flat(task_row('TSK-0052')); assert 'AUTO_ALLOWED' in r and re.search(r'\bA4\b',r)
req_rows=md_rows(read('Plans/Master/Registers/REQUIREMENTS.md'),'| REQ-'); mx_rows=md_rows(read('TSK_0145_REQUIREMENT_TO_EVIDENCE_TRACEABILITY_2026-08-28.md'),'| REQ-')
req={r[0]:r for r in req_rows}; mx={r[0]:r for r in mx_rows}; assert len(req)==91; assert set(req)==set(mx)
for rid,rr in req.items():
    mr=mx[rid]; assert mr[1]==rr[6]; assert mr[3]==rr[1]; assert mr[4]==rr[5]; assert all([mr[2],mr[5],mr[6],mr[7],mr[8]])
assert all(x in ' | '.join(req['REQ-0011']) for x in ['optional parent account','fully usable accountless core'])
print('TRACEABILITY_REQUIREMENTS 91 PASS')
baseline=read('prototype/TSK-0309/BASELINE.md'); manifest=json.loads(read('prototype/TSK-0309/BASELINE_MANIFEST.json'))
assert manifest['version']=='2.0.0-post-cr0006' and manifest['representative_source']=='prototype/TSK-0333'; assert manifest['mode_contract']['accountless_core_usable_without_login']; assert manifest['mode_contract']['optional_parent_account']; assert not manifest['mode_contract']['mandatory_login_for_core_value']; assert 'optional parent Google sign-in/account/session continuity' in baseline
expected={'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013','prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212','prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8','prototype/TSK-0333/prototype.css':'385dc5269de79b7baca9aa597b9ecf4cca8a95f2'}; key={'index.html':'index','model.mjs':'model','app.mjs':'app','prototype.css':'styles'}
for p,sha in expected.items(): assert git_blob(p)==sha and manifest['artifacts'][key[Path(p).name]]['git_blob']==sha
print('TSK0309_SOURCE_IDENTITY PASS')
access=read('TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md')
for x in ['Focused 320px / 200% text proof: **PASS**','Full current SafeWeb TSK-0333 Chromium regression: **PASS**','Full post-CR-0007 TSK-0321 mechanical accessibility suite: **PASS**','Product source identity remained unchanged during the review: **PASS**']: assert x in access
print('TSK0309_ACCEPTED_TEST_EVIDENCE PASS')
support=read('TSK_0628_POST_CR0006_NO_ROUTINE_HUMAN_SUPPORT_OPERATING_MODEL_2026-09-01.md')
for x in ['Sign-in / provider return','Session expiry / revocation / logout','Dashboard access','Add / save / manage device','Device replacement / revoke / record deletion','Account deletion','Removal / recovery','human escalation is exceptional','without making routine human support a dependency','account presence/device ownership never creates `Verified` protection state']: assert x in support
print('TSK0628_DUAL_MODE_SUPPORT_MODEL PASS')
review=read('TSK_0043_POST_CR0006_CROSS_FUNCTIONAL_REQUIREMENTS_REVIEW_2026-09-01.md')
for x in ['0 unresolved critical requirement conflicts','Accountless core vs optional account','Anonymous state vs persistent account','Account/device ownership vs protection truth','Account deletion vs DNS/device removal','Accessibility vs responsive/account expansion','Self-service vs account lifecycle','NCF-0043-01','NCF-0043-02']: assert x in review
assert review.count('| None |')>=12
print('TSK0043_CONFLICT_REVIEW PASS')
changes=read('Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md'); assert '| CR-0006 |' in changes and '| CR-0007 |' in changes and 'ACTIVATED_V1_SCOPE' in changes
print('CURRENT_CHANGE_AUTHORITY PASS'); print('LG06_PREDECESSOR_REQUALIFICATION_BASELINE PASS')
