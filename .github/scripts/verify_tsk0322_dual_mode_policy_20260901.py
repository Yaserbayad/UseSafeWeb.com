import csv, json, subprocess
from pathlib import Path

EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'CURRENT_STATE.md':'586a36d156ad05f1bc07298fda8328e9c54de027',
'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md':'9344140b48ec99e0bd14639ac6640b581ee66d9f',
'content/TSK-0322/POLICY.json':'b4d8d144a8aac26114848542729bf2ac4aeee8d6',
'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md':'00abb274c7397e6fa8ffff3d6e1d407cc5cb9cc3',
'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
}

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0322_BLOB_MISMATCH={p}')
print('TSK0322_CURRENT_BLOBS=PASS')

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig',newline='') as f:
    row=next(r for r in csv.DictReader(f) if r['Task_ID']=='TSK-0322')
req(row['Lifecycle_Stage']=='L4','TSK0322_LIFECYCLE')
req(row['Dependencies'].strip()=='TSK-0327','TSK0322_DEP')
req(row['Acceptance_ID']=='ACC-0322' and row['Verification_ID']=='VER-0322' and row['Evidence_ID']=='EVD-0322','TSK0322_IDS')
req(row['AI_Capability_A0_A4']=='A4' and row['Action_Authority']=='AUTO_ALLOWED','TSK0322_AUTH')
acc=row['Acceptance_Criteria'].lower()
for s in ['approved/prohibited claims','state','child-readable','reading-level','review ownership']:
    req(s in acc,f'TSK0322_ACC_MISSING={s}')
print('TSK0322_WBS_CONTRACT=PASS')

runtime=Path('CURRENT_STATE.md').read_text(encoding='utf-8')
req('## TSK-0327 current accepted stable state — 2026-09-01 — POST-CR-0007' in runtime,'TSK0322_CURRENT_TSK0327_MISSING')
req('version `2.1.0-post-cr0007`' in runtime,'TSK0322_TSK0327_VERSION_MISSING')
req('## TSK-0333 current accepted stable state — 2026-09-01 — POST-CR-0007' in runtime,'TSK0322_CURRENT_TSK0333_MISSING')
print('TSK0322_CURRENT_PREDECESSOR_CONTEXT=PASS')

guide=Path('content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md').read_text(encoding='utf-8')
for s in [
'**Version:** 2.0.0-post-cr0007','**Action authority:** A4 / AUTO_ALLOWED','visible brand/product identity: **`SafeWeb`**',
'current Version 1 is dual-mode','optional parent account/session','mandatory login for core value','browsing/query/activity history',
'automatic J0/J1-to-account linkage','account/device/dashboard presence as technical verification',
'optional parent account can provide continuity and a lightweight saved-device dashboard',
'A saved device or signed-in account does not by itself mean protection is Verified',
'Logging out changes account access only','Deleting a saved device record is different from removing SafeWeb DNS',
'unknown destructive results remain explicitly uncertain','Ordinary optional-account/dashboard copy inside the frozen DEC-0053 Version-1 scope'
]: req(s in guide,f'TSK0322_GUIDE_MISSING={s}')
req('no claim implies an account/dashboard/activity-history product exists in the current baseline' not in guide,'TSK0322_STALE_ACCOUNT_EXCLUSION')
for s in ['Your child is safe','Fully protected','100% safe online','monitor browsing']:
    req(s in guide,f'TSK0322_PROHIBITED_LIBRARY_MISSING={s}')
print('TSK0322_GUIDE_SEMANTICS=PASS')

p=json.loads(Path('content/TSK-0322/POLICY.json').read_text(encoding='utf-8'))
req(p['schema']=='usesafeweb.product-language-policy.v2' and p['version']=='2.0.0-post-cr0007','TSK0322_POLICY_VERSION')
req(p['visible_brand']=='SafeWeb','TSK0322_POLICY_BRAND')
req(p['action_authority']=='A4_AUTO_ALLOWED','TSK0322_POLICY_AUTH')
scope=p['product_scope']
for k in ['accountless_core_required','optional_parent_account_session','minimum_saved_device_ownership_persistence','lightweight_dashboard_device_management','bounded_account_device_lifecycle']:
    req(scope.get(k) is True,f'TSK0322_POLICY_SCOPE_TRUE={k}')
for k in ['mandatory_login_for_core','browsing_query_activity_history','child_accounts_profiles','broad_raw_dns_administration','automatic_j0_j1_account_linkage']:
    req(scope.get(k) is False,f'TSK0322_POLICY_SCOPE_FALSE={k}')
for inv in ['account_or_saved_device_presence_never_equals_verified','provider_or_session_failure_never_rewrites_physical_protection_truth','logout_account_delete_record_delete_revoke_unlink_and_physical_dns_removal_are_distinct','unknown_destructive_result_never_implies_success_or_automatic_replay']:
    req(inv in p['truth_invariants'],f'TSK0322_POLICY_INVARIANT={inv}')
for cls in ['mandatory_login_for_core_value','browsing_query_activity_history_product','child_accounts_or_profiles','broad_or_raw_dns_administration','account_device_or_dashboard_presence_as_technical_verification','automatic_j0_j1_to_account_linkage_or_expiry_extension','lifecycle_operation_conflation','unknown_destructive_result_as_success_or_automatic_replay']:
    req(cls in p['prohibited_claim_classes'],f'TSK0322_POLICY_PROHIBITED={cls}')
print('TSK0322_MACHINE_POLICY=PASS')

identity=Path('brand/identity/TSK-0301/README.md').read_text(encoding='utf-8')
req('visible product/brand name is exactly **SafeWeb**' in identity and 'do not render `UseSafeWeb`' in identity,'TSK0322_IDENTITY_AUTHORITY')
req('dns.usesafeweb.com' in guide and 'https://dns.usesafeweb.com/dns-query' in guide,'TSK0322_ENDPOINTS')
print('TSK0322_IDENTITY_ENDPOINT_FENCE=PASS')
print('TSK0322_DUAL_MODE_VERIFICATION=PASS')
