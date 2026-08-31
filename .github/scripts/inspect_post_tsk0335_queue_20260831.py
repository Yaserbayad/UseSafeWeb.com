import csv, os, re
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'

with WBS.open(newline='',encoding='utf-8-sig') as f:
    rows={r.get('Task_ID'):r for r in csv.DictReader(f)}

graph=GRAPH.read_text(encoding='utf-8')
runtime=RUNTIME.read_text(encoding='utf-8')

# direct task successors are nodes whose graph block targets TSK-0335 as a dependency
successors=[]
for m in re.finditer(r'^  (TSK-[0-9]+):\n',graph,re.M):
    tid=m.group(1); start=m.start(); nxt=re.search(r'^  TSK-[0-9]+:\n',graph[m.end():],re.M)
    end=m.end()+nxt.start() if nxt else len(graph)
    block=graph[start:end]
    if 'target: TSK-0335' in block:
        successors.append(tid)
print('POST_TSK0335_SUCCESSORS='+(';'.join(successors) if successors else 'NONE'))

for tid in sorted(set(successors+['TSK-0333','TSK-0335','TSK-0334','TSK-0331','TSK-0146'])):
    r=rows.get(tid)
    if not r:
        print(f'{tid}_WBS=MISSING'); continue
    print(f'--- {tid} ---')
    for k in ('Task_ID','Task_Name','Layer','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_ID','Requirement_IDs','Interface_IDs','Source_Reference','Notes'):
        if k in r: print(f'{k}={r.get(k)}')
    h_current=f'## {tid} current accepted stable state'
    h_wait=f'## {tid} current waiting state'
    h_hist=f'## {tid} accepted stable state'
    print(f'RUNTIME_CURRENT_PASS={h_current in runtime}')
    print(f'RUNTIME_CURRENT_WAITING={h_wait in runtime}')
    print(f'RUNTIME_HISTORICAL_PASS={h_hist in runtime}')

# print exact TSK-0333 graph block, normalized to relevant targets
m=re.search(r'^  TSK-0333:\n',graph,re.M)
if m:
    nxt=re.search(r'^  TSK-[0-9]+:\n',graph[m.end():],re.M)
    end=m.end()+nxt.start() if nxt else len(graph)
    block=graph[m.start():end]
    targets=re.findall(r'target: ([A-Z0-9-]+)',block)
    print('TSK0333_GRAPH_TARGETS='+';'.join(targets))

# discover durable TSK-0333 artifacts, excluding tooling
found=[]
for p in ROOT.rglob('*'):
    if not p.is_file(): continue
    s=p.as_posix()
    if 'TSK-0333' in s or 'TSK_0333' in p.name:
        if not s.startswith('.github/'):
            found.append(s)
print('TSK0333_EXISTING_ARTIFACTS='+';'.join(sorted(found)) if found else 'TSK0333_EXISTING_ARTIFACTS=NONE')
