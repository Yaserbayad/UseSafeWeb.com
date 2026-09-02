from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED={
    'CURRENT_STATE.md':'077e6c61df6284441d447c4a796185adb5f3e65b',
    'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_BUDGET_2026-09-02.md':'27f1b6de7924ceba713f9aed9ffc90df9a31efe5',
    'TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_EVIDENCE_2026-09-02.md':'aaaa68119c21d76bc29d04e54443c23ce808bebc',
    'TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md':'97cf09f294c757f80ad5c0fbe6110ed8d471159c',
}
NEW='## TSK-0316 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE FRICTION REQUALIFICATION'
PROTECTED=(
    '## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 CORRECTED OWNER-IDENTITY BINDING',
    '## TSK-0485 current accepted stable state',
    '## TSK-0318 current accepted stable state',
    '## TSK-0319 current accepted stable state',
    '## TSK-0301 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION',
)
EXPECTED_SECTION_SHA={
    PROTECTED[0]:'d570e24eebd814ffd3014a51d4f60f1b7031f07a7e049dd3fb899b4c4ca0fc7c',
    PROTECTED[1]:'7f968a36ca0831b65f8441bffec6f73f09d6e282338baf8033c152cab56cbf3f',
    PROTECTED[2]:'71983d6d3689d030cddda123780ee4c5deeddf8bea691938f64d16627ba83d80',
    PROTECTED[3]:'f736e0301fefbe394a7c061430261e23e9b62ae2004557bf38c6ebfab448baa3',
    PROTECTED[4]:'80f664b1d347044b311eab361a837db8e31fbd67c50124e00f309e32dee48785',
}

def blob(path): return subprocess.check_output(['git','hash-object',path],text=True).strip()
def sha(text): return hashlib.sha256(text.encode()).hexdigest()
def section(text,prefix):
    m=re.search(r'^'+re.escape(prefix)+r'.*$',text,re.MULTILINE)
    if not m: raise SystemExit('missing section: '+prefix)
    n=re.search(r'^## ',text[m.end():],re.MULTILINE)
    end=m.end()+n.start() if n else len(text)
    return text[m.start():end]

for path,expected in EXPECTED.items():
    actual=blob(path)
    if actual!=expected: raise SystemExit(f'hash mismatch {path}: {actual} != {expected}')

p=Path('CURRENT_STATE.md')
state=p.read_text(encoding='utf-8')
if NEW in state:
    s=section(state,NEW)
    if '**PASS**' in s and 'TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_EVIDENCE_2026-09-02.md' in s:
        print('TSK0316_CURRENT_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous current TSK-0316 state')
if not state.endswith('\n'): raise SystemExit('CURRENT_STATE.md must end with newline')
if '## TSK-0315 current accepted stable state — 2026-08-31 — POST-CR-0007' not in state:
    raise SystemExit('current TSK-0315 predecessor runtime anchor missing')

before={h:section(state,h) for h in PROTECTED}
for h,s in before.items():
    if sha(s)!=EXPECTED_SECTION_SHA[h]: raise SystemExit('protected pre-hash mismatch: '+h)

evd=Path('TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in ['TSK-0316 post-CR-0008 dual-mode friction requalification: PASS','33574008442 / 100073872441','TSK0316_CURRENT_ACC=PASS','TSK0315_CURRENT_PREDECESSOR=PASS']:
    if token not in evd: raise SystemExit('evidence token missing: '+token)

append=r'''## TSK-0316 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE FRICTION REQUALIFICATION

`TSK-0316 — Define a friction budget and challenge every click, field, choice, confirmation, account, and manual step`: **PASS** under current `ACC-0316 / VER-0316 / EVD-0316`, current TSK-0315 dual-mode predecessor, DEC-0053/CR-0006, DEC-0054/CR-0007, and DEC-0055/CR-0008.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0315`.
- Current artifact `TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_BUDGET_2026-09-02.md`, version `2.0.0-post-cr0008`, blob `27f1b6de7924ceba713f9aed9ffc90df9a31efe5`, publication commit `8af4b735cd0e9013c21cf8faa1b63d6f1a99015c`.
- Current durable evidence `TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_EVIDENCE_2026-09-02.md`, blob `aaaa68119c21d76bc29d04e54443c23ce808bebc`, publication commit `6b52b2471e0f7a2f6edf3897b8df8b5c252c472a`.
- Independent read-only VER-0316 workflow `.github/workflows/verify-tsk0316-post-cr0008.yml`, blob `c4948995ad5fde72c827d588132ec5aa7ff1dd09`; run/job `33574008442 / 100073872441`: **SUCCESS** with `contents: read`.
- Current predecessor TSK-0315 is durable PASS under `TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md`, blob `97cf09f294c757f80ad5c0fbe6110ed8d471159c`.
- Historical accountless-only TSK-0316 remains compatible evidence only for unchanged minimisation principles; it is superseded for current acceptance because CR-0006 added optional account/session/dashboard/device-management scope.
- The current friction budget challenges all 25 current TSK-0315 stages and uses seven reason classes covering irreducible decisions, platform/security actions, evidence interactions, conditional routing, optional account continuity, consequential lifecycle actions, and recovery/help.
- Complete accountless setup/verification/Protection Map/help/removal/recovery remains first-class and can finish/exit without login. Optional account continuity occurs only after explicit choice or already-authenticated account-only use.
- Successful sign-in does not automatically link/import/promote/extend J0/J1 or create a managed-device record; valid session suppresses redundant sign-in; dashboard empty/list is output rather than mandatory form friction.
- Managed-device persistence remains minimum bounded continuity and is not a child profile, browsing-history domain or technical protection-verification signal.
- Logout, unlink/revoke, device-record deletion, account deletion, anonymous reset and physical SafeWeb DNS removal remain distinct operations with explicit object/consequence semantics.
- Ambiguous consequential effects are reconciled before replay; equivalent failures do not loop without changed condition/new evidence.
- Platform/security actions and evidence interactions that cannot truthfully be automated remain explicit. Unsupported silent-install/one-click/complete-safety claims are prohibited.
- Parent-facing generic naming uses `SafeWeb` / `SafeWeb DNS`; `UseSafeWeb.com` and `dns.usesafeweb.com` appear only when they are actual technical identifiers.
- No browsing/query/activity history, raw AdGuard admin/control surface, mandatory child account/profile or analytics/marketing field is introduced by the friction budget.
- `RSK-0002` remains OPEN/non-blocking before L8; no representative-parent usability/comprehension is inferred.
- **Non-inference:** L4 friction-design PASS only; no TSK-0317, LG-06, provider/auth architecture, persistent schema/storage, implementation/build, legal/privacy completion, publication, payment, production behavior or launch PASS is inferred.

### Queue status after current TSK-0316 requalification

Recompute the next executable frontier from canonical WBS/graph, current runtime PASS evidence, lifecycle/gates, action authority and latest owner instruction. Do not infer TSK-0317 or any other successor PASS solely from TSK-0316 completion. Preserve corrected TSK-0299, TSK-0485, TSK-0318, TSK-0319 and current TSK-0301 accepted states unchanged.
'''

stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
base,count=re.subn(r'^\*\*Updated:\*\* .+$','**Updated:** '+stamp,state,count=1,flags=re.MULTILINE)
if count!=1: raise SystemExit('Updated header replacement failed')
result=base+append
for h,s in before.items():
    if section(result,h)!=s: raise SystemExit('protected section changed: '+h)
if result.count(NEW)!=1: raise SystemExit('new TSK-0316 section count invalid')
p.write_text(result,encoding='utf-8')
check=p.read_text(encoding='utf-8')
for h,s in before.items():
    if section(check,h)!=s: raise SystemExit('post-write protected section changed: '+h)
print('TSK0299_SECTION_PRESERVED=PASS')
print('TSK0485_SECTION_PRESERVED=PASS')
print('TSK0318_SECTION_PRESERVED=PASS')
print('TSK0319_SECTION_PRESERVED=PASS')
print('TSK0301_SECTION_PRESERVED=PASS')
print('TSK0316_CURRENT_STATE_RECONCILIATION=PASS')
