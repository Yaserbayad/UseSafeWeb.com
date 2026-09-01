#!/usr/bin/env python3
import csv
import re
import subprocess
from pathlib import Path

TASK = 'TSK-0231'
ARTIFACT = Path('TSK_0231_ARCHITECTURE_DECISIONS_AND_REJECTED_ALTERNATIVES_2026-09-01.md')
EXPECTED_ARTIFACT_BLOB = '9479f19f44a94fe37671ea38e4ec96c170687181'
EXPECTED_DEPS = ['TSK-0355', 'TSK-0411', 'TSK-0233', 'TSK-0444', 'TSK-0354']
EXPECTED_ACCEPTANCE = (
    'Every material decision has context, options, decision, rationale, consequences, evidence, owner, review trigger, '
    'and links to requirements/risks.'
)


def norm(v):
    return (v or '').strip()


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


artifact = ARTIFACT.read_text(encoding='utf-8')
state = Path('CURRENT_STATE.md').read_text(encoding='utf-8')

assert git('rev-parse', f'HEAD:{ARTIFACT.as_posix()}') == EXPECTED_ARTIFACT_BLOB

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = next(r for r in rows if norm(r.get('Task_ID')) == TASK)
assert norm(row.get('Title')) == 'Record architecture decisions and rejected alternatives'
assert norm(row.get('Lifecycle_Stage')) == 'L5'
assert norm(row.get('Priority')) == 'MEDIUM'
assert norm(row.get('AI_Capability_A0_A4')) == 'A3'
assert norm(row.get('Action_Authority')) == 'AUTO_ALLOWED'
assert norm(row.get('Plan_Status')) == 'PLANNED'
assert re.findall(r'TSK-\d{4}', row.get('Dependencies') or '') == EXPECTED_DEPS
assert set(re.findall(r'REQ-\d{4}', row.get('Requirement_Reference') or '')) == {'REQ-0018', 'REQ-0019'}
assert set(re.findall(r'CON-\d{4}', row.get('Requirement_Reference') or '')) == {'CON-0007', 'CON-0008'}
assert set(re.findall(r'RSK-\d{4}', row.get('Risk_Reference') or '')) == {'RSK-0001'}
assert set(re.findall(r'INT-\d{4}', row.get('Interface_Reference') or '')) == {'INT-0006', 'INT-0007'}
assert norm(row.get('Acceptance_ID')) == 'ACC-0231'
assert norm(row.get('Verification_ID')) == 'VER-0231'
assert norm(row.get('Evidence_ID')) == 'EVD-0231'
assert norm(row.get('Acceptance_Criteria')) == EXPECTED_ACCEPTANCE

for dep in EXPECTED_DEPS:
    assert re.search(rf'^##\s+{dep}(?:\s*/[^\n#]+)?\s+current accepted stable state\b', state, flags=re.M | re.I), dep
assert not re.search(r'^##\s+TSK-0231(?:\s*/[^\n#]+)?\s+current accepted stable state\b', state, flags=re.M | re.I)

reg = Path('Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md').read_text(encoding='utf-8')
rr = next(line for line in reg.splitlines() if line.startswith('| TSK-0231 |'))
cells = [c.strip() for c in rr.strip().strip('|').split('|')]
assert cells[0] == 'TSK-0231'
assert cells[1] == 'VER-0231'
assert cells[3] == 'EVD-0231'
assert cells[5] == 'ACC-0231'
assert cells[6] == EXPECTED_ACCEPTANCE

linked = {
    'Plans/Master/Registers/REQUIREMENTS.md': ['REQ-0018', 'REQ-0019'],
    'Plans/Master/Registers/CONSTRAINTS.md': ['CON-0007', 'CON-0008'],
    'Plans/Master/Registers/RISKS.md': ['RSK-0001'],
    'Plans/Master/Registers/INTERFACES.md': ['INT-0006', 'INT-0007'],
}
for path, ids in linked.items():
    source_lines = Path(path).read_text(encoding='utf-8').splitlines()
    for item_id in ids:
        matches = [line for line in source_lines if line.startswith(f'| {item_id} |')]
        assert len(matches) == 1, (path, item_id, len(matches))

required_global = [
    '**Version:** 1.0.0',
    'ADR index/consolidation, not a second mutable decision register, WBS, runtime state store or checkpoint',
    'It does not create a new owner decision or silently modify scope.',
    '`RSK-0001` remains OPEN',
    '`INT-0007` still requires later inspection',
    'no J1-to-account migration or linkage',
    '`ClientID` is an opaque DNS-control reference and is **never authentication or authorization**',
    'persistent identifiable query/file logging OFF',
    'no persistent staging unless later evidence justifies it',
    'ACC-0231 / VER-0231 / EVD-0231',
    '**Non-inference:** this record does not itself make TSK-0231 PASS.',
]
for marker in required_global:
    assert marker in artifact, marker

adr_matches = list(re.finditer(r'^## ADR-(\d{2}) — .+$', artifact, flags=re.M))
assert [m.group(1) for m in adr_matches] == [f'{i:02d}' for i in range(1, 11)]
required_fields = [
    '**Context:**',
    '**Options:**',
    '**Decision:**',
    '**Rationale:**',
    '**Rejected alternatives:**',
    '**Consequences:**',
    '**Evidence:**',
    '**Owner:**',
    '**Review trigger:**',
    '**Links to requirements/risks:**',
]
for idx, match in enumerate(adr_matches):
    end = adr_matches[idx + 1].start() if idx + 1 < len(adr_matches) else artifact.index('\n## 2. Rejected-alternative cross-check')
    body = artifact[match.end():end]
    for field in required_fields:
        assert field in body, (match.group(0), field)
    links = re.search(r'\*\*Links to requirements/risks:\*\*(.*)', body)
    assert links and 'RSK-0001' in links.group(1), match.group(0)

# Material decision markers must remain aligned to the current dependency architecture.
architecture_markers = [
    'one production-capable TypeScript + Next.js full-stack application under `/website`',
    'full Phone → Internet → Services → truthful Protection Map/recovery core without login',
    'hard non-sliding maximum 24-hour lifetime',
    'concrete datastore product/runtime selection',
    '`dns.usesafeweb.com`',
    '`https://dns.usesafeweb.com/dns-query`',
    'server-only behind narrow typed/allowlisted application operations',
    'No product schema/store for DNS queries, domains, visited URLs, browsing/top-domain history or child activity',
    'PROD plus disposable CI/ephemeral synthetic/test environments',
    'separate web/app VM and DNS/AdGuard VM boundary',
    'Keep `RSK-0001` OPEN',
]
for marker in architecture_markers:
    assert marker in artifact, marker

# Explicit rejected-alternative coverage from the accepted dependency set/current decisions.
rejected_markers = [
    'Mandatory login is rejected',
    'automatic promotion',
    'Premature datastore selection',
    'Public plain DNS and public administration are rejected',
    'Browser-admin access, arbitrary control passthrough and ClientID-based authorization are rejected',
    'Browsing history, top-domain product metrics, persistent identifiable query logs',
    'Mandatory persistent staging and a separate mandatory pilot lifecycle are superseded',
    'Mandatory Docker/Kubernetes',
    'Self-certifying compliance from design documents',
]
for marker in rejected_markers:
    assert marker in artifact, marker

# Privacy and non-inference fences.
for forbidden_claim in [
    'RSK-0001 is CLOSED',
    'LG-07 is PASS',
    'LG-08 is PASS',
    'LG-09 is PASS',
    'final legal compliance is established',
    'real England participant processing is approved',
]:
    assert forbidden_claim not in artifact

assert 'These are architecture consequences of current authority, not independent new owner decisions.' in artifact
assert 'does **not** infer implementation, deployment, LG-07/LG-08/LG-09 PASS, participant activation, production processing authority, final legal compliance, public launch or downstream task PASS' in artifact

print('TSK0231_WBS_CONTRACT=PASS')
print('TSK0231_DEPENDENCIES=PASS')
print('TSK0231_ACC_REGISTER=PASS')
print('TSK0231_LINKED_CONTROLS=PASS')
print('TSK0231_ARTIFACT_BLOB=PASS')
print('TSK0231_ADR_COUNT=10')
print('TSK0231_ADR_FIELD_COMPLETENESS=PASS')
print('TSK0231_REJECTED_ALTERNATIVES=PASS')
print('TSK0231_DERIVED_NOT_AUTHORITY=PASS')
print('TSK0231_PRIVACY_FENCES=PASS')
print('TSK0231_RSK0001_NONINFERENCE=PASS')
print('TSK0231_INT0007_RUNTIME_FENCE=PASS')
