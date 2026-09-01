#!/usr/bin/env python3
import csv
import re
import subprocess
from pathlib import Path

TASK = 'TSK-0238'
ARTIFACT = Path('TSK_0238_LEAN_OPERATIONAL_OWNERSHIP_ONCALL_ESCALATION_MODEL_2026-09-01.md')
EXPECTED_ARTIFACT_BLOB = '069d015435f4a0d45a1b3326f7e2d210712b4cb1'
EXPECTED_DEPS = ['TSK-0231']
EXPECTED_ACCEPTANCE = (
    'Model identifies primary/backup owner, routine cadence, incident escalation, human-only decisions, coverage gaps, '
    'and activation triggers for additional staffing/services.'
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
assert norm(row.get('Title')) == 'Define lean operational ownership and on-call/escalation model'
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
assert norm(row.get('Acceptance_ID')) == 'ACC-0238'
assert norm(row.get('Verification_ID')) == 'VER-0238'
assert norm(row.get('Evidence_ID')) == 'EVD-0238'
assert norm(row.get('Acceptance_Criteria')) == EXPECTED_ACCEPTANCE

assert re.search(r'^##\s+TSK-0231(?:\s*/[^\n#]+)?\s+current accepted stable state\b', state, flags=re.M | re.I)
assert not re.search(r'^##\s+TSK-0238(?:\s*/[^\n#]+)?\s+current accepted stable state\b', state, flags=re.M | re.I)

reg = Path('Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md').read_text(encoding='utf-8')
rr = next(line for line in reg.splitlines() if line.startswith('| TSK-0238 |'))
cells = [c.strip() for c in rr.strip().strip('|').split('|')]
assert cells[0] == 'TSK-0238'
assert cells[1] == 'VER-0238'
assert cells[3] == 'EVD-0238'
assert cells[5] == 'ACC-0238'
assert cells[6] == EXPECTED_ACCEPTANCE

linked = {
    'Plans/Master/Registers/REQUIREMENTS.md': ['REQ-0018', 'REQ-0019'],
    'Plans/Master/Registers/CONSTRAINTS.md': ['CON-0007', 'CON-0008'],
    'Plans/Master/Registers/RISKS.md': ['RSK-0001', 'RSK-0005'],
    'Plans/Master/Registers/INTERFACES.md': ['INT-0006', 'INT-0007'],
}
for path, ids in linked.items():
    source_lines = Path(path).read_text(encoding='utf-8').splitlines()
    for item_id in ids:
        matches = [line for line in source_lines if line.startswith(f'| {item_id} |')]
        assert len(matches) == 1, (path, item_id, len(matches))

required_markers = [
    '**Version:** 1.0.0',
    '**Acceptance:** ACC-0238 / VER-0238 / EVD-0238',
    '**Primary operational duty owner: SRE / Operations function.**',
    '**Backup operational duty owner: Project Owner.**',
    '## 3. Routine operating cadence',
    '## 4. Incident escalation model',
    '### SEV-1',
    '### SEV-2',
    '### SEV-3',
    '## 5. Human-only / owner-controlled decisions',
    '## 6. Current coverage gaps',
    '## 7. Evidence triggers for additional staffing or services',
    'Crossing a trigger opens a **review**, not an automatic hire, purchase, contract or organizational change.',
    'no independently verified second human delegate is currently assigned',
    'no 24/7 human on-call or staffed customer-support promise',
    '`RSK-0001` remains OPEN',
    '`INT-0007` still requires later inspection',
    'persistent identifiable query/file logging remains OFF',
    'identifiable per-client statistics remain OFF/excluded',
    '500-active-user milestone',
    'not an automatic hiring, legal, expansion or spend threshold',
    'no real England participant may be activated',
    '## 10. Non-inference',
]
for marker in required_markers:
    assert marker in artifact, marker

# The six acceptance dimensions must be independently visible and concrete.
acceptance_sections = {
    'primary_owner': r'### 2\.1 Primary operational owner',
    'backup_owner': r'### 2\.2 Backup operational owner',
    'cadence': r'## 3\. Routine operating cadence',
    'incident_escalation': r'## 4\. Incident escalation model',
    'human_only': r'## 5\. Human-only / owner-controlled decisions',
    'coverage_gaps': r'## 6\. Current coverage gaps',
    'staffing_triggers': r'## 7\. Evidence triggers for additional staffing or services',
}
for name, pattern in acceptance_sections.items():
    assert re.search(pattern, artifact, flags=re.M), name

# Cadence and escalation are operationally usable, not label-only.
assert artifact.count('| Event-driven / continuous when active |') == 1
assert artifact.count('| Daily during active production ramp or active material incident |') == 1
assert artifact.count('| Weekly during development/readiness and active production |') == 1
assert artifact.count('| Monthly |') == 1
assert artifact.count('| Quarterly or after material topology/security/operations change |') == 1
assert artifact.count('**Default action:**') == 3

# Staffing/service triggers must be explicit and non-automatic.
trigger_names = [
    'Human-authority continuity trigger',
    'Support-load trigger',
    'Incident-load trigger',
    'Security/privacy expertise trigger',
    'Availability/recovery trigger',
    'Capacity/operations trigger',
    'Vendor/service trigger',
    'Coverage-hours trigger',
    '500-active-user review trigger',
]
for name in trigger_names:
    assert name in artifact, name

# Retained owner boundaries from current CR-0007 authority must not be silently erased.
owner_markers = [
    'named official-market activation',
    'organizational/entity/formalization decisions',
    'entering a new contract',
    'regulated fees',
    'banking or merchant identity decisions',
    'legal attestations, signatures',
    'material or unbudgeted spend',
    'strategic modify/pivot/pause/stop/transfer/resume decisions',
    'material change to frozen product/scope/policy boundaries',
    'owner-managed Azure control-plane provisioning/configuration',
]
for marker in owner_markers:
    assert marker in artifact, marker

# Routine autonomy and product/support boundaries remain intact.
for marker in [
    'routine objective work inside frozen scope is AI-autonomous where current Action Authority permits it',
    'ordinary user problems are designed toward self-service',
    'Routine safe remediation remains with the primary operational function wherever authority permits.',
    'Repeated ordinary human help is primarily a product/UX/automation defect',
    'The existence of a serious incident does **not** automatically make every technical containment/recovery step human-only.',
]:
    assert marker in artifact, marker

# This design cannot self-certify downstream reality or consequential acts.
for forbidden_claim in [
    'RSK-0001 is CLOSED',
    '24/7 human coverage is active',
    'staffing is approved',
    'a contractor is approved',
    'production monitoring is implemented',
    'real England participant processing is approved',
    'LG-07 is PASS',
    'LG-08 is PASS',
    'LG-09 is PASS',
    'final legal compliance is established',
]:
    assert forbidden_claim not in artifact

print('TSK0238_WBS_CONTRACT=PASS')
print('TSK0238_DEPENDENCY=PASS')
print('TSK0238_ACC_REGISTER=PASS')
print('TSK0238_LINKED_CONTROLS=PASS')
print('TSK0238_ARTIFACT_BLOB=PASS')
print('TSK0238_PRIMARY_BACKUP_OWNERS=PASS')
print('TSK0238_ROUTINE_CADENCE=PASS')
print('TSK0238_INCIDENT_ESCALATION=PASS')
print('TSK0238_HUMAN_BOUNDARIES=PASS')
print('TSK0238_COVERAGE_GAPS=PASS')
print('TSK0238_STAFFING_SERVICE_TRIGGERS=9')
print('TSK0238_PRIVACY_LEGAL_FENCES=PASS')
print('TSK0238_NONINFERENCE=PASS')
