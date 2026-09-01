#!/usr/bin/env python3
import csv
import re
import subprocess
from pathlib import Path

TASK = 'TSK-0485'
ARTIFACT = Path('TSK_0485_END_TO_END_THREAT_ABUSE_MODEL_2026-09-01.md')
EXPECTED_ARTIFACT_BLOB = '373ac62ba1f244328e7d8e52ae6648d72e5a5ed7'
EXPECTED_WBS_BLOB = 'b27a0c5df2f5636d8ed71051e9e26a68959a2616'
EXPECTED_DEPS = ['TSK-0231']
EXPECTED_ACCEPTANCE = (
    'Threat model covers the accountless web path plus the active Version-1 account/session/dashboard surface: '
    'XSS/CSRF/session theft/account takeover, IDOR/cross-parent access, ClientID/ownership confusion, '
    'auth/provider/datastore failure, admin/API abuse, DNS amplification, dependency/supply-chain, CI/CD/secrets, '
    'deletion/recovery and privacy leakage. High/critical paths have prevention/detection/recovery controls and '
    'release-blocking tests.'
)


def norm(v):
    return (v or '').strip()


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


artifact = ARTIFACT.read_text(encoding='utf-8')
state = Path('CURRENT_STATE.md').read_text(encoding='utf-8')

assert git('rev-parse', 'HEAD:Plans/Master/WBS/master-wbs.csv') == EXPECTED_WBS_BLOB
assert git('rev-parse', f'HEAD:{ARTIFACT.as_posix()}') == EXPECTED_ARTIFACT_BLOB

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = next(r for r in rows if norm(r.get('Task_ID')) == TASK)
assert norm(row.get('Title')) == 'Perform end-to-end threat and abuse modeling'
assert norm(row.get('Lifecycle_Stage')) == 'L5'
assert norm(row.get('Priority')) == 'MEDIUM'
assert norm(row.get('AI_Capability_A0_A4')) == 'A3'
assert norm(row.get('Action_Authority')) == 'AUTO_ALLOWED'
assert norm(row.get('Plan_Status')) == 'PLANNED'
assert re.findall(r'TSK-\d{4}', row.get('Dependencies') or '') == EXPECTED_DEPS
assert set(re.findall(r'REQ-\d{4}', row.get('Requirement_Reference') or '')) == {'REQ-0055', 'REQ-0056', 'REQ-0057'}
assert set(re.findall(r'CON-\d{4}', row.get('Requirement_Reference') or '')) == {'CON-0009', 'CON-0028'}
assert set(re.findall(r'RSK-\d{4}', row.get('Risk_Reference') or '')) == {'RSK-0007'}
assert set(re.findall(r'INT-\d{4}', row.get('Interface_Reference') or '')) == {'INT-0015'}
assert norm(row.get('Acceptance_ID')) == 'ACC-0485'
assert norm(row.get('Verification_ID')) == 'VER-0485'
assert norm(row.get('Evidence_ID')) == 'EVD-0485'
assert norm(row.get('Acceptance_Criteria')) == EXPECTED_ACCEPTANCE

assert re.search(r'^##\s+TSK-0231(?:\s*/[^\n#]+)?\s+current accepted stable state\b', state, flags=re.M | re.I)
assert not re.search(r'^##\s+TSK-0485(?:\s*/[^\n#]+)?\s+current accepted stable state\b', state, flags=re.M | re.I)

reg = Path('Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md').read_text(encoding='utf-8')
rr = next(line for line in reg.splitlines() if line.startswith('| TSK-0485 |'))
cells = [c.strip() for c in rr.strip().strip('|').split('|')]
assert cells[0] == 'TSK-0485'
assert cells[1] == 'VER-0485'
assert cells[3] == 'EVD-0485'
assert cells[5] == 'ACC-0485'
assert cells[6] == EXPECTED_ACCEPTANCE

linked = {
    'Plans/Master/Registers/REQUIREMENTS.md': ['REQ-0055', 'REQ-0056', 'REQ-0057'],
    'Plans/Master/Registers/CONSTRAINTS.md': ['CON-0009', 'CON-0028'],
    'Plans/Master/Registers/RISKS.md': ['RSK-0007'],
    'Plans/Master/Registers/INTERFACES.md': ['INT-0015'],
}
for path, ids in linked.items():
    source_lines = Path(path).read_text(encoding='utf-8').splitlines()
    for item_id in ids:
        matches = [line for line in source_lines if line.startswith(f'| {item_id} |')]
        assert len(matches) == 1, (path, item_id, len(matches))

required_markers = [
    '**Version:** 1.0.0',
    '**Acceptance:** ACC-0485 / VER-0485 / EVD-0485',
    'accountless web/setup/protection journey',
    'optional parent account/session',
    '`ClientID` is an opaque DNS-control reference and is never authentication or authorization',
    'only fresh qualifying technical evidence may produce `protected_verified`',
    'persistent identifiable DNS query/file logging remains OFF',
    'identifiable per-client statistics remain OFF/excluded',
    'no automatic anonymous-to-account linkage',
    'AI action authority remains independent of infrastructure/server privilege',
    '## 3. Assets, actors and trust boundaries',
    '## 4. Threat and abuse catalogue',
    '## 5. High/Critical control and release-blocking rules',
    '## 6. Required downstream verification mapping',
    '## 7. Current gaps and blockers carried forward',
    '## 9. Acceptance disposition',
    'CONTROL PLAN DEFINED; IMPLEMENTATION/RETEST REQUIRED',
    '`RSK-0001` remains OPEN',
    '`INT-0007`',
    '**Non-inference:**',
]
for marker in required_markers:
    assert marker in artifact, marker

# Required trust boundaries are explicit.
for tb in ['TB-WEB', 'TB-ANON', 'TB-AUTH', 'TB-OWN', 'TB-ADG', 'TB-DNS', 'TB-OPS', 'TB-CI', 'TB-EXT', 'TB-REC']:
    assert f'**{tb}:**' in artifact, tb

# Parse the canonical threat catalogue rows.
threat_rows = []
for line in artifact.splitlines():
    if re.match(r'^\| TM-\d{2} \|', line):
        c = [v.strip() for v in line.strip().strip('|').split('|')]
        assert len(c) == 9, (c[0], len(c))
        threat_rows.append(c)
assert len(threat_rows) == 30, len(threat_rows)
ids = [c[0] for c in threat_rows]
assert ids == [f'TM-{i:02d}' for i in range(1, 31)], ids

critical = 0
high = 0
for c in threat_rows:
    tid, severity, surface, scenario, prevention, detection, recovery, blocking_test, status = c
    assert severity in {'Critical', 'High', 'Medium', 'Low'}, (tid, severity)
    assert surface and scenario
    if severity in {'Critical', 'High'}:
        if severity == 'Critical':
            critical += 1
        else:
            high += 1
        for name, value in [
            ('prevention', prevention),
            ('detection', detection),
            ('recovery', recovery),
            ('blocking_test', blocking_test),
        ]:
            assert len(value) >= 40, (tid, name, value)
            assert value.lower() not in {'n/a', 'none', 'tbd', 'todo'}
        assert status == 'CONTROL PLAN DEFINED; IMPLEMENTATION/RETEST REQUIRED', (tid, status)
assert critical > 0 and high > 0
assert critical + high == len(threat_rows)

# Exact ACC category coverage, with dedicated threat rows/phrases.
category_checks = {
    'xss': ['TM-01', 'XSS'],
    'csrf': ['TM-02', 'CSRF'],
    'session_theft': ['TM-03', 'Session theft'],
    'account_takeover': ['TM-04', 'account takeover'],
    'idor_cross_parent': ['TM-05', 'IDOR / cross-parent'],
    'clientid_ownership': ['TM-06', '`ClientID`'],
    'auth_provider_failure': ['TM-07', 'Authentication-provider outage'],
    'datastore_failure': ['TM-08', 'Datastore timeout/partial write'],
    'admin_api_abuse': ['TM-09', 'arbitrary `/control/*`'],
    'dns_amplification': ['TM-10', 'DNS resolver abuse/amplification/resource/cost exhaustion'],
    'dependency_supply_chain': ['TM-12', 'Malicious/compromised dependency'],
    'cicd_secrets': ['TM-13', 'Workflow injection'],
    'deletion_recovery': ['TM-15', 'Partial account/device deletion'],
    'privacy_leakage': ['TM-16', 'prohibited identifiable DNS/domain browsing history'],
}
for name, markers in category_checks.items():
    for marker in markers:
        assert marker in artifact, (name, marker)

# Additional end-to-end invariants that prevent false-safety and authority failures.
for marker in [
    'TM-17', 'J0/J1 identifier enumeration',
    'TM-18', 'Forged/tampered configuration',
    'TM-19', 'Private Relay',
    'TM-23', 'root/server/API capability',
    'TM-30', 'conflates account/device registration',
    'No exploitable Critical/High open path may be released merely because this threat model exists.',
    'Authentication alone, opaque IDs or `ClientID` do not authorize a device operation.',
    'A lost, stale, conflicting or tampered verification path downgrades the protection state',
    'Public/browser access, arbitrary `/control` passthrough and browser-held administration secrets are release blockers.',
    'No-history privacy is a security control.',
    'Technical privilege never creates owner authority.',
]:
    assert marker in artifact, marker

# The design must surface non-PASS downstream prerequisites rather than self-certify them.
for marker in [
    '`TSK-0356` authentication/server-session architecture is not yet PASS',
    '`TSK-0232` parent/device ownership authorization model is not yet PASS',
    '`TSK-0410` typed/allowlisted AdGuard adapter and ClientID lifecycle contract is not yet PASS',
    'production observability, alert routes and runbooks are not yet fully implemented/rehearsed',
    '`RSK-0001` remains OPEN',
    'TSK-0240 remains planning-DEFERRED',
]:
    assert marker in artifact, marker

# Supporting standards are pinned by explicit source names/URLs, without being treated as project authority.
for url in [
    'https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html',
    'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html',
    'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html',
    'https://docs.github.com/en/actions/reference/security/secure-use',
    'https://docs.github.com/en/actions/concepts/security/secrets',
]:
    assert url in artifact, url

for forbidden_claim in [
    'RSK-0007 is CLOSED',
    'RSK-0001 is CLOSED',
    'all controls are implemented',
    'all controls are deployed',
    'production monitoring is implemented',
    'penetration testing is complete',
    'LG-07 is PASS',
    'LG-08 is PASS',
    'LG-09 is PASS',
    'real participant processing is approved',
    'final legal compliance is established',
]:
    assert forbidden_claim not in artifact

print('TSK0485_WBS_CONTRACT=PASS')
print('TSK0485_DEPENDENCY=PASS')
print('TSK0485_ACC_REGISTER=PASS')
print('TSK0485_LINKED_CONTROLS=PASS')
print('TSK0485_ARTIFACT_BLOB=PASS')
print(f'TSK0485_THREAT_ROWS={len(threat_rows)}')
print(f'TSK0485_CRITICAL_ROWS={critical}')
print(f'TSK0485_HIGH_ROWS={high}')
print('TSK0485_REQUIRED_ACC_CATEGORIES=PASS')
print('TSK0485_HIGH_CRITICAL_PDR_TESTS=PASS')
print('TSK0485_TRUST_BOUNDARIES=10')
print('TSK0485_PRIVACY_TRUTH_AUTHORITY_INVARIANTS=PASS')
print('TSK0485_DOWNSTREAM_GAPS=PASS')
print('TSK0485_NONINFERENCE=PASS')
