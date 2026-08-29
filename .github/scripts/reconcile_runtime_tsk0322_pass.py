from datetime import datetime, timezone
from pathlib import Path
import re

p=Path('CURRENT_STATE.md')
text=p.read_text(encoding='utf-8')
marker='## TSK-0322 product voice / claims / terminology — 2026-08-29'
if marker in text:
    print('RUNTIME_TSK0322_ALREADY_RECONCILED=PASS')
    raise SystemExit(0)
now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text,n=re.subn(r'^\*\*Updated:\*\* .+$',f'**Updated:** {now}',text,count=1,flags=re.M)
if n!=1: raise SystemExit('Updated timestamp replacement failed')
block=f'''\n\n{marker}\n\n`TSK-0322 — Create product voice, claims, and terminology guide`: **PASS**.\n\n- Guide: `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` blob `d12c1e707f0390915002b27bf3a5073d0135d466`, version `1.0.0`.\n- Machine policy: `content/TSK-0322/POLICY.json` blob `97c214504ceeeadebd92a79069e081311d60dd99`.\n- Durable evidence: `TSK_0322_PRODUCT_LANGUAGE_POLICY_EVIDENCE_2026-08-29.md`, blob `9cd540243be6855c28d709083ff30fa1ce7a73f6`.\n- Acceptance run/job: `33267585578` / `99140301619`; guide structure, source currency, state semantics, approved claims, representative content tasks and WBS/runtime authority all PASS.\n- Current visible identity is `SafeWeb`; S1-S6 labels remain TSK-0320 exact; no complete-safety, surveillance, fabricated-validation or public-authority claim is introduced.\n- ACC-0322/VER-0322/EVD-0322 satisfied.\n\n### Exact next authoritative step\n\nExecute `TSK-0323` against the accepted TSK-0322 policy and current source-backed instruction/state authorities; create the critical-path/error-state content library without inventing unsupported platform steps or strengthening claims.\n'''
p.write_text(text.rstrip()+block,encoding='utf-8')
print('RUNTIME_TSK0322_PASS_EDIT=PASS')
