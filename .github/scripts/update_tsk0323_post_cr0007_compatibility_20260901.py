import json, subprocess
from pathlib import Path

MD=Path('content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md')
JS=Path('content/TSK-0323/CATALOGUE.json')
EXPECTED={
'MD':'bbe9ed90b205f2ca852ebdaefedf054446dd7f91',
'JS':'842e18c5666a82d53e2d348715dd6b9198daa44c',
'WBS':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'RUNTIME':'ff880a1c4853740d7fef48a5fc2fdee4575eb0fe',
'TSK0322_GUIDE':'9344140b48ec99e0bd14639ac6640b581ee66d9f',
'TSK0322_POLICY':'b4d8d144a8aac26114848542729bf2ac4aeee8d6',
}
PATHS={
'MD':str(MD),'JS':str(JS),'WBS':'Plans/Master/WBS/master-wbs.csv','RUNTIME':'CURRENT_STATE.md',
'TSK0322_GUIDE':'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md','TSK0322_POLICY':'content/TSK-0322/POLICY.json'}
def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for k,h in EXPECTED.items(): req(blob(PATHS[k])==h,f'TSK0323_INPUT_STALE={k}')

text=MD.read_text(encoding='utf-8')
repls={
'**Version:** 1.0.0  ':'**Version:** 1.0.1-post-cr0007',
'**Current sequencing:** DEC-0052 / CR-0005  ':'**Current sequencing:** DEC-0053 / CR-0006 + DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains the pre-L8 human-evidence rule',
'**Last source review:** 2026-08-29  ':'**Last source review:** 2026-09-01',
'DEC-0052 / CR-0005 applies: no pre-product parent/user/participant evidence is claimed or required. Technical/source/device/browser/accessibility verification remains mandatory through L7; real-user validation begins only at the controlled L8 integrated-product pilot.':'Current Version 1 is dual-mode under DEC-0053 / CR-0006: the complete setup, verification, help, recovery, and removal core remains usable without login, while optional parent account/session, minimum saved-device ownership persistence, and lightweight dashboard/device management may exist on separate product surfaces. This device/service catalogue does not make account state part of instruction applicability unless a platform-owned prerequisite explicitly requires an external platform account. Account, session, saved-device, or dashboard presence never establishes S1 `Verified`. DEC-0052 / CR-0005 still applies to human evidence: no pre-L8 parent/user/participant evidence is claimed or required; technical/source/device/browser/accessibility verification remains mandatory through L7.',
'4. **Accountless by default.** SafeWeb never collects Apple/Google/provider credentials, child browsing/DNS history, or a persistent child/device profile for these instructions.':'4. **Accountless core is preserved.** These instructions never require SafeWeb sign-in for core setup, verification, help, recovery, or removal. SafeWeb never collects Apple/Google/provider credentials, child browsing/DNS history, or child identity/profile data for these instructions. Optional parent-account/session or saved-device metadata on separately approved product surfaces does not alter instruction applicability or verification truth.',
'## 3. Current external source set rechecked 2026-08-29':'## 3. Current external source set rechecked 2026-09-01',
}
for old,new in repls.items():
    req(old in text,f'TSK0323_EXPECTED_TEXT_MISSING={old[:100]}')
    text=text.replace(old,new,1)
marker='8. **No named external service is currently hard-coded.** The service layer supports zero or one service only when a separately current approved named-service instruction exists. Until then, the correct service outcome is skip/Not covered/uncertain.'
req(marker in text,'TSK0323_RULE8_MISSING')
text=text.replace(marker, marker+'\n9. **Optional SafeWeb account/dashboard state is non-authoritative for technical protection.** Sign-in, session, ownership, saved-device, or dashboard presence may support continuity only; it never upgrades S2/S3/S4/S5/S6 to S1, never changes a physical DNS state by itself, and never makes logout/account deletion equivalent to DNS removal.',1)
MD.write_text(text,encoding='utf-8')

p=json.loads(JS.read_text(encoding='utf-8'))
req(p['version']=='1.0.0','TSK0323_JSON_VERSION_UNEXPECTED')
p['version']='1.0.1-post-cr0007'
p['last_source_review']='2026-09-01'
p['sequencing']='DEC-0053/CR-0006 + DEC-0054/CR-0007; DEC-0052/CR-0005 pre-L8 human-evidence rule retained'
p['canonical_sources']['TSK-0322']['blob']='9344140b48ec99e0bd14639ac6640b581ee66d9f'
p['scope_compatibility']={
'accountless_core_required':True,
'optional_parent_account_session_allowed_elsewhere':True,
'lightweight_dashboard_saved_device_continuity_allowed_elsewhere':True,
'safeweb_login_required_for_instruction_core':False,
'account_session_saved_device_dashboard_presence_is_technical_verification':False,
'logout_or_account_record_deletion_equals_physical_dns_removal':False,
'browsing_query_activity_history':False,
'child_identity_profiles':False,
'broad_raw_dns_administration':False,
'automatic_j0_j1_account_linkage':False,
}
for s in p['external_sources'].values(): s['checked']='2026-09-01'
for r in p['records']: r['last_verified']='2026-09-01'
JS.write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

print('TSK0323_BOUNDED_UPDATE=PASS')
