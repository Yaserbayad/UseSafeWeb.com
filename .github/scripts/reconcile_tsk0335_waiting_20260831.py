import subprocess
from pathlib import Path

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
BASE=ROOT/'design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md'
AMEND=ROOT/'design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md'
EVIDENCE=ROOT/'TSK_0335_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md'

EXPECTED={
 RUNTIME:'f1c209ffd4e6816ca115ca71a3353291bd036f7c',
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 BASE:'7c65a697a98961d0df278658e59262ce39874ff5',
 AMEND:'80db66d9261e6ccf85e0253530819ad262b39497',
 EVIDENCE:'03e7a35b7943586d635975fdc9a53bfd0e99ee44',
}

def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()

def req(cond,msg):
    if not cond:
        raise SystemExit(msg)

for path,expected in EXPECTED.items():
    req(path.exists(),f'TSK0335_WAITING_INPUT_MISSING={path.as_posix()}')
    req(blob(path)==expected,f'TSK0335_WAITING_INPUT_CHANGED={path.as_posix()}')

text=RUNTIME.read_text(encoding='utf-8')
current_heading='## TSK-0335 current waiting state — 2026-08-31 — POST-CR-0007'
historical_heading='## TSK-0335 accepted stable state — 2026-08-30'
req(current_heading not in text,'TSK0335_WAITING_ALREADY_RECORDED')
req(historical_heading in text,'TSK0335_HISTORICAL_SECTION_MISSING')
req('## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007' in text,'TSK0335_CURRENT_DEPENDENCY_MISSING')

section='''## TSK-0335 current waiting state — 2026-08-31 — POST-CR-0007

`TSK-0335 — Design Protection Map and coverage-limit interactions`: **WAITING / HUMAN_APPROVAL_REQUIRED** under current `ACC-0335 / VER-0335 / EVD-0335` and post-CR-0007 authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependency `TSK-0330`, A1 / `HUMAN_ONLY`.
- Dependency `TSK-0330` is current-qualified PASS.
- Historical owner-approved base remains `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`; its unchanged six-state/no-score/material-gap/deterministic/L8-hook semantics remain valid evidence.
- Current-scope amendment candidate: `design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md`, version `1.0.0-post-cr0007`, blob `80db66d9261e6ccf85e0253530819ad262b39497`.
- Preparation evidence: `TSK_0335_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md`, blob `03e7a35b7943586d635975fdc9a53bfd0e99ee44`.
- Deterministic preparation run/job `33430327495 / 99613846431`: **SUCCESS**; exact input blobs, current WBS/graph, current dependency and HUMAN_ONLY boundary, historical truth contract, dual-mode amendment, privacy/accessibility fences, current-source alignment, `git diff --check`, and clean-worktree checks PASS.
- The amendment supersedes only stale accountless-only whole-product assumptions: the optional dashboard may present the same Protection Map truth model, while saved records/accounts/sessions never create `Verified`, stale results are not treated as current, and account/data lifecycle remains distinct from physical protection removal.
- The historical 2026-08-30 owner approval does **not** approve this later current-scope amendment.
- Deterministic resolution condition: exact Project Owner approval `APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT`, followed by final owner-bound verification and guarded runtime PASS reconciliation.
- Until that condition is satisfied, TSK-0335 is non-PASS; TSK-0333, LG-06, implementation, real-user validation and launch do not inherit PASS.
- `RSK-0002` remains OPEN/non-blocking before L8.

'''
pos=text.index(historical_heading)
text=text[:pos]+section+text[pos:]
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]='**Updated:** 2026-08-31T19:23:58Z'
        break
RUNTIME.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
print('TSK0335_WAITING_RUNTIME_PRECONDITIONS=PASS')
