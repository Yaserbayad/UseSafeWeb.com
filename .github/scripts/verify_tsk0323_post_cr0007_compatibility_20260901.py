import csv, json, subprocess
from pathlib import Path

EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'CURRENT_STATE.md':'ff880a1c4853740d7fef48a5fc2fdee4575eb0fe',
'content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md':'f848372f7820ed9455fe80668e761bec741423ae',
'content/TSK-0323/CATALOGUE.json':'79753cc4916d38ed8d2f0ed6d01890e62df3fb04',
'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md':'9344140b48ec99e0bd14639ac6640b581ee66d9f',
'content/TSK-0322/POLICY.json':'b4d8d144a8aac26114848542729bf2ac4aeee8d6',
}
OLD_MD='bbe9ed90b205f2ca852ebdaefedf054446dd7f91'
OLD_JSON='842e18c5666a82d53e2d348715dd6b9198daa44c'

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def git_blob(h): return subprocess.check_output(['git','cat-file','-p',h],text=True)
def req(c,m):
    if not c: raise SystemExit(m)
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0323_BLOB_MISMATCH={p}')
print('TSK0323_CURRENT_BLOBS=PASS')

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig',newline='') as f:
    r=next(x for x in csv.DictReader(f) if x['Task_ID']=='TSK-0323')
req(r['Lifecycle_Stage']=='L4' and r['Dependencies'].strip()=='TSK-0322','TSK0323_WBS_DEP')
req(r['Acceptance_ID']=='ACC-0323' and r['Verification_ID']=='VER-0323' and r['Evidence_ID']=='EVD-0323','TSK0323_WBS_IDS')
req(r['AI_Capability_A0_A4']=='A3' and r['Action_Authority']=='AUTO_ALLOWED','TSK0323_WBS_AUTH')
acc=r['Acceptance_Criteria'].lower()
for s in ['platform/version applicability','source reference','last verified date','owner','expected result','fallback','test case','unsupported states']:
    req(s in acc,f'TSK0323_ACC_MISSING={s}')
print('TSK0323_WBS_CONTRACT=PASS')

runtime=Path('CURRENT_STATE.md').read_text(encoding='utf-8')
req('## TSK-0322 current accepted stable state — 2026-09-01 — POST-CR-0007' in runtime,'TSK0323_CURRENT_TSK0322_MISSING')
req('TSK_0322_POST_CR0007_DUAL_MODE_LANGUAGE_ACCEPTANCE_EVIDENCE_2026-09-01.md' in runtime,'TSK0323_TSK0322_CURRENT_EVIDENCE_MISSING')
print('TSK0323_CURRENT_DEPENDENCY=PASS')

p=json.loads(Path('content/TSK-0323/CATALOGUE.json').read_text(encoding='utf-8'))
old=json.loads(git_blob(OLD_JSON))
req(p['schema']=='usesafeweb.device-service-instructions.v1','TSK0323_SCHEMA')
req(p['version']=='1.0.1-post-cr0007' and p['last_source_review']=='2026-09-01','TSK0323_VERSION_DATE')
req(p['canonical_sources']['TSK-0322']['blob']=='9344140b48ec99e0bd14639ac6640b581ee66d9f','TSK0323_TSK0322_PIN')
req(len(p['records'])==12 and len(old['records'])==12,'TSK0323_RECORD_COUNT')
required=['platform_version_applicability','source_references','last_verified','owner','expected_result','fallback','unsupported_state','test_case','review_trigger']
for rec in p['records']:
    for k in required: req(bool(rec.get(k)),f"TSK0323_RECORD_FIELD={rec.get('id')}:{k}")
    req(rec['last_verified']=='2026-09-01',f"TSK0323_RECORD_DATE={rec['id']}")
old_by={x['id']:x for x in old['records']}
for rec in p['records']:
    before=dict(old_by[rec['id']]); after=dict(rec)
    before['last_verified']='2026-09-01'
    req(after==before,f"TSK0323_RECORD_SEMANTICS_CHANGED={rec['id']}")
print('TSK0323_RECORD_SEMANTICS=12/12_PASS')

scope=p['scope_compatibility']
truth={
'accountless_core_required':True,'optional_parent_account_session_allowed_elsewhere':True,
'lightweight_dashboard_saved_device_continuity_allowed_elsewhere':True,
'safeweb_login_required_for_instruction_core':False,
'account_session_saved_device_dashboard_presence_is_technical_verification':False,
'logout_or_account_record_deletion_equals_physical_dns_removal':False,
'browsing_query_activity_history':False,'child_identity_profiles':False,
'broad_raw_dns_administration':False,'automatic_j0_j1_account_linkage':False}
for k,v in truth.items(): req(scope.get(k) is v,f'TSK0323_SCOPE={k}')
for s in p['external_sources'].values(): req(s['checked']=='2026-09-01','TSK0323_SOURCE_REVIEW_DATE')
print('TSK0323_DUAL_MODE_SCOPE_FENCE=PASS')

md=Path('content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md').read_text(encoding='utf-8')
oldmd=git_blob(OLD_MD)
for s in ['**Version:** 1.0.1-post-cr0007','**Last source review:** 2026-09-01','Current Version 1 is dual-mode','Accountless core is preserved','Optional SafeWeb account/dashboard state is non-authoritative for technical protection','account, session, saved-device, or dashboard presence never establishes S1 `Verified`']:
    req(s in md,f'TSK0323_MD_CURRENT_SCOPE={s}')
req(md[md.index('## 4. Registry'):]==oldmd[oldmd.index('## 4. Registry'):],'TSK0323_PROCEDURE_BODY_CHANGED')
print('TSK0323_PROCEDURE_BODY_UNCHANGED=PASS')

policy=json.loads(Path('content/TSK-0322/POLICY.json').read_text(encoding='utf-8'))
req(policy['product_scope']['accountless_core_required'] is True and policy['product_scope']['optional_parent_account_session'] is True,'TSK0323_TSK0322_SCOPE')
req(policy['product_scope']['mandatory_login_for_core'] is False and policy['product_scope']['browsing_query_activity_history'] is False,'TSK0323_TSK0322_FENCES')
print('TSK0323_LANGUAGE_POLICY_ALIGNMENT=PASS')
print('TSK0323_POST_CR0007_VERIFICATION=PASS')
