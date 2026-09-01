import json, subprocess
from pathlib import Path

MD=Path('prototype/TSK-0324/UI_COMPONENT_RULES.md')
JS=Path('prototype/TSK-0324/COMPONENT_CONTRACT.json')
EXPECTED={
'MD':'0b7012a12070f7eccf45a1bbb2f453fde8507ff6',
'JS':'dc1f767025c2b016274d247d997411128105c5e4',
'WBS':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'RUNTIME':'e1c183ee32301a98c4c1c7dd3a4aa59d2d9f074f',
'TSK0322_GUIDE':'9344140b48ec99e0bd14639ac6640b581ee66d9f',
'TSK0322_POLICY':'b4d8d144a8aac26114848542729bf2ac4aeee8d6',
'TOKENS':'cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f',
'COMPONENTS':'831e92a74b6dda04252d93242cb33bd491a02381',
}
PATHS={'MD':str(MD),'JS':str(JS),'WBS':'Plans/Master/WBS/master-wbs.csv','RUNTIME':'CURRENT_STATE.md','TSK0322_GUIDE':'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md','TSK0322_POLICY':'content/TSK-0322/POLICY.json','TOKENS':'brand/system/TSK-0300/tokens.css','COMPONENTS':'brand/system/TSK-0300/components.css'}
def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for k,h in EXPECTED.items(): req(blob(PATHS[k])==h,f'TSK0324_INPUT_STALE={k}')

text=MD.read_text(encoding='utf-8')
repls={
'**Version:** 1.0.0  ':'**Version:** 1.1.0-post-cr0007',
'**Sequencing:** DEC-0052 / CR-0005  ':'**Sequencing:** DEC-0053 / CR-0006 + DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains the pre-L8 human-evidence rule',
'1. current owner-frozen planning authority and DEC-0052 / CR-0005;':'1. current owner-frozen planning authority including DEC-0053 / CR-0006 and DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains applicable to pre-L8 human-evidence claims;',
'Older TSK-0300/0320 sequencing text that references CR-0003/CR-0004 is superseded for sequencing by current DEC-0052/CR-0005; the still-valid visual/state rules remain usable unless separately contradicted.':'Older TSK-0300/0320 sequencing text that references CR-0003/CR-0004 is superseded by current owner-approved sequencing. The still-valid visual/state rules remain usable unless separately contradicted. Current Version 1 is dual-mode: complete core product value remains usable without login, while optional parent account/session, saved-device continuity, and lightweight dashboard/device-management surfaces are allowed. Account, session, saved-device, or dashboard presence never establishes technical verification.',
'SafeWeb UI is whitespace-led, mobile-first, calm and task-directed. Product/setup surfaces are operational rather than dashboard-like; public surfaces may carry more brand expression, but proposition and next action outrank decoration.':'SafeWeb UI is whitespace-led, mobile-first, calm and task-directed. Core setup surfaces are operational rather than dashboard-like; the optional signed-in dashboard remains lightweight and task-directed rather than dense administration chrome. Public surfaces may carry more brand expression, but proposition and next action outrank decoration.',
'| `BrandHeader` | `header` + `nav` where present | approved logo master; `SafeWeb` alt; no account/dashboard nav in current baseline |':'| `BrandHeader` | `header` + `nav` where present | approved logo master; `SafeWeb` alt; accountless core navigation remains available; optional sign-in/account/dashboard navigation may appear where current IA permits; visible keyboard focus |',
'No text input, identity field, child profile field, payment field or diagnostic upload is part of the current critical journey. Adding one requires separate necessity, privacy and scope authority rather than a local component variant.':'No SafeWeb password/credential field, child profile field, payment field or diagnostic upload is part of the current critical journey. Optional Google sign-in/account continuity uses the separately approved account/session flow and must not create a local credential form. Adding materially broader identity, child, payment, activity-history or diagnostic collection requires separate necessity, privacy and scope authority rather than a local component variant.',
'Reviewed 2026-08-29 against current first-party W3C sources:':'Reviewed 2026-09-01 against current first-party W3C sources:',
'- no token/logo/state/claim/account fork is created.':'- optional account/session/dashboard/device-lifecycle controls preserve accountless core access, keyboard/focus semantics, truthful protection state, explicit destructive consequences, and uncertainty on unknown destructive results;\n- no token/logo/state/claim/account fork is created.'
}
for old,new in repls.items():
    req(old in text,f'TSK0324_EXPECTED_TEXT_MISSING={old[:100]}')
    text=text.replace(old,new,1)
anchor='### Target size\n\nButtons generated from the existing padding/type tokens must be verified in implementation to meet the WCAG 2.2 AA target-size requirement. Inline text links may use the standard inline-content exception when applicable; clustered navigation links must retain sufficient target size/spacing.'
req(anchor in text,'TSK0324_TARGET_ANCHOR_MISSING')
addition=anchor+'''\n\n### Optional account/session/dashboard and lifecycle controls\n\n- Sign-in, account and dashboard navigation is optional continuity UI; it must never gate `Start setup`, verification, Help, recovery or removal.\n- Session/account status is announced as account state only and must never reuse S1–S6 protection-state styling as evidence of device protection.\n- A saved-device card distinguishes saved record metadata from current Protection Map evidence; record presence cannot create `Verified`.\n- Logout, account deletion, saved-record deletion, revoke/unlink and physical SafeWeb DNS removal use distinct labels and consequences.\n- Destructive account/device actions require the current lifecycle confirmation pattern, keyboard-operable controls, visible focus, and a deterministic return/focus target after completion or cancellation.\n- If a destructive provider result is unknown, the UI states uncertainty, blocks duplicate destructive replay and offers authoritative read-back/recovery; it never announces success.\n- At 320 px, optional account/dashboard navigation may collapse or wrap but cannot hide the accountless core path, current protection truth, recovery or removal.\n- Dashboard/device-management surfaces remain lightweight: no browsing/query/activity history, child profiles/accounts or broad/raw DNS administration.''' 
text=text.replace(anchor,addition,1)
MD.write_text(text,encoding='utf-8')

p=json.loads(JS.read_text(encoding='utf-8'))
req(p['version']=='1.0.0','TSK0324_JSON_VERSION')
p['version']='1.1.0-post-cr0007'
p['sequencing']='DEC-0053/CR-0006 + DEC-0054/CR-0007; DEC-0052/CR-0005 pre-L8 human-evidence rule retained'
p['shared_sources']['language_policy']['blob']='9344140b48ec99e0bd14639ac6640b581ee66d9f'
p['shared_sources']['wbs']['blob']='f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
p['wcag_source_review']['reviewed_date']='2026-09-01'
p['dual_mode_scope']={
'accountless_core_required':True,'optional_parent_account_session':True,'lightweight_dashboard_device_management':True,
'mandatory_login_for_core':False,'account_device_dashboard_presence_is_technical_verification':False,
'browsing_query_activity_history':False,'child_accounts_profiles':False,'broad_raw_dns_administration':False,
'automatic_j0_j1_account_linkage':False}
for c in p['components']:
    if c['name']=='BrandHeader':
        c['requirements']=['approved identity','accountless core navigation available','optional account/dashboard navigation only where current IA permits','visible focus']
extra=[
{"name":"AccountContinuityNav","semantic":"nav/native links or buttons","keyboard":"native reading order","requirements":["optional only","never gates core","visible focus","session state text"]},
{"name":"SessionStatus","semantic":"status/text","keyboard":"n/a","requirements":["account state only","never protection evidence","truthful expiry/error"]},
{"name":"SavedDeviceCard","semantic":"section/article","keyboard":"native actions","requirements":["record metadata distinct from protection evidence","no record-presence verification","responsive"]},
{"name":"LifecycleConfirmation","semantic":"dialog/confirmation region when required","keyboard":"contained logical order and deterministic return focus","requirements":["explicit consequence","cancel available where applicable","unknown result is uncertain","no duplicate destructive replay"]}
]
names={c['name'] for c in p['components']}
for c in extra:
    if c['name'] not in names: p['components'].append(c)
for item in ['browsing/query/activity history UI','child accounts/profiles','broad/raw DNS administration','account/device/dashboard presence as technical verification','automatic J0/J1 account linkage']:
    if item not in p['forbidden_scope']: p['forbidden_scope'].append(item)
p['account_lifecycle_ui']={
'logout_distinct_from_dns_removal':True,'account_delete_distinct_from_dns_removal':True,'saved_record_delete_distinct_from_dns_removal':True,
'revoke_unlink_distinct_from_dns_removal':True,'unknown_destructive_result_announces_success':False,'automatic_destructive_replay_on_unknown_result':False,
'confirmation_keyboard_operable':True,'deterministic_focus_return_required':True}
JS.write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('TSK0324_BOUNDED_UPDATE=PASS')
