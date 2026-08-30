#!/usr/bin/env python3
from pathlib import Path

p=Path('CURRENT_STATE.md')
s=p.read_text(encoding='utf-8')
heading='## TSK-0335 prepared HUMAN_ONLY Protection Map boundary — 2026-08-30'
assert heading in s, 'expected TSK-0335 WAITING heading missing'
assert '`TSK-0335 — Design Protection Map and coverage-limit interactions`: **WAITING / non-PASS**' in s
assert '7c65a697a98961d0df278658e59262ce39874ff5' in s
assert '27fd622b84351c2eb6690167f7d6dd59b9dd5549' in s
start=s.index(heading)
prefix=s[:start].rstrip()
block='''## TSK-0335 accepted stable state — 2026-08-30

`TSK-0335 — Design Protection Map and coverage-limit interactions`: **PASS** under the current WBS acceptance contract. Project Owner explicitly approved `APPROVE TSK-0335 PROTECTION MAP COVERAGE-LIMIT INTERACTIONS` at `2026-08-30T09:01:35Z`, closing the task's `HUMAN_ONLY` decision boundary for the exact verified candidate blob.

- Accepted candidate: `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`.
- Preparation evidence: `TSK_0335_PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_PREPARATION_EVIDENCE_2026-08-30.md`, blob `27fd622b84351c2eb6690167f7d6dd59b9dd5549`.
- Final acceptance evidence: `TSK_0335_PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_ACCEPTANCE_EVIDENCE_2026-08-30.md`, blob `0d1c67746dd2d12c397fae306f9f842d9ae4db25`.
- Preflight run/job `33301129850` / `99229374133`: SUCCESS; exact WBS/source identities pinned.
- Candidate verification run/job `33301200786` / `99229572624`: SUCCESS; six-state model `6/6`, material-gap timing PASS, deterministic truth-state matrix `16/16`, later-L8 interaction points `8/8`, privacy/accessibility guards and repository cleanliness PASS.
- Final owner-bound acceptance run/job `33303080298` / `99234682891`: SUCCESS; `TSK0335_OWNER_APPROVAL_BINDING=PASS`; `TSK0335_APPROVED_BLOB_IDENTITY=PASS`; `TSK0335_ACCEPTANCE_CONTRACT=PASS`; `TSK0335_FINAL_ACCEPTANCE=PASS`; repository clean.
- Dependency `TSK-0330` remains canonical PASS. `TSK-0334` remains canonical PASS. Their conjunction satisfies the known direct predecessor set for `TSK-0333`, subject to fresh WBS/gate/queue derivation.
- Accepted scope preserves strict S1 `Verified` vs S2 parent-confirmed separation, immediate material-gap disclosure, mixed-state completion without an overall safety score, deterministic truth-state hooks, later-L8 comprehension-test interaction points, accountless-first operation, and current accessibility/RTL/privacy fences.
- `DEC-0052 / CR-0005` sequencing remains unchanged. No current human comprehension evidence, LG-06/L5/L6 authority, publication, payment, market activation or launch authority is created by this PASS.

### Queue status after TSK-0335 acceptance

Do not infer a successor from task numbering. Recompute current eligibility from WBS, dependencies, gates, runtime evidence and Action Authority after this state write/read-back.
'''
p.write_text(prefix+'\n\n'+block,encoding='utf-8')
print('RUNTIME_TSK0335_PASS_EDIT=PASS')
