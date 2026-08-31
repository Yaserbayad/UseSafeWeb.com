import csv
import subprocess
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
EXPECTED_WBS = 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_STATE = '6feab0d1991035304293c25c0af1398e75ff91f7'


def blob(path: str) -> str:
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'], text=True).strip()

if blob(str(WBS)) != EXPECTED_WBS: raise SystemExit('unexpected WBS blob')
if blob(str(STATE)) != EXPECTED_STATE: raise SystemExit('unexpected state blob')
with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
for tid in ['TSK-0325','TSK-0328']:
    r = rows[tid]
    for k in ['Task_ID','Title','Lifecycle_Stage','Plan_Status','Execution_State','Priority','Dependencies','Acceptance_ID','Acceptance_Criteria','Verification_ID','Evidence_ID','AI_Capability_A0_A4','Action_Authority','Risk_Reference','Interface_Reference','Requirement_Reference','Source_Reference','Notes']:
        print(f'{tid}_FIELD|{k}|' + r.get(k,'').replace('\n',' ').replace('|','/'))
state = STATE.read_text(encoding='utf-8')
for tid in ['TSK-0325','TSK-0328']:
    print(f'{tid}_STATE_OCCURRENCES={state.count(tid)}')
    idx = state.find(tid)
    if idx >= 0:
        print(f'{tid}_STATE_SNIPPET|' + state[max(0,idx-220):idx+1400].replace('\n',' ').replace('|','/'))
for tid in ['0325','0328']:
    found=[]
    for p in Path('.').rglob(f'*{tid}*'):
        if '.git' in p.parts or not p.is_file(): continue
        path=p.as_posix().lstrip('./')
        try: sha=blob(path)
        except Exception: continue
        found.append((path,sha,p.stat().st_size))
    for path,sha,size in sorted(found): print(f'TSK{tid}_FILE|{path}|{sha}|{size}')
    print(f'TSK{tid}_FILE_COUNT={len(found)}')
print('TSK0325_PREFLIGHT_INSPECTION=PASS')
