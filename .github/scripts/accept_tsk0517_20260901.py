#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import subprocess
from pathlib import Path

ARTIFACT = Path('TSK_0517_CROSS_BROWSER_DEVICE_NETWORK_ACCEPTANCE_TEST_PLAN_2026-09-01.md')
STATE = Path('CURRENT_STATE.md')
WBS = Path('Plans/Master/WBS/master-wbs.csv')
EXPECTED_ARTIFACT_BLOB = 'a3da0c1c6fe6d5ae12dfaf37e7f9606202848df5'
EXPECTED_WBS_BLOB = 'b27a0c5df2f5636d8ed71051e9e26a68959a2616'
EXPECTED_LAYER5_BLOB = '2097d83961affaa69850e41a5ffcd72a660d69cd'
ARTIFACT_PUBLICATION_COMMIT = '8b1305f3bd31e9e7955ab97e77c3ab17f643ec30'


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
    row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0517')
    assert (row.get('Lifecycle_Stage') or '').strip() == 'L5'
    assert (row.get('Priority') or '').strip() == 'HIGH'
    assert (row.get('AI_Capability_A0_A4') or '').strip() == 'A3'
    assert (row.get('Action_Authority') or '').strip() == 'AUTO_ALLOWED'
    assert {x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()} == {'TSK-0354','TSK-0409'}
    assert (row.get('Acceptance_ID') or '').strip() == 'ACC-0517'
    assert (row.get('Verification_ID') or '').strip() == 'VER-0517'
    assert (row.get('Evidence_ID') or '').strip() == 'EVD-0517'
    assert (row.get('Risk_Reference') or '').strip() == 'RSK-0050'
    assert (row.get('Interface_Reference') or '').strip() == 'INT-0017'
    assert {x.strip() for x in (row.get('Requirement_Reference') or '').split(';') if x.strip()} == {'REQ-0065','REQ-0066','CON-0023','CON-0029'}
    assert (row.get('Acceptance_Criteria') or '').strip() == (
        'Test coverage maps every critical requirement and state transition; fixtures contain no real child browsing data; exact environments/versions are specified.'
    )

    state = STATE.read_text(encoding='utf-8')
    assert 'ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0008 PUBLISHED, RECONCILED, READ-BACK VERIFIED.' in state
    assert '## TSK-0354 current accepted stable state' in state
    assert '## TSK-0409 current accepted stable state — 2026-09-01 — POST-CR-0008' in state
    heading = '## TSK-0517 current accepted stable state — 2026-09-01 — POST-CR-0008'
    assert heading not in state

    artifact = ARTIFACT.read_text(encoding='utf-8')
    for marker in (
        '**Version:** 1.0.0', 'REQ-0065; REQ-0066; CON-0023; CON-0029; RSK-0050; INT-0017',
        'no downstream test execution, target-runtime PASS, build, release or production outcome is inferred',
        'iOS `26.6.1`', 'iPadOS `26.6.1`', 'Safari `26.6.1`', 'Firefox `155`',
        '153.0.8010.24', 'Android `16` stable platform', 'ubuntu-24.04', '20260823.283.1',
        'No real child browsing data', 'exact replacement version', 'no floating `latest` label is accepted as evidence',
        'CON-0023', 'CON-0029', 'INT-0017', 'RSK-0050',
        'PASS candidate pending deterministic verification',
    ):
        assert marker in artifact, marker

    suites = {'TS-GOV','TS-NOAUTH','TS-ACCOUNT','TS-DNS','TS-STATE','TS-UX','TS-A11Y','TS-PRIV','TS-SEC','TS-PERF','TS-FAIL','TS-REC','TS-OPS'}
    found_suites = set(re.findall(r'\| (TS-[A-Z0-9]+) \|', artifact))
    assert suites <= found_suites, suites - found_suites

    for marker in ('functional', 'browser/device/network', 'UX', 'accessibility', 'security/privacy', 'performance', 'failure/recovery', 'rollback', 'environment-specific'):
        assert marker.lower() in artifact.lower(), marker

    dns_section = artifact.split('## 6. TSK-0409 device/network coverage — all 14 matrix cases',1)[1].split('## 7. TSK-0320 state and transition coverage',1)[0]
    dns_rows = [line for line in dns_section.splitlines() if line.startswith('| ')][1:]
    assert len(dns_rows) == 14, len(dns_rows)
    for required_case in ('Chrome custom', 'app-specific DoH/DoT', 'VPN/DNS-changing', 'Private Relay', 'Firefox own', 'Captive portal', 'Wi-Fi/cellular', 'Unsupported OS/version', 'Intentional removal'):
        assert required_case.lower() in dns_section.lower(), required_case

    states = ('protected_verified','configured_parent_confirmed','action_needed','not_covered','uncertain_error','removed')
    for s in states:
        assert f'`{s}`' in artifact, s
    for i in range(1,13):
        assert f'ST-{i:02d}' in artifact
    for marker in ('cannot masquerade as technical verification', 'parent/configuration confirmation', 'account/device deletion or parent report alone cannot prove DNS removal'):
        assert marker.lower() in artifact.lower(), marker

    for marker in ('NA-01','NA-06','AC-01','AC-07','mandatory login','cross-parent','IDOR','AdGuard','Quad9/upstream failure','session revoked mid-operation','post-recovery verification'):
        assert marker.lower() in artifact.lower(), marker

    for marker in ('`REQ-0001`–`REQ-0006`','`REQ-0007`–`REQ-0012`','`REQ-0013`–`REQ-0017`','`REQ-0042` onward','`REQ-0060`–`REQ-0064`','`REQ-0065`–`REQ-0066`','Zero missing applicable requirements is required'):
        assert marker in artifact, marker

    for marker in ('DNS question/domain/URL history', 'messages, contacts, photos, location', 'reserved documentation names such as `example.com`'):
        assert marker in artifact, marker
    for pattern in (r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', r'ghp_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}', r'AKIA[0-9A-Z]{16}'):
        assert not re.search(pattern, artifact)
    print('TSK0517_LITERAL_SECRET_GUARD=PASS')

    controls = {
        'Plans/Master/Registers/REQUIREMENTS.md': ('REQ-0065','REQ-0066'),
        'Plans/Master/Registers/CONSTRAINTS.md': ('CON-0023','CON-0029'),
        'Plans/Master/Registers/RISKS.md': ('RSK-0050',),
        'Plans/Master/Registers/INTERFACES.md': ('INT-0017',),
    }
    for path, markers in controls.items():
        text = Path(path).read_text(encoding='utf-8')
        for marker in markers:
            assert marker in text, (path, marker)

    validation = subprocess.run(['python3','Plans/Master/Tools/validate_master_plan.py'], text=True, capture_output=True, check=True)
    print(validation.stdout, end='')
    combined = validation.stdout + validation.stderr
    for marker in ('VALIDATION PASS','assembly_modules=25','tasks=641','dependency_edges=858','relationship_entities=5178','relationship_targets=20472','broken_links=0','generated_missing_task_ids=0'):
        assert marker in combined, marker

    section = f'''{heading}

`TSK-0517 — Define cross-browser/device/network functional, failure, privacy, accessibility, performance, recovery/removal, and no-auth tests`: **PASS** under current `ACC-0517 / VER-0517 / EVD-0517`, current `TSK-0354` + `TSK-0409` dependency proof, and CR-0008 authority.

- Action authority: **A3 / AUTO_ALLOWED**.
- Artifact: `TSK_0517_CROSS_BROWSER_DEVICE_NETWORK_ACCEPTANCE_TEST_PLAN_2026-09-01.md`, version `1.0.0`, blob `{EXPECTED_ARTIFACT_BLOB}`, publication commit `{ARTIFACT_PUBLICATION_COMMIT}`.
- Verification source commit: `{source_commit}`; GitHub Actions run/attempt `{run_id} / {run_attempt}`.
- Acceptance proof: exact WBS/ACC/VER/EVD/dependencies/authority; REQ-0065/0066; CON-0023/0029; RSK-0050; INT-0017; all integrated test classes; all 14 TSK-0409 cases; all six TSK-0320 states and ST-01..ST-12; accountless/no-auth and optional-account negative boundaries; exact dated environment/version references; privacy-safe synthetic-fixture rule; secret guard; and full modular validator all passed before runtime mutation.
- Dated reference environments include iOS/iPadOS 26.6.1, Safari 26.6.1, Firefox 155, Chromium/Chrome 153.0.8010.24 reference, Android 16 stable and ubuntu-24.04 CI; actual execution must record exact installed full versions and may not use floating `latest` as evidence.
- Non-production/synthetic results remain non-production evidence and cannot be relabelled as production/live-user evidence.
- Runtime acceptance does not alter WBS, graph, manifest, planning modules or the CR-0008 owner-frozen baseline.
- **Non-inference:** this PASS freezes the acceptance-test definition only; it does not claim those downstream browser/device/network/runtime tests executed, any release passed, production was activated, or real-user outcomes exist.'''
    STATE.write_text(state.rstrip() + '\n\n' + section.strip() + '\n', encoding='utf-8')
    print('ACC_0517=PASS')
    print('VER_0517=PASS')
    print('EVD_0517=PASS')
    print('TSK0517_STATE_CANDIDATE=PASS')

if __name__ == '__main__':
    main()
