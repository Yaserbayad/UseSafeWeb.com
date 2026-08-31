import csv
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'

with WBS.open(newline='',encoding='utf-8-sig') as f:
    rows={r['Task_ID']:r for r in csv.DictReader(f)}
runtime=RUNTIME.read_text(encoding='utf-8')
graph=GRAPH.read_text(encoding='utf-8')

# Exact outgoing dependency consumers of newly accepted TSK-0332.
successors=[]
for tid,row in rows.items():
    deps=[x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()]
    if 'TSK-0332' in deps:
        successors.append(tid)
print('POST_TSK0332_SUCCESSORS='+';'.join(successors))

# Inspect direct successors plus their dependency chain and nearby current-scope candidates.
candidates=[]
for tid in successors + ['TSK-0331','TSK-0333','TSK-0334','TSK-0335','TSK-0352']:
    if tid in rows and tid not in candidates:
        candidates.append(tid)

for tid in candidates:
    row=rows[tid]
    print(f'---{tid}---')
    for key in ['Task_ID','Task_Name','Lifecycle_Stage','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_Reference','Requirement_Reference','Interface_Reference','Source_Reference']:
        print(f'{key}={row.get(key,"")}')
    deps=[x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()]
    current=[]
    for dep in deps:
        current_marker=f'## {dep} current accepted stable state'
        generic_marker=f'## {dep} accepted stable state'
        if current_marker in runtime:
            current.append(f'{dep}:CURRENT_PASS')
        elif generic_marker in runtime:
            current.append(f'{dep}:HISTORICAL_OR_UNQUALIFIED_PASS')
        else:
            current.append(f'{dep}:NO_PASS_HEADING')
    print('DEPENDENCY_RUNTIME_MARKERS='+';'.join(current))

# Exact graph block for TSK-0331.
start=graph.find('  TSK-0331:\n')
if start<0: raise SystemExit('TSK0331_GRAPH_MISSING')
end=graph.find('\n  TSK-',start+3)
block=graph[start:end if end>=0 else len(graph)]
print('---GRAPH_TSK0331_BEGIN---')
print(block)
print('---GRAPH_TSK0331_END---')

# Current runtime excerpts that materially affect 0331 eligibility/currentness.
for heading in [
    '## TSK-0332 current accepted stable state',
    '## TSK-0334 accepted stable state',
    '## TSK-0334 current accepted stable state',
    '## TSK-0333 accepted stable state',
    '## TSK-0333 current accepted stable state',
]:
    print(f'{heading}={"YES" if heading in runtime else "NO"}')

print('POST_TSK0332_QUEUE_INSPECTION=PASS')
