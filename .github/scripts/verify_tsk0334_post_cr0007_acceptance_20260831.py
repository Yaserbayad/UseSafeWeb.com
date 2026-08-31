import csv, subprocess
from pathlib import Path

ROOT = Path('.')
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
RUNTIME = ROOT / 'CURRENT_STATE.md'
BASE = ROOT / 'design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md'
AMD = ROOT / 'design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md'
PREP = ROOT / 'TSK_0334_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md'
OWNER = ROOT / 'TSK_0334_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md'

EXPECTED = {
    WBS: 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    RUNTIME: 'f8c1a9ca9bb69899c2a55bd7f6700f6d018dabb9',
    BASE: '44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f',
    AMD: 'de423bdb8aeb2b0a0f25a85850be380cfab7e67d',
    PREP: '652845396bc62a1df859b2a9f1944576268066b6',
    OWNER: 'ece3d3cb92829a84877ad62bf59f89b453223942',
}


def blob(path):
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


for path, expected in EXPECTED.items():
    require(path.exists(), f'TSK0334_REQUIRED_FILE_MISSING={path.as_posix()}')
    require(blob(path) == expected, f'TSK0334_BLOB_CHANGED={path.as_posix()}')
print('TSK0334_EXACT_INPUT_BLOBS=PASS')

with WBS.open(newline='', encoding='utf-8-sig') as handle:
    row = next(r for r in csv.DictReader(handle) if r.get('Task_ID') == 'TSK-0334')
require(row.get('Dependencies') == 'TSK-0330', 'TSK0334_DEPENDENCY_CHANGED')
require(row.get('Acceptance_ID') == 'ACC-0334', 'TSK0334_ACCEPTANCE_ID_CHANGED')
require(row.get('Verification_ID') == 'VER-0334', 'TSK0334_VERIFICATION_ID_CHANGED')
require(row.get('Evidence_ID') == 'EVD-0334', 'TSK0334_EVIDENCE_ID_CHANGED')
require(row.get('AI_Capability_A0_A4') == 'A1', 'TSK0334_CAPABILITY_CHANGED')
require(row.get('Action_Authority') == 'HUMAN_ONLY', 'TSK0334_AUTHORITY_CHANGED')
print('TSK0334_WBS_CONTRACT=PASS')

runtime = RUNTIME.read_text(encoding='utf-8')
require('## TSK-0334 current state — 2026-08-31 — POST-CR-0007' in runtime, 'TSK0334_WAITING_STATE_MISSING')
require('**WAITING / HUMAN_APPROVAL_REQUIRED**, not PASS' in runtime, 'TSK0334_WAITING_PRECONDITION_CHANGED')
require('## TSK-0334 current accepted stable state — 2026-08-31 — POST-CR-0007' not in runtime, 'TSK0334_PREMATURE_CURRENT_PASS')
print('TSK0334_WAITING_PRECONDITION=PASS')

base = BASE.read_text(encoding='utf-8').lower()
amd = AMD.read_text(encoding='utf-8').lower()
for idx in range(1, 6):
    require(f'sup-0{idx}' in base, f'TSK0334_BASE_CATEGORY_MISSING=SUP-0{idx}')
for idx in range(6, 9):
    require(f'sup-0{idx}' in amd, f'TSK0334_AMENDMENT_CATEGORY_MISSING=SUP-0{idx}')
for document, label, minimum in ((base, 'BASE', 5), (amd, 'AMENDMENT', 3)):
    for field in ('accessible path', 'minimal diagnostic', 'protection consequence', 'escalation', 'success state'):
        require(document.count(field) >= minimum, f'TSK0334_{label}_ACC_FIELD_MISSING={field}')
print('TSK0334_ACC0334_EIGHT_CATEGORY_COVERAGE=PASS')

for token in (
    'without login',
    'ownership mismatch',
    'account-only',
    'no automatic replay',
    'j0/j1',
    'physical usesafeweb',
    'browsing/query/activity history',
    'authoritative',
):
    require(token in amd, f'TSK0334_CURRENT_SCOPE_SEMANTIC_MISSING={token}')
print('TSK0334_CURRENT_SCOPE_SEMANTICS=PASS')

prep = PREP.read_text(encoding='utf-8')
require('33415828154 / 99566111401' in prep and 'completed **SUCCESS**' in prep, 'TSK0334_PREPARATION_RUN_NOT_BOUND')
for marker in (
    'TSK0334_WBS_HUMAN_BOUNDARY=PASS',
    'TSK0334_EIGHT_CATEGORY_COVERAGE=PASS',
    'TSK0334_CURRENT_SCOPE_SEMANTICS=PASS',
    'TSK0334_HUMAN_PASS_FENCE=PASS',
    'TSK0334_PREPARATION_VERIFICATION=PASS',
):
    require(marker in prep, f'TSK0334_PREPARATION_MARKER_MISSING={marker}')
print('TSK0334_PREPARATION_EVIDENCE=PASS')

owner = OWNER.read_text(encoding='utf-8')
require('**Decision:** APPROVED' in owner, 'TSK0334_OWNER_DECISION_NOT_APPROVED')
require('**APPROVE TSK-0334 POST-CR-0007 CURRENT-SCOPE SUPPORT AMENDMENT**' in owner, 'TSK0334_EXACT_OWNER_APPROVAL_MISSING')
require('44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f' in owner, 'TSK0334_OWNER_BASE_BINDING_MISSING')
require('de423bdb8aeb2b0a0f25a85850be380cfab7e67d' in owner, 'TSK0334_OWNER_AMENDMENT_BINDING_MISSING')
for non_inference in ('TSK-0331', 'TSK-0333', 'LG-06'):
    require(non_inference in owner, f'TSK0334_OWNER_BOUNDARY_MISSING={non_inference}')
print('TSK0334_OWNER_AUTHORITY=PASS')

print('TSK0334_FINAL_ACCEPTANCE_VERIFICATION=PASS')
