#!/usr/bin/env python3
from pathlib import Path
import csv
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / 'TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_2026-09-01.md'
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
REQ = ROOT / 'Plans/Master/Registers/REQUIREMENTS.md'
RISKS = ROOT / 'Plans/Master/Registers/RISKS.md'
CONSTRAINTS = ROOT / 'Plans/Master/Registers/CONSTRAINTS.md'
INTERFACES = ROOT / 'Plans/Master/Registers/INTERFACES.md'
DECISIONS = ROOT / 'Plans/Master/Registers/DECISIONS_TRIGGERS.md'
RECOVERY = ROOT / 'infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md'
RECOVERY_EVIDENCE = ROOT / 'TSK_0446_RECOVERY_SCOPE_CONTRACT_EVIDENCE_2026-09-01.md'
BUNDLE_DIR = ROOT / 'infrastructure/adguard-server/tsk-0413-bundle-v1'
BUNDLE = BUNDLE_DIR / 'bundle.json'


def fail(msg: str) -> None:
    raise SystemExit('TSK_0518_VERIFY_FAIL: ' + msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f'missing required text in {where}: {needle}')


plan = PLAN.read_text(encoding='utf-8')
state = STATE.read_text(encoding='utf-8')
req = REQ.read_text(encoding='utf-8')
risks = RISKS.read_text(encoding='utf-8')
constraints = CONSTRAINTS.read_text(encoding='utf-8')
interfaces = INTERFACES.read_text(encoding='utf-8')
decisions = DECISIONS.read_text(encoding='utf-8')
recovery = RECOVERY.read_text(encoding='utf-8')
recovery_evidence = RECOVERY_EVIDENCE.read_text(encoding='utf-8')
bundle = json.loads(BUNDLE.read_text(encoding='utf-8'))

# Exact current task authority.
with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = [r for r in rows if r['Task_ID'] == 'TSK-0518']
if len(row) != 1:
    fail('expected exactly one TSK-0518 WBS row')
row = row[0]
expected = {
    'Lifecycle_Stage': 'L5',
    'Priority': 'CRITICAL',
    'Dependencies': 'TSK-0446',
    'AI_Capability_A0_A4': 'A3',
    'Action_Authority': 'AUTO_ALLOWED',
    'Acceptance_ID': 'ACC-0518',
    'Verification_ID': 'VER-0518',
    'Evidence_ID': 'EVD-0518',
}
for key, value in expected.items():
    if row.get(key, '').strip() != value:
        fail(f'TSK-0518 {key} drift: {row.get(key)!r}')
expected_acc = 'Plan prevents producer-only self-certification and maps every recovery requirement to evidence and severity/blocking rules.'
if row['Acceptance_Criteria'] != expected_acc:
    fail('ACC-0518 wording drift')
if row['Verification_Method'] != 'Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.':
    fail('VER-0518 method drift')

# Current gate and predecessor runtime must be durable.
require(state, '## TSK-0052 / LG-06 current accepted stable state — 2026-09-01 — POST-CR-0007', 'CURRENT_STATE.md')
require(state, '## TSK-0446 current accepted stable state — 2026-09-01', 'CURRENT_STATE.md')
require(state, 'TSK_0446_RECOVERY_SCOPE_CONTRACT_EVIDENCE_2026-09-01.md', 'CURRENT_STATE.md')
require(state, 'GitHub Actions run/job `33504115232 / 99843993787` — **SUCCESS**', 'CURRENT_STATE.md')
require(recovery_evidence, '**TSK-0446: PASS** at its defined L5 recovery-contract boundary.', 'TSK-0446 evidence')

# Exact predecessor artifacts have not drifted.
expected_hashes = {
    RECOVERY: '18d998e2406e801c7ac08f4daa2e3b763ea9b523',
    RECOVERY_EVIDENCE: '714a5ccf4e7d0dc104ff55c1d87381571ab786f9',
    BUNDLE: 'f0735e6a508f16de7a9c4510cc2893b972c1786c',
}
for path, expected_hash in expected_hashes.items():
    actual = subprocess.check_output(['git', 'hash-object', str(path)], cwd=ROOT, text=True).strip()
    if actual != expected_hash:
        fail(f'predecessor artifact drift: {path} {actual}')

# Re-run the accepted TSK-0413 bundle verifier.
proc = subprocess.run([sys.executable, str(BUNDLE_DIR / 'verify_bundle.py')], cwd=ROOT, text=True, capture_output=True)
if proc.returncode != 0 or 'TSK_0413_BUNDLE_VERIFY=PASS' not in proc.stdout:
    fail('TSK-0413 bundle self-verification failed: ' + proc.stdout + proc.stderr)

# Current privacy-first desired state.
settings = bundle['settings']
if settings['querylog'] != {'enabled': False, 'file_enabled': False, 'interval': '1d'}:
    fail('querylog desired-state drift')
if settings['statistics'] != {'enabled': True, 'interval': '1d'}:
    fail('aggregate statistics desired-state drift')
if settings['dns']['anonymize_client_ip'] is not True:
    fail('client-IP anonymization drift')
if settings['dns']['edns_client_subnet'] != {'enabled': False, 'use_custom': False, 'custom_ip': ''}:
    fail('ECS desired-state drift')
if settings['dns']['upstream_dns'] != ['https://dns10.quad9.net/dns-query']:
    fail('upstream desired-state drift')

# Governing requirement/risk/constraint/interface texts.
require(req, '| REQ-0065 | MUST | PKG-12 | Every critical requirement shall map to verification, evidence, acceptance, and a gate or operational decision where applicable.', 'REQUIREMENTS.md')
require(req, '| REQ-0066 | MUST | PKG-12 | Integrated verification shall cover functional, device/network, UX/comprehension, accessibility, security, privacy, performance, failure, recovery, and rollback paths.', 'REQUIREMENTS.md')
require(risks, '| RSK-0050 |  | QA or AI marks PASS from artifact existence, local behavior, or incomplete evidence.', 'RISKS.md')
require(constraints, '| CON-0023 | Correctness, security/privacy, reliability/trust, and product quality are hard gates;', 'CONSTRAINTS.md')
require(constraints, '| CON-0029 | No hidden chain-of-thought is evidence.', 'CONSTRAINTS.md')
require(interfaces, '| INT-0017 | Verified release to operations | PKG-12 | PKG-13 | OPERATIONAL_HANDOFF |', 'INTERFACES.md')
require(interfaces, '| INT-0025 | Recovery system to independent acceptance | PKG-09 | PKG-12 | ARTIFACT |', 'INTERFACES.md')
require(decisions, 'minimum anonymized aggregate operational statistics may be enabled with 24-hour retention', 'DECISIONS_TRIGGERS.md')

# Structural acceptance plan checks.
required_fragments = [
    '**Plan version:** 1.0.0',
    '**Owner:** QA / Release Acceptance',
    '## 2. Independence model — producer-only self-certification is prohibited',
    '**Producer:** Cloud / Platform Engineering (`PKG-09`)',
    '**Acceptance owner:** QA / Release Acceptance (`PKG-12`)',
    'Producer-generated logs, unit tests, screenshots, local runs, or declarations are **supporting evidence only**',
    'A local/container/mock-only result cannot satisfy a criterion',
    '## 4. Evidence classes',
    '`DT` Direct target evidence',
    '`IN` Inference',
    '**Never**',
    '## 5. Severity and blocking rules',
    '### Evidence blocker `EB`',
    '### `S1 — Critical` — always blocking',
    '### `S2 — High` — always blocking for recovery acceptance',
    'No numeric tolerance around “approximately 30 minutes” is invented by QA',
    '## 6. Recovery requirement-to-evidence matrix',
    '## 7. Required independent execution suites',
    '## 8. Evidence record schema',
    '## 9. PASS algorithm',
    '## 11. Reopen / invalidation triggers',
    'persistent query/file logging off',
    'minimum anonymized aggregate operational statistics enabled with `1d` retention',
    'identifiable per-client statistics/history remain excluded',
    'Any older source saying simply “statistics off” is not allowed to override current DEC-0016/TSK-0413.',
    'This document is an acceptance **plan**.',
]
for fragment in required_fragments:
    require(plan, fragment, PLAN.name)

# Require exactly RA-01..RA-20 as matrix rows, all with evidence class and blocking field.
rows = re.findall(r'^\| `RA-(\d{2})` \|([^\n]+)$', plan, flags=re.MULTILINE)
ids = [int(i) for i, _ in rows]
if ids != list(range(1, 21)):
    fail(f'RA matrix must contain exactly RA-01..RA-20 in order, got {ids}')
for i, rest in rows:
    cells = [c.strip() for c in rest.split('|')]
    if len(cells) < 4:
        fail(f'RA-{i} incomplete matrix row')
    evidence_class = cells[-2]
    severity = cells[-1]
    if not any(k in evidence_class for k in ['DT', 'IR', 'DO']):
        fail(f'RA-{i} has no direct/reproducible evidence class')
    if not any(k in severity for k in ['EB', 'S1', 'S2', 'S3', 'S4']):
        fail(f'RA-{i} has no severity/blocking mapping')

# Coverage must include all recovery-contract acceptance areas and no target-result inference.
for area in [
    'host', 'packages', 'AdGuard', 'configuration', 'network', 'firewall', 'DNS', 'TLS',
    'filter', 'security', 'privacy', 'startup', 'verification', 'health', 'timing', 'rollback',
    'idempotency', 'drift', 'failure', 'backup', 'restore',
]:
    if area.lower() not in plan.lower():
        fail('missing recovery coverage term: ' + area)

for forbidden in [
    'clean-server recovery passed',
    'rto achieved in approximately 30 minutes',
    'production recovery accepted',
]:
    if forbidden in plan.lower():
        fail('forbidden target-result inference: ' + forbidden)

# Planned downstream evidence producers are explicitly non-PASS/non-dependency statements.
for task in ['TSK-0456', 'TSK-0457', 'TSK-0462', 'TSK-0459', 'TSK-0460', 'TSK-0447', 'TSK-0519', 'TSK-0461', 'TSK-0482']:
    require(plan, f'`{task}`', PLAN.name)
require(plan, 'listing them does not mark them complete or create new dependencies', PLAN.name)

print('TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_VERIFY=PASS')
print('plan_version=1.0.0')
print('dependency=TSK-0446')
print('mapped_recovery_rows=20')
print('producer_only_self_certification=prohibited')
print('privacy_baseline=tsk0413_dec0016_current')
print('target_execution_claimed=false')
