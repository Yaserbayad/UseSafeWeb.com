import csv, json, re, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
INDEX=ROOT/'prototype/TSK-0333/index.html'
MODEL=ROOT/'prototype/TSK-0333/model.mjs'
APP=ROOT/'prototype/TSK-0333/app.mjs'
CSS=ROOT/'prototype/TSK-0333/prototype.css'

EXPECTED_WBS='f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_GRAPH='c108d2c162bcea2ee4cc01def46d0487a9501032'
EXPECTED_RUNTIME='15948b153c5c0c07b93fc894ac9f4ca6c537cce0'

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob(WBS)==EXPECTED_WBS,'TSK0333_WBS_BLOB_CHANGED')
req(blob(GRAPH)==EXPECTED_GRAPH,'TSK0333_GRAPH_BLOB_CHANGED')
req(blob(RUNTIME)==EXPECTED_RUNTIME,'TSK0333_RUNTIME_BLOB_CHANGED')
print('TSK0333_CURRENT_AUTHORITY_BLOBS=PASS')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0333')
expected_acc='Prototype covers the full accountless core and optional Version-1 account paths: Google sign-in/account creation/return/session expiry/logout/delete entry, lightweight dashboard/device management, Android/iPhone DNS setup and verification, Protection Map, false-positive, support, account/device removal/revoke/reinstall/replacement/recovery, provider/error/unsupported states, responsive/mobile/RTL/accessibility and privacy boundaries. Core value never requires login; browsing/activity history and broad DNS administration are absent.'
req(row.get('Dependencies')=='TSK-0335; TSK-0334; TSK-0146; TSK-0331','TSK0333_DEPENDENCIES_CHANGED')
req(row.get('Acceptance_Criteria')==expected_acc,'TSK0333_ACC_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0333' and row.get('Verification_ID')=='VER-0333' and row.get('Evidence_ID')=='EVD-0333','TSK0333_IDS_CHANGED')
req(row.get('AI_Capability_A0_A4')=='A3' and row.get('Action_Authority')=='AUTO_ALLOWED','TSK0333_AUTH_CHANGED')
print('TSK0333_WBS_CONTRACT=PASS')

graph=GRAPH.read_text(encoding='utf-8')
start=graph.find('  TSK-0333:\n'); req(start>=0,'TSK0333_GRAPH_NODE_MISSING')
end=graph.find('\n  TSK-',start+3); block=graph[start:end if end>=0 else len(graph)]
for target in ('TSK-0335','TSK-0334','TSK-0146','TSK-0331','ACC-0333','VER-0333','EVD-0333','REQ-0028','REQ-0029','CON-0010','CON-0017','INT-0009','INT-0010'):
    req(f'target: {target}' in block,f'TSK0333_GRAPH_TARGET_MISSING={target}')
print('TSK0333_GRAPH_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
for dep in ('TSK-0335','TSK-0334','TSK-0146','TSK-0331'):
    req(f'## {dep} current accepted stable state' in runtime,f'TSK0333_CURRENT_DEP_MISSING={dep}')
req('## TSK-0333 current accepted stable state' not in runtime,'TSK0333_PREMATURE_CURRENT_PASS')
print('TSK0333_DEPENDENCY_RUNTIME=PASS')

for p in (INDEX,MODEL,APP,CSS): req(p.exists(),f'TSK0333_REQUIRED_ARTIFACT_MISSING={p.as_posix()}')
index=INDEX.read_text(encoding='utf-8').lower()
model=MODEL.read_text(encoding='utf-8').lower()
app=APP.read_text(encoding='utf-8').lower()
css=CSS.read_text(encoding='utf-8').lower()

# Current integrated surface contract.
for token in ('usesafeweb','start setup','sign in','dashboard','skip to current task','noindex,nofollow'):
    req(token in index,f'TSK0333_INDEX_CURRENT_SCOPE_MISSING={token}')
for screen in ('home','router','native','dns','verify','service','map','troubleshoot','false-positive','help','limits','remove','recovery','reset-lost','account-entry','sign-in','provider-pending','first-session','account-error','dashboard','device-detail','device-manage','reauth','account','data-use','logout-pending','delete-entry','lifecycle-confirm','lifecycle-unknown'):
    req(screen in model,f'TSK0333_MODEL_SCREEN_MISSING={screen}')
for state in ('verified','parent-confirmed','action-needed','not-covered','uncertain','removed'):
    req(state in model,f'TSK0333_EVIDENCE_STATE_MISSING={state}')
for invariant in ('core value never requires login','account presence never creates verified','no automatic j0/j1','no browsing/query/activity history','no broad dns administration','no automatic replay','physical removal','record deletion','account deletion'):
    req(invariant in model,f'TSK0333_MODEL_INVARIANT_MISSING={invariant}')
print('TSK0333_STRUCTURED_MODEL=PASS')

# Required interaction families in the UI controller.
for token in ('renderhome','renderrouter','rendernative','renderdns','renderverify','rendermap','rendersignin','renderfirstsession','renderdashboard','renderdevicedetail','renderdevicemanage','renderreauth','renderaccount','renderdeleteentry','renderlifecycleconfirm','renderlifecycleunknown'):
    req(token in app,f'TSK0333_APP_RENDERER_MISSING={token}')
for action in ('start','choose_platform','native_confirmed','dns_configured','verify_result','service_none','open_false_positive','remove_dns','confirm_removed','reconfigure','open_account_entry','start_google_signin','provider_success_new','provider_success_returning','create_account','open_dashboard','open_device','open_manage','reverify_device','reinstall_device','replace_device','revoke_device','delete_device_record','expire_session','reauthenticate','logout','open_delete_account','confirm_account_delete','resolve_unknown'):
    req(action in app or action in model,f'TSK0333_ACTION_MISSING={action}')
print('TSK0333_INTERACTION_COVERAGE=PASS')

# Privacy / lifecycle fences.
combined='\n'.join((index,model,app))
for forbidden in ('localstorage','sessionstorage','indexeddb','document.cookie'):
    req(forbidden not in combined,f'TSK0333_PERSISTENCE_API_FORBIDDEN={forbidden}')
for phrase in ('browsing history','activity history','raw dns','child profile'):
    req(phrase in combined,f'TSK0333_PRIVACY_BOUNDARY_MISSING={phrase}')
print('TSK0333_PRIVACY_LIFECYCLE_FENCES=PASS')

# Accessibility/responsive/RTL static contract.
for token in (':focus-visible','@media','320','[dir="rtl"]','prefers-reduced-motion'):
    req(token in css,f'TSK0333_CSS_CONTRACT_MISSING={token}')
for token in ('aria-live','main-content','skip-link'):
    req(token in index,f'TSK0333_ACCESSIBILITY_STATIC_MISSING={token}')
print('TSK0333_STATIC_UI_CONTRACT=PASS')
print('TSK0333_POST_CR0007_STRUCTURED_VERIFICATION=PASS')
