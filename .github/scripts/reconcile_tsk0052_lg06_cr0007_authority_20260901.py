#!/usr/bin/env python3
import csv
import hashlib
import io
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('.')
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
AUTONOMY = ROOT / 'Plans/Master/Governance/AUTONOMY_POLICY.yaml'
GENERATED = ROOT / 'Plans/Master/Generated/MASTER_PLAN_FULL.md'
SUMS = ROOT / 'Plans/SHA256SUMS.txt'
RUNTIME = ROOT / 'CURRENT_STATE.md'
EVIDENCE = ROOT / 'TSK_0052_LG06_CR0007_AUTO_AUTHORITY_RECONCILIATION_EVIDENCE_2026-09-01.md'
TARGET = 'TSK-0052'
EXPECTED_DEPS = 'TSK-0043; TSK-0321; TSK-0309; TSK-0628'
EXPECTED_ACC = ('LG-06 passes only if the Version-1 product/non-goals are frozen as a dual-mode baseline: the complete accountless core setup/protection journey remains usable without login, and optional parent account, Google sign-in/session, minimum parent/device ownership persistence, lightweight dashboard/device management, account/device deletion/recovery and associated privacy/security/truth states are included. Requirements, setup/Protection-Map journey, brand/design system, content, accessibility/i18n, self-service and traceability must be internally/automatically accepted to the current L4 contract; mandatory login, browsing/activity history, child accounts and broad DNS administration remain excluded; critical conflicts are resolved. Under DEC-0052 no real-user evidence is required before this gate and none may be inferred.')


def read_rows():
    with WBS.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def one_row(rows):
    hits = [r for r in rows if r.get('Task_ID') == TARGET]
    if len(hits) != 1:
        raise SystemExit(f'expected exactly one {TARGET} row, found {len(hits)}')
    return hits[0]


def update_target_line():
    raw = WBS.read_bytes()
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    lines = text.splitlines(keepends=True)
    if not lines:
        raise SystemExit('empty WBS')
    header = next(csv.reader([lines[0].rstrip('\r\n')]))
    cap_i = header.index('AI_Capability_A0_A4')
    auth_i = header.index('Action_Authority')
    id_i = header.index('Task_ID')
    matches = []
    for i, line in enumerate(lines[1:], 1):
        row = next(csv.reader([line.rstrip('\r\n')]))
        if len(row) != len(header):
            raise SystemExit(f'multiline/unexpected CSV record at physical line {i+1}')
        if row[id_i] == TARGET:
            matches.append((i, row, line[len(line.rstrip(chr(10)+chr(13))):]))
    if len(matches) != 1:
        raise SystemExit(f'expected one physical {TARGET} row, found {len(matches)}')
    i, row, ending = matches[0]
    if row[cap_i] != 'A1' or row[auth_i] != 'HUMAN_ONLY':
        raise SystemExit(f'unexpected pre-authority {row[cap_i]}/{row[auth_i]}')
    row[cap_i] = 'A4'
    row[auth_i] = 'AUTO_ALLOWED'
    out = io.StringIO(newline='')
    csv.writer(out, lineterminator='').writerow(row)
    lines[i] = out.getvalue() + ending
    encoded = ''.join(lines).encode('utf-8')
    if bom:
        encoded = b'\xef\xbb\xbf' + encoded
    WBS.write_bytes(encoded)


def update_autonomy_projection():
    text = AUTONOMY.read_text(encoding='utf-8')
    replacements = {
        r'(?m)^  A1: 53$': '  A1: 52',
        r'(?m)^  A4: 58$': '  A4: 59',
        r'(?m)^  AUTO_ALLOWED: 539$': '  AUTO_ALLOWED: 540',
        r'(?m)^  HUMAN_ONLY: 53$': '  HUMAN_ONLY: 52',
    }
    for pat, repl in replacements.items():
        text2, n = re.subn(pat, repl, text)
        if n != 1:
            raise SystemExit(f'autonomy projection precondition failed: {pat} count={n}')
        text = text2
    AUTONOMY.write_text(text, encoding='utf-8')


def rebuild():
    subprocess.run(['python3', 'Plans/Master/Tools/rebuild_master_plan.py'], check=True)


def refresh_sums():
    lines = SUMS.read_text(encoding='utf-8').splitlines()
    out = []
    for line in lines:
        if not line.strip():
            continue
        old, rel = line.split('  ', 1)
        p = ROOT / 'Plans' / rel
        if not p.is_file():
            raise SystemExit(f'checksum path missing: {rel}')
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        out.append(f'{h}  {rel}')
    SUMS.write_text('\n'.join(out) + '\n', encoding='utf-8')


def verify_apply(before_rows):
    after_rows = read_rows()
    before = {r['Task_ID']: r for r in before_rows}
    after = {r['Task_ID']: r for r in after_rows}
    if before.keys() != after.keys() or len(after) != 641:
        raise SystemExit('WBS identity/count changed')
    changed = []
    for tid in before:
        for key in before[tid]:
            if before[tid].get(key) != after[tid].get(key):
                changed.append((tid, key, before[tid].get(key), after[tid].get(key)))
    expected = [
        (TARGET, 'AI_Capability_A0_A4', 'A1', 'A4'),
        (TARGET, 'Action_Authority', 'HUMAN_ONLY', 'AUTO_ALLOWED'),
    ]
    if changed != expected:
        raise SystemExit(f'unexpected WBS semantic changes: {changed}')
    r = one_row(after_rows)
    if r.get('Dependencies') != EXPECTED_DEPS:
        raise SystemExit('dependencies changed')
    if r.get('Acceptance_Criteria') != EXPECTED_ACC:
        raise SystemExit('acceptance changed')
    if r.get('Plan_Status') != 'PLANNED' or r.get('Execution_State') != 'WAITING':
        raise SystemExit('planning/execution snapshot changed')
    if r.get('Acceptance_ID') != 'ACC-0052' or r.get('Verification_ID') != 'VER-0052' or r.get('Evidence_ID') != 'EVD-0052':
        raise SystemExit('ACC/VER/EVD identity changed')


def apply():
    before_rows = read_rows()
    r = one_row(before_rows)
    if r.get('Dependencies') != EXPECTED_DEPS or r.get('Acceptance_Criteria') != EXPECTED_ACC:
        raise SystemExit('current TSK-0052 contract differs from approved repair precondition')
    update_target_line()
    update_autonomy_projection()
    verify_apply(before_rows)
    rebuild()
    refresh_sums()
    subprocess.run(['python3', 'Plans/Master/Tools/validate_master_plan.py'], check=True)
    print('TSK0052_AUTHORITY_REPAIR=A4/AUTO_ALLOWED')
    print('TSK0052_CONTRACT_UNCHANGED=PASS')


def blob_at(commit, path):
    return subprocess.check_output(['git', 'rev-parse', f'{commit}:{path}'], text=True).strip()


def record():
    commit = os.environ['PLAN_COMMIT']
    run_id = os.environ['GITHUB_RUN_ID']
    wbs_blob = blob_at(commit, 'Plans/Master/WBS/master-wbs.csv')
    auto_blob = blob_at(commit, 'Plans/Master/Governance/AUTONOMY_POLICY.yaml')
    gen_blob = blob_at(commit, 'Plans/Master/Generated/MASTER_PLAN_FULL.md')
    sums_blob = blob_at(commit, 'Plans/SHA256SUMS.txt')
    evidence = f'''# TSK-0052 / LG-06 CR-0007 auto-authority reconciliation evidence\n\n**Date:** 2026-09-01  \n**Owner authority:** explicit Project Owner instruction `APPROVE TSK-0052 LG-06 CR-0007 AUTO-AUTHORITY RECONCILIATION`, followed by `continue autonomously`.  \n**Scope:** canonical repair of stale TSK-0052 action metadata only; no acceptance, dependency, scope, gate-outcome, or task-state change.\n\n## Reconciliation\n\n- Before: `A1 / HUMAN_ONLY`.\n- After: `A4 / AUTO_ALLOWED`.\n- Basis: DEC-0054 / CR-0007 makes LG-06 objective gate acceptance automatic inside frozen scope; the exact CR-0007 WBS authority transition for formerly human-only product/design work is `A1/HUMAN_ONLY -> A4/AUTO_ALLOWED`.\n- TSK-0052 dependencies remain exactly `{EXPECTED_DEPS}`.\n- ACC/VER/EVD remain `ACC-0052 / VER-0052 / EVD-0052`.\n- `Plan_Status=PLANNED` and WBS snapshot `Execution_State=WAITING` remain unchanged.\n- This authority repair does **not** make TSK-0052 or LG-06 PASS.\n\n## Durable verification\n\n- Planning repair commit: `{commit}`.\n- GitHub Actions run: `{run_id}` on self-hosted `adguardvm`.\n- Full deterministic master-plan validator: PASS before publication.\n- WBS semantic diff assertion: only `AI_Capability_A0_A4` and `Action_Authority` on TSK-0052 changed.\n- WBS blob: `{wbs_blob}`.\n- Autonomy projection blob: `{auto_blob}`.\n- Generated master-plan blob: `{gen_blob}`.\n- Plans checksum index blob: `{sums_blob}`.\n\nA fresh current-evidence LG-06 acceptance review is required after this read-back before any PASS is assigned.\n'''
    if EVIDENCE.exists():
        raise SystemExit('reconciliation evidence already exists')
    EVIDENCE.write_text(evidence, encoding='utf-8')
    runtime = RUNTIME.read_text(encoding='utf-8')
    heading = '## TSK-0052 / LG-06 CR-0007 auto-authority reconciliation — 2026-09-01'
    if heading in runtime:
        raise SystemExit('runtime reconciliation section already exists')
    section = f'''\n\n{heading}\n\n- Project Owner explicitly approved `APPROVE TSK-0052 LG-06 CR-0007 AUTO-AUTHORITY RECONCILIATION` and instructed autonomous continuation.\n- The stale WBS metadata was reconciled from `A1 / HUMAN_ONLY` to **`A4 / AUTO_ALLOWED`**, matching DEC-0054 / CR-0007 objective LG-06 authority semantics.\n- Planning repair commit: `{commit}`; GitHub Actions run `{run_id}`.\n- Current repaired WBS blob: `{wbs_blob}`.\n- Dependencies, ACC-0052 contract, Plan_Status and WBS execution snapshot were not changed by this repair.\n- **No PASS is inferred from the authority repair.** TSK-0052 / LG-06 remains non-PASS until a fresh current-evidence ACC-0052 review is durably verified and reconciled.\n- Evidence: `TSK_0052_LG06_CR0007_AUTO_AUTHORITY_RECONCILIATION_EVIDENCE_2026-09-01.md`.\n'''
    RUNTIME.write_text(runtime.rstrip() + section + '\n', encoding='utf-8')
    print(f'RECORDED_WBS_BLOB={wbs_blob}')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode == 'apply':
        apply()
    elif mode == 'record':
        record()
    else:
        raise SystemExit('usage: reconcile_tsk0052_lg06_cr0007_authority_20260901.py apply|record')
