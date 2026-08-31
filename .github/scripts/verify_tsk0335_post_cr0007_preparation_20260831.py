import csv, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
BASE=ROOT/'design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md'
AMEND=ROOT/'design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md'
IA=ROOT/'prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md'
DASH=ROOT/'prototype/TSK-0332/DASHBOARD_DEVICE_MANAGEMENT_PROTOTYPE.md'
SUPPORT=ROOT/'design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md'
LIFE_EVIDENCE=ROOT/'TSK_0331_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md'

EXPECTED={
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 GRAPH:'c108d2c162bcea2ee4cc01def46d0487a9501032',
 RUNTIME:'f1c209ffd4e6816ca115ca71a3353291bd036f7c',
 BASE:'7c65a697a98961d0df278658e59262ce39874ff5',
 AMEND:'80db66d9261e6ccf85e0253530819ad262b39497',
 IA:'527436958a1cd75fc91057410f4347ad56a3f53a',
 DASH:'7b19f726fefd4675f55fcad2ffb5fbf4e1c4aa2d',
 SUPPORT:'de423bdb8aeb2b0a0f25a85850be380cfab7e67d',
 LIFE_EVIDENCE:'3c128d430d2d31998f2e637a292a46ed740464e6',
}

def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()

def req(cond,msg):
    if not cond:
        raise SystemExit(msg)

for path,expected in EXPECTED.items():
    req(path.exists(),f'TSK0335_REQUIRED_INPUT_MISSING={path.as_posix()}')
    req(blob(path)==expected,f'TSK0335_INPUT_BLOB_CHANGED={path.as_posix()}')
print('TSK0335_EXACT_INPUT_BLOBS=PASS')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0335')
expected_acc='Prototype never labels parent confirmation as verification, exposes material gaps at the right time, supports deterministic internal/automated truth-state checks, and preserves the interaction points needed for later L8 human comprehension validation.'
req(row.get('Dependencies')=='TSK-0330','TSK0335_WBS_DEPENDENCY_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0335' and row.get('Verification_ID')=='VER-0335' and row.get('Evidence_ID')=='EVD-0335','TSK0335_WBS_IDS_CHANGED')
req(row.get('Acceptance_Criteria')==expected_acc,'TSK0335_ACC_CHANGED')
req(row.get('AI_Capability_A0_A4')=='A1' and row.get('Action_Authority')=='HUMAN_ONLY','TSK0335_AUTHORITY_CHANGED')
print('TSK0335_CURRENT_WBS_CONTRACT=PASS')

graph=GRAPH.read_text(encoding='utf-8')
start=graph.find('  TSK-0335:\n'); req(start>=0,'TSK0335_GRAPH_NODE_MISSING')
end=graph.find('\n  TSK-',start+3); block=graph[start:end if end>=0 else len(graph)]
for target in ('TSK-0330','ACC-0335','VER-0335','EVD-0335','REQ-0028','REQ-0029','CON-0010','CON-0017','INT-0009','INT-0010'):
    req(f'target: {target}' in block,f'TSK0335_GRAPH_TARGET_MISSING={target}')
print('TSK0335_GRAPH_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
req('## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,'TSK0335_CURRENT_DEPENDENCY_MISSING')
req('## TSK-0335 accepted stable state — 2026-08-30' in runtime,'TSK0335_HISTORICAL_PASS_MISSING')
req('## TSK-0335 current accepted stable state' not in runtime,'TSK0335_PREMATURE_CURRENT_PASS')
req('APPROVE TSK-0335 PROTECTION MAP COVERAGE-LIMIT INTERACTIONS' in runtime,'TSK0335_HISTORICAL_OWNER_APPROVAL_MISSING')
print('TSK0335_DEPENDENCY_AND_HUMAN_BOUNDARY=PASS')

base=BASE.read_text(encoding='utf-8')
amend=AMEND.read_text(encoding='utf-8')
base_low=base.lower(); amend_low=amend.lower()
for state in ('Verified','You confirmed this is set up','Action needed','Not covered','Status uncertain','Removed'):
    req(state in base,f'TSK0335_BASE_STATE_MISSING={state}')
for token in ('evidence map, not a safety score','material gap','deterministic','parent confirmation','independently verified'):
    req(token in base_low,f'TSK0335_BASE_SEMANTIC_MISSING={token}')
for i in range(1,17):
    req(f'TC-0335-{i:02d}' in base,f'TSK0335_BASE_TEST_MISSING={i:02d}')
for i in range(1,9):
    req(f'L8-PT-{i:02d}' in base,f'TSK0335_L8_HOOK_MISSING={i:02d}')
print('TSK0335_HISTORICAL_TRUTH_CONTRACT=PASS')

for token in (
'complete accountless core plus optional parent account/session/minimum device persistence/lightweight dashboard',
'saved record != verification',
'persisted/last-known state is not automatically current',
'current s1 still requires current qualifying technical evidence',
'account/provider/session failures are account-only',
'no anonymous-to-account promotion',
'lifecycle actions remain distinct',
'physical `removed` remains evidence-owned',
'no history expansion',
'no safety score',
'login is never required to obtain or understand the core protection map',
):
    req(token in amend_low,f'TSK0335_AMENDMENT_INVARIANT_MISSING={token}')
for i in range(17,25):
    req(f'TC-0335-{i:02d}' in amend,f'TSK0335_AMENDMENT_TEST_MISSING={i:02d}')
req('`APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT`' in amend,'TSK0335_APPROVAL_COMMAND_MISSING')
req('not approved / not pass' in amend_low,'TSK0335_AMENDMENT_PREMATURE_PASS')
print('TSK0335_DUAL_MODE_AMENDMENT=PASS')

for forbidden in ('browsing/query/activity history','raw dns logs','child profiles','unrestricted adguard administration','broad per-domain controls'):
    req(forbidden in amend_low,f'TSK0335_PRIVACY_FENCE_MISSING={forbidden}')
for token in ('mobile/rtl','reading/focus order','color-only','future validation hooks only'):
    req(token in amend_low,f'TSK0335_ACCESSIBILITY_VALIDATION_FENCE_MISSING={token}')
print('TSK0335_PRIVACY_ACCESSIBILITY_FENCES=PASS')

req('three connected experience systems' in IA.read_text(encoding='utf-8').lower(),'TSK0335_CURRENT_IA_DUAL_MODE_NOT_FOUND')
req('record presence, sign-in, session validity and dashboard presence never establish **verified** protection' in DASH.read_text(encoding='utf-8').lower(),'TSK0335_DASHBOARD_TRUTH_RULE_NOT_FOUND')
req('provider/account/session/dashboard/device-record presence never establishes technical `verified` protection' in SUPPORT.read_text(encoding='utf-8').lower(),'TSK0335_SUPPORT_TRUTH_RULE_NOT_FOUND')
req('current dependency-complete pass' in LIFE_EVIDENCE.read_text(encoding='utf-8').lower(),'TSK0335_LIFECYCLE_CORRECTIVE_EVIDENCE_NOT_CURRENT')
print('TSK0335_CURRENT_SOURCE_ALIGNMENT=PASS')
print('TSK0335_PREPARATION_VERIFICATION=PASS')
