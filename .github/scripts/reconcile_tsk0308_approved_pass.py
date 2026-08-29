#!/usr/bin/env python3
from pathlib import Path
import re

path = Path('CURRENT_STATE.md')
text = path.read_text(encoding='utf-8')
old_heading = '## TSK-0308 prepared HUMAN_ONLY decision boundary — 2026-08-29'
new_heading = '## TSK-0308 accepted stable state — 2026-08-29'
evidence = '343961f30bc46a20762ad2b0108a4afe9593e5a3'

if new_heading in text:
    section = text[text.index(new_heading):]
    assert '**PASS**' in section
    assert evidence in section
    print('RUNTIME_TSK0308_PASS_NOOP=PASS')
    raise SystemExit(0)

if old_heading not in text:
    raise SystemExit('Expected TSK-0308 WAITING boundary not found')

start = text.index(old_heading)
next_match = re.search(r'^## (?!#)', text[start + len(old_heading):], re.M)
if next_match:
    end = start + len(old_heading) + next_match.start()
else:
    end = len(text)

replacement = f'''{new_heading}

`TSK-0308 — Create the shared responsive design system for public and product surfaces`: **PASS**.

- Project Owner HUMAN_ONLY approval received at `2026-08-29T21:42:01Z`: exact disposition `APPROVE TSK-0308 CANDIDATE`.
- Approved immutable candidate v1.0.0-candidate: `prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md`, blob `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4`.
- Candidate composition CSS blob `de5571379ff240f36b5aecd50f555a07176dbd32`; reference surface blob `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862`; deterministic map blob `cd83279cdf5381cd7dae3feb177439158c1f9197`; requirement/interface trace blob `5e34ce9c192c6af65ba493cb356adb964c3d30b6`.
- Final acceptance evidence: `TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `{evidence}`.
- `ACC-0308=SATISFIED`; `VER-0308=PASS`; `EVD-0308=SATISFIED`.
- Final technical verification remains run `33273620531` / job `99156419342`: components `13/13`, required state classes `6/6`, protection states `6/6`, requirement/interface trace `8/8`, Chromium viewports `320/768/1024/1440`, visible focus, reduced motion, RTL/LTR isolation, target-size floor, browser console and repository-clean checks PASS.
- GitHub compare from verification commit `836208641efccd2325409cb41c22a8d3692796b6` to pre-acceptance head `c4c28aef711f862d19d6316659593c0f1e83dfcf` proved no approved candidate or bound source artifact changed before approval processing.
- TSK-0300 remains sole shared token/primitive authority; TSK-0308 accepts responsive composition/state/accessibility/localization/recovery specifications without creating a second token/design system.
- `RSK-0002` remains OPEN. `DEC-0052 / CR-0005` sequencing remains unchanged. No real-user/native-speaker validation, legal/privacy completion, production build, publication, participant processing, payment, market activation or launch authority is inferred.

### Queue status after TSK-0308 acceptance

Do not infer a successor from task numbering. Recompute current eligibility from WBS, dependencies, gates, runtime evidence and Action Authority after this state write/read-back.
'''

new_text = text[:start].rstrip() + '\n\n' + replacement.rstrip() + '\n'
if end < len(text):
    new_text += '\n' + text[end:].lstrip('\n')
path.write_text(new_text, encoding='utf-8')
print('RUNTIME_TSK0308_PASS_EDIT=PASS')
