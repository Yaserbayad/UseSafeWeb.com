import csv, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
PROTO=ROOT/'prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md'
MODEL=ROOT/'prototype/TSK-0331/LIFECYCLE_STATE_MODEL.json'
HTML=ROOT/'prototype/TSK-0331/index.html'
CSS=ROOT/'prototype/TSK-0331/prototype.css'
APP=ROOT/'prototype/TSK-0331/app.mjs'
ANALYTICAL=ROOT/'TSK_0331_POST_CR0007_ACCOUNT_DEVICE_LIFECYCLE_ACCEPTANCE_EVIDENCE_2026-08-31.md'
DETERMINISTIC=ROOT/'TSK_0331_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md'
CORRECTED_0334=ROOT/'TSK_0334_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md'

EXPECTED={
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 RUNTIME:'e43fd43c4cb6d3ac3ae405c10cb04e83d8e30206',
 PROTO:'9f5994b31b63a018ea0212ce21083b9dacb39ecc',
 MODEL:'442c5a7fb2fb0f5af23ef29878f383fd3cfaa294',
 HTML:'64bb4fa2f64d76dc4655f55f85304da5c6ffca9a',
 CSS:'2a0d633efb4f138566d8d05e9fc60632e5409f29',
 APP:'9b8df052bc19c15bfa8cc217bb7932a251b80588',
 ANALYTICAL:'81ebe13e71d168b4305d9a3791a15be70baa43b9',
 DETERMINISTIC:'9b4b274d39a8d8d60b98392131e5dacc0a7199df',
 CORRECTED_0334:'c61ca9bde3184761ef793d2ae3f80cd4cffe021c',
}

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,e in EXPECTED.items():
    req(p.exists(),f'TSK0331_REVAL_MISSING={p.as_posix()}')
    req(blob(p)==e,f'TSK0331_REVAL_BLOB_CHANGED={p.as_posix()}')
print('TSK0331_REVAL_EXACT_BLOBS=PASS')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0331')
expected_acc='Flows make consequences explicit, require appropriate confirmation, handle partial/provider failures, offer safe recovery, preserve truthful protection state and define what account/device metadata is deleted or retained.'
req(row.get('Dependencies')=='TSK-0332; TSK-0334','TSK0331_REVAL_DEPS_CHANGED')
req(row.get('Acceptance_Criteria')==expected_acc,'TSK0331_REVAL_ACC_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0331' and row.get('Verification_ID')=='VER-0331' and row.get('Evidence_ID')=='EVD-0331','TSK0331_REVAL_IDS_CHANGED')
req(row.get('AI_Capability_A0_A4')=='A4' and row.get('Action_Authority')=='AUTO_ALLOWED','TSK0331_REVAL_AUTH_CHANGED')
print('TSK0331_REVAL_WBS_CONTRACT=PASS')

runtime=RUNTIME.read_text(encoding='utf-8')
for dep in ('TSK-0332','TSK-0334'):
    req(f'## {dep} current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,f'TSK0331_REVAL_CURRENT_DEP_MISSING={dep}')
req('Corrective dependency-complete revalidation:' in runtime,'TSK0331_REVAL_TSK0334_CORRECTION_NOT_RECONCILED')
req('33420242950 / 99580565616' in runtime,'TSK0331_REVAL_TSK0334_CORRECTIVE_RUN_NOT_BOUND')
req('## TSK-0331 current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,'TSK0331_REVAL_CURRENT_SECTION_MISSING')
print('TSK0331_REVAL_DEPENDENCY_COMPLETE=PASS')

model=MODEL.read_text(encoding='utf-8').lower()
proto=PROTO.read_text(encoding='utf-8').lower()
for token in ('account deletion','physical protection','no automatic replay','ownership mismatch','replacement','reconfigure','j0/j1','without login'):
    req(token in proto or token in model,f'TSK0331_REVAL_SEMANTIC_MISSING={token}')
print('TSK0331_REVAL_ACC_ARTIFACT=PASS')

det=DETERMINISTIC.read_text(encoding='utf-8')
req('**Final run/job `33419292638 / 99577450844`: SUCCESS**' in det,'TSK0331_REVAL_FINAL_BROWSER_RUN_MISSING')
for marker in (
'TSK0331_BROWSER_FUNCTIONAL=PASS','TSK0331_BROWSER_NEGATIVE_SECURITY=PASS','TSK0331_BROWSER_CONFIGURATION_TRUTH=PASS',
'TSK0331_BROWSER_PRIVACY=PASS','TSK0331_BROWSER_ROLLBACK_RECOVERY=PASS','TSK0331_BROWSER_RESPONSIVE=PASS',
'TSK0331_BROWSER_KEYBOARD=PASS','TSK0331_BROWSER_RTL=PASS','TSK0331_BROWSER_NO_CONSOLE_ERRORS=PASS'):
    req(marker in det,f'TSK0331_REVAL_BROWSER_MARKER_MISSING={marker}')
print('TSK0331_REVAL_PRIOR_TARGET_BROWSER_PROOF=PASS')
print('TSK0331_DEPENDENCY_COMPLETE_REVALIDATION=PASS')
