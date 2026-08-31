import csv, json, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
PROTO=ROOT/'prototype/TSK-0332/DASHBOARD_DEVICE_MANAGEMENT_PROTOTYPE.md'
MODEL=ROOT/'prototype/TSK-0332/DASHBOARD_STATE_MODEL.json'
HTML=ROOT/'prototype/TSK-0332/index.html'
CSS=ROOT/'prototype/TSK-0332/prototype.css'
APP=ROOT/'prototype/TSK-0332/app.mjs'

EXPECTED_WBS='f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_RUNTIME='3565211485530631e56a4db63163710d2218dfe0'

def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)], text=True).strip()

def require(cond,msg):
    if not cond: raise SystemExit(msg)

require(blob(WBS)==EXPECTED_WBS,'TSK0332_WBS_BLOB_CHANGED')
require(blob(RUNTIME)==EXPECTED_RUNTIME,'TSK0332_RUNTIME_BLOB_CHANGED')
with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0332')
require(row.get('Dependencies')=='TSK-0329; TSK-0142','TSK0332_WBS_DEPENDENCIES_CHANGED')
require(row.get('Acceptance_ID')=='ACC-0332' and row.get('Verification_ID')=='VER-0332' and row.get('Evidence_ID')=='EVD-0332','TSK0332_WBS_ACCEPTANCE_CONTRACT_CHANGED')
require(row.get('AI_Capability_A0_A4')=='A4' and row.get('Action_Authority')=='AUTO_ALLOWED','TSK0332_WBS_AUTHORITY_CHANGED')
print('TSK0332_WBS_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
for dep in ('TSK-0329','TSK-0142'):
    require(f'## {dep} current accepted stable state' in runtime,f'TSK0332_DEPENDENCY_NOT_CURRENT_PASS={dep}')
require('LG-06 remains non-PASS' in runtime,'TSK0332_LG06_FENCE_MISSING')
print('TSK0332_DEPENDENCY_RUNTIME=PASS')

graph=GRAPH.read_text(encoding='utf-8')
start=graph.find('  TSK-0332:\n')
require(start>=0,'TSK0332_GRAPH_MISSING')
end=graph.find('\n  TSK-',start+3)
block=graph[start:end if end>=0 else len(graph)]
for dep in ('TSK-0329','TSK-0142'):
    require(f'target: {dep}' in block and 'type: depends_on' in block,f'TSK0332_GRAPH_DEP_MISSING={dep}')
for ref in ('ACC-0332','VER-0332','EVD-0332','REQ-0028','REQ-0029','CON-0010','CON-0017','INT-0009','INT-0010'):
    require(f'target: {ref}' in block,f'TSK0332_GRAPH_REF_MISSING={ref}')
print('TSK0332_GRAPH_CONTRACT=PASS')

for p in (PROTO,MODEL,HTML,CSS,APP):
    require(p.exists(),f'TSK0332_REQUIRED_ARTIFACT_MISSING={p.as_posix()}')

proto=PROTO.read_text(encoding='utf-8')
model=json.loads(MODEL.read_text(encoding='utf-8'))
html=HTML.read_text(encoding='utf-8')
css=CSS.read_text(encoding='utf-8')
app=APP.read_text(encoding='utf-8')

require(model.get('schema')=='usesafeweb.tsk0332.dashboard-prototype.v1','TSK0332_MODEL_SCHEMA')
require(model.get('task')=='TSK-0332' and model.get('acceptance')=='ACC-0332','TSK0332_MODEL_IDENTITY')
require(model.get('dependencies')==['TSK-0329','TSK-0142'],'TSK0332_MODEL_DEPENDENCIES')
required_states={'empty','device-protected','device-parent-confirmed','device-action-needed','device-not-covered','device-uncertain','device-removed','add-device','continue-setup','verify','reconfigure','replace','unlink','remove-protection','remove-record','help','session-expired','account-error'}
state_ids={x['id'] for x in model.get('states',[])}
require(required_states <= state_ids,f'TSK0332_MODEL_STATES_MISSING={sorted(required_states-state_ids)}')
required_actions={'add-device','continue-setup','verify','reverify','rename','reconfigure','replace','unlink','remove-protection','remove-record','account','logout','help'}
actions=set(model.get('curated_actions',[]))
require(required_actions <= actions,f'TSK0332_ACTIONS_MISSING={sorted(required_actions-actions)}')
for forbidden in ('browsing history','query history','top sites','raw adguard','per-domain','child profile'):
    require(forbidden in [x.lower() for x in model.get('excluded_surfaces',[])],f'TSK0332_EXCLUSION_MISSING={forbidden}')
for invariant in ('core usable without login','record presence never establishes verified','account/session failure does not alter dns/core truth','record deletion is distinct from physical protection removal','no activity history'):
    require(invariant in [x.lower() for x in model.get('required_invariants',[])],f'TSK0332_INVARIANT_MISSING={invariant}')
print('TSK0332_STRUCTURED_MODEL=PASS')

low=proto.lower()
for token in ('mobile-first','empty dashboard','add device','protection map','contextual help','provider/account unavailable','ownership mismatch','remove from dashboard','remove usesafeweb protection','english','turkish','arabic','rtl','wcag 2.2 aa'):
    require(token in low,f'TSK0332_PROTO_SEMANTIC_MISSING={token}')
require(('dash-session-expired' in low or 'session expired' in low or 'session ended' in low) and 'sign in again' in low,'TSK0332_SESSION_EXPIRY_SEMANTIC_MISSING')
require('browsing/query/activity history' in low,'TSK0332_HISTORY_EXCLUSION_MISSING')
require('record presence' in low and 'verified' in low,'TSK0332_VERIFICATION_SEPARATION_MISSING')
require('without login' in low,'TSK0332_ACCOUNTLESS_CORE_MISSING')
print('TSK0332_NORMATIVE_PROTOTYPE=PASS')

for token in ('<main','aria-live','data-state','add device','protection map','help'):
    require(token in html.lower() or token in app.lower(),f'TSK0332_UI_STRUCTURE_MISSING={token}')
for token in ('@media','max-width','focus-visible','prefers-reduced-motion'):
    require(token in css.lower(),f'TSK0332_CSS_REQUIREMENT_MISSING={token}')
for forbidden in ('adguard','top sites','browsing history','query history'):
    require(forbidden not in html.lower(),f'TSK0332_USER_UI_FORBIDDEN_TERM={forbidden}')
print('TSK0332_STATIC_UI_CONTRACT=PASS')

require('TSK-0332' not in runtime or '## TSK-0332 current accepted stable state' not in runtime,'TSK0332_PREMATURE_RUNTIME_PASS')
print('TSK0332_PASS_FENCE=PASS')
print('TSK0332_STRUCTURED_VERIFICATION=PASS')
