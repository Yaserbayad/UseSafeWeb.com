from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess

EXPECTED = {
    'runtime': 'cd65636a10e0d0f6c72f5062a269cba69279399d',
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'graph': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'artifact': '527436958a1cd75fc91057410f4347ad56a3f53a',
    'projection': 'd3b345a982f98bc7bdb32bc105fda4ac5659e9ab',
    'analytical': '4f2f62fc06dd4ab037f443480fd67191bc213713',
    'deterministic': '72976333541e50afa26f75b9326f8d02b4b86ad7',
    'verifier': '0e0aca9aed951a90e9decc3da4e77d5a034b2623',
    'workflow': '9647ee6b2822c4b753a6814bf0286f8b7a9a2542',
}
PATHS = {
    'runtime': 'CURRENT_STATE.md',
    'wbs': 'Plans/Master/WBS/master-wbs.csv',
    'graph': 'Plans/Master/RELATIONSHIP_INDEX.yaml',
    'artifact': 'prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md',
    'projection': 'prototype/TSK-0328/ACCEPTANCE_MATRIX.json',
    'analytical': 'TSK_0328_POST_CR0007_INFORMATION_ARCHITECTURE_ACCEPTANCE_EVIDENCE_2026-08-31.md',
    'deterministic': 'TSK_0328_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md',
    'verifier': '.github/scripts/verify_tsk0328_post_cr0007_structured_20260831.py',
    'workflow': '.github/workflows/verify-tsk0328-post-cr0007-structured-20260831.yml',
}
REOPENED = '## TSK-0328 current reopened state — 2026-08-31 — POST-CR-0007'
ACCEPTED = '## TSK-0328 current accepted stable state — 2026-08-31 — POST-CR-0007'


def blob(path):
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


for key, path in PATHS.items():
    actual = blob(path)
    if actual != EXPECTED[key]:
        raise SystemExit(f'unexpected {key} blob: {actual}')

p = Path(PATHS['runtime'])
text = p.read_text(encoding='utf-8')
if REOPENED not in text:
    raise SystemExit('current TSK-0328 reopened marker absent')
if '`TSK-0328 — Define information architecture and navigation model`: **TODO / REOPENED**' not in text:
    raise SystemExit('current TSK-0328 reopened TODO disposition absent')
if ACCEPTED in text:
    raise SystemExit('TSK-0328 current accepted marker already present')
for marker in [
    '## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007',
]:
    if marker not in text:
        raise SystemExit(f'required dependency marker absent: {marker}')

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
text = re.sub(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {now}', text, count=1)
section = '''## TSK-0328 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0328 — Define information architecture and navigation model`: **PASS** under current `ACC-0328 / VER-0328 / EVD-0328` and `DEC-0053/CR-0006 + DEC-0054/CR-0007` authority.

- This accepted section supersedes the preceding TSK-0328 reopened-TODO runtime snapshot; that earlier section remains historical pre-acceptance evidence only.
- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependencies `TSK-0325; TSK-0315`, A3 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Relationship graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032`; bounded graph inspection run/job `33407284717 / 99537877018`: **SUCCESS**.
- Both hard dependencies are current durable PASS under their post-CR-0007 accepted-state sections.
- Accepted normative IA: `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md`, version `2.0.0-post-cr0007`, blob `527436958a1cd75fc91057410f4347ad56a3f53a`.
- Structured acceptance projection: `prototype/TSK-0328/ACCEPTANCE_MATRIX.json`, blob `d3b345a982f98bc7bdb32bc105fda4ac5659e9ab`.
- Analytical evidence: `TSK_0328_POST_CR0007_INFORMATION_ARCHITECTURE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `4f2f62fc06dd4ab037f443480fd67191bc213713`.
- Deterministic evidence: `TSK_0328_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `72976333541e50afa26f75b9326f8d02b4b86ad7`.
- Independent structured verifier blob `0e0aca9aed951a90e9decc3da4e77d5a034b2623`; workflow blob `9647ee6b2822c4b753a6814bf0286f8b7a9a2542`; final run/job `33408013645 / 99540324630`: **SUCCESS** on self-hosted `adguardvm`.
- Final observed markers: WBS contract PASS; graph contract PASS; dependency/runtime PASS; structured projection PASS; artifact structure PASS; analytical/downstream-PASS fences PASS; current-scope reconciliation PASS; independent verification PASS; `git diff --check` and clean-worktree checks also succeeded.
- Accepted architecture preserves a complete signed-out core path from public Start setup through supported configuration, current technical verification, Protection Map, troubleshooting/recovery/removal and Exit without login.
- Optional account continuity now includes sign-in/error/re-authentication, returning-session, dashboard empty/list, device detail/add/manage, record-deletion and account-lifecycle routes without becoming a core-value gate.
- Provider/account/session failures affect account-only access and preserve truthful accountless setup/help/removal availability and DNS state.
- Every logical screen has a documented user goal and current requirement trace. Account/device/dashboard presence or historical state never creates technical `Verified` evidence.
- Logout, revoke/unlink, dashboard-record deletion, account deletion, J0/J1 deletion and physical DNS removal remain distinct operations.
- Browsing/query/activity history, child accounts/profiles, raw/unrestricted AdGuard administration, broad per-domain controls, mandatory login and safety-score routes remain excluded.
- English/Turkish/Arabic+RTL capability remains technical experience scope only and does not activate a non-UK market.
- This PASS does **not** infer TSK-0329, provider/vendor/security/privacy architecture, persistent schema/storage, implementation/build, behavioral validation, LG-06 or any later gate PASS.
- `RSK-0002` remains OPEN/non-blocking before L8. `LG-06` remains non-PASS.

### Queue status after post-CR-0007 TSK-0328 acceptance

Recompute eligibility from current WBS dependencies, relationship graph, runtime evidence, gates/constraints and Action Authority. TSK-0329 may be reconsidered only after a fresh dependency/authority check; no successor PASS is inherited from TSK-0328.
'''
new_text = text.rstrip() + '\n\n' + section.rstrip() + '\n'
p.write_text(new_text, encoding='utf-8')
