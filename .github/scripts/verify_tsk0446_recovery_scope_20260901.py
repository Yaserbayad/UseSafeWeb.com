#!/usr/bin/env python3
from pathlib import Path
import csv
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / 'infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md'
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
DECISIONS = ROOT / 'Plans/Master/Registers/DECISIONS_TRIGGERS.md'
STATE = ROOT / 'CURRENT_STATE.md'
BUNDLE_DIR = ROOT / 'infrastructure/adguard-server/tsk-0413-bundle-v1'
BUNDLE = BUNDLE_DIR / 'bundle.json'
ENDPOINTS = BUNDLE_DIR / 'endpoints.json'
BUNDLE_EVIDENCE = ROOT / 'TSK_0413_BUNDLE_VERIFICATION_EVIDENCE_2026-09-01.md'
BACKUP_POLICY = ROOT / 'infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md'


def fail(msg: str) -> None:
    raise SystemExit('TSK_0446_VERIFY_FAIL: ' + msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f'missing required text in {where}: {needle}')


contract = CONTRACT.read_text(encoding='utf-8')
decisions = DECISIONS.read_text(encoding='utf-8')
state = STATE.read_text(encoding='utf-8')
bundle_evidence = BUNDLE_EVIDENCE.read_text(encoding='utf-8')
backup_policy = BACKUP_POLICY.read_text(encoding='utf-8')
bundle = json.loads(BUNDLE.read_text(encoding='utf-8'))
endpoints = json.loads(ENDPOINTS.read_text(encoding='utf-8'))

# Current task authority and dependency contract.
with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = [r for r in rows if r['Task_ID'] == 'TSK-0446']
if len(row) != 1:
    fail('expected exactly one TSK-0446 WBS row')
row = row[0]
if row['Layer'] != 'L5':
    fail('TSK-0446 is not L5')
if row['Priority'] != 'CRITICAL':
    fail('TSK-0446 priority drift')
if row['Dependencies'].strip() != 'TSK-0413':
    fail('TSK-0446 hard dependency drift')
if row['AI_Capability_A0_A4'] != 'A3' or row['Action_Authority'] != 'AUTO_ALLOWED':
    fail('TSK-0446 capability/authority drift')
expected_acc = 'Contract covers host/packages/AdGuard/config/network/firewall/DNS endpoint/TLS/filter/security/privacy/startup/verification/health and measures actual service restoration within approximately 30 minutes.'
if row['Acceptance_Criteria'] != expected_acc:
    fail('ACC-0446 wording drift')

# Gate and predecessor must be current in volatile runtime, not inferred from the WBS snapshot.
require(state, 'TSK-0052 / LG-06 — Product, Brand and Experience Freeze', 'CURRENT_STATE.md')
require(state, 'TSK-0413', 'CURRENT_STATE.md')
require(state, 'current accepted stable state', 'CURRENT_STATE.md')
require(state, 'TSK_0413_BUNDLE_VERIFICATION_EVIDENCE_2026-09-01.md', 'CURRENT_STATE.md')
require(bundle_evidence, 'All current `ACC-0413` clauses are evidenced.', 'TSK-0413 evidence')
require(bundle_evidence, 'Run/job: `33500597612 / 99832778403`', 'TSK-0413 evidence')

# Owner-approved current privacy semantics. The key point is identifiable-history prohibition plus bounded anonymized aggregate stats.
require(decisions, 'DEC-0016', 'DECISIONS_TRIGGERS.md')
require(decisions, 'minimum anonymized aggregate operational statistics may be enabled with 24-hour retention', 'DECISIONS_TRIGGERS.md')
require(decisions, 'persistent raw query history and file query logging are off', 'DECISIONS_TRIGGERS.md')
require(decisions, 'identifiable per-client statistics/history remain excluded', 'DECISIONS_TRIGGERS.md')

# Exact TSK-0413 recovery-consumer baseline.
if bundle.get('bundle_version') != '1.0.0':
    fail('TSK-0413 bundle version drift')
compat = bundle['compatibility']
if compat['adguard_home_version'] != 'v0.107.79' or compat['config_schema_version'] != 34:
    fail('AdGuard compatibility drift')
if compat['official_tag_commit'] != '05ba17b282da1c4393d6a4ba4db0cf519194a362':
    fail('AdGuard tag commit drift')
settings = bundle['settings']
if settings['querylog'] != {'enabled': False, 'file_enabled': False, 'interval': '1d'}:
    fail('querylog baseline drift')
if settings['statistics'] != {'enabled': True, 'interval': '1d'}:
    fail('statistics baseline drift')
if settings['dns']['anonymize_client_ip'] is not True:
    fail('client IP anonymization drift')
if settings['dns']['edns_client_subnet'] != {'enabled': False, 'use_custom': False, 'custom_ip': ''}:
    fail('ECS baseline drift')
if settings['dns']['upstream_dns'] != ['https://dns10.quad9.net/dns-query']:
    fail('upstream drift')
if settings['filters'] != [{'name': 'AdGuard DNS filter', 'url': 'https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt', 'enabled': True}]:
    fail('filter baseline drift')
if settings['whitelist_filters'] != [] or settings['user_rules'] != []:
    fail('allowlist/user-rule baseline drift')
if bundle['admin_policy']['bind_address'] != '127.0.0.1:3000' or bundle['admin_policy']['public_exposure'] is not False:
    fail('admin exposure baseline drift')
if endpoints['public_encrypted_dns_tls_termination'] != 'same-host path-restricted reverse proxy; AdGuard internal TLS listener remains disabled':
    fail('TLS termination topology drift')

# Re-run the predecessor bundle's deterministic self-verifier.
proc = subprocess.run([sys.executable, str(BUNDLE_DIR / 'verify_bundle.py')], cwd=ROOT, text=True, capture_output=True)
if proc.returncode != 0 or 'TSK_0413_BUNDLE_VERIFY=PASS' not in proc.stdout:
    fail('TSK-0413 bundle self-verification failed: ' + proc.stdout + proc.stderr)

# ACC-0446 coverage and non-inference guard.
required_contract_fragments = [
    '**fresh Ubuntu 24.04 LTS**',
    'approximately **30 minutes**',
    '## 3. RTO measurement contract',
    '### Host and packages',
    '### AdGuard Home',
    '### Configuration and protected state',
    '### Network and firewall',
    '### DNS endpoint and encrypted protocols',
    '### TLS',
    '### Filters and allowlist',
    '### Privacy',
    '### Security and administration',
    '### Startup and service management',
    '### Verification and health',
    '## 8. Failure-safe behavior and rollback',
    '## 9. Required recovery outputs/evidence',
    '## 10. Explicit exclusions',
    'No timed clean-server drill is claimed by TSK-0446.',
    'Azure VM creation, subscription/resource-group setup, region selection, network-resource creation, and other Azure control-plane provisioning are outside the recovery clock',
    'final safe-field projection matches the current TSK-0413 bundle',
    'persistent raw query logging: **off**',
    'file query logging: **off**',
    'minimum anonymized aggregate statistics, enabled with **24-hour / `1d` retention**',
    'client-IP anonymization: **on**',
    'ECS: **off**',
    'browsing/query/activity-history metrics: prohibited',
    'same-host path-restricted reverse proxy',
    '`https://dns10.quad9.net/dns-query`',
    '`https://dns.usesafeweb.com/dns-query`',
    'official `AdGuard DNS filter` (`filter_1.txt`)',
    'A backup restore, process `active` state, or localhost-only DNS response is insufficient by itself.',
]
for fragment in required_contract_fragments:
    require(contract, fragment, CONTRACT.name)

# Historical backup scope is explicitly reconciled rather than silently treated as current desired state.
require(backup_policy, 'statistics `false`', 'BACKUP_SCOPE_POLICY.md')
require(contract, 'its recorded historical live preflight required `statistics=false` before the 2026-09-01 owner approval', CONTRACT.name)
require(contract, 'any later backup-creation workflow that still requires `statistics=false` must be revalidated/reconciled before being used against the new desired state', CONTRACT.name)

# Contract must not assert that target execution has already happened.
for forbidden in [
    'clean-server recovery completed within 30 minutes',
    'actual clean-server recovery: PASS',
    'measured clean-server recovery: PASS',
]:
    if forbidden.lower() in contract.lower():
        fail('forbidden target-execution inference: ' + forbidden)

print('TSK_0446_RECOVERY_SCOPE_CONTRACT_VERIFY=PASS')
print('contract_version=1.0.0')
print('dependency=TSK-0413')
print('bundle_version=1.0.0')
print('adguard_home_version=v0.107.79')
print('rto_target=approximately_30_minutes')
print('target_timed_drill_claimed=false')
