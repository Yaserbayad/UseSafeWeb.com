#!/usr/bin/env python3
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
OUT = ROOT / 'TSK_0048_DEPENDENCY_ORDERED_VERTICAL_IMPLEMENTATION_BACKLOG_2026-09-02.md'

LANES = [
    ('FOUNDATION', 'Build/release foundation', ('build','lint','source','structure','dependency inventory','sbom','continuous integration','deployment automation','environment','server/network','script','secret','version pinning','configuration pipeline')),
    ('ACCOUNTLESS', 'Accountless public journey', ('public','landing','anonymous','routing','intake','phone','internet','services','completion')),
    ('DNS', 'DNS/AdGuard service and verification', ('dns','adguard','resolver','filter policy','doh','quad9','firewall','rate-limit','abuse')),
    ('SETUP', 'Configuration delivery, verification, recovery/removal', ('configuration delivery','activation','verification','private relay','vpn','secure dns','remove','removal','revoke','reset','replacement','reinstall','automated checks')),
    ('SAFEGUARD', 'Protection Map and safeguard guidance', ('protection map','safeguard','device/service content')),
    ('ACCOUNT', 'Optional parent account/session/device management', ('google sign-in','server session','parent account','dashboard','device provisioning','device cards','protection controls','clientid','ownership','account settings','sign-out','account deletion')),
    ('PRIVACY', 'Privacy, transparency, support and product events', ('privacy','retention','deletion','data-subject','support','feedback','false-positive','transparency','product events','metric validation','help')),
    ('OPS', 'Operations, observability, resilience and incident response', ('operational','metrics','dashboard','alert','notification','runbook','outage','incident','retry','reconciliation','backup','restore','recovery')),
    ('POLISH', 'Localization, accessibility and hardening', ('locale','rtl','accessibility','responsive','polish','troubleshooting','compatibility')),
]

def current_pass(state: str, tid: str) -> bool:
    pats = [
        rf'^##+\s+{re.escape(tid)}\s+current accepted stable state[^\n]*$',
        rf'^##+\s+{re.escape(tid)}\s+accepted stable state[^\n]*$',
    ]
    starts = []
    for pat in pats:
        starts.extend(m.start() for m in re.finditer(pat, state, re.M | re.I))
    if not starts:
        return False
    start = max(starts)
    end = state.find('\n## ', start + 3)
    if end < 0:
        end = len(state)
    section = state[start:end]
    return '**PASS**' in section or ': **PASS**' in section or '`: **PASS**' in section

def deps(row):
    return [x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()]

def lane_for(title: str):
    t = title.lower()
    best = None
    best_hits = 0
    for code, label, needles in LANES:
        hits = sum(1 for n in needles if n in t)
        if hits > best_hits:
            best = (code, label)
            best_hits = hits
    return best or ('CORE', 'Core implementation and integration')

def size_for(row):
    d = len(deps(row))
    crit = len(row.get('Acceptance_Criteria') or '')
    if d <= 1 and crit < 210:
        return 'S'
    return 'M'

def load_rows():
    with WBS.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    state = STATE.read_text(encoding='utf-8-sig')
    return rows, state

def topo(rows):
    selected = {r['Task_ID']: r for r in rows}
    indeg = {tid: 0 for tid in selected}
    children = defaultdict(list)
    for tid, row in selected.items():
        for d in deps(row):
            if d in selected:
                indeg[tid] += 1
                children[d].append(tid)
    ready = sorted([tid for tid, n in indeg.items() if n == 0])
    order = []
    depth = {tid: 0 for tid in ready}
    while ready:
        tid = ready.pop(0)
        order.append(tid)
        for c in sorted(children[tid]):
            depth[c] = max(depth.get(c, 0), depth.get(tid, 0) + 1)
            indeg[c] -= 1
            if indeg[c] == 0:
                ready.append(c)
                ready.sort()
    if len(order) != len(selected):
        missing = sorted(set(selected) - set(order))
        raise SystemExit(f'L6 dependency cycle or unresolved internal ordering: {missing}')
    return order, depth

def esc(s):
    return (s or '').replace('|', '/').replace('\n', ' ').strip()

def main():
    all_rows, state = load_rows()
    l6 = [r for r in all_rows if r.get('Lifecycle_Stage') == 'L6' and not current_pass(state, r['Task_ID'])]
    by_id = {r['Task_ID']: r for r in l6}
    order, depth = topo(l6)

    buckets = defaultdict(list)
    for tid in order:
        row = by_id[tid]
        code, label = lane_for(row.get('Title') or '')
        buckets[(depth.get(tid, 0), code, label)].append(tid)

    slices = []
    for key in sorted(buckets, key=lambda x: (x[0], x[1])):
        tids = buckets[key]
        for i in range(0, len(tids), 4):
            slices.append((key, tids[i:i+4]))

    pos = {tid: i for i, tid in enumerate(order)}
    lines = []
    lines += [
        '# TSK-0048 — Dependency-Ordered Vertical Implementation Backlog',
        '',
        '**Version:** 1.0.0  ',
        '**Date:** 2026-09-02  ',
        '**Authority:** Derived execution view from canonical `Plans/Master/WBS/master-wbs.csv`; WBS remains the sole task/dependency/acceptance authority.  ',
        '**Scope:** Current non-PASS L6 implementation work only. No task ID, dependency, gate, acceptance criterion, runtime state, product scope, or authority boundary is changed by this artifact.',
        '',
        '## Guardrails',
        '',
        '- Preserve the complete **accountless core**; mandatory login is prohibited for core value.',
        '- Optional Version-1 scope may include Google sign-in/server session, minimum parent/device ownership persistence, lightweight dashboard/device management, and deletion/recovery only within frozen scope.',
        '- Excluded: browsing/query/activity history, child accounts, unrestricted customer DNS administration, and unapproved product expansion.',
        '- CR-0009/DEC-0056 legal/regulatory/compliance work remains owner-external for sequencing only; this backlog makes no legal conclusion or legal PASS claim.',
        '- Production, spend, secrets, target-environment actions, and human-only decisions remain subject to their own gates and Action Authority.',
        '',
        f'## Backlog summary',
        '',
        f'- Current non-PASS L6 tasks represented: **{len(order)}**.',
        f'- Dependency-ordered execution slices: **{len(slices)}**; each slice contains at most 4 canonical tasks and is grouped by topological wave plus user/operational outcome lane.',
        '- Ordering rule: a task never appears before any non-PASS L6 dependency. Dependencies outside L6 must independently satisfy their own current gate/state before execution.',
        '- Size is a derived execution estimate (`S`/`M`) only; canonical task semantics remain in WBS. Risk is represented by canonical risk reference, plan priority, and critical-path flag.',
        '',
    ]

    for sn, ((wave, code, label), tids) in enumerate(slices, 1):
        lines += [f'## Slice {sn:02d} — Wave {wave} — {label}', '']
        lines += ['| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |',
                  '|---:|---|---|---|---|---|---|:---:|---|---|---|---|']
        for tid in tids:
            r = by_id[tid]
            ds = deps(r)
            bad = [d for d in ds if d in pos and pos[d] >= pos[tid]]
            if bad:
                raise SystemExit(f'ordering violation {tid}: {bad}')
            risk = '; '.join(x for x in [r.get('Risk_Reference'), f"priority {r.get('Priority')}", f"critical-path {r.get('Critical_Path')}"] if x)
            acceptance = f"{r.get('Acceptance_ID')}: {esc(r.get('Acceptance_Criteria'))}"
            verification = f"{r.get('Verification_ID')}: {esc(r.get('Verification_Method'))}"
            lines.append('| ' + ' | '.join([
                str(pos[tid] + 1),
                f"`{tid}` — {esc(r.get('Title'))}",
                esc(r.get('Primary_Owner')),
                esc(r.get('Dependencies')) or 'None',
                acceptance,
                verification,
                esc(r.get('Output/Artifact')),
                size_for(r),
                risk,
                esc(r.get('Relative_Timing')) or 'L6 / dependency-led',
                f"{esc(r.get('Action_Authority'))} / {esc(r.get('AI_Capability_A0_A4'))}",
                esc(r.get('Plan_Status')),
            ]) + ' |')
        lines += ['', '### Slice checkpoint', '', '- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.', '- Verify each task against its canonical acceptance/verification contract before any PASS state.', '- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.', '']

    lines += [
        '## Coverage checkpoints required before LG-07',
        '',
        '- Accountless public/setup journey and configuration delivery/verification are represented.',
        '- Optional authentication/session, parent/device ownership persistence, dashboard/device management, deletion/recovery are represented without making login mandatory.',
        '- AdGuard/DNS typed integration, privacy-minimal state/logging, Protection Map truth, native safeguard and relevant external-service guidance are represented.',
        '- Troubleshooting, removal/recovery, security/privacy negative tests, CI/release/recovery, observability/support/operations are represented.',
        '- No L6 task is marked PASS by this planning artifact. `TSK-0516`, `TSK-0047`, `TSK-0587`, `TSK-0051`, and later gates retain their own acceptance boundaries.',
        '',
        '## Execution handoff',
        '',
        'After TSK-0048 acceptance, create/accept TSK-0516 master verification and acceptance plan, then TSK-0047 release/checkpoint/rollback plan, while independently completing any other eligible L5 prerequisites. L6 build begins only after LG-07 is actually PASS under current authority.',
        '',
    ]
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'WROTE={OUT.name}')
    print(f'L6_TASKS={len(order)}')
    print(f'SLICES={len(slices)}')

if __name__ == '__main__':
    main()
