from pathlib import Path
import os
import subprocess


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'rev-parse', f'HEAD:{path}'], text=True).strip()

verification_commit = os.environ['VERIFICATION_COMMIT']
run_id = os.environ['RUN_ID']

evidence = Path('TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md')
evidence.write_text(
    f"""# TSK-0321 — Post-CR-0007 Final Integrated Accessibility Evidence

**Task:** `TSK-0321 — Review design and content against accessibility requirements`  
**Date:** 2026-09-01  
**Disposition:** `PASS` only after owner-approved remediation and authoritative no-overlay review.  
**Owner authority:** exact approval received: `APPROVE TSK-0321 POST-CR-0007 ACCESSIBILITY REMEDIATION AND REVIEW`.

## Proven current boundary

- WBS blob: `{blob('Plans/Master/WBS/master-wbs.csv')}`.
- Authoritative TSK-0333 index/model/app blobs: `{blob('prototype/TSK-0333/index.html')}` / `{blob('prototype/TSK-0333/model.mjs')}` / `{blob('prototype/TSK-0333/app.mjs')}`.
- Authoritative remediated CSS blob: `{blob('prototype/TSK-0333/prototype.css')}`.
- Verification workflow blob: `{blob('.github/workflows/verify-tsk0321-post-cr0007-accessibility-20260901.yml')}`.
- Verification script blob: `{blob('.github/scripts/verify_tsk0321_post_cr0007_accessibility_browser_20260901.mjs')}`.
- Verification source commit: `{verification_commit}`.
- GitHub Actions run: `{run_id}` on self-hosted `adguardvm`.

## Required post-approval verification

All commands below completed successfully against the authoritative `prototype/TSK-0333` source with no remediation overlay:

1. Focused 320px / 200% text proof: **PASS**.
2. Full current SafeWeb TSK-0333 Chromium regression: **PASS**.
3. Full post-CR-0007 TSK-0321 mechanical accessibility suite: **PASS**.
4. Product source identity remained unchanged during the review: **PASS**.

The owner-approved candidate is now the authoritative CSS. The prior preparation-only evidence remains provenance. No real-user/assistive-technology validation, successor PASS, LG-06 PASS, implementation, production activation, participant processing, publication or launch is inferred beyond the current L4 contract.
""",
    encoding='utf-8',
)

state = Path('CURRENT_STATE.md')
text = state.read_text(encoding='utf-8')
start_heading = '## TSK-0321 current waiting state — 2026-09-01 — POST-CR-0007'
start = text.find(start_heading)
if start < 0:
    raise SystemExit('TSK0321_WAITING_SECTION_NOT_FOUND')
next_heading = text.find('\n## ', start + len(start_heading))
if next_heading < 0:
    next_heading = len(text)
replacement = f"""## TSK-0321 current accepted stable state — 2026-09-01 — POST-CR-0007

`TSK-0321 — Review design and content against accessibility requirements`: **PASS** under the current post-CR-0007 task contract, after exact Project Owner approval and authoritative remediation/review.

- Owner approval: `APPROVE TSK-0321 POST-CR-0007 ACCESSIBILITY REMEDIATION AND REVIEW`.
- Current WBS blob `{blob('Plans/Master/WBS/master-wbs.csv')}`: L4; hard dependencies `TSK-0323`, `TSK-0324`, `TSK-0333`; all remain current-qualified PASS.
- Authoritative remediated TSK-0333 CSS blob: `{blob('prototype/TSK-0333/prototype.css')}`; index/model/app remain `{blob('prototype/TSK-0333/index.html')}` / `{blob('prototype/TSK-0333/model.mjs')}` / `{blob('prototype/TSK-0333/app.mjs')}`.
- Durable final evidence: `TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md`.
- Authoritative verification source commit `{verification_commit}`; GitHub Actions run `{run_id}` on self-hosted `adguardvm`: focused 320px/200% proof PASS; full current SafeWeb TSK-0333 Chromium regression PASS; full post-CR-0007 TSK-0321 accessibility suite PASS; source unchanged during review.
- The prior 320px/200% horizontal overflow defect is remediated in authoritative source. No current critical accessibility defect remains within the verified L4 mechanical review boundary.
- Mechanical evidence does not fabricate real-user/assistive-technology validation beyond the L4 contract.
- Non-inference fence: this PASS does not self-certify any successor, `LG-06`, implementation, real-user validation, publication, production activation, participant processing, payment, market activation or launch.

### Queue status after TSK-0321 acceptance

Recompute successor eligibility from current WBS dependencies, graph, gates, runtime evidence and Action Authority; do not infer eligibility from task numbering.
"""
state.write_text(text[:start] + replacement + text[next_heading:], encoding='utf-8')
