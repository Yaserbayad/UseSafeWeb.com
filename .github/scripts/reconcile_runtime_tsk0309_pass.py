from datetime import datetime, timezone
from pathlib import Path
import re

p=Path('CURRENT_STATE.md')
text=p.read_text(encoding='utf-8')
marker='## TSK-0309 implementation-ready experience baseline — 2026-08-29'
if marker in text:
    print('RUNTIME_TSK0309_ALREADY_RECONCILED=PASS')
    raise SystemExit(0)

now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text,n=re.subn(r'^\*\*Updated:\*\* .+$',f'**Updated:** {now}',text,count=1,flags=re.M)
if n!=1:
    raise SystemExit('Updated timestamp replacement failed')

old='- `TSK-0309 — Freeze the implementation-ready experience baseline from current internal and automated acceptance evidence`: **TODO / eligible**. Its hard dependencies are satisfied under current semantics: `TSK-0310=PASS`; `TSK-0187=NOT_APPLICABLE+PASS` exclusion. It is L4, A3/AUTO_ALLOWED, and no current human-validation gate blocks it.'
new='- `TSK-0309 — Freeze the implementation-ready experience baseline from current internal and automated acceptance evidence`: **PASS**. Baseline `1.0.0` is frozen at `prototype/TSK-0309/`; durable evidence `TSK_0309_IMPLEMENTATION_READY_BASELINE_EVIDENCE_2026-08-29.md`, blob `b5944be85d9b60eb1ba4afdd31c151d340822e6e`. ACC-0309/VER-0309/EVD-0309 are satisfied.'
if text.count(old)!=1:
    raise SystemExit('TSK-0309 TODO runtime line replacement precondition failed')
text=text.replace(old,new,1)

block=f'''\n\n{marker}\n\n`TSK-0309`: **PASS**.\n\n- Frozen baseline: `prototype/TSK-0309/BASELINE.md` blob `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`, version `1.0.0`.\n- Machine-readable manifest: `prototype/TSK-0309/BASELINE_MANIFEST.json` blob `dba23b4593224b81361bab06bc3fa4332015d1b5`.\n- Durable evidence: `TSK_0309_IMPLEMENTATION_READY_BASELINE_EVIDENCE_2026-08-29.md`, blob `b5944be85d9b60eb1ba4afdd31c151d340822e6e`.\n- Final acceptance run/job: `33267199945` / `99139256895` on `adguardvm`; baseline/source/WBS/model checks PASS; retained Chromium `151.0.7922.34`; `BROWSER_ACCEPTANCE_CHECKS=218`; rendered regression PASS; npm audit 0 vulnerabilities; AdGuard/Nginx configs, listeners and failed-unit state unchanged.\n- No prototype product-code change was justified or made; current evidence establishes zero open critical/high pre-product defects for this contract.\n- No new account/dashboard/persistence scope or release/production/payment/market/launch authority is created.\n\n### Exact next authoritative step\n\nRecompute current eligibility from the WBS/graph/gates with `TSK-0309=PASS`; select the highest-priority actually eligible task under current action authority before further mutation.\n'''
text=text.rstrip()+block
p.write_text(text,encoding='utf-8')
print('RUNTIME_TSK0309_PASS_EDIT=PASS')
