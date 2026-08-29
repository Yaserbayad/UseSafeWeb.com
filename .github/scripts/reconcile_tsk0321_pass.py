#!/usr/bin/env python3
from pathlib import Path

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')
start_marker = '## TSK-0321 prepared HUMAN_ONLY accessibility-review boundary — 2026-08-29\n'
if s.count(start_marker) != 1:
    raise SystemExit(f'Expected exactly one TSK-0321 WAITING block, found {s.count(start_marker)}')
start = s.index(start_marker)
next_heading = s.find('\n## ', start + len(start_marker))
end = len(s) if next_heading < 0 else next_heading + 1
replacement = '''## TSK-0321 accepted accessibility-review state — 2026-08-29

`TSK-0321 — Review design and content against accessibility requirements`: **PASS** under `ACC-0321 / VER-0321 / EVD-0321`. The Project Owner explicitly approved `APPROVE TSK-0321 ACCESSIBILITY REMEDIATION AND REVIEW` at 2026-08-29T22:41:21Z. The exact approved remediation candidate was applied to authoritative TSK-0310 at commit `181a5f4a420b6b2bcec29daf4370dcb7857ba499`; updated stylesheet blob `004b0b34c0e5d94e3eacbeae25710284ef9a7886`.

- Final acceptance evidence: `TSK_0321_ACCESSIBILITY_REVIEW_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `7ab9dd2467ca8ad755ef308c4b2ecade71023be8`.
- Final authoritative verification run/job: `33279388546` / `99171833940`: SUCCESS.
- Original TSK-0310 rendered regression suite: `218/218` checks PASS; `TSK0310_RENDERED_REACCEPTANCE=PASS`. TSK-0310 therefore remains PASS after the approved stylesheet mutation.
- TSK-0321 accessibility suite on actual authoritative source: `667/667` checks PASS; `A11Y_FAILURES=0`; `A11Y_ACCEPTANCE_FAILURES=0`; `TSK0321_AUTHORITATIVE_ACCESSIBILITY_REVIEW=PASS`.
- Production invariants: AdGuard/Nginx active; AdGuard config, Nginx config, listeners and failed-unit set unchanged; no temporary listener remains; package delta empty; repository clean.
- Retained noncritical integrated-product accessibility notes: `A11Y-LIVE-001` (scope broad live-region behavior during later screen-reader verification) and `A11Y-SKIP-001` (add a keyboard bypass mechanism when the production shell has repeated navigation). These are not current critical barriers and are not discarded.
- Initial final-verifier run `33279326137` / `99171670004` failed before product assertions due only to temporary npm `ENOLOCK`; source identity/pre/post host checks passed, the verifier setup was corrected, and the complete subsequent run passed.
- `CR-0005 / DEC-0052` sequencing remains unchanged. No real-participant validation, legal/privacy completion, public publication, payment, market activation or launch authority is inferred.

'''
s2 = (s[:start] + replacement + s[end:]).rstrip('\n') + '\n'
if 'TSK-0321 — Review design and content against accessibility requirements`: **WAITING / non-PASS**' in s2:
    raise SystemExit('Stale TSK-0321 WAITING text remains')
if s2.count('## TSK-0321 accepted accessibility-review state — 2026-08-29') != 1:
    raise SystemExit('PASS block not unique')
p.write_text(s2, encoding='utf-8')
print('RUNTIME_TSK0321_PASS_EDIT=PASS')
