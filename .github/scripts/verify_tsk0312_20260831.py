import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    'CURRENT_STATE.md': '7d337793c68b72f5001b305905acc606c1f839c7',
    'Plans/Master/WBS/master-wbs.csv': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'Plans/Master/Registers/REQUIREMENTS.md': 'a2212059f69c4602eb0c05961d5d1639e3543f83',
    'Plans/Master/Registers/CONSTRAINTS.md': '9464720bff94fd569e3b939568996a26eed83ca1',
    'Plans/Master/Registers/INTERFACES.md': 'b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c',
    'TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md': '8ed698b3e34540aefac617e5f6754e20d9dfbdc3',
    'TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md': '2955c2762e726f95ec67c33b9abbc5e4b25cb84a',
    'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md': '8dd71bccbd24ac5f62d5c536e644e7d9209b5832',
    'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_ACCEPTANCE_EVIDENCE_2026-08-31.md': '8a4eec66fb63b57d01a6413ca9459c0713f29ff5',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'hash mismatch {path}: {actual} != {sha}')

with open('Plans/Master/WBS/master-wbs.csv', encoding='utf-8-sig', newline='') as f:
    rows = [r for r in csv.DictReader(f) if r['Task_ID'] == 'TSK-0312']
if len(rows) != 1:
    raise SystemExit(f'TSK-0312 row count={len(rows)}')
r = rows[0]
expected_row = {
    'Lifecycle_Stage': 'L4',
    'Plan_Status': 'PLANNED',
    'Dependencies': 'TSK-0140',
    'AI_Capability_A0_A4': 'A3',
    'Action_Authority': 'AUTO_ALLOWED',
    'Acceptance_ID': 'ACC-0312',
    'Verification_ID': 'VER-0312',
    'Evidence_ID': 'EVD-0312',
    'Risk_Reference': 'RSK-0002',
    'Interface_Reference': 'INT-0009; INT-0010',
    'Requirement_Reference': 'REQ-0028; REQ-0029; REQ-0034; CON-0010; CON-0017',
}
for key, expected in expected_row.items():
    if r.get(key) != expected:
        raise SystemExit(f'WBS {key}: {r.get(key)!r} != {expected!r}')
acc = r['Acceptance_Criteria']
for token in [
    'Google social sign-in',
    'account/session lifecycle',
    'minimal required identity fields',
    'logout/revocation/deletion',
    'intake fields',
    'prohibited data',
    'validation',
    'errors',
    'resume/expiry behavior',
    'CSRF/session protections',
    'test cases',
    'no password or SMS authentication is introduced without a later decision',
]:
    if token not in acc:
        raise SystemExit('ACC-0312 token missing: ' + token)

state = Path('CURRENT_STATE.md').read_text(encoding='utf-8')
for token in [
    '## TSK-0140 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '`TSK-0140 — Issue the post-validation product brief`: **PASS**',
    '33391565765 / 99486171756',
]:
    if token not in state:
        raise SystemExit('runtime dependency token missing: ' + token)
if '## TSK-0312 current accepted stable state' in state:
    raise SystemExit('TSK-0312 already has current PASS section before verifier')

requirements = Path('Plans/Master/Registers/REQUIREMENTS.md').read_text(encoding='utf-8')
for token in [
    '| REQ-0028 | MUST | PKG-06 | Every user interaction, field, choice, confirmation, and account step shall have a documented necessity.',
    '| REQ-0029 | MUST | PKG-06 | Setup shall use automatic profiles/configuration where supported and reliable',
    '| REQ-0034 | MUST | PKG-06 | Product requirements shall define both the accountless core path and optional Version-1 account path',
]:
    if token not in requirements:
        raise SystemExit('requirement token missing: ' + token)
constraints = Path('Plans/Master/Registers/CONSTRAINTS.md').read_text(encoding='utf-8')
for token in [
    '| CON-0010 | Version 1 includes optional parent accounts, minimum parent/device ownership persistence and a lightweight dashboard while the complete core safety setup remains usable without login.',
    '| CON-0017 | First public release is multilingual in English, Turkish, and Arabic with RTL;',
]:
    if token not in constraints:
        raise SystemExit('constraint token missing: ' + token)
interfaces = Path('Plans/Master/Registers/INTERFACES.md').read_text(encoding='utf-8')
for token in [
    '| INT-0009 | Validated experience specification |',
    '| INT-0010 | UX/accessibility/i18n acceptance contract |',
]:
    if token not in interfaces:
        raise SystemExit('interface token missing: ' + token)

brief = Path('TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md').read_text(encoding='utf-8')
for token in [
    'the complete core setup/protection journey remains usable **without login**',
    'planned initial route: Google/Firebase social sign-in',
    'No password or SMS authentication is introduced by this brief.',
    'no automatic J1-to-account join, conversion or promotion is authorized',
    'CSRF/session protections appropriate to the chosen implementation',
]:
    if token not in brief:
        raise SystemExit('TSK-0140 baseline token missing: ' + token)

nolink = Path('TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md').read_text(encoding='utf-8')
for token in [
    'J0/J1 must not be automatically joined, converted, stitched or promoted into a parent account/device record.',
    'retaining J1 longer because the parent later signs in',
    'account/device deletion does not claim DNS configuration was removed unless the technical removal is separately verified',
]:
    if token not in nolink:
        raise SystemExit('TSK-0229 token missing: ' + token)

artifact = Path('TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md').read_text(encoding='utf-8')
required = [
    '**Version:** 1.0.0',
    'Version 1 shall provide **Google social sign-in** as the planned parent authentication route.',
    'No local password authentication is introduced.',
    'No SMS/phone-number authentication is introduced.',
    'Opaque internal parent-account identifier',
    'Provider-bound stable identity reference',
    'No automatic J0/J1-to-account join, conversion, promotion or linkage is authorized by this task.',
    'password credentials managed by UseSafeWeb',
    'browsing history, DNS-query history, visited/top domains, app/activity history or engagement profiling',
    '**Session expired / invalid**',
    'Logout shall terminate the applicable UseSafeWeb authenticated session',
    'Revoked, expired, invalid or otherwise unusable sessions shall fail closed',
    'Account deletion shall be an explicit, understandable action',
    'downstream implementation shall enforce authoritative validation at the trusted application boundary',
    'State-changing authenticated browser operations shall include implementation-appropriate CSRF protection',
    'Session identifiers/tokens shall not be exposed in user-visible URLs, analytics events, logs or content.',
    'Exact idle/absolute session duration values are **not invented by this L4 task**',
    'English, Turkish and Arabic, including RTL layout capability',
    '**Candidate disposition:** ACC-0312 is ready for independent post-publication verification; TSK-0312 remains non-PASS',
]
for token in required:
    if token not in artifact:
        raise SystemExit('artifact token missing: ' + token)
for forbidden in [
    'password sign-in is required',
    'SMS authentication is required',
    'child account is required',
    'automatic J0/J1-to-account linkage is authorized',
    'LG-06: PASS',
    'provider acceptance: PASS',
]:
    if forbidden in artifact:
        raise SystemExit('forbidden artifact token present: ' + forbidden)

test_ids = sorted(set(re.findall(r'\bAUTH-T(\d{2})\b', artifact)))
expected_tests = [f'{i:02d}' for i in range(1,17)]
if test_ids != expected_tests:
    raise SystemExit(f'test IDs mismatch: {test_ids} != {expected_tests}')

evidence = Path('TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_ACCEPTANCE_EVIDENCE_2026-08-31.md').read_text(encoding='utf-8')
for token in [
    '**Analytical result: ACC-0312 PASS candidate.**',
    'TSK-0312 shall not be marked runtime PASS until a separate deterministic verification',
    'No current canonical source inspected contradicts the persisted TSK-0312 artifact.',
]:
    if token not in evidence:
        raise SystemExit('analytical evidence token missing: ' + token)

print('TSK0312_WBS_CONTRACT=PASS')
print('TSK0312_DEPENDENCY_RUNTIME=PASS')
print('TSK0312_PRODUCT_SCOPE=PASS')
print('TSK0312_IDENTITY_INTAKE_MINIMIZATION=PASS')
print('TSK0312_ACCOUNT_SESSION_LIFECYCLE=PASS')
print('TSK0312_CSRF_SESSION_REQUIREMENTS=PASS')
print('TSK0312_NO_LINKAGE=PASS')
print('TSK0312_NO_PASSWORD_SMS=PASS')
print('TSK0312_TEST_CASES_16=PASS')
print('TSK0312_NO_DOWNSTREAM_PASS_INFERENCE=PASS')
print('TSK0312_INDEPENDENT_VERIFICATION=PASS')
