## 1. Layer 1 - Program Architecture & Strategic Baseline

### 1.1 Program identity, mission, customer and JTBD

| Element | Constitutional baseline |
| --- | --- |
| Program | UseSafeWeb.com |
| Product | UseSafeWeb - First Phone Safety Setup |
| Primary customer | Parent or caregiver at the life stage where a roughly 10-12-year-old receives a first independently used smartphone; age is a life-stage indicator, not rigid eligibility. |
| Core JTBD | Establish sensible, age-appropriate guardrails quickly without invasive surveillance or requiring the parent to research multiple disconnected systems. |
| Experience model | Minimal intake/routing -> relevant Apple/Google safeguards -> real baseline DNS protection -> one relevant external-service safeguard -> truthful Protection Map. |
| Trust posture | Simple guardrails. Clear limits. No invasive monitoring. |
| Minimum product truth | Protected/verified, configured/parent-confirmed, action-needed, not-covered, uncertain/error, and removed are distinct states. |
| Startup model | Small, bootstrapped, AI-operated, product-first startup; responsibility packages do not imply departments or hires. |

### 1.2 Scope and explicit non-goals

| In scope now | Explicitly out of active baseline / conditional only |
| --- | --- |
| Accountless discovery and guided first-phone setup | Mandatory account/authentication/persistent parent dashboard (EXC-0001) |
| Native Apple/Google safeguard coordination | Rebuilding Apple/Google native parental controls |
| AdGuard-backed encrypted DNS baseline | Customer-facing generic DNS administration console |
| One relevant external-service safeguard | App catalogue or broad unsupported service configuration |
| Truthful Protection Map | Complete-safety, blocks-everything, or generic unverified no-logs claims |
| Self-service verification/troubleshooting/recovery/removal | Routine staffed human support operation (EXC-0008) |
| Public website plus product/setup surface | Native mobile app, child account, school portal, GROW automation (EXC-0005) |
| Core safety outcome free; optional supporter after value | Card/trial/payment before value or deliberate weakening of free safety |
| UK-targeted first; first public release multilingual in English, Turkish, and Arabic with RTL support | Official non-UK market activation/support without LG-16 evidence and approval |
| Lean recoverable infrastructure | Expensive near-zero-downtime HA without measured justification |

### 1.3 Lean-startup, quality and optimization doctrine

The governing rule is: **product correctness, security/privacy, reliability/trust, and quality are non-negotiable gates; inside those gates maximize AI autonomy/automation, then simplicity/operability, execution efficiency, cost efficiency, and only then scale/complexity**. The objective is the best working product for the correct effort without overkill; autonomy never lowers a gate or changes human-only authority.

- Validate the riskiest behavior before expensive build; L3 concierge validation and L8 integrated-product pilot remain separate.
- Use the minimum process necessary to produce high-quality, safe, verifiable work. Remove ceremony, reports, committees, duplicated documentation, or tooling that does not improve a real outcome/control.
- Direct customer-value packages dominate effort. Mandatory enabling/control functions remain lean. Administrative work remains minimal.
- Rolling-wave detail is allowed: near-term tasks are highly executable; medium-term tasks expose interfaces/quality/dependencies; distant Year-1 tasks preserve complete responsibility without false micromanagement.
- No exact future due date, cost, user number, or market result is invented. Relative timing, gates, sourced calculations, and hypotheses are used.
- Production rollout is simple by default: prechecks, health verification, known-good rollback, and post-change observation. Stronger blue/green/canary or equivalent rollout mechanics are added only for changes whose measured/risk profile justifies the extra complexity.

### 1.4 Product, UX, self-service and brand principles

| Principle | Binding interpretation |
| --- | --- |
| Near-zero friction | Every click/field/choice/account/confirmation/manual step requires a documented reason; remove anything not needed for decision, safety, or technical execution. |
| No mandatory account | Immediate accountless value is the baseline; optional persistence only after EXC-0001 trigger and full approval. |
| Installation | Use automatic/profile/configuration installation where supported/reliable; otherwise use the simplest technically correct platform-specific fallback. |
| Self-service | Ordinary issues are prevented or solved by UX, automated verification/troubleshooting, concise knowledge, AI assistance, recovery/removal. Repeated human help is a defect signal. |
| Truth | Parent confirmation is never technical verification; DNS/native/external-service limitations are disclosed at the relevant moment. |
| Experience before code | Customer evidence -> product definition -> service/journey design -> prototype -> usability/comprehension -> brand/design system -> validated UI -> implementation. |
| Brand | A full accessible visual/verbal system, not merely logo/colors; final polish follows sufficient behavioral evidence. |
| Two surfaces | Public website: discover/understand/trust/decide/start. Product/setup: start/configure/verify/understand/recover/manage. One shared design system, separate jobs. |

### 1.5 Market, geography and internationalization

| Concept | Baseline |
| --- | --- |
| Initial behavioral validation | England |
| Initial actively targeted market | United Kingdom |
| Technically available geography | May include Turkey, Arabic-speaking regions, and other permissible locations without implying official localized support. |
| Official localized/supported market | Requires LG-16 for a named market/locale. |
| First-public-release language capability | English, Turkish, and Arabic user-facing content/locale routing are supported from first public release, with externalized translation files, locale metadata, applicability controls, fallbacks, and tested RTL layout. |
| Market/support distinction | Multilingual technical/product capability does not imply official non-UK market activation, localized legal/support/channel commitments, or marketing claims; those remain gated by LG-16 for each named market. |

### 1.6 Business, funding and GTM constraints

- Bootstrapped; no fundraising program for approximately the first two years without a new owner decision.
- Core safety outcome remains free; no card/trial/payment before value. If the later supporter gate opens, fixed recurring choices are GBP £2/month or £20/year, EUR €2/month or €20/year, and USD $2/month or $20/year; currency is suggested automatically but manually selectable; Stripe and PayPal are the approved payment gateways; cancellation is available at any time; payment never changes protection.
- No advertising, sale, or monetization of family browsing behavior.
- Initial discretionary GTM budget is approximately USD 20-50/month maximum; funds may accumulate for bounded experiments.
- Earn distribution rather than buy it. Candidate engines include school/transition, parent/community/referral, high-intent organic content/search, and trusted organizations.
- At a growth stage, operate one primary engine and at most one serious challenger. Paid advertising is experimental only.
- AI may heavily assist high-quality original content; mass low-quality AI SEO is prohibited.
- 500 verified active users is an organizational/commercial review trigger, not a legal, geographic, hiring, or automatic scale threshold.

### 1.7 Frozen/current technical and privacy baseline

| Area | Baseline |
| --- | --- |
| Domain | UseSafeWeb.com |
| Backend | AdGuard, frozen unless verified material blocker/incompatibility/security/privacy/legal failure requires owner reconsideration. |
| Encrypted DNS | Essential. |
| Hosting | Microsoft Azure; owner provisions the base Azure VMs manually, and project automation begins only after an approved VM is available and reachable. |
| Application | One accountless-first full-stack TypeScript + Next.js application under top-level `/website`, covering the public website and setup/product surfaces in one deployable codebase. |
| Web UI/content | A mature accessible component library with light UseSafeWeb customization plus a lightweight browser-editable CMS; exact library/CMS implementation is selected at architecture execution against these constraints, not by adding a second application platform. |
| Application state | No application database by default; introduce persistent local storage only for a concrete validated requirement. Stripe/PayPal remain billing source of truth with only minimum reliable local references if required. |
| Repository/deployment layout | One canonical monorepo; `/website` owns the web application and `/infrastructure/adguard-server` owns the reproducible AdGuard/server deployment system and non-secret deployment material. |
| Server topology | Owner provides two separate fresh Ubuntu 24.04 LTS Azure VMs: one web/application server and one AdGuard/DNS server; Azure control-plane configuration is owner-managed; one AdGuard node initially; direct host installation is preferred and Docker/container orchestration is not a default requirement. |
| Environments | Production/pilot plus CI/ephemeral preview/test environments; no persistent staging unless evidence later justifies it. |
| Website edge | Cloudflare may provide authoritative DNS/CDN/WAF/TLS for the public website where beneficial; it is not inserted into the family AdGuard DNS resolution path by default. |
| Hostname separation | `UseSafeWeb.com` is the public website; encrypted DNS uses dedicated subdomain(s); private admin/operations/status hostnames are separate only when needed and are not unnecessarily exposed. |
| Experiment 1 region | Azure West Europe / Netherlands only for child-linked DNS. |
| Upstream | https://dns10.quad9.net/dns-query |
| ECS | Disabled; do not substitute an ECS endpoint. |
| Filtering/policy | AdGuard remains the sole product filtering/policy layer. |
| Query/file logs | Persistent identifiable query logging OFF; file query logging OFF. |
| Per-client statistics | Identifiable per-client statistics OFF/excluded unless specifically justified. |
| IP records | Anonymize client IP wherever operational records can contain it. |
| Product/analytics | No browsing history, top domains, visited-domain, or child activity metric. |
| Diagnostics | Only when necessary, minimum, time-boxed, access-controlled, and deleted after resolution. |

### 1.8 Availability and recovery model

Initial architecture deliberately accepts approximately **30 minutes of service downtime/recovery** for server failure or planned rebuild. Near-zero-downtime HA is not a current requirement and one AdGuard node is the initial baseline. The owner creates/provides the Azure VM; the automated responsibility begins from a reachable supported fresh Ubuntu 24.04 LTS host. One production-grade direct-host Bash deployment/recovery path under `/infrastructure/adguard-server` must provision the OS/service baseline, install/pin AdGuard, apply the approved DNS/TLS/upstream/filter/privacy state, harden firewall/access, verify DoH/DoT and health, perform backup/restore, and support controlled upgrade/rollback. Most live AdGuard configuration remains server-managed; Git stores deployment code and reviewed non-secret templates/expectations, while recoverable runtime configuration/secrets are protected through Azure/server backup/secret mechanisms and never committed to Git. Azure-native backup capability is the backup platform direction and must be configured, monitored, and restore-tested before it can satisfy recovery acceptance. Actual restoration time, not script runtime alone, is the acceptance measure.

### 1.9 Authority, source of truth and change control

- Latest explicit owner decision supersedes stale repository/tracker text until the authorized canonical update is written and read back.
- After owner freeze/publication, GitHub main is authoritative for the master plan/current state; ClickUp is the preferred operational derived view; Monday is optional executive/reporting only.
- No task, package, tracker, AI, or gate may redefine objectives, scope, requirements, interfaces, authority, acceptance, or frozen decisions outside approved change control.
- Material change requires CR-xxxx with initiator, reason/evidence, affected objects/interfaces/gates/risks, authority, decision, migration/rollback, verification, and canonical read-back.
- DEFERRED_EXCEPTION is distinct from N/Not Applicable. Exceptions have explicit trigger, authority, and current exclusion.

### 1.10 Status and state semantics

| Dimension | Allowed state | Meaning |
| --- | --- | --- |
| Planning | COMPLETED_RECORD / COMPLETED_EVIDENCE_INCOMPLETE / COMPLETED_CANDIDATE / READY_FOR_OWNER_ACTION / PLANNED / PLANNED_RECURRING / DEFERRED / SUPERSEDED_BASELINE / NOT_APPLICABLE | What the plan says exists or is intended. |
| Execution | TODO | Eligible now after dependency/gate/authority recomputation. |
| Execution | PASS | Every applicable acceptance criterion is supported by current evidence. |
| Execution | WAITING | Valid work is not eligible because a predecessor, lifecycle, trigger, gate, or authority is not satisfied. |
| Execution | BLOCKED | Work should be eligible now but a specific unexpected impediment prevents execution. |
| Lifecycle | L0-L13 | Where the program currently operates; not task completion. |
| Gate | Open / evidence-ready / decided outcome | Formal progression/transition control with explicit outcome. |

Parent roll-up rules: a parent cannot PASS while mandatory children are TODO/WAITING/BLOCKED; optional/conditional children require explicit deferred/not-applicable/superseded disposition; active recurring work keeps the operating parent active; evidence-incomplete historical work does not satisfy a successor requiring direct evidence.

### 1.11 Package taxonomy

| Package | Name | Startup relevance | Primary owner | AI target |
| --- | --- | --- | --- | --- |
| PKG-01 | Program Governance & Knowledge Management | Mandatory lean control | Project Owner / AI Governor | A4 where state changes are reversible and evidence-backed; A2 for canonical writes; A1 for owner decisions |
| PKG-02 | Business Strategy & Product Management | Direct customer value | Project Owner / Product | A3 for analysis and backlog management; A2 for consequential recommendations; A1 for owner product and strategic decisions |
| PKG-03 | Research, Validation & Experimentation | Direct customer value / de-risking | Product Research | A3 for design, synthesis, and analysis; A2 for participant operations; A1 for research involving real people |
| PKG-04 | Legal, Privacy, Compliance & Safeguarding | Mandatory trust/safety control | Privacy / Legal / Project Owner | A3 for research, inventories, drafts, and monitoring; A1 for legal conclusions, signatures, attestations, and residual-risk approval |
| PKG-05 | Brand System & Visual Identity | Direct trust/customer value after validation evidence | Brand / Product Owner | A3 for exploration and production; A1 for final owner taste/identity decisions |
| PKG-06 | UX, Service Design, Content & Accessibility | Core direct customer value | UX / Service Design / Content | A3 for synthesis, design, content, and test support; A1 for owner taste and real-user study authorization |
| PKG-07 | Web Experience & Application Engineering | Direct customer value after validation | Software / Frontend / Backend Engineering | A4 for tested delivery and explicitly low-risk reversible production releases after automated gates; A2 for material production infrastructure/security/data changes; A1 for irreversible external actions |
| PKG-08 | DNS / AdGuard Service Engineering | Core technical customer value | Network / DNS Engineering | A4 for tested configuration generation/verification/recovery; A2 for production DNS/filter changes |
| PKG-09 | Cloud Infrastructure & Platform Engineering | Mandatory enabling control | Cloud / Platform Engineering | A4 for post-VM automation, monitoring, tested reversible maintenance and rehearsed recovery; owner supplies base VMs; A2 for material production topology/security/data changes or destructive actions |
| PKG-10 | Security & Abuse Protection | Mandatory trust/safety control | Security | A4 for scanning/monitoring and bounded remediation; A2 for access/secret/network production changes; A1 for material residual-risk acceptance |
| PKG-11 | Data, Analytics & Measurement | Decision-enabling, privacy-minimal | Product Analytics | A4 for validated pipelines/monitoring; A3 for analysis; A2 for material metric/data-model change |
| PKG-12 | Quality Assurance, Verification & Release Readiness | Mandatory quality control | QA / Release Acceptance | A4 for automated verification; A3 for test design/analysis; A1 for final owner acceptance where consequential |
| PKG-13 | Service Operations, Reliability & Technical Support | Mandatory enabling control | SRE / Operations | A4 for monitoring, diagnosis, tested reversible maintenance/runbooks/recovery; A2 for material production remediation; A1 for service-disable/incident authority where material |
| PKG-14 | Marketing, Communications, Partnerships & Distribution | Direct growth value after product evidence | Growth / Communications / Partnerships | A3 for research/content/outreach preparation and measurement; A2 for public publishing/outreach; A1 for contracts/endorsements/material spend |
| PKG-15 | Finance, Cost, Vendor & Administration | Mandatory lean control | Project Owner / Finance | A3 for budgets/reconciliation/research; A2 for vendor configuration; A0/A1 for payments, contracts, tax filings, identity and banking |
| PKG-16 | Customer Experience Operations & Lifecycle Management | Direct customer value / self-service | Customer Experience / Product Operations | A4 for self-service assistance, classification, routing, and lifecycle automation; A2 for exceptional diagnostics/communications; A1 for safeguarding or sensitive escalations |

### 1.12 Lifecycle model

| Lifecycle | Name | Purpose | Primary exit gate |
| --- | --- | --- | --- |
| L0 | Original Inception & Technical Feasibility | Establish the problem, trust boundary, project identity, and technical feasibility without committing to full build. | LG-01 |
| L1 | Business & Product Evaluation | Complete evidence-based opportunity, product, market, operating, risk, and business-model evaluation. | LG-02 |
| L2 | Validation Readiness & Mandatory Controls | Make the bounded behavioral experiment legally, technically, operationally, and evidentially safe to run. | LG-03 |
| L3 | Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | LG-05 |
| L4 | Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system. | LG-06 |
| L5 | Architecture, Security, Privacy & Delivery Readiness | Approve production-capable architecture, controls, delivery plan, cost envelope, and implementation evidence model. | LG-07 |
| L6 | Build & Integration | Implement the smallest validated integrated product, website, DNS service, automation, and supporting systems. | LG-08 |
| L7 | Integrated Verification & Release Readiness | Prove the integrated release meets functional, UX, accessibility, security, privacy, reliability, recovery, and operational acceptance. | LG-09 |
| L8 | Controlled Integrated-Product Pilot | Operate the real integrated product with a bounded cohort and collect minimum evidence on value, persistence, reliability, supportability, and funding. | LG-10 |
| L9 | Pilot Evaluation & Production Decision | Synthesize pilot evidence and decide proceed, repeat, reduce, pivot, pause, or stop. | LG-11 |
| L10 | Production Launch Readiness | Prepare the approved UK production baseline, policies, operations, website, acquisition engine, budget, and staged rollout. | LG-12 |
| L11 | Production Launch & Stabilization | Launch in controlled stages, verify guardrails, correct high-value defects, and establish a stable operating baseline. | LG-14 |
| L12 | Year-1 Operations, Improvement & Responsible Growth | Operate, maintain, improve, automate, measure, and grow responsibly through the first full operating year. | LG-15 |
| L13 | Year-1 Close & Year-2 Decision | Close Year 1 with reconciled evidence and decide continue, adjust, expand, formalize, transfer, pause, or stop. | LG-15 |

### 1.13 Package x lifecycle obligation model

Every one of the 224 package/lifecycle intersections is dispositioned in Section 6.5. `R` means mandatory; `C` means the cell activates only on its exact recorded trigger; `N` means genuinely not applicable with rationale. Required/conditional work deliberately postponed is recorded separately as a DEFERRED_EXCEPTION, never disguised as N.

### 1.14 Interfaces and end-to-end traceability

Material cross-package work is exchanged through versioned interfaces in Section 6.6. Target traceability is: **Objective/Need -> Requirement/Constraint -> Package -> Deliverable -> Work Package -> Task -> VER -> EVD -> ACC -> Gate**. A task has one primary package owner; consumers use interfaces/dependencies instead of duplicate ownership.

### 1.15 Completeness and anti-omission controls

- 16 responsibility packages and all mandatory deliverable families.
- 14 lifecycle stages including distinct concierge and integrated-product pilots.
- 224 explicit matrix cells.
- Objective/requirement/constraint coverage and stable traceability.
- Material interfaces and handoff acceptance.
- Year-1 operations, maintenance, content currency, privacy/security, cost, support automation, growth, localization triggers, and close.
- Pause/pivot/stop/transfer/decommission route.
- Deterministic validation plus independent adversarial review.

### 1.16 Layer-1 acceptance/freeze criteria

Layer 1 is acceptable only when the identity/product/trust/technical/privacy/business/geography/recovery/autonomy/source/status/change models are internally consistent, every package/lifecycle/requirement/interface has ownership and evidence semantics, no latest owner decision is contradicted, and all completeness checks in Section 9 pass.
