import csv
from pathlib import Path

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
by_id = {r['Task_ID']: r for r in rows}
fields = ['Task_ID','Parent_ID','Package_ID','Phase_ID','Deliverable_ID','Lifecycle_Stage','Title','Purpose','Plan_Status','Execution_State','Priority','Critical_Path','Dependencies','Trigger','Preconditions','Inputs','Acceptance_ID','Acceptance_Criteria','Verification_ID','Verification_Method','Evidence_ID','Primary_Owner','AI_Capability_A0_A4','Action_Authority','Risk_Reference','Interface_Reference','Requirement_Reference','Relative_Timing','Source_Reference','Notes']
for tid in ['TSK-0142','TSK-0329']:
    if tid not in by_id: raise SystemExit(tid + ' missing')
    r = by_id[tid]
    for key in fields:
        print(f'{tid}_FIELD|{key}|' + r.get(key,'').replace('\n',' ').replace('|','/'))

state = Path('CURRENT_STATE.md').read_text(encoding='utf-8')
for tid in ['TSK-0312','TSK-0041','TSK-0328']:
    # Print bounded context around the first exact accepted-state heading if present.
    marker = f'### {tid} accepted stable state'
    marker2 = f'## {tid} current accepted stable state'
    idx = state.find(marker2)
    if idx < 0: idx = state.find(marker)
    print(f'RUNTIME_MARKER|{tid}|' + ('FOUND' if idx >= 0 else 'MISSING'))
    if idx >= 0:
        snippet = state[idx:idx+1800].replace('\n',' ')
        print(f'RUNTIME_SNIPPET|{tid}|' + snippet.replace('|','/'))

# Identify direct WBS successors of TSK-0312, regardless of lifecycle.
for r in rows:
    deps = [d.strip() for d in r.get('Dependencies','').replace(';',',').split(',') if d.strip()]
    if 'TSK-0312' in deps:
        print('TSK0312_SUCCESSOR|' + '|'.join(r.get(k,'').replace('\n',' ').replace('|','/') for k in ['Task_ID','Lifecycle_Stage','Title','Plan_Status','Execution_State','Priority','Critical_Path','Dependencies','AI_Capability_A0_A4','Action_Authority','Acceptance_ID']))

print('POST_TSK0312_SUCCESSOR_INSPECTION=PASS')
