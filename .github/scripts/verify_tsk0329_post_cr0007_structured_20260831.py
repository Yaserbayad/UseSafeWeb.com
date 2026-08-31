import csv
import json
import re
import subprocess
from pathlib import Path

EXPECTED = {
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'graph': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'runtime': 'c080a364ef2eb5d0f3b168928b381a5328b3e751',
    'tsk0328': '527436958a1cd75fc91057410f4347ad56a3f53a',
    'tsk0312': '8dd71bccbd24ac5f62d5c536e644e7d9209b5832',
    'artifact': 'bc9ff6c3240c06e12af977097ccbc05fca9ad8ef',
    'model': 'c4ffbe4c5795b57dc074f41e1480fe610784679d',
    'analytical': '8f416952e33c09c3508d88ae5a5873b75f3814ca',
}
PATHS = {
    'wbs': 'Plans/Master/WBS/master-wbs.csv',
    'graph': 'Plans/Master/RELATIONSHIP_INDEX.yaml',
    'runtime': 'CURRENT_STATE.md',
    'tsk0328': 'prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md',
    'tsk0312': 'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md',
    'artifact': 'prototype/TSK-0329/AUTH_ACCOUNT_INTERACTION_PROTOTYPE.md',
    'model': 'prototype/TSK-0329/INTERACTION_STATE_MODEL.json',
    'analytical': 'TSK_0329_AUTH_ACCOUNT_INTERACTION_ACCEPTANCE_EVIDENCE_2026-08-31.md',
}


def blob(path):
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


def require(cond, msg):
    if not cond:
        raise SystemExit(msg)


def section(text, title):
    marker = f'## {title}'
    start = text.find(marker)
    require(start >= 0, f'missing section: {title}')
    end = text.find('\n## ', start + len(marker))
    return text[start:] if end < 0 else text[start:end]


def graph_block(text, entity):
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if line == f'  {entity}:'), None)
    require(start is not None, f'graph entity missing: {entity}')
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r'^  [^ ].*:$', lines[i]):
            end = i
            break
    return '\n'.join(lines[start:end])


for key, path in PATHS.items():
    require(blob(path) == EXPECTED[key], f'unexpected {key} blob')

with Path(PATHS['wbs']).open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f)}
r = rows.get('TSK-0329')
require(r is not None, 'TSK-0329 missing from WBS')
require(r.get('Lifecycle_Stage') == 'L4', 'lifecycle mismatch')
require(r.get('Priority') == 'MEDIUM', 'priority mismatch')
require(r.get('Dependencies') == 'TSK-0328; TSK-0312', 'dependency mismatch')
require(r.get('Acceptance_ID') == 'ACC-0329', 'acceptance mismatch')
require(r.get('Verification_ID') == 'VER-0329', 'verification mismatch')
require(r.get('Evidence_ID') == 'EVD-0329', 'evidence mismatch')
require(r.get('AI_Capability_A0_A4') == 'A4', 'capability mismatch')
require(r.get('Action_Authority') == 'AUTO_ALLOWED', 'authority mismatch')
for ref in ['REQ-0028', 'REQ-0029', 'CON-0010', 'CON-0017']:
    require(ref in r.get('Requirement_Reference', ''), f'missing WBS requirement: {ref}')
for ref in ['INT-0009', 'INT-0010']:
    require(ref in r.get('Interface_Reference', ''), f'missing WBS interface: {ref}')
require('RSK-0002' in r.get('Risk_Reference', ''), 'RSK-0002 link absent')
print('TSK0329_WBS_CONTRACT=PASS')

graph = Path(PATHS['graph']).read_text(encoding='utf-8')
task = graph_block(graph, 'TSK-0329')
for target, rel in [
    ('ACC-0329', 'acceptance'), ('VER-0329', 'verified_by'), ('EVD-0329', 'evidence_required'),
    ('TSK-0328', 'depends_on'), ('TSK-0312', 'depends_on'), ('INT-0009', 'uses_interface'),
    ('INT-0010', 'uses_interface'), ('RSK-0002', 'affected_by_risk')
]:
    require(f'target: {target}' in task and f'type: {rel}' in task, f'graph relation missing: {target}/{rel}')
print('TSK0329_GRAPH_CONTRACT=PASS')

state = Path(PATHS['runtime']).read_text(encoding='utf-8')
require('## TSK-0328 current accepted stable state — 2026-08-31 — POST-CR-0007' in state, 'current TSK-0328 PASS absent')
require('## TSK-0312 current accepted stable state — 2026-08-31' in state, 'current TSK-0312 PASS absent')
require('## TSK-0329 current accepted stable state' not in state, 'TSK-0329 already accepted in runtime')
require('LG-06 is not PASS' in state or '`LG-06` is not PASS' in state or 'LG-06 remains non-PASS' in state, 'LG-06 non-PASS boundary absent')
print('TSK0329_DEPENDENCY_RUNTIME=PASS')

model = json.loads(Path(PATHS['model']).read_text(encoding='utf-8'))
require(model.get('schema') == 'usesafeweb.tsk0329.interaction-prototype.v1', 'model schema mismatch')
require(model.get('version') == '1.0.0-post-cr0007', 'model version mismatch')
require(model.get('normative_artifact_blob') == EXPECTED['artifact'], 'model artifact binding mismatch')
require(model.get('dependencies') == ['TSK-0328', 'TSK-0312'], 'model dependencies mismatch')
require(set(model.get('requirements', [])) == {'REQ-0028', 'REQ-0029', 'CON-0010', 'CON-0017'}, 'model requirements mismatch')
require(set(model.get('interfaces', [])) == {'INT-0009', 'INT-0010'}, 'model interfaces mismatch')
screens = {s['id']: s for s in model.get('screens', [])}
flows = {f['id']: f for f in model.get('flows', [])}
intake = {i['item']: i for i in model.get('intake_states', [])}
require(len(screens) == 12, 'screen count mismatch')
require(len(flows) == 12, 'flow count mismatch')
require(len(intake) == 10, 'intake-state count mismatch')
require(len(model.get('error_classes', [])) == 6, 'error-class count mismatch')
require(len(model.get('required_invariants', [])) == 13, 'invariant count mismatch')
require(model.get('acceptance_cases') == [f'AUTH-P{i:02d}' for i in range(1, 21)], 'acceptance-case sequence mismatch')
for sid, s in screens.items():
    require(s.get('goal', '').strip(), f'screen goal missing: {sid}')
    trace = set(s.get('trace', []))
    require('REQ-0028' in trace and 'TSK-0312' in trace and {'INT-0009', 'INT-0010'} <= trace, f'screen trace incomplete: {sid}')
for required in ['AUTH-ENTRY','AUTH-PROVIDER-PENDING','AUTH-CALLBACK-RESOLVING','AUTH-FIRST-SESSION','AUTH-CREATE-PENDING','AUTH-ERROR','AUTH-RETURN','AUTH-REAUTH','AUTH-ACCOUNT','AUTH-DATA-USE','AUTH-LOGOUT-PENDING','AUTH-DELETE-ENTRY']:
    require(required in screens, f'required screen missing: {required}')
for required in ['existing-parent-signin','first-session-create','provider-error','session-expiry','logout','account-deletion-entry','data-use-review']:
    require(required in flows, f'required flow missing: {required}')
require(flows['first-session-create']['sequence'] == ['AUTH-ENTRY','AUTH-PROVIDER-PENDING','AUTH-CALLBACK-RESOLVING','AUTH-FIRST-SESSION','AUTH-CREATE-PENDING','AUTH-RETURN'], 'first-session flow mismatch')
require('no J0/J1 import' in flows['first-session-create']['terminal'], 'first-session no-linkage terminal absent')
require('DNS/core unchanged' in flows['provider-error']['terminal'], 'provider-error core-neutral terminal absent')
require('destructive action not auto-replayed' in flows['session-expiry']['terminal'], 'session reauth replay fence absent')
require('session access ends only' in flows['logout']['terminal'], 'logout lifecycle terminal absent')
require('account vs J0/J1 vs DNS' in flows['account-deletion-entry']['terminal'], 'deletion separation terminal absent')
require(intake['child identity fields']['classification'] == 'prohibited', 'child identity classification mismatch')
require(intake['phone/SMS/password']['classification'] == 'prohibited-auth-route', 'password/SMS classification mismatch')
require(intake['email']['classification'] == 'not-required-by-default', 'email minimum-intake classification mismatch')
require(intake['display name/profile image']['classification'] == 'not-required-by-default', 'provider-profile minimum-intake classification mismatch')
required_invariants = {
    'complete core remains usable without login',
    'Google social sign-in is the only planned Version-1 authentication route',
    'no UseSafeWeb password, SMS or child login is introduced',
    'first-session account creation is explicit and minimal',
    'no automatic J0/J1 join, conversion, promotion, linkage or expiry extension',
    'sign-in, account, session and dashboard presence never directly establish technical Verified evidence',
    'provider/session failure affects account-only access and preserves truthful accountless core and DNS state',
    'ambiguous identity fails closed without merge, duplicate account, password or SMS fallback',
    'logout, account deletion, dashboard/device-record deletion, J0/J1 deletion and physical DNS removal remain distinct operations',
    'data-use explanation is available before first account creation and later from Account without inventing legal consent or compliance claims',
    'child identity, browsing/query/activity history and unnecessary provider-profile fields are not required for account creation',
    'back, refresh, retry and resume behavior is idempotent and does not replay destructive actions automatically',
    'English/Turkish/Arabic+RTL and WCAG 2.2 AA interaction capability do not imply non-UK market activation',
}
require(required_invariants <= set(model.get('required_invariants', [])), 'model invariant missing')
print('TSK0329_STRUCTURED_MODEL=PASS')

art = Path(PATHS['artifact']).read_text(encoding='utf-8')
require('**Version:** 1.0.0-post-cr0007' in art, 'artifact version mismatch')
binding = section(art, '2. Binding interaction rules').lower()
for token in ['account is optional', 'google sign-in is the only planned version-1 account entry', 'first-session account creation is explicit and minimal', 'no automatic j0/j1 promotion or linkage', 'account state is protection-state neutral', 'provider/session failure is account-only', 'ambiguous identity fails closed', 'lifecycle actions are distinct', 'data use is explained']:
    require(token in binding, f'binding semantic missing: {token}')
for sid in screens:
    require(f'`{sid}`' in art, f'artifact screen absent: {sid}')
first = section(art, '5. Screen prototype details').lower()
for token in ['create my account', 'not now', 'provider unavailable', 'identity/account binding ambiguous', 'sign in again to continue', 'delete your account', 'account data use', 'log out']:
    require(token in first, f'prototype detail missing: {token}')
intake_sec = section(art, '6. First-session intake field/state prototype').lower()
for token in ['provider-bound stable identity reference', 'email', 'display name/profile image', 'child identity fields', 'phone/sms/password', 'device nickname']:
    require(token in intake_sec, f'intake semantic missing: {token}')
back_sec = section(art, '7. Back, refresh, retry and resume behavior').lower()
for token in ['back from `auth-entry`', 'refresh callback/resolving state', 'network loss after create my account', 'session expires before destructive action', 'anonymous j0/j1 expires']:
    require(token in back_sec, f'back/resume semantic missing: {token}')
data_sec = section(art, '8. Data-use and privacy copy constraints').lower()
for token in ['optional account for continuity/device-management', 'minimum account/session identity binding', 'no account requirement for core setup', 'no browsing/query/activity-history product', 'technical verification remains separate']:
    require(token in data_sec, f'data-use semantic missing: {token}')
a11y = section(art, '9. Accessibility, responsive and RTL interaction contract').lower()
for token in ['wcag 2.2 aa', 'mobile-first', 'keyboard', 'arabic', 'rtl', 'no state meaning is communicated by color alone']:
    require(token in a11y, f'accessibility semantic missing: {token}')
require('screen-reader' in (binding + '\n' + a11y), 'screen-reader accessibility semantic missing from binding/accessibility contract')
cases = section(art, '10. Deterministic interaction cases')
require(len(re.findall(r'^\| `AUTH-P\d{2}` \|', cases, flags=re.M)) == 20, 'artifact deterministic case count mismatch')
coverage = section(art, '11. ACC-0329 coverage')
for token in ['Google sign-in', 'first-session account creation', 'signed-in return', 'errors/provider outage', 'logout', 'session expiry', 'account deletion entry', 'intake field states', 'back/resume', 'data-use explanation']:
    require(token.lower() in coverage.lower(), f'ACC coverage missing: {token}')
require('remains non-PASS until' in coverage, 'artifact non-PASS fence absent')
print('TSK0329_ARTIFACT_STRUCTURE=PASS')

ev = Path(PATHS['analytical']).read_text(encoding='utf-8')
require('**Analytical result: ACC-0329 PASS candidate.**' in ev, 'analytical disposition absent')
require('no pre-existing TSK-0329 product/prototype artifact' in ev, 'fresh-artifact provenance absent')
noninfer = section(ev, '7. Downstream non-inference').lower()
for token in ['google/firebase vendor', 'persistent schema/storage', 'actual account deletion execution', 'implementation/build', 'real-user behavioral validation', 'lg-06']:
    require(token in noninfer, f'non-inference missing: {token}')
combined = art + '\n' + ev
for marker in ['## TSK-0331 current accepted stable state', '## TSK-0332 current accepted stable state', '## LG-06 current accepted stable state']:
    require(marker not in combined, f'actual downstream accepted marker found: {marker}')
print('TSK0329_ANALYTICAL_AND_PASS_FENCES=PASS')
print('TSK0329_CURRENT_SCOPE_RECONCILIATION=PASS')
print('TSK0329_INDEPENDENT_VERIFICATION=PASS')
