#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import re

path = Path('CURRENT_STATE.md')
text = path.read_text(encoding='utf-8')
marker = '## TSK-0325 accepted stable state — 2026-08-29'
if marker in text:
    print('RUNTIME_TSK0325_ALREADY_PRESENT=PASS')
    raise SystemExit(0)

updated = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text, n = re.subn(r'^\*\*Updated:\*\* .*$', f'**Updated:** {updated}', text, count=1, flags=re.M)
if n != 1:
    raise SystemExit('CURRENT_STATE Updated marker not found exactly once')

section = r'''

## TSK-0325 accepted stable state — 2026-08-29

`TSK-0325 — Create end-to-end parent journey and service blueprint`: **PASS** under `ACC-0325 / VER-0325 / EVD-0325` and current `DEC-0052 / CR-0005` sequencing.

- Normative blueprint v1.0.0: `prototype/TSK-0325/SERVICE_BLUEPRINT.md`, blob `1701f5f7b13ac8f7fa3092e39005b3da7627c89f`, publication commit `6203b699618ef09ad07c5e26cb232d71dede3887`.
- Non-authoritative acceptance projection v1.0.0: `prototype/TSK-0325/ACCEPTANCE_MATRIX.json`, blob `aee3ead9756f10fb829e948f3ca00336ee0780b3`, publication commit `4c17e37d597044859748d2a934897f5794375ff4`.
- Durable evidence: `TSK_0325_PARENT_JOURNEY_SERVICE_BLUEPRINT_EVIDENCE_2026-08-29.md`, blob `b6895c2d0de21c21def0aa9b6433c60b2315b550`, publication commit `2eace354398e9e4bfc01d1a68cb03eeb608ceb35`.
- Deterministic verification: run `33270478672`, job `99147944373`, self-hosted `adguardvm`; WBS/dependency/source-blob checks PASS; required paths `8/8`; touchpoint requirement traces `13/13`; current TSK-0323 instruction bindings `12/12`; state truth/accountless/privacy/i18n/claims checks PASS; repository clean.
- Sole dependency `TSK-0326` remains `NOT_APPLICABLE + PASS` only as the verified CR-0005 pre-product-human-validation exclusion; no behavioral evidence is inferred.
- `RSK-0002` remains OPEN. This PASS is internal L4 service-blueprint acceptance and does not imply parent comprehension/usability evidence, production implementation, public release, participant processing, payment, market activation, or launch authority.

### Queue status after TSK-0325 reconciliation

Do not infer a successor from task numbering. Recompute eligible work from the current WBS, graph, gates, runtime evidence and Action Authority after this state write/read-back.
'''

path.write_text(text.rstrip() + section.rstrip() + '\n', encoding='utf-8')
print('RUNTIME_TSK0325_EDIT=PASS')
