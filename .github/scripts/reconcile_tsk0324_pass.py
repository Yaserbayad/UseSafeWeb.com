#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import re

path=Path('CURRENT_STATE.md')
text=path.read_text(encoding='utf-8')
marker='## TSK-0324 accepted stable state — 2026-08-29'
if marker in text:
    print('RUNTIME_TSK0324_ALREADY_PRESENT=PASS')
    raise SystemExit(0)
updated=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text,n=re.subn(r'^\*\*Updated:\*\* .*$',f'**Updated:** {updated}',text,count=1,flags=re.M)
if n!=1:
    raise SystemExit('CURRENT_STATE Updated marker not found exactly once')
section=r'''

## TSK-0324 accepted stable state — 2026-08-29

`TSK-0324 — Define lightweight visual identity and reusable UI component rules`: **PASS** under `ACC-0324 / VER-0324 / EVD-0324` and current `DEC-0052 / CR-0005` sequencing.

- Normative UX/UI consumer contract v1.0.0: `prototype/TSK-0324/UI_COMPONENT_RULES.md`, blob `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`, publication commit `cdd9e2987be1c7050682184220b81c75de7e4283`.
- Non-authoritative machine projection v1.0.0: `prototype/TSK-0324/COMPONENT_CONTRACT.json`, blob `dc1f767025c2b016274d247d997411128105c5e4`, publication commit `96ce10c87483cc8a13e7e88b231d923f7feafcaf`.
- Durable evidence: `TSK_0324_UI_COMPONENT_RULES_EVIDENCE_2026-08-29.md`, blob `8f192c58bdb3ed2538dd5570edf0b5e3f5814bf5`, publication commit `fd629b12259d8e88345a168fe30f6b93d12e3922`.
- Deterministic verification: run `33270916940`, job `99149118903`, self-hosted `adguardvm`; WBS/dependency/source-blob checks PASS; typography/spacing PASS; computed contrast/focus PASS; controls/feedback PASS; Protection Map states `6/6`; responsive/RTL/identity PASS; accessible component specs `13/13`; no design-system fork; repository clean.
- Current W3C WCAG 2.2 source review is recorded in EVD-0324. The historical ACC four-state minimum is satisfied by the current six-state S1-S6 authority without dropping S5/S6.
- TSK-0300 tokens/components remain unchanged. This PASS does not self-certify `TSK-0308`, which remains `HUMAN_ONLY`.
- `RSK-0002` remains OPEN. No behavioral/comprehension, production implementation, public publication, participant processing, payment, market activation or launch authority is inferred.

### Queue status after TSK-0324 reconciliation

Do not infer a successor from task numbering. Recompute eligible work from current WBS, dependencies, gates, runtime evidence and Action Authority after this state write/read-back.
'''
path.write_text(text.rstrip()+section.rstrip()+'\n',encoding='utf-8')
print('RUNTIME_TSK0324_EDIT=PASS')
