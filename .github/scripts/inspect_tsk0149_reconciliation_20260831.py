import csv
import subprocess
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
EXPECTED_WBS = 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_STATE = 'e3d8a09ccf42f61f65b48ecd2e43773a7300bfbf'


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()

if blob(str(WBS)) != EXPECTED_WBS:
    raise SystemExit('unexpected WBS blob')
if blob(str(STATE)) != EXPECTED_STATE:
    raise SystemExit('unexpected CURRENT_STATE blob')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows['TSK-0149']
for k in ['Task_ID','Title','Plan_Status','Execution_State','Priority','Dependencies','Acceptance_ID','Acceptance_Criteria','Verification_ID','Evidence_ID','AI_Capability_A0_A4','Action_Authority','Source_Reference','Notes']:
    print('TSK0149_ROW|' + k + '|' + r.get(k,'').replace('\n',' ').replace('|','/'))

state = STATE.read_text(encoding='utf-8')
for needle in ['TSK-0149','ACC-0149','EVD-0149']:
    positions = []
    start = 0
    while True:
        idx = state.find(needle, start)
        if idx < 0:
            break
        positions.append(idx)
        start = idx + len(needle)
    print(f'STATE_OCCURRENCES|{needle}|{len(positions)}')
    for idx in positions[:5]:
        snippet = state[max(0, idx-220):idx+900].replace('\n',' ').replace('|','/')
        print(f'STATE_SNIPPET|{needle}|{snippet}')

matches = []
for p in Path('.').rglob('*0149*'):
    if '.git' in p.parts or not p.is_file():
        continue
    path = p.as_posix().lstrip('./')
    try:
        sha = blob(path)
    except Exception:
        continue
    matches.append((path, sha, p.stat().st_size))
for path, sha, size in sorted(matches):
    print(f'TSK0149_FILE|{path}|{sha}|{size}')
print(f'TSK0149_FILE_COUNT={len(matches)}')

# Also discover source files that mention ACC-0149/TSK-0149 even when filename differs.
mention_paths = []
for p in Path('.').rglob('*.md'):
    if '.git' in p.parts or p.stat().st_size > 2_000_000:
        continue
    try:
        txt = p.read_text(encoding='utf-8')
    except Exception:
        continue
    if 'ACC-0149' in txt or 'TSK-0149' in txt:
        mention_paths.append(p.as_posix().lstrip('./'))
for path in sorted(set(mention_paths))[:50]:
    print(f'TSK0149_MENTION|{path}|{blob(path)}')
print(f'TSK0149_MENTION_COUNT={len(set(mention_paths))}')
print('TSK0149_RECON_INSPECTION=PASS')
