# TSK-0138 post-PASS full L4 queue inspection

**Date:** 2026-08-28  
**Purpose:** derive dependency-ready L4 candidates after accepting TSK-0138, without treating readiness as automatic acceptance.

- Conservative current PASS set size: 91
- Dependency-ready non-PASS L4 candidates: 7

## Dependency-ready L4 candidates

### TSK-0187 — Validate the proposed accountless critical journey before production coding
- **Priority:** HIGH
- **Critical_Path:** NO
- **Dependencies:** TSK-0146
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0187
- **Acceptance_Criteria:** Representative parents can complete the prototype, understand protection limits, and recover/remove without hidden facilitation; findings and contrary evidence are recorded.
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005

### TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules
- **Priority:** HIGH
- **Critical_Path:** NO
- **Dependencies:** TSK-0146
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0229
- **Acceptance_Criteria:** Only fields necessary for the active journey exist; no browsing history or persistent child profile; expiry/deletion and diagnostic boundaries are testable.
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0018; REQ-0019; CON-0007; CON-0008
- **Interface_Reference:** INT-0006; INT-0007

### TSK-0408 — Define one coherent UseSafeWeb DNS identity and approved platform-specific endpoint/profile mechanisms
- **Priority:** HIGH
- **Critical_Path:** NO
- **Dependencies:** TSK-0146
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0408
- **Acceptance_Criteria:** Hostname/DoH path/profile naming, certificates, verification, removal, fallback, and environment separation are clear; no false universal FQDN workflow.
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0042; REQ-0043; REQ-0048; CON-0002; CON-0003
- **Interface_Reference:** INT-0013

### TSK-0140 — Issue the post-validation product brief
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0138
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0140
- **Acceptance_Criteria:** Brief is reviewed by owner, product, network, privacy, security, UX, support, and finance; conflicts with canonical decisions are resolved before approval.
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.
- **Preflight flags:** POTENTIAL_HUMAN_OR_REAL_EVIDENCE_BOUNDARY

### TSK-0143 — Specify native-device safeguard routing requirements
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0146
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0143
- **Acceptance_Criteria:** Requirements cover supported platform states, already-configured handling, parent confirmation, unsupported paths, stale guidance, and verification limitations.
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle. Legacy dependency on the superseded authenticated-dashboard baseline is replaced by the accountless equivalent.

### TSK-0330 — Design Phone → Internet → Services setup flows
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0146
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0330
- **Acceptance_Criteria:** Each flow has prerequisites, step-by-step actions, verification/confirmation, skip conditions, unsupported/conflict states, troubleshooting, and no misleading completion state.
- **AI_Capability_A0_A4:** A1
- **Action_Authority:** HUMAN_ONLY
- **Requirement_Reference:** REQ-0028; REQ-0029; CON-0010; CON-0017
- **Interface_Reference:** INT-0009; INT-0010
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle. Legacy dependency on the superseded authenticated-dashboard baseline is replaced by the accountless equivalent.
- **Preflight flags:** NON_AUTO_AUTHORITY

### TSK-0559 — Define the research, originality, usefulness, source, claims, update, localization, and pruning standard for first-phone content
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0558
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0559
- **Acceptance_Criteria:** Mass low-quality AI SEO is prohibited; every item solves a real high-intent job and connects to product/help with source/review/owner/metric.
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0075; REQ-0076; CON-0014; CON-0015
- **Interface_Reference:** INT-0019

