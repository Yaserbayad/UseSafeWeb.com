import csv
from pathlib import Path

root = Path('.')
wbs_path = root / 'Plans/Master/WBS/master-wbs.csv'
graph_path = root / 'Plans/Master/RELATIONSHIP_INDEX.yaml'
runtime_path = root / 'CURRENT_STATE.md'

with wbs_path.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
by_id = {r.get('Task_ID'): r for r in rows}

runtime = runtime_path.read_text(encoding='utf-8')
graph = graph_path.read_text(encoding='utf-8')

def current_pass(task_id: str) -> bool:
    marker = f'## {task_id} current accepted stable state'
    pos = runtime.find(marker)
    if pos < 0:
        return False
    nxt = runtime.find('\n## ', pos + 4)
    block = runtime[pos:nxt if nxt >= 0 else len(runtime)]
    return '**PASS**' in block or ': **PASS**' in block

def headings(task_id: str):
    out=[]
    for line in runtime.splitlines():
        if line.startswith('## ') and task_id in line:
            out.append(line)
    return out

def graph_block(task_id: str):
    key=f'  {task_id}:'
    start=graph.find(key)
    if start < 0:
        return ''
    end=graph.find('\n  TSK-', start+len(key))
    return graph[start:end if end >= 0 else len(graph)]

for tid in ['TSK-0322','TSK-0323','TSK-0324']:
    row=by_id.get(tid)
    if not row:
        raise SystemExit(f'MISSING_{tid}')
    print(f'--- {tid} ---')
    for k,v in row.items():
        if v:
            print(f'{k}={v}')
    print(f'{tid}_CURRENT_PASS={current_pass(tid)}')
    for h in headings(tid):
        print(f'{tid}_HEADING={h}')
    print(f'{tid}_GRAPH_BLOCK_BEGIN')
    print(graph_block(tid))
    print(f'{tid}_GRAPH_BLOCK_END')

print('RELATED_FILES_BEGIN')
needles=('0322','0323','0324','ACCESSIBILITY','CONTENT','DESIGN')
for p in sorted(root.rglob('*')):
    if not p.is_file() or '.git' in p.parts:
        continue
    s=str(p)
    if any(n.lower() in s.lower() for n in needles):
        print(s)
print('RELATED_FILES_END')
