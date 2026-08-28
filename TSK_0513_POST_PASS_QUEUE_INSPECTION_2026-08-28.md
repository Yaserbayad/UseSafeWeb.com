# TSK-0513 post-verification queue inspection

**Date:** 2026-08-28  
**Run:** 33181787037  
**Purpose:** inspect exact WBS prerequisites around the sole direct TSK-0513 successor before runtime PASS reconciliation.  
**TSK-0513 evidence blob:** `717a59aaf8e748e302b4a1aa972c2d3d2936d3aa`.

## TSK-0028 — Update canonical state after G-02 decision

- **Lifecycle_Stage:** L2
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** HIGH
- **Critical_Path:** YES
- **Dependencies:** TSK-0027; TSK-0011
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker. Owner-frozen final plan is published and fetch-verified; governance hold is released.
- **Acceptance_ID:** ACC-0028
- **Acceptance_Criteria:** Canonical files agree on the outcome; evidence links are preserved; no contradictory “ready” or “blocked” status remains.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0173 — Verify Experiment-1 launch entry criteria

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0028; TSK-0513
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0173
- **Acceptance_Criteria:** Every entry criterion has direct evidence; any unresolved safety/privacy/technical blocker results in DEFER or FAIL.
- **Verification_Method:** Use the approved checklist/test procedure against the exact artifact/environment; retain reproducible outputs and reviewer result.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A2
- **Action_Authority:** HUMAN_APPROVAL_REQUIRED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **CURRENT_STATE references:**
  - none found

## TSK-0037 — Authorise or deny Experiment-1 recruitment

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0173
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0037
- **Acceptance_Criteria:** Decision includes scope, cohort, permitted dates/sequence, stop conditions, incident contacts, and work unlocked.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Owner
- **AI_Capability_A0_A4:** A1
- **Action_Authority:** HUMAN_ONLY
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0036 — Aggregate/anonymise findings and delete participant-level metrics

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0039
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0036
- **Acceptance_Criteria:** Aggregate report cannot reasonably be re-linked; all participant-level copies are deleted from collection, working, backup, and export locations by deadline.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Privacy Engineering
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0035 — Delete participant contact details after follow-up

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0183
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0035
- **Acceptance_Criteria:** Every participant has deletion date, data locations, executor, verification, and exception if any; no contact data remains after deadline.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Privacy Engineering
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0034 — Produce aggregate/anonymised Experiment-1 report

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0031; TSK-0032; TSK-0033
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0034
- **Acceptance_Criteria:** Report contains all ten protocol outputs, distinguishes Wave A/B, identifies serious incidents, states uncertainty, and recommends continue/modify/pivot/stop.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0033 — Calculate comprehension, compatibility, and 14-day persistence results

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0030
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0033
- **Acceptance_Criteria:** Report compares ≥80% comprehension and ≥70% 14-day persistence, quantifies >30% friction removal risk, and provides platform/root-cause breakdown.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Analytics
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0032 — Calculate abandonment, duplication, and support-burden results

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0030
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0032
- **Acceptance_Criteria:** Report compares ≤25% add/duplicate-work abandonment and ≤30% substantial help, gives median/mean help minutes, and classifies dominant causes.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Analytics
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0031 — Calculate activation and incremental-safeguard results

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0030
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0031
- **Acceptance_Criteria:** Report states counts, denominators, wave/device breakdown, ≥60% and ≥50% comparisons, and uncertainty without population generalisation.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Analytics
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0030 — Validate and freeze Experiment-1 analysis dataset

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0183
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0030
- **Acceptance_Criteria:** All 20–30 records are dispositioned; eligibility and wave are explicit; prohibited data is absent; formulas reproduce activation and thresholds.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Analytics
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

## TSK-0029 — Decide whether Wave A permits controlled iteration

- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0172
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0029
- **Acceptance_Criteria:** Owner reviews incidents and metrics; decision states continue, pause/remediate, or stop with evidence and work unlocked.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **CURRENT_STATE references:**
  - none found

