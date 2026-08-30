from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED = {
    'CURRENT_STATE.md': '091d063cf71c6c50432b02c5faf2643bf481b1f4',
    'Plans/Master/WBS/master-wbs.csv': '3bb1598a6233a2bbefa52c746a7621867c6c6e89',
    'Plans/Master/Registers/DECISIONS_TRIGGERS.md': '9cb2908f4c6f19cb38fce4a8aff71abca3b7b095',
    'TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md': '9d3870d90add696fc352829fb4763c834b8d09af',
    'TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_EVIDENCE_2026-08-30.md': 'b785c4a52217b24cf6eb9f66dce0773ddef7a639',
}

for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')

replacements = [
(
"- Prior PASS/evidence remains valid only for unchanged facts. Account-exclusion-dependent L4 evidence is reopened: `TSK-0146` is current `TODO`; revised account-inclusive `TSK-0313`, `TSK-0315`, `TSK-0328`, `TSK-0333`, `TSK-0321`, `TSK-0309`, and `TSK-0628` are non-PASS until their current acceptance contracts are satisfied. Activated HUMAN_ONLY account UX decisions (`TSK-0329`, `TSK-0332`, `TSK-0331`) remain human-authority work when dependency-eligible.",
"- Prior PASS/evidence remains valid only for unchanged facts. `TSK-0146` is current **PASS** under the revised DEC-0053/CR-0006 dual-mode Version-1 contract and evidence recorded below; revised account-inclusive `TSK-0313`, `TSK-0315`, `TSK-0328`, `TSK-0333`, `TSK-0321`, `TSK-0309`, and `TSK-0628` remain non-PASS until their current acceptance contracts are satisfied. Activated HUMAN_ONLY account UX decisions (`TSK-0329`, `TSK-0332`, `TSK-0331`) remain human-authority work when dependency-eligible."
),
(
"- Historical accepted-stable sections for `TSK-0146`, `TSK-0333`, `TSK-0321`, `TSK-0309`, `TSK-0628` or other account-exclusion-dependent artifacts are historical evidence only where CR-0006 changed acceptance; they do not satisfy the revised task state.",
"- The historical pre-CR-0006 `TSK-0146` accepted-stable section is superseded by the current post-CR-0006 TSK-0146 state below. Historical accepted-stable sections for `TSK-0333`, `TSK-0321`, `TSK-0309`, `TSK-0628` or other account-exclusion-dependent artifacts remain historical evidence only where CR-0006 changed acceptance; they do not satisfy the revised task state."
),
(
"- Exact next task must be recomputed from the CR-0006 WBS/graph after this runtime write/read-back; do not infer the successor from task numbering or the old LG-06 readiness package.",
"- After this TSK-0146 PASS is persisted/read back, exact next work must be recomputed from current WBS dependencies, gates, Action Authority and runtime evidence; do not infer the successor from task numbering or the old LG-06 readiness package."
),
(
"## TSK-0146 accepted stable state — 2026-08-30\n\n`TSK-0146 — Freeze accountless-first product baseline and optional-account trigger`: **PASS**",
"## Historical TSK-0146 pre-CR-0006 accepted state — 2026-08-30 — SUPERSEDED\n\n> Historical only. DEC-0053/CR-0006 superseded this account-exclusion-dependent acceptance. Do not use this section as current TSK-0146 runtime state.\n\n`TSK-0146 — Freeze accountless-first product baseline and optional-account trigger`: **PASS**"
),
]

for old, new in replacements:
    if s.count(old) != 1:
        raise SystemExit('runtime replacement boundary mismatch: ' + old[:100])
    s = s.replace(old, new, 1)

marker = '## Frozen technical identity\n'
if s.count(marker) != 1:
    raise SystemExit('frozen technical identity marker mismatch')

current = '''## TSK-0146 current accepted stable state — 2026-08-30 — POST-CR-0006

`TSK-0146 — Freeze Version-1 optional-account product baseline and accountless core path`: **PASS** under `ACC-0146 / VER-0146 / EVD-0146` and current `DEC-0053 / CR-0006` authority.

- Current WBS blob `3bb1598a6233a2bbefa52c746a7621867c6c6e89`: L4, CRITICAL, zero hard dependencies, A3, `AUTO_ALLOWED`; WBS planning snapshot was `TODO` before this execution and is not used as runtime proof.
- Accepted Version-1 baseline: `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md`, version `1.0.0`, blob `9d3870d90add696fc352829fb4763c834b8d09af`, publication commit `1a913b44a09c383ac6c9939959648629351d9f6c`.
- Durable acceptance evidence: `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_EVIDENCE_2026-08-30.md`, blob `b785c4a52217b24cf6eb9f66dce0773ddef7a639`.
- Deterministic verification run/job `33307541477 / 99246630910`: SUCCESS on self-hosted `adguardvm`; WBS contract, exact canonical source hashes, all required ACC-0146 clauses, non-goals and no-downstream-PASS-inference checks passed.
- Frozen product rule: Version 1 includes a required **optional parent account** with secure-session product requirements, minimum parent/device ownership persistence and lightweight dashboard/device management, while the complete core safety setup/protection journey remains usable without login.
- Mandatory login, browsing/query/activity history, child accounts and unrestricted/raw customer DNS administration remain prohibited absent later explicit Project Owner change. Account ownership/device registration never substitutes for technical Protection Map verification.
- Google/Firebase remains the planned initial authentication route only; L5 vendor/privacy/security/architecture acceptance is not inferred. Exact persistence schema, retention, storage, access, backup, deletion and ownership mechanics remain downstream tasks.
- `RSK-0002` remains OPEN/non-blocking before L8 under DEC-0052; no human/user validation is inferred. Account/dashboard privacy-drift risk remains for downstream design/build/runtime verification.
- LG-06 remains non-PASS. Revised account-inclusive L4 UX/prototype tasks, L5 architecture/security/privacy/vendor work, L6 implementation and L7 auth/authz/IDOR/ClientID/deletion/recovery acceptance retain their own task/gate requirements.

### Queue status after post-CR-0006 TSK-0146 acceptance

Recompute current eligibility from WBS hard dependencies, current runtime evidence, lifecycle/gates and Action Authority. Do not revive pre-CR-0006 PASS for tasks whose acceptance changed, and do not infer LG-06 readiness from the superseded readiness review.

'''
s = s.replace(marker, current + marker, 1)

lines = s.splitlines()
if len(lines) < 3 or not lines[2].startswith('**Updated:** '):
    raise SystemExit('Updated header mismatch')
lines[2] = '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')
p.write_text(s, encoding='utf-8')

assert '`TSK-0146` is current **PASS**' in s
assert '## TSK-0146 current accepted stable state — 2026-08-30 — POST-CR-0006' in s
assert '## Historical TSK-0146 pre-CR-0006 accepted state — 2026-08-30 — SUPERSEDED' in s
assert 'b785c4a52217b24cf6eb9f66dce0773ddef7a639' in s
print('TSK0146_RUNTIME_TRANSFORM=PASS')
