from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess

EXPECTED = {
    'runtime': 'c080a364ef2eb5d0f3b168928b381a5328b3e751',
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'graph': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'tsk0328': '527436958a1cd75fc91057410f4347ad56a3f53a',
    'tsk0312': '8dd71bccbd24ac5f62d5c536e644e7d9209b5832',
    'artifact': 'bc9ff6c3240c06e12af977097ccbc05fca9ad8ef',
    'model': 'c4ffbe4c5795b57dc074f41e1480fe610784679d',
    'analytical': '8f416952e33c09c3508d88ae5a5873b75f3814ca',
    'deterministic': '66f6ed2237481815874212b90381f0c40448dc07',
    'verifier': 'a3226acb62c8ded1e016246d29843cc27a61fb4a',
    'workflow': 'f88bdd71321c962a0bc290b9a847234b7915bc72',
}
PATHS = {
    'runtime': 'CURRENT_STATE.md',
    'wbs': 'Plans/Master/WBS/master-wbs.csv',
    'graph': 'Plans/Master/RELATIONSHIP_INDEX.yaml',
    'tsk0328': 'prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md',
    'tsk0312': 'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md',
    'artifact': 'prototype/TSK-0329/AUTH_ACCOUNT_INTERACTION_PROTOTYPE.md',
    'model': 'prototype/TSK-0329/INTERACTION_STATE_MODEL.json',
    'analytical': 'TSK_0329_AUTH_ACCOUNT_INTERACTION_ACCEPTANCE_EVIDENCE_2026-08-31.md',
    'deterministic': 'TSK_0329_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md',
    'verifier': '.github/scripts/verify_tsk0329_post_cr0007_structured_20260831.py',
    'workflow': '.github/workflows/verify-tsk0329-post-cr0007-structured-20260831.yml',
}
ACCEPTED = '## TSK-0329 current accepted stable state — 2026-08-31 — POST-CR-0007'


def blob(path):
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


for key, path in PATHS.items():
    actual = blob(path)
    if actual != EXPECTED[key]:
        raise SystemExit(f'unexpected {key} blob: {actual}')

p = Path(PATHS['runtime'])
text = p.read_text(encoding='utf-8')
for marker in [
    '## TSK-0328 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0312 current accepted stable state — 2026-08-31',
]:
    if marker not in text:
        raise SystemExit(f'required dependency marker absent: {marker}')
if ACCEPTED in text:
    raise SystemExit('TSK-0329 current accepted marker already present')
if 'LG-06 is not PASS' not in text and '`LG-06` is not PASS' not in text and 'LG-06 remains non-PASS' not in text:
    raise SystemExit('LG-06 non-PASS boundary absent')

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
text = re.sub(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {now}', text, count=1)
section = '''## TSK-0329 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0329 — Design and prototype Google sign-in, first-session account creation, and signed-in return interactions`: **PASS** under current `ACC-0329 / VER-0329 / EVD-0329`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependencies `TSK-0328; TSK-0312`, A4 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Relationship graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032`; bounded current-authority inspection run/job `33408418927 / 99541674501`: **SUCCESS**.
- Both hard dependencies are current durable PASS: post-CR-0007 TSK-0328 information architecture and current TSK-0312 parent authentication/account/session/minimal-intake requirements.
- Accepted normative prototype: `prototype/TSK-0329/AUTH_ACCOUNT_INTERACTION_PROTOTYPE.md`, version `1.0.0-post-cr0007`, blob `bc9ff6c3240c06e12af977097ccbc05fca9ad8ef`.
- Structured interaction state model: `prototype/TSK-0329/INTERACTION_STATE_MODEL.json`, blob `c4ffbe4c5795b57dc074f41e1480fe610784679d`.
- Analytical evidence: `TSK_0329_AUTH_ACCOUNT_INTERACTION_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `8f416952e33c09c3508d88ae5a5873b75f3814ca`.
- Deterministic evidence: `TSK_0329_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `66f6ed2237481815874212b90381f0c40448dc07`.
- Corrected structured verifier blob `a3226acb62c8ded1e016246d29843cc27a61fb4a`; workflow blob `f88bdd71321c962a0bc290b9a847234b7915bc72`; final run/job `33409037262 / 99543709479`: **SUCCESS** on self-hosted `adguardvm`.
- Final observed markers: WBS contract PASS; graph contract PASS; dependency/runtime PASS; structured interaction model PASS; artifact structure PASS; analytical/downstream-PASS fences PASS; current-scope reconciliation PASS; independent verification PASS; `git diff --check` and clean-worktree checks also succeeded.
- Initial run/job `33408877929 / 99543192828` is retained as diagnostic evidence only. It failed on a verifier section-scope false negative for `screen-reader`; the normative prototype, state model, analytical evidence, WBS, graph and runtime were unchanged. The corrected semantic-scope check passed.
- Accepted interaction scope covers optional Google sign-in, explicit first-session product-account creation, signed-in return, provider/cancel/network/ambiguous-identity/session errors, session expiry/re-authentication, logout, account-deletion entry, minimum intake-field states, back/refresh/retry/resume and data-use explanation.
- The complete accountless core remains usable without login. No local password/SMS/child-login path is authorized; Google remains the planned Version-1 route only and this PASS does not approve provider/security/vendor architecture.
- No automatic J0/J1 join/conversion/promotion/linkage or expiry extension is authorized. Account/session/dashboard presence never directly establishes technical `Verified` evidence.
- Provider/session failures are account-only and do not change configured DNS/core truth. Ambiguous identity fails closed without silent merge, duplicate-account creation or password/SMS fallback.
- Logout, account deletion, dashboard/device-record deletion, J0/J1 deletion and physical DNS removal remain distinct operations.
- Child identity, browsing/query/activity history and unnecessary provider-profile intake remain excluded. Email/display name/profile image are not product-required by default merely because the provider may supply them.
- WCAG 2.2 AA target, mobile-first behavior and English/Turkish/Arabic+RTL interaction capability are represented without inferring non-UK market activation or pre-L8 behavioral validation.
- This PASS does **not** infer TSK-0331, TSK-0332, TSK-0333, provider/vendor/security/privacy architecture, persistent schema/storage, actual account-deletion execution, implementation/build, behavioral validation, LG-06 or any later gate PASS.
- `RSK-0002` remains OPEN/non-blocking before L8. `LG-06` remains non-PASS.

### Queue status after post-CR-0007 TSK-0329 acceptance

Recompute eligibility from current WBS dependencies, relationship graph, runtime evidence, gates/constraints and Action Authority. No successor or gate inherits PASS from TSK-0329.
'''
new_text = text.rstrip() + '\n\n' + section.rstrip() + '\n'
p.write_text(new_text, encoding='utf-8')
