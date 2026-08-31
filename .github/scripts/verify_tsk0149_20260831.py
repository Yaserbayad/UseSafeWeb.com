import csv
import subprocess
from pathlib import Path

EXPECTED = {
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'runtime': 'e3d8a09ccf42f61f65b48ecd2e43773a7300bfbf',
    'artifact': '3eb1b90dc9fc3a79be94c7343cd16a9d3093748f',
    'evidence': 'e55306c70fee60079aedfb42fd6cffbc863936f5',
}
WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
ART = Path('TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_2026-08-31.md')
EVD = Path('TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_ACCEPTANCE_EVIDENCE_2026-08-31.md')


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

require(blob(str(WBS)) == EXPECTED['wbs'], 'unexpected WBS blob')
require(blob(str(STATE)) == EXPECTED['runtime'], 'unexpected runtime blob')
require(blob(str(ART)) == EXPECTED['artifact'], 'unexpected artifact blob')
require(blob(str(EVD)) == EXPECTED['evidence'], 'unexpected analytical evidence blob')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows.get('TSK-0149')
require(r is not None, 'TSK-0149 missing')
require(r.get('Lifecycle_Stage') == 'L4', 'lifecycle mismatch')
require(r.get('Priority') == 'HIGH', 'priority mismatch')
require(r.get('Dependencies') == 'TSK-0146', 'dependency mismatch')
require(r.get('Acceptance_ID') == 'ACC-0149', 'acceptance mismatch')
require(r.get('Verification_ID') == 'VER-0149', 'verification mismatch')
require(r.get('Evidence_ID') == 'EVD-0149', 'evidence mismatch')
require(r.get('Action_Authority') == 'AUTO_ALLOWED', 'authority mismatch')
require(r.get('AI_Capability_A0_A4') == 'A3', 'capability mismatch')
print('TSK0149_WBS_CONTRACT=PASS')

state = STATE.read_text(encoding='utf-8')
require('TSK-0146 current accepted stable state' in state, 'current TSK-0146 marker absent')
require('TSK-0149 current accepted stable state' not in state, 'TSK-0149 already current PASS')
print('TSK0149_DEPENDENCY_RUNTIME=PASS')

art = ART.read_text(encoding='utf-8')
ev = EVD.read_text(encoding='utf-8')
for phrase in [
    'Public website outcome — discover / understand / trust / decide / start.',
    'Product/setup outcome — start / configure / verify / understand / recover/manage.',
    'one brand and one coherent design system',
    'start the accountless core directly without creating an account or providing payment details',
    'complete the entire core safety journey without login',
    'optionally sign in for bounded continuity',
    'Public content does not silently create a persistent parent/device record',
    'Returning to public information/help must not mutate protection state',
    'shared identity, typography, color/token system, icon/imagery language and voice',
    'mandatory login for core safety value',
    'browsing/query/activity history',
    'unrestricted customer DNS administration',
]:
    require(phrase in art, f'missing artifact requirement: {phrase}')
print('TSK0149_ACC_SEMANTICS=PASS')

for i in range(1, 11):
    require(f'{i}.' in art.split('## 9. Deterministic acceptance assertions',1)[1].split('## 10.',1)[0], f'missing assertion {i}')
print('TSK0149_ASSERTIONS_10=PASS')

require('WBS snapshot was not reused as runtime proof' in ev, 'WBS snapshot proof fence absent')
require('Analytical result: ACC-0149 PASS candidate.' in ev, 'analytical result absent')
require('TSK-0328 remains responsible for exact current information architecture/navigation and must be rebuilt/reverified' in ev, 'stale TSK-0328 dependency reconciliation absent')
print('TSK0149_ANALYTICAL_EVIDENCE=PASS')

for forbidden in ['LG-06 is PASS','implementation is PASS','provider acceptance is PASS','behavioral validation is PASS']:
    require(forbidden not in art and forbidden not in ev, f'downstream PASS inference found: {forbidden}')
print('TSK0149_NO_DOWNSTREAM_PASS_INFERENCE=PASS')
print('TSK0149_INDEPENDENT_VERIFICATION=PASS')
