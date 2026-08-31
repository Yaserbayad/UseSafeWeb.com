import csv, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob(WBS)=='f3c29b5db8b835ef2c896f61335656ea51d8ba1c','QUEUE_WBS_CHANGED')
req(blob(RUNTIME)=='7ec16c5099c0a450bcac35da218a70692f51d9af','QUEUE_RUNTIME_CHANGED')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    rows=list(csv.DictReader(f))
byid={r.get('Task_ID'):r for r in rows}
succ=[]
for r in rows:
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    if 'TSK-0331' in deps:
        succ.append(r.get('Task_ID'))
print('POST_TSK0331_SUCCESSORS='+';'.join(succ))

runtime=RUNTIME.read_text(encoding='utf-8')
for tid in sorted(set(succ+['TSK-0333','TSK-0335','TSK-0330'])):
    r=byid.get(tid)
    if not r: continue
    print(f'---{tid}---')
    for key,value in r.items():
        if value:
            print(f'{key}={value}')
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    markers=[]
    for dep in deps:
        current=f'## {dep} current accepted stable state'
        historical=f'## {dep} accepted stable state'
        if current in runtime: state='CURRENT_PASS'
        elif historical in runtime: state='HISTORICAL_OR_UNQUALIFIED_PASS'
        else: state='NO_CURRENT_PASS'
        markers.append(f'{dep}:{state}')
    print('DEPENDENCY_RUNTIME_MARKERS='+';'.join(markers))
    print(f'CURRENT_PASS_HEADING={"YES" if f"## {tid} current accepted stable state" in runtime else "NO"}')
    print(f'HISTORICAL_PASS_HEADING={"YES" if f"## {tid} accepted stable state" in runtime else "NO"}')

for tid in ('TSK-0333','TSK-0335'):
    print(f'---{tid}_MATCHING_FILES_BEGIN---')
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and tid.replace('-','').lower() in p.as_posix().replace('-','').lower() and '.git/' not in p.as_posix():
            print(p.as_posix())
    print(f'---{tid}_MATCHING_FILES_END---')

print('POST_TSK0331_QUEUE_INSPECTION=PASS')
