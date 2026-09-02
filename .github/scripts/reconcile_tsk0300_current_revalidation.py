from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME = '16e545c765219e7d1da735b45045f3a9a3621816'
EXPECTED = {
    'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0300_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-02.md':'b7e731ad958d224fde3c132495df571a925ed697',
    'TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md':'efaf7c80c1723208569b13ba4e725b2e7cad8d1a',
    'brand/system/TSK-0300/README.md':'f7d013723c8dd967bb8337b44a52a19f32664d41',
    'brand/system/TSK-0300/tokens.css':'cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f',
    'brand/system/TSK-0300/components.css':'831e92a74b6dda04252d93242cb33bd491a02381',
    'brand/system/TSK-0300/templates/public.html':'309f6a1f38474f78cd8a241aad3028fd495f9b8e',
    'brand/system/TSK-0300/templates/product.html':'872920b6f7af6561a1015e1d8fea55dcf95f1249',
    'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
}

NEW = '## TSK-0300 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION'
PROTECTED = (
    '## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 CORRECTED OWNER-IDENTITY BINDING',
    '## TSK-0485 current accepted stable state',
    '## TSK-0318 current accepted stable state',
    '## TSK-0319 current accepted stable state',
    '## TSK-0301 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION',
    '## TSK-0316 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE FRICTION REQUALIFICATION',
)
PROTECTED_SHA = {
    PROTECTED[0]:'d570e24eebd814ffd3014a51d4f60f1b7031f07a7e049dd3fb899b4c4ca0fc7c',
    PROTECTED[1]:'7f968a36ca0831b65f8441bffec6f73f09d6e282338baf8033c152cab56cbf3f',
    PROTECTED[2]:'71983d6d3689d030cddda123780ee4c5deeddf8bea691938f64d16627ba83d80',
    PROTECTED[3]:'f736e0301fefbe394a7c061430261e23e9b62ae2004557bf38c6ebfab448baa3',
    PROTECTED[4]:'80f664b1d347044b311eab361a837db8e31fbd67c50124e00f309e32dee48785',
    PROTECTED[5]:'6a33a6a62d1ce61dfb3a69cc648ae990b55fdbec50771e929b3b0d50b2ae71b9',
}

def blob(path: str) -> str:
    return subprocess.check_output(['git','hash-object',path], text=True).strip()

def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def section(text: str, prefix: str) -> str:
    m = re.search(r'^' + re.escape(prefix) + r'.*$', text, re.MULTILINE)
    if not m:
        raise SystemExit('missing section: ' + prefix)
    n = re.search(r'^## ', text[m.end():], re.MULTILINE)
    end = m.end() + n.start() if n else len(text)
    return text[m.start():end]

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f'hash mismatch {path}: {actual} != {expected}')

p = Path('CURRENT_STATE.md')
state = p.read_text(encoding='utf-8')

# Idempotent success only if the exact accepted state is already durable.
if NEW in state:
    current = section(state, NEW)
    required = [
        '**PASS**',
        'TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md',
        '33575760274 / 100079267725',
        'Identity redesign/reselection: **NO / NO**',
    ]
    if all(token in current for token in required):
        print('TSK0300_CURRENT_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous existing current TSK-0300 section')

if blob('CURRENT_STATE.md') != PRE_RUNTIME:
    raise SystemExit('pre-runtime blob mismatch; refuse stale write')
if not state.endswith('\n'):
    raise SystemExit('CURRENT_STATE.md must end with newline')

before = {h: section(state,h) for h in PROTECTED}
for h,s in before.items():
    if sha(s) != PROTECTED_SHA[h]:
        raise SystemExit('protected pre-hash mismatch: ' + h)

evidence = Path('TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in [
    'TSK-0300 current dependency-complete revalidation: PASS.',
    '33575760274 / 100079267725',
    'TSK0300_CURRENT_ACC=PASS',
    'TSK0300_IDENTITY_REDESIGN_REQUIRED=NO',
    'TSK0300_IDENTITY_RESELECTION_REQUIRED=NO',
]:
    if token not in evidence:
        raise SystemExit('evidence token missing: ' + token)

append = r'''## TSK-0300 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION

`TSK-0300 — Translate the approved identity into shared tokens, components, templates, and asset conventions`: **PASS** under current `ACC-0300 / VER-0300 / EVD-0300`, current direct predecessor TSK-0301, DEC-0053/CR-0006 dual-mode scope, DEC-0055/CR-0008 action authority, and the existing Project Owner SafeWeb identity approval.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0301`.
- Current revalidation artifact `TSK_0300_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-02.md`, blob `b7e731ad958d224fde3c132495df571a925ed697`, publication commit `8ca84c3a157772b100efbe8eb1de526cda59c0d0`.
- Current durable evidence `TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `efaf7c80c1723208569b13ba4e725b2e7cad8d1a`, publication commit `564af9c3b2347a924bed032dde4722c7a7f40abf`.
- Independent read-only VER-0300: workflow `.github/workflows/verify-tsk0300-current-revalidation.yml`, final blob `60f308f3025daa885e22c0ba577985272bd2af57`; run/job `33575760274 / 100079267725`: **SUCCESS** with `contents: read`.
- Earlier runs/jobs `33575603456 / 100078778694` and `33575680967 / 100079022886` are diagnostic-only verifier-shape failures; neither mutated governed state and the final verifier changed only brittle wording matchers.
- Current predecessor TSK-0301 remains durable PASS and its owner-approved SafeWeb identity was not reopened.
- Identity redesign/reselection: **NO / NO**. Identity specification remains blob `b8ffd2ed234465a238558a7b94e56274de49696a`; primary/inverse/monochrome/monogram master blobs remain `f93958e3e4a16f9056693072c1b9b8b31fcda852` / `c38709e4239a2d36b340b4d9d630df85a17bb494` / `ef9b6e0d52926f24c7e81bccb4489569067b852f` / `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`.
- Core shared implementation remains byte-identical: `tokens.css` blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`; `components.css` blob `831e92a74b6dda04252d93242cb33bd491a02381`.
- The verified CR-0006 contradiction was narrow: historical public/product wording excluded all Login/Dashboard/Account surfaces. Current dual-mode IA instead permits optional, non-coercive account continuity while preserving a complete login-free core.
- Narrow corrected references are `brand/system/TSK-0300/README.md` blob `f7d013723c8dd967bb8337b44a52a19f32664d41`, `templates/public.html` blob `309f6a1f38474f78cd8a241aad3028fd495f9b8e`, and `templates/product.html` blob `872920b6f7af6561a1015e1d8fea55dcf95f1249`.
- Exactly six reference contexts remain: public, product, help, status, partner and social; all load the one shared token/component system and reference TSK-0301 masters without duplicate brand hex values, remote scripts/styles/trackers or a second identity authority.
- Public `Start setup` remains primary; optional `Sign in / Manage devices` is secondary and non-coercive. Product setup retains `Finish without account` plus optional sign-in/manage continuity.
- Sign-in/session/dashboard/device ownership never automatically joins/imports/promotes/extends J0/J1 and never substitutes for current technical protection verification. Managed-device persistence is bounded continuity, not a child profile or browsing/query/activity-history surface.
- Protection-state accessibility remains text/evidence based and non-color-only; the approved low-contrast display restriction and monochrome/off-white fallback remain unchanged.
- **Non-inference:** L4 shared-brand-system PASS only; no integrated build, authentication/provider architecture, persistent schema/storage, legal/privacy completion, representative-parent evidence, publication, payment, market activation, production behavior, LG-06, launch or successor PASS is inferred.

### Queue status after current TSK-0300 revalidation

Recompute the next executable frontier from current WBS/graph, runtime evidence, lifecycle/gates and Action Authority. TSK-0317 is the expected remaining successor-chain candidate only if its current dependency/gate/semantic validity independently passes. Preserve corrected TSK-0299, TSK-0485, synchronized TSK-0318/TSK-0319, current TSK-0301 and current TSK-0316 unchanged.
'''

stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
base, count = re.subn(r'^\*\*Updated:\*\* .+$', '**Updated:** ' + stamp, state, count=1, flags=re.MULTILINE)
if count != 1:
    raise SystemExit('Updated header replacement failed')
result = base + append

for h,s in before.items():
    if section(result,h) != s:
        raise SystemExit('protected section changed: ' + h)
if result.count(NEW) != 1:
    raise SystemExit('new TSK-0300 section count invalid')

p.write_text(result, encoding='utf-8')
check = p.read_text(encoding='utf-8')
for h,s in before.items():
    if section(check,h) != s:
        raise SystemExit('post-write protected section changed: ' + h)

print('TSK0299_SECTION_PRESERVED=PASS')
print('TSK0485_SECTION_PRESERVED=PASS')
print('TSK0318_SECTION_PRESERVED=PASS')
print('TSK0319_SECTION_PRESERVED=PASS')
print('TSK0301_SECTION_PRESERVED=PASS')
print('TSK0316_SECTION_PRESERVED=PASS')
print('TSK0300_CURRENT_STATE_RECONCILIATION=PASS')
