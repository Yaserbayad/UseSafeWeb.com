from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME='a09b3c3a9dece3ec19c21d5bf5f1fdd2f004b482'
EXPECTED={
    'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md':'285ee390499190137e8aac0fed976975fb79ed80',
    'TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'a7461f68f99ccda5c947a4ee77453817db9db1e5',
    'TSK_0485_END_TO_END_THREAT_ABUSE_MODEL_2026-09-01.md':'373ac62ba1f244328e7d8e52ae6648d72e5a5ed7',
    'TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFRS_2026-09-01.md':'eda85b062a3a7ba29544de35a8a813c9790092f2',
}
NEW='## TSK-0484 current accepted stable state — 2026-09-02 — POST-CR-0008 SECURITY NFR REVALIDATION'

def blob(path): return subprocess.check_output(['git','hash-object',path],text=True).strip()
for path,expected in EXPECTED.items():
    if not Path(path).exists(): raise SystemExit('missing guarded input: '+path)
    actual=blob(path)
    if actual!=expected: raise SystemExit(f'hash mismatch {path}: {actual} != {expected}')

p=Path('CURRENT_STATE.md')
state=p.read_text(encoding='utf-8')
if NEW in state:
    section=state[state.index(NEW):]
    required=['**PASS**','TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md','33579079770 / 100089332047','`AUTO_ALLOWED`','16 current threat-mapped measurable security NFRs']
    if all(x in section for x in required):
        print('TSK0484_CURRENT_STATE_ALREADY_APPLIED=PASS'); raise SystemExit(0)
    raise SystemExit('ambiguous existing current TSK-0484 section')
if blob('CURRENT_STATE.md')!=PRE_RUNTIME: raise SystemExit('pre-runtime blob mismatch; refuse stale write')
if not state.endswith('\n'): raise SystemExit('CURRENT_STATE.md must end with newline')

evidence=Path('TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in ['TSK-0484 current security and abuse-resistance NFR revalidation: PASS.','ACC-0484 = PASS. VER-0484 = PASS. EVD-0484 = SATISFIED.','33579079770 / 100089332047','TSK0484_16_NFR_THREAT_CONTROL_VERIFICATION_MAP=PASS','TSK0484_CURRENT_ACC=PASS']:
    if token not in evidence: raise SystemExit('missing evidence token: '+token)

append=r'''## TSK-0484 current accepted stable state — 2026-09-02 — POST-CR-0008 SECURITY NFR REVALIDATION

`TSK-0484 — Define security and abuse-resistance NFRs`: **PASS** under current `ACC-0484 / VER-0484 / EVD-0484`, current dependency TSK-0230, current TSK-0485 30-threat/10-boundary model, current dual-mode Version-1 scope and refreshed first-party security-source review.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0230`.
- Current artifact `TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `285ee390499190137e8aac0fed976975fb79ed80`, publication commit `45ce41549d878fcf7875d880803a9134d075555f`.
- Current evidence `TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `a7461f68f99ccda5c947a4ee77453817db9db1e5`, publication commit `d4fb458003e72cb3d07b8421dbb7c03b7a86be80`.
- Independent read-only VER-0484 final workflow blob `b12ec1801dee4afe633fafb8830fc2be7498a07d`; run/job `33579079770 / 100089332047`: **SUCCESS**.
- The historical TSK-0484 contract explicitly reopened itself when account/authentication or persistent customer storage was introduced; CR-0006 activated optional parent auth/session and minimum persistent parent/device/dashboard state, so this was a genuine current-boundary requalification rather than date-only refresh.
- Current TSK-0485 supplies all 30 threat rows and 10 trust boundaries; current TSK-0230 supplies the accountless/account/session/device/ClientID/privacy/deletion boundary.
- Sixteen current threat-mapped measurable security NFRs are accepted across resolver abuse, web/application, authentication, session, authorization, persistent-data consistency, provider failure, AdGuard control, privacy, anonymous state, truthful protection state, CI/supply-chain, recovery and source-backed guidance.
- Public resolver abuse/availability remains distinct from application/user-data security. Authentication never substitutes for authorization; parent/device ownership is server-enforced; ClientID is never a credential or authorization token; account/configuration presence is never technical protection evidence.
- No browsing/query/activity-history product store is authorized through account, dashboard, analytics, diagnostics or backup paths. J0/J1 and account domains remain separate.
- High/Critical current-release threat paths remain release-blocking until their implementation and blocking target-environment verification actually succeed.
- TSK-0353 retains detailed authentication/session/security-NFR ownership; TSK-0352 retains exact typed/allowlisted AdGuard API/ClientID lifecycle ownership. Neither task is inferred PASS.
- **Non-inference:** L4 security-NFR definition PASS only; no application/authentication/datastore implementation, provider activation, production security, final legal/privacy compliance, TSK-0352/0353, later gate, participant, publication, payment, market activation or launch PASS is inferred.

### Queue status after current TSK-0484 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific reopen/change semantics, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
'''

stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
base,count=re.subn(r'^\*\*Updated:\*\* .+$','**Updated:** '+stamp,state,count=1,flags=re.MULTILINE)
if count!=1: raise SystemExit('Updated header replacement failed')
result=base+'\n'+append
if not result.startswith(base): raise SystemExit('existing runtime prefix not preserved')
if result.count(NEW)!=1: raise SystemExit('new section count invalid')
p.write_text(result,encoding='utf-8')
check=p.read_text(encoding='utf-8')
if check!=result or not check.startswith(base): raise SystemExit('runtime reread preservation failure')
for token in ['## TSK-0299 current accepted stable state','## TSK-0485 current accepted stable state','## TSK-0318 current accepted stable state','## TSK-0319 current accepted stable state','## TSK-0301 current accepted stable state','## TSK-0316 current accepted stable state','## TSK-0300 current accepted stable state','## TSK-0317 current accepted stable state','## TSK-0310 current accepted stable state']:
    if token not in base: raise SystemExit('protected anchor missing: '+token)
print('TSK0484_EXISTING_RUNTIME_PREFIX_PRESERVED=PASS')
print('TSK0484_PROTECTED_PASS_ANCHORS_PRESERVED=PASS')
print('TSK0484_CURRENT_STATE_RECONCILIATION=PASS')
