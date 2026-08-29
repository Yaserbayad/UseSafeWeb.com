#!/usr/bin/env python3
from pathlib import Path

p=Path('CURRENT_STATE.md')
s=p.read_text(encoding='utf-8')
old='## TSK-0330 prepared HUMAN_ONLY setup-flow boundary — 2026-08-29'
new='## TSK-0330 accepted stable state — 2026-08-29'
if new in s:
    print('RUNTIME_TSK0330_PASS_ALREADY_PRESENT=PASS')
    raise SystemExit(0)
start=s.find(old)
if start<0:
    raise SystemExit('prepared TSK-0330 boundary not found')
next_heading=s.find('\n## ', start+len(old))
end=len(s) if next_heading<0 else next_heading+1
block='''## TSK-0330 accepted stable state — 2026-08-29

`TSK-0330 — Design Phone → Internet → Services setup flows`: **PASS** under the current WBS acceptance contract. Project Owner explicitly approved `APPROVE TSK-0330 PHONE INTERNET SERVICES FLOWS` at `2026-08-29T23:06:35Z`, closing the task's `HUMAN_ONLY` decision boundary for the exact verified candidate blob.

- Accepted candidate: `design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md`, blob `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7`.
- Preparation evidence: `TSK_0330_PHONE_INTERNET_SERVICES_FLOW_PREPARATION_EVIDENCE_2026-08-29.md`, blob `a595b4cafaac10ae6262e296c6b5d482945d4e45`.
- Final acceptance evidence: `TSK_0330_PHONE_INTERNET_SERVICES_FLOW_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `794e12b56e902270f6d4ef052abaa2d1fba1963b`.
- Preparation verification run/job `33279766680` / `99172831252`: SUCCESS; all seven acceptance elements and the 12-case deterministic branch matrix passed.
- Final owner-bound acceptance run/job `33280241901` / `99174073706`: SUCCESS; `TSK0330_OWNER_APPROVAL_BINDING=PASS`; `TSK0330_APPROVED_BLOB_IDENTITY=PASS`; `TSK0330_ACCEPTANCE_CONTRACT=PASS`; `TSK0330_FINAL_ACCEPTANCE=PASS`; repository clean.
- Source WBS blob: `f23b4f017d1baf73258fa30ecd71549bbfe1b815`. Dependency `TSK-0146` remains frozen PASS with no contradictory current evidence.
- Accepted scope remains accountless-first and preserves independent Phone / Internet / Service evidence states, exact Android/iPhone DNS values, truthful mixed-state Protection Map completion, safe unsupported/conflict/removal behavior, and zero valid external services unless a separately approved current named-service record exists.
- No account/dashboard/persistence/activity-history/payment scope, pre-product participant evidence, LG-06/L5/L6 authority, publication, market activation or launch authority is created by this task PASS.
- `DEC-0052 / CR-0005` sequencing remains unchanged.
'''
pre=s[:start].rstrip('\n')
post=s[end:].lstrip('\n')
out=pre+'\n\n'+block.rstrip('\n')
if post:
    out+='\n\n'+post.rstrip('\n')
out+='\n'
p.write_text(out,encoding='utf-8')
print('RUNTIME_TSK0330_PASS_EDIT=PASS')
