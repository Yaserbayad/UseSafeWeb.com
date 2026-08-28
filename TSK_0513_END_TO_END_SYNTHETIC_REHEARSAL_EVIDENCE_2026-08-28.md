# TSK-0513 — End-to-end synthetic rehearsal verification evidence

**Task:** TSK-0513 — Run end-to-end synthetic rehearsal  
**Acceptance:** ACC-0513  
**Date:** 2026-08-28  
**Verification:** guarded GitHub Actions machine audit  
**Run:** 33181725004  
**Job:** verify

## Exact artifacts

- Rehearsal report: `TSK_0513_END_TO_END_SYNTHETIC_REHEARSAL_2026-08-28.md`, blob `1c90d5e5734832c1e5b26d83fdb21e6aefc2305e`.
- Synthetic fixture: `fixtures/experiment1/TSK_0513_SYNTHETIC_REHEARSAL_FIXTURE_V1.json`, blob `8189de9d6f5fa554ff23fb127f95604c8fc381a5`.
- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `2e4560103b71bb350b14673ce3e415afc3dbfe3a`.
- Runtime state before TSK-0513 reconciliation: `4f438a44a51b9f77e1434f6a3b2e300bd5a1c819`.

## Verification result

The machine audit parsed the exact TSK-0513 WBS row and ACC-0513 text, validated all required synthetic participant-schema fields and controlled values, verified all participant/case IDs are explicit `SYN-*` fixtures with no real-person mapping, checked the 16-step main rehearsal path, verified support/false-positive, withdrawal/removal and safeguarding-boundary branches, and rejected the defined prohibited-data key classes.

Rehearsal-execution blockers: none. Real-participant legal/contact blockers remain explicitly DEFERRED/OPEN and are **not** treated as cleared for G-03/LG-04. G-02/LG-03 remains DEFER; recruitment and real-participant processing remain unauthorized.

**Stable verification outcome: TSK-0513 = PASS candidate pending runtime reconciliation/read-back.**

## Direct WBS successors containing TSK-0513 as a hard dependency

| Task | Stage | Title | Plan status | WBS execution state | Priority | Dependencies | AI capability | Action authority | Trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TSK-0173 | L3 | Verify Experiment-1 launch entry criteria | PLANNED | WAITING | MEDIUM | TSK-0028; TSK-0513 | A2 | HUMAN_APPROVAL_REQUIRED | Applicable lifecycle/gate and all hard dependencies satisfied. |
