import csv, json, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
PROTO=ROOT/'prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md'
MODEL=ROOT/'prototype/TSK-0331/LIFECYCLE_STATE_MODEL.json'
HTML=ROOT/'prototype/TSK-0331/index.html'
CSS=ROOT/'prototype/TSK-0331/prototype.css'
APP=ROOT/'prototype/TSK-0331/app.mjs'

EXPECTED_WBS='f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_RUNTIME='b5700eef473850ac49fdc83ea5bfbe7f2c6e54f2'

def blob(path): return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
def req(cond,msg):
    if not cond: raise SystemExit(msg)

req(blob(WBS)==EXPECTED_WBS,'TSK0331_WBS_BLOB_CHANGED')
req(blob(RUNTIME)==EXPECTED_RUNTIME,'TSK0331_RUNTIME_BLOB_CHANGED')
with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0331')
req(row.get('Dependencies')=='TSK-0332; TSK-0334','TSK0331_WBS_DEPENDENCIES_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0331' and row.get('Verification_ID')=='VER-0331' and row.get('Evidence_ID')=='EVD-0331','TSK0331_WBS_ACCEPTANCE_CHANGED')
req(row.get('AI_Capability_A0_A4')=='A4' and row.get('Action_Authority')=='AUTO_ALLOWED','TSK0331_WBS_AUTHORITY_CHANGED')
expected_acc='Flows make consequences explicit, require appropriate confirmation, handle partial/provider failures, offer safe recovery, preserve truthful protection state and define what account/device metadata is deleted or retained.'
req(row.get('Acceptance_Criteria')==expected_acc,'TSK0331_ACC_TEXT_CHANGED')
print('TSK0331_WBS_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
for dep in ('TSK-0332','TSK-0334'):
    req(f'## {dep} current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,f'TSK0331_DEP_NOT_CURRENT_PASS={dep}')
req('## TSK-0331 current accepted stable state' not in runtime,'TSK0331_PREMATURE_RUNTIME_PASS')
print('TSK0331_DEPENDENCY_RUNTIME=PASS')

graph=GRAPH.read_text(encoding='utf-8')
start=graph.find('  TSK-0331:\n'); req(start>=0,'TSK0331_GRAPH_MISSING')
end=graph.find('\n  TSK-',start+3); block=graph[start:end if end>=0 else len(graph)]
for dep in ('TSK-0332','TSK-0334'):
    req(f'target: {dep}' in block,'TSK0331_GRAPH_DEP_MISSING='+dep)
for ref in ('ACC-0331','VER-0331','EVD-0331','REQ-0028','REQ-0029','CON-0010','CON-0017','INT-0009','INT-0010'):
    req(f'target: {ref}' in block,'TSK0331_GRAPH_REF_MISSING='+ref)
print('TSK0331_GRAPH_CONTRACT=PASS')

for p in (PROTO,MODEL,HTML,CSS,APP):
    req(p.exists(),f'TSK0331_REQUIRED_ARTIFACT_MISSING={p.as_posix()}')

proto=PROTO.read_text(encoding='utf-8')
low=proto.lower()
model=json.loads(MODEL.read_text(encoding='utf-8'))
html=HTML.read_text(encoding='utf-8').lower()
css=CSS.read_text(encoding='utf-8').lower()
app=APP.read_text(encoding='utf-8').lower()

req(model.get('schema')=='usesafeweb.tsk0331.lifecycle-prototype.v1','TSK0331_MODEL_SCHEMA')
req(model.get('task')=='TSK-0331' and model.get('acceptance')=='ACC-0331','TSK0331_MODEL_IDENTITY')
req(model.get('dependencies')==['TSK-0332','TSK-0334'],'TSK0331_MODEL_DEPENDENCIES')
required_states={
'account','delete-entry','delete-confirm','delete-pending','delete-success','delete-failed','delete-unknown',
'device','unlink-confirm','unlink-pending','unlink-success','unlink-unknown','remove-record-confirm','remove-record-success',
'remove-protection-confirm','remove-protection-success','reconfigure','replace-confirm','replace-new','session-expired','provider-error','ownership-mismatch','recovery'
}
ids={x.get('id') for x in model.get('states',[])}
req(required_states <= ids,'TSK0331_MODEL_STATES_MISSING='+','.join(sorted(required_states-ids)))
for action in ('delete-account','unlink-device','remove-record','remove-protection','reconfigure','replace-device','logout','reauth','resolve-unknown'):
    req(action in model.get('actions',[]),'TSK0331_ACTION_MISSING='+action)
for invariant in (
'account deletion does not claim physical protection removal',
'record deletion does not claim physical protection removal',
'unknown destructive outcome is not automatically replayed',
'ownership mismatch fails closed',
'account/session/provider failure does not alter physical protection truth',
'new replacement device inherits no verified or parent-confirmed state',
'core usable without login',
):
    req(invariant in [x.lower() for x in model.get('required_invariants',[])],'TSK0331_INVARIANT_MISSING='+invariant)
print('TSK0331_STRUCTURED_MODEL=PASS')

for token in (
'account deletion','device record','physical protection','confirmation','partial failure','provider failure','unknown result','safe recovery',
'deleted','retained','session expiry','ownership mismatch','reinstall','reconfigure','replacement','revoke','logout','j0/j1','without login'
): req(token in low,'TSK0331_PROTO_SEMANTIC_MISSING='+token)
for token in ('browsing/query/activity history','no automatic replay','does not remove usesafeweb protection'):
    req(token in low,'TSK0331_SAFETY_BOUNDARY_MISSING='+token)
print('TSK0331_NORMATIVE_PROTOTYPE=PASS')

for token in ('<main','aria-live','data-state','confirm','cancel','help'):
    req(token in html or token in app,'TSK0331_UI_STRUCTURE_MISSING='+token)
for token in ('@media','max-width','focus-visible','prefers-reduced-motion'):
    req(token in css,'TSK0331_CSS_REQUIREMENT_MISSING='+token)
for forbidden in ('browsing history','query history','top sites','raw adguard'):
    req(forbidden not in html,'TSK0331_FORBIDDEN_USER_SURFACE='+forbidden)
print('TSK0331_STATIC_UI_CONTRACT=PASS')
print('TSK0331_STRUCTURED_VERIFICATION=PASS')
