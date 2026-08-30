#!/usr/bin/env python3
from pathlib import Path
p=Path('CURRENT_STATE.md')
s=p.read_text(encoding='utf-8')
heading='## TSK-0335 prepared HUMAN_ONLY Protection Map boundary — 2026-08-30'
if heading in s or '`TSK-0335 — Design Protection Map and coverage-limit interactions`:' in s:
    raise SystemExit('TSK-0335 runtime record already exists; refusing duplicate state')
assert '## TSK-0334 accepted stable state — 2026-08-30' in s
assert '`TSK-0334 — Design support, false-positive, removal, and reconfiguration flows`: **PASS**' in s
block='''## TSK-0335 prepared HUMAN_ONLY Protection Map boundary — 2026-08-30

`TSK-0335 — Design Protection Map and coverage-limit interactions`: **WAITING / non-PASS**. The task-specific Protection Map / coverage-limit interaction candidate has been prepared and technically verified, but WBS Action Authority is `HUMAN_ONLY`; Project Owner disposition is required before acceptance or PASS.

- Candidate: `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`.
- Preparation evidence: `TSK_0335_PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_PREPARATION_EVIDENCE_2026-08-30.md`, blob `27fd622b84351c2eb6690167f7d6dd59b9dd5549`.
- Preflight run/job `33301129850` / `99229374133`: SUCCESS; exact WBS contract and all owning source identities pinned; repository clean.
- Candidate verification run/job `33301200786` / `99229572624`: SUCCESS; six-state model `6/6`; material-gap timing PASS; deterministic matrix `16`; later-L8 interaction hooks `8`; privacy/accessibility guards PASS; repository clean.
- Dependency `TSK-0330` is canonical PASS. `TSK-0334` is canonical PASS. `TSK-0333` remains ineligible until TSK-0335 PASS because it depends on both TSK-0334 and TSK-0335.
- Candidate preserves strict S1 `Verified` vs S2 parent-confirmed separation, immediate material-gap disclosure, mixed-state completion without an overall safety score, deterministic internal truth-state hooks, and future L8 comprehension-test interaction points without claiming any current human evidence.
- `DEC-0052 / CR-0005` sequencing remains unchanged; no pre-product parent/user/participant evidence is required or inferred.

Resolution condition: Project Owner must provide exactly `APPROVE TSK-0335 PROTECTION MAP COVERAGE-LIMIT INTERACTIONS` to accept the prepared candidate, or `REVISE TSK-0335: <specific change>` to reopen it. No TSK-0335 PASS, TSK-0333 execution, LG-06 PASS, L5/L6 authorization, real-user validation, public publication, payment, market activation or launch authority is inferred before the required disposition and subsequent verification/evidence/state reconciliation.'''
p.write_text(s.rstrip()+'\n\n'+block+'\n',encoding='utf-8')
print('RUNTIME_TSK0335_PREPARATION_WAITING_EDIT=PASS')
