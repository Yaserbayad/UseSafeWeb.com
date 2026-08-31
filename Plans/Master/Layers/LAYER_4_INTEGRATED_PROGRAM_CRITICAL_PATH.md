# Layer 4 - Integrated Program & Critical-Path Plan

## 4.1 Integrated lifecycle and gate sequence

| Order | Lifecycle | Primary program outcome | Exit/decision gate |
| --- | --- | --- | --- |
| 0 | L0 - Original Inception & Technical Feasibility | Establish the problem, trust boundary, project identity, and technical feasibility without committing to full build. | LG-01 |
| 1 | L1 - Business & Product Evaluation | Complete evidence-based opportunity, product, market, operating, risk, and business-model evaluation. | LG-02 |
| 2 | L2 - Validation Readiness & Mandatory Controls | Maintain independently required technical/privacy/security/readiness controls; pre-product participant validation is not an active progression prerequisite under DEC-0052. | LG-03 (inactive active-path gate) |
| 3 | L3 - Concierge Behavioral Validation | Historical pre-product participant-validation stage; NOT_APPLICABLE to the active integrated-product-first path under DEC-0052/CR-0005. | LG-05 (inactive active-path gate) |
| 4 | L4 - Product Definition, Requirements & Experience Design | Define and freeze the owner-approved product, service journey, brand, UX and content baseline from current owner/product/technical/synthetic/internal evidence; real-user validation is intentionally deferred until L8. | LG-06 |
| 5 | L5 - Architecture, Security, Privacy & Delivery Readiness | Approve production-capable architecture, controls, delivery plan, cost envelope, and implementation evidence model. | LG-07 |
| 6 | L6 - Build & Integration | Implement the smallest approved integrated product, website, DNS service, automation and supporting systems after LG-06/LG-07 without a pre-product human-testing prerequisite. | LG-08 |
| 7 | L7 - Integrated Verification & Release Readiness | Prove the integrated release meets functional, UX, accessibility, security, privacy, reliability, recovery, and operational acceptance. | LG-09 |
| 8 | L8 - Initial Live Production Validation & Observation | First active parent/user/participant validation stage: operate the fully integrated LG-09-approved product with a bounded cohort and collect value, comprehension, persistence, reliability, supportability and funding evidence. | LG-10 |
| 9 | L9 - Initial Production Evidence & Continuation Decision | Synthesize initial production evidence and decide proceed, repeat, reduce, pivot, pause, or stop. | LG-11 |
| 10 | L10 - Production Launch Readiness | Prepare the approved UK production baseline, policies, operations, website, acquisition engine, budget, and staged rollout. | LG-12 |
| 11 | L11 - Production Launch & Stabilization | Launch in controlled stages, verify guardrails, correct high-value defects, and establish a stable operating baseline. | LG-14 |
| 12 | L12 - Year-1 Operations, Improvement & Responsible Growth | Operate, maintain, improve, automate, measure, and grow responsibly through the first full operating year. | LG-15 |
| 13 | L13 - Year-1 Close & Year-2 Decision | Close Year 1 with reconciled evidence and decide continue, adjust, expand, formalize, transfer, pause, or stop. | LG-15 |

## 4.2 Integrated dependency strategy

- Current planning freeze is a hard program predecessor: owner freeze -> authorized GitHub publication -> fetch/read-back -> CURRENT_STATE rebaseline. Derived trackers follow later and cannot block canonical execution.
- After the governance hold is released, LG-03 closes through parallel legal/privacy and technical deployment branches. Final notices/LIA-DPIA/gate evidence consume verified deployed reality.
- DEC-0052/CR-0005 retires LG-03/LG-04/LG-05 and the 31-task L3 Experiment-1 branch from the active pre-product path. Those tasks/gates remain traceable historical/exclusion records and do not provide behavioral evidence.
- L4 product/brand/service/UX definition may proceed from current owner/product/technical/synthetic/internal evidence. LG-06 and LG-07 still require exact applicable product, accessibility, architecture, security/privacy and delivery evidence; their PASS may unlock L6 build without real-user evidence. L7 then independently proves the integrated product and LG-09 must PASS before the first L8 human/user validation.
- L5 resolves application/DNS/platform/security/privacy/data/test/recovery/cost contracts. L6 implements in bounded vertical slices. L7 independently proves the exact integrated release and Ubuntu recovery path.
- L8 operates one controlled integrated pilot. L9 evaluates the evidence and selects production action. No launch work substitutes for a failed product-value decision.
- L10 production readiness may parallelize platform, legal/security, operations, brand/web, finance and the selected GTM engine, but LG-12 requires all applicable branches.
- L11 stages launch and stabilization. L12 operates/improves one primary value path, one primary acquisition engine plus optional challenger, progressive localization, and evidence-triggered scaling. L13 reconciles the year and decides Year 2.
- Recurring activities are operating inputs and do not become false finish-to-start predecessors that can never complete.

## 4.3 Current/next critical execution network

The **authoritative task-level critical network is the WBS**, not a duplicated Markdown table. Use [WBS/master-wbs.csv](../WBS/master-wbs.csv) with `Critical_Path=YES`, then traverse `Dependencies` / `RELATIONSHIP_INDEX.yaml` and resolve the governing gate through [GATES.md](../Registers/GATES.md). Runtime eligibility/status must additionally be reconciled with canonical `CURRENT_STATE.md` after publication.

At this pre-freeze candidate point, the only owner action exposed as `TODO` is `TSK-0017` (owner freeze/rework decision). After owner freeze, the already-defined sequence is `TSK-0009` (publish complete approved `Plans/` tree) -> `TSK-0011` (file-for-file/checksum read-back) -> `TSK-0010` (rebaseline canonical current state). Only then may ordinary LG-03 validation-readiness work resume according to its existing WBS dependencies.

This section intentionally does **not** repeat task titles, acceptance criteria, execution states, or dependency lists. Those facts have one authoritative owner in the WBS/current-state control plane, preventing cross-file drift.

## 4.4 Customer-value critical path

Owner-authorized product definition from current evidence -> service blueprint/friction budget/truth state -> brand/prototype -> internal/automated accessibility, browser/device and truth-state acceptance -> LG-06 decision -> architecture/security/privacy/delivery readiness -> LG-07 -> accountless-core plus optional parent-account/dashboard build and real DNS -> LG-08 -> integrated L7 acceptance/self-service/recovery -> LG-09 -> first real-user controlled pilot in L8 -> product correction and production decision -> production readiness -> staged launch -> persistence/support/root-cause improvement -> Year-1 decision. Pre-L8 work must never be labelled user/behaviorally validated.

## 4.5 Technical critical path

Current technical/privacy/security readiness -> DNS endpoint/platform mechanism contract -> dual-mode accountless-core plus optional-account/session/dashboard and DNS integration architecture -> versioned DNS recovery bundle -> production-grade Ubuntu 24.04 recovery path -> security/idempotency/failure-injection/clean-server acceptance -> LG-06/LG-07 -> integrated build -> L7 integrated release verification -> LG-09 -> first L8 real-user pilot -> production deployment/runbooks -> Year-1 maintenance and recovery rehearsals.

## 4.6 Legal/safety gate path

OWNER LEGAL HOLD (2026-08-27 to 2027-08-27 unless reactivated earlier) remains independently controlling for applicable legal/regulatory/compliance acts; DEC-0052 does not waive or satisfy legal evidence. The retired pre-product L3 experiment no longer gates L4-L7. Applicable legal/privacy/vendor/participant-readiness evidence for the first actual human/user pilot must be current before LG-09 can authorize L8 participant activation; public launch remains governed by later production gates.

## 4.7 Parallel work rules

| Can proceed in parallel | Cannot be substituted or bypassed |
| --- | --- |
| LG-03 legal/ICO route and Azure/AdGuard deployment | Neither branch substitutes for the other; final notice/DPIA consumes both. |
| L4 brand strategy, service blueprint, content source registry and i18n design after product baseline | Final UI implementation cannot precede validated experience baseline. |
| L5 application, DNS, platform, security, privacy, measurement, test and delivery designs | Build cannot begin until the integrated contracts/gate pass. |
| L6 public site, setup app, DNS service, infrastructure/recovery and self-service components in small integrated slices | No package may invent conflicting state/data/interface semantics. |
| L10 platform, legal/security, operations, brand/web, finance and selected GTM readiness | LG-12 requires all applicable evidence; launch date pressure cannot waive controls. |
| L12 product improvement, reliability/security/privacy maintenance, self-service, primary growth engine, finance/vendor and progressive localization readiness | Do not activate unsupported locales/channels/features merely because readiness work exists. |

## 4.8 Governance gates

The complete gate definitions from source Section 4.8 were normalized to the authoritative [Gate Register](../Registers/GATES.md). This Layer 4 section governs sequence/use of gates but does not redefine gate records.

## 4.9 Milestones

The complete milestone definitions from source Section 4.9 were normalized to the authoritative [Milestone Register](../Registers/MILESTONES.md). This Layer 4 section uses those IDs without maintaining a second definition.

## 4.10 Year-1 operating sequence

| Period | Primary focus | Mandatory cross-package outcomes |
| --- | --- | --- |
| Launch + stabilization | Controlled rollout and rapid correction | Exact release/config; monitoring/runbooks; truthful states; self-service; incidents; cost/cap; channel source; LG-14. |
| M1-M3 | Reliability, friction and persistence baseline | DNS/web health; false positives; setup/recovery; support automation; privacy/security checks; first content/channel evidence; budget actuals. |
| M4-M6 | Focused product improvement and acquisition commitment | Highest-value root causes; one primary engine plus challenger; supporter experiment only if authorized; recovery rehearsal; vendor/content/platform updates. |
| M7-M9 | Responsible growth and conditional locale readiness | Capacity/cost/support guardrails; primary engine replication; Turkish/Arabic/RTL readiness tests; LG-16 only for a named justified market. |
| M10-M12 | Consolidation and annual evidence close | Reliability/security/privacy/rights/vendor/finance/channel/product/brand/content/AI governance reconciliation; Year-2 options. |
| Year-1 close | Owner decision | Continue, modify, expand, formalize, transfer, pause or stop through LG-15. |

## 4.11 Pause, repeat, pivot and stop routes

Any gate may return REWORK/REPEAT/REVALIDATE/PIVOT/PAUSE/STOP as applicable. LG-18 is available at every stage. Stop/decommission is a valid terminal transition with user/service/data/payment/vendor/domain/access/legal/communications/asset/evidence obligations; it is not a normal next lifecycle stage.
### CR-0007 active production-only continuation path

From `LG-09` onward, the active path is **live production**, not a separate pilot or staging lifecycle: integrated production release readiness -> bounded/ramped live production activation -> initial production evidence -> automatic CONTINUE when frozen thresholds pass -> UK public production readiness -> automatic public-production GO -> objective stabilization -> Year-1 operations. Pre-release verification, security/privacy/accessibility/performance tests, clean-server recovery and rollback remain mandatory. Named-market expansion, organizational formalization, contracts/legal identity acts, material unbudgeted commitments and strategic pivot/pause/stop/transfer/resume retain the human boundaries in DEC-0054. Historical pilot/staging language is traceability only and does not control active sequencing.
