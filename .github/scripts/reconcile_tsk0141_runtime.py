from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED = {
    'CURRENT_STATE.md': '6731369b823c9a3b4c8c5b344ad67b990b68850a',
    'Plans/Master/WBS/master-wbs.csv': '3bb1598a6233a2bbefa52c746a7621867c6c6e89',
    'TSK_0141_PROVISIONAL_MINIMUM_PRODUCT_SCOPE_AND_NON_GOALS_2026-08-28.md': 'c72bfd906fdca4a106dcd7d4ff458a2577e32c90',
    'TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md': '9d3870d90add696fc352829fb4763c834b8d09af',
    'TSK_0141_POST_CR0006_SCOPE_REVALIDATION_EVIDENCE_2026-08-30.md': '384455df94b084982d75d71eca1560cf24766412',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')

old = "- Prior PASS/evidence remains valid only for unchanged facts. `TSK-0146` and `TSK-0229` are current **PASS** under the revised DEC-0053/CR-0006 dual-mode Version-1 contract and evidence recorded below; revised account-inclusive `TSK-0313`, `TSK-0315`, `TSK-0328`, `TSK-0333`, `TSK-0321`, `TSK-0309`, and `TSK-0628` remain non-PASS until their current acceptance contracts are satisfied. Activated HUMAN_ONLY account UX decisions (`TSK-0329`, `TSK-0332`, `TSK-0331`) remain human-authority work when dependency-eligible."
new = "- Prior PASS/evidence remains valid only for unchanged facts. `TSK-0146`, `TSK-0229`, and post-CR-0006 `TSK-0141` are current **PASS** under the revised DEC-0053/CR-0006 dual-mode Version-1 contract and evidence recorded below; revised account-inclusive `TSK-0313`, `TSK-0315`, `TSK-0328`, `TSK-0333`, `TSK-0321`, `TSK-0309`, and `TSK-0628` remain non-PASS until their current acceptance contracts are satisfied. Activated HUMAN_ONLY account UX decisions (`TSK-0329`, `TSK-0332`, `TSK-0331`) remain human-authority work when dependency-eligible."
if s.count(old) != 1:
    raise SystemExit('top CR0006 current-PASS bullet mismatch')
s = s.replace(old, new, 1)

old = "- `TSK-0146` and post-CR-0006 `TSK-0229` are now the current accepted product/privacy baselines recorded below. Exact next work must be recomputed from current WBS dependencies, gates, Action Authority and runtime evidence; do not infer the successor from task numbering or the old LG-06 readiness package."
new = "- `TSK-0146`, post-CR-0006 `TSK-0229`, and post-CR-0006 `TSK-0141` are now current accepted product/privacy/scope baselines recorded below. Exact next work must be recomputed from current WBS dependencies, gates, Action Authority and runtime evidence; do not infer the successor from task numbering or the old LG-06 readiness package."
if s.count(old) != 1:
    raise SystemExit('CR0006 execution-boundary bullet mismatch')
s = s.replace(old, new, 1)

old = "### TSK-0141 accepted stable state\n\n`TSK-0141 — Freeze minimum product scope and non-goals`: **PASS for provisional L4 scope under DEC-0050/CR-0003**."
new = "### Historical TSK-0141 accepted stable state — PRE-CR-0006 — SUPERSEDED\n\n> Historical only. DEC-0053/CR-0006 superseded the account-exclusion clauses in this acceptance. Use the post-CR-0006 TSK-0141 section below for current runtime state.\n\n`TSK-0141 — Freeze minimum product scope and non-goals`: **PASS for provisional L4 scope under DEC-0050/CR-0003**."
if s.count(old) != 1:
    raise SystemExit('historical TSK0141 heading mismatch')
s = s.replace(old, new, 1)

marker = '## Frozen technical identity\n'
if s.count(marker) != 1:
    raise SystemExit('frozen technical identity marker mismatch')
current = '''## TSK-0141 current accepted stable state — 2026-08-30 — POST-CR-0006

`TSK-0141 — Freeze minimum product scope and non-goals`: **PASS** under current `ACC-0141 / VER-0141 / EVD-0141` and `DEC-0053 / CR-0006` authority.

- Current WBS blob `3bb1598a6233a2bbefa52c746a7621867c6c6e89`: L4, dependency `TSK-0139`, A3 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Dependency `TSK-0139` remains current PASS for bounded L4 product-definition/design authority; CR-0006 did not invalidate its evidence-limits mandate.
- Historical pre-CR-0006 scope artifact `TSK_0141_PROVISIONAL_MINIMUM_PRODUCT_SCOPE_AND_NON_GOALS_2026-08-28.md`, blob `c72bfd906fdca4a106dcd7d4ff458a2577e32c90`, remains evidence only for compatible facts. Its clauses deferring accounts/Google sign-in/persistent dashboard are superseded.
- Current revised scope is supplied without duplication by accepted `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md`, version `1.0.0`, blob `9d3870d90add696fc352829fb4763c834b8d09af`.
- Durable revalidation evidence: `TSK_0141_POST_CR0006_SCOPE_REVALIDATION_EVIDENCE_2026-08-30.md`, blob `384455df94b084982d75d71eca1560cf24766412`.
- Deterministic verifier run/job `33308167888 / 99248297105`: SUCCESS on self-hosted `adguardvm`; dependency, stale pre-CR-0006 scope detection, current-scope mapping, ACC-0141 and no-behavioral-inference checks all PASS.
- Current minimum scope includes optional parent accounts plus lightweight dashboard/device management while preserving the complete core setup/protection journey without login.
- Mandatory login, browsing/query/activity history, child accounts/profiles and unrestricted DNS administration remain excluded/prohibited absent later explicit authority.
- No capability is represented as behaviorally/user validated before the controlled integrated-product pilot in L8 after LG-09; `RSK-0002` remains OPEN.
- This PASS does not approve detailed account requirements, persistent schema, vendor/privacy/security architecture, account UX/prototype, implementation, LG-06, participant processing, release, payment or launch.

### Queue status after post-CR-0006 TSK-0141 acceptance

TSK-0141 may now satisfy its current hard-dependency edges. Successor eligibility must still be recomputed against all other current WBS dependencies, runtime evidence, lifecycle/gates and Action Authority.

'''
s = s.replace(marker, current + marker, 1)

lines = s.splitlines()
if len(lines) < 3 or not lines[2].startswith('**Updated:** '):
    raise SystemExit('Updated header mismatch')
lines[2] = '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')
p.write_text(s, encoding='utf-8')

for token in [
    '`TSK-0146`, `TSK-0229`, and post-CR-0006 `TSK-0141` are current **PASS**',
    '## TSK-0141 current accepted stable state — 2026-08-30 — POST-CR-0006',
    '### Historical TSK-0141 accepted stable state — PRE-CR-0006 — SUPERSEDED',
    '384455df94b084982d75d71eca1560cf24766412',
    '33308167888 / 99248297105',
]:
    if token not in s:
        raise SystemExit('post-transform token missing: ' + token)
print('TSK0141_RUNTIME_TRANSFORM=PASS')
