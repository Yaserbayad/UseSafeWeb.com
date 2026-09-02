#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
MATRIX = ROOT / 'TSK_0239_SECURITY_PRIVACY_CONTROL_IMPLEMENTATION_VERIFICATION_MATRIX_2026-09-02.md'
STATE = ROOT / 'CURRENT_STATE.md'
MANIFEST = ROOT / 'Plans/Master/MANIFEST.yaml'
LAYER5 = ROOT / 'Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md'
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'

EXPECTED_BLOBS = {
    'TSK_0485_END_TO_END_THREAT_ABUSE_MODEL_2026-09-01.md': '373ac62ba1f244328e7d8e52ae6648d72e5a5ed7',
    'TSK_0356_POST_CR0008_FIREBASE_AUTH_SERVER_SESSION_ARCHITECTURE_2026-09-02.md': '7dd47124db837ea4eaf6a06661788423d22f3c6e',
    'TSK_0232_POST_CR0008_PARENT_DEVICE_OWNERSHIP_AUTHORIZATION_MODEL_2026-09-02.md': '30de2625f977e4d8017630c15de74ea19fde195c',
    'TSK_0410_POST_CR0008_ALLOWLISTED_ADGUARD_ADAPTER_CLIENTID_LIFECYCLE_2026-09-02.md': 'a0f98fbd69c49a5082c7853afc2487439b753c91',
    'TSK_0234_POST_CR0008_PARTIAL_FAILURE_DELETION_MIGRATION_STATE_MACHINE_2026-09-02.md': '361ecdfa733a8a27f82616725e6d9b348ad57c1f',
    'TSK_0486_AI_EXECUTED_OPERATIONS_SECURITY_CONTROL_2026-09-01.md': 'ef2df08094f1e80ee592abcada145deaa8b600db',
    'TSK_0487_ANONYMOUS_JOURNEY_THREAT_MODEL_2026-09-01.md': 'daa96693e96bbcc749681b1f0264858d90b51244',
    'TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md': '6b7a5095122c74ed9ec860b74408dab474576659',
    'TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md': '3aa832777276115912e4f3990b30cb541c458f4f',
    'TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md': 'bdc6bacc424669708f410466f3cfd5527f1c2b3c',
    'infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md': '18d998e2406e801c7ac08f4daa2e3b763ea9b523',
    'TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_2026-09-01.md': '9915f59e356c0d06a0c54ce0c9d4bb63f7e0b553',
}
EXPECTED_MATRIX_BLOB = '674c21b4c169da4fb496617164ad68cfc6527fb4'
ARTIFACT_COMMIT = 'f1386b0af35b4f5b60134fcf2a9aefe13f466306'


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def verify() -> str:
    assert MATRIX.is_file(), MATRIX
    manifest = MANIFEST.read_text(encoding='utf-8')
    layer5 = LAYER5.read_text(encoding='utf-8')
    state = STATE.read_text(encoding='utf-8')

    assert 'latest_change: CR-0009' in manifest
    assert '### 5.3.8 Owner-external legal/compliance scope (DEC-0056 / CR-0009)' in layer5
    assert 'Legal-scope items are **OWNER_EXTERNAL_SATISFIED**' in layer5
    assert '## TSK-0485 current accepted stable state — 2026-09-01 — POST-CR-0008' in state
    assert '`TSK-0485 — Perform end-to-end threat and abuse modeling`: **PASS**' in state
    assert '## TSK-0239 current accepted stable state — 2026-09-02 — POST-CR-0009' not in state

    with WBS.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0239')
    assert (row.get('Action_Authority') or '').strip() == 'AUTO_ALLOWED'
    assert (row.get('AI_Capability_A0_A4') or '').strip() == 'A3'
    values = [(v or '').strip() for v in row.values()]
    assert 'L5' in values
    assert 'TSK-0485; TSK-0240' in values
    assert 'ACC-0239' in values and 'VER-0239' in values and 'EVD-0239' in values
    assert any('Create security/privacy control implementation and verification matrix' in v for v in values)

    for rel, expected in EXPECTED_BLOBS.items():
        p = ROOT / rel
        assert p.is_file(), rel
        actual = git_blob_sha(p)
        assert actual == expected, f'{rel}: {actual} != {expected}'
    assert (ROOT / 'infrastructure/adguard-server/tsk-0413-bundle-v1').is_dir()

    matrix_blob = git_blob_sha(MATRIX)
    assert matrix_blob == EXPECTED_MATRIX_BLOB, matrix_blob
    text = MATRIX.read_text(encoding='utf-8')
    rows = [ln for ln in text.splitlines() if re.match(r'^\| \*\*TM-\d{2} ', ln)]
    assert len(rows) == 30, len(rows)
    ids = []
    for line in rows:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        assert len(cells) == 9, (len(cells), line)
        match = re.match(r'\*\*(TM-\d{2}) (Critical|High)', cells[0])
        assert match, cells[0]
        ids.append(match.group(1))
        assert all(cells)
        assert cells[-1] in {
            'DESIGN_BOUND / IMPLEMENTATION_PENDING',
            'CONFIG_BASELINE_BOUND / RUNTIME_REVERIFY',
        }
        assert 'LG-08' in cells[5] or 'LG-09' in cells[5]
    assert ids == [f'TM-{i:02d}' for i in range(1, 31)], ids

    required = [
        'Implementation owner',
        'Current artifact/config authority',
        'L6 implementation target',
        'Verification method / evidence path',
        'Release gate',
        'Monitoring / detection',
        'Failure response',
        'Current status',
        'TSK-0240 is `OWNER_EXTERNAL_SATISFIED`',
        'is **not** represented here as legal PASS',
        'TSK-0048 must assign each row',
        'TSK-0539 must bind every actionable SLI/threat signal',
        'does not itself implement a control, close a vulnerability',
        'ClientID never substitute for ownership authorization',
        'only fresh qualifying technical evidence may produce `protected_verified`',
        'persistent identifiable query/file logging and identifiable per-client statistics remain OFF/excluded',
        'no production secret/token/private key in Git',
        'ambiguous non-idempotent effects stop progression until reconciliation',
    ]
    for token in required:
        assert token in text, token

    subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
    subprocess.run(['python3', 'Plans/Master/Tools/validate_master_plan.py'], cwd=ROOT, check=True)
    return matrix_blob


def record_state(matrix_blob: str) -> None:
    run_id = os.environ.get('GITHUB_RUN_ID', '').strip()
    run_attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '').strip()
    source_sha = os.environ.get('GITHUB_SHA', '').strip()
    assert run_id and run_attempt and source_sha, 'GitHub Actions run metadata required for state acceptance'

    text = STATE.read_text(encoding='utf-8')
    marker = '## CR-0007 current authority and execution boundary\n'
    assert marker in text
    section = f'''## TSK-0239 current accepted stable state — 2026-09-02 — POST-CR-0009\n\n`TSK-0239 — Create security/privacy control implementation and verification matrix`: **PASS** under current `ACC-0239 / VER-0239 / EVD-0239`, current `TSK-0485` PASS, and DEC-0056/CR-0009 owner-external treatment of the legal-only TSK-0240 predecessor.\n\n- Current WBS: L5 / MEDIUM / A3 / `AUTO_ALLOWED`; hard dependencies `TSK-0485; TSK-0240`. TSK-0485 is current durable PASS; TSK-0240 remains DEFERRED/WAITING and is `OWNER_EXTERNAL_SATISFIED` for sequencing only — no legal PASS/evidence is claimed.\n- Accepted matrix: `TSK_0239_SECURITY_PRIVACY_CONTROL_IMPLEMENTATION_VERIFICATION_MATRIX_2026-09-02.md`, version `1.0.0`, blob `{matrix_blob}`, publication commit `{ARTIFACT_COMMIT}`.\n- Independent GitHub Actions verification run/attempt `{run_id} / {run_attempt}`, source commit `{source_sha}`, verified exact upstream artifact blobs, current WBS contract, CR-0009 semantics, all 30 TM-01..TM-30 rows exactly once, required owner/location/verification/gate/monitoring/failure/status cells, global security/privacy invariants, `git diff --check`, and full modular master-plan validator PASS before this runtime mutation.\n- Every High/Critical control remains mapped to downstream L6 implementation and LG-08/LG-09 verification; this L5 matrix does not self-certify deployed controls. TSK-0048 must assign exact physical code/config locations in the implementation backlog, and TSK-0539 must bind privacy-safe runtime signals/alerts.\n- CR-0009 boundary is preserved: legal/regulatory/compliance conclusions are owner-external/not AI-verified; technical privacy engineering, auth/authz/CSRF/IDOR, ClientID isolation, deletion/recovery, no-history telemetry, secrets, supply chain, DNS abuse, protection truth, monitoring and rollback remain mandatory.\n- **Non-inference:** no control implementation, vulnerability closure, penetration-test result, RSK-0001/RSK-0007 closure, TSK-0539/TSK-0048/TSK-0049/LG-07 PASS, L6 build, production activation, publication, payment, market or launch authority is inferred from TSK-0239 PASS.\n\n### Queue status after TSK-0239 acceptance\n\nRecompute the residual L5 frontier from current WBS/graph/runtime/gates and DEC-0056 semantics. Direct successors may consume TSK-0239 only if their other current dependencies and own acceptance are independently satisfied.\n\n'''
    text = text.replace(marker, section + marker, 1)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    text = re.sub(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {now}', text, count=1)
    STATE.write_text(text, encoding='utf-8')


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else '--verify'
    blob = verify()
    print('TSK0239_MATRIX_BLOB=' + blob)
    print('TSK0239_VERIFY=PASS')
    if mode == '--record-state':
        record_state(blob)
        print('TSK0239_STATE_PREPARED=1')
    elif mode != '--verify':
        raise SystemExit('usage: verify_tsk0239_security_control_matrix_20260902.py [--verify|--record-state]')


if __name__ == '__main__':
    main()
