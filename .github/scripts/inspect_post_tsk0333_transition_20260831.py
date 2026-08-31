import csv,re
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
GATES=ROOT/'Plans/Master/Registers/GATES.md'
with WBS.open(newline='',encoding='utf-8-sig') as f: rows={r.get('Task_ID'):r for r in csv.DictReader(f)}
graph=GRAPH.read_text(encoding='utf-8'); runtime=RUNTIME.read_text(encoding='utf-8'); gates=GATES.read_text(encoding='utf-8')

def block_for(node):
    m=re.search(rf'^  {re.escape(node)}:\n',graph,re.M)
    if not m:return ''
    n=re.search(r'^  [A-Z]+-[0-9]+:\n',graph[m.end():],re.M)
    end=m.end()+n.start() if n else len(graph)
    return graph[m.start():end]

def show_task(tid):
    r=rows.get(tid); print(f'--- {tid} ---')
    if not r: print('WBS=MISSING'); return
    for k in ('Task_ID','Task_Name','Layer','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_ID','Requirement_IDs','Interface_IDs','Source_Reference','Notes'):
        if k in r: print(f'{k}={r.get(k)}')
    print('RUNTIME_CURRENT_PASS='+str(f'## {tid} current accepted stable state' in runtime))
    print('RUNTIME_CURRENT_WAITING='+str(f'## {tid} current waiting state' in runtime))
    print('RUNTIME_HISTORICAL_PASS='+str(f'## {tid} accepted stable state' in runtime))
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    for d in deps:
        print(f'DEP_{d}_CURRENT_PASS='+str(f'## {d} current accepted stable state' in runtime or (f'`{d}' in runtime and ': **PASS**' in runtime)))

# Direct successors of current TSK-0333.
succ=[]
for m in re.finditer(r'^  (TSK-[0-9]+):\n',graph,re.M):
    tid=m.group(1); b=block_for(tid)
    if 'target: TSK-0333' in b: succ.append(tid)
print('POST_TSK0333_SUCCESSORS='+(';'.join(succ) if succ else 'NONE'))
for tid in sorted(set(succ+['TSK-0052'])): show_task(tid)

# Exact graph targets for readiness task and LG-06 gate.
for node in ('TSK-0052','LG-06'):
    b=block_for(node)
    targets=re.findall(r'target: ([A-Z0-9-]+)',b)
    print(f'{node.replace("-","")}_GRAPH_TARGETS='+';'.join(targets))

# Print bounded LG-06 gate section from authoritative register.
m=re.search(r'^##\s+LG-06\b.*$',gates,re.M)
if m:
    nxt=re.search(r'^##\s+LG-[0-9]+\b.*$',gates[m.end():],re.M)
    end=m.end()+nxt.start() if nxt else min(len(gates),m.start()+8000)
    section=gates[m.start():end]
    print('LG06_GATE_SECTION_BEGIN')
    print(section[:8000])
    print('LG06_GATE_SECTION_END')
else: print('LG06_GATE_SECTION=MISSING')

# Existing current/superseded TSK-0052 artifacts.
found=[]
for p in ROOT.rglob('*'):
    if p.is_file() and ('TSK_0052' in p.name or 'TSK-0052' in p.as_posix()) and not p.as_posix().startswith('.github/'):
        found.append(p.as_posix())
print('TSK0052_EXISTING_ARTIFACTS='+';'.join(sorted(found)) if found else 'TSK0052_EXISTING_ARTIFACTS=NONE')
