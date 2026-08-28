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

## L4 tasks whose acceptance/evidence wording may require real behavioral evidence

### TSK-0041 — Specify baseline DNS-protection activation requirements
- **Dependencies:** TSK-0143
- **Acceptance_Criteria:** Requirements cover endpoint format, DoH setup, filtering verification, fail-safe behavior, uninstall/removal, Private Relay/VPN conflicts, false positives, and no-history constraints.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0044 — Define AdGuard API compatibility, credential-isolation and failure NFRs
- **Dependencies:** TSK-0484; TSK-0538; TSK-0146
- **Acceptance_Criteria:** NFRs define the private/restricted AdGuard administration path, secret storage/rotation, API/config timeouts/retries, partial-failure reconciliation, opaque setup/configuration identifiers if technically required, explicit privacy booleans, version/contract regression checks, and safe behavior when AdGuard or the verification path is unavailable; no mandatory customer-authentication or persistent datastore dependency is introduced.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0046 — Define performance and capacity NFRs
- **Dependencies:** TSK-0538
- **Acceptance_Criteria:** NFRs state expected pilot load, safety margin, DNS latency/availability test method, web journey performance, degradation behavior, and capacity-review trigger.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0139 — Translate the G-04 decision into authorised product outcomes
- **Dependencies:** TSK-0040
- **Acceptance_Criteria:** Mandate identifies the validated job, target user, required outcome, unresolved evidence, constraints, stop conditions, and explicitly authorised build scope.
- **Verification_Method:** Review the complete evidence index, contrary evidence, risks, and authority; record an explicit stable decision and work unlocked.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0141 — Freeze minimum product scope and non-goals
- **Dependencies:** TSK-0139
- **Acceptance_Criteria:** Every included capability maps to a validated need, mandatory operation/safety requirement, or explicit owner-approved architectural decision. The first coded product is accountless-first and uses only the minimum public/setup application and DNS integration needed for the validated journey; mandatory authentication, persistent parent dashboard and customer-facing AdGuard control plane remain deferred under EXC-0001, while surveillance/activity history, child accounts and other advanced capabilities remain excluded unless separately reauthorised.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0146 — Freeze accountless-first product baseline and optional-account trigger
- **Dependencies:** 
- **Acceptance_Criteria:** Product brief states no mandatory UseSafeWeb account, preserves immediate value, defines the exact future persistence/account trigger and owner authority, and supersedes the v1.4 dashboard-first mandate.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0147 — Freeze targeted market, technical availability, and official localized-market semantics
- **Dependencies:** 
- **Acceptance_Criteria:** UK is targeted/optimized first; broader technical availability is not represented as official localization/support; Turkey/Arabic markets use explicit activation gates.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0297 — Publish concise brand guidelines, source/editable asset library, versioning, ownership, and usage rules
- **Dependencies:** TSK-0300
- **Acceptance_Criteria:** A human or AI can generate a compliant asset without guessing; deprecated assets are traceable; no font files are exposed as user deliverables.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0298 — Create the evidence-grounded brand strategy, promise, personality, audience, differentiation, trust, and prohibited-expression brief
- **Dependencies:** TSK-0187
- **Acceptance_Criteria:** Brief is traceable to validated customer/product evidence and non-surveillance/claims constraints; it is approved before identity finalization.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0299 — Define tone, voice, terminology, trust language, protection-state language, and communication examples
- **Dependencies:** TSK-0298
- **Acceptance_Criteria:** Verbal system is clear to normal parents, child-aware, non-alarmist, non-technical, legally/claims reviewed, and reusable across surfaces/locales.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0301 — Finalize logo system, typography, color, imagery, iconography, visual language, and layout principles
- **Dependencies:** TSK-0302; TSK-0299
- **Acceptance_Criteria:** Owner approves one system; all masters are editable/versioned; small/mobile/mono/contrast/readability uses pass; no safety guarantee is implied visually.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0302 — Develop and evaluate a small set of coherent visual identity directions
- **Dependencies:** TSK-0298
- **Acceptance_Criteria:** Directions are distinct, accessible, scalable, editable, aligned to brand strategy, and evaluated without premature high-volume asset production.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0308 — Create the shared responsive design system for public and product surfaces
- **Dependencies:** TSK-0309; TSK-0300
- **Acceptance_Criteria:** Components include content/error/loading/verification/uncertain/recovery states, tokens, accessibility behavior, localization expansion, and implementation specs.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0309 — Correct the prototype from usability/comprehension evidence and freeze the implementation-ready experience baseline
- **Dependencies:** TSK-0310; TSK-0187
- **Acceptance_Criteria:** Material findings have root cause/disposition; critical friction/comprehension/accessibility failures are corrected and retested; speculative features are excluded.
- **Verification_Method:** Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0311 — Define translation keys/files, locale metadata, plural/date rules, content ownership, localized instruction variants, and fallback behavior
- **Dependencies:** TSK-0318
- **Acceptance_Criteria:** English baseline uses externalized content; no hard-coded UI copy blocks Turkish/Arabic; locale fallback and content versioning are testable.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0312 — Specify parent authentication, account/session, and minimal intake requirements
- **Dependencies:** TSK-0140
- **Acceptance_Criteria:** Requirements define Google social sign-in, account/session lifecycle, minimal required identity fields, logout/revocation/deletion, intake fields, prohibited data, validation, errors, resume/expiry behavior, CSRF/session protections and test cases; no password or SMS authentication is introduced without a later decision.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0313 — Specify Protection Map state and evidence requirements
- **Dependencies:** TSK-0041; TSK-0144; TSK-0146
- **Acceptance_Criteria:** Every Protection Map state has entry/evidence rules, parent-facing copy, transition rules, unsupported behavior, persistence scope, device/journey-state boundary and testable examples; parent-confirmed and system-verified states are never conflated; no account ownership model is assumed in the active baseline.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0314 — Define accessibility, responsive, browser, OS, and device support NFRs
- **Dependencies:** TSK-0046
- **Acceptance_Criteria:** Requirements define target WCAG level, keyboard/screen-reader/text-resize behavior, supported browsers/OS versions, device test tiers, and unsupported-state messaging.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0315 — Create the accountless end-to-end service blueprint from discovery through recovery/removal
- **Dependencies:** TSK-0149; TSK-0229
- **Acceptance_Criteria:** Blueprint identifies parent actions, system actions, evidence states, dependencies, failures, automated support, privacy, and owner-only exceptions.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0316 — Define a friction budget and challenge every click, field, choice, confirmation, account, and manual step
- **Dependencies:** TSK-0315
- **Acceptance_Criteria:** Each retained interaction has a decision/technical/safety reason; removable steps are removed; platform constraints are explicit; unsupported one-click claims are absent.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems
- **Dependencies:** TSK-0315
- **Acceptance_Criteria:** Each page/screen has one purpose, entry/exit, content owner, SEO/index intent, privacy/accessibility requirement, and no duplicated or missing critical step.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0320 — Freeze the protection-state model and copy rules
- **Dependencies:** TSK-0315
- **Acceptance_Criteria:** Protected/verified, configured/parent-confirmed, action-needed, not-covered, uncertain/error, and removed states have exact evidence and transition rules; no confirmation masquerades as verification.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0322 — Create product voice, claims, and terminology guide
- **Dependencies:** TSK-0327
- **Acceptance_Criteria:** Guide includes approved/prohibited claims, state labels, child-readable principles, reading-level goals, and review ownership; no complete-safety promise is allowed.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0323 — Create versioned device and service instruction catalogue
- **Dependencies:** TSK-0322
- **Acceptance_Criteria:** Every instruction has platform/version applicability, source reference, last verified date, owner, expected result, fallback, and test case; unsupported states are explicit.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0324 — Define lightweight visual identity and reusable UI component rules
- **Dependencies:** TSK-0322
- **Acceptance_Criteria:** System covers typography, spacing, contrast, focus, controls, feedback, four Protection Map states, mobile/desktop behavior, logo/domain use, and accessible component specifications.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0325 — Create end-to-end parent journey and service blueprint
- **Dependencies:** TSK-0326
- **Acceptance_Criteria:** Map covers normal, already-configured, unsupported, failed-activation, false-positive, resume, removal, and support paths; each touchpoint maps to requirements.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0326 — Synthesize experiment friction, comprehension, and support evidence
- **Dependencies:** TSK-0034; TSK-0043
- **Acceptance_Criteria:** Each problem states evidence frequency/severity, affected cohort/path, root-cause hypothesis, business/safety impact, and whether design can address it.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0327 — Resolve critical usability, trust, and accessibility findings
- **Dependencies:** TSK-0336
- **Acceptance_Criteria:** All critical/high findings are fixed or formally accepted by the owner with rationale; retest evidence confirms critical paths and Protection Map comprehension.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0328 — Define information architecture and navigation model
- **Dependencies:** TSK-0325
- **Acceptance_Criteria:** Architecture supports the normal and exception paths, avoids unnecessary sections/accounts, and maps each screen to a user goal and requirement.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0329 — Design Google sign-in, account/session, minimal intake and dashboard-entry interactions
- **Dependencies:** TSK-0328
- **Acceptance_Criteria:** Prototype covers Google sign-in, first-session account creation, signed-in return, errors/provider outage, logout, session expiry, account deletion entry, intake field states, back/resume and data-use explanation with minimal identity collection.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0330 — Design Phone → Internet → Services setup flows
- **Dependencies:** TSK-0146
- **Acceptance_Criteria:** Each flow has prerequisites, step-by-step actions, verification/confirmation, skip conditions, unsupported/conflict states, troubleshooting, and no misleading completion state.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0332 — Design lightweight parent dashboard and device-management interactions
- **Dependencies:** TSK-0329; TSK-0142
- **Acceptance_Criteria:** Prototype includes polished mobile-first empty/device states, add/setup/status/Protection Map, curated controls and contextual help; normal and error states are understandable without AdGuard/DNS administration terminology and expose no activity history.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0333 — Assemble end-to-end responsive interactive prototype
- **Dependencies:** TSK-0335; TSK-0334; TSK-0146
- **Acceptance_Criteria:** Prototype includes all critical normal/exception paths, representative iOS/Android content, responsive states, accessibility annotations, and analytics/test markers.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0334 — Design support, false-positive, removal, and reconfiguration flows
- **Dependencies:** TSK-0330
- **Acceptance_Criteria:** Each major support category has an accessible path, minimal diagnostic request, clear protection consequence, escalation option, and success state.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0335 — Design Protection Map and coverage-limit interactions
- **Dependencies:** TSK-0330
- **Acceptance_Criteria:** Prototype never labels parent confirmation as verification, exposes material gaps at the right time, and supports the comprehension test defined by product metrics.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** HUMAN_ONLY

### TSK-0336 — Run focused prototype usability and comprehension testing
- **Dependencies:** TSK-0333
- **Acceptance_Criteria:** Testing covers accountless entry/routing, setup/Protection Map comprehension, native and relevant external-service steps, DNS configuration/verification, recovery/removal and core exception paths; critical tasks and comprehension are measured without requiring a UseSafeWeb account or processing real child DNS in prototype testing.
- **Verification_Method:** Use the approved checklist/test procedure against the exact artifact/environment; retain reproducible outputs and reviewer result.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0538 — Define reliability, observability, recovery, and service-level NFRs
- **Dependencies:** TSK-0484
- **Acceptance_Criteria:** Specification defines critical user journeys, provisional SLI/SLO targets, alert conditions, recovery objectives, backup scope, restore test, maintenance behavior, and escalation ownership.
- **Verification_Method:** Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0558 — Freeze the USD 20-50/month discretionary budget, earned-distribution priority, and one-primary/one-challenger rule
- **Dependencies:** 
- **Acceptance_Criteria:** GTM plan cannot require paid acquisition or simultaneous platform programs; spend caps/accumulation/approval and channel stop rules are explicit.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

### TSK-0559 — Define the research, originality, usefulness, source, claims, update, localization, and pruning standard for first-phone content
- **Dependencies:** TSK-0558
- **Acceptance_Criteria:** Mass low-quality AI SEO is prohibited; every item solves a real high-intent job and connects to product/help with source/review/owner/metric.
- **Verification_Method:** Review against approved brief, user evidence, claims, accessibility, source currency, and surface acceptance; test with representative tasks where applicable.
- **Action_Authority:** AUTO_ALLOWED

## Cross-authority references requiring CR-0003 review

### Governance/CURRENT_STATE_INTERFACE.md
- L15: | Integrated product definition/build | WAITING | Requires positive LG-05, then LG-06/LG-07. |

### Governance/SOURCE_PLAN_FREEZE_AUDIT.md
- L101: | Overbuilding before validation | PASS | LG-05 precedes full product definition/build; L3 and L8 remain different. |

### Layers/LAYER_1_PROGRAM_ARCHITECTURE_STRATEGIC_BASELINE.md
- L59: | Initial behavioral validation | England |
- L157: | L3 | Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | LG-05 |
- L158: | L4 | Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system. | LG-06 |

### Layers/LAYER_4_INTEGRATED_PROGRAM_CRITICAL_PATH.md
- L10: | 3 | L3 - Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | LG-05 |
- L11: | 4 | L4 - Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system. | LG-06 |
- L26: - LG-04 authorizes concierge recruitment only after LG-03 and the synthetic operating rehearsal. L3 tests behavior before integrated software build.
- L27: - Positive LG-05 evidence unlocks product/brand/service/UX definition. The implementation-ready prototype, product requirements, and truth/self-service models constrain architecture and build.
- L44: Behavioral validation -> accountless minimum product/non-goals -> service blueprint/friction budget/truth state -> full brand system and implementation-ready prototype -> usability/comprehension/accessibility evidence -> architecture -> accountless public/setup build plus real DNS -> integrated acceptance/self-service/recovery -> controlled pilot -> product correction and primary-channel selection -> production readiness -> staged launch -> persistence/support/root-cause improvement -> Year-1 decision.

### RELATIONSHIP_INDEX.yaml
- L15061: LG-05:
- L15155: - target: LG-05
- L15163: - target: LG-05
- L15171: - target: LG-05
- L17141: - target: LG-05
- L17165: - target: LG-05
- L17261: - target: LG-05
- L17405: - target: LG-05

### Registers/CONSTRAINTS.md
- L30: | CON-0025 | Behavioral validation precedes expensive integrated product build. | L3 and L8 remain distinct experiments. | TSK-0099; TSK-0164; TSK-0165; TSK-0166; TSK-0167; TSK-0168; TSK-0169; TSK-0170; TSK-0171; TSK-0172; TSK-0173; TSK-0174; TSK-0175; TSK-0176; TSK-0177; TSK-0178; TSK-0179; TSK-0180; TSK-0181; TSK-0182; TSK-0183; TSK-0184; TSK-0185; TSK-0186; TSK-0187; TSK-0188; TSK-0189; TSK-0190; TSK-0191; TSK-0192; TSK-0193; TSK-0194; TSK-0195; TSK-0196; TSK-0197 |

### Registers/DECISIONS_TRIGGERS.md
- L7: | DEC-0002 | D-002 | Customer-facing product | FROZEN for validation — UseSafeWeb — First Phone Safety Setup, a lightweight orchestration service, not DNS software/surveillance. | Business evaluation close | Behavioral validation may modify execution details but not silently restore the broad family-DNS proposition. | Project Owner | USW-01.05.03.001; USW-04.01 | CURRENT_STATE.md; BUSINESS_PHASES_23_42.md |

### Registers/DELIVERABLES.md
- L109: | DEL-0104 | PHS-0041 | PKG-03 | L2 | Concierge behavioral validation protocol | PASS | All child work packages and tasks satisfy their acceptance criteria with current evidence or explicit deferred/not-applicable disposition. |

### Registers/GATES.md
- L8: | LG-02 | Business and Product Evaluation Decision | L1 | Decide whether and how to proceed to behavioral validation. | Phases 1-42 analyses complete. | Evaluation evidence, risks, scorecard, MODIFY/GO/PIVOT/NO-GO rationale, validation path. | PASS; MODIFY; PIVOT; STOP | Project Owner | G-01 | Unlocks validation-readiness work only. |
- L11: | LG-05 | Behavioral Validation Outcome | L3 exit | Decide whether the orchestration proposition merits integrated product definition/build. | Wave A, controlled refinement, Wave B, 14-day evidence complete. | Activation, incremental safeguard, assistance, abandonment, comprehension, persistence, incidents, privacy deletion, contrary evidence. | PASS/PROCEED; REPEAT; MODIFY; PIVOT; PAUSE; STOP | Project Owner | G-04 | Unlocks L4 product/experience definition only on positive/qualified outcome. |
- L12: | LG-06 | Product, Brand and Experience Freeze | L4 | Freeze the accountless minimum product, requirements, service journey, brand/design system, prototype, content, accessibility and i18n baseline. | LG-05 permits continued product work. | Product/non-goals; traceability; validated prototype; usability/comprehension; brand; design system; self-service; content sources; accountless/privacy model. | PASS; REWORK; REDUCE; REPEAT VALIDATION; STOP | Project Owner | G-05 | Unlocks final architecture/delivery readiness. |

### Registers/LEGACY_RECONCILIATION.md
- L115: | USW-02.07.01 | Deliverable | Concierge behavioral validation protocol | Stage 2 — Validation Readiness & Pre-Experiment Controls | Completed | PKG-03 | L2 | PHS-0041 | 1 | PRESERVED/RESTRUCTURED |
- L119: | USW-03 | Lifecycle Stage | Stage 3 — Experiment 1 Concierge Behavioral Validation | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01; PKG-03; PKG-06; PKG-11 | L3 | PHS-0007; PHS-0008; PHS-0009; PHS-0010; PHS-0042; PHS-0043; PHS-0044; PHS-0045; PHS-0079; PHS-0144 | 31 | RESTRUCTURED |
- L120: | USW-03.01 | Phase | Experiment Launch, Recruitment & Cohort Qualification | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01; PKG-03 | L3 | PHS-0009; PHS-0043 | 5 | RESTRUCTURED |
- L121: | USW-03.01.01 | Deliverable | G-03 experiment launch authorisation | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01; PKG-03 | L3 | PHS-0009; PHS-0043 | 2 | RESTRUCTURED |
- L122: | USW-03.01.02 | Deliverable | Qualified 20–30 participant cohort | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-03 | L3 | PHS-0043 | 3 | RESTRUCTURED |
- L123: | USW-03.02 | Phase | Wave A — First 10 Qualified Participants | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-03 | L3 | PHS-0044 | 6 | RESTRUCTURED |
- L124: | USW-03.02.01 | Deliverable | Completed Wave A sessions and records | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-03 | L3 | PHS-0044 | 6 | RESTRUCTURED |
- L125: | USW-03.03 | Phase | Controlled Iteration After Wave A | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01; PKG-03; PKG-06; PKG-11 | L3 | PHS-0007; PHS-0042; PHS-0079; PHS-0144 | 6 | RESTRUCTURED |
- L126: | USW-03.03.01 | Deliverable | Wave A friction and root-cause analysis | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01; PKG-03; PKG-11 | L3 | PHS-0007; PHS-0042; PHS-0144 | 3 | RESTRUCTURED |
- L127: | USW-03.03.02 | Deliverable | One materially improved concierge journey | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-03; PKG-06 | L3 | PHS-0042; PHS-0079 | 3 | RESTRUCTURED |
- L128: | USW-03.04 | Phase | Wave B — Remaining 10–20 Qualified Participants | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-03 | L3 | PHS-0045 | 4 | RESTRUCTURED |
- L129: | USW-03.04.01 | Deliverable | Completed Wave B sessions and records | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-03 | L3 | PHS-0045 | 4 | RESTRUCTURED |
- L130: | USW-03.05 | Phase | Experiment Close, Analysis, Retention & Evidence Package | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01 | L3 | PHS-0008 | 7 | RESTRUCTURED |
- L131: | USW-03.05.01 | Deliverable | Experiment-1 aggregate results report | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01 | L3 | PHS-0008 | 5 | RESTRUCTURED |
- L132: | USW-03.05.02 | Deliverable | Experiment-1 deletion and archive evidence | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01 | L3 | PHS-0008 | 2 | RESTRUCTURED |
- L133: | USW-03.06 | Phase | G-04 Experiment Conclusion & Product-Build Decision | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01 | L3 | PHS-0010 | 3 | RESTRUCTURED |
- L134: | USW-03.06.01 | Deliverable | Experiment-1 pass/modify/pivot/stop decision | Stage 3 — Experiment 1 Concierge Behavioral Validation | Planned | PKG-01 | L3 | PHS-0010 | 3 | RESTRUCTURED |

### Registers/LIFECYCLE_OBLIGATIONS.md
- L9: | L3 | Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | 31 | LG-05 |
- L10: | L4 | Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system. | 68 | LG-06 |
- L51: | MX-01-03 | PKG-01 | L3 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L65: | MX-02-03 | PKG-02 | L3 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L79: | MX-03-03 | PKG-03 | L3 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L93: | MX-04-03 | PKG-04 | L3 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L121: | MX-06-03 | PKG-06 | L3 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L149: | MX-08-03 | PKG-08 | L3 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L163: | MX-09-03 | PKG-09 | L3 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L177: | MX-10-03 | PKG-10 | L3 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L191: | MX-11-03 | PKG-11 | L3 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L205: | MX-12-03 | PKG-12 | L3 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L219: | MX-13-03 | PKG-13 | L3 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L233: | MX-14-03 | PKG-14 | L3 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
- L261: | MX-16-03 | PKG-16 | L3 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |

### Registers/MILESTONES.md
- L12: | MS-0007 | Wave A complete | L3 | First 10 qualified sessions and follow-ups complete. | LG-05 |
- L13: | MS-0008 | Wave B complete | L3 | Controlled refinement and remaining cohort complete. | LG-05 |
- L14: | MS-0009 | Behavioral proposition decision complete | L3 | Proceed/repeat/pivot/stop decision recorded. | LG-05 |

### Registers/OBJECTIVES.md
- L7: | OBJ-0002 | Minimize user friction and technical burden. | PKG-06 | REQ-0028; REQ-0029; REQ-0030; CON-0010; CON-0017 | TSK-0306; TSK-0307; TSK-0308 | Every interaction is justified and critical paths approach one-to-three meaningful actions where technically possible. | LG-05 |
- L8: | OBJ-0003 | Represent protection truthfully. | PKG-06 | REQ-0028; REQ-0029; REQ-0030; CON-0010; CON-0017 | TSK-0306; TSK-0307; TSK-0308 | Protection Map always distinguishes verified, parent-confirmed, action needed, and not covered. | LG-05 |
- L12: | OBJ-0007 | Make UX/UI a core product capability. | PKG-06 | REQ-0028; REQ-0029; REQ-0030; CON-0010; CON-0017 | TSK-0306; TSK-0307; TSK-0308 | Major experience decisions are designed and tested before implementation and critical journeys pass usability/accessibility checks. | LG-05 |
- L18: | OBJ-0013 | Avoid future internationalization rebuild. | PKG-06 | REQ-0028; REQ-0029; REQ-0030; CON-0010; CON-0017 | TSK-0306; TSK-0307; TSK-0308 | Architecture, content, design, and tests support English, Turkish, Arabic, RTL, and locale metadata before localization is activated. | LG-05 |

### Registers/PHASES.md
- L12: | PHS-0007 | PKG-01 | L3 | L3 - Controlled Iteration After Wave A | Deliver the Program Governance & Knowledge Management obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L13: | PHS-0008 | PKG-01 | L3 | L3 - Experiment Close, Analysis, Retention & Evidence Package | Deliver the Program Governance & Knowledge Management obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L14: | PHS-0009 | PKG-01 | L3 | L3 - Experiment Launch, Recruitment & Cohort Qualification | Deliver the Program Governance & Knowledge Management obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L15: | PHS-0010 | PKG-01 | L3 | L3 - G-04 Experiment Conclusion & Product-Build Decision | Deliver the Program Governance & Knowledge Management obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L47: | PHS-0042 | PKG-03 | L3 | L3 - Controlled Iteration After Wave A | Deliver the Research, Validation & Experimentation obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L48: | PHS-0043 | PKG-03 | L3 | L3 - Experiment Launch, Recruitment & Cohort Qualification | Deliver the Research, Validation & Experimentation obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L49: | PHS-0044 | PKG-03 | L3 | L3 - Wave A — First 10 Qualified Participants | Deliver the Research, Validation & Experimentation obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L50: | PHS-0045 | PKG-03 | L3 | L3 - Wave B — Remaining 10–20 Qualified Participants | Deliver the Research, Validation & Experimentation obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L84: | PHS-0079 | PKG-06 | L3 | L3 - Controlled Iteration After Wave A | Deliver the UX, Service Design, Content & Accessibility obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |
- L149: | PHS-0144 | PKG-11 | L3 | L3 - Controlled Iteration After Wave A | Deliver the Data, Analytics & Measurement obligations for Concierge Behavioral Validation. | WAITING | All mandatory child deliverables/tasks meet acceptance with evidence; deferred/conditional work is explicitly dispositioned. |

### Registers/REQUIREMENTS.md
- L30: | REQ-0025 | MUST | PKG-05 | Full brand polish shall follow sufficient proposition evidence rather than precede behavioral validation. | TSK-0297; TSK-0298; TSK-0299; TSK-0300; TSK-0301; TSK-0302; TSK-0303; TSK-0304; TSK-0305 | Lifecycle/dependency audit. | Owner decision 2026-08-27 |

## Exact relationship-index blocks for affected L4 tasks

### TSK-0139
```yaml
  TSK-0139:
    relationships:
    - target: WP-0134
      type: parent_work_package
    - target: PKG-02
      type: belongs_to_package
    - target: PHS-0032
      type: belongs_to_phase
    - target: DEL-0088
      type: belongs_to_deliverable
    - target: L4
      type: belongs_to_lifecycle
    - target: TSK-0040
      type: depends_on
    - target: ACC-0139
      type: acceptance
    - target: VER-0139
      type: verified_by
    - target: EVD-0139
      type: evidence_required
    - target: RSK-0002
      type: affected_by_risk
    - target: INT-0003
      type: uses_interface
    - target: INT-0004
      type: uses_interface
    - target: REQ-0007
      type: governed_by
    - target: REQ-0008
      type: governed_by
    - target: CON-0001
      type: governed_by
    - target: CON-0002
      type: governed_by
    - target: USW-04.01.01.001
      type: migrated_from
    source: WBS/master-wbs.csv
    type: task
```

### TSK-0326
```yaml
  TSK-0326:
    relationships:
    - target: WP-0314
      type: parent_work_package
    - target: PKG-06
      type: belongs_to_package
    - target: PHS-0086
      type: belongs_to_phase
    - target: DEL-0183
      type: belongs_to_deliverable
    - target: L4
      type: belongs_to_lifecycle
    - target: TSK-0034
      type: depends_on
    - target: TSK-0043
      type: depends_on
    - target: ACC-0326
      type: acceptance
    - target: VER-0326
      type: verified_by
    - target: EVD-0326
      type: evidence_required
    - target: RSK-0002
      type: affected_by_risk
    - target: INT-0009
      type: uses_interface
    - target: INT-0010
      type: uses_interface
    - target: REQ-0028
      type: governed_by
    - target: REQ-0029
      type: governed_by
    - target: CON-0010
      type: governed_by
    - target: CON-0017
      type: governed_by
    - target: USW-04.03.01.001
      type: migrated_from
    source: WBS/master-wbs.csv
    type: task
```

