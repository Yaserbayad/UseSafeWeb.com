#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[3]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
OUT = ROOT / 'CR_0008_ACTION_AUTHORITY_AUDIT_2026-09-01.md'

with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))

human = [r for r in rows if (r.get('Action_Authority') or '').strip() in {'HUMAN_ONLY', 'HUMAN_APPROVAL_REQUIRED'}]

lines = [
    '# CR-0008 action-authority audit — 2026-09-01',
    '',
    '**Bounded audit evidence only. This file does not change task authority, scope, acceptance, dependencies, gates, or runtime PASS.**',
    '',
    f'- WBS rows parsed: `{len(rows)}`',
    f'- HUMAN_ONLY / HUMAN_APPROVAL_REQUIRED rows: `{len(human)}`',
    '',
    '| Row | Task | Lifecycle | Priority | Capability | Authority | Plan status | Task | Acceptance |',
    '|---:|---|---|---|---|---|---|---|---|',
]

def clean(v):
    return (v or '').replace('|', '\\|').replace('\n', ' ').strip()

for idx, r in enumerate(rows, start=2):
    auth = (r.get('Action_Authority') or '').strip()
    if auth not in {'HUMAN_ONLY', 'HUMAN_APPROVAL_REQUIRED'}:
        continue
    title = r.get('Task_Name') or r.get('Task_Title') or r.get('Title') or r.get('Task') or r.get('Description') or ''
    lines.append(
        f"| {idx} | `{clean(r.get('Task_ID'))}` | {clean(r.get('Lifecycle_Stage'))} | {clean(r.get('Priority'))} | "
        f"{clean(r.get('AI_Capability_A0_A4'))} | {clean(auth)} | {clean(r.get('Planning_Status') or r.get('Plan_Status') or r.get('Disposition'))} | "
        f"{clean(title)} | {clean(r.get('Acceptance_Criteria'))} |"
    )

lines += [
    '',
    '## Audit rule',
    '',
    'Review every row against DEC-0054/CR-0007 and the owner-approved CR-0008 direction. Reclassify only delegable research, analysis, architecture, design, drafting, coding, testing, objective evidence gates, or ordinary technical work. Preserve human authority for genuinely nondelegable legal signatures/attestations, contracts requiring human acceptance, identity/KYC/credential/consent acts requiring a person, named-market activation, organizational/entity formalization, material/unbudgeted commitments, strategic modify/pivot/pause/stop/transfer/resume, irreversible human-authority acts, and material frozen-scope changes.',
    '',
]
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'CR0008_AUTHORITY_AUDIT_ROWS={len(human)}')
print(f'CR0008_AUTHORITY_AUDIT_OUT={OUT.name}')
