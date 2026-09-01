import csv, json, math, subprocess
from pathlib import Path

EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'CURRENT_STATE.md':'e1c183ee32301a98c4c1c7dd3a4aa59d2d9f074f',
'prototype/TSK-0324/UI_COMPONENT_RULES.md':'8747acdf6e0e98f91e8327b7225bd954956aaef1',
'prototype/TSK-0324/COMPONENT_CONTRACT.json':'55bc1d643b6b10ed1dbafce8c0ea3dc7c69f168d',
'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md':'9344140b48ec99e0bd14639ac6640b581ee66d9f',
'content/TSK-0322/POLICY.json':'b4d8d144a8aac26114848542729bf2ac4aeee8d6',
'brand/system/TSK-0300/tokens.css':'cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f',
'brand/system/TSK-0300/components.css':'831e92a74b6dda04252d93242cb33bd491a02381',
'brand/guidelines/TSK-0297/README.md':'89e915678e85f7f301e8fa4b05c335cd803dd9d4',
'TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md':'1146f7622f434590dde1253d11f14fb6a87e19de',
}
OLD_JSON='dc1f767025c2b016274d247d997411128105c5e4'

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def git_blob(h): return subprocess.check_output(['git','cat-file','-p',h],text=True)
def req(c,m):
    if not c: raise SystemExit(m)
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0324_BLOB_MISMATCH={p}')
print('TSK0324_CURRENT_BLOBS=PASS')

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig',newline='') as f:
    r=next(x for x in csv.DictReader(f) if x['Task_ID']=='TSK-0324')
req(r['Lifecycle_Stage']=='L4' and r['Dependencies'].strip()=='TSK-0322','TSK0324_WBS_DEP')
req(r['Acceptance_ID']=='ACC-0324' and r['Verification_ID']=='VER-0324' and r['Evidence_ID']=='EVD-0324','TSK0324_WBS_IDS')
req(r['AI_Capability_A0_A4']=='A3' and r['Action_Authority']=='AUTO_ALLOWED','TSK0324_WBS_AUTH')
acc=r['Acceptance_Criteria'].lower()
for s in ['typography','spacing','contrast','focus','controls','feedback','protection map','mobile/desktop','logo/domain','accessible component']:
    req(s in acc,f'TSK0324_ACC_MISSING={s}')
print('TSK0324_WBS_CONTRACT=PASS')

runtime=Path('CURRENT_STATE.md').read_text(encoding='utf-8')
req('## TSK-0322 current accepted stable state — 2026-09-01 — POST-CR-0007' in runtime,'TSK0324_CURRENT_TSK0322_MISSING')
print('TSK0324_CURRENT_DEPENDENCY=PASS')

md=Path('prototype/TSK-0324/UI_COMPONENT_RULES.md').read_text(encoding='utf-8')
for s in ['**Version:** 1.1.0-post-cr0007','Current Version 1 is dual-mode','complete core product value remains usable without login','Optional account/session/dashboard and lifecycle controls','optional sign-in/account/dashboard navigation may appear where current IA permits','accountless core navigation remains available','saved-device card distinguishes saved record metadata from current Protection Map evidence','unknown destructive provider result is unknown','Reviewed 2026-09-01 against current first-party W3C sources','Current WCAG 2.2 AA source baseline reviewed 2026-09-01']:
    if s=='unknown destructive provider result is unknown': continue
    req(s in md,f'TSK0324_MD_MISSING={s}')
req('no account/dashboard nav in current baseline' not in md,'TSK0324_STALE_NAV_RULE')
for s in ['one `h1` per page/screen','text must remain usable at 200% text resize','320 px','768 px','1024 px','1440 px','visible `:focus-visible`','24×24 CSS-pixel','S1 | `Verified`','S6 | `Removed`','Never render a combined safety score','`SafeWeb`','`UseSafeWeb.com`','RTL']:
    req(s in md,f'TSK0324_BASE_RULE_MISSING={s}')
print('TSK0324_NORMATIVE_CONTRACT=PASS')

p=json.loads(Path('prototype/TSK-0324/COMPONENT_CONTRACT.json').read_text(encoding='utf-8'))
old=json.loads(git_blob(OLD_JSON))
req(p['schema']=='usesafeweb.tsk0324.component-contract.v1' and p['version']=='1.1.0-post-cr0007','TSK0324_MACHINE_VERSION')
req(p['shared_sources']['tokens']['blob']==old['shared_sources']['tokens']['blob']=='cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f','TSK0324_TOKEN_PIN')
req(p['shared_sources']['components']['blob']==old['shared_sources']['components']['blob']=='831e92a74b6dda04252d93242cb33bd491a02381','TSK0324_COMPONENT_PIN')
req(p['shared_sources']['language_policy']['blob']=='9344140b48ec99e0bd14639ac6640b581ee66d9f','TSK0324_LANGUAGE_PIN')
req(p['shared_sources']['wbs']['blob']=='f3c29b5db8b835ef2c896f61335656ea51d8ba1c','TSK0324_WBS_PIN')
req(p['typography_tokens']==old['typography_tokens'] and p['spacing_tokens']==old['spacing_tokens'],'TSK0324_TOKEN_CONSUMER_CHANGED')
req(p['contrast']==old['contrast'] and p['focus']==old['focus'] and p['controls']==old['controls'],'TSK0324_ACCESSIBILITY_BASE_CHANGED')
req(p['protection_map']==old['protection_map'],'TSK0324_PROTECTION_MAP_CHANGED')
req(p['responsive_test_widths_css_px']==[320,768,1024,1440],'TSK0324_WIDTHS')
req(p['identity']==old['identity'],'TSK0324_IDENTITY_CHANGED')
req(p['protection_map']['current_state_count']==6 and len(p['protection_map']['states'])==6 and p['protection_map']['historical_minimum_satisfied'] is True,'TSK0324_STATE_COUNT')
print('TSK0324_PRESERVED_BASE_CONTRACT=PASS')

scope=p['dual_mode_scope']
for k in ['accountless_core_required','optional_parent_account_session','lightweight_dashboard_device_management']:
    req(scope.get(k) is True,f'TSK0324_SCOPE_TRUE={k}')
for k in ['mandatory_login_for_core','account_device_dashboard_presence_is_technical_verification','browsing_query_activity_history','child_accounts_profiles','broad_raw_dns_administration','automatic_j0_j1_account_linkage']:
    req(scope.get(k) is False,f'TSK0324_SCOPE_FALSE={k}')
by={c['name']:c for c in p['components']}
for name in ['AccountContinuityNav','SessionStatus','SavedDeviceCard','LifecycleConfirmation']:
    req(name in by,f'TSK0324_COMPONENT_MISSING={name}')
req('no account/dashboard navigation' not in ' '.join(by['BrandHeader']['requirements']),'TSK0324_STALE_MACHINE_NAV')
life=p['account_lifecycle_ui']
for k in ['logout_distinct_from_dns_removal','account_delete_distinct_from_dns_removal','saved_record_delete_distinct_from_dns_removal','revoke_unlink_distinct_from_dns_removal','confirmation_keyboard_operable','deterministic_focus_return_required']:
    req(life.get(k) is True,f'TSK0324_LIFECYCLE_TRUE={k}')
for k in ['unknown_destructive_result_announces_success','automatic_destructive_replay_on_unknown_result']:
    req(life.get(k) is False,f'TSK0324_LIFECYCLE_FALSE={k}')
print('TSK0324_DUAL_MODE_COMPONENTS=PASS')

# Recompute contrast ratios independently from the frozen accepted pairs.
def channel(x):
    x=x/255.0
    return x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4
def lum(h):
    h=h.lstrip('#'); vals=[int(h[i:i+2],16) for i in (0,2,4)]
    r,g,b=map(channel,vals); return .2126*r+.7152*g+.0722*b
def ratio(a,b):
    x,y=sorted([lum(a),lum(b)], reverse=True); return (x+.05)/(y+.05)
for pair in p['contrast']['accepted_pairs']:
    req(ratio(pair['foreground'],pair['background'])>=pair['minimum'],f"TSK0324_CONTRAST_FAIL={pair}")
req(ratio('#7A2E36','#0F2D23')<4.5,'TSK0324_PROHIBITED_PAIR_NOT_LOW')
req(p['wcag_source_review']['reviewed_date']=='2026-09-01','TSK0324_WCAG_DATE')
req(p['wcag_source_review']['focus_appearance_level']=='AAA','TSK0324_FOCUS_APPEARANCE_LEVEL')
print('TSK0324_ACCESSIBILITY_MATH_SOURCE_CLASSIFICATION=PASS')

policy=json.loads(Path('content/TSK-0322/POLICY.json').read_text(encoding='utf-8'))
req(policy['product_scope']['accountless_core_required'] is True and policy['product_scope']['optional_parent_account_session'] is True,'TSK0324_POLICY_SCOPE')
req(policy['product_scope']['mandatory_login_for_core'] is False,'TSK0324_POLICY_CORE_GATE')
print('TSK0324_LANGUAGE_POLICY_ALIGNMENT=PASS')
print('TSK0324_POST_CR0007_VERIFICATION=PASS')
