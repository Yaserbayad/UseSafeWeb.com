#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
from pathlib import Path

ARTIFACT = Path('TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md')
STATE = Path('CURRENT_STATE.md')
WBS = Path('Plans/Master/WBS/master-wbs.csv')
EXPECTED_EVENTS = [
    'journey_started',
    'journey_step_entered',
    'journey_step_outcome',
    'journey_completed',
    'protection_state_evaluated',
    'protection_verification_outcome',
    'self_service_opened',
    'self_service_outcome',
    'synthetic_service_probe_result',
    'recovery_operation_outcome',
    'channel_entry',
    'cost_period_recorded',
]


def git_hash(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def prepare() -> None:
    s = ARTIFACT.read_text(encoding='utf-8')
    assert '**Version:** 1.0.0' in s
    assert 'Only the eleven event names in this contract are accepted.' in s
    names = re.findall(r'^#### `([a-z0-9_]+)`$', s, flags=re.M)
    assert names == EXPECTED_EVENTS, names
    s, n = re.subn(r'^\*\*Version:\*\* 1\.0\.0[ \t]*$', '**Version:** 1.0.1', s, count=1, flags=re.M)
    assert n == 1
    s = s.replace(
        'Only the eleven event names in this contract are accepted.',
        'Only the twelve event names in this contract are accepted.',
        1,
    )
    ARTIFACT.write_text(s, encoding='utf-8')
    print('TSK0498_PREACCEPT_CORRECTION=PASS')
    print('TSK0498_APPROVED_EVENT_COUNT=12')


def verify_and_stage_state() -> None:
    artifact_commit = os.environ['TSK0498_ARTIFACT_COMMIT']
    artifact_blob = os.environ['TSK0498_ARTIFACT_BLOB']
    run_id = os.environ.get('GITHUB_RUN_ID', 'UNKNOWN')
    run_attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '1')

    artifact = ARTIFACT.read_text(encoding='utf-8')
    state = STATE.read_text(encoding='utf-8')
    assert git_hash(str(ARTIFACT)) == artifact_blob
    assert git_hash(str(WBS)) == 'b27a0c5df2f5636d8ed71051e9e26a68959a2616'
    assert git_hash('Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md') == '2097d83961affaa69850e41a5ffcd72a660d69cd'

    with WBS.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0498')
    assert (row.get('Lifecycle_Stage') or '').strip() == 'L5'
    assert {x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()} == {'TSK-0229', 'TSK-0320'}
    assert (row.get('Priority') or '').strip() == 'HIGH'
    assert (row.get('AI_Capability_A0_A4') or '').strip() == 'A3'
    assert (row.get('Action_Authority') or '').strip() == 'AUTO_ALLOWED'
    assert (row.get('Acceptance_ID') or '').strip() == 'ACC-0498'
    assert (row.get('Verification_ID') or '').strip() == 'VER-0498'
    assert (row.get('Evidence_ID') or '').strip() == 'EVD-0498'
    assert (row.get('Risk_Reference') or '').strip() == 'RSK-0049'
    assert (row.get('Interface_Reference') or '').strip() == 'INT-0016'
    assert {x.strip() for x in (row.get('Requirement_Reference') or '').split(';') if x.strip()} == {
        'REQ-0060', 'REQ-0061', 'REQ-0062', 'CON-0007', 'CON-0008', 'CON-0009'
    }
    assert (row.get('Acceptance_Criteria') or '').strip() == (
        'Every event has purpose/fields/retention/owner/denominator; no domains, browsing, child activity, '
        'addictive engagement, or persistent identity linkage exists.'
    )

    assert 'ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0008 PUBLISHED, RECONCILED, READ-BACK VERIFIED.' in state
    assert '## TSK-0229 current accepted stable state' in state
    assert '## TSK-0320 current accepted stable state — 2026-09-01 — POST-CR-0008' in state
    heading = '## TSK-0498 current accepted stable state — 2026-09-01 — POST-CR-0008'
    assert heading not in state

    assert '**Version:** 1.0.1' in artifact
    assert re.findall(r'^#### `([a-z0-9_]+)`$', artifact, flags=re.M) == EXPECTED_EVENTS
    assert 'Only the twelve event names in this contract are accepted.' in artifact
    for i, name in enumerate(EXPECTED_EVENTS):
        start = artifact.index(f'#### `{name}`')
        end = artifact.index(f'#### `{EXPECTED_EVENTS[i + 1]}`') if i + 1 < len(EXPECTED_EVENTS) else artifact.index('## 6. Explicitly prohibited events and fields')
        section = artifact[start:end]
        for marker in ('- **Purpose:**', '- **Event fields:**', '- **Retention:**', '- **Owner:**', '- **Denominator:**'):
            assert marker in section, (name, marker)

    required_artifact_markers = (
        '**Persistent identity linkage is prohibited.**',
        'No analytics identifier survives the accountless journey TTL.',
        'maximum life and raw retention **24 hours**',
        'Sign-in cannot extend this lifetime.',
        'Unknown fields cause rejection/quarantine and privacy review, not silent storage.',
        '`configured_parent_confirmed` is never counted as `protected_verified`.',
        'Parent/configuration confirmation does not create this event and cannot be represented as a positive result.',
        'No browsing/query/activity history',
        'Missing data and uncertainty are shown beside the metric; they are never silently imputed as success.',
        'Operational logs/traces are governed separately and must not be treated as a backdoor analytics store.',
    )
    for marker in required_artifact_markers:
        assert marker in artifact, marker
    assert not ({'dns_query', 'domain_visited', 'top_domain', 'child_activity'} & set(EXPECTED_EVENTS))

    control_checks = (
        ('REQ-0060', 'Plans/Master/Registers/REQUIREMENTS.md'),
        ('REQ-0061', 'Plans/Master/Registers/REQUIREMENTS.md'),
        ('REQ-0062', 'Plans/Master/Registers/REQUIREMENTS.md'),
        ('CON-0007', 'Plans/Master/Registers/CONSTRAINTS.md'),
        ('CON-0008', 'Plans/Master/Registers/CONSTRAINTS.md'),
        ('CON-0009', 'Plans/Master/Registers/CONSTRAINTS.md'),
        ('RSK-0049', 'Plans/Master/Registers/RISKS.md'),
        ('INT-0016', 'Plans/Master/Registers/INTERFACES.md'),
    )
    for marker, path in control_checks:
        assert marker in Path(path).read_text(encoding='utf-8')

    for pattern in (
        r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        r'ghp_[A-Za-z0-9]{30,}',
        r'github_pat_[A-Za-z0-9_]{40,}',
        r'AKIA[0-9A-Z]{16}',
    ):
        assert not re.search(pattern, artifact)
    print('TSK0498_LITERAL_SECRET_GUARD=PASS')

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

`TSK-0498 — Define only decision-linked accountless journey, protection-state, self-service, reliability, channel, and cost events`: **PASS** under current `ACC-0498 / VER-0498 / EVD-0498`, current `TSK-0229` + `TSK-0320` dependency proof, and `DEC-0055/CR-0008` authority.

- Action authority: **A3 / AUTO_ALLOWED**.
- Artifact: `TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md`, version `1.0.1`, blob `{artifact_blob}`, acceptance source commit `{artifact_commit}`.
- Verification: GitHub Actions run/attempt `{run_id} / {run_attempt}` checked exact WBS/ACC/VER/EVD/dependencies/authority; REQ-0060/0061/0062; CON-0007/0008/0009; RSK-0049; INT-0016; exact 12-event allowlist; per-event purpose/fields/retention/owner/denominator; privacy/truth-state boundaries; literal-secret guard; and full modular master-plan validator.
- Approved data is decision-linked only. Accountless correlation is random, first-party, session-only and maximum 24 hours; sign-in cannot extend/link it. Retained product aggregates are non-linkable; synthetic reliability data is user-independent.
- No DNS question/domain/URL/browsing/top-domain/child activity/free-text support/persistent account-device analytics identifier/addictive-engagement event is approved. Unknown events/fields fail schema acceptance.
- `configured/parent-confirmed` remains distinct from technical `protected/verified`; parent/configuration confirmation cannot produce a positive technical verification event.
- Every consuming KPI must state source/formula/numerator/denominator/window/release-or-cohort/owner/guardrail/decision action; missing data and reproduction failure remain explicit.
- A pre-PASS catalogue-count defect (`eleven` vs actual 12) and the first acceptance workflow's trailing-whitespace failure were corrected before acceptance; neither produced runtime PASS.
- Runtime acceptance does not alter the WBS, graph, manifest, planning modules or CR-0008 owner-frozen baseline.
- **Non-inference:** no analytics vendor/implementation/runtime collection, legal/DPIA conclusion, KPI result, downstream gate, build, production activation, launch or real-user outcome becomes PASS from this definition task.'''
    STATE.write_text(state.rstrip() + '\n\n' + section + '\n', encoding='utf-8')
    print('ACC_0498=PASS')
    print('VER_0498=PASS')
    print('EVD_0498=PASS')
    print('TSK0498_STATE_CANDIDATE=PASS')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in {'prepare', 'verify-state'}:
        raise SystemExit('usage: accept_tsk0498_20260901.py prepare|verify-state')
    if sys.argv[1] == 'prepare':
        prepare()
    else:
        verify_and_stage_state()
