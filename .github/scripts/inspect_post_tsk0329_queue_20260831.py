import csv
import re
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
GRAPH = Path('Plans/Master/RELATIONSHIP_INDEX.yaml')
STATE = Path('CURRENT_STATE.md')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}

graph = GRAPH.read_text(encoding='utf-8')
lines = graph.splitlines()
blocks = {}
current = None
buf = []
for line in lines:
    m = re.match(r'^  (TSK-\d{4}):$', line)
    if m:
        if current:
            blocks[current] = '\n'.join(buf)
        current = m.group(1)
        buf = [line]
    elif current:
        if re.match(r'^  [^ ].*:$', line):
            blocks[current] = '\n'.join(buf)
            current = None
            buf = []
        else:
            buf.append(line)
if current:
    blocks[current] = '\n'.join(buf)

successors = []
for tid, block in blocks.items():
    if 'target: TSK-0329' in block and 'type: depends_on' in block:
        successors.append(tid)

print('POST_TSK0329_SUCCESSORS=' + ';'.join(successors))
state = STATE.read_text(encoding='utf-8')
for tid in sorted(set(successors + ['TSK-0330','TSK-0331','TSK-0332','TSK-0333','TSK-0334','TSK-0352'])):
    r = rows.get(tid)
    if not r:
        continue
    print(f'---{tid}---')
    for key in ['Task_Name','Lifecycle_Stage','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_Reference','Requirement_Reference','Interface_Reference']:
        print(f'{key}={r.get(key, "")}')
    headings = [line for line in state.splitlines() if line.startswith('## ') and tid in line]
    for h in headings[-5:]:
        print(f'RUNTIME_HEADING={h}')
    block = blocks.get(tid, '')
    deps = []
    b_lines = block.splitlines()
    for i, line in enumerate(b_lines):
        if line.strip().startswith('- target: TSK-') and i + 1 < len(b_lines) and b_lines[i+1].strip() == 'type: depends_on':
            deps.append(line.split(':',1)[1].strip())
    print('GRAPH_DEPENDENCIES=' + ';'.join(deps))
print('POST_TSK0329_QUEUE_INSPECTION=PASS')
