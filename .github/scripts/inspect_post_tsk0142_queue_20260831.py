import csv
import subprocess
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
EXPECTED_WBS = 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_STATE = 'e3d8a09ccf42f61f65b48ecd2e43773a7300bfbf'


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()

if blob(str(WBS)) != EXPECTED_WBS:
    raise SystemExit('unexpected WBS blob')
if blob(str(STATE)) != EXPECTED_STATE:
    raise SystemExit('unexpected CURRENT_STATE blob')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
by_id = {r['Task_ID']: r for r in rows}
order = {r['Task_ID']: i for i, r in enumerate(rows)}
state = STATE.read_text(encoding='utf-8')


def deps(r):
    return [d.strip() for d in r.get('Dependencies','').replace(';',',').split(',') if d.strip()]


def marker_found(tid):
    patterns = [
        f'## {tid} current accepted stable state',
        f'### {tid} current accepted stable state',
        f'## {tid} accepted stable state',
        f'### {tid} accepted stable state',
    ]
    return any(p in state for p in patterns)

# TSK-0142 itself must now be current PASS.
if '## TSK-0142 current accepted stable state — 2026-08-31' not in state:
    raise SystemExit('TSK-0142 current PASS marker missing')

candidates = []
for r in rows:
    ds = deps(r)
    if 'TSK-0142' in ds:
        candidates.append(r)
        print('TSK0142_SUCCESSOR|' + '|'.join(r.get(k,'').replace('\n',' ').replace('|','/') for k in [
            'Task_ID','Lifecycle_Stage','Title','Plan_Status','Execution_State','Priority','Critical_Path','Dependencies','AI_Capability_A0_A4','Action_Authority','Acceptance_ID'
        ]))

# Carry the still-open sibling branch exposed after TSK-0312.
if 'TSK-0329' in by_id and not marker_found('TSK-0329'):
    candidates.append(by_id['TSK-0329'])

seen = set()
for r in sorted(candidates, key=lambda x: order[x['Task_ID']]):
    tid = r['Task_ID']
    if tid in seen:
        continue
    seen.add(tid)
    ds = deps(r)
    dep_bits = []
    all_found = True
    for d in ds:
        found = marker_found(d)
        all_found = all_found and found
        dep_bits.append(f'{d}:{"FOUND" if found else "MISSING"}')
    print('CANDIDATE|' + '|'.join([
        str(order[tid]), tid, r.get('Lifecycle_Stage',''), r.get('Title','').replace('|','/'),
        r.get('Priority',''), r.get('Critical_Path',''), r.get('Action_Authority',''),
        r.get('AI_Capability_A0_A4',''), r.get('Plan_Status',''), r.get('Execution_State',''),
        ';'.join(ds), ';'.join(dep_bits), 'ALL_DEP_MARKERS_FOUND' if all_found else 'DEP_MARKER_MISSING',
        r.get('Acceptance_ID',''), r.get('Acceptance_Criteria','').replace('|','/').replace('\n',' ')
    ]))

print('POST_TSK0142_QUEUE_INSPECTION=PASS')
