from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED = {
    'CURRENT_STATE.md': '7d337793c68b72f5001b305905acc606c1f839c7',
    'Plans/Master/WBS/master-wbs.csv': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md': '8dd71bccbd24ac5f62d5c536e644e7d9209b5832',
    'TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_ACCEPTANCE_EVIDENCE_2026-08-31.md': '8a4eec66fb63b57d01a6413ca9459c0713f29ff5',
    'TSK_0312_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md': '995c6bb771c762b8bb104a8610ca593ac32db705',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')
if '## TSK-0312 current accepted stable state' in s:
    raise SystemExit('current TSK-0312 section already exists')

# The predecessor must still be current PASS in the exact runtime baseline.
for token in [
    '## TSK-0140 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '`TSK-0140 — Issue the post-validation product brief`: **PASS**',
]:
    if token not in s:
        raise SystemExit('TSK-0140 dependency token missing: ' + token)

marker = '## Frozen technical identity\n'
if s.count(marker) != 1:
    raise SystemExit(f'frozen technical identity marker count={s.count(marker)}')

current = '''## TSK-0312 current accepted stable state — 2026-08-31

`TSK-0312 — Specify parent authentication, account/session, and minimal intake requirements`: **PASS** under current `ACC-0312 / VER-0312 / EVD-0312`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, sole hard dependency `TSK-0140`, A3 / `AUTO_ALLOWED`; the WBS planning/execution snapshot is not runtime proof.
- Hard dependency `TSK-0140` is current post-CR-0007 PASS.
- Requirements artifact: `TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md`, version `1.0.0`, blob `8dd71bccbd24ac5f62d5c536e644e7d9209b5832`, publication commit `f2f383c0c7b01b72b1eb708e0522bf13bb415369`.
- Analytical acceptance evidence: `TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `8a4eec66fb63b57d01a6413ca9459c0713f29ff5`, publication commit `4cd272051fcb42643054361169ba828426ff3c8b`.
- Deterministic verification evidence: `TSK_0312_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `995c6bb771c762b8bb104a8610ca593ac32db705`, publication commit `afdd090ec101abf4e9d7539f0738e53d30af77ee`.
- Independent verifier run/job `33397888358 / 99506708568` on self-hosted `adguardvm`: WBS contract, dependency runtime, product scope, identity/intake minimization, account/session lifecycle, CSRF/session requirements, no-linkage, no-password/SMS, all 16 deterministic test cases, no-downstream-PASS inference and independent verification all PASS; repository diff/clean checks passed.
- Accepted product requirement: Version 1 uses the planned Google social sign-in route for the optional parent account; no local password or SMS authentication is introduced without later authority.
- Account/session requirements now explicitly define minimum identity/intake allowlists, account/session lifecycle, logout/revocation/deletion, errors/recovery/expiry, trusted-boundary validation, CSRF/session outcomes and QA-testable cases.
- The accountless core remains usable without login. J0/J1 stays separate from persistent account state; sign-in does not extend anonymous expiry and no automatic anonymous-to-account linkage/promotion is authorized.
- Account/device ownership never substitutes for technical DNS/Protection Map verification. Account deletion, anonymous-state deletion and DNS configuration removal remain distinct operations.
- English/Turkish/Arabic + RTL technical capability is required for auth/account surfaces, without implying official non-UK market activation.
- Exact Google/Firebase vendor/privacy/terms/architecture, persistent schema/storage/retention, cookie/token/session/CSRF implementation, security testing, implementation, real-user evidence, legal/privacy compliance and all later gates remain with their owning tasks. `LG-06` remains non-PASS.

### Queue status after TSK-0312 acceptance

TSK-0312 may satisfy outgoing hard-dependency edges including `TSK-0142` and `TSK-0329`, but neither successor is assumed eligible. Recompute each against all current hard dependencies, runtime evidence, gates/constraints, inputs and Action Authority.

'''
s = s.replace(marker, current + marker, 1)

lines = s.splitlines()
if len(lines) < 3 or not lines[2].startswith('**Updated:** '):
    raise SystemExit('Updated header mismatch')
lines[2] = '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')

for token in [
    '## TSK-0312 current accepted stable state — 2026-08-31',
    '`TSK-0312 — Specify parent authentication, account/session, and minimal intake requirements`: **PASS**',
    '33397888358 / 99506708568',
    '995c6bb771c762b8bb104a8610ca593ac32db705',
    'TSK-0312 may satisfy outgoing hard-dependency edges including `TSK-0142` and `TSK-0329`',
    '`LG-06` remains non-PASS',
]:
    if token not in s:
        raise SystemExit('post-transform token missing: ' + token)

p.write_text(s, encoding='utf-8')
print('TSK0312_RUNTIME_TRANSFORM=PASS')
