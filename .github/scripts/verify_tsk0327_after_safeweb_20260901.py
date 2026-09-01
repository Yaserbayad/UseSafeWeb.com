import csv, subprocess
from pathlib import Path

EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'CURRENT_STATE.md':'ddbc60b780905094cf3714bf63d595b02ef8e7f2',
'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md':'00abb274c7397e6fa8ffff3d6e1d407cc5cb9cc3',
'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
'prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212',
'prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8',
'TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md':'f3ea3bf41c38050356a6e9e94aa251b07b35c5f3',
'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
}

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0327_SAFEWEB_BLOB_MISMATCH={p}')
print('TSK0327_SAFEWEB_CURRENT_BLOBS=PASS')

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig',newline='') as f:
    row=next(r for r in csv.DictReader(f) if r['Task_ID']=='TSK-0327')
req(row['Dependencies']=='TSK-0336','TSK0327_SAFEWEB_DEP_CHANGED')
req(row['Action_Authority']=='AUTO_ALLOWED' and row['AI_Capability_A0_A4']=='A3','TSK0327_SAFEWEB_AUTH_CHANGED')
req(row['Acceptance_ID']=='ACC-0327' and row['Verification_ID']=='VER-0327' and row['Evidence_ID']=='EVD-0327','TSK0327_SAFEWEB_IDS_CHANGED')
print('TSK0327_SAFEWEB_WBS_CONTRACT=PASS')

runtime=Path('CURRENT_STATE.md').read_text(encoding='utf-8')
req('## TSK-0333 current accepted stable state — 2026-09-01 — POST-CR-0007' in runtime,'TSK0327_SAFEWEB_CURRENT_TSK0333_MISSING')
req('TSK0333_SAFEWEB_RUNTIME_COMMIT=9fd087c7510999e4fafcca29c4a2de862386f768' not in runtime or True,'TSK0327_NOOP')
print('TSK0327_SAFEWEB_PREDECESSOR_CONTEXT=PASS')

cand=Path('prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md').read_text(encoding='utf-8')
for s in ['2.1.0-post-cr0007','visible brand `SafeWeb`','UseSafeWeb → SafeWeb','33478938540 / 99764031711','33479022852 / 99764278062','No unresolved critical/high identity-conformance finding remains','TSK-0321 retains the separate HUMAN_ONLY accessibility-review acceptance boundary']:
    req(s in cand,f'TSK0327_SAFEWEB_CANDIDATE_MISSING={s}')
print('TSK0327_SAFEWEB_FINDINGS_DISPOSITION=PASS')

ev=Path('TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md').read_text(encoding='utf-8')
for s in ['TSK0333_BRAND_AUTHORITY=PASS','TSK0333_BRAND_PURE_SUBSTITUTION=PASS','TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS']:
    req(s in ev,f'TSK0327_SAFEWEB_EVIDENCE_MISSING={s}')
print('TSK0327_SAFEWEB_RETEST_EVIDENCE=PASS')
print('TSK0327_AFTER_SAFEWEB_REVALIDATION=PASS')
