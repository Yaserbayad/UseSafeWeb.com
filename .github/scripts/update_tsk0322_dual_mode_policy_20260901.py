import json, subprocess
from pathlib import Path

GUIDE=Path('content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md')
POLICY=Path('content/TSK-0322/POLICY.json')
EXPECTED={
'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md':'d12c1e707f0390915002b27bf3a5073d0135d466',
'content/TSK-0322/POLICY.json':'97c214504ceeeadebd92a79069e081311d60dd99',
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'CURRENT_STATE.md':'586a36d156ad05f1bc07298fda8328e9c54de027',
'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md':'00abb274c7397e6fa8ffff3d6e1d407cc5cb9cc3',
}

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0322_INPUT_STALE={p}')

text=GUIDE.read_text(encoding='utf-8')
repls={
'**Version:** 1.0.0':'**Version:** 2.0.0-post-cr0007',
'**Action authority:** A3 / AUTO_ALLOWED':'**Action authority:** A4 / AUTO_ALLOWED',
'**Current sequencing:** DEC-0052 / CR-0005':'**Current sequencing:** DEC-0053 / CR-0006 + DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains the pre-L8 no-human-evidence rule',
'It consolidates the accepted verbal-system intent from TSK-0299, the protection-state semantics owned by TSK-0320, the current visible-identity rule owned by TSK-0297/TSK-0301, and the frozen implementation-ready experience baseline TSK-0309.':'It consolidates the accepted verbal-system intent from TSK-0299, the protection-state semantics owned by TSK-0320, the visible-identity rule owned by TSK-0297/TSK-0301, and the current dual-mode Version-1 product/experience baseline proven through TSK-0146 and the corrected integrated TSK-0333 prototype.',
'- pre-product human/user validation is not claimed and is not required before L8 under DEC-0052/CR-0005.':'- current Version 1 is dual-mode: the complete core setup/protection journey remains usable without login, while an optional parent account/session, minimum saved-device ownership persistence, lightweight dashboard/device management, and bounded account/device lifecycle flows are approved under DEC-0053/CR-0006;\n- mandatory login for core value, browsing/query/activity history, child accounts/profiles, broad/raw DNS administration, automatic J0/J1-to-account linkage, and treating account/device/dashboard presence as technical verification remain prohibited;\n- pre-product human/user validation is not claimed and is not required before L8 under DEC-0052/CR-0005.',
'- `You do not need a SafeWeb account for the current setup journey.`':'- `You do not need a SafeWeb account for the core setup, verification, help, recovery, or removal journey.`',
'### Control/recovery\n\n- `You can remove the supported SafeWeb DNS configuration and follow recovery guidance.`':'### Optional account continuity\n\n- `You can use SafeWeb without signing in; an optional parent account can provide continuity and a lightweight saved-device dashboard.`\n- `A saved device or signed-in account does not by itself mean protection is Verified.`\n- `Logging out changes account access only; it does not remove SafeWeb DNS from a device.`\n- `Deleting a saved device record is different from removing SafeWeb DNS from the physical device.`\n\nThese claims authorize only the bounded current Version-1 account/dashboard scope. They do not authorize browsing/activity history, child profiles/accounts, broad DNS administration, automatic anonymous-to-account linkage, or a stronger protection claim.\n\n### Control/recovery\n\n- `You can remove the supported SafeWeb DNS configuration and follow recovery guidance.`',
'| `Available in [market]` | Separate market/legal/publication authority exists; language availability alone is insufficient. |':'| `Saved in your dashboard` | The parent is signed in, the device record is explicitly saved/owned, and the product does not present record presence as technical verification. |\n| `Signed in` / `Session ended` | Current account/session state only; wording must not rewrite physical protection truth. |\n| `Available in [market]` | Separate market/legal/publication authority exists; language availability alone is insufficient. |',
'- shield/padlock/certification language or iconography used to imply guaranteed/certified safety.':'- shield/padlock/certification language or iconography used to imply guaranteed/certified safety;\n- wording that makes login/account creation mandatory for core setup, verification, help, recovery, or removal;\n- wording that implies browsing/query/activity history, child accounts/profiles, or broad/raw DNS administration exists in the current product;\n- wording that treats sign-in, account ownership, saved-device presence, or dashboard presence as technical `Verified`;\n- wording that implies automatic J0/J1 import, promotion, linkage, or expiry extension from sign-in/account activity;\n- wording that conflates logout, account deletion, saved-record deletion, revoke/unlink, anonymous-state deletion, and physical SafeWeb DNS removal;\n- wording that reports an unknown destructive-operation result as success or encourages automatic destructive replay.',
'| New product capability/account/dashboard claim | Product scope/exception owner authority |':'| Ordinary optional-account/dashboard copy inside the frozen DEC-0053 Version-1 scope | Content (TSK-0322 owner), preserving product/privacy/truth authorities |\n| New or materially broader product capability/account/dashboard claim | Project Owner / product-scope authority |',
'10. no claim implies an account/dashboard/activity-history product exists in the current baseline;':'10. optional account/dashboard copy never implies mandatory login for core value, browsing/query/activity surveillance, child accounts/profiles, broad/raw DNS administration, automatic J0/J1 linkage, or technical verification from account/device/dashboard presence;',
'12. technical endpoint strings remain exact.':'12. technical endpoint strings remain exact;\n13. logout, account deletion, saved-record deletion, revoke/unlink, anonymous-state deletion, and physical SafeWeb DNS removal remain distinct in user-facing language;\n14. unknown destructive results remain explicitly uncertain and never imply automatic replay or success.'
}
for old,new in repls.items():
    req(old in text,f'TSK0322_EXPECTED_GUIDE_TEXT_MISSING={old[:80]}')
    text=text.replace(old,new,1)
req('no claim implies an account/dashboard/activity-history product exists in the current baseline' not in text,'TSK0322_STALE_QA_REMAINS')
for s in ['2.0.0-post-cr0007','optional parent account/session','optional parent account can provide continuity','A saved device or signed-in account does not by itself mean protection is Verified','automatic J0/J1','unknown destructive results','visible brand/product identity: **`SafeWeb`**']:
    req(s in text,f'TSK0322_GUIDE_CURRENT_SCOPE_MISSING={s}')
GUIDE.write_text(text,encoding='utf-8')

p=json.loads(POLICY.read_text(encoding='utf-8'))
p['schema']='usesafeweb.product-language-policy.v2'
p['version']='2.0.0-post-cr0007'
p['action_authority']='A4_AUTO_ALLOWED'
p['scope_authority']=['DEC-0053/CR-0006','DEC-0054/CR-0007','DEC-0052/CR-0005-pre-L8-evidence-rule']
p['product_scope']={
    'accountless_core_required': True,
    'optional_parent_account_session': True,
    'minimum_saved_device_ownership_persistence': True,
    'lightweight_dashboard_device_management': True,
    'bounded_account_device_lifecycle': True,
    'mandatory_login_for_core': False,
    'browsing_query_activity_history': False,
    'child_accounts_profiles': False,
    'broad_raw_dns_administration': False,
    'automatic_j0_j1_account_linkage': False
}
for item in [
'account_or_saved_device_presence_never_equals_verified',
'provider_or_session_failure_never_rewrites_physical_protection_truth',
'logout_account_delete_record_delete_revoke_unlink_and_physical_dns_removal_are_distinct',
'unknown_destructive_result_never_implies_success_or_automatic_replay'
]:
    if item not in p['truth_invariants']: p['truth_invariants'].append(item)
p['approved_claims']=[x for x in p['approved_claims'] if x!='You do not need a SafeWeb account for the current setup journey.']
for item in [
'You do not need a SafeWeb account for the core setup, verification, help, recovery, or removal journey.',
'An optional parent account can provide continuity and a lightweight saved-device dashboard.',
'A saved device or signed-in account does not by itself mean protection is Verified.',
'Logging out changes account access only; it does not remove SafeWeb DNS from a device.',
'Deleting a saved device record is different from removing SafeWeb DNS from the physical device.'
]:
    if item not in p['approved_claims']: p['approved_claims'].append(item)
for item in [
'mandatory_login_for_core_value',
'browsing_query_activity_history_product',
'child_accounts_or_profiles',
'broad_or_raw_dns_administration',
'account_device_or_dashboard_presence_as_technical_verification',
'automatic_j0_j1_to_account_linkage_or_expiry_extension',
'lifecycle_operation_conflation',
'unknown_destructive_result_as_success_or_automatic_replay'
]:
    if item not in p['prohibited_claim_classes']: p['prohibited_claim_classes'].append(item)
p['review_ownership']['ordinary_optional_account_dashboard_copy']='Content_within_DEC-0053_scope'
p['review_ownership']['material_product_scope_change']='Project_Owner_product_scope_authority'
p['review_ownership'].pop('new_product_account_dashboard_claim',None)
POLICY.write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

req(json.loads(POLICY.read_text(encoding='utf-8'))['visible_brand']=='SafeWeb','TSK0322_VISIBLE_BRAND_CHANGED')
print('TSK0322_DUAL_MODE_POLICY_UPDATE=PASS')
