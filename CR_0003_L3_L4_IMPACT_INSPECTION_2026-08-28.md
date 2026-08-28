# CR-0003 L3 to L4 impact inspection

- WBS rows: 641
- L3 tasks: 31
- L4 tasks: 68
- L4 roots (no L4 predecessor): 5
- L4 tasks with direct L3 dependency: 2

## L3 tasks directly feeding L4

### TSK-0034 — Produce aggregate/anonymised Experiment-1 report
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.01.005; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0040 — Persist Experiment-1 evidence and decision in GitHub
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0039
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0040
- **Acceptance_Criteria:** No participant identity/raw browsing data is committed; commit SHA is verified; CURRENT_STATE and WBS statuses agree.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.06.01.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

## L4 roots

### TSK-0139 — Translate the G-04 decision into authorised product outcomes
- **Lifecycle_Stage:** L4
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0040
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0139
- **Acceptance_Criteria:** Mandate identifies the validated job, target user, required outcome, unresolved evidence, constraints, stop conditions, and explicitly authorised build scope.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-04.01.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0146 — Freeze accountless-first product baseline and optional-account trigger
- **Lifecycle_Stage:** L4
- **Plan_Status:** COMPLETED_CANDIDATE
- **Execution_State:** PASS
- **Priority:** CRITICAL
- **Critical_Path:** NO
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0146
- **Acceptance_Criteria:** Product brief states no mandatory UseSafeWeb account, preserves immediate value, defines the exact future persistence/account trigger and owner authority, and supersedes the v1.4 dashboard-first mandate.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; source or exact environment; verification output; date; verifier; deviations and disposition.
- **Primary_Owner:** Project Owner
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Source_Reference:** Latest owner master prompt 2026-08-27

### TSK-0147 — Freeze targeted market, technical availability, and official localized-market semantics
- **Lifecycle_Stage:** L4
- **Plan_Status:** COMPLETED_CANDIDATE
- **Execution_State:** PASS
- **Priority:** HIGH
- **Critical_Path:** NO
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0147
- **Acceptance_Criteria:** UK is targeted/optimized first; broader technical availability is not represented as official localization/support; Turkey/Arabic markets use explicit activation gates.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; source or exact environment; verification output; date; verifier; deviations and disposition.
- **Primary_Owner:** Project Owner
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Source_Reference:** Latest owner master prompt 2026-08-27

### TSK-0148 — Apply the owner-approved optimization order to product and roadmap decisions
- **Lifecycle_Stage:** L4
- **Plan_Status:** COMPLETED_CANDIDATE
- **Execution_State:** PASS
- **Priority:** HIGH
- **Critical_Path:** NO
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0148
- **Acceptance_Criteria:** Roadmap prioritization demonstrably orders correct product, exceptional UX, customer value, reliability/trust, quality, simplicity, autonomy, execution/operations/cost and rejects superficial speed.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Evidence_Required:** Artifact/version; source or exact environment; verification output; date; verifier; deviations and disposition.
- **Primary_Owner:** Project Owner
- **AI_Capability_A0_A4:** A1
- **Action_Authority:** HUMAN_ONLY
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Source_Reference:** Latest owner master prompt 2026-08-27

### TSK-0558 — Freeze the USD 20-50/month discretionary budget, earned-distribution priority, and one-primary/one-challenger rule
- **Lifecycle_Stage:** L4
- **Plan_Status:** COMPLETED_CANDIDATE
- **Execution_State:** PASS
- **Priority:** HIGH
- **Critical_Path:** NO
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0558
- **Acceptance_Criteria:** GTM plan cannot require paid acquisition or simultaneous platform programs; spend caps/accumulation/approval and channel stop rules are explicit.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Evidence_Required:** Artifact/version; source or exact environment; verification output; date; verifier; deviations and disposition.
- **Primary_Owner:** Growth
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0075; REQ-0076; CON-0014; CON-0015
- **Interface_Reference:** INT-0019
- **Source_Reference:** Latest owner master prompt 2026-08-27

## L4 tasks with direct L3 dependencies

### TSK-0139 — Translate the G-04 decision into authorised product outcomes
- **Lifecycle_Stage:** L4
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0040
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0139
- **Acceptance_Criteria:** Mandate identifies the validated job, target user, required outcome, unresolved evidence, constraints, stop conditions, and explicitly authorised build scope.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0007; REQ-0008; CON-0001; CON-0002
- **Interface_Reference:** INT-0003; INT-0004
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-04.01.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0326 — Synthesize experiment friction, comprehension, and support evidence
- **Lifecycle_Stage:** L4
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0034; TSK-0043
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0326
- **Acceptance_Criteria:** Each problem states evidence frequency/severity, affected cohort/path, root-cause hypothesis, business/safety impact, and whether design can address it.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** UX Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0028; REQ-0029; CON-0010; CON-0017
- **Interface_Reference:** INT-0009; INT-0010
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-04.03.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

## L3 exit / gate / outcome candidates

### TSK-0029 — Decide whether Wave A permits controlled iteration
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.03.01.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0030 — Validate and freeze Experiment-1 analysis dataset
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0031 — Calculate activation and incremental-safeguard results
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.01.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0032 — Calculate abandonment, duplication, and support-burden results
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.01.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0033 — Calculate comprehension, compatibility, and 14-day persistence results
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.01.004; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0034 — Produce aggregate/anonymised Experiment-1 report
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.01.005; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0035 — Delete participant contact details after follow-up
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.02.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0036 — Aggregate/anonymise findings and delete participant-level metrics
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.05.02.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0037 — Authorise or deny Experiment-1 recruitment
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.01.01.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0038 — Run cross-functional Experiment-1 evidence review
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0034
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0038
- **Acceptance_Criteria:** Review addresses all thresholds, serious incidents, data quality, support economics, platform differences, sample limitations, and alternative explanations.
- **Verification_Method:** Use the approved checklist/test procedure against the exact artifact/environment; retain reproducible outputs and reviewer result.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.06.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0039 — Decide continue to minimal MCP, modify/repeat, pivot, or stop
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0038
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0039
- **Acceptance_Criteria:** Decision states outcome, evidence, unresolved uncertainty, accepted risks, authorised scope, prohibited scope, next gate, and whether build funding/time is approved.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Owner
- **AI_Capability_A0_A4:** A1
- **Action_Authority:** HUMAN_ONLY
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.06.01.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0040 — Persist Experiment-1 evidence and decision in GitHub
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0039
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0040
- **Acceptance_Criteria:** No participant identity/raw browsing data is committed; commit SHA is verified; CURRENT_STATE and WBS statuses agree.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0001; REQ-0002; CON-0020; CON-0021
- **Interface_Reference:** INT-0001; INT-0002
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.06.01.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0170 — Select the single coherent Wave B refinement
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0029
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0170
- **Acceptance_Criteria:** Decision cites Wave A evidence, expected mechanism, affected steps, non-goals, and unchanged primary metrics.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.03.02.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0171 — Re-run privacy, safety, technical, and measurement check for Wave B
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0306
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0171
- **Acceptance_Criteria:** Review records changes, affected risks, test evidence, updated materials, and explicit authorisation to recruit/execute Wave B.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.03.02.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0172 — Analyze Wave A activation, abandonment, support, comprehension, and persistence
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0496
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0172
- **Acceptance_Criteria:** Report includes denominator definitions, rates, help minutes, stage/reason breakdowns, device patterns, false positives, comprehension, 14-day state, and uncertainty.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.03.01.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0173 — Verify Experiment-1 launch entry criteria
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
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.01.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0174 — Recruit and qualify Wave A participants
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0176
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0174
- **Acceptance_Criteria:** Ten qualified participants meet all cohort rules; disqualified reasons are recorded without excess personal data; notices and scheduling are complete.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.01.02.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0175 — Recruit and qualify Wave B participants
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0171
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0175
- **Acceptance_Criteria:** Total qualified starters across both waves is 20–30; Wave B participants meet the same criteria and have not seen an incompatible earlier version.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.01.02.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0176 — Select lean recruitment channels for the qualified cohort
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0037
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0176
- **Acceptance_Criteria:** Plan identifies channel, invitation owner, expected qualification path, privacy notice timing, and prohibits paid acquisition/channel conclusions.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.01.02.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0177 — Measure Protection Map and coverage-gap comprehension
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0180
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0177
- **Acceptance_Criteria:** Result uses a predefined scoring rule; facilitator does not teach the answer before measurement; failures are classified.
- **Verification_Method:** Reproduce calculations from versioned source data; verify definitions, denominators, time window, uncertainty, and privacy limits.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.02.01.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0178 — Complete Wave A 14-day follow-ups
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0180
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0178
- **Acceptance_Criteria:** Each participant has active/inactive/unknown status, reason, support needed, and false-positive/compatibility cause where applicable; contact data then enters deletion schedule.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.02.01.006; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0179 — Monitor Wave A immediate-stop conditions
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0180
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0179
- **Acceptance_Criteria:** Each session/incident is checked; stop events trigger immediate suspension, incident response, owner decision, and no further activation until reauthorised.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A4
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.02.01.005; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0180 — Run Wave A concierge setup sessions
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0180
- **Acceptance_Criteria:** All applicable real actions are attempted; full activation is calculated from the frozen definition; facilitator does not silently complete the setup; intervention minutes and reasons are recorded.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.02.01.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0181 — Deliver pre-session notice and confirm voluntary participation
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0174
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0181
- **Acceptance_Criteria:** Participant received current notice version; voluntary continuation and contact route are recorded without treating consent as the lawful basis by default.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.02.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0182 — Triage Wave A setup failures, false positives, and compatibility issues
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0180
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0182
- **Acceptance_Criteria:** Every issue has severity, category, intervention time, diagnostic authorisation where needed, resolution, participant impact, and deletion evidence.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Support
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.02.01.004; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0183 — Complete Wave B 14-day follow-ups
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0185
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0183
- **Acceptance_Criteria:** Each participant has a 14-day status and reason; contact deletion timing begins immediately after follow-up.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.04.01.004; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0184 — Monitor Wave B stop conditions
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0185
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0184
- **Acceptance_Criteria:** Any serious privacy/security/safety event suspends processing and triggers owner review before further sessions.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Project Governance
- **AI_Capability_A0_A4:** A4
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.04.01.003; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0185 — Run Wave B concierge setup sessions
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0175; TSK-0171
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0185
- **Acceptance_Criteria:** All qualified participants receive the approved version; interventions, activation, incremental safeguards, abandonment, comprehension, and immediate issues are captured consistently.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/Research
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.04.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0186 — Triage Wave B technical and support issues
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0185
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0186
- **Acceptance_Criteria:** All interventions have time, category, root cause, resolution, participant impact, and diagnostic deletion evidence where applicable.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Support
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0013; REQ-0014; CON-0025; CON-0009
- **Interface_Reference:** INT-0005
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.04.01.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0306 — Update journey, instructions, scripts, and support materials
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0170
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0306
- **Acceptance_Criteria:** All affected materials share one version; privacy/claims remain accurate; activation definition and primary metrics are unchanged.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Product/UX
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0028; REQ-0029; CON-0010; CON-0017
- **Interface_Reference:** INT-0009; INT-0010
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.03.02.002; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

### TSK-0496 — Clean and validate Wave A structured records
- **Lifecycle_Stage:** L3
- **Plan_Status:** PLANNED
- **Execution_State:** WAITING
- **Priority:** MEDIUM
- **Critical_Path:** NO
- **Dependencies:** TSK-0178
- **Trigger:** Applicable lifecycle/gate and all hard dependencies satisfied.
- **Preconditions:** Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.
- **Acceptance_ID:** ACC-0496
- **Acceptance_Criteria:** No prohibited fields exist; missing/inconsistent values are resolved or documented; activation is reproducible from raw structured fields.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Evidence_Required:** Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.
- **Primary_Owner:** Analytics
- **AI_Capability_A0_A4:** A3
- **Action_Authority:** AUTO_ALLOWED
- **Requirement_Reference:** REQ-0060; REQ-0061; CON-0007; CON-0008
- **Interface_Reference:** INT-0016
- **Source_Reference:** UseSafeWeb_Master_Plan-1.4.md::USW-03.03.01.001; canonical repository Yaserbayad/UseSafeWeb.com@c672991229acc7675f1e25b978af6fbdacd04590
- **Notes:** Future gate/dependency not yet satisfied. Valid work is retained but re-owned by one responsibility package and attached to the new L0-L13 lifecycle.

