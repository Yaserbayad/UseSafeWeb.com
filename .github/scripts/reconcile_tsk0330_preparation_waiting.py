#!/usr/bin/env python3
from pathlib import Path

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')
heading = '## TSK-0330 prepared HUMAN_ONLY setup-flow boundary — 2026-08-29'
if heading in s or 'TSK-0330 — Design Phone → Internet → Services setup flows' in s:
    raise SystemExit('TSK-0330 runtime record already exists; refusing duplicate state')
block = '''

## TSK-0330 prepared HUMAN_ONLY setup-flow boundary — 2026-08-29

`TSK-0330 — Design Phone → Internet → Services setup flows`: **WAITING / non-PASS**. The task-specific Phone → Internet → Services design candidate has been prepared and technically verified, but WBS Action Authority is `HUMAN_ONLY`; Project Owner disposition is required before acceptance or PASS.

- Candidate: `design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md`, blob `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7`.
- Preparation evidence: `TSK_0330_PHONE_INTERNET_SERVICES_FLOW_PREPARATION_EVIDENCE_2026-08-29.md`, blob `a595b4cafaac10ae6262e296c6b5d482945d4e45`.
- Candidate verification run/job: `33279766680` / `99172831252`: SUCCESS; `TSK0330_WBS_AUTHORITY=PASS`; `TSK0330_SOURCE_PINS=PASS`; `TSK0330_ACCEPTANCE_COVERAGE=PASS`; 12-case deterministic branch matrix; scope/truth guards PASS; repository clean.
- Source pins: WBS `f23b4f017d1baf73258fa30ecd71549bbfe1b815`; TSK-0309 baseline `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`; TSK-0323 catalogue `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`.
- Dependency `TSK-0146` is frozen WBS PASS with no contradictory current evidence.
- The candidate covers prerequisites, step-by-step actions, verification/confirmation, already-configured/skip conditions, unsupported/conflict states, troubleshooting/removal/recovery, and truthful mixed-state Protection Map completion for Phone → Internet → Services. It introduces no account/dashboard/persistence/activity-history/payment or named-service scope.
- Downstream `TSK-0334` and `TSK-0335` remain unresolved HUMAN_ONLY work dependent on TSK-0330; `TSK-0333` remains downstream AUTO_ALLOWED work dependent on TSK-0334/TSK-0335. LG-06 is therefore not ready while these active-path L4 items remain unresolved.
- `DEC-0052 / CR-0005` sequencing remains unchanged; no pre-product parent/user/participant evidence is required or inferred.

Resolution condition: Project Owner must provide exactly `APPROVE TSK-0330 PHONE INTERNET SERVICES FLOWS` to accept the prepared candidate, or `REVISE TSK-0330: <specific change>` to reopen it. No TSK-0330 PASS, LG-06 PASS, L5/L6 authorization, real-user validation, public publication, payment, market activation or launch authority is inferred before the required disposition and subsequent verification/evidence/state reconciliation.
'''
s2 = s.rstrip('\n') + block + '\n'
p.write_text(s2, encoding='utf-8')
print('RUNTIME_TSK0330_PREPARATION_WAITING_EDIT=PASS')
