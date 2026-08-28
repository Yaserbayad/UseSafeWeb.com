# TSK-0313 post-PASS L4 queue inspection

**Date:** 2026-08-28  
**Purpose:** conservative derived queue after TSK-0313 PASS. This report is not authority and does not change task state.

- Conservative PASS set size: 115
- Dependency-ready non-PASS AUTO_ALLOWED L4 candidates: 3

## Candidates in deterministic priority/WBS order

### TSK-0187 — Validate the proposed accountless critical journey before production coding
- **Priority:** HIGH
- **Dependencies:** TSK-0146
- **Acceptance:** ACC-0187 — Representative parents can complete the prototype, understand protection limits, and recover/remove without hidden facilitation; findings and contrary evidence are recorded.
- **AI / authority:** A3 / AUTO_ALLOWED
- **Requirements:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interfaces:** INT-0005
- **Notes:** 
- **Preflight flags:** REAL_OR_BEHAVIOR_EVIDENCE_CHECK

### TSK-0042 — Specify user support, exception, recovery, and removal requirements
- **Priority:** MEDIUM
- **Dependencies:** TSK-0041; TSK-0146
- **Acceptance:** ACC-0042 — Requirements identify accountless setup/journey-state recovery, device-configuration lifecycle, AdGuard/DNS integration, false-positive and unsupported-state incidents; remedies, escalation, data-minimising diagnostics, response expectations, deletion/removal/recovery and support-burden metrics are explicit. Account-access requirements remain excluded unless EXC-0001 is activated.
- **AI / authority:** A3 / AUTO_ALLOWED
- **Requirements:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interfaces:** INT-0001; INT-0002
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle. Legacy dependency on the superseded authenticated-dashboard baseline is replaced by the accountless equivalent. Legacy dependency on the superseded authenticated-dashboard baseline is replaced by the accountless equivalent. Pre-canonicalization audit correction 2026-08-27: reconciled to higher-authority DEC-0042 / EXC-0001 and/or the owner-authorized modular planning architecture; stable ID and dependency semantics preserved.
- **Preflight flags:** (none)

### TSK-0140 — Issue the post-validation product brief
- **Priority:** MEDIUM
- **Dependencies:** TSK-0138
- **Acceptance:** ACC-0140 — Brief is reviewed by owner, product, network, privacy, security, UX, support, and finance; conflicts with canonical decisions are resolved before approval.
- **AI / authority:** A3 / AUTO_ALLOWED
- **Requirements:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interfaces:** INT-0003; INT-0004
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.
- **Preflight flags:** OWNER_REVIEW_CHECK

