import csv, subprocess
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
BASE=ROOT/'design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md'
AMD=ROOT/'design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md'

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
req(blob(WBS)=='f3c29b5db8b835ef2c896f61335656ea51d8ba1c','WBS_CHANGED')
req(blob(RUNTIME)=='f735ab7b68cd0231dc3515739992242d67f5193e','RUNTIME_CHANGED')
req(blob(BASE)=='44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f','BASE_CHANGED')
req(blob(AMD)=='de423bdb8aeb2b0a0f25a85850be380cfab7e67d','AMENDMENT_CHANGED')
with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0334')
req(row.get('Dependencies')=='TSK-0330','DEP_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0334' and row.get('Verification_ID')=='VER-0334' and row.get('Evidence_ID')=='EVD-0334','ACC_CHANGED')
req(row.get('Action_Authority')=='HUMAN_ONLY','AUTHORITY_CHANGED')
print('TSK0334_WBS_HUMAN_BOUNDARY=PASS')
base=BASE.read_text(encoding='utf-8').lower(); amd=AMD.read_text(encoding='utf-8').lower()
for i in range(1,6): req(f'sup-0{i}' in base,f'BASE_SUP{i}_MISSING')
for i in range(6,9): req(f'sup-0{i}' in amd,f'AMD_SUP{i}_MISSING')
for section in ('accessible path','minimal diagnostic request','protection consequence','escalation','success state'):
    req(amd.count(section)>=3,f'AMD_FIELD_MISSING={section}')
for token in ('account-only','ownership mismatch','authoritative','no automatic replay','without login','physical usesafeweb','j0/j1','browsing/query/activity history'):
    req(token in amd,f'AMD_SEMANTIC_MISSING={token}')
for i in range(1,17): req(f'tc-0334-c{i:02d}' in amd,f'CASE_MISSING={i}')
req('not approved / not pass' in amd and 'human_only' in amd,'HUMAN_PASS_FENCE_MISSING')
req('## TSK-0334 current accepted stable state' not in RUNTIME.read_text(encoding='utf-8'),'PREMATURE_CURRENT_PASS')
print('TSK0334_EIGHT_CATEGORY_COVERAGE=PASS')
print('TSK0334_CURRENT_SCOPE_SEMANTICS=PASS')
print('TSK0334_HUMAN_PASS_FENCE=PASS')
print('TSK0334_PREPARATION_VERIFICATION=PASS')
