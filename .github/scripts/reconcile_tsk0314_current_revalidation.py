from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME="fb051be724892e1e49d9de3e93b485406649518f"
EXPECTED={
    'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0314_POST_CR0008_DUAL_MODE_ACCESSIBILITY_BROWSER_DEVICE_NFR_REVALIDATION_2026-09-02.md':'e193abd8398d2c91bc113dfc88ad605e67b475f6',
    'TSK_0314_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'924d93313eed32daf5811650758fef2955fad738',
    'TSK_0046_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'0d01804887723c76edc2a8426dfa00585944b84b',
}
NEW='## TSK-0314 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE ACCESSIBILITY/BROWSER/DEVICE NFR REVALIDATION'

def blob(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
def sections(text): return [m.group(0) for m in re.finditer(r'^## TSK-\d{4} current accepted stable state.*?(?=^## |\Z)',text,re.M|re.S)]

for p,sha in EXPECTED.items():
    actual=blob(p)
    if actual!=sha: raise SystemExit(f'hash mismatch {p}: {actual} != {sha}')
state_path=Path('CURRENT_STATE.md'); state=state_path.read_text(encoding='utf-8')
if NEW in state:
    m=re.search(r'^'+re.escape(NEW)+r'.*?(?=^## |\Z)',state,re.M|re.S)
    required=['**PASS**','TSK_0314_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md','33582350458 / 100099089873','`AUTO_ALLOWED`']
    if m and all(x in m.group(0) for x in required):
        print('TSK0314_CURRENT_STATE_ALREADY_APPLIED=PASS'); raise SystemExit(0)
    raise SystemExit('ambiguous existing TSK-0314 current section')
if blob('CURRENT_STATE.md')!=PRE_RUNTIME: raise SystemExit('pre-runtime blob mismatch; refuse stale write')
if not state.endswith('\n'): raise SystemExit('CURRENT_STATE.md must end with newline')
before=sections(state)
for tid in ['TSK-0299','TSK-0485','TSK-0318','TSK-0319','TSK-0301','TSK-0316','TSK-0300','TSK-0317','TSK-0310','TSK-0484','TSK-0538','TSK-0046']:
    if not any(s.startswith(f'## {tid} current accepted stable state') for s in before): raise SystemExit('missing protected current section '+tid)
ev=Path('TSK_0314_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in ['**ACC-0314 = PASS.**','**VER-0314 = PASS.**','**EVD-0314 = SATISFIED.**','33582350458 / 100099089873','TSK0314_CURRENT_REVALIDATION=PASS']:
    if token not in ev: raise SystemExit('evidence token missing: '+token)
append=r'''## TSK-0314 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE ACCESSIBILITY/BROWSER/DEVICE NFR REVALIDATION

`TSK-0314 — Define accessibility, responsive, browser, OS, and device support NFRs`: **PASS** under current `ACC-0314 / VER-0314 / EVD-0314`, current direct predecessor TSK-0046, `DEC-0053/CR-0006` dual-mode scope and `DEC-0054/CR-0007` production-only lifecycle semantics.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A4 / `AUTO_ALLOWED`; dependency exactly `TSK-0046`.
- Current artifact `TSK_0314_POST_CR0008_DUAL_MODE_ACCESSIBILITY_BROWSER_DEVICE_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `e193abd8398d2c91bc113dfc88ad605e67b475f6`, publication commit `71cfd0c44512808232f6ea6a019dd1b5ca3dd967`.
- Current durable evidence `TSK_0314_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `924d93313eed32daf5811650758fef2955fad738`, publication commit `62147a0011966e9fed162a45ed35f0b9dd1b56a1`.
- Independent read-only VER-0314 workflow blob `7a74e23fc573d953e9e035f46310fdc8517b9a75`; run/job `33582350458 / 100099089873`: **SUCCESS** with `contents: read`.
- Earlier runs `33582215492 / 100098677323` and `33582284284 / 100098891745` are diagnostic-only verifier wording failures; they did not mutate governed state or change the accepted artifact.
- WCAG 2.2 AA remains the target; keyboard/focus, screen-reader semantics, 200% resize, 320 CSS px reflow, contrast, target-size, reduced-motion, responsive/RTL and four-tier testing requirements remain binding for implemented critical public/product flows.
- Approved optional sign-in/session/dashboard/device/account-lifecycle surfaces receive the same accessibility, localization and support-state obligations as the accountless core; account/login/dashboard state cannot upgrade technical protection evidence.
- Release-time browser/OS support remains evidence-driven. Current 2026-09-02 source snapshot records Chrome 152 Stable, Firefox 155 Release, Edge 152 Stable with 153 not yet Stable, iOS/iPadOS 26.6.1, macOS 26.6.2/Safari 26.6.1, and the August 2026 Android bulletin as the latest published Android bulletin on this date. Exact release versions must be refreshed at each release boundary.
- Web UI support remains separate from DNS setup/mechanism support and from current Protection Map verification state.
- Current TSK-0046 performance/capacity requirements cannot trade away accessibility correctness or support-state truthfulness.
- **Non-inference:** L4 NFR-definition PASS only; no implemented WCAG conformance, assistive-technology execution, real-user accessibility evidence, public support promise, DNS support expansion, implementation/build, legal/privacy completion, participant/publication/payment/market/launch, gate or successor PASS is inferred.

### Queue status after current TSK-0314 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
'''
stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
base,count=re.subn(r'^\*\*Updated:\*\* .+$','**Updated:** '+stamp,state,count=1,flags=re.M)
if count!=1: raise SystemExit('Updated header replacement failed')
result=base+append
after=sections(result)
if len(after)!=len(before)+1: raise SystemExit('current section count changed unexpectedly')
for s in before:
    if s not in after: raise SystemExit('existing current accepted-state section changed')
if sum(1 for s in after if s.startswith(NEW))!=1: raise SystemExit('new TSK-0314 section count invalid')
state_path.write_text(result,encoding='utf-8')
check=state_path.read_text(encoding='utf-8'); check_sections=sections(check)
for s in before:
    if s not in check_sections: raise SystemExit('post-write existing current section changed')
print('PROTECTED_CURRENT_SECTION_COUNT='+str(len(before)))
print('ALL_EXISTING_CURRENT_ACCEPTED_SECTIONS_PRESERVED=PASS')
print('TSK0314_CURRENT_STATE_RECONCILIATION=PASS')
