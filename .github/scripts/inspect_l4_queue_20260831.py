import csv
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))

if not rows:
    raise SystemExit('empty WBS')
print('WBS_COLUMNS=' + '|'.join(rows[0].keys()))

l4 = [r for r in rows if r.get('Lifecycle_Stage') == 'L4' and r.get('Action_Authority') == 'AUTO_ALLOWED']
print(f'L4_AUTO_ALLOWED_COUNT={len(l4)}')
fields = ['Task_ID','Task_Name','Status','Planning_Status','Disposition','Priority','Plan_Priority','Critical_Path','Dependencies','AI_Capability_A0_A4','Action_Authority','Acceptance_ID','Verification_ID','Evidence_ID','Source_Reference']
for r in l4:
    vals = [r.get(k,'') for k in fields]
    print('L4ROW|' + '|'.join(v.replace('\n',' ').replace('|','/') for v in vals))

for r in l4:
    deps = [d.strip() for d in r.get('Dependencies','').replace(';',',').split(',') if d.strip()]
    if 'TSK-0140' in deps:
        vals = [r.get(k,'') for k in fields]
        print('TSK0140_SUCCESSOR|' + '|'.join(v.replace('\n',' ').replace('|','/') for v in vals))

# Relationship index must contain every L4 candidate and TSK-0140; WBS remains task/dependency authority.
rel = Path('Plans/Master/RELATIONSHIP_INDEX.yaml').read_text(encoding='utf-8')
if 'TSK-0140' not in rel:
    raise SystemExit('TSK-0140 missing from relationship index')
missing = [r['Task_ID'] for r in l4 if r['Task_ID'] not in rel]
if missing:
    raise SystemExit('L4 AUTO_ALLOWED task(s) missing from relationship index: ' + ','.join(missing))
print('RELATIONSHIP_INDEX_L4_COVERAGE=PASS')
