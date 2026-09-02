from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    'CURRENT_STATE.md': 'dbe82497b0bfe5a699c446ca8b343568c7ca456f',
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0301_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-01.md': '12c5de46b5ca880752d6f244e9bc2320e9689fa3',
    'TSK_0301_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md': 'c8935b9cfebe06fe1260b04d7af3c84318a6b5e0',
    'TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md': '66f4b545c03571649a8baa4c0fe3d1df564b5949',
    'brand/identity/TSK-0301/README.md': 'b8ffd2ed234465a238558a7b94e56274de49696a',
}

NEW = '## TSK-0301 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION'
PROTECTED = (
    '## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 CORRECTED OWNER-IDENTITY BINDING',
    '## TSK-0485 current accepted stable state',
    '## TSK-0318 current accepted stable state',
    '## TSK-0319 current accepted stable state',
)


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


def section(text: str, prefix: str) -> str:
    m = re.search(r'^' + re.escape(prefix) + r'.*$', text, re.MULTILINE)
    if not m:
        raise SystemExit(f'missing section: {prefix}')
    n = re.search(r'^## ', text[m.end():], re.MULTILINE)
    end = m.end() + n.start() if n else len(text)
    return text[m.start():end]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f'hash mismatch {path}: {actual} != {expected}')

p = Path('CURRENT_STATE.md')
state = p.read_text(encoding='utf-8')
if NEW in state:
    s = section(state, NEW)
    if 'TSK_0301_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md' in s and '**PASS**' in s:
        print('TSK0301_CURRENT_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous existing current TSK-0301 section')

if '### TSK-0301 accepted stable state' not in state:
    raise SystemExit('historical TSK-0301 accepted-state anchor missing')
if '### TSK-0302 accepted stable state' not in state:
    raise SystemExit('TSK-0302 predecessor runtime anchor missing')

before = {h: sha256(section(state, h)) for h in PROTECTED}
expected_hashes = {
    PROTECTED[0]: 'd570e24eebd814ffd3014a51d4f60f1b7031f07a7e049dd3fb899b4c4ca0fc7c',
    PROTECTED[1]: '7f968a36ca0831b65f8441bffec6f73f09d6e282338baf8033c152cab56cbf3f',
    PROTECTED[2]: '71983d6d3689d030cddda123780ee4c5deeddf8bea691938f64d16627ba83d80',
    PROTECTED[3]: 'f736e0301fefbe394a7c061430261e23e9b62ae2004557bf38c6ebfab448baa3',
}
for h, expected in expected_hashes.items():
    if before[h] != expected:
        raise SystemExit(f'protected section pre-hash mismatch: {h}')

evidence = Path('TSK_0301_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in [
    'TSK-0301 current dependency-complete revalidation: PASS',
    '33573469599 / 100072230006',
    'TSK0301_CURRENT_ACC=PASS',
    'IDENTITY_RESELECTION_REQUIRED=NO',
]:
    if token not in evidence:
        raise SystemExit(f'evidence token missing: {token}')

append = r'''

## TSK-0301 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION

`TSK-0301 — Finalize logo system, typography, color, imagery, iconography, visual language, and layout principles`: **PASS** under current `ACC-0301 / VER-0301 / EVD-0301`, current direct predecessors `TSK-0302` and corrected `TSK-0299`, the existing Project Owner identity approval, and CR-0008 Action Authority normalization.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0302; TSK-0299`.
- Current revalidation artifact `TSK_0301_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-01.md`, blob `12c5de46b5ca880752d6f244e9bc2320e9689fa3`, publication commit `b103eaec21c92851a64396d5cef95d568ddee875`.
- Current durable acceptance evidence `TSK_0301_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `c8935b9cfebe06fe1260b04d7af3c84318a6b5e0`, publication commit `6aac9580976d24cb4f6bc41fd4a1106ff24a72d2`.
- Successful independent read-only VER-0301 v2: workflow `.github/workflows/verify-tsk0301-current-revalidation-v2.yml`, blob `21b362de5342832e14e2bfa1d08d0d700e4293c1`; run/job `33573469599 / 100072230006`: **SUCCESS** with `contents: read`.
- The earlier run/job `33573390907 / 100071992638` is diagnostic-only: it failed solely because an over-broad verifier assertion rejected the standard W3C SVG namespace URL; no governed artifact/state changed and v2 corrected only the verifier shape.
- Project Owner identity approval remains unchanged: `TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md`, blob `66f4b545c03571649a8baa4c0fe3d1df564b5949`; visible brand remains exactly `SafeWeb`, Concept A wordmark-first, `Safe` dark green `#173F35`, `Web` maroon `#7A2E36`.
- Identity specification remains unchanged: `brand/identity/TSK-0301/README.md`, blob `b8ffd2ed234465a238558a7b94e56274de49696a`.
- Editable master blobs remain unchanged: primary `f93958e3e4a16f9056693072c1b9b8b31fcda852`; inverse `c38709e4239a2d36b340b4d9d630df85a17bb494`; monochrome `ef9b6e0d52926f24c7e81bccb4489569067b852f`; monogram `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`.
- Current TSK-0302 predecessor remains valid for visual-direction acceptance. Corrected current TSK-0299 explicitly preserves this owner-approved identity and uses `SafeWeb` as visible brand copy; no identity reselection is required or authorized.
- ACC-0301 remains proven: one owner-approved system; editable/versioned masters; small/mobile/mono/contrast/readability acceptance with mandatory high-contrast fallback for the low-contrast maroon-on-dark-green display combination; no visual safety guarantee.
- CR-0006 optional account/lightweight dashboard does not require identity redesign. The same SafeWeb identity applies across accountless setup and optional account/dashboard surfaces while product-state truth remains separate from brand colour.
- The historical `### TSK-0301 accepted stable state` remains historical evidence for unchanged facts and is superseded as current dependency proof by this section.
- **Non-inference:** no TSK-0300, LG-06, behavioral validation, legal/privacy completion, implementation/build, provider acceptance, publication, payment, market activation, production behavior or launch PASS is inferred.

### Queue status after current TSK-0301 revalidation

Recompute current eligibility from canonical WBS/graph and runtime evidence. TSK-0316 remains a known CR-0006 dual-mode friction requalification candidate but must be independently rechecked against all other current eligible work before execution. Preserve corrected TSK-0299, TSK-0485, TSK-0318 and TSK-0319 accepted states unchanged.
'''

lines = state.rstrip().splitlines()
for i, line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i] = '**Updated:** ' + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
        break
else:
    raise SystemExit('Updated header missing')

result = '\n'.join(lines).rstrip() + append + '\n'
for h, digest in before.items():
    if sha256(section(result, h)) != digest:
        raise SystemExit(f'protected section changed: {h}')
if result.count(NEW) != 1:
    raise SystemExit('new TSK-0301 current section count invalid')

p.write_text(result, encoding='utf-8')
check = p.read_text(encoding='utf-8')
for h, digest in before.items():
    if sha256(section(check, h)) != digest:
        raise SystemExit(f'post-write protected section changed: {h}')

print('TSK0299_SECTION_PRESERVED=PASS')
print('TSK0485_SECTION_PRESERVED=PASS')
print('TSK0318_SECTION_PRESERVED=PASS')
print('TSK0319_SECTION_PRESERVED=PASS')
print('TSK0301_CURRENT_STATE_RECONCILIATION=PASS')
