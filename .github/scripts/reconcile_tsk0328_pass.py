#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import re

path=Path('CURRENT_STATE.md')
text=path.read_text(encoding='utf-8')
marker='## TSK-0328 accepted stable state — 2026-08-29'
if marker in text:
    print('RUNTIME_TSK0328_ALREADY_PRESENT=PASS')
    raise SystemExit(0)
updated=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text,n=re.subn(r'^\*\*Updated:\*\* .*$',f'**Updated:** {updated}',text,count=1,flags=re.M)
if n!=1:
    raise SystemExit('CURRENT_STATE Updated marker not found exactly once')
section=r'''

## TSK-0328 accepted stable state — 2026-08-29

`TSK-0328 — Define information architecture and navigation model`: **PASS** under `ACC-0328 / VER-0328 / EVD-0328` and current `DEC-0052 / CR-0005` sequencing.

- Normative IA/navigation contract v1.0.0: `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md`, blob `4efb624005061e242e427994953d0fc00fcd745f`, publication commit `908871d1474645b8939a32a1c94f5433e8c3a716`.
- Non-authoritative machine projection v1.0.0: `prototype/TSK-0328/IA_MAP.json`, blob `2f77c1a844f16cf080817bf4ea31c80bb7067a06`, publication commit `7108fe18205ec95c013ab152c8055a69a25013f5`.
- Durable evidence: `TSK_0328_INFORMATION_ARCHITECTURE_NAVIGATION_EVIDENCE_2026-08-29.md`, blob `8e5274307674c05183dd063e49bdbe66cf23ef8d`, publication commit `cb62f8c88798f1840a49a49d23ca97cf52eaea55`.
- Final deterministic verification: run `33271356007`, job `99150274452`, self-hosted `adguardvm`; WBS/dependency/source blobs PASS; systems `2/2`; public routes `6/6`; setup logical screens `15/15` with goal/requirement trace; required paths `8/8`; accountless/no-unnecessary-sections, navigation-state/privacy, accessibility/RTL and repository-clean checks PASS.
- First run `33271313226` / job `99150159697` stopped on a verifier prose-string false negative. The IA artifacts were unchanged; the corrected full verifier reran and passed. See EVD-0328.
- `TSK-0308` and `TSK-0321` remain `HUMAN_ONLY` and are not self-certified. `RSK-0002` remains OPEN.
- This PASS is internal L4 information-architecture evidence only and does not imply real-parent/native-speaker comprehension, production implementation, public publication, participant processing, payment, market activation or launch authority.

### Queue status after TSK-0328 reconciliation

Do not infer a successor from task numbering. Recompute current eligibility from WBS, dependencies, gates, runtime evidence and Action Authority after this state write/read-back.
'''
path.write_text(text.rstrip()+section.rstrip()+'\n',encoding='utf-8')
print('RUNTIME_TSK0328_EDIT=PASS')
