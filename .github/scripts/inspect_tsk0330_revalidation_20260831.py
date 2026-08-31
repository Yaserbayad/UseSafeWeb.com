import csv, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob(WBS)=='f3c29b5db8b835ef2c896f61335656ea51d8ba1c','TSK0330_WBS_CHANGED')
req(blob(RUNTIME)=='7ec16c5099c0a450bcac35da218a70692f51d9af','TSK0330_RUNTIME_CHANGED')
with WBS.open(newline='',encoding='utf-8-sig') as f:
    row=next(r for r in csv.DictReader(f) if r.get('Task_ID')=='TSK-0330')
print('---TSK-0330_WBS---')
for k,v in row.items():
    if v: print(f'{k}={v}')

runtime=RUNTIME.read_text(encoding='utf-8')
for heading in ('## TSK-0330 current accepted stable state','## TSK-0330 accepted stable state'):
    print(f'{heading}={"YES" if heading in runtime else "NO"}')
if '## TSK-0330 accepted stable state' in runtime:
    start=runtime.index('## TSK-0330 accepted stable state')
    end=runtime.find('\n## ',start+3)
    print('---TSK-0330_RUNTIME_SECTION_BEGIN---')
    print(runtime[start:end if end>=0 else len(runtime)])
    print('---TSK-0330_RUNTIME_SECTION_END---')

print('---TSK-0330_MATCHING_FILES_BEGIN---')
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and '0330' in p.as_posix().replace('-','').lower() and '.git/' not in p.as_posix():
        print(p.as_posix())
print('---TSK-0330_MATCHING_FILES_END---')
print('TSK0330_REVALIDATION_INSPECTION=PASS')
