import csv
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'; RUNTIME=ROOT/'CURRENT_STATE.md'; GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0321')
print('TSK0321_ALL_NONEMPTY_FIELDS_BEGIN')
for k,v in row.items():
    if v not in (None,''): print(f'{k}={v}')
print('TSK0321_ALL_NONEMPTY_FIELDS_END')
runtime=RUNTIME.read_text(encoding='utf-8')
for dep in [x.strip() for x in row.get('Dependencies','').split(';') if x.strip()]:
    print(f'{dep}_CURRENT_PASS='+str(f'## {dep} current accepted stable state' in runtime))
    # report headings containing dep to distinguish historical/current sections
    for line in runtime.splitlines():
        if line.startswith('## ') and dep in line: print(f'{dep}_HEADING={line}')
print('TSK0321_CURRENT_PASS='+str('## TSK-0321 current accepted stable state' in runtime))
print('TSK0321_CURRENT_WAITING='+str('## TSK-0321 current waiting state' in runtime))
print('TSK0321_HISTORICAL_PASS='+str('## TSK-0321 accepted stable state' in runtime))
# graph block
text=GRAPH.read_text(encoding='utf-8'); start=text.find('  TSK-0321:\n'); end=text.find('\n  TSK-',start+3)
print('TSK0321_GRAPH_BLOCK_BEGIN'); print(text[start:end if end>=0 else len(text)]); print('TSK0321_GRAPH_BLOCK_END')
# find product/evidence artifacts by token, excluding .github
hits=[]
for p in ROOT.rglob('*'):
    if p.is_file() and not p.as_posix().startswith('.github/'):
        s=p.as_posix()
        if '0321' in s or 'accessibility' in s.lower() or 'a11y' in s.lower(): hits.append(s)
print('TSK0321_RELATED_FILES_BEGIN')
for s in sorted(set(hits)): print(s)
print('TSK0321_RELATED_FILES_END')
