from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'CURRENT_STATE.md': 'db1f55f6d78e2408bab515fa6bcddd0c6cb5ac20',
    'TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md': '44c9c299465e821e2ffd84a54b77e3e615d61925',
    'TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_2026-08-28.md': 'd81537ef3ef66789528336e101d1e05f30030892',
    'TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_EVIDENCE_2026-08-28.md': 'bd7a9f0d8a54dd28d423587257f1cd226b3e5dbc',
    'TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md': '285ee390499190137e8aac0fed976975fb79ed80',
    'TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md': 'a7461f68f99ccda5c947a4ee77453817db9db1e5',
}


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def between(text: str, start: str, end: str) -> str:
    assert start in text, f'missing section start: {start}'
    tail = text.split(start, 1)[1]
    assert end in tail, f'missing section end: {end}'
    return tail.split(end, 1)[0]


def table_rows(section: str, columns: int, header_prefix: str) -> list[list[str]]:
    rows = []
    for line in section.splitlines():
        if not line.startswith('| '):
            continue
        if line.startswith(header_prefix) or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == columns:
            rows.append(cells)
    return rows


for path, expected in EXPECTED.items():
    p = Path(path)
    assert p.exists(), f'missing {path}'
    actual = blob(path)
    assert actual == expected, f'hash drift {path}: {actual} != {expected}'
print('TSK0538_IMMUTABLE_INPUT_HASHES=PASS')

with open('Plans/Master/WBS/master-wbs.csv', newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
byid = {r['Task_ID']: r for r in rows if r.get('Task_ID')}
r = byid['TSK-0538']
assert (r['Lifecycle_Stage'], r['Priority'], r['AI_Capability_A0_A4'], r['Action_Authority']) == ('L4', 'MEDIUM', 'A3', 'AUTO_ALLOWED')
assert r['Dependencies'].strip() == 'TSK-0484'
assert (r['Acceptance_ID'], r['Verification_ID'], r['Evidence_ID']) == ('ACC-0538', 'VER-0538', 'EVD-0538')
acc = r['Acceptance_Criteria'].lower()
for concept in ['critical user journeys', 'sli/slo', 'alert conditions', 'recovery objectives', 'backup scope', 'restore test', 'maintenance behavior', 'escalation ownership']:
    assert concept in acc, concept
print('TSK0538_CURRENT_WBS_CONTRACT=PASS')

runtime = Path('CURRENT_STATE.md').read_text(encoding='utf-8')
task_pattern = re.compile(r'^(##|###) (TSK-\d{4})\b.*?(?=^(?:##|###) |\Z)', re.MULTILINE | re.DOTALL)
sections = [m.group(0) for m in task_pattern.finditer(runtime) if m.group(2) == 'TSK-0484']
assert any('**PASS' in s and 'POST-CR-0008 SECURITY NFR REVALIDATION' in s for s in sections)
print('TSK0538_CURRENT_TSK0484_PREDECESSOR=PASS')

old = Path('TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_2026-08-28.md').read_text(encoding='utf-8')
assert 'Accountless web/app start -> setup -> Protection Map' in old
old_journey_section = between(old, '## 3. Critical journeys and service boundaries', '## 4.')
for active_row in ['Optional sign-in', 'Dashboard/device read', 'Auth provider failure', 'Datastore/ownership failure']:
    assert active_row not in old_journey_section, active_row
assert 'future web/app' in old.lower()
print('TSK0538_HISTORICAL_ACCOUNTLESS_ONLY_APP_GAP=PASS')

a = Path('TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md').read_text(encoding='utf-8')
al = a.lower()
assert 'current direct predecessor tsk-0484' in al
for concept in ['authentication', 'session', 'ownership', 'provider', 'datastore', 'consequential mutation reconciliation', 'accountless fallback']:
    assert concept in al, concept
print('TSK0538_CURRENT_DEPENDENCY_GAP_CLOSURE=PASS')

journeys = table_rows(between(a, '## 6. Current critical-journey catalogue', '## 7.'), 4, '| Journey')
names = {row[0] for row in journeys}
required_journeys = {
    'DoH transaction', 'DoT transaction', 'Accountless start → supported setup → verification → Protection Map', 'Accountless recovery/removal',
    'Optional sign-in → session establish/refresh', 'Dashboard/device read', 'Device register/update/unlink/delete', 'Logout/session revoke', 'Account deletion',
    'Auth provider failure', 'Datastore/ownership failure', 'AdGuard control/verification failure',
}
assert names == required_journeys, (names, required_journeys)
assert all(len(row[2]) >= 25 and len(row[3]) >= 20 for row in journeys)
print('TSK0538_12_CRITICAL_JOURNEYS=PASS')

questions = between(a, '## 5. Current on-call questions', '## 6.')
qnums = {int(x) for x in re.findall(r'(?m)^(\d+)\. ', questions)}
assert qnums == set(range(1, 14)), qnums
print('TSK0538_13_ONCALL_QUESTIONS=PASS')

signal = between(a, '## 7. Signal contract', '## 8.').lower()
for token in ['request/operation rate', 'error/outcome rate', 'latency histograms', 'auth provider', 'datastore', 'adguard control', 'request/correlation id', 'structured logs', 'distributed tracing is optional', 'opentelemetry']:
    assert token in signal, token
for forbidden in ['parent/user/account id', 'firebase uid or provider subject', 'device id or `clientid`', 'dns/domain/query data', 'raw url/query string']:
    assert forbidden in signal, forbidden
assert 'request/correlation ids are diagnostic fields, not metric labels' in signal
print('TSK0538_SIGNAL_AND_CARDINALITY_CONTRACT=PASS')

slo_rows = table_rows(between(a, '## 8. Provisional current SLIs/SLOs', '## 9.'), 3, '| SLI')
slos = {row[0]: (row[1], row[2]) for row in slo_rows}
required_slos = {
    'DoH availability', 'DoT availability', 'DNS correctness', 'DNS latency', 'TLS validity', 'Accountless web critical-path availability',
    'Accountless critical-route latency', 'Optional session-establishment availability', 'Dashboard/device-read availability',
    'Account mutation terminal-truth correctness', 'Authorization isolation', 'Accountless fallback during auth/provider failure',
    'Recovery objective attainment', 'Telemetry critical-path coverage',
}
assert set(slos) == required_slos, (set(slos), required_slos)
assert '>=99.9%' in slos['Optional session-establishment availability'][1]
assert '100%' in slos['Account mutation terminal-truth correctness'][1]
assert '100%' in slos['Authorization isolation'][1]
assert '100%' in slos['Accountless fallback during auth/provider failure'][1]
assert 'p95' in slos['DNS latency'][1] and 'p99' in slos['DNS latency'][1]
print('TSK0538_14_PROVISIONAL_SLI_SLO_CONTRACTS=PASS')

alert = between(a, '## 9. Alert contract', '## 10.').lower()
assert '**page**' in alert and '**ticket**' in alert
for concept in ['accountless critical path', 'optional sign-in/session', 'ownership/authorization', 'deletion/revoke', 'resurrected or still-live authority', 'security/privacy', 'slo/error-budget burn', 'telemetry blind spot']:
    assert concept in alert, concept
assert 'every alert must identify the affected journey, symptom, first diagnostic query/check, current owner and runbook' in alert
print('TSK0538_ALERT_CONTRACT=PASS')

recovery = between(a, '## 10. Recovery and fail-safe objectives', '## 11.').lower()
assert '`<=30 minutes` end to end' in recovery
assert 'provisional internal rto is **`<=30 minutes`**' in recovery
assert 'cannot promise third-party provider recovery time' in recovery
assert 'zero security-authority regression is tolerated' in recovery
assert 'unknown/reconcile-required' in recovery and 'not automatic replay or success' in recovery
print('TSK0538_RECOVERY_OBJECTIVES=PASS')

restore = between(a, '## 11. Backup / restore scope', '## 12.').lower()
for excluded in ['dns/query/domain/browsing history', 'j0/j1 transient journey records', 'raw product event streams', 'session cookies/bearer tokens/refresh tokens', 'provider/service-account secrets']:
    assert excluded in restore, excluded
restore_steps = {int(x) for x in re.findall(r'(?m)^(\d+)\. ', restore)}
assert set(range(1, 13)).issubset(restore_steps), restore_steps
assert 'revoked/deleted authority is not resurrected' in restore
print('TSK0538_BACKUP_RESTORE_CONTRACT=PASS')

maintenance = between(a, '## 12. Maintenance behavior', '## 13.').lower()
for concept in ['auth provider', 'persistent account/device schema', 'ownership/clientid lifecycle', 'delete/revoke semantics', 'observability schema', 'tsk-0484 high/critical control', 'restore path or backup scope']:
    assert concept in maintenance, concept
print('TSK0538_MAINTENANCE_REVALIDATION_TRIGGERS=PASS')

incident_rows = table_rows(between(a, '## 13. Incident and escalation ownership', '## 14.'), 3, '| Incident')
domains = {row[0] for row in incident_rows}
required_domains = {'DNS/platform', 'Public/accountless web app', 'Auth/session/provider', 'Parent/device ownership/datastore', 'AdGuard control/ClientID', 'Privacy/security control', 'Azure/control-plane', 'Public/customer communication'}
assert domains == required_domains, (domains, required_domains)
print('TSK0538_ESCALATION_OWNERSHIP=PASS')

for url in [
    'https://sre.google/sre-book/monitoring-distributed-systems/',
    'https://sre.google/workbook/implementing-slos/',
    'https://opentelemetry.io/docs/concepts/observability-primer/',
    'https://opentelemetry.io/docs/concepts/signals/',
    'https://opentelemetry.io/docs/concepts/signals/metrics/',
    'https://opentelemetry.io/docs/specs/otel/logs/',
    'https://prometheus.io/docs/practices/naming/',
]:
    assert url in a, url
print('TSK0538_CURRENT_SOURCE_BINDINGS=PASS')

assertion_section = between(a, '## 14. Current acceptance assertions', '## 15.')
assertions = {int(x) for x in re.findall(r'(?m)^(\d+)\. ', assertion_section)}
assert assertions == set(range(1, 17)), assertions
assert '**ACC-0538 current candidate: PASS pending independent current VER-0538.**' in a
assert 'no collector/backend/APM purchase or deployment is authorized' in a
assert 'does not implement or self-certify TSK-0352 or TSK-0353' in a
print('TSK0538_CURRENT_ACCEPTANCE_ASSERTIONS=PASS')

subprocess.check_call(['git', 'diff', '--check'])
print('TSK0538_CURRENT_ACC=PASS')
print('WBS_BLOB=' + blob('Plans/Master/WBS/master-wbs.csv'))
print('GRAPH_BLOB=' + blob('Plans/Master/RELATIONSHIP_INDEX.yaml'))
print('RUNTIME_BLOB=' + blob('CURRENT_STATE.md'))
print('ARTIFACT_BLOB=' + blob('TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md'))
