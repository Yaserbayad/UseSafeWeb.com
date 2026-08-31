import re
import subprocess
from pathlib import Path

STATE = Path('CURRENT_STATE.md')
EXPECTED_RUNTIME = 'e3d8a09ccf42f61f65b48ecd2e43773a7300bfbf'
EXPECTED_ARTIFACT = '3eb1b90dc9fc3a79be94c7343cd16a9d3093748f'
EXPECTED_ANALYTICAL = 'e55306c70fee60079aedfb42fd6cffbc863936f5'
EXPECTED_DETERMINISTIC = 'ea9ffa5bbbfe4e423e9d85bcd2e10020dfdc08da'


def blob(path: str) -> str:
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'], text=True).strip()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

require(blob('CURRENT_STATE.md') == EXPECTED_RUNTIME, 'runtime baseline changed before reconciliation')
require(blob('TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_2026-08-31.md') == EXPECTED_ARTIFACT, 'artifact blob mismatch')
require(blob('TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_ACCEPTANCE_EVIDENCE_2026-08-31.md') == EXPECTED_ANALYTICAL, 'analytical evidence blob mismatch')
require(blob('TSK_0149_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md') == EXPECTED_DETERMINISTIC, 'deterministic evidence blob mismatch')

text = STATE.read_text(encoding='utf-8')
require('TSK-0146 current accepted stable state' in text, 'TSK-0146 current PASS marker absent')
require('TSK-0149 current accepted stable state' not in text, 'TSK-0149 already current PASS')
text, count = re.subn(r'^\*\*Updated:\*\* .*$', '**Updated:** 2026-08-31T14:22:00Z', text, count=1, flags=re.MULTILINE)
require(count == 1, 'Updated marker not replaced exactly once')

section = r'''

## TSK-0149 current accepted stable state — 2026-08-31

`TSK-0149 — Freeze the distinct public website and product/setup outcomes`: **PASS** under current `ACC-0149 / VER-0149 / EVD-0149`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, priority HIGH, hard dependency `TSK-0146`, A3 / `AUTO_ALLOWED`. Its prior `COMPLETED_CANDIDATE/PASS` WBS snapshot was not used as runtime proof because no prior durable TSK-0149 artifact/evidence/runtime record existed.
- Hard dependency `TSK-0146` is current post-CR-0006 PASS for the dual-mode Version-1 product baseline.
- Current requirements artifact: `TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_2026-08-31.md`, version `1.0.0-post-cr0007`, blob `3eb1b90dc9fc3a79be94c7343cd16a9d3093748f`, publication commit `06efdf5e9b1d5ee4366714875b042bd19f31f333`.
- Analytical acceptance evidence: `TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `e55306c70fee60079aedfb42fd6cffbc863936f5`, publication commit `29ae07dca4d8ba247abb2fad44e1c5b3347ce182`.
- Deterministic verification evidence: `TSK_0149_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `ea9ffa5bbbfe4e423e9d85bcd2e10020dfdc08da`, publication commit `97c1608e2edeedee4c3b68e4dab06c98c9f6a664`.
- Independent verifier run/job `33402148107 / 99520837413` on self-hosted `adguardvm`: WBS contract, dependency runtime, current ACC semantics, all 10 deterministic assertions, analytical evidence and no-downstream-PASS inference all PASS; repository diff/clean checks passed.
- Accepted split: public website owns `discover / understand / trust / decide / start`; product/setup owns `start / configure / verify / understand / recover/manage`; both share one coherent brand/design system.
- The current split includes optional account sign-in/return/dashboard continuity as product/setup capability while preserving a complete login-free core journey. Public information/viewing cannot manufacture or mutate technical protection state.
- Mandatory login, payment gating of core value, browsing/query/activity history, child surveillance profiles and unrestricted DNS administration remain excluded.
- Exact current IA/navigation, implementation, provider/vendor/security architecture, real-user evidence, LG-06 and all later gates retain their own acceptance requirements; no successor PASS is inferred.
- `RSK-0002` remains OPEN/non-blocking before L8 under current sequencing.

### Queue status after TSK-0149 acceptance

TSK-0149 may now satisfy its outgoing hard-dependency edges. Recompute current L4 eligibility from WBS dependencies, current runtime evidence, graph, gates/constraints and Action Authority before selecting a successor.
'''
out = text.rstrip() + section.rstrip() + '\n'
require(not out.endswith('\n\n'), 'blank line at EOF would be created')
STATE.write_text(out, encoding='utf-8')
out = STATE.read_text(encoding='utf-8')
require('## TSK-0149 current accepted stable state — 2026-08-31' in out, 'TSK-0149 section missing')
require('Independent verifier run/job `33402148107 / 99520837413`' in out, 'verifier binding missing')
require(not out.endswith('\n\n'), 'blank line at EOF after write')
print('TSK0149_RUNTIME_TRANSFORM=PASS')
print('TSK0149_EOF_GUARD=PASS')
