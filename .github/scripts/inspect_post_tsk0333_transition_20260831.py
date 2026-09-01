import csv,re,subprocess,io
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'
with WBS.open(newline='',encoding='utf-8-sig') as f: rows={r.get('Task_ID'):r for r in csv.DictReader(f)}
graph=GRAPH.read_text(encoding='utf-8'); runtime=RUNTIME.read_text(encoding='utf-8')

def block_for(node):
    m=re.search(rf'^  {re.escape(node)}:\n',graph,re.M)
    if not m:return ''
    n=re.search(r'^  [A-Z]+-[0-9]+:\n',graph[m.end():],re.M)
    end=m.end()+n.start() if n else len(graph)
    return graph[m.start():end]

def current_pass_marker(tid):
    return f'## {tid} current accepted stable state' in runtime

def historical_pass_marker(tid):
    return f'## {tid} accepted stable state' in runtime

def show_task(tid):
    r=rows.get(tid); print(f'--- {tid} ---')
    if not r: print('WBS=MISSING'); return
    for k in ('Task_ID','Title','Layer','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_ID','Requirement_IDs','Interface_IDs','Source_Reference','Notes'):
        if k in r: print(f'{k}={r.get(k)}')
    print('RUNTIME_CURRENT_PASS='+str(current_pass_marker(tid)))
    print('RUNTIME_HISTORICAL_PASS='+str(historical_pass_marker(tid)))
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    for d in deps:
        print(f'DEP_{d}_STRICT_CURRENT_PASS='+str(current_pass_marker(d)))

for tid in ['TSK-0043','TSK-0309','TSK-0321','TSK-0628','TSK-0052']:
    show_task(tid)

print('TSK0052_ALL_STRICT_CURRENT_PREDECESSORS='+str(all(current_pass_marker(x) for x in ['TSK-0043','TSK-0321','TSK-0309','TSK-0628'])))
print('CR0006_RUNTIME_SUPERSESSION_TEXT='+str('Historical accepted-stable sections for `TSK-0333`, `TSK-0321`, `TSK-0309`, `TSK-0628` or other account-exclusion-dependent artifacts remain historical evidence only where CR-0006 changed acceptance; they do not satisfy the revised task state.' in runtime))

# Compare task contracts across the CR-0006 publication to identify material acceptance changes.
def csv_at(rev):
    raw=subprocess.check_output(['git','show',f'{rev}:Plans/Master/WBS/master-wbs.csv'])
    return {r['Task_ID']:r for r in csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))}
pre=csv_at('40a5e4612e08b25ac63dd9e63b142eec1179b877^')
post=csv_at('40a5e4612e08b25ac63dd9e63b142eec1179b877')
print('CR0006_PREDECESSOR_CONTRACT_DELTAS_BEGIN')
for tid in ['TSK-0043','TSK-0309','TSK-0321','TSK-0628','TSK-0052']:
    changed=[]
    for k in ('Title','Dependencies','Acceptance_Criteria','Plan_Status','Execution_State','AI_Capability_A0_A4','Action_Authority','Notes'):
        if pre[tid].get(k)!=post[tid].get(k): changed.append(k)
    print(f'{tid}|'+(';'.join(changed) if changed else 'NONE'))
print('CR0006_PREDECESSOR_CONTRACT_DELTAS_END')
