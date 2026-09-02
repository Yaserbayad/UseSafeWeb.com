from __future__ import annotations
import re,subprocess
from datetime import datetime,timezone
from pathlib import Path
PRE='60364cebcdf91f052311a40e3af83f6c984fb18f'
EXPECTED={'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616','Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032','TSK_0045_POST_CR0008_DUAL_MODE_MAINTAINABILITY_DEPLOYMENT_COST_NFR_REVALIDATION_2026-09-02.md':'0df1b4747afea4521e4e98b0728c83750ed2b547','TSK_0045_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'50114d20c3422d2546ba046538bc0bda9a00ef49','TSK_0314_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'924d93313eed32daf5811650758fef2955fad738'}
NEW='## TSK-0045 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE MAINTAINABILITY/DEPLOYMENT/COST NFR REVALIDATION'
def blob(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
def sections(t): return [m.group(0) for m in re.finditer(r'^## TSK-\d{4} current accepted stable state.*?(?=^## |\Z)',t,re.M|re.S)]
for p,h in EXPECTED.items():
    a=blob(p)
    if a!=h: raise SystemExit(f'hash mismatch {p}: {a} != {h}')
p=Path('CURRENT_STATE.md'); state=p.read_text(encoding='utf-8')
if NEW in state:
    m=re.search(r'^'+re.escape(NEW)+r'.*?(?=^## |\Z)',state,re.M|re.S)
    req=['**PASS**','TSK_0045_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md','33582987002 / 100101061365','`AUTO_ALLOWED`']
    if m and all(x in m.group(0) for x in req): print('TSK0045_CURRENT_STATE_ALREADY_APPLIED=PASS'); raise SystemExit(0)
    raise SystemExit('ambiguous existing TSK-0045 current section')
if blob('CURRENT_STATE.md')!=PRE: raise SystemExit('pre-runtime blob mismatch; refuse stale write')
if not state.endswith('\n'): raise SystemExit('runtime must end newline')
before=sections(state)
for tid in ['TSK-0299','TSK-0485','TSK-0318','TSK-0319','TSK-0301','TSK-0316','TSK-0300','TSK-0317','TSK-0310','TSK-0484','TSK-0538','TSK-0046','TSK-0314']:
    if not any(s.startswith(f'## {tid} current accepted stable state') for s in before): raise SystemExit('missing protected '+tid)
ev=Path('TSK_0045_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in ['**ACC-0045 = PASS.**','**VER-0045 = PASS.**','**EVD-0045 = SATISFIED.**','33582987002 / 100101061365','TSK0045_CURRENT_REVALIDATION=PASS']:
    if token not in ev: raise SystemExit('missing evidence token '+token)
append=r'''## TSK-0045 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE MAINTAINABILITY/DEPLOYMENT/COST NFR REVALIDATION

`TSK-0045 — Define maintainability, deployment, and cost-control NFRs`: **PASS** under current `ACC-0045 / VER-0045 / EVD-0045`, current direct predecessor TSK-0314, CR-0006 dual-mode scope and CR-0007 production-only/autonomy semantics.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0314`.
- Current artifact `TSK_0045_POST_CR0008_DUAL_MODE_MAINTAINABILITY_DEPLOYMENT_COST_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `0df1b4747afea4521e4e98b0728c83750ed2b547`, publication commit `8a87baff9599d70b66de8e308b24c467b9bb1c6c`.
- Current durable evidence `TSK_0045_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `50114d20c3422d2546ba046538bc0bda9a00ef49`, publication commit `049da0fd24721dd49b4e56464ab022017092281e`.
- Independent read-only VER-0045 final workflow blob `a9bee09c494027ea187769744b181ec3f770305e`; run/job `33582987002 / 100101061365`: **SUCCESS**.
- v1/v2 verifier runs `33582857623 / 100100660777` and `33582933326 / 100100896434` are diagnostic-only wording failures; they changed no accepted artifact/state.
- Deterministic deployment/read-back/version/rollback/drift/documentation/dependency-review and cost-control semantics remain binding, extended to optional account/provider/datastore lifecycle without weakening the complete accountless core.
- CR-0007 current authority allows routine reversible technical deployment/recovery/patching/scaling inside approved architecture/budget when evidence/gates permit; owner-provided Azure VM/control-plane creation, material/unbudgeted spend, new contracts, identity/organizational acts, named-market activation and frozen-scope change retain human authority.
- No mandatory staging/pilot environment is created. Pre-release verification remains mandatory; first users are live-production users only after LG-09 and all applicable prerequisites.
- Infrastructure currency budget remains `UNFROZEN`. Azure cost attribution must verify usage records; parent tag presence alone is not cost proof. Budgets/alerts are monitoring/accountability controls, not automatic service-stop authority.
- TSK-0314 accessibility/browser/device and TSK-0046/0538 performance/reliability constraints remain deployment regression invariants.
- **Non-inference:** L4 NFR-definition PASS only; no Azure mutation/spend/deployment, web/auth/datastore implementation, legal/privacy completion, participant/publication/payment/market/launch, gate or successor PASS is inferred.

### Queue status after current TSK-0045 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
'''
stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
base,n=re.subn(r'^\*\*Updated:\*\* .+$','**Updated:** '+stamp,state,count=1,flags=re.M)
if n!=1: raise SystemExit('updated header failure')
result=base+append; after=sections(result)
if len(after)!=len(before)+1: raise SystemExit('section count mismatch')
for s in before:
    if s not in after: raise SystemExit('existing current section changed')
if sum(1 for s in after if s.startswith(NEW))!=1: raise SystemExit('new section count invalid')
p.write_text(result,encoding='utf-8')
check=sections(p.read_text(encoding='utf-8'))
for s in before:
    if s not in check: raise SystemExit('post-write existing section changed')
print('PROTECTED_CURRENT_SECTION_COUNT='+str(len(before)))
print('ALL_EXISTING_CURRENT_ACCEPTED_SECTIONS_PRESERVED=PASS')
print('TSK0045_CURRENT_STATE_RECONCILIATION=PASS')
