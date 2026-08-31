import csv, os, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME=ROOT/'CURRENT_STATE.md'

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob(WBS)=='f3c29b5db8b835ef2c896f61335656ea51d8ba1c','TSK0331_WBS_CHANGED')
req(blob(RUNTIME)=='b5700eef473850ac49fdc83ea5bfbe7f2c6e54f2','TSK0331_RUNTIME_CHANGED')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0331')
for key,value in row.items():
    if value:
        print(f'{key}={value}')

req(row.get('Dependencies')=='TSK-0332; TSK-0334','TSK0331_DEPENDENCIES_CHANGED')
req(row.get('Acceptance_ID')=='ACC-0331' and row.get('Verification_ID')=='VER-0331' and row.get('Evidence_ID')=='EVD-0331','TSK0331_ACCEPTANCE_CONTRACT_CHANGED')
req(row.get('AI_Capability_A0_A4')=='A4' and row.get('Action_Authority')=='AUTO_ALLOWED','TSK0331_AUTHORITY_CHANGED')

runtime=RUNTIME.read_text(encoding='utf-8')
for dep in ('TSK-0332','TSK-0334'):
    req(f'## {dep} current accepted stable state — 2026-08-31 — POST-CR-0007' in runtime,f'TSK0331_DEP_NOT_CURRENT_PASS={dep}')
print('TSK0331_DEPENDENCIES_CURRENT_PASS=PASS')

graph=GRAPH.read_text(encoding='utf-8')
start=graph.find('  TSK-0331:\n')
req(start>=0,'TSK0331_GRAPH_MISSING')
end=graph.find('\n  TSK-',start+3)
block=graph[start:end if end>=0 else len(graph)]
for dep in ('TSK-0332','TSK-0334'):
    req(f'target: {dep}' in block,'TSK0331_GRAPH_DEP_MISSING='+dep)
for ref in ('ACC-0331','VER-0331','EVD-0331','REQ-0028','REQ-0029','CON-0010','CON-0017','INT-0009','INT-0010'):
    req(f'target: {ref}' in block,'TSK0331_GRAPH_REF_MISSING='+ref)
print('TSK0331_GRAPH_CONTRACT=PASS')

matches=[]
for p in ROOT.rglob('*'):
    if p.is_file() and '0331' in p.as_posix().lower() and not p.as_posix().startswith('.git/'):
        matches.append(p.as_posix())
print('TSK0331_MATCHING_FILES_BEGIN')
for p in sorted(matches): print(p)
print('TSK0331_MATCHING_FILES_END')

print('TSK0331_CURRENT_INSPECTION=PASS')
