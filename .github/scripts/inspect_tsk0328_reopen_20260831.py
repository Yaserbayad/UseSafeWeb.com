import csv
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
ART = Path('prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows.get('TSK-0328')
if r is None:
    raise SystemExit('TSK-0328 missing from WBS')

fields = [
    'Task_ID','Task_Name','Lifecycle_Stage','Priority','Plan_Status','Execution_State',
    'Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','AI_Capability_A0_A4',
    'Action_Authority','Requirement_Reference','Interface_Reference'
]
for k in fields:
    print(f'{k}={r.get(k, "")}')

expected = {
    'Lifecycle_Stage': 'L4',
    'Priority': 'MEDIUM',
    'Dependencies': 'TSK-0325; TSK-0315',
    'Acceptance_ID': 'ACC-0328',
    'Verification_ID': 'VER-0328',
    'Evidence_ID': 'EVD-0328',
    'AI_Capability_A0_A4': 'A3',
    'Action_Authority': 'AUTO_ALLOWED',
}
for k, v in expected.items():
    if r.get(k) != v:
        raise SystemExit(f'TSK-0328 {k} mismatch: {r.get(k)!r} != {v!r}')

acc = r.get('Acceptance_Criteria', '')
for phrase in [
    'accountless core',
    'optional account sign-in/return/dashboard/account lifecycle',
    'keeps login optional for core value',
    'maps each screen to a user goal and requirement',
]:
    if phrase not in acc:
        raise SystemExit(f'current ACC-0328 semantic missing: {phrase}')

state = STATE.read_text(encoding='utf-8')
for marker in [
    '## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007',
]:
    if marker not in state:
        raise SystemExit(f'current dependency marker missing: {marker}')

art = ART.read_text(encoding='utf-8')
for stale in [
    'The current IA has **no**:',
    'Login, Sign up, Account, Dashboard',
    'No Login/Dashboard/Account/Pricing item exists.',
    'it does not become a marketing site or account dashboard',
]:
    if stale not in art:
        raise SystemExit(f'historical accountless-only indicator missing: {stale}')

if 'Version:** 1.0.0' not in art:
    raise SystemExit('historical TSK-0328 version mismatch')

print('TSK0328_WBS_CURRENT_CONTRACT=PASS')
print('TSK0328_DEPENDENCIES_CURRENT_PASS=PASS')
print('TSK0328_HISTORICAL_ARTIFACT_STALE_UNDER_CR0006=PASS')
print('TSK0328_REOPEN_DISPOSITION=TODO')
