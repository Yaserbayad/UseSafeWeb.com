#!/usr/bin/env python3
from pathlib import Path

path = Path('CURRENT_STATE.md')
text = path.read_text(encoding='utf-8')
marker = '## TSK-0308 prepared HUMAN_ONLY decision boundary — 2026-08-29'

if marker in text:
    print('RUNTIME_TSK0308_PREPARATION_NOOP=PASS')
    raise SystemExit(0)

section = r'''## TSK-0308 prepared HUMAN_ONLY decision boundary — 2026-08-29

`TSK-0308 — Create the shared responsive design system for public and product surfaces`: **WAITING / non-PASS**. The complete candidate has been prepared and technically verified, but WBS Action Authority is `HUMAN_ONLY`; Project Owner approval has not yet been given and must not be inferred from preparation authority.

- Normative candidate v1.0.0-candidate: `prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md`, blob `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4`.
- Candidate composition CSS: `prototype/TSK-0308/candidate.css`, blob `de5571379ff240f36b5aecd50f555a07176dbd32`; no raw brand palette, local shared token declarations, local font stack or external asset URL.
- Internal reference surface: `prototype/TSK-0308/reference.html`, blob `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862`.
- Machine verification projection: `prototype/TSK-0308/DESIGN_SYSTEM_MAP.json`, blob `cd83279cdf5381cd7dae3feb177439158c1f9197`.
- Requirement/interface trace: `prototype/TSK-0308/REQUIREMENT_INTERFACE_TRACE.md`, blob `5e34ce9c192c6af65ba493cb356adb964c3d30b6`; current bindings `REQ-0028`, `REQ-0029`, `REQ-0030`, `CON-0010`, `CON-0017`, `CON-0022`, `INT-0009`, `INT-0010` all covered.
- Durable preparation evidence: `TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_PREPARATION_EVIDENCE_2026-08-29.md`, blob `a03ba55d4228b8debde5b1a6fff42fa0ea136cfd`.
- Final preparation verification: run `33273620531`, job `99156419342`, self-hosted `adguardvm`, Node `v22.23.2`, Playwright `1.62.0`; WBS/dependencies/source/candidate blobs PASS; requirement/interface trace `8/8`; components `13/13`; required state classes `6/6`; protection states `6/6`; responsive/localization/no-fork/account-support-truth fences PASS; Chromium viewports `320/768/1024/1440` PASS; visible focus, reduced motion, RTL/LTR isolation, target-size floor, browser console and repository-clean checks PASS.
- Candidate remains deliberately lightweight: TSK-0300 continues to own shared tokens/primitives; TSK-0308 adds responsive composition/state/recovery specifications rather than a second design/token system.
- `RSK-0002` remains OPEN. No real-user/native-speaker validation, legal completion, production build, publication, participant processing, payment, market activation or launch authority is inferred. CR-0005 sequencing remains unchanged.

### Deterministic resolution condition

Project Owner must provide one explicit disposition for this exact candidate version:

- `APPROVE TSK-0308 CANDIDATE`; or
- `REVISE TSK-0308: <specific change>`.

Only explicit approval authorizes final `VER-0308 / EVD-0308` acceptance processing and potential runtime PASS. Preparation evidence alone is insufficient for PASS.
'''

new_text = text.rstrip() + '\n\n' + section.rstrip() + '\n'
path.write_text(new_text, encoding='utf-8')
print('RUNTIME_TSK0308_PREPARATION_EDIT=PASS')
