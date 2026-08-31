import csv
import json
import re
import subprocess
from pathlib import Path

EXPECTED = {
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'graph': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'runtime': 'cd65636a10e0d0f6c72f5062a269cba69279399d',
    'tsk0315': '97cf09f294c757f80ad5c0fbe6110ed8d471159c',
    'tsk0325': '7763a6d16760d85df3ad23789f764d3e431849ef',
    'tsk0312': '8dd71bccbd24ac5f62d5c536e644e7d9209b5832',
    'tsk0142': '77b432e9d06741d0d303de2c2a2524e804cdcf5e',
    'artifact': '527436958a1cd75fc91057410f4347ad56a3f53a',
    'projection': 'd3b345a982f98bc7bdb32bc105fda4ac5659e9ab',
    'analytical': '4f2f62fc06dd4ab037f443480fd67191bc213713',
}
PATHS = {
    'wbs': 'Plans/Master/WBS/master-wbs.csv',
    'graph': 'Plans/Master/RELATIONSHIP_INDEX.yaml',
    'runtime': 'CURRENT_STATE.md',
    'tsk0315': 'TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md',
    'tsk0325': 'prototype/TSK-0325/SERVICE_BLUEPRINT.md',
    'tsk0312': 'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md',
    'tsk0142': 'TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_REQUIREMENTS_2026-08-31.md',
    'artifact': 'prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md',
    'projection': 'prototype/TSK-0328/ACCEPTANCE_MATRIX.json',
    'analytical': 'TSK_0328_POST_CR0007_INFORMATION_ARCHITECTURE_ACCEPTANCE_EVIDENCE_2026-08-31.md',
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


def yaml_entity_block(text, entity):
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
r = rows.get('TSK-0328')
require(r is not None, 'TSK-0328 missing from WBS')
require(r.get('Lifecycle_Stage') == 'L4', 'lifecycle mismatch')
require(r.get('Priority') == 'MEDIUM', 'priority mismatch')
require(r.get('Dependencies') == 'TSK-0325; TSK-0315', 'dependency mismatch')
require(r.get('Acceptance_ID') == 'ACC-0328', 'acceptance mismatch')
require(r.get('Verification_ID') == 'VER-0328', 'verification mismatch')
require(r.get('Evidence_ID') == 'EVD-0328', 'evidence mismatch')
require(r.get('AI_Capability_A0_A4') == 'A3', 'capability mismatch')
require(r.get('Action_Authority') == 'AUTO_ALLOWED', 'action authority mismatch')
for ref in ['REQ-0028', 'REQ-0029', 'CON-0010', 'CON-0017']:
    require(ref in r.get('Requirement_Reference', ''), f'missing WBS requirement ref: {ref}')
for ref in ['INT-0009', 'INT-0010']:
    require(ref in r.get('Interface_Reference', ''), f'missing WBS interface ref: {ref}')
print('TSK0328_WBS_CONTRACT=PASS')

graph = Path(PATHS['graph']).read_text(encoding='utf-8')
task_block = yaml_entity_block(graph, 'TSK-0328')
acc_block = yaml_entity_block(graph, 'ACC-0328')
evd_block = yaml_entity_block(graph, 'EVD-0328')
ver_block = yaml_entity_block(graph, 'VER-0328')
next_block = yaml_entity_block(graph, 'TSK-0329')
require('target: TSK-0328' in acc_block and 'type: acceptance_criterion_for' in acc_block, 'ACC-0328 graph relation missing')
require('target: TSK-0328' in evd_block and 'type: evidence_for' in evd_block, 'EVD-0328 graph relation missing')
require('target: TSK-0328' in ver_block and 'type: verification_for' in ver_block, 'VER-0328 graph relation missing')
require('target: TSK-0328' in next_block and 'type: depends_on' in next_block, 'TSK-0329 -> TSK-0328 dependency missing')
for ref in ['ACC-0328', 'VER-0328', 'EVD-0328']:
    require(ref in graph, f'graph missing {ref}')
require('target: WP-0316' in task_block and 'type: parent_work_package' in task_block, 'TSK-0328 parent work package relation missing')
print('TSK0328_GRAPH_CONTRACT=PASS')

state = Path(PATHS['runtime']).read_text(encoding='utf-8')
require('## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007' in state, 'current TSK-0315 PASS marker absent')
require('## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007' in state, 'current TSK-0325 PASS marker absent')
require('## TSK-0328 current reopened state — 2026-08-31 — POST-CR-0007' in state, 'TSK-0328 reopened TODO marker absent')
require('`TSK-0328 — Define information architecture and navigation model`: **TODO / REOPENED**' in state, 'TSK-0328 runtime TODO disposition absent')
require('## TSK-0328 current accepted stable state — 2026-08-31 — POST-CR-0007' not in state, 'TSK-0328 already accepted in runtime')
print('TSK0328_DEPENDENCY_RUNTIME=PASS')

proj = json.loads(Path(PATHS['projection']).read_text(encoding='utf-8'))
require(proj.get('schema') == 'usesafeweb.tsk0328.acceptance-projection.v2', 'projection schema mismatch')
require(proj.get('version') == '2.0.0-post-cr0007', 'projection version mismatch')
require(proj.get('normative_artifact_blob') == EXPECTED['artifact'], 'projection artifact binding mismatch')
require(proj.get('dependencies') == ['TSK-0325', 'TSK-0315'], 'projection dependencies mismatch')
require(set(proj.get('requirements', [])) == {'REQ-0028', 'REQ-0029', 'CON-0010', 'CON-0017'}, 'projection requirements mismatch')
require(set(proj.get('interfaces', [])) == {'INT-0009', 'INT-0010'}, 'projection interfaces mismatch')
systems = {s['id']: s for s in proj.get('experience_systems', [])}
require(set(systems) == {'PUBLIC', 'SETUP', 'ACCOUNT'} and len(systems) == 3, 'experience systems mismatch')
paths = {p['id']: p for p in proj.get('required_paths', [])}
require(len(paths) == 11, 'required path count mismatch')
screens = {s['id']: s for s in proj.get('screen_inventory', [])}
require(len(screens) == 32, 'screen inventory count mismatch')
for sid, screen in screens.items():
    require(screen.get('goal', '').strip(), f'screen goal missing: {sid}')
    trace = set(screen.get('trace', []))
    require('REQ-0028' in trace, f'REQ-0028 trace missing: {sid}')
    if sid != 'PUB-NOTICES':
        require({'CON-0010', 'CON-0017', 'INT-0009', 'INT-0010'} <= trace, f'current CON/INT trace incomplete: {sid}')
    require(screen.get('system') in systems, f'unknown screen system: {sid}')
require(set(paths['accountless-normal']['must_include']) >= {'PUB-HOME', 'SCR-START', 'SCR-NATIVE', 'SCR-DNS-SETUP', 'SCR-VERIFY', 'SCR-MAP'}, 'accountless normal path incomplete')
require({'ACC-SIGNIN', 'DASH-HOME'} <= set(paths['accountless-normal']['must_exclude']), 'accountless path login/dashboard exclusion missing')
require({'SCR-MAP', 'ACC-ENTRY', 'ACC-SIGNIN', 'DASH-HOME'} <= set(paths['optional-account']['must_include']), 'optional-account path incomplete')
require({'DASH-HOME', 'DASH-DEVICE'} <= set(paths['returning-account']['must_include']), 'returning account path incomplete')
require({'ACC-SIGNIN', 'ACC-ERROR'} <= set(paths['provider-error']['must_include']), 'provider error path incomplete')
require('ACC-REAUTH' in paths['session-expiry']['must_include'], 'session expiry path incomplete')
require({'SCR-REMOVE', 'SCR-RECOVERY'} <= set(paths['physical-removal']['must_include']), 'physical removal path incomplete')
require('DASH-RECORD-DELETE' in paths['record-deletion']['must_include'], 'record deletion path incomplete')
require({'ACC-ACCOUNT', 'ACC-DELETE'} <= set(paths['account-deletion']['must_include']), 'account deletion path incomplete')
required_invariants = {
    'full core setup is completable without login',
    'Start setup remains available regardless of sign-in state',
    'optional account continuity never gates core value',
    'provider/account failure leaves accountless core available',
    'no automatic J0/J1-to-account/device linkage or expiry extension',
    'account/device/dashboard presence never directly establishes Verified',
    'logout, revoke/unlink, dashboard-record deletion, account deletion, J0/J1 deletion and physical DNS removal remain distinct operations',
    'no browsing/query/activity history, child account/profile, raw AdGuard administration or broad per-domain control route exists',
    'every logical screen maps to a user goal and current requirement trace',
    'English/Turkish/Arabic+RTL capability does not imply non-UK market activation',
}
require(required_invariants <= set(proj.get('mandatory_invariants', [])), 'mandatory invariant missing')
print('TSK0328_PROJECTION_CONTRACT=PASS')

art = Path(PATHS['artifact']).read_text(encoding='utf-8')
require('**Version:** 2.0.0-post-cr0007' in art, 'artifact version mismatch')
binding = section(art, '2. Binding architecture rules').lower()
for token in ['core value is accountless', 'account continuity is optional', 'no automatic anonymous-to-account stitching', 'technical verification stays technical', 'lifecycle actions remain distinct', 'no unnecessary gates', 'no surveillance/admin expansion']:
    require(token in binding, f'binding semantic missing: {token}')
systems_sec = section(art, '3. Experience-system model')
for heading in ['### A. Public information system', '### B. Accountless operational setup system', '### C. Optional authenticated continuity system']:
    require(heading in systems_sec, f'experience system heading missing: {heading}')
nav = section(art, '4. Global navigation model')
for token in ['**Start setup** — primary action', 'signed out: **Sign in**', 'signed in: **Dashboard** and **Account**']:
    require(token in nav, f'global navigation semantic missing: {token}')
for sid in screens:
    require(f'`{sid}`' in art, f'artifact screen missing: {sid}')
require(art.count('| `PUB-') >= 6, 'public screen rows incomplete')
require(art.count('| `SCR-') >= 15, 'setup screen rows incomplete')
require(art.count('| `ACC-') + art.count('| `DASH-') >= 11, 'account/dashboard screen rows incomplete')
normal = section(art, '9. Canonical normal paths')
accountless_sub = normal[normal.find('### 9.1 Signed-out accountless core'):normal.find('### 9.2 Optional continuity after core value')]
for token in ['SCR-START', 'SCR-NATIVE', 'SCR-DNS-SETUP', 'SCR-VERIFY', 'SCR-MAP', 'Exit']:
    require(token in accountless_sub, f'accountless artifact path missing: {token}')
require('ACC-SIGNIN' not in accountless_sub and 'DASH-HOME' not in accountless_sub, 'accountless artifact path contains account gate')
optional_sub = normal[normal.find('### 9.2 Optional continuity after core value'):normal.find('### 9.3 Returning signed-in parent')]
for token in ['SCR-MAP', 'ACC-ENTRY', 'ACC-SIGNIN', 'DASH-HOME']:
    require(token in optional_sub, f'optional continuity artifact path missing: {token}')
require('Exit' in optional_sub or 'continue signed out' in optional_sub.lower(), 'optional account lacks signed-out alternative')
returning_sub = normal[normal.find('### 9.3 Returning signed-in parent'):normal.find('### 9.4 Signed-in parent starts new setup')]
require('DASH-HOME' in returning_sub and 'DASH-DEVICE' in returning_sub, 'returning signed-in route incomplete')
require('cannot skip technical verification' in returning_sub.lower() or 'cannot' in returning_sub.lower() and 'technical verification' in returning_sub.lower(), 'returning account technical-truth fence absent')
exceptions = section(art, '10. Exception-path navigation').lower()
for token in ['already configured', 'unsupported / not covered', 'failed activation / verification', 'false positive', 'account sign-in cancellation/error/provider outage', 'session expiry/revocation', 'lost accountless state / resume', 'physical removal', 'dashboard record deletion', 'revoke/unlink', 'account deletion']:
    require(token in exceptions, f'exception path missing: {token}')
lifecycle = section(art, '12. Lifecycle-separation contract').lower()
for token in ['logout', 'revoke/unlink', 'delete dashboard record', 'delete account', 'j0/j1 expiry/deletion', 'remove usesafeweb dns']:
    require(token in lifecycle, f'lifecycle operation missing: {token}')
truth = section(art, '13. Protection-evidence and state rules').lower()
for token in ['never directly establishes `verified`', 'parent confirmation', 'current qualifying technical verifier', '`removed`', 'protection-state neutral']:
    require(token in truth, f'protection truth semantic missing: {token}')
necessity = section(art, '14. Necessity and duplication controls').lower()
for token in ['every interaction must satisfy req-0028', 'sign in exists only', 'dashboard exists only', 'no route exists solely for analytics', 'do not duplicate technical instructions']:
    require(token in necessity, f'necessity semantic missing: {token}')
a11y = section(art, '15. Accessibility, responsive and localization inheritance').lower()
for token in ['wcag 2.2 aa', 'mobile-first', 'english/turkish/arabic+rtl', 'does not imply official non-uk']:
    require(token in a11y, f'accessibility/localization semantic missing: {token}')
accept_cases = section(art, '16. Minimum deterministic/synthetic IA acceptance cases')
require(len(re.findall(r'^\| `IA-T\d{2}` \|', accept_cases, flags=re.M)) == 18, 'IA deterministic case count mismatch')
coverage = section(art, '17. Current ACC-0328 coverage')
require('ready for independent post-publication verification' in coverage, 'candidate verification disposition absent')
require('remains non-PASS until' in coverage, 'non-PASS fence absent')
print('TSK0328_ARTIFACT_STRUCTURE=PASS')

ev = Path(PATHS['analytical']).read_text(encoding='utf-8')
require('Historical TSK-0328 v1.0.0 was accepted' in ev, 'historical impact analysis absent')
require('**Analytical result: ACC-0328 PASS candidate.**' in ev, 'analytical PASS-candidate disposition absent')
noninfer = section(ev, '9. Downstream non-inference').lower()
for token in ['tsk-0329', 'implementation/build', 'real-user behavioral validation', 'lg-06']:
    require(token in noninfer, f'downstream non-inference missing: {token}')
combined = art + '\n' + ev
for marker in [
    '## TSK-0329 current accepted stable state',
    '## LG-06 current accepted stable state',
]:
    require(marker not in combined, f'actual downstream accepted-state marker found: {marker}')
print('TSK0328_ANALYTICAL_AND_PASS_FENCES=PASS')
print('TSK0328_CURRENT_SCOPE_RECONCILIATION=PASS')
print('TSK0328_INDEPENDENT_VERIFICATION=PASS')
