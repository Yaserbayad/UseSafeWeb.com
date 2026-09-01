#!/usr/bin/env python3
from pathlib import Path
import csv, io

ROOT=Path('.')
DEC=ROOT/'Plans/Master/Registers/DECISIONS_TRIGGERS.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
STATE=ROOT/'CURRENT_STATE.md'
EVID=ROOT/'TSK_0413_OWNER_PRIVACY_BASELINE_RECONCILIATION_2026-09-01.md'

old_dec='| DEC-0016 | D-016 | DNS privacy configuration | FROZEN minimum — query/file logging off; identifiable stats off/excluded; IP anonymisation where possible; ECS off; no history metrics; diagnostics time-boxed/deleted. | Owner/repository decision 2026-08-26 | Direct deployed inspection/test required at every gate and after material change. | Project Owner | USW-02.05.01.002; USW-05.06.02; USW-08.02.02 | CURRENT_STATE.md; VALIDATION_READINESS_GATE.md |'
new_dec='| DEC-0016 | D-016 | DNS privacy configuration | FROZEN privacy-first baseline — persistent raw query history and file query logging are off; exceptional operational query diagnostics, if explicitly activated later, are time-boxed to a 24-hour maximum and deleted; only minimum anonymized aggregate operational statistics may be enabled with 24-hour retention; identifiable per-client statistics/history remain excluded; client IP anonymisation is on wherever records can contain it; ECS is off; browsing/activity-history metrics are prohibited. | Owner approval 2026-09-01, refining the 2026-08-26 minimum without weakening its identifiable-history prohibition. | Direct deployed inspection/test required at every gate and after material change; any diagnostic exception must prove the 24-hour ceiling and deletion. | Project Owner | USW-02.05.01.002; USW-05.06.02; USW-08.02.02; TSK-0410; TSK-0413 | CURRENT_STATE.md; VALIDATION_READINESS_GATE.md; explicit Project Owner approval `APPROVE TSK-0413 RECOMMENDED PRIVACY-FIRST ADGUARD BASELINE` 2026-09-01 |'
text=DEC.read_text(encoding='utf-8')
assert text.count(old_dec)==1, 'DEC-0016 baseline drift'
DEC.write_text(text.replace(old_dec,new_dec),encoding='utf-8')

lines=WBS.read_text(encoding='utf-8-sig').splitlines(keepends=True)
header=next(csv.reader([lines[0].rstrip('\r\n')]))
idx={name:i for i,name in enumerate(header)}
found=0
for i,line in enumerate(lines[1:],1):
    if not line.startswith('TSK-0410,'):
        continue
    row=next(csv.reader([line.rstrip('\r\n')]))
    assert row[idx['Task_ID']]=='TSK-0410'
    old='explicitly enforces no-querylog/no-statistics settings'
    new='explicitly enforces no-querylog/no-identifiable-statistics settings while allowing only the owner-approved anonymized aggregate operational statistics with 24-hour retention'
    assert old in row[idx['Acceptance_Criteria']], 'TSK-0410 ACC drift'
    row[idx['Acceptance_Criteria']]=row[idx['Acceptance_Criteria']].replace(old,new)
    note=' Owner approval 2026-09-01 reconciles the prior no-statistics shorthand to no-identifiable-statistics while allowing anonymized aggregate operational statistics for 24 hours; no browsing/query/activity history is authorized.'
    assert note.strip() not in row[idx['Notes']]
    row[idx['Notes']]=row[idx['Notes']].rstrip()+note
    out=io.StringIO(newline='')
    csv.writer(out,lineterminator='\n').writerow(row)
    lines[i]=out.getvalue()
    found+=1
assert found==1
WBS.write_text(''.join(lines),encoding='utf-8-sig')

EVID.write_text('''# TSK-0413 owner privacy-first AdGuard baseline reconciliation — 2026-09-01\n\n**Owner approval:** `APPROVE TSK-0413 RECOMMENDED PRIVACY-FIRST ADGUARD BASELINE`\n\n## Approved baseline\n\n- Persistent raw DNS query history: **off**.\n- File query logging: **off**.\n- Exceptional operational query diagnostics: allowed only when specifically needed later, with a **24-hour maximum** and deletion; this is not the default production state.\n- Operational statistics: **minimum anonymized aggregate statistics only**, enabled with **24-hour retention**; identifiable per-client statistics/history remain excluded.\n- Client IP anonymization: **on** wherever query/statistical records can contain client IP.\n- ECS: **off**.\n- Filter baseline: only the official **AdGuard DNS filter** is active initially; no stacked third-party lists without later evidence.\n- Allowlist/exceptions: minimal, centrally controlled, documented, reversible, and limited to verified false positives or essential functionality.\n- AdGuard administration: private management only, never directly public; authentication is mandatory; credentials remain outside Git.\n- Browsing/query/activity history remains prohibited.\n\n## Authority reconciliation\n\n`DEC-0016` is the owning privacy decision and is refined to persist the approved 24-hour anonymized aggregate-statistics baseline without weakening its historical prohibition on identifiable history. `REQ-0044` remains unchanged because default query/file logging stays off. `REQ-0045` remains unchanged because identifiable per-client statistics remain excluded and IP anonymization stays on.\n\n`TSK-0410` contained the older shorthand `no-querylog/no-statistics`. Its acceptance wording is narrowly reconciled to `no-querylog/no-identifiable-statistics` plus the owner-approved anonymized aggregate 24-hour statistics. No dependency, lifecycle, priority, action authority, task status, gate state, requirement, interface, or risk is changed.\n\n## Impact\n\n- `TSK-0413`: approved input is now durable and may be used to construct the versioned secret-safe recovery-consumable AdGuard bundle.\n- `TSK-0410`: future acceptance no longer contradicts the approved privacy baseline. No PASS is implied.\n- Current live AdGuard settings are not changed by this planning reconciliation; deployment remains separate governed work.\n- No LG-07 or downstream PASS is implied.\n''',encoding='utf-8')

state=STATE.read_text(encoding='utf-8').rstrip()
marker='## TSK-0413 owner-approved privacy-first AdGuard baseline — 2026-09-01'
assert marker not in state
state += f'''\n\n{marker}\n\nThe Project Owner approved `APPROVE TSK-0413 RECOMMENDED PRIVACY-FIRST ADGUARD BASELINE`. The owning DNS privacy decision (`DEC-0016`) and the stale future `TSK-0410` no-statistics shorthand are reconciled to the approved privacy-first semantics.\n\n- Default persistent raw/file query logging remains off.\n- Exceptional operational query diagnostics are capped at 24 hours and deleted.\n- Only minimum anonymized aggregate operational statistics may be enabled, with 24-hour retention; identifiable per-client statistics/history remain excluded.\n- Client-IP anonymization and ECS-off remain mandatory.\n- Initial filtering uses only the official AdGuard DNS filter; exceptions are minimal/central/reversible.\n- AdGuard administration remains private/authenticated; credentials and secret material stay outside Git.\n- This reconciliation does **not** mark `TSK-0413`, `TSK-0410`, `LG-07`, deployment, or production activation PASS.\n\n### Queue effect\n\n`TSK-0413` remains the current autonomous L5 task and may consume this owner-approved baseline plus current `TSK-0408` PASS evidence to construct and verify its versioned recovery-consumable bundle.\n'''
STATE.write_text(state.rstrip()+'\n',encoding='utf-8')
