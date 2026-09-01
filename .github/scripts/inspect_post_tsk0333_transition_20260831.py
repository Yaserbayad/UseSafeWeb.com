import csv,re,subprocess,io
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
    for k in ('Task_ID','Task_Name','Title','Layer','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_ID','Requirement_IDs','Interface_IDs','Source_Reference','Notes'):
        if k in r: print(f'{k}={r.get(k)}')
    print('RUNTIME_CURRENT_PASS='+str(f'## {tid} current accepted stable state' in runtime))
    print('RUNTIME_CURRENT_WAITING='+str(f'## {tid} current waiting state' in runtime))
    print('RUNTIME_HISTORICAL_PASS='+str(f'## {tid} accepted stable state' in runtime))
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    for d in deps:
        print(f'DEP_{d}_CURRENT_PASS='+str(f'## {d} current accepted stable state' in runtime or (f'`{d}' in runtime and ': **PASS**' in runtime)))

succ=[]
for m in re.finditer(r'^  (TSK-[0-9]+):\n',graph,re.M):
    tid=m.group(1); b=block_for(tid)
    if 'target: TSK-0333' in b: succ.append(tid)
print('POST_TSK0333_SUCCESSORS='+(';'.join(succ) if succ else 'NONE'))
for tid in sorted(set(succ+['TSK-0052'])): show_task(tid)
for node in ('TSK-0052','LG-06'):
    b=block_for(node)
    targets=re.findall(r'target: ([A-Z0-9-]+)',b)
    print(f'{node.replace("-","")}_GRAPH_TARGETS='+';'.join(targets))
found=[]
for p in ROOT.rglob('*'):
    if p.is_file() and ('TSK_0052' in p.name or 'TSK-0052' in p.as_posix()) and not p.as_posix().startswith('.github/'):
        found.append(p.as_posix())
print('TSK0052_EXISTING_ARTIFACTS='+';'.join(sorted(found)) if found else 'TSK0052_EXISTING_ARTIFACTS=NONE')

print('GATE_AUTHORITY_PEERS_BEGIN')
for tid,r in sorted(rows.items()):
    title=(r.get('Task_Name') or r.get('Title') or '').strip()
    if re.search(r'\bLG-(?:0[6-9]|1[0-5])\b', title):
        print('|'.join([tid,title,r.get('AI_Capability_A0_A4') or '',r.get('Action_Authority') or '',r.get('Plan_Status') or '',r.get('Execution_State') or '']))
print('GATE_AUTHORITY_PEERS_END')

# Inspect the exact authority transitions made by canonical CR-0007.
def csv_at(rev):
    raw=subprocess.check_output(['git','show',f'{rev}:Plans/Master/WBS/master-wbs.csv'])
    text=raw.decode('utf-8-sig')
    return {r['Task_ID']:r for r in csv.DictReader(io.StringIO(text))}
old=csv_at('c730c8c147e8cb4559ee03c8fe5b8a91429bc2c6^')
new=csv_at('c730c8c147e8cb4559ee03c8fe5b8a91429bc2c6')
print('CR0007_AUTHORITY_TRANSITIONS_BEGIN')
for tid in sorted(new):
    a=(old[tid].get('AI_Capability_A0_A4'),old[tid].get('Action_Authority'))
    b=(new[tid].get('AI_Capability_A0_A4'),new[tid].get('Action_Authority'))
    if a!=b:
        title=new[tid].get('Task_Name') or new[tid].get('Title') or ''
        print('|'.join([tid,title,a[0] or '',a[1] or '',b[0] or '',b[1] or '']))
print('CR0007_AUTHORITY_TRANSITIONS_END')
