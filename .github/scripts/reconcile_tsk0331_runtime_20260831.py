from datetime import datetime, timezone
from pathlib import Path
import subprocess

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
PROTO=ROOT/'prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md'
MODEL=ROOT/'prototype/TSK-0331/LIFECYCLE_STATE_MODEL.json'
HTML=ROOT/'prototype/TSK-0331/index.html'
CSS=ROOT/'prototype/TSK-0331/prototype.css'
APP=ROOT/'prototype/TSK-0331/app.mjs'
ANALYTICAL=ROOT/'TSK_0331_POST_CR0007_ACCOUNT_DEVICE_LIFECYCLE_ACCEPTANCE_EVIDENCE_2026-08-31.md'
DETERMINISTIC=ROOT/'TSK_0331_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md'
STRUCT=ROOT/'.github/scripts/verify_tsk0331_post_cr0007_structured_20260831.py'
BROWSER=ROOT/'.github/scripts/verify_tsk0331_browser_20260831.mjs'
WORKFLOW=ROOT/'.github/workflows/verify-tsk0331-post-cr0007-structured-20260831.yml'

EXPECTED={
RUNTIME:'b5700eef473850ac49fdc83ea5bfbe7f2c6e54f2',
WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
PROTO:'9f5994b31b63a018ea0212ce21083b9dacb39ecc',
MODEL:'442c5a7fb2fb0f5af23ef29878f383fd3cfaa294',
HTML:'64bb4fa2f64d76dc4655f55f85304da5c6ffca9a',
CSS:'2a0d633efb4f138566d8d05e9fc60632e5409f29',
APP:'9b8df052bc19c15bfa8cc217bb7932a251b80588',
ANALYTICAL:'81ebe13e71d168b4305d9a3791a15be70baa43b9',
DETERMINISTIC:'9b4b274d39a8d8d60b98392131e5dacc0a7199df',
STRUCT:'9b9de230512dda3debc6d75b33cb7bedaaeec6c2',
BROWSER:'e4940c55dce3f589c04c16a533d0c08eb8ea982f',
WORKFLOW:'6cea6ddc3a0f8071180ca1ef2dfa6da083da2ff4',
}

def blob(path): return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
def req(cond,msg):
    if not cond: raise SystemExit(msg)

for path,expected in EXPECTED.items():
    req(path.exists(),f'TSK0331_RECONCILE_MISSING={path.as_posix()}')
    req(blob(path)==expected,f'TSK0331_RECONCILE_BLOB_CHANGED={path.as_posix()}')

text=RUNTIME.read_text(encoding='utf-8')
for dep in ('TSK-0332','TSK-0334'):
    req(f'## {dep} current accepted stable state — 2026-08-31 — POST-CR-0007' in text,f'TSK0331_DEP_NOT_CURRENT_PASS={dep}')
heading='## TSK-0331 current accepted stable state — 2026-08-31 — POST-CR-0007'
req(heading not in text,'TSK0331_CURRENT_PASS_ALREADY_PRESENT')
req('33419292638 / 99577450844' in DETERMINISTIC.read_text(encoding='utf-8'),'TSK0331_FINAL_RUN_NOT_BOUND')

section='''\n## TSK-0331 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0331 — Design account/device deletion, reinstall, revoke, replacement and recovery flows`: **PASS** under current `ACC-0331 / VER-0331 / EVD-0331`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, hard dependencies `TSK-0332; TSK-0334`, A4 / `AUTO_ALLOWED`; both hard dependencies are current durable PASS.
- Accepted normative lifecycle prototype: `prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md`, version `1.0.0-post-cr0007`, blob `9f5994b31b63a018ea0212ce21083b9dacb39ecc`.
- Structured lifecycle model: `prototype/TSK-0331/LIFECYCLE_STATE_MODEL.json`, blob `442c5a7fb2fb0f5af23ef29878f383fd3cfaa294`.
- Runnable UI: `prototype/TSK-0331/index.html` blob `64bb4fa2f64d76dc4655f55f85304da5c6ffca9a`, CSS blob `2a0d633efb4f138566d8d05e9fc60632e5409f29`, interaction controller blob `9b8df052bc19c15bfa8cc217bb7932a251b80588`.
- Analytical evidence: `TSK_0331_POST_CR0007_ACCOUNT_DEVICE_LIFECYCLE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `81ebe13e71d168b4305d9a3791a15be70baa43b9`.
- Deterministic evidence: `TSK_0331_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `9b4b274d39a8d8d60b98392131e5dacc0a7199df`.
- Test-first RED run/job `33418733004 / 99575585891` proved the required artifact absence before implementation; no runtime mutation occurred.
- First GREEN run/job `33419145661 / 99576961041` passed all structural checks and exposed a test-setup-only skip-link assertion issue; product files were unchanged for that correction.
- Final run/job `33419292638 / 99577450844`: **SUCCESS** on self-hosted `adguardvm`; WBS/dependency/graph, structured model, normative prototype, static UI, functional, negative-security, configuration-truth, privacy, rollback/recovery, responsive, keyboard, RTL, zero-console-error, `git diff --check`, and clean-worktree checks all PASS.
- Current accepted interaction rule: account deletion, saved-record deletion, unlink/revoke, logout, J0/J1 deletion, physical UseSafeWeb removal, reconfigure and replacement remain distinct lifecycles with explicit consequences and truthful state.
- Unknown non-idempotent destructive outcomes require authoritative read-back before retry; reauthentication never automatically replays a destructive operation; ownership mismatch fails closed.
- Account deletion targets only account-domain data owned by the downstream approved deletion contract and does not claim physical UseSafeWeb removal or unrelated J0/J1 deletion. Any future required limited retention remains owned by separately approved data/legal/privacy/security authority; no retention duration is invented here.
- Replacement begins with fresh unverified state and inherits no Verified/parent-confirmed state or activity history. Reconfiguration requires new current technical evidence before a stronger protection state.
- No provider/vendor/security/privacy architecture, persistence schema/storage/retention/backup/authz implementation, legal retention obligation, production deletion/removal execution, build/deployment behavior, TSK-0333, real-user validation, or LG-06 PASS is inferred.
- `RSK-0002` remains OPEN/non-blocking before L8.

### Queue status after post-CR-0007 TSK-0331 acceptance

Recompute eligibility from current WBS dependencies, relationship graph, runtime evidence, gates/constraints, current changed-scope validity, and Action Authority. No successor or gate inherits PASS from TSK-0331.
'''

text=text.rstrip()+section
now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]=f'**Updated:** {now}'
        break
else:
    raise SystemExit('CURRENT_STATE_UPDATED_FIELD_MISSING')
RUNTIME.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
print('TSK0331_RUNTIME_PRECONDITIONS=PASS')
