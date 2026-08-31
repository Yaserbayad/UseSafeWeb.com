from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess

EXPECTED = {
    'runtime': '0001c60094e2053c5e9e3a8c1ca64c8a6448adf7',
    'wbs': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'artifact': '4efb624005061e242e427994953d0fc00fcd745f',
    'evidence': '0047367fa046409fcdc4cb031bcc13b2614fc310',
}
PATHS = {
    'runtime': 'CURRENT_STATE.md',
    'wbs': 'Plans/Master/WBS/master-wbs.csv',
    'artifact': 'prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md',
    'evidence': 'TSK_0328_POST_CR0007_REOPEN_EVIDENCE_2026-08-31.md',
}
MARKER = '## TSK-0328 current reopened state — 2026-08-31 — POST-CR-0007'


def blob(path):
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()

for key, path in PATHS.items():
    actual = blob(path)
    if actual != EXPECTED[key]:
        raise SystemExit(f'unexpected {key} blob: {actual}')

p = Path(PATHS['runtime'])
text = p.read_text(encoding='utf-8')
if MARKER in text:
    raise SystemExit('TSK-0328 current reopened marker already present')
for dep in [
    '## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0325 current accepted stable state — 2026-08-31 — POST-CR-0007',
]:
    if dep not in text:
        raise SystemExit(f'missing dependency marker: {dep}')

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
text = re.sub(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {now}', text, count=1)
section = '''

## TSK-0328 current reopened state — 2026-08-31 — POST-CR-0007

`TSK-0328 — Define information architecture and navigation model`: **TODO / REOPENED** under current `ACC-0328 / VER-0328 / EVD-0328` and `DEC-0053/CR-0006 + DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependencies `TSK-0325; TSK-0315`, A3 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Both hard dependencies are current durable PASS under their post-CR-0007 accepted-state sections.
- Reopen evidence: `TSK_0328_POST_CR0007_REOPEN_EVIDENCE_2026-08-31.md`, blob `0047367fa046409fcdc4cb031bcc13b2614fc310`; inspection run/job `33406511402 / 99535321940`: **SUCCESS**.
- Historical artifact `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md`, version `1.0.0`, blob `4efb624005061e242e427994953d0fc00fcd745f`, remains stale for current acceptance because it explicitly excludes Login/Account/Dashboard and persistent account-dashboard navigation.
- Current ACC-0328 requires normal and exception paths for the accountless core plus optional account sign-in/return/dashboard/account lifecycle, no unnecessary gated steps, login optional for core value, and every screen mapped to a user goal and requirement.
- The historical artifact may be reused only for still-compatible public/setup structure; it does **not** constitute current PASS.
- Current disposition is TODO: rebuild and independently verify the IA/navigation model under current optional-account scope before any TSK-0328 PASS can be recorded.
- No TSK-0329, implementation/build, behavioral-validation, LG-06 or later gate PASS is inferred. `RSK-0002` remains OPEN/non-blocking before L8.
'''
p.write_text((text.rstrip() + section).rstrip() + '\n', encoding='utf-8')
