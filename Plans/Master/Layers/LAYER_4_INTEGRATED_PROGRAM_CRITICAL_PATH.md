# Layer 4 - Integrated Program & Critical-Path Plan

## 4.1 Integrated lifecycle and gate sequence

| Order | Lifecycle | Primary program outcome | Exit/decision gate |
| --- | --- | --- | --- |
| 0 | L0 - Original Inception & Technical Feasibility | Establish the problem, trust boundary, project identity, and technical feasibility without committing to full build. | LG-01 |
| 1 | L1 - Business & Product Evaluation | Complete evidence-based opportunity, product, market, operating, risk, and business-model evaluation. | LG-02 |
| 2 | L2 - Validation Readiness & Mandatory Controls | Make the bounded behavioral experiment legally, technically, operationally, and evidentially safe to run. | LG-03 |
| 3 | L3 - Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | LG-05 |
| 4 | L4 - Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system; DEC-0050 temporarily permits provisional internal definition/design from technical/synthetic evidence while L3 remains deferred. | LG-06 |
| 5 | L5 - Architecture, Security, Privacy & Delivery Readiness | Approve production-capable architecture, controls, delivery plan, cost envelope, and implementation evidence model. | LG-07 |
| 6 | L6 - Build & Integration | Implement the smallest validated integrated product, website, DNS service, automation, and supporting systems. | LG-08 |
| 7 | L7 - Integrated Verification & Release Readiness | Prove the integrated release meets functional, UX, accessibility, security, privacy, reliability, recovery, and operational acceptance. | LG-09 |
| 8 | L8 - Controlled Integrated-Product Pilot | Operate the real integrated product with a bounded cohort and collect minimum evidence on value, persistence, reliability, supportability, and funding. | LG-10 |
| 9 | L9 - Pilot Evaluation & Production Decision | Synthesize pilot evidence and decide proceed, repeat, reduce, pivot, pause, or stop. | LG-11 |
| 10 | L10 - Production Launch Readiness | Prepare the approved UK production baseline, policies, operations, website, acquisition engine, budget, and staged rollout. | LG-12 |
| 11 | L11 - Production Launch & Stabilization | Launch in controlled stages, verify guardrails, correct high-value defects, and establish a stable operating baseline. | LG-14 |
| 12 | L12 - Year-1 Operations, Improvement & Responsible Growth | Operate, maintain, improve, automate, measure, and grow responsibly through the first full operating year. | LG-15 |
| 13 | L13 - Year-1 Close & Year-2 Decision | Close Year 1 with reconciled evidence and decide continue, adjust, expand, formalize, transfer, pause, or stop. | LG-15 |

## 4.2 Integrated dependency strategy

- Current planning freeze is a hard program predecessor: owner freeze -> authorized GitHub publication -> fetch/read-back -> CURRENT_STATE rebaseline. Derived trackers follow later and cannot block canonical execution.
- After the governance hold is released, LG-03 closes through parallel legal/privacy and technical deployment branches. Final notices/LIA-DPIA/gate evidence consume verified deployed reality.
- LG-04 authorizes concierge recruitment only after LG-03 and the synthetic operating rehearsal. L3 tests behavior before integrated software build.
- Positive LG-05 evidence normally unlocks product/brand/service/UX definition. Through 2027-08-27, DEC-0050/CR-0003 instead permits bounded provisional internal L4 definition/design from current technical/synthetic evidence while LG-05 remains DEFER; missing real-participant evidence is explicit RSK-0002, cannot be fabricated, and any real-evidence-dependent L4 task remains deferred. The override does not authorize LG-06 PASS, L5/L6 progression, integrated build, or launch.
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

Behavioral validation (currently DEFER under DEC-0050) -> provisional accountless minimum product/non-goals from technical/synthetic evidence -> service blueprint/friction budget/truth state -> brand/prototype work that does not require real-user evidence -> deferred usability/comprehension evidence where real users are required -> LG-06 decision -> architecture -> accountless public/setup build plus real DNS -> integrated acceptance/self-service/recovery -> controlled pilot -> product correction and primary-channel selection -> production readiness -> staged launch -> persistence/support/root-cause improvement -> Year-1 decision. No arrow after the provisional L4 segment implies that missing behavioral evidence was satisfied.

## 4.5 Technical critical path

LG-03 Azure/AdGuard/DNS/TLS/privacy acceptance -> DNS endpoint/platform mechanism contract -> accountless app and DNS integration architecture -> versioned DNS recovery bundle -> production-grade Ubuntu 24.04 Bash recovery script -> security/idempotency/failure-injection/clean-server acceptance -> integrated release -> controlled pilot -> production deployment/runbooks -> Year-1 maintenance and recovery rehearsals.

## 4.6 Legal/safety gate path

OWNER LEGAL HOLD (2026-08-27 to 2027-08-27 unless reactivated earlier): UK representative/Article-27, ICO, DPIA/LIA/legal-notice/terms/tax-regulatory work is DEFERRED/WAITING while eligible technical privacy/security/infrastructure readiness continues. Real-participant Experiment 1 authorization still requires LG-03 PASS, so unresolved mandatory legal evidence remains a gate blocker rather than being treated as complete. DEC-0050/CR-0003 separately defers the complete real-participant L3 branch to the same date and permits only provisional internal L4 definition/design; it does not satisfy any legal condition or participant gate. After reactivation/resolution: Experiment 1 authorization -> behavioral evidence -> reconciliation of provisional L4 assumptions -> architecture/privacy/security readiness -> integrated acceptance -> later pilot/production gates.

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
