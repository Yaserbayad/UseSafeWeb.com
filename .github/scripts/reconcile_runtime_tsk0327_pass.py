from datetime import datetime, timezone
from pathlib import Path
import re

p=Path('CURRENT_STATE.md')
text=p.read_text(encoding='utf-8')
marker='## TSK-0327 critical/high findings disposition — 2026-08-29'
if marker in text:
    print('RUNTIME_TSK0327_ALREADY_RECONCILED=PASS')
    raise SystemExit(0)
now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text,n=re.subn(r'^\*\*Updated:\*\* .+$',f'**Updated:** {now}',text,count=1,flags=re.M)
if n!=1:
    raise SystemExit('Updated timestamp replacement failed')
block=f'''\n\n{marker}\n\n`TSK-0327 — Resolve critical usability, trust, and accessibility findings`: **PASS**.\n\n- Accepted artifact: `prototype/TSK-0327/FINDINGS_DISPOSITION.md` blob `69eb61673a195793b73c249d79436c631e7a1a36`, version `1.0.0`.\n- Durable evidence: `TSK_0327_CRITICAL_FINDINGS_DISPOSITION_EVIDENCE_2026-08-29.md`, blob `30460710026c732136c1af7e0c228555fcc3c8ea`.\n- ACC-0327/VER-0327/EVD-0327 are satisfied from the current source-backed/internal/automated evidence set. The current successful rendered retest remains source-current: run/job `33267199945` / `99139256895`, 218 browser checks PASS, target-environment truth-state/responsive/current automated accessibility/recovery/privacy checks PASS.\n- GitHub compare from retest head `309f0c51347610e6256535fffdabb8425dd7e115` through the findings disposition shows no accepted TSK-0310/TSK-0309 source change.\n- Zero unresolved critical/high pre-product findings are established. No product/UX correction was justified or made. The two known failures were closed verification-harness defects, not product defects.\n- This PASS does not self-certify HUMAN_ONLY design/accessibility work and does not create human comprehension evidence or release/production/payment/market/launch authority.\n\n### Exact next authoritative step\n\nRecompute current L4 eligibility from WBS/graph/gates and Action Authority with `TSK-0327=PASS`; continue the highest-priority AUTO_ALLOWED work and do not self-certify HUMAN_ONLY tasks.\n'''
p.write_text(text.rstrip()+block,encoding='utf-8')
print('RUNTIME_TSK0327_PASS_EDIT=PASS')
