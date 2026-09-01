#!/usr/bin/env python3
from pathlib import Path
import csv
import os
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
OUT = ROOT / 'CURRENT_L5_FRONTIER_AUDIT_2026-09-01.md'
SOURCE_COMMIT = os.environ.get('SOURCE_COMMIT', 'UNKNOWN')
RUN_ID = os.environ.get('GITHUB_RUN_ID', 'LOCAL')
RUN_ATTEMPT = os.environ.get('GITHUB_RUN_ATTEMPT', '1')


def norm(value):
    return (value or '').strip()


def get(row, *names):
    for name in names:
        if name in row:
            return norm(row.get(name))
    return ''


def task_ids(value):
    return re.findall(r'TSK-\d{4}', value or '')


def md(value):
    return (value or '').replace('|', '\\|').replace('\n', ' ').strip()


state = STATE.read_text(encoding='utf-8')
with WBS.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames or []
    rows = list(reader)

if 'Task_ID' not in fieldnames or 'Lifecycle_Stage' not in fieldnames or 'Dependencies' not in fieldnames:
    raise SystemExit(f'FRONTIER_AUDIT_FAIL: unexpected WBS header: {fieldnames}')

# Current dependency proof is deliberately strict. A task counts as current PASS only when
# CURRENT_STATE has an explicit current-accepted-stable-state heading for that task.
# This avoids the previously rejected heuristic "task id appears somewhere + some PASS appears somewhere".
accepted = set(re.findall(
    r'^##\s+(TSK-\d{4})(?:\s*/[^\n#]+)?\s+current accepted stable state\b',
    state,
    flags=re.MULTILINE | re.IGNORECASE,
))

lg06_heading = '## TSK-0052 / LG-06 current accepted stable state — 2026-09-01 — POST-CR-0007'
if lg06_heading not in state:
    raise SystemExit('FRONTIER_AUDIT_FAIL: current LG-06 PASS heading not found')
if 'TSK-0446' not in accepted or 'TSK-0518' not in accepted or 'TSK-0413' not in accepted:
    raise SystemExit('FRONTIER_AUDIT_FAIL: expected current accepted predecessor headings absent')

priority_rank = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
excluded_planning = {'NOT_APPLICABLE', 'DEFERRED', 'CANCELLED', 'CANCELED'}

l5 = []
for idx, row in enumerate(rows, start=2):
    if get(row, 'Lifecycle_Stage') != 'L5':
        continue
    tid = get(row, 'Task_ID')
    deps = task_ids(get(row, 'Dependencies'))
    missing = [d for d in deps if d not in accepted]
    planning = get(row, 'Planning_Status', 'Disposition', 'Plan_Status')
    authority = get(row, 'Action_Authority')
    capability = get(row, 'AI_Capability_A0_A4')
    priority = get(row, 'Priority').upper()
    already_pass = tid in accepted
    excluded = planning.upper() in excluded_planning
    dep_ready = not missing
    auto = authority == 'AUTO_ALLOWED'
    human = authority in {'HUMAN_ONLY', 'HUMAN_APPROVAL_REQUIRED'}
    # Unknown action authority fails closed rather than being treated as autonomous.
    eligible_auto = (not already_pass and not excluded and dep_ready and auto)
    human_ready = (not already_pass and not excluded and dep_ready and human)
    l5.append({
        'idx': idx,
        'row': row,
        'tid': tid,
        'deps': deps,
        'missing': missing,
        'planning': planning,
        'authority': authority,
        'capability': capability,
        'priority': priority,
        'already_pass': already_pass,
        'excluded': excluded,
        'eligible_auto': eligible_auto,
        'human_ready': human_ready,
    })

# Sort strictly by objective plan priority and WBS order. Project-level safety/gate/dependency
# constraints are represented separately below; customer-value tie-breaking is intentionally not
# invented when no explicit WBS field encodes it.
def sort_key(item):
    return (priority_rank.get(item['priority'], 9), item['idx'], item['tid'])

eligible_auto = sorted([x for x in l5 if x['eligible_auto']], key=sort_key)
human_ready = sorted([x for x in l5 if x['human_ready']], key=sort_key)
blocked = sorted([
    x for x in l5
    if not x['already_pass'] and not x['excluded'] and not x['eligible_auto'] and not x['human_ready']
], key=sort_key)
passed = sorted([x for x in l5 if x['already_pass']], key=sort_key)
excluded = sorted([x for x in l5 if x['excluded']], key=sort_key)

# Surface any task-specific gate/trigger/precondition/control columns instead of silently assuming none exist.
control_cols = [c for c in fieldnames if any(k in c.lower() for k in ('gate', 'trigger', 'precondition'))]

def control_summary(row):
    vals = []
    for c in control_cols:
        v = norm(row.get(c))
        if v:
            vals.append(f'{c}={v}')
    return '; '.join(vals) or '—'


def title(row):
    return get(row, 'Task_Name', 'Task_Title', 'Title', 'Task', 'Description')


def refs(row, *tokens):
    vals = []
    for c in fieldnames:
        cl = c.lower()
        if any(t in cl for t in tokens):
            v = norm(row.get(c))
            if v:
                vals.append(f'{c}={v}')
    return '; '.join(vals) or '—'


def line_for(x):
    row = x['row']
    deps = ', '.join(x['deps']) or 'none'
    dep_proof = ', '.join(f'{d}=CURRENT_PASS' if d in accepted else f'{d}=MISSING_CURRENT_PASS' for d in x['deps']) or 'none'
    return (
        f"| {x['idx']} | `{x['tid']}` | {md(x['priority'])} | {md(x['capability'])} | {md(x['authority'])} | "
        f"{md(x['planning'] or '—')} | {md(deps)} | {md(dep_proof)} | {md(control_summary(row))} | "
        f"{md(title(row))} | {md(get(row, 'Acceptance_Criteria'))} |"
    )


def section(title_text, items):
    out = [f'## {title_text}', '']
    if not items:
        out += ['_None._', '']
        return out
    out += [
        '| WBS row | Task | Priority | Capability | Action authority | Planning status | Hard deps | Current dependency proof | Gate/trigger/precondition fields | Task | Acceptance |',
        '|---:|---|---|---|---|---|---|---|---|---|---|',
    ]
    out += [line_for(x) for x in items]
    out += ['']
    return out

counts = Counter(x['priority'] for x in l5)
lines = [
    '# Current L5 frontier audit — 2026-09-01',
    '',
    '**Derived audit only — not a mutable state store, WBS, checkpoint, task claim, or PASS decision.**',
    '',
    f'- Source commit: `{SOURCE_COMMIT}`',
    f'- GitHub Actions run/attempt: `{RUN_ID} / {RUN_ATTEMPT}`',
    '- Canonical inputs: `Plans/Master/WBS/master-wbs.csv` + `CURRENT_STATE.md` on the source commit.',
    '- Gate prerequisite: current `TSK-0052 / LG-06` accepted-stable heading is present.',
    f'- WBS rows parsed: `{len(rows)}`; L5 rows: `{len(l5)}`.',
    f'- Current accepted task headings detected: `{len(accepted)}`.',
    f'- L5 priorities: `{dict(sorted(counts.items()))}`.',
    f'- Autonomous dependency-ready candidates: `{len(eligible_auto)}`.',
    f'- Human-boundary dependency-ready candidates: `{len(human_ready)}`.',
    f'- Non-ready/non-human candidates: `{len(blocked)}`.',
    '',
    '## Selection semantics',
    '',
    '1. Current dependency satisfaction comes only from explicit `current accepted stable state` task headings in `CURRENT_STATE.md`.',
    '2. Historical WBS `Runtime_State`, stray PASS text, remembered state, adjacency, or artifact existence do not satisfy dependencies.',
    '3. L5 work is considered only because the current LG-06 accepted-stable heading exists.',
    '4. `NOT_APPLICABLE`, `DEFERRED`, or cancelled planning dispositions are excluded from executable candidates.',
    '5. `AUTO_ALLOWED` and dependency-ready tasks are listed separately from `HUMAN_ONLY` / `HUMAN_APPROVAL_REQUIRED` tasks.',
    '6. Ordering inside each list is explicit WBS priority (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`) then WBS row/task ID. No unstated customer-value tie-breaker is invented.',
    '7. Any non-empty task gate/trigger/precondition fields are surfaced for manual governor reconciliation before execution.',
    '',
]
lines += section('Eligible autonomous L5 candidates', eligible_auto)
lines += section('Dependency-ready human boundary', human_ready)
lines += section('L5 tasks blocked or unresolved', blocked)
lines += section('Current accepted L5 tasks', passed)
lines += section('Planning-excluded L5 tasks', excluded)

# Add compact control references for top candidates to support authoritative manual reconciliation.
lines += ['## Top-candidate control references', '']
for x in (eligible_auto[:12] + human_ready[:8]):
    row = x['row']
    lines += [
        f"### {x['tid']}",
        '',
        f"- Risk/constraint refs: {refs(row, 'risk', 'constraint')}",
        f"- Requirement refs: {refs(row, 'requirement')}",
        f"- Interface refs: {refs(row, 'interface')}",
        f"- Evidence/verification refs: {refs(row, 'acceptance_id', 'verification_id', 'evidence_id')}",
        f"- Critical-path field(s): {refs(row, 'critical_path')}",
        '',
    ]

lines += [
    '## Governor disposition',
    '',
    'This audit does not itself choose or execute a task. The governor must inspect the highest-ranked autonomous candidate against any surfaced gates/triggers/preconditions, current referenced risks/requirements/interfaces, current owner decisions (including DEC-0016 / TSK-0413), and any contradictory current evidence before execution.',
    '',
]
OUT.write_text('\n'.join(lines), encoding='utf-8')

print('CURRENT_L5_FRONTIER_AUDIT=PASS')
print(f'source_commit={SOURCE_COMMIT}')
print(f'l5_rows={len(l5)}')
print(f'accepted_headings={len(accepted)}')
print(f'eligible_auto={len(eligible_auto)}')
print(f'human_ready={len(human_ready)}')
for x in eligible_auto[:20]:
    print(f"ELIGIBLE_AUTO|{x['priority']}|{x['idx']}|{x['tid']}|deps={','.join(x['deps']) or 'none'}|authority={x['authority']}|title={title(x['row'])}")
for x in human_ready[:20]:
    print(f"HUMAN_READY|{x['priority']}|{x['idx']}|{x['tid']}|deps={','.join(x['deps']) or 'none'}|authority={x['authority']}|title={title(x['row'])}")
