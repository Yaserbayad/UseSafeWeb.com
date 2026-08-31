from datetime import datetime, timezone
from pathlib import Path
import subprocess

ROOT = Path('.')
RUNTIME = ROOT / 'CURRENT_STATE.md'
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
BASE = ROOT / 'design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md'
AMD = ROOT / 'design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md'
PREP = ROOT / 'TSK_0334_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md'
OWNER = ROOT / 'TSK_0334_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md'
FINAL = ROOT / 'TSK_0334_POST_CR0007_DETERMINISTIC_ACCEPTANCE_EVIDENCE_2026-08-31.md'

EXPECTED = {
    RUNTIME: 'f8c1a9ca9bb69899c2a55bd7f6700f6d018dabb9',
    WBS: 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    BASE: '44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f',
    AMD: 'de423bdb8aeb2b0a0f25a85850be380cfab7e67d',
    PREP: '652845396bc62a1df859b2a9f1944576268066b6',
    OWNER: 'ece3d3cb92829a84877ad62bf59f89b453223942',
    FINAL: '33941cefac1aa2c67192f7da90a611d48bd72396',
}


def blob(path):
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


for path, expected in EXPECTED.items():
    require(path.exists(), f'TSK0334_RECONCILE_MISSING={path.as_posix()}')
    require(blob(path) == expected, f'TSK0334_RECONCILE_BLOB_CHANGED={path.as_posix()}')

text = RUNTIME.read_text(encoding='utf-8')
old_heading = '## TSK-0334 current state — 2026-08-31 — POST-CR-0007'
new_heading = '## TSK-0334 current accepted stable state — 2026-08-31 — POST-CR-0007'
require(old_heading in text, 'TSK0334_WAITING_HEADING_MISSING')
require('**WAITING / HUMAN_APPROVAL_REQUIRED**, not PASS' in text, 'TSK0334_WAITING_STATE_CHANGED')
require(new_heading not in text, 'TSK0334_CURRENT_PASS_ALREADY_PRESENT')
require('## TSK-0332 current accepted stable state — 2026-08-31 — POST-CR-0007' in text, 'TSK0332_CURRENT_PASS_MISSING')

start = text.index(old_heading)
next_heading = text.find('\n## ', start + len(old_heading))
end = len(text) if next_heading == -1 else next_heading + 1

section = '''## TSK-0334 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0334 — Design support, false-positive, removal, and reconfiguration flows`: **PASS** under current `ACC-0334 / VER-0334 / EVD-0334`, explicit Project Owner approval, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependency `TSK-0330`, A1 / `HUMAN_ONLY`; the WBS planning snapshot is not runtime proof.
- Historical base support candidate remains accepted for still-valid technical categories SUP-01 through SUP-05: `design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md`, blob `44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f`.
- Current-scope amendment accepted for optional-account/dashboard support categories SUP-06 through SUP-08: `design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md`, version `1.0.0-post-cr0007`, blob `de423bdb8aeb2b0a0f25a85850be380cfab7e67d`.
- Explicit Project Owner approval `2026-08-31T17:10:48Z`: `APPROVE TSK-0334 POST-CR-0007 CURRENT-SCOPE SUPPORT AMENDMENT`; durable approval evidence `TSK_0334_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md`, blob `ece3d3cb92829a84877ad62bf59f89b453223942`.
- Preparation evidence `TSK_0334_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md`, blob `652845396bc62a1df859b2a9f1944576268066b6`; preparation run/job `33415828154 / 99566111401`: SUCCESS.
- Final deterministic evidence `TSK_0334_POST_CR0007_DETERMINISTIC_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `33941cefac1aa2c67192f7da90a611d48bd72396`.
- Final post-approval verification run/job `33418348987 / 99574340777`: SUCCESS; exact input blobs, WBS contract, waiting-state precondition, all eight ACC-0334 support-category fields, current-scope semantics, preparation evidence, and owner authority all PASS; `git diff --check` and clean-worktree checks also passed.
- Current accepted support scope: SUP-01 setup/verification troubleshooting; SUP-02 false positive; SUP-03 physical UseSafeWeb removal/connectivity recovery; SUP-04 reconfiguration/start again; SUP-05 unsupported/uncertain/limitations; SUP-06 account sign-in/session/provider access; SUP-07 saved-device record/ownership/unlink/dashboard management; SUP-08 account/device deletion and uncertain lifecycle results.
- Core remains usable without login. Account/session/provider/device-record state never establishes or rewrites physical protection truth. Ownership mismatch fails account-only operations closed. Unknown destructive outcomes require authoritative resolution before retry. Logout, account deletion, record deletion, unlinking, J0/J1 deletion, and physical UseSafeWeb removal remain distinct.
- No provider/vendor/security/privacy architecture, persistent schema/storage/retention/backup/authorization implementation, live support operation, production deletion behavior, TSK-0331/TSK-0333, real-user validation, or LG-06 PASS is inferred.
- `RSK-0002` remains OPEN/non-blocking before L8.

### Queue status after post-CR-0007 TSK-0334 acceptance

Recompute eligibility from current WBS dependencies, relationship graph, runtime evidence, gates/constraints and Action Authority. TSK-0331 may use TSK-0334 as a current dependency PASS only after this runtime mutation is committed, read back and verified.
'''

text = text[:start] + section + text[end:]
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines = text.splitlines()
for idx, line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[idx] = f'**Updated:** {now}'
        break
else:
    raise SystemExit('CURRENT_STATE_UPDATED_FIELD_MISSING')
RUNTIME.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')

print('TSK0334_RUNTIME_ACCEPTANCE_PRECONDITIONS=PASS')
