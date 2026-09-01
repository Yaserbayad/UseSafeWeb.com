from pathlib import Path
import subprocess

EXPECTED_RUNTIME = 'c86b04508452c3483d4b164d670ab32c538bde42'
EXPECTED_WBS = 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_EVIDENCE = 'f9b970f67454b9354653030b192f8622ed2f57a3'
EXPECTED_CANDIDATE = 'eb5242880974a936121f362df0d960746a596795'


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

req(blob('CURRENT_STATE.md') == EXPECTED_RUNTIME, 'TSK0321_WAITING_RUNTIME_STALE')
req(blob('Plans/Master/WBS/master-wbs.csv') == EXPECTED_WBS, 'TSK0321_WAITING_WBS_STALE')
req(blob('TSK_0321_POST_CR0007_INTEGRATED_ACCESSIBILITY_PREPARATION_EVIDENCE_2026-09-01.md') == EXPECTED_EVIDENCE, 'TSK0321_WAITING_EVIDENCE_STALE')
req(blob('prototype/TSK-0321/POST_CR0007_REMEDIATION_CANDIDATE.css') == EXPECTED_CANDIDATE, 'TSK0321_WAITING_CANDIDATE_STALE')

p = Path('CURRENT_STATE.md')
text = p.read_text(encoding='utf-8')
marker = '## TSK-0321 current waiting state — 2026-09-01 — POST-CR-0007'
req(marker not in text, 'TSK0321_WAITING_SECTION_ALREADY_PRESENT')
req('APPROVE TSK-0321 POST-CR-0007 ACCESSIBILITY REMEDIATION AND REVIEW' not in text, 'TSK0321_WAITING_APPROVAL_COMMAND_ALREADY_PRESENT')

section = r'''

## TSK-0321 current waiting state — 2026-09-01 — POST-CR-0007

`TSK-0321 — Review design and content against accessibility requirements`: **WAITING / HUMAN_APPROVAL_REQUIRED** under current `A1 / HUMAN_ONLY` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4; hard dependencies `TSK-0323`, `TSK-0324`, `TSK-0333`; all three are current-qualified durable PASS.
- Historical 2026-08-29 TSK-0321 PASS/approval remains provenance only for the pre-account surface and does not approve this post-CR-0007 changed-scope review/remediation.
- Current authoritative integrated prototype remains unchanged: TSK-0333 `index.html` `934dc19d00cc9dd32e1ebc20c604373d153d4013`, `model.mjs` `fc25e4b1facc303840311e8ce186612eb8799212`, `app.mjs` `98659ba74a86d539b89664708bbcb830292486f8`, `prototype.css` `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.
- Current audit found one real accessibility defect in the authoritative source: at 320px with 200% text, document width expanded to 383px because nested grid/flex/action items retained intrinsic minimum sizing.
- HUMAN_ONLY remediation candidate `prototype/TSK-0321/POST_CR0007_REMEDIATION_CANDIDATE.css`, blob `eb5242880974a936121f362df0d960746a596795`, is preparation only and has **not** been applied to authoritative product source.
- Durable preparation evidence: `TSK_0321_POST_CR0007_INTEGRATED_ACCESSIBILITY_PREPARATION_EVIDENCE_2026-09-01.md`, blob `f9b970f67454b9354653030b192f8622ed2f57a3`.
- Final candidate verification run/job `33486312320 / 99787090076`: **SUCCESS** on self-hosted `adguardvm`. Focused 200% check changed 320px/383px failure to 320px/320px PASS; full current SafeWeb TSK-0333 Chromium regression PASS; full TSK-0321 mechanical accessibility review PASS with `1,500` checks across `28` unique screens; authoritative product source remained unmutated.
- Current review covers accountless setup plus optional account/provider/session/dashboard/device/destructive-lifecycle states, keyboard/focus/skip navigation, axe WCAG checks, target sizing, 320–1440 responsive layouts, 200% reflow, RTL, reduced motion, privacy/no-persistence/no-external-transport and console/page-error boundaries.
- No current critical accessibility defect remains in the verified candidate. Mechanical evidence does not fabricate real-user/assistive-technology human validation beyond the L4 task contract.
- Deterministic resolution condition is exact Project Owner approval: `APPROVE TSK-0321 POST-CR-0007 ACCESSIBILITY REMEDIATION AND REVIEW`.
- After approval only: apply the exact verified candidate to authoritative TSK-0333 CSS, read back its commit/blob, rerun focused 200% proof + full current SafeWeb TSK-0333 regression + full TSK-0321 suite on authoritative source with no overlay, create owner-bound final evidence, and reconcile PASS only if all current ACC/VER/EVD requirements remain proven.
- Until then TSK-0321 is non-PASS. No successor, LG-06, implementation, real-user validation, release or launch status is inferred.
'''

p.write_text(text.rstrip() + section.rstrip() + '\n', encoding='utf-8')
print('TSK0321_WAITING_RUNTIME_PRECONDITIONS=PASS')
print('TSK0321_WAITING_RUNTIME_SECTION=PREPARED')
