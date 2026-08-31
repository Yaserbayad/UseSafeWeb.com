from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess

EXPECTED = {
    'runtime': '6feab0d1991035304293c25c0af1398e75ff91f7',
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'artifact': '7763a6d16760d85df3ad23789f764d3e431849ef',
    'projection': '9826c7ab39e087002c6e0a51d7353e52ca6cc34b',
    'analytical': '36d838ad4e9de2f705005a16930d72a768727d68',
    'deterministic': 'a0758133ebf516cccd10cbf3329c656a375392d4',
}
PATHS = {
    'runtime': 'CURRENT_STATE.md',
    'wbs': 'Plans/Master/WBS/master-wbs.csv',
    'artifact': 'prototype/TSK-0325/SERVICE_BLUEPRINT.md',
    'projection': 'prototype/TSK-0325/ACCEPTANCE_MATRIX.json',
    'analytical': 'TSK_0325_POST_CR0007_PARENT_JOURNEY_SERVICE_BLUEPRINT_EVIDENCE_2026-08-31.md',
    'deterministic': 'TSK_0325_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md',
}
MARKER = '## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007'


def blob(path):
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


for key, path in PATHS.items():
    actual = blob(path)
    if actual != EXPECTED[key]:
        raise SystemExit(f'unexpected {key} blob: {actual}')

p = Path(PATHS['runtime'])
text = p.read_text(encoding='utf-8')
if MARKER in text:
    raise SystemExit('TSK-0325 current marker already present')

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
text = re.sub(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {now}', text, count=1)
section = '''

## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0325 — Create end-to-end parent journey and service blueprint`: **PASS** under current `ACC-0325 / VER-0325 / EVD-0325` and `DEC-0053/CR-0006 + DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependency `TSK-0326`, A3 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Dependency `TSK-0326` remains `NOT_APPLICABLE + PASS` solely as the verified CR-0005 exclusion of pre-L8 human validation; no behavioral/user evidence is inferred.
- Supporting dual-mode service baseline `TSK-0315` is current post-CR-0007 PASS.
- Accepted normative blueprint: `prototype/TSK-0325/SERVICE_BLUEPRINT.md`, version `2.0.0-post-cr0007`, blob `7763a6d16760d85df3ad23789f764d3e431849ef`.
- Structured acceptance projection: `prototype/TSK-0325/ACCEPTANCE_MATRIX.json`, blob `9826c7ab39e087002c6e0a51d7353e52ca6cc34b`.
- Analytical evidence: `TSK_0325_POST_CR0007_PARENT_JOURNEY_SERVICE_BLUEPRINT_EVIDENCE_2026-08-31.md`, blob `36d838ad4e9de2f705005a16930d72a768727d68`.
- Deterministic evidence: `TSK_0325_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `a0758133ebf516cccd10cbf3329c656a375392d4`.
- Final structured verifier blob `bae7ea3714495bb3a11f40dcadfecf3c714c1409`; final run/job `33405928577 / 99533392966`: **SUCCESS** on self-hosted `adguardvm`.
- Final observed markers: WBS contract PASS; dependency/runtime PASS; eight-path + 17-touchpoint structure PASS; projection lifecycle contract PASS; artifact lifecycle structure PASS; analytical/downstream-PASS fences PASS; current-scope reconciliation PASS; independent verification PASS; `git diff --check` and clean-worktree checks also succeeded.
- The verifier diagnostic sequence established false negatives in brittle prose/punctuation/negation matching; the normative blueprint, projection, WBS, analytical evidence and pre-reconciliation runtime blobs were not modified to obtain PASS. Earlier failed runs remain diagnostic evidence only.
- Accepted journey scope covers normal, already-configured, unsupported, failed-activation, false-positive, resume, removal/recovery and support/help paths, with all 17 touchpoints traced to current requirements/constraints/interfaces.
- The complete core journey remains usable without login; optional account/session/dashboard/device continuity remains optional and cannot strengthen technical verification.
- No automatic J0/J1-to-account/device promotion/linkage is authorized. Logout/session, revoke/unlink, device-record deletion, account deletion, J0/J1 deletion and physical DNS removal retain distinct lifecycle semantics.
- Browsing/query/activity history, child accounts/profiles and raw/unrestricted AdGuard administration remain excluded.
- This PASS does **not** infer current TSK-0328, TSK-0329, implementation/build, behavioral validation, LG-06 or any later gate PASS. Historical TSK-0328 accountless-only acceptance remains stale under CR-0006 and must be independently rebuilt/revalidated before use.
- `RSK-0002` remains OPEN/non-blocking before L8. `LG-06` remains non-PASS.

### Queue status after post-CR-0007 TSK-0325 acceptance

Recompute eligibility from current WBS dependencies, current runtime evidence, gates and Action Authority. TSK-0328 may now be reconsidered against current `TSK-0325` and `TSK-0315` evidence, but its historical pre-CR-0006 accountless-only artifact/PASS must not be reused where current acceptance requires optional account sign-in/return/dashboard/account-lifecycle navigation.
'''
p.write_text(text.rstrip() + section + '\n', encoding='utf-8')
