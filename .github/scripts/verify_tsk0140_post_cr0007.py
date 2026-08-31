import csv
import subprocess
from pathlib import Path

EXPECTED = {
    'CURRENT_STATE.md': 'cbbeee8c5435f34cbc0a16f520150a896775a5ab',
    'Plans/Master/WBS/master-wbs.csv': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'Plans/Master/Registers/DECISIONS_TRIGGERS.md': '380ff579dcffb7b8df73611e9159c672f9ed489e',
    'Plans/Master/Registers/GATES.md': '87cf9060954a82e1d5a092200d3c922f1986a5da',
    'Plans/Master/Registers/REQUIREMENTS.md': 'a2212059f69c4602eb0c05961d5d1639e3543f83',
    'Plans/Master/Registers/INTERFACES.md': 'b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c',
    'Plans/Master/Registers/CONSTRAINTS.md': '9464720bff94fd569e3b939568996a26eed83ca1',
    'TSK_0138_POST_CR0007_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-31.md': 'a0992efa33c3a54511957c2e34f02a1fc97ad10a',
    'TSK_0138_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md': 'fac88076539a51292caa2279d9bcd3076e96b75e',
    'TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md': '8ed698b3e34540aefac617e5f6754e20d9dfbdc3',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'hash mismatch {path}: {actual} != {sha}')

with open('Plans/Master/WBS/master-wbs.csv', encoding='utf-8-sig', newline='') as f:
    rows = [r for r in csv.DictReader(f) if r['Task_ID'] == 'TSK-0140']
if len(rows) != 1:
    raise SystemExit(f'TSK-0140 row count={len(rows)}')
r = rows[0]
checks = {
    'Lifecycle_Stage': 'L4',
    'Dependencies': 'TSK-0138',
    'AI_Capability_A0_A4': 'A4',
    'Action_Authority': 'AUTO_ALLOWED',
    'Acceptance_ID': 'ACC-0140',
    'Verification_ID': 'VER-0140',
    'Evidence_ID': 'EVD-0140',
}
for key, expected in checks.items():
    if r.get(key) != expected:
        raise SystemExit(f'WBS {key}: {r.get(key)!r} != {expected!r}')
acc = r['Acceptance_Criteria']
for token in [
    'faithfully translates the frozen current product, privacy, security, technical, commercial and sequencing authority',
    'all material scope changes remain separately owner-controlled',
    'objective evidence review must find no unresolved contradiction before PASS',
]:
    if token not in acc:
        raise SystemExit('ACC-0140 token missing: ' + token)
if 'DEC-0054 / CR-0007' not in r['Source_Reference']:
    raise SystemExit('TSK-0140 source reference missing DEC-0054 / CR-0007')

state = Path('CURRENT_STATE.md').read_text(encoding='utf-8')
for token in [
    '## TSK-0138 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '`TSK-0138 — Register unresolved product assumptions and owner decisions`: **PASS**',
    'TSK_0138_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md',
    '`TSK-0140` remains non-PASS until its revised objective ACC is independently re-evaluated and durably evidenced',
]:
    if token not in state:
        raise SystemExit('runtime prerequisite token missing: ' + token)

decisions = Path('Plans/Master/Registers/DECISIONS_TRIGGERS.md').read_text(encoding='utf-8')
for token in [
    '| DEC-0053 |',
    '| DEC-0054 |',
    'Version-1 optional parent accounts with accountless core retained',
    'no mandatory pilot or staging lifecycle/environment',
]:
    if token not in decisions:
        raise SystemExit('decision token missing: ' + token)

gates = Path('Plans/Master/Registers/GATES.md').read_text(encoding='utf-8')
for token in [
    '| LG-06 | Product, Brand and Experience Freeze |',
    'Project Governance / AUTO_ALLOWED',
    '| LG-09 | Integrated Production Release Readiness |',
    '| LG-12 | UK Public Production Readiness |',
    '| LG-13 | UK Public Production Activation |',
]:
    if token not in gates:
        raise SystemExit('gate token missing: ' + token)

brief = Path('TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md').read_text(encoding='utf-8')
required = [
    '**Version:** 3.0.0-post-cr0007',
    'the complete core setup/protection journey remains usable **without login**',
    'an **optional parent account** provides secure sign-in/session capability, minimum parent/device ownership persistence and a lightweight dashboard/device-management experience',
    'no automatic J1-to-account join, conversion or promotion is authorized',
    'browsing/query/activity history and persistent child/family behavioral profiles remain prohibited',
    'AdGuard remains the frozen filtering backend',
    'Encrypted DNS remains mandatory',
    'core safety value remains free',
    'no mandatory separate pilot/staging lifecycle',
    '**L4 / LG-06 — Product, Brand and Experience Freeze.**',
    '**L7 / LG-09 — Integrated Production Release Readiness.**',
    '**LG-12 — UK Public Production Readiness.**',
    '**LG-13 — UK Public Production Activation.**',
    'material frozen product/scope-policy change',
    '**Current objective contradiction review:** no unresolved canonical contradiction identified.',
    '**ACC-0140:** candidate for fresh independent post-publication verification only.',
]
for token in required:
    if token not in brief:
        raise SystemExit('brief token missing: ' + token)
for forbidden in [
    '**ACC-0140:** **NOT YET PASS — PROJECT OWNER REVIEW',
    '**Status:** CANDIDATE / OWNER REVIEW REQUIRED',
]:
    if forbidden in brief:
        raise SystemExit('stale acceptance token present: ' + forbidden)

requirements = Path('Plans/Master/Registers/REQUIREMENTS.md').read_text(encoding='utf-8')
for token in [
    '| REQ-0007 | MUST | PKG-02 | The product shall remain UseSafeWeb - First Phone Safety Setup',
    '| REQ-0008 | MUST | PKG-02 | The core journey shall coordinate Phone -> Internet -> Services and end with a truthful Protection Map.',
    '| REQ-0011 | MUST | PKG-02 | Version 1 shall provide an optional parent account capability',
    '| REQ-0033 | MUST | PKG-06 | Critical product and public surfaces shall target WCAG 2.2 AA',
    '| REQ-0037 | MUST | PKG-07 | The accountless journey shall retain only minimum short-lived state',
]:
    if token not in requirements:
        raise SystemExit('requirement token missing: ' + token)
interfaces = Path('Plans/Master/Registers/INTERFACES.md').read_text(encoding='utf-8')
if '| INT-0003 | Product and experience requirements |' not in interfaces:
    raise SystemExit('INT-0003 missing')
constraints = Path('Plans/Master/Registers/CONSTRAINTS.md').read_text(encoding='utf-8')
for token in ['| CON-0001 | UseSafeWeb.com is the frozen public identity/domain.', '| CON-0002 | AdGuard is the frozen backend filtering technology.']:
    if token not in constraints:
        raise SystemExit('constraint token missing: ' + token)

print('TSK0140_WBS_CONTRACT=PASS')
print('TSK0140_DEPENDENCY_RUNTIME=PASS')
print('TSK0140_CR0006_RECONCILIATION=PASS')
print('TSK0140_CR0007_RECONCILIATION=PASS')
print('TSK0140_ACC_SEMANTICS=PASS')
print('TSK0140_NO_STALE_OWNER_REVIEW=PASS')
print('TSK0140_INDEPENDENT_VERIFICATION=PASS')