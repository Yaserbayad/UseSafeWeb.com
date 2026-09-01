import csv
import subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
CAND=ROOT/'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md'
AN=ROOT/'TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md'
DET=ROOT/'TSK_0333_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md'

def req(cond,msg):
    if not cond:
        raise SystemExit(msg)

def blob(path):
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'],text=True).strip()

with WBS.open(encoding='utf-8-sig',newline='') as f:
    rows={r['Task_ID']:r for r in csv.DictReader(f)}
r=rows['TSK-0327']
req(r['Lifecycle_Stage']=='L4','TSK0327_WBS_LIFECYCLE')
req(r['Dependencies'].strip()=='TSK-0336','TSK0327_WBS_DEPENDENCY')
req(r['Acceptance_ID']=='ACC-0327' and r['Verification_ID']=='VER-0327' and r['Evidence_ID']=='EVD-0327','TSK0327_WBS_IDS')
req(r['AI_Capability_A0_A4']=='A3' and r['Action_Authority']=='AUTO_ALLOWED','TSK0327_WBS_AUTHORITY')
req('All critical/high findings from current internal/automated' in r['Acceptance_Criteria'],'TSK0327_WBS_ACC')
print('TSK0327_WBS_CONTRACT=PASS')

graph=GRAPH.read_text(encoding='utf-8')
start=graph.find('  TSK-0327:')
end=graph.find('\n  TSK-',start+1)
block=graph[start:end if end>=0 else len(graph)]
req('target: TSK-0336' in block and 'type: depends_on' in block,'TSK0327_GRAPH_DEP')
print('TSK0327_GRAPH_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
req('TSK-0336' in runtime and 'NOT_APPLICABLE' in runtime and 'PASS' in runtime,'TSK0327_TSK0336_EXCLUSION')
req('## TSK-0333 current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,'TSK0327_TSK0333_CURRENT')
print('TSK0327_CURRENT_PREDECESSOR_CONTEXT=PASS')

expected={
'prototype/TSK-0333/index.html':'9395f0e105d20683b5beafa01b02d7b300e79a8d',
'prototype/TSK-0333/model.mjs':'9b7c239024d8ae24371b687aa39de6fa6b2b62b6',
'prototype/TSK-0333/app.mjs':'476ea932d95592fabf586f7ba381be0d346117fe',
'prototype/TSK-0333/prototype.css':'6f8af459a0b0b1c9ec132657dfcd7ebff43090b8',
'TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md':'4de73da09d637a142fc9968873ffdd755fdb07f3',
'TSK_0333_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md':'d1427b8bdd64772aab82683220af9becaf07f2ac',
'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md':'1836484278e741a041dea172ddc63edf9053ef6a',
}
for p,h in expected.items():
    req(blob(p)==h,f'TSK0327_BLOB_MISMATCH={p}')
print('TSK0327_CURRENT_SOURCE_BLOBS=PASS')

cand=CAND.read_text(encoding='utf-8')
for s in [
'2.0.0-post-cr0007','CR-0006','CR-0007','account/session','dashboard/device management',
'configured SafeWeb DNS removal was not reachable','TSK0333_BROWSER_REMOVAL_RECOVERY=PASS',
'No unresolved critical/high trust-state finding remains','No unresolved critical/high barrier is established',
'No human comprehension/usability claim is made before L8','TSK-0321 retains the separate HUMAN_ONLY accessibility-review acceptance boundary'
]: req(s in cand,f'TSK0327_CANDIDATE_MISSING={s}')
print('TSK0327_CURRENT_FINDINGS_DISPOSITION=PASS')

an=AN.read_text(encoding='utf-8')
det=DET.read_text(encoding='utf-8')
for s in ['33432762152','99621849637','TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS']:
    req(s in an or s in det,f'TSK0327_TSK0333_EVIDENCE_MISSING={s}')
for s in [
'TSK0333_BROWSER_KEYBOARD=PASS','TSK0333_BROWSER_ACCOUNTLESS_ANDROID=PASS','TSK0333_BROWSER_REMOVAL_RECOVERY=PASS',
'TSK0333_BROWSER_NEW_ACCOUNT=PASS','TSK0333_BROWSER_RETURNING_DASHBOARD=PASS','TSK0333_BROWSER_DEVICE_REPLACEMENT=PASS',
'TSK0333_BROWSER_PROVIDER_ERROR=PASS','TSK0333_BROWSER_SESSION_LOGOUT_DELETE_BOUNDARY=PASS',
'TSK0333_BROWSER_RTL_RESPONSIVE=PASS','TSK0333_BROWSER_PRIVACY_NO_TRANSPORT=PASS','TSK0333_BROWSER_NO_CONSOLE_ERRORS=PASS'
]: req(s in det,f'TSK0327_BROWSER_MARKER_MISSING={s}')
print('TSK0327_CURRENT_RETEST_EVIDENCE=PASS')

req('No failed run changed runtime PASS state' in cand,'TSK0327_FAILURE_FENCE')
req('RSK-0002' in cand,'TSK0327_RISK_FENCE')
print('TSK0327_PASS_FENCE=PASS')
print('TSK0327_POST_CR0007_VERIFICATION=PASS')
