from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME='feb4b34a1860befed1ef52e5ebebb9eda6fd568c'
EXPECTED={
    'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md':'37173d2f9cb970a7b5e6a83af90c8f868f9fbfa8',
    'TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'cd001f3ce391634e38ef0c89934cb34f4f347401',
    'TSK_0316_POST_CR0008_DUAL_MODE_FRICTION_EVIDENCE_2026-09-02.md':'aaaa68119c21d76bc29d04e54443c23ce808bebc',
    'TSK_0408_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md':'0bbf1d934ecd4a7693baf7de56362391e46dcf55',
    'TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md':'3aa832777276115912e4f3990b30cb541c458f4f',
}
NEW='## TSK-0317 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT PLATFORM-PATH REVALIDATION'
PROTECTED=(
    '## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 CORRECTED OWNER-IDENTITY BINDING',
    '## TSK-0485 current accepted stable state',
    '## TSK-0318 current accepted stable state',
    '## TSK-0319 current accepted stable state',
    '## TSK-0301 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION',
    '## TSK-0316 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE FRICTION REQUALIFICATION',
    '## TSK-0300 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION',
)
PROTECTED_SHA={
    PROTECTED[0]:'d570e24eebd814ffd3014a51d4f60f1b7031f07a7e049dd3fb899b4c4ca0fc7c',
    PROTECTED[1]:'7f968a36ca0831b65f8441bffec6f73f09d6e282338baf8033c152cab56cbf3f',
    PROTECTED[2]:'71983d6d3689d030cddda123780ee4c5deeddf8bea691938f64d16627ba83d80',
    PROTECTED[3]:'f736e0301fefbe394a7c061430261e23e9b62ae2004557bf38c6ebfab448baa3',
    PROTECTED[4]:'80f664b1d347044b311eab361a837db8e31fbd67c50124e00f309e32dee48785',
    PROTECTED[5]:'6a33a6a62d1ce61dfb3a69cc648ae990b55fdbec50771e929b3b0d50b2ae71b9',
    PROTECTED[6]:'b86eb69c654c94b4f3b1939fedcc7c23cb0151c87cb443a726f9ed417bdb2255',
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
    current=section(state,NEW)
    required=['**PASS**','TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md','33576615158 / 100081874297','`AUTO_ALLOWED`']
    if all(x in current for x in required):
        print('TSK0317_CURRENT_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous existing current TSK-0317 section')
if blob('CURRENT_STATE.md')!=PRE_RUNTIME: raise SystemExit('pre-runtime blob mismatch; refuse stale write')
if not state.endswith('\n'): raise SystemExit('CURRENT_STATE.md must end with newline')

before={h:section(state,h) for h in PROTECTED}
for h,s in before.items():
    if sha(s)!=PROTECTED_SHA[h]: raise SystemExit('protected pre-hash mismatch: '+h)

evidence=Path('TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in ['TSK-0317 current dependency-complete platform-path revalidation: PASS.','33576615158 / 100081874297','TSK0317_CURRENT_ACC=PASS','TSK0317_APPLE_FUNCTIONAL_NEGATIVE_ROLLBACK_DESIGN=PASS','TSK0317_ANDROID_FUNCTIONAL_NEGATIVE_ROLLBACK_DESIGN=PASS']:
    if token not in evidence: raise SystemExit('evidence token missing: '+token)

append=r'''## TSK-0317 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT PLATFORM-PATH REVALIDATION

`TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform`: **PASS** under current `ACC-0317 / VER-0317 / EVD-0317`, current direct predecessor TSK-0316, DEC-0053/CR-0006 dual-mode scope, DEC-0055/CR-0008 Action Authority, current TSK-0408/0409 technical mechanism/conflict authority, and current external Android/Apple source review.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A4 / `AUTO_ALLOWED`; dependency exactly `TSK-0316`.
- Current artifact `TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md`, version `2.0.0-post-cr0008`, blob `37173d2f9cb970a7b5e6a83af90c8f868f9fbfa8`, publication commit `2dcaa44f4b0f536729d5f3f6d2ac2c509c35bd3a`.
- Current durable evidence `TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `cd001f3ce391634e38ef0c89934cb34f4f347401`, publication commit `b82f658214f5f75821a94419bedf3d1ef36d36bf`.
- Independent read-only VER-0317 final workflow `.github/workflows/verify-tsk0317-current-revalidation.yml`, blob `b36c1fca1c4ad6f31cf8eb4b55cb25a33c35b6e6`; run/job `33576615158 / 100081874297`: **SUCCESS** with `contents: read`.
- Earlier VER runs/jobs `33576324000 / 100080973119`, `33576461447 / 100081409912`, and `33576541527 / 100081654136` are diagnostic-only brittle-source-text matcher failures. They did not mutate governed state or weaken acceptance.
- Historical TSK-0317 platform mechanics remain compatible where current verification confirms them, but historical `A1 / HUMAN_ONLY`, human-decision packet and generic parent-facing `UseSafeWeb` wording are superseded by current WBS/CR-0008 and corrected TSK-0299.
- The complete install/verify/remove/recover platform path remains accountless. Optional account/session/dashboard/device continuity is orthogonal and never changes the OS setup mechanism, creates technical verification evidence or automatically links J0/J1.
- Android current baseline retains the native Private DNS provider-hostname path with exact technical hostname `dns.usesafeweb.com`; the parent/OS performs the system setting change. The Apple DoH URL is not substituted into the Android provider-hostname field.
- iPhone current baseline retains the separately verified SafeWeb profile/DoH route with canonical technical endpoint `https://dns.usesafeweb.com/dns-query`; TSK-0317 does not fabricate/release a `.mobileconfig` artifact and installation/removal remain explicit user/OS actions.
- Current official-source review on 2026-09-02 confirmed Android's provider-hostname Private DNS model, Apple manual profile-install/removal permission model and Apple encrypted DNS Settings payload semantics. If current Apple security policy such as Stolen Device Protection blocks profile installation, SafeWeb does not instruct the parent to weaken security merely to obtain a positive state.
- Automatic behavior is limited to reliable routing, copy/delivery of already verified artifacts, controlled verification and state rendering. Unsupported/managed/VPN/Private-Relay/app-specific-resolver/network conflicts stop or demote the claim rather than being hidden.
- Configuration/profile/account/dashboard/device ownership/parent confirmation never equals `Verified`; current controlled technical evidence owns the protection claim. No browsing/query/activity history is required for verification.
- Removal/recovery is explicit. Removing the SafeWeb DNS mechanism ends the SafeWeb DNS claim and does not falsely imply account/device/anonymous-state deletion; deleting account/device state does not falsely imply physical DNS removal.
- No silent plaintext downgrade may retain an active SafeWeb protection claim. Retry/replay requires changed condition/new evidence and reconciliation of ambiguous consequential state.
- Parent-facing generic product/feature wording uses `SafeWeb` / `SafeWeb DNS`; `UseSafeWeb.com`, `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query` remain literal only as actual domain/technical identifiers.
- **Non-inference:** current L4 platform-path design PASS only; no integrated implementation/build, release profile, auth/provider architecture, persistent schema/storage, legal/privacy completion, representative-parent evidence, participant/publication/payment/market activation, production behavior, LG-06, launch or successor PASS is inferred.

### Queue status after current TSK-0317 revalidation

Recompute the next executable frontier from canonical WBS/graph, current runtime PASS evidence, lifecycle/gates, current source validity and Action Authority. Do not infer any successor PASS solely from TSK-0317 completion. Preserve corrected TSK-0299, TSK-0485, synchronized TSK-0318/TSK-0319, current TSK-0301, current TSK-0316 and current TSK-0300 unchanged.
'''

stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
base,count=re.subn(r'^\*\*Updated:\*\* .+$','**Updated:** '+stamp,state,count=1,flags=re.MULTILINE)
if count!=1: raise SystemExit('Updated header replacement failed')
result=base+append
for h,s in before.items():
    if section(result,h)!=s: raise SystemExit('protected section changed: '+h)
if result.count(NEW)!=1: raise SystemExit('new TSK-0317 section count invalid')
p.write_text(result,encoding='utf-8')
check=p.read_text(encoding='utf-8')
for h,s in before.items():
    if section(check,h)!=s: raise SystemExit('post-write protected section changed: '+h)

print('TSK0299_SECTION_PRESERVED=PASS')
print('TSK0485_SECTION_PRESERVED=PASS')
print('TSK0318_SECTION_PRESERVED=PASS')
print('TSK0319_SECTION_PRESERVED=PASS')
print('TSK0301_SECTION_PRESERVED=PASS')
print('TSK0316_SECTION_PRESERVED=PASS')
print('TSK0300_SECTION_PRESERVED=PASS')
print('TSK0317_CURRENT_STATE_RECONCILIATION=PASS')
