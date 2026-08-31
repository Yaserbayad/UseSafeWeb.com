import csv
from pathlib import Path

ROOT = Path('.')
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
GRAPH = ROOT / 'Plans/Master/RELATIONSHIP_INDEX.yaml'
RUNTIME = ROOT / 'CURRENT_STATE.md'
TASK = 'TSK-0332'

with WBS.open(newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
row = next((r for r in rows if r.get('Task_ID') == TASK), None)
if not row:
    raise SystemExit('TSK0332_WBS_MISSING')

for key in ['Task_ID','Task_Name','Lifecycle_Stage','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_Reference','Requirement_Reference','Interface_Reference','Source_Reference']:
    print(f'{key}={row.get(key, "")}')

runtime = RUNTIME.read_text(encoding='utf-8')
for dep in [x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()]:
    marker = f'## {dep} current accepted stable state'
    if marker not in runtime:
        raise SystemExit(f'TSK0332_DEPENDENCY_NOT_CURRENT_PASS={dep}')
print('TSK0332_DEPENDENCY_RUNTIME=PASS')

lines = GRAPH.read_text(encoding='utf-8').splitlines()
start = next((i for i,l in enumerate(lines) if l.strip() == f'{TASK}:'), None)
if start is None:
    raise SystemExit('TSK0332_GRAPH_MISSING')
end = len(lines)
base_indent = len(lines[start]) - len(lines[start].lstrip())
for i in range(start+1, len(lines)):
    s = lines[i]
    if s.strip() and (len(s)-len(s.lstrip())) == base_indent and s.strip().endswith(':'):
        end = i
        break
block = lines[start:end]
print('---GRAPH_TSK0332_BEGIN---')
print('\n'.join(block))
print('---GRAPH_TSK0332_END---')
for dep in [x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()]:
    if not any(f'target: {dep}' in l for l in block) or not any('type: depends_on' in l for l in block):
        raise SystemExit(f'TSK0332_GRAPH_DEP_MISSING={dep}')
print('TSK0332_GRAPH_DEPENDENCIES=PASS')

matches=[]
for p in ROOT.rglob('*'):
    if p.is_file() and '0332' in p.as_posix().lower() and '.git/' not in p.as_posix():
        matches.append(p.as_posix())
print('---TSK0332_MATCHING_FILES_BEGIN---')
for p in sorted(matches): print(p)
print('---TSK0332_MATCHING_FILES_END---')
print(f'TSK0332_MATCHING_FILE_COUNT={len(matches)}')

# Current-scope guard: runtime must already contain current TSK-0329 and TSK-0142 PASS.
for dep in ('TSK-0329','TSK-0142'):
    if f'## {dep} current accepted stable state' not in runtime:
        raise SystemExit(f'TSK0332_REQUIRED_CURRENT_PASS_MISSING={dep}')
print('TSK0332_CURRENT_INSPECTION=PASS')
