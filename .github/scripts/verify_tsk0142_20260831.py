import csv
import subprocess
from pathlib import Path

EXPECTED = {
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'runtime': 'bc95bd395097ace6ab93e368d10812aeeef5fc0f',
    'artifact': '77b432e9d06741d0d303de2c2a2524e804cdcf5e',
    'evidence': '6cad75df075d9444abf67fa564452dc32a0692f3',
}

ART = Path('TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_REQUIREMENTS_2026-08-31.md')
EVD = Path('TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_ACCEPTANCE_EVIDENCE_2026-08-31.md')
STATE = Path('CURRENT_STATE.md')
WBS = Path('Plans/Master/WBS/master-wbs.csv')


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

require(blob(str(WBS)) == EXPECTED['wbs'], 'unexpected WBS blob')
require(blob(str(STATE)) == EXPECTED['runtime'], 'unexpected runtime baseline blob')
require(blob(str(ART)) == EXPECTED['artifact'], 'unexpected TSK-0142 artifact blob')
require(blob(str(EVD)) == EXPECTED['evidence'], 'unexpected TSK-0142 analytical evidence blob')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
row = rows.get('TSK-0142')
require(row is not None, 'TSK-0142 missing from WBS')
require(row.get('Lifecycle_Stage') == 'L4', 'TSK-0142 lifecycle mismatch')
require(row.get('Action_Authority') == 'AUTO_ALLOWED', 'TSK-0142 authority mismatch')
require(row.get('AI_Capability_A0_A4') == 'A3', 'TSK-0142 capability mismatch')
require(row.get('Acceptance_ID') == 'ACC-0142', 'TSK-0142 acceptance ID mismatch')
require(row.get('Verification_ID') == 'VER-0142', 'TSK-0142 verification ID mismatch')
require(row.get('Evidence_ID') == 'EVD-0142', 'TSK-0142 evidence ID mismatch')
deps = {d.strip() for d in row.get('Dependencies', '').replace(';', ',').split(',') if d.strip()}
require(deps == {'TSK-0312', 'TSK-0041'}, f'unexpected TSK-0142 dependencies: {deps}')
print('TSK0142_WBS_CONTRACT=PASS')

state = STATE.read_text(encoding='utf-8')
require('## TSK-0312 current accepted stable state — 2026-08-31' in state, 'current TSK-0312 PASS marker absent')
require('### TSK-0041 accepted stable state' in state, 'TSK-0041 accepted marker absent')
require('TSK-0142 current accepted stable state' not in state, 'TSK-0142 already marked current PASS')
print('TSK0142_DEPENDENCIES_RUNTIME=PASS')

art = ART.read_text(encoding='utf-8')
ev = EVD.read_text(encoding='utf-8')

required_artifact = [
    'Parent-chosen device nickname or safe generic default',
    '### DEV-01 — Add device',
    '### DEV-02 — Setup / continue setup',
    '### DEV-03 — Verify / re-verify',
    '### DEV-04 — Reinstall / reconfigure',
    '### DEV-05 — Replace device',
    '### DEV-06 — Revoke / unlink dashboard management',
    '### DEV-07 — Remove UseSafeWeb protection from device',
    '### DEV-08 — Remove/delete dashboard device record',
    'S1 — Protected / Verified',
    'S2 — Set up / Parent confirmed',
    'S3 — Action needed',
    'S4 — Not covered',
    'S5 — Status uncertain / error',
    'S6 — Removed',
    '## 8. Curated controls — allowed surface',
    '## 10. Help and self-service requirements',
    '## 11. Account lifecycle interactions',
    'browsing history, DNS-query history, visited/top domains or app/activity history',
    'raw/unrestricted AdGuard administration',
    'Account/device ownership, a device-record row, dashboard presence or historical setup completion never yields S1',
    'Creating/signing into an account shall not automatically import J0/J1 accountless journey state',
]
for phrase in required_artifact:
    require(phrase in art, f'missing artifact requirement: {phrase}')
print('TSK0142_ACC_SEMANTICS=PASS')

for i in range(1, 21):
    require(f'DASH-T{i:02d}' in art, f'missing DASH-T{i:02d}')
print('TSK0142_TEST_CASES_20=PASS')

require('complete accountless core' in art.lower() or 'core remains fully usable without login' in art.lower(), 'accountless core guarantee absent')
require('child accounts or child behavioral profiles' in art, 'child-account non-goal absent')
require('broad per-domain allow/block administration' in art, 'broad DNS-admin non-goal absent')
require('payment/paywall controls required for safety value' in art, 'safety-paywall non-goal absent')
print('TSK0142_SCOPE_FENCES=PASS')

require('no automatic J0/J1-to-account/device promotion/linkage' in ev, 'analytical no-linkage reconciliation absent')
require('configuration/dashboard record presence never creates DNS S1' in ev, 'DNS truth reconciliation absent')
require('Analytical result: ACC-0142 PASS candidate.' in ev, 'analytical disposition absent')
require('TSK-0142 shall remain non-PASS until a separate deterministic verification' in ev, 'pre-PASS fence absent')
print('TSK0142_ANALYTICAL_EVIDENCE=PASS')

for forbidden in [
    'LG-06 is PASS',
    'provider acceptance is PASS',
    'implementation is PASS',
    'legal/privacy compliance is PASS',
]:
    require(forbidden not in art and forbidden not in ev, f'downstream PASS inference found: {forbidden}')
print('TSK0142_NO_DOWNSTREAM_PASS_INFERENCE=PASS')
print('TSK0142_INDEPENDENT_VERIFICATION=PASS')
