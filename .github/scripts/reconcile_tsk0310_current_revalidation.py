from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME = '2d2e3c9de8f247bcff4f54388002917127c55c24'
EXPECTED = {
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0310_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-02.md': 'c24d89d23dd81063e1b4b6693a0b98212e750ec6',
    'TSK_0310_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md': '189d0c47282e4e0a391852a1be08ca3b85291705',
    'TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md': '02b34756862a62091908e60d32b490059a84a67c',
    'prototype/TSK-0310/index.html': '5d80dfdefb52042bc34468723354fefd325285e4',
    'prototype/TSK-0310/model.mjs': '01343273fd09c3c12d26f0c0eb1ae9a2fce10c91',
    'prototype/TSK-0310/app.mjs': 'a4a0aff8848f8541e2581e333efbf48767c9f0ff',
    'prototype/TSK-0310/prototype.css': '004b0b34c0e5d94e3eacbeae25710284ef9a7886',
    'brand/system/TSK-0300/tokens.css': 'cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f',
    'brand/system/TSK-0300/components.css': '831e92a74b6dda04252d93242cb33bd491a02381',
    'brand/identity/TSK-0301/safeweb-wordmark-primary.svg': 'f93958e3e4a16f9056693072c1b9b8b31fcda852',
}
NEW = '## TSK-0310 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION'


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


for path, expected in EXPECTED.items():
    p = Path(path)
    if not p.exists():
        raise SystemExit(f'missing guarded input: {path}')
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f'guarded input hash mismatch {path}: {actual} != {expected}')

state_path = Path('CURRENT_STATE.md')
state = state_path.read_text(encoding='utf-8')

if NEW in state:
    start = state.index(NEW)
    section = state[start:]
    required = [
        '**PASS**',
        'TSK_0310_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md',
        '33577924582 / 100085830058',
        '`AUTO_ALLOWED`',
        'BROWSER_ACCEPTANCE_CHECKS=218',
    ]
    if all(token in section for token in required):
        print('TSK0310_CURRENT_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous existing current TSK-0310 section')

actual_runtime = blob('CURRENT_STATE.md')
if actual_runtime != PRE_RUNTIME:
    raise SystemExit(f'pre-runtime blob mismatch: {actual_runtime} != {PRE_RUNTIME}')
if not state.endswith('\n'):
    raise SystemExit('CURRENT_STATE.md must end with newline')

# Validate evidence terminal markers before touching runtime.
evidence = Path('TSK_0310_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
required_evidence = [
    'TSK-0310 current dependency-complete revalidation: PASS.',
    'ACC-0310 = PASS. VER-0310 = PASS. EVD-0310 = SATISFIED.',
    '33577924582 / 100085830058',
    'BROWSER_ACCEPTANCE_CHECKS=218',
    'TSK0310_CURRENT_RENDERED_ACCEPTANCE=PASS',
    'TSK0310_VER_SOURCE_UNCHANGED=PASS',
]
for token in required_evidence:
    if token not in evidence:
        raise SystemExit(f'missing evidence token: {token}')

append = r'''## TSK-0310 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT DEPENDENCY REVALIDATION

`TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation`: **PASS** under current `ACC-0310 / VER-0310 / EVD-0310`, current direct predecessors TSK-0318 / TSK-0317 / TSK-0320 / TSK-0300, current CR-0006/CR-0008 scope, and fresh isolated rendered-browser verification.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0318; TSK-0317; TSK-0320; TSK-0300`.
- Current revalidation artifact `TSK_0310_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-02.md`, blob `c24d89d23dd81063e1b4b6693a0b98212e750ec6`, publication commit `9c10f62ecc53ca9b98dcfa4de2d941a70c514428`.
- Current durable evidence `TSK_0310_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `189d0c47282e4e0a391852a1be08ca3b85291705`, publication commit `0984bdcbaf83f644d15886e63969829ea9dbf7d2`.
- Independent read-only VER-0310 workflow `.github/workflows/verify-tsk0310-current-revalidation.yml`, blob `30f9ff10875a600d0de8d54329739e90a4d8587d`; run/job `33577924582 / 100085830058`: **SUCCESS** on GitHub-hosted Ubuntu 24.04, Node 22.23.2, Playwright 1.62.0 and Chromium 151.0.7922.34.
- Fresh current rendered result: `BROWSER_ACCEPTANCE_CHECKS=218`, `BROWSER_ACCEPTANCE=PASS`, `TSK0310_CURRENT_RENDERED_ACCEPTANCE=PASS`; tracked prototype/TSK-0300 shared-system/TSK-0301 identity source remained unchanged with `TSK0310_VER_SOURCE_UNCHANGED=PASS`.
- Historical rendered-browser evidence `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `02b34756862a62091908e60d32b490059a84a67c`, remains valid for the unchanged ACC-0310 public-to-setup boundary and is retained rather than replaced.
- Current authoritative prototype source remains index `5d80dfdefb52042bc34468723354fefd325285e4`, model `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`, app `a4a0aff8848f8541e2581e333efbf48767c9f0ff`, and accessibility-remediated CSS `004b0b34c0e5d94e3eacbeae25710284ef9a7886`.
- TSK-0321's accepted remediation already requalified that CSS with the original TSK-0310 `218/218` rendered suite and `667/667` accessibility checks; fresh current VER-0310 rerendered the same accepted source successfully.
- Current TSK-0300 tokens/components remain exact imported authorities and unchanged; the approved SafeWeb primary wordmark remains unchanged. No identity reselection, visual redesign, token redesign, design-system fork or prototype rebuild occurred.
- Current TSK-0317 platform-path semantics and owning TSK-0408 endpoint semantics are compatible with the existing Android/iPhone rendered routes.
- Current TSK-0318 explicitly preserves TSK-0310's accountless public-to-setup evidence for its own current ACC and does not broaden TSK-0310 into optional account/dashboard implementation.
- Current TSK-0320 evidence-state/copy semantics remain compatible with the rendered state machine and Protection Map.
- **Non-inference:** this is current L4 TSK-0310 public-to-setup prototype PASS only; it does not prove optional account/dashboard implementation, integrated production build, authentication/provider architecture, persistent schema/storage, final legal/privacy completion, representative-parent evidence, participant processing, public publication, payment, market activation, production behavior, LG-06, launch or any successor PASS.

### Queue status after current TSK-0310 revalidation

Recompute the next executable frontier from canonical WBS/graph, current runtime evidence, gates, current source validity and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence explicitly invalidates them; do not infer a successor PASS solely from TSK-0310 completion.
'''

stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
updated, count = re.subn(r'^\*\*Updated:\*\* .+$', '**Updated:** ' + stamp, state, count=1, flags=re.MULTILINE)
if count != 1:
    raise SystemExit('Updated header replacement failed')

# Exact preservation boundary: the full prior runtime remains byte-for-byte identical
# except the single Updated line; all new content is appended after the prior EOF.
expected_prefix, prefix_count = re.subn(r'^\*\*Updated:\*\* .+$', '**Updated:** ' + stamp, state, count=1, flags=re.MULTILINE)
if prefix_count != 1 or updated != expected_prefix:
    raise SystemExit('runtime preservation transform mismatch')
result = updated + '\n' + append
if not result.startswith(expected_prefix):
    raise SystemExit('existing runtime prefix was not preserved')
if result.count(NEW) != 1:
    raise SystemExit('new TSK-0310 section count invalid')

state_path.write_text(result, encoding='utf-8')
check = state_path.read_text(encoding='utf-8')
if check != result:
    raise SystemExit('runtime reread differs from intended result')
if not check.startswith(expected_prefix):
    raise SystemExit('post-write existing runtime prefix changed')

# Explicitly prove the requested protected/current anchors still exist in preserved prefix.
for token in [
    '## TSK-0299 current accepted stable state',
    '## TSK-0485 current accepted stable state',
    '## TSK-0318 current accepted stable state',
    '## TSK-0319 current accepted stable state',
    '## TSK-0301 current accepted stable state',
    '## TSK-0316 current accepted stable state',
    '## TSK-0300 current accepted stable state',
    '## TSK-0317 current accepted stable state',
]:
    if token not in expected_prefix:
        raise SystemExit(f'protected anchor missing before append: {token}')

print('TSK0310_EXISTING_RUNTIME_PREFIX_PRESERVED=PASS')
print('TSK0310_PROTECTED_PASS_ANCHORS_PRESERVED=PASS')
print('TSK0310_CURRENT_STATE_RECONCILIATION=PASS')
