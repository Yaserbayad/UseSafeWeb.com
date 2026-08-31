import csv
from pathlib import Path

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
if not rows:
    raise SystemExit('empty WBS')

matches = [r for r in rows if r.get('Task_ID') == 'TSK-0312']
if len(matches) != 1:
    raise SystemExit(f'TSK-0312 row count={len(matches)}')
r = matches[0]
for key in r.keys():
    print('TSK0312_FIELD|' + key + '|' + r.get(key,'').replace('\n',' ').replace('|','/'))

if r.get('Lifecycle_Stage') != 'L4': raise SystemExit('TSK-0312 not L4')
if r.get('Dependencies') != 'TSK-0140': raise SystemExit('TSK-0312 dependency mismatch')
if r.get('Action_Authority') != 'AUTO_ALLOWED': raise SystemExit('TSK-0312 not AUTO_ALLOWED')
if r.get('Acceptance_ID') != 'ACC-0312': raise SystemExit('TSK-0312 acceptance mismatch')

state = Path('CURRENT_STATE.md').read_text(encoding='utf-8')
if '## TSK-0140 current accepted stable state — 2026-08-31 — POST-CR-0007' not in state:
    raise SystemExit('current TSK-0140 PASS section missing')
if '`TSK-0140 — Issue the post-validation product brief`: **PASS**' not in state:
    raise SystemExit('current TSK-0140 PASS token missing')
if '## TSK-0312 current accepted stable state' in state:
    raise SystemExit('TSK-0312 already has a current accepted runtime section')

rel = Path('Plans/Master/RELATIONSHIP_INDEX.yaml').read_text(encoding='utf-8')
for token in ['TSK-0140','TSK-0312']:
    if token not in rel: raise SystemExit(token + ' missing from relationship index')
print('TSK0312_PREFLIGHT_STATIC=PASS')
print('TSK0312_RUNTIME_DEPENDENCY=PASS')
print('TSK0312_CURRENT_PASS_ABSENT=PASS')
print('TSK0312_RELATIONSHIP_COVERAGE=PASS')
