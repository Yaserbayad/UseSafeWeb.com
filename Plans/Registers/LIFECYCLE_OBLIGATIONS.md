# Lifecycle and package x lifecycle obligation registers


| Lifecycle | Name | Purpose | Tasks | Exit gate |
| --- | --- | --- | --- | --- |
| L0 | Original Inception & Technical Feasibility | Establish the problem, trust boundary, project identity, and technical feasibility without committing to full build. | 13 | LG-01 |
| L1 | Business & Product Evaluation | Complete evidence-based opportunity, product, market, operating, risk, and business-model evaluation. | 43 | LG-02 |
| L2 | Validation Readiness & Mandatory Controls | Make the bounded behavioral experiment legally, technically, operationally, and evidentially safe to run. | 84 | LG-03 |
| L3 | Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | 31 | LG-05 |
| L4 | Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system. | 68 | LG-06 |
| L5 | Architecture, Security, Privacy & Delivery Readiness | Approve production-capable architecture, controls, delivery plan, cost envelope, and implementation evidence model. | 36 | LG-07 |
| L6 | Build & Integration | Implement the smallest validated integrated product, website, DNS service, automation, and supporting systems. | 76 | LG-08 |
| L7 | Integrated Verification & Release Readiness | Prove the integrated release meets functional, UX, accessibility, security, privacy, reliability, recovery, and operational acceptance. | 48 | LG-09 |
| L8 | Controlled Integrated-Product Pilot | Operate the real integrated product with a bounded cohort and collect minimum evidence on value, persistence, reliability, supportability, and funding. | 42 | LG-10 |
| L9 | Pilot Evaluation & Production Decision | Synthesize pilot evidence and decide proceed, repeat, reduce, pivot, pause, or stop. | 8 | LG-11 |
| L10 | Production Launch Readiness | Prepare the approved UK production baseline, policies, operations, website, acquisition engine, budget, and staged rollout. | 59 | LG-12 |
| L11 | Production Launch & Stabilization | Launch in controlled stages, verify guardrails, correct high-value defects, and establish a stable operating baseline. | 9 | LG-14 |
| L12 | Year-1 Operations, Improvement & Responsible Growth | Operate, maintain, improve, automate, measure, and grow responsibly through the first full operating year. | 108 | LG-15 |
| L13 | Year-1 Close & Year-2 Decision | Close Year 1 with reconciled evidence and decide continue, adjust, expand, formalize, transfer, pause, or stop. | 16 | LG-15 |

#### 6.5.1 16 x 14 matrix

| Package | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 | L11 | L12 | L13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PKG-01 | R | R | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-02 | R | R | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-03 | C | R | R | R | R | C | C | C | R | R | C | C | R | R |
| PKG-04 | C | R | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-05 | N | C | C | C | R | R | R | R | C | C | R | R | R | C |
| PKG-06 | C | R | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-07 | N | C | C | C | R | R | R | R | R | R | R | R | R | C |
| PKG-08 | R | C | R | R | R | R | R | R | R | R | R | R | R | C |
| PKG-09 | C | C | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-10 | C | C | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-11 | C | R | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-12 | C | C | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-13 | N | C | R | R | R | R | R | R | R | R | R | R | R | R |
| PKG-14 | N | C | C | R | C | C | C | C | R | R | R | R | R | R |
| PKG-15 | C | R | R | C | R | R | R | R | R | R | R | R | R | R |
| PKG-16 | N | C | C | R | R | R | R | R | R | R | R | R | R | R |

Legend: R = Required; C = Conditional with exact activation trigger below; N = Not Applicable with rationale below. A deliberate postponement uses EXC/DEFERRED_EXCEPTION, not N.

#### 6.5.2 All 224 cell dispositions

| Cell | Package | Lifecycle | Disposition | Exact trigger/rationale | Deferred exception |
| --- | --- | --- | --- | --- | --- |
| MX-01-00 | PKG-01 | L0 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L0 - Original Inception & Technical Feasibility or its gate. |  |
| MX-01-01 | PKG-01 | L1 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-01-02 | PKG-01 | L2 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-01-03 | PKG-01 | L3 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-01-04 | PKG-01 | L4 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-01-05 | PKG-01 | L5 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-01-06 | PKG-01 | L6 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-01-07 | PKG-01 | L7 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-01-08 | PKG-01 | L8 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-01-09 | PKG-01 | L9 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-01-10 | PKG-01 | L10 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-01-11 | PKG-01 | L11 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-01-12 | PKG-01 | L12 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-01-13 | PKG-01 | L13 | R | Required: Program Governance & Knowledge Management has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-02-00 | PKG-02 | L0 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L0 - Original Inception & Technical Feasibility or its gate. |  |
| MX-02-01 | PKG-02 | L1 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-02-02 | PKG-02 | L2 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-02-03 | PKG-02 | L3 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-02-04 | PKG-02 | L4 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-02-05 | PKG-02 | L5 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-02-06 | PKG-02 | L6 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-02-07 | PKG-02 | L7 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-02-08 | PKG-02 | L8 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-02-09 | PKG-02 | L9 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-02-10 | PKG-02 | L10 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-02-11 | PKG-02 | L11 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-02-12 | PKG-02 | L12 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-02-13 | PKG-02 | L13 | R | Required: Business Strategy & Product Management has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-03-00 | PKG-03 | L0 | C | Conditional trigger: A feasibility uncertainty requires direct user/stakeholder evidence before the technical concept can be accepted. |  |
| MX-03-01 | PKG-03 | L1 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-03-02 | PKG-03 | L2 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-03-03 | PKG-03 | L3 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-03-04 | PKG-03 | L4 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-03-05 | PKG-03 | L5 | C | Conditional trigger: A material architecture/security/privacy decision depends on user behavior or comprehension not resolved at L4. |  |
| MX-03-06 | PKG-03 | L6 | C | Conditional trigger: Implementation reveals a material user-behavior uncertainty that cannot be resolved by existing evidence or ordinary QA. |  |
| MX-03-07 | PKG-03 | L7 | C | Conditional trigger: A release-readiness criterion requires representative human usability/comprehension evidence beyond existing studies. |  |
| MX-03-08 | PKG-03 | L8 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-03-09 | PKG-03 | L9 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-03-10 | PKG-03 | L10 | C | Conditional trigger: Launch scope or communication contains a new material behavior/understanding assumption absent from pilot evidence. |  |
| MX-03-11 | PKG-03 | L11 | C | Conditional trigger: Stabilization data reveals a high-impact product uncertainty requiring a bounded study rather than immediate implementation. |  |
| MX-03-12 | PKG-03 | L12 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-03-13 | PKG-03 | L13 | R | Required: Research, Validation & Experimentation has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-04-00 | PKG-04 | L0 | C | Conditional trigger: Feasibility activity processes real personal data, enters a legal commitment, or makes public safety/privacy claims. |  |
| MX-04-01 | PKG-04 | L1 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-04-02 | PKG-04 | L2 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-04-03 | PKG-04 | L3 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-04-04 | PKG-04 | L4 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-04-05 | PKG-04 | L5 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-04-06 | PKG-04 | L6 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-04-07 | PKG-04 | L7 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-04-08 | PKG-04 | L8 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-04-09 | PKG-04 | L9 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-04-10 | PKG-04 | L10 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-04-11 | PKG-04 | L11 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-04-12 | PKG-04 | L12 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-04-13 | PKG-04 | L13 | R | Required: Legal, Privacy, Compliance & Safeguarding has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-05-00 | PKG-05 | L0 | N | Not applicable rationale: Original feasibility requires only the frozen name/trust boundary; executing a brand system would be premature and is owned later after evidence. |  |
| MX-05-01 | PKG-05 | L1 | C | Conditional trigger: Evaluation needs basic positioning/identity expression beyond the frozen name to test comprehension or differentiation. |  |
| MX-05-02 | PKG-05 | L2 | C | Conditional trigger: A participant-facing artifact needs minimum trusted visual/verbal consistency before Experiment 1. |  |
| MX-05-03 | PKG-05 | L3 | C | Conditional trigger: Concierge evidence specifically tests brand/trust comprehension or requires a controlled visual treatment. |  |
| MX-05-04 | PKG-05 | L4 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-05-05 | PKG-05 | L5 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-05-06 | PKG-05 | L6 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-05-07 | PKG-05 | L7 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-05-08 | PKG-05 | L8 | C | Conditional trigger: Pilot evidence requires brand/trust refinement or a material new pilot surface; otherwise use the L4 baseline. |  |
| MX-05-09 | PKG-05 | L9 | C | Conditional trigger: Pilot synthesis identifies a brand-positioning decision that must be resolved before production scope. |  |
| MX-05-10 | PKG-05 | L10 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-05-11 | PKG-05 | L11 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-05-12 | PKG-05 | L12 | R | Required: Brand System & Visual Identity has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-05-13 | PKG-05 | L13 | C | Conditional trigger: Year-1 evidence supports a material brand repositioning or new Year-2 market/locale system. |  |
| MX-06-00 | PKG-06 | L0 | C | Conditional trigger: A minimal user-facing feasibility journey or explanation is required to test the technical concept truthfully. |  |
| MX-06-01 | PKG-06 | L1 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-06-02 | PKG-06 | L2 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-06-03 | PKG-06 | L3 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-06-04 | PKG-06 | L4 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-06-05 | PKG-06 | L5 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-06-06 | PKG-06 | L6 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-06-07 | PKG-06 | L7 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-06-08 | PKG-06 | L8 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-06-09 | PKG-06 | L9 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-06-10 | PKG-06 | L10 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-06-11 | PKG-06 | L11 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-06-12 | PKG-06 | L12 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-06-13 | PKG-06 | L13 | R | Required: UX, Service Design, Content & Accessibility has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-07-00 | PKG-07 | L0 | N | Not applicable rationale: The original technical feasibility can be proven without a customer-facing application; disposable technical work remains under PKG-08/09. |  |
| MX-07-01 | PKG-07 | L1 | C | Conditional trigger: Evaluation requires a disposable prototype or technical spike; no production product implementation is authorized. |  |
| MX-07-02 | PKG-07 | L2 | C | Conditional trigger: Validation readiness needs a minimal experiment surface or automation not achievable safely by static/manual means. |  |
| MX-07-03 | PKG-07 | L3 | C | Conditional trigger: Concierge validation needs a bounded prototype/tool while preserving manual simulation and no full product build. |  |
| MX-07-04 | PKG-07 | L4 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-07-05 | PKG-07 | L5 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-07-06 | PKG-07 | L6 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-07-07 | PKG-07 | L7 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-07-08 | PKG-07 | L8 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-07-09 | PKG-07 | L9 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-07-10 | PKG-07 | L10 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-07-11 | PKG-07 | L11 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-07-12 | PKG-07 | L12 | R | Required: Web Experience & Application Engineering has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-07-13 | PKG-07 | L13 | C | Conditional trigger: Year-1 close requires a technical migration/export/closure artifact or an approved Year-2 implementation kickoff. |  |
| MX-08-00 | PKG-08 | L0 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L0 - Original Inception & Technical Feasibility or its gate. |  |
| MX-08-01 | PKG-08 | L1 | C | Conditional trigger: Business/product evaluation requires a specific DNS feasibility/cost/compatibility fact beyond the frozen baseline. |  |
| MX-08-02 | PKG-08 | L2 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-08-03 | PKG-08 | L3 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-08-04 | PKG-08 | L4 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-08-05 | PKG-08 | L5 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-08-06 | PKG-08 | L6 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-08-07 | PKG-08 | L7 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-08-08 | PKG-08 | L8 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-08-09 | PKG-08 | L9 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-08-10 | PKG-08 | L10 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-08-11 | PKG-08 | L11 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-08-12 | PKG-08 | L12 | R | Required: DNS / AdGuard Service Engineering has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-08-13 | PKG-08 | L13 | C | Conditional trigger: Year-1 close requires DNS migration, decommission, or Year-2 architecture action beyond normal L12 operations. |  |
| MX-09-00 | PKG-09 | L0 | C | Conditional trigger: A minimal host/cloud proof is needed to establish AdGuard/DoH feasibility; avoid production architecture. |  |
| MX-09-01 | PKG-09 | L1 | C | Conditional trigger: Evaluation requires a current hosting/cost/capacity fact not resolvable from verified existing evidence. |  |
| MX-09-02 | PKG-09 | L2 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-09-03 | PKG-09 | L3 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-09-04 | PKG-09 | L4 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-09-05 | PKG-09 | L5 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-09-06 | PKG-09 | L6 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-09-07 | PKG-09 | L7 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-09-08 | PKG-09 | L8 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-09-09 | PKG-09 | L9 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-09-10 | PKG-09 | L10 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-09-11 | PKG-09 | L11 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-09-12 | PKG-09 | L12 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-09-13 | PKG-09 | L13 | R | Required: Cloud Infrastructure & Platform Engineering has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-10-00 | PKG-10 | L0 | C | Conditional trigger: Feasibility exposes a public service, secret, or real data requiring a minimal threat/hardening control. |  |
| MX-10-01 | PKG-10 | L1 | C | Conditional trigger: Evaluation introduces a material security/abuse assumption requiring focused analysis. |  |
| MX-10-02 | PKG-10 | L2 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-10-03 | PKG-10 | L3 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-10-04 | PKG-10 | L4 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-10-05 | PKG-10 | L5 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-10-06 | PKG-10 | L6 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-10-07 | PKG-10 | L7 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-10-08 | PKG-10 | L8 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-10-09 | PKG-10 | L9 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-10-10 | PKG-10 | L10 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-10-11 | PKG-10 | L11 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-10-12 | PKG-10 | L12 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-10-13 | PKG-10 | L13 | R | Required: Security & Abuse Protection has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-11-00 | PKG-11 | L0 | C | Conditional trigger: Feasibility needs a defined measurement or evidence record beyond simple technical pass/fail. |  |
| MX-11-01 | PKG-11 | L1 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-11-02 | PKG-11 | L2 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-11-03 | PKG-11 | L3 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-11-04 | PKG-11 | L4 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-11-05 | PKG-11 | L5 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-11-06 | PKG-11 | L6 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-11-07 | PKG-11 | L7 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-11-08 | PKG-11 | L8 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-11-09 | PKG-11 | L9 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-11-10 | PKG-11 | L10 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-11-11 | PKG-11 | L11 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-11-12 | PKG-11 | L12 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-11-13 | PKG-11 | L13 | R | Required: Data, Analytics & Measurement has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-12-00 | PKG-12 | L0 | C | Conditional trigger: Feasibility evidence is consequential enough to require independent verification rather than a recorded owner observation. |  |
| MX-12-01 | PKG-12 | L1 | C | Conditional trigger: A business/product conclusion depends on a technical or data claim requiring independent validation. |  |
| MX-12-02 | PKG-12 | L2 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-12-03 | PKG-12 | L3 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-12-04 | PKG-12 | L4 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-12-05 | PKG-12 | L5 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-12-06 | PKG-12 | L6 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-12-07 | PKG-12 | L7 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-12-08 | PKG-12 | L8 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-12-09 | PKG-12 | L9 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-12-10 | PKG-12 | L10 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-12-11 | PKG-12 | L11 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-12-12 | PKG-12 | L12 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-12-13 | PKG-12 | L13 | R | Required: Quality Assurance, Verification & Release Readiness has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-13-00 | PKG-13 | L0 | N | Not applicable rationale: No live service operations exist during original concept feasibility; only bounded technical test cleanup is required under the producing package. |  |
| MX-13-01 | PKG-13 | L1 | C | Conditional trigger: Evaluation requires a current operations/reliability/support-burden feasibility finding beyond existing evidence. |  |
| MX-13-02 | PKG-13 | L2 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-13-03 | PKG-13 | L3 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-13-04 | PKG-13 | L4 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-13-05 | PKG-13 | L5 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-13-06 | PKG-13 | L6 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-13-07 | PKG-13 | L7 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-13-08 | PKG-13 | L8 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-13-09 | PKG-13 | L9 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-13-10 | PKG-13 | L10 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-13-11 | PKG-13 | L11 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-13-12 | PKG-13 | L12 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-13-13 | PKG-13 | L13 | R | Required: Service Operations, Reliability & Technical Support has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-14-00 | PKG-14 | L0 | N | Not applicable rationale: Acquisition, partnerships and public communications are not necessary to prove the original problem/technical feasibility. |  |
| MX-14-01 | PKG-14 | L1 | C | Conditional trigger: Evaluation needs current channel/market communication evidence; no acquisition program starts. |  |
| MX-14-02 | PKG-14 | L2 | C | Conditional trigger: Validation recruitment/material requires a bounded approved channel or communication before LG-04. |  |
| MX-14-03 | PKG-14 | L3 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-14-04 | PKG-14 | L4 | C | Conditional trigger: Product definition needs channel/content requirements or positioning evidence; no broad campaign execution. |  |
| MX-14-05 | PKG-14 | L5 | C | Conditional trigger: Architecture/delivery choices depend on a material channel integration, content platform, or communication requirement. |  |
| MX-14-06 | PKG-14 | L6 | C | Conditional trigger: Build needs only approved launch/content instrumentation or share mechanics; no multi-channel growth program. |  |
| MX-14-07 | PKG-14 | L7 | C | Conditional trigger: Release readiness requires claims/content/channel asset verification or a bounded pre-pilot recruitment artifact. |  |
| MX-14-08 | PKG-14 | L8 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-14-09 | PKG-14 | L9 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-14-10 | PKG-14 | L10 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-14-11 | PKG-14 | L11 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-14-12 | PKG-14 | L12 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-14-13 | PKG-14 | L13 | R | Required: Marketing, Communications, Partnerships & Distribution has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-15-00 | PKG-15 | L0 | C | Conditional trigger: Feasibility incurs a material purchase, contract, domain/hosting commitment, or cost decision. |  |
| MX-15-01 | PKG-15 | L1 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L1 - Business & Product Evaluation or its gate. |  |
| MX-15-02 | PKG-15 | L2 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L2 - Validation Readiness & Mandatory Controls or its gate. |  |
| MX-15-03 | PKG-15 | L3 | C | Conditional trigger: Experiment 1 incurs a material vendor/cost/admin action; payment testing remains prohibited. |  |
| MX-15-04 | PKG-15 | L4 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-15-05 | PKG-15 | L5 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-15-06 | PKG-15 | L6 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-15-07 | PKG-15 | L7 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-15-08 | PKG-15 | L8 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-15-09 | PKG-15 | L9 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-15-10 | PKG-15 | L10 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-15-11 | PKG-15 | L11 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-15-12 | PKG-15 | L12 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-15-13 | PKG-15 | L13 | R | Required: Finance, Cost, Vendor & Administration has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
| MX-16-00 | PKG-16 | L0 | N | Not applicable rationale: There is no customer lifecycle or operating support service before a user-facing validation journey exists. |  |
| MX-16-01 | PKG-16 | L1 | C | Conditional trigger: Evaluation needs direct adjacent-product support/lifecycle evidence or a supportability assumption assessment. |  |
| MX-16-02 | PKG-16 | L2 | C | Conditional trigger: Validation readiness needs participant-facing issue/recovery handling beyond the experiment operating pack. |  |
| MX-16-03 | PKG-16 | L3 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L3 - Concierge Behavioral Validation or its gate. |  |
| MX-16-04 | PKG-16 | L4 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L4 - Product Definition, Requirements & Experience Design or its gate. |  |
| MX-16-05 | PKG-16 | L5 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L5 - Architecture, Security, Privacy & Delivery Readiness or its gate. |  |
| MX-16-06 | PKG-16 | L6 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L6 - Build & Integration or its gate. |  |
| MX-16-07 | PKG-16 | L7 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L7 - Integrated Verification & Release Readiness or its gate. |  |
| MX-16-08 | PKG-16 | L8 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L8 - Controlled Integrated-Product Pilot or its gate. |  |
| MX-16-09 | PKG-16 | L9 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L9 - Pilot Evaluation & Production Decision or its gate. |  |
| MX-16-10 | PKG-16 | L10 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L10 - Production Launch Readiness or its gate. |  |
| MX-16-11 | PKG-16 | L11 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L11 - Production Launch & Stabilization or its gate. |  |
| MX-16-12 | PKG-16 | L12 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L12 - Year-1 Operations, Improvement & Responsible Growth or its gate. |  |
| MX-16-13 | PKG-16 | L13 | R | Required: Customer Experience Operations & Lifecycle Management has a mandatory obligation needed to complete L13 - Year-1 Close & Year-2 Decision or its gate. |  |
