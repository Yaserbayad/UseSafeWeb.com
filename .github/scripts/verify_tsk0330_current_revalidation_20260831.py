import csv, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
CANDIDATE=ROOT/'design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md'
PREP=ROOT/'TSK_0330_PHONE_INTERNET_SERVICES_FLOW_PREPARATION_EVIDENCE_2026-08-29.md'
ACCEPT=ROOT/'TSK_0330_PHONE_INTERNET_SERVICES_FLOW_ACCEPTANCE_EVIDENCE_2026-08-29.md'

EXPECTED={
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 RUNTIME:'7ec16c5099c0a450bcac35da218a70692f51d9af',
 CANDIDATE:'07fa10b3fa9b91ddd02f19f5d1c68b15184677a7',
 PREP:'a595b4cafaac10ae6262e296c6b5d482945d4e45',
 ACCEPT:'794e12b56e902270f6d4ef052abaa2d1fba1963b',
}

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

for p,e in EXPECTED.items():
    req(p.exists(),f'TSK0330_MISSING={p.as_posix()}')
    req(blob(p)==e,f'TSK0330_BLOB_CHANGED={p.as_posix()}')
print('TSK0330_EXACT_INPUT_BLOBS=PASS')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0330')
expected_acc='Each flow has prerequisites, step-by-step actions, verification/confirmation, skip conditions, unsupported/conflict states, troubleshooting, and no misleading completion state.'
req(row.get('Dependencies')=='TSK-0146','TSK0330_DEPENDENCY_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0330' and row.get('Verification_ID')=='VER-0330' and row.get('Evidence_ID')=='EVD-0330','TSK0330_IDS_CHANGED')
req(row.get('Acceptance_Criteria')==expected_acc,'TSK0330_ACCEPTANCE_CHANGED')
req(row.get('AI_Capability_A0_A4')=='A1' and row.get('Action_Authority')=='HUMAN_ONLY','TSK0330_AUTHORITY_CHANGED')
print('TSK0330_CURRENT_WBS_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
req('## TSK-0146 current accepted stable state' in runtime,'TSK0330_TSK0146_CURRENT_PASS_MISSING')
req('## TSK-0330 current accepted stable state' not in runtime,'TSK0330_PREMATURE_CURRENT_PASS')
req('## TSK-0330 accepted stable state — 2026-08-29' in runtime,'TSK0330_HISTORICAL_APPROVAL_RECORD_MISSING')
req('CR-0006 current execution boundary' in runtime and 'accountless core plus optional parent account' in runtime,'TSK0330_CURRENT_DUAL_MODE_SCOPE_MISSING')
print('TSK0330_CURRENT_DEPENDENCY_AND_SCOPE=PASS')

candidate=CANDIDATE.read_text(encoding='utf-8').lower()
for token in ('prerequisites','step-by-step','verification','confirmation','skip condition','unsupported','conflict','troubleshooting','removed','protection map completion'):
    req(token in candidate,f'TSK0330_ACC_ELEMENT_MISSING={token}')
for case in range(1,13):
    req(f'tc-0330-{case:02d}' in candidate,f'TSK0330_CASE_MISSING={case}')
for token in ('dns.usesafeweb.com','https://dns.usesafeweb.com/dns-query','parent confirmation is not system verification','one layer never certifies another','zero external services is valid'):
    req(token in candidate,f'TSK0330_TRUTH_GUARD_MISSING={token}')
# The artifact is accountless-first and says this setup flow does not introduce account/dashboard scope;
# that is compatible with current dual-mode V1 because the complete core must remain usable without login.
req('accountless-first' in candidate,'TSK0330_ACCOUNTLESS_CORE_MISSING')
req('no persistent dashboard/account scope' in candidate,'TSK0330_FLOW_SCOPE_BOUNDARY_MISSING')
print('TSK0330_CANDIDATE_CURRENT_ACC=PASS')

accept=ACCEPT.read_text(encoding='utf-8')
req('APPROVE TSK-0330 PHONE INTERNET SERVICES FLOWS' in accept,'TSK0330_OWNER_APPROVAL_MISSING')
req('07fa10b3fa9b91ddd02f19f5d1c68b15184677a7' in accept,'TSK0330_OWNER_APPROVED_BLOB_MISSING')
req('33280241901' in accept and '99174073706' in accept and 'SUCCESS' in accept,'TSK0330_OWNER_BOUND_VERIFICATION_MISSING')
print('TSK0330_EXISTING_HUMAN_AUTHORITY=PASS')

print('TSK0330_CURRENT_REVALIDATION=PASS')
