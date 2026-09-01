from __future__ import annotations
import csv
from pathlib import Path

wbs = Path('Plans/Master/WBS/master-wbs.csv').read_text(encoding='utf-8-sig')
rows = {r['Task_ID']: r for r in csv.DictReader(wbs.splitlines())}
r = rows['TSK-0408']
decisions = Path('Plans/Master/Registers/DECISIONS_TRIGGERS.md').read_text(encoding='utf-8')
old = Path('TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md').read_text(encoding='utf-8')
new = Path('TSK_0408_POST_CR0007_REVALIDATION_EVIDENCE_2026-09-01.md').read_text(encoding='utf-8')

assert r['Acceptance_ID'] == 'ACC-0408'
assert r['Verification_ID'] == 'VER-0408'
assert r['Evidence_ID'] == 'EVD-0408'
assert r['AI_Capability_A0_A4'] == 'A3'
assert r['Action_Authority'] == 'AUTO_ALLOWED'
assert r['Acceptance_Criteria'] == 'Hostname/DoH path/profile naming, certificates, verification, removal, fallback, and environment separation are clear; no false universal FQDN workflow.'

assert '| DEC-0053 |' in decisions
assert '| DEC-0054 |' in decisions
assert 'no mandatory pilot or staging lifecycle/environment' in decisions
assert 'local/dev/CI/synthetic/device/network/security/privacy/accessibility/performance/recovery/rollback verification remains mandatory' in decisions

for token in [
    'dns.usesafeweb.com',
    'https://dns.usesafeweb.com/dns-query',
    'UseSafeWeb DNS',
    'Android native Private DNS',
    'Apple',
    'browsing/query history',
]:
    assert token in old

required = [
    'Superseded lifecycle/environment semantics',
    'There is no mandatory separate pilot or staging service.',
    'non-production validation evidence',
    'No FQDN, path, profile identifier, callback URL or support endpoint may be invented',
    'must never become an arbitrary `/control` proxy',
    'core DNS protection login-dependent',
    'Candidate result: TSK-0408 = PASS',
]
for token in required:
    assert token in new, token

assert 'Current environment/evidence contract' in new
current = new.split('## Current environment/evidence contract',1)[1].split('## ACC-0408 mapping',1)[0]
assert 'controlled-pilot endpoint' not in current
assert 'mandatory pilot ->' not in current

print('TSK_0408_POST_CR0007_REVALIDATION_VERIFIER=PASS')
