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
ART = ROOT / 'TSK_0539_PRIVACY_SAFE_LOGS_METRICS_TRACES_DASHBOARDS_ALERTS_2026-09-02.md'
STATE = ROOT / 'CURRENT_STATE.md'
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
MANIFEST = ROOT / 'Plans/Master/MANIFEST.yaml'
LAYER5 = ROOT / 'Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md'
EXPECTED_ART_BLOB = '291cd76d5f71fedb98188e6ecd5679c16ea44a98'
ARTIFACT_COMMIT = 'fc4581f3e27b136395d10ff069af450437241688'
EXPECTED_DEP_BLOBS = {
    'TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md': '44c9c299465e821e2ffd84a54b77e3e615d61925',
    'TSK_0239_SECURITY_PRIVACY_CONTROL_IMPLEMENTATION_VERIFICATION_MATRIX_2026-09-02.md': '674c21b4c169da4fb496617164ad68cfc6527fb4',
}
EXPECTED_SLIS = [
    'DoH availability','DoT availability','DNS correctness','DNS latency','TLS validity',
    'Accountless web critical-path availability','Accountless critical-route latency',
    'Optional session-establishment availability','Dashboard/device-read availability',
    'Account mutation terminal-truth correctness','Authorization isolation',
    'Accountless fallback during auth/provider failure','Recovery objective attainment',
    'Telemetry critical-path coverage',
]


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def table_rows_between(text: str, start: str, end: str):
    a = text.index(start)
    b = text.index(end, a + len(start))
    rows = []
    for line in text[a:b].splitlines():
        if not line.startswith('|'):
            continue
        if re.match(r'^\|\s*-+', line):
            continue
        if line.lower().startswith('| sli ') or line.lower().startswith('| threat ') or line.lower().startswith('| runbook '):
            continue
        rows.append(line)
    return rows


def verify() -> str:
    assert ART.is_file()
    text = ART.read_text(encoding='utf-8')
    state = STATE.read_text(encoding='utf-8')
    manifest = MANIFEST.read_text(encoding='utf-8')
    layer5 = LAYER5.read_text(encoding='utf-8')

    assert 'latest_change: CR-0009' in manifest
    assert '### 5.3.8 Owner-external legal/compliance scope (DEC-0056 / CR-0009)' in layer5
    assert '## TSK-0538 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE RELIABILITY NFR REVALIDATION' in state
    assert '`TSK-0538 — Define reliability, observability, recovery, and service-level NFRs`: **PASS**' in state
    assert '## TSK-0239 current accepted stable state — 2026-09-02 — POST-CR-0009' in state
    assert '`TSK-0239 — Create security/privacy control implementation and verification matrix`: **PASS**' in state
    assert '## TSK-0539 current accepted stable state — 2026-09-02 — POST-CR-0009' not in state

    with WBS.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0539')
    assert (row.get('Lifecycle_Stage') or '').strip() == 'L5'
    assert {x.strip() for x in (row.get('Dependencies') or '').split(';') if x.strip()} == {'TSK-0538','TSK-0239'}
    assert (row.get('Priority') or '').strip() == 'MEDIUM'
    assert (row.get('AI_Capability_A0_A4') or '').strip() == 'A3'
    assert (row.get('Action_Authority') or '').strip() == 'AUTO_ALLOWED'
    assert (row.get('Acceptance_ID') or '').strip() == 'ACC-0539'
    assert (row.get('Verification_ID') or '').strip() == 'VER-0539'
    assert (row.get('Evidence_ID') or '').strip() == 'EVD-0539'
    assert (row.get('Risk_Reference') or '').strip() == 'RSK-0006'
    assert (row.get('Interface_Reference') or '').strip() == 'INT-0018'
    reqs = {x.strip() for x in (row.get('Requirement_Reference') or '').split(';') if x.strip()}
    assert reqs == {'REQ-0070','REQ-0071','CON-0018','CON-0022'}
    acc = (row.get('Acceptance_Criteria') or '').strip()
    for token in ('SLI/threat','collection point','fields','retention','access','alert threshold','runbook','privacy review','DNS/domain history','identifiable client statistics'):
        assert token.lower() in acc.lower(), token

    for rel, expected in EXPECTED_DEP_BLOBS.items():
        p = ROOT / rel
        assert p.is_file(), rel
        assert git_blob_sha(p) == expected, rel
    assert git_blob_sha(ART) == EXPECTED_ART_BLOB

    sli_rows = table_rows_between(text, '## 7. SLI → signal / collection / retention / alert / runbook matrix', '## 8. Threat → telemetry / alert / runbook matrix')
    assert len(sli_rows) == 14, len(sli_rows)
    sli_names = []
    for line in sli_rows:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        assert len(cells) == 9, (len(cells), line)
        assert all(cells)
        sli_names.append(cells[0])
        assert 'R1' in cells[4] or 'R2' in cells[4] or 'R3' in cells[4]
        assert 'RB-' in cells[7]
        assert 'PR-' in cells[8]
    assert sli_names == EXPECTED_SLIS, sli_names

    threat_rows = table_rows_between(text, '## 8. Threat → telemetry / alert / runbook matrix', '## 9. Runbook catalogue')
    assert len(threat_rows) == 30, len(threat_rows)
    ids = []
    for line in threat_rows:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        assert len(cells) == 7, (len(cells), line)
        assert all(cells)
        m = re.match(r'TM-(\d{2})\b', cells[0])
        assert m, cells[0]
        ids.append('TM-' + m.group(1))
        assert 'R1' in cells[3] or 'R2' in cells[3] or 'R3' in cells[3]
        assert 'RB-' in cells[5]
        assert 'PR-' in cells[6]
    assert ids == [f'TM-{i:02d}' for i in range(1,31)], ids

    runbook_rows = table_rows_between(text, '## 9. Runbook catalogue', '## 10. Dashboard contract')
    assert len(runbook_rows) == 9, len(runbook_rows)
    assert [f'`RB-{i:02d}' in runbook_rows[i-1] for i in range(1,10)] == [True]*9

    for marker in (
        '`R0_FORBIDDEN`','`R1_DIAGNOSTIC`','`R2_OPERATIONAL_AGGREGATE`','`R3_ACCEPTANCE_EVIDENCE`',
        '`0` — do not collect','`<=24h`','`<=30d`','Unknown fields fail telemetry schema validation',
        'Never use request/correlation ID, trace/span ID, identity, ClientID, raw URL, DNS/domain/query, error text or timestamp as a metric label',
        'All latency metrics are histograms','p50/p95/p99',
        'No user/device/client/domain drill-down exists',
        'Tracing is **disabled by default','successful-request sampling is capped at `<=1%`',
        '`PAGE`','`TICKET`','missing telemetry is `unknown/blind`, never healthy',
        '`PR-01 FIELD_ALLOWLIST`','`PR-02 CARDINALITY`','`PR-03 NO_HISTORY_NO_SECRET`',
        '`PR-04 RETENTION`','`PR-05 ACCESS`','`PR-06 SYNTHETIC_FIXTURES`',
        'no monitoring vendor, paid service, implementation, target-environment success, legal conclusion or downstream gate PASS is inferred',
    ):
        assert marker in text, marker

    for event in (
        'ops_http_request_outcome','ops_dependency_call_outcome','ops_session_operation_outcome',
        'ops_authorization_denied','ops_device_mutation_outcome','ops_reconciliation_outcome',
        'ops_protection_verification_outcome','ops_synthetic_probe_outcome','ops_recovery_operation_outcome',
        'ops_security_control_violation','ops_telemetry_guard_violation',
    ):
        assert text.count(f'`{event}`') == 1, event

    for dash in ('### D1 — Core Protection Health','### D2 — Optional Account Health','### D3 — Security / Privacy Controls','### D4 — Recovery / Capacity'):
        assert dash in text

    # Literal secret guard for the artifact itself.
    for pat in (r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', r'ghp_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}', r'AKIA[0-9A-Z]{16}'):
        assert not re.search(pat, text)

    subprocess.run(['git','diff','--check'], cwd=ROOT, check=True)
    completed = subprocess.run(['python3','Plans/Master/Tools/validate_master_plan.py'], cwd=ROOT, text=True, capture_output=True, check=True)
    combined = completed.stdout + completed.stderr
    assert 'VALIDATION PASS' in combined
    print(completed.stdout, end='')
    print('ACC_0539=PASS')
    print('VER_0539=PASS')
    print('EVD_0539=PASS')
    return EXPECTED_ART_BLOB


def record_state(blob: str) -> None:
    run_id = os.environ.get('GITHUB_RUN_ID','').strip()
    run_attempt = os.environ.get('GITHUB_RUN_ATTEMPT','').strip()
    source_sha = os.environ.get('GITHUB_SHA','').strip()
    assert run_id and run_attempt and source_sha
    text = STATE.read_text(encoding='utf-8')
    marker = '## CR-0007 current authority and execution boundary\n'
    assert marker in text
    heading = '## TSK-0539 current accepted stable state — 2026-09-02 — POST-CR-0009'
    assert heading not in text
    section = f'''{heading}\n\n`TSK-0539 — Design privacy-safe logs, metrics, traces, dashboards, and alerts`: **PASS** under current `ACC-0539 / VER-0539 / EVD-0539`, direct predecessor `TSK-0538` PASS and direct predecessor `TSK-0239` PASS.\n\n- Current WBS: L5 / MEDIUM / A3 / `AUTO_ALLOWED`; hard dependencies exactly `TSK-0538; TSK-0239`.\n- Accepted artifact: `TSK_0539_PRIVACY_SAFE_LOGS_METRICS_TRACES_DASHBOARDS_ALERTS_2026-09-02.md`, version `1.0.0`, blob `{blob}`, publication commit `{ARTIFACT_COMMIT}`.\n- Independent GitHub Actions verification run/attempt `{run_id} / {run_attempt}`, source commit `{source_sha}`, verified current WBS/ACC/VER/EVD/dependency/authority contract; exact TSK-0538 and TSK-0239 artifact blobs; all 14 current SLI rows; all TM-01..TM-30 threat rows; nine runbook mappings; R0/R1/R2/R3 retention/access classes; event/metric/cardinality/privacy guards; four dashboard contracts; optional bounded tracing; literal-secret guard; `git diff --check`; and full modular master-plan validator PASS.\n- The accepted design uses privacy-minimal structured operational events, bounded RED/USE/synthetic metrics, optional vendor-neutral tracing, PAGE/TICKET symptom/control alerts, explicit runbooks, automatic bounded retention and schema/cardinality/no-history guards.\n- No telemetry signal may contain DNS/domain/query/browsing history, identity, raw IP, raw ClientID, credentials/tokens, request bodies, raw URLs or persistent anonymous-to-account linkage. R1 diagnostic telemetry is capped at 24h; R2 aggregate telemetry at 30d; durable evidence retains only aggregate/test/version/run metadata.\n- No monitoring/APM/log backend, collector, alerting vendor, HA topology or paid service is selected or purchased by this task. Physical code/config locations remain owned by TSK-0048 and implementation/target-environment proof remains downstream.\n- CR-0009 is preserved: legal/compliance conclusions remain owner-external/not AI-verified; the technical privacy-engineering obligations in this telemetry design remain mandatory.\n- **Non-inference:** no instrumentation/backend/collector/tracing deployment, notification delivery, production SLO attainment, TSK-0239 control closure, TSK-0049/TSK-0237/TSK-0048/LG-07 PASS, L6 build, production activation, legal readiness, payment, market or launch PASS is inferred.\n\n### Queue status after TSK-0539 acceptance\n\nRecompute the residual L5 frontier from current WBS/graph/runtime/gates and DEC-0056 semantics. TSK-0049 and TSK-0237 may consume TSK-0539 only if their other current dependencies and own acceptance are independently satisfied.\n\n'''
    text = text.replace(marker, section + marker, 1)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
    text = re.sub(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {now}', text, count=1)
    STATE.write_text(text, encoding='utf-8')


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else '--verify'
    blob = verify()
    if mode == '--record-state':
        record_state(blob)
        print('TSK0539_STATE_PREPARED=1')
    elif mode != '--verify':
        raise SystemExit('usage: verify_tsk0539_privacy_safe_observability_20260902.py [--verify|--record-state]')


if __name__ == '__main__':
    main()
