#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import subprocess
from pathlib import Path

ARTIFACT = Path('TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md')
STATE = Path('CURRENT_STATE.md')
WBS = Path('Plans/Master/WBS/master-wbs.csv')

EXPECTED_ARTIFACT_BLOB = '3aa832777276115912e4f3990b30cb541c458f4f'
EXPECTED_WBS_BLOB = 'b27a0c5df2f5636d8ed71051e9e26a68959a2616'
EXPECTED_LAYER5_BLOB = '2097d83961affaa69850e41a5ffcd72a660d69cd'
ARTIFACT_PUBLICATION_COMMIT = 'bcccf7599dddd6e1665ba1207cafcadd6afe164d'


def git_hash(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def main() -> None:
    source_commit = os.environ['SOURCE_COMMIT']
    run_id = os.environ.get('GITHUB_RUN_ID', 'UNKNOWN')
    run_attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '1')

    assert git_hash(str(ARTIFACT)) == EXPECTED_ARTIFACT_BLOB
    assert git_hash(str(WBS)) == EXPECTED_WBS_BLOB
    assert git_hash('Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md') == EXPECTED_LAYER5_BLOB

    with WBS.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0409')
    assert (row.get('Lifecycle_Stage') or '').strip() == 'L4'
    assert (row.get('Priority') or '').strip() == 'HIGH'
    assert (row.get('AI_Capability_A0_A4') or '').strip() == 'A3'
    assert (row.get('Action_Authority') or '').strip() == 'AUTO_ALLOWED'
    assert [x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()] == ['TSK-0408']
    assert (row.get('Acceptance_ID') or '').strip() == 'ACC-0409'
    assert (row.get('Verification_ID') or '').strip() == 'VER-0409'
    assert (row.get('Evidence_ID') or '').strip() == 'EVD-0409'
    assert (row.get('Risk_Reference') or '').strip() == 'RSK-0004'
    assert (row.get('Interface_Reference') or '').strip() == 'INT-0013'
    reqs = {x.strip() for x in (row.get('Requirement_Reference') or '').split(';') if x.strip()}
    assert reqs == {'REQ-0042', 'REQ-0043', 'CON-0002', 'CON-0003'}
    assert (row.get('Acceptance_Criteria') or '').strip() == (
        'Every supported combination has a tested mechanism or explicit unsupported status; '
        'Private Relay/VPN/app/browser/network bypass limits are covered.'
    )

    state = STATE.read_text(encoding='utf-8')
    assert 'ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0008 PUBLISHED, RECONCILED, READ-BACK VERIFIED.' in state
    assert '## TSK-0408 current accepted stable state — 2026-09-01 — POST-CR-0007' in state
    assert '## TSK-0320 current accepted stable state — 2026-09-01 — POST-CR-0008' in state
    heading = '## TSK-0409 current accepted stable state — 2026-09-01 — POST-CR-0008'
    assert heading not in state

    artifact = ARTIFACT.read_text(encoding='utf-8')
    required = (
        '**Version:** 1.0.0',
        '**Configuration evidence is never technical protection evidence.**',
        '`protected_verified` requires current technical evidence',
        '`protected_verified`, `configured_parent_confirmed`, `action_needed`, `not_covered`, `uncertain_error`, `removed`',
        'Android **Private DNS provider hostname** using `dns.usesafeweb.com`',
        'TSK-0408 Apple DoH profile/Server-URL mechanism',
        'iCloud Private Relay / Limit IP Address Tracking',
        'Chrome custom Secure DNS provider',
        'Firefox with its own DoH provider',
        'VPN or DNS-changing security/privacy app',
        'app-specific DoH/DoT/custom resolver',
        'captive portal / sign-in network',
        'Wi-Fi <-> cellular switch',
        'Unsupported OS/version',
        'User intentionally removes the approved UseSafeWeb DNS mechanism',
        'https://dns10.quad9.net/dns-query` with ECS disabled',
        'do **not** prove the future UseSafeWeb implementation or any physical device/runtime test result',
        'PASS candidate pending independent deterministic verification',
    )
    for marker in required:
        assert marker in artifact, marker

    matrix = artifact.split('## 3. Frozen support and bypass matrix', 1)[1].split('## 4. Deterministic state-transition rules', 1)[0]
    table_rows = [line for line in matrix.splitlines() if line.startswith('| ')]
    assert table_rows and table_rows[0].startswith('| Combination / condition |')
    data_rows = table_rows[1:]
    assert len(data_rows) == 14, len(data_rows)
    allowed_statuses = {'SUPPORTED-L4', 'CONDITIONAL', 'NOT-COVERED', 'NOT-COVERED or UNCERTAIN/ERROR', 'SUPPORTED removal path'}
    for line in data_rows:
        cells = [c.strip() for c in line.strip('|').split('|')]
        assert len(cells) == 6, cells
        status = cells[1]
        assert status in allowed_statuses, status
        assert cells[2] and cells[3] and cells[4] and cells[5]
        if status in {'SUPPORTED-L4', 'CONDITIONAL'}:
            assert any(term in cells[3].lower() for term in ('verification', 'verify', 'reverify')), cells
        assert any(state_name in cells[5] for state_name in (
            'protected_verified', 'configured_parent_confirmed', 'action_needed',
            'not_covered', 'uncertain_error', 'removed', 'recompute state', 'inherit applicable verified state'
        )), cells

    negative_markers = (
        'none may produce `protected_verified`',
        'Profile/configuration presence is not verification.',
        'Configuration presence is setup evidence only.',
        'do not infer from the Android setting',
        'no protected claim is allowed',
        'Unknown is not success.',
        'configuration disappearance alone does not prove',
    )
    for marker in negative_markers:
        assert marker in artifact, marker

    source_markers = (
        'support.google.com/android/answer/9654714',
        'support.google.com/chrome/answer/10468685',
        'support.google.com/android/answer/16927813',
        'support.mozilla.org/en-US/kb/firefox-dns-over-https',
        'support.mozilla.org/en-US/kb/how-will-dns-work-when-using-vpn-extension',
        'support.mozilla.org/en-US/kb/configuring-networks-disable-dns-over-https',
        'support.apple.com/en-gb/102022',
    )
    for marker in source_markers:
        assert marker in artifact, marker

    for marker in ('DNS questions', 'domains', 'URLs', 'browsing history', 'child activity', 'persistent identity linkage'):
        assert marker in artifact
    for pattern in (
        r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        r'ghp_[A-Za-z0-9]{30,}',
        r'github_pat_[A-Za-z0-9_]{40,}',
        r'AKIA[0-9A-Z]{16}',
    ):
        assert not re.search(pattern, artifact)
    print('TSK0409_LITERAL_SECRET_GUARD=PASS')

    controls = {
        'Plans/Master/Registers/REQUIREMENTS.md': ('REQ-0042', 'REQ-0043'),
        'Plans/Master/Registers/CONSTRAINTS.md': ('CON-0002', 'CON-0003'),
        'Plans/Master/Registers/RISKS.md': ('RSK-0004',),
        'Plans/Master/Registers/INTERFACES.md': ('INT-0013',),
    }
    for path, markers in controls.items():
        text = Path(path).read_text(encoding='utf-8')
        for marker in markers:
            assert marker in text, (path, marker)

    validation = subprocess.run(
        ['python3', 'Plans/Master/Tools/validate_master_plan.py'],
        text=True,
        capture_output=True,
        check=True,
    )
    print(validation.stdout, end='')
    combined = validation.stdout + validation.stderr
    for marker in (
        'VALIDATION PASS', 'assembly_modules=25', 'tasks=641', 'dependency_edges=858',
        'relationship_entities=5178', 'relationship_targets=20472', 'broken_links=0',
        'generated_missing_task_ids=0',
    ):
        assert marker in combined, marker

    section = f'''{heading}

`TSK-0409 — Freeze supported-device/network verification coverage and explicit unsupported/bypass behavior`: **PASS** under current `ACC-0409 / VER-0409 / EVD-0409`, current `TSK-0408` dependency proof, and CR-0008 authority.

- Action authority: **A3 / AUTO_ALLOWED**.
- Artifact: `TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md`, version `1.0.0`, blob `{EXPECTED_ARTIFACT_BLOB}`, publication commit `{ARTIFACT_PUBLICATION_COMMIT}`.
- Verification source commit: `{source_commit}`; GitHub Actions run/attempt `{run_id} / {run_attempt}`.
- Acceptance proof: exact WBS metadata/dependency/ACC/VER/EVD, REQ-0042/0043, CON-0002/0003, RSK-0004, INT-0013, current TSK-0408 + TSK-0320 state, matrix completeness, bypass/conflict coverage, truth-state negative assertions, privacy/secret guard, current official-source markers and the full modular-plan validator all passed before runtime mutation.
- Frozen L4 support mechanisms remain Android Private DNS/DoT hostname and Apple DoH profile/Server-URL from TSK-0408. Chrome/Firefox custom DNS, VPN/app resolvers, Private Relay, captive portals, network changes and unknown combinations are handled conservatively with mandatory reverification or explicit `not_covered` / `uncertain_error` semantics.
- Configuration/profile/account/ClientID/parent-confirmation evidence never becomes `protected_verified`; only fresh qualifying technical evidence for the effective DNS path may do so.
- No DNS questions/domains/URLs/browsing history/child activity/persistent identity linkage is required by this contract.
- Runtime acceptance does not alter WBS, graph, manifest, planning modules, AdGuard, Quad9 dns10/ECS policy or the CR-0008 owner-frozen baseline.
- **Non-inference:** this L4 PASS does not claim physical-device/runtime acceptance, implementation, LG-07, build, production activation, launch or real-user outcomes.'''
    STATE.write_text(state.rstrip() + '\n\n' + section.strip() + '\n', encoding='utf-8')
    print('ACC_0409=PASS')
    print('VER_0409=PASS')
    print('EVD_0409=PASS')
    print('TSK0409_STATE_CANDIDATE=PASS')


if __name__ == '__main__':
    main()
