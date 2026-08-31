import csv
import re
import subprocess
from pathlib import Path

WBS = Path('Plans/Master/WBS/master-wbs.csv')
STATE = Path('CURRENT_STATE.md')
GRAPH = Path('Plans/Master/RELATIONSHIP_INDEX.yaml')

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows.get('TSK-0329')
if r is None:
    raise SystemExit('TSK-0329 missing from WBS')
for key in [
    'Task_ID', 'Task_Name', 'Lifecycle_Stage', 'Priority', 'Plan_Status', 'Execution_State',
    'Dependencies', 'Acceptance_ID', 'Verification_ID', 'Evidence_ID',
    'AI_Capability_A0_A4', 'Action_Authority', 'Requirement_Reference', 'Interface_Reference',
    'Risk_Reference', 'Gate_Reference', 'Decision_Reference', 'Source_Reference'
]:
    if key in r:
        print(f'{key}={r.get(key, "")}')

state = STATE.read_text(encoding='utf-8')
for marker in [
    '## TSK-0328 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0312 current accepted stable state — 2026-08-31',
]:
    if marker not in state:
        raise SystemExit(f'missing dependency runtime marker: {marker}')
if '## TSK-0329 current accepted stable state' in state:
    raise SystemExit('TSK-0329 already accepted in runtime')
print('TSK0329_DEPENDENCY_RUNTIME=PASS')

graph = GRAPH.read_text(encoding='utf-8')
lines = graph.splitlines()
start = next((i for i, line in enumerate(lines) if line == '  TSK-0329:'), None)
if start is None:
    raise SystemExit('TSK-0329 graph entity missing')
end = len(lines)
for i in range(start + 1, len(lines)):
    if re.match(r'^  [^ ].*:$', lines[i]):
        end = i
        break
block = '\n'.join(lines[start:end])
print('---GRAPH_TSK0329_BEGIN---')
print(block)
print('---GRAPH_TSK0329_END---')
for dep in ['TSK-0328', 'TSK-0312']:
    if f'target: {dep}' not in block:
        raise SystemExit(f'missing graph dependency: {dep}')
print('TSK0329_GRAPH_DEPENDENCIES=PASS')

files = subprocess.check_output(['git', 'ls-files'], text=True).splitlines()
matches = [p for p in files if '0329' in p.lower()]
print('---TSK0329_MATCHING_FILES_BEGIN---')
for p in matches:
    print(p)
print('---TSK0329_MATCHING_FILES_END---')
print(f'TSK0329_MATCHING_FILE_COUNT={len(matches)}')
print('TSK0329_CURRENT_INSPECTION=PASS')
