import csv, subprocess
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
BASE=ROOT/'design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md'
AMD=ROOT/'design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md'
OWNER=ROOT/'TSK_0334_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md'
PREP=ROOT/'TSK_0334_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md'
OLDDET=ROOT/'TSK_0334_POST_CR0007_DETERMINISTIC_ACCEPTANCE_EVIDENCE_2026-08-31.md'
EXPECTED={
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 RUNTIME:'d0fc4fd26949f718e96d8cccb5fc81709569bc71',
 BASE:'44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f',
 AMD:'de423bdb8aeb2b0a0f25a85850be380cfab7e67d',
 OWNER:'ece3d3cb92829a84877ad62bf59f89b453223942',
 PREP:'652845396bc62a1df859b2a9f1944576268066b6',
 OLDDET:'33941cefac1aa2c67192f7da90a611d48bd72396',
}
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,e in EXPECTED.items():
    req(p.exists(),f'TSK0334_REVAL_MISSING={p.as_posix()}')
    req(blob(p)==e,f'TSK0334_REVAL_BLOB_CHANGED={p.as_posix()}')
print('TSK0334_REVAL_EXACT_BLOBS=PASS')
with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0334')
req(row.get('Dependencies')=='TSK-0330','TSK0334_REVAL_DEP_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0334' and row.get('Verification_ID')=='VER-0334' and row.get('Evidence_ID')=='EVD-0334','TSK0334_REVAL_IDS_CHANGED')
req(row.get('Action_Authority')=='HUMAN_ONLY','TSK0334_REVAL_AUTH_CHANGED')
print('TSK0334_REVAL_WBS_CONTRACT=PASS')
runtime=RUNTIME.read_text(encoding='utf-8')
req('## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,'TSK0334_REVAL_CURRENT_DEP_MISSING')
req('## TSK-0334 current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,'TSK0334_REVAL_CURRENT_SECTION_MISSING')
print('TSK0334_REVAL_DEPENDENCY_COMPLETE=PASS')
base=BASE.read_text(encoding='utf-8').lower(); amd=AMD.read_text(encoding='utf-8').lower()
for i in range(1,6): req(f'sup-0{i}' in base,f'TSK0334_REVAL_SUP_MISSING={i}')
for i in range(6,9): req(f'sup-0{i}' in amd,f'TSK0334_REVAL_SUP_MISSING={i}')
for doc,label,minimum in ((base,'BASE',5),(amd,'AMD',3)):
    for field in ('accessible path','minimal diagnostic','protection consequence','escalation','success state'):
        req(doc.count(field)>=minimum,f'TSK0334_REVAL_{label}_FIELD_MISSING={field}')
print('TSK0334_REVAL_ACC_COVERAGE=PASS')
owner=OWNER.read_text(encoding='utf-8')
req('APPROVE TSK-0334 POST-CR-0007 CURRENT-SCOPE SUPPORT AMENDMENT' in owner,'TSK0334_REVAL_OWNER_APPROVAL_MISSING')
req('44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f' in owner and 'de423bdb8aeb2b0a0f25a85850be380cfab7e67d' in owner,'TSK0334_REVAL_OWNER_BINDING_CHANGED')
print('TSK0334_REVAL_OWNER_AUTHORITY=PASS')
print('TSK0334_DEPENDENCY_COMPLETE_REVALIDATION=PASS')
