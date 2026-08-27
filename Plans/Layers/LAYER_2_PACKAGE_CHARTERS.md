## 2. Layer 2 - Complete Package Charters

### PKG-01 - Program Governance & Knowledge Management

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory lean control |
| Purpose | Maintain one coherent, current, traceable program baseline and a deterministic execution system without startup bureaucracy. |
| Business/customer outcome | The owner and AI can always identify authoritative state, eligible work, evidence, decisions, risks, and the exact next bounded action. |
| Scope | Program constitution; source authority; baselines; WBS; registers; gates; change control; decision records; evidence indexes; GitHub persistence; derived tracker reconciliation; pause/stop governance. |
| Explicit out of scope | Product strategy decisions owned by PKG-02; legal opinions owned by PKG-04; technical implementation owned by engineering packages; routine administrative reporting with no decision value. |
| Responsibility boundaries | Defines governance contracts and accepts evidence; does not silently decide owner-only scope, risk, spend, launch, legal, or market choices. |
| Mandatory deliverable families | Program baseline; master plan; current-state checkpoint; decision/risk/evidence/change registers; gate packs; tracker derivation; closure archive. |
| Lifecycle obligations | Active in every lifecycle stage; depth scales with risk and current gate, not document volume. |
| Interfaces | Receives verified evidence from all packages; publishes approved baselines, eligibility, gates, decisions, and state. |
| Inputs | Owner decisions, canonical repository, verification evidence, risk/decision triggers, package outputs. |
| Outputs | Approved/frozen baselines, current state, gate decisions, next-task selection, change records, reconciled derived views. |
| Primary owner/authority | Project Owner / AI Governor |
| AI autonomy target | A4 where state changes are reversible and evidence-backed; A2 for canonical writes; A1 for owner decisions |
| Human authority boundaries | Owner approval for freeze, strategic scope changes, material residual risk, public launch, stop/pivot, large spend, irreversible production decisions. |
| Quality requirements | No unsupported PASS; no stale source override; complete traceability; idempotent writes; fetch/read-back verification; minimal governance overhead. |
| Acceptance/success criteria | Canonical state is internally consistent; every active gate has evidence; every task has one owner; no derived system can override GitHub. |
| KPIs/decision signals | State drift incidents; orphan/duplicate findings; gate evidence completeness; failed canonical-write verification; time to identify next eligible task. |
| Risks | Stale state, false completion, tracker drift, duplicated ownership, AI authority overreach, excessive process. |
| Triggers | Any material decision, gate, scope change, incident, evidence change, source conflict, tracker sync, pause/pivot/stop event. |
| Dependencies | All packages supply evidence; GitHub availability; owner authority. |
| Evidence requirements | Commit/blob SHA, read-back comparison, validated registers, gate evidence index, audit report. |
| Condition for deliberate minimalism | Keep a single current-state checkpoint, one master plan, and only registers needed for decisions/evidence. |

### PKG-02 - Business Strategy & Product Management

| Charter field | Definition |
| --- | --- |
| Startup relevance | Direct customer value |
| Purpose | Define the correct customer problem, product promise, scope, value model, roadmap, and decision thresholds. |
| Business/customer outcome | UseSafeWeb remains a focused first-phone safety setup product that adds measurable value without surveillance or unnecessary features. |
| Scope | Mission; customer/JTBD; product definition; scope/non-goals; requirements; prioritization; product economics assumptions; roadmap; product decisions; lifecycle value; stop/pivot criteria. |
| Explicit out of scope | Primary research execution PKG-03; legal PKG-04; UX artifacts PKG-06; implementation PKG-07/08/09; GTM execution PKG-14; finance operations PKG-15. |
| Responsibility boundaries | Owns what and why; consuming packages own how within approved interfaces and acceptance. |
| Mandatory deliverable families | Product brief; requirements; non-goals; roadmap; decision thresholds; value hypothesis; product baseline; quarterly/year-end decisions. |
| Lifecycle obligations | Continuous, with highest detail at evaluation, validation synthesis, product definition, pilot decisions, launch scope, and Year-1 prioritization. |
| Interfaces | Supplies requirements and priorities; consumes research, UX, technical, legal, quality, operations, finance, and channel evidence. |
| Inputs | Owner direction, customer evidence, product analytics, support root causes, cost/risk evidence, platform constraints. |
| Outputs | Approved product definition, requirements, prioritized backlog, outcome metrics, decision recommendations, scope controls. |
| Primary owner/authority | Project Owner / Product |
| AI autonomy target | A3 for analysis and backlog management; A2 for consequential recommendations; A1 for owner product and strategic decisions |
| Human authority boundaries | Final product taste, material objective/scope changes, funding/model changes, market/pivot/stop decisions. |
| Quality requirements | Evidence before build; no feature inflation; clear requirements; measurable acceptance; no false certainty; product/UX value dominates admin. |
| Acceptance/success criteria | All critical customer needs map to requirements, tasks, tests, evidence, and gates; non-goals remain excluded unless explicitly reopened. |
| KPIs/decision signals | Full activation; incremental safeguard completion; protection persistence; comprehension; abandonment due to added work; support burden. |
| Risks | Wrong product, native-control redundancy, overbuilding, dashboard/account creep, weak incremental value. |
| Triggers | New behavioral evidence, material platform change, threshold breach, support pattern, strategic review, owner decision. |
| Dependencies | PKG-03 evidence; PKG-04 constraints; PKG-06 validation; PKG-11 measures; PKG-15 economics. |
| Evidence requirements | Approved product brief/requirements; traceability; decision records; measured outcome reports. |
| Condition for deliberate minimalism | Maintain only the active product brief, non-goals, critical requirements, prioritized backlog, and decision thresholds. |

### PKG-03 - Research, Validation & Experimentation

| Charter field | Definition |
| --- | --- |
| Startup relevance | Direct customer value / de-risking |
| Purpose | Resolve the highest-value uncertainties with the smallest ethical experiment before increasing investment. |
| Business/customer outcome | Behavioral, usability, channel, and product decisions are based on observed evidence rather than stated interest or model inference. |
| Scope | Research questions; protocols; recruitment; concierge validation; usability/comprehension studies; controlled pilot studies; experiments; synthesis; sample limitations. |
| Explicit out of scope | Product decisions PKG-02; legal basis PKG-04; production analytics PKG-11; routine customer lifecycle PKG-16. |
| Responsibility boundaries | Produces evidence and recommendations; does not silently authorize build, launch, or strategic change. |
| Mandatory deliverable families | Experiment protocol; screener; facilitator pack; structured records; Wave A/B evidence; usability studies; pilot evidence; synthesis reports. |
| Lifecycle obligations | Required at evaluation/concierge/pilot; conditional elsewhere when uncertainty is decision-material. |
| Interfaces | Consumes product questions, privacy constraints, prototype/service; supplies findings to product, UX, engineering, GTM, finance, and gates. |
| Inputs | Decision questions, cohort definition, minimum data schema, prototype/product, thresholds, prior evidence. |
| Outputs | Validated/invalidated hypotheses, observed behavior, friction/root causes, recommendations, anonymized evidence. |
| Primary owner/authority | Product Research |
| AI autonomy target | A3 for design, synthesis, and analysis; A2 for participant operations; A1 for research involving real people |
| Human authority boundaries | Participant contact/consent communication, sensitive facilitation, owner authorization for real cohorts, safeguarding escalation. |
| Quality requirements | Predefined question and thresholds; minimum data; no leading; interventions measured; observed vs inferred separated; limitations explicit. |
| Acceptance/success criteria | Protocol is reproducible; data minimum is respected; analysis formulas/denominators are auditable; decision output addresses contrary evidence. |
| KPIs/decision signals | Qualified cohort; completion; intervention minutes; comprehension; persistence; sample/data-quality defects. |
| Risks | Biased facilitation, tiny samples overclaimed, hidden human assistance, privacy leakage, experimentation after answer is already clear. |
| Triggers | Critical uncertainty; failed threshold; new path/platform; material product/market change; gate requirement. |
| Dependencies | PKG-02 questions; PKG-04 approval; PKG-06 journey/prototype; PKG-08/09 safe DNS path; PKG-11 measurement. |
| Evidence requirements | Versioned protocol, pseudonymous dataset, analysis notebook/report, decision record, deletion verification. |
| Condition for deliberate minimalism | One decision question, smallest qualified cohort, minimum metrics, one controlled iteration, explicit stop conditions. |

### PKG-04 - Legal, Privacy, Compliance & Safeguarding

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory trust/safety control |
| Purpose | Keep the service lawful, privacy-minimal, transparent, child-appropriate, and within its safeguarding and claims boundaries. |
| Business/customer outcome | No real-user stage proceeds without applicable authority, data minimization, transparency, rights, vendor, claims, and safeguarding controls. |
| Scope | Territorial/applicability analysis; controller/representative/fees; data flows; lawful basis; LIA/DPIA; notices/terms; rights; retention/deletion; safeguarding; claims; vendor DPAs/transfers; legal monitoring. |
| Explicit out of scope | Security engineering PKG-10; data implementation PKG-07/11; finance execution PKG-15; product definition PKG-02. |
| Responsibility boundaries | Defines obligations and accepts legal/privacy evidence; technical packages implement controls; owner/specialist makes final legal/residual decisions. |
| Mandatory deliverable families | Legal/applicability record; data inventory; LIA/DPIA; notices/terms; rights/deletion procedures; safeguarding/claims policy; vendor register; compliance monitoring. |
| Lifecycle obligations | Required before and during any real-user processing; scaled down for synthetic/historical stages. |
| Interfaces | Publishes constraints/approved text/controls; consumes actual data flows, logs, vendors, UX, incidents, releases, and changes. |
| Inputs | Product/service design, data flows, technical configuration, vendors, geography, user journey, incidents/changes. |
| Outputs | Approved legal/privacy baseline, public disclosures, processing controls, risk decisions, compliance actions. |
| Primary owner/authority | Privacy / Legal / Project Owner |
| AI autonomy target | A3 for research, inventories, drafts, and monitoring; A1 for legal conclusions, signatures, attestations, and residual-risk approval |
| Human authority boundaries | Legal advice/opinions, signatures, representative appointment, fee/payment, contracts, residual-risk acceptance, regulator communication. |
| Quality requirements | Current authoritative sources; actual deployed reality; no generic no-logs claim; child-readable transparency; minimum data and retention. |
| Acceptance/success criteria | Every processing purpose has basis/necessity; actual flows match records/notices; high risks are resolved or explicitly decided; rights/deletion tests pass. |
| KPIs/decision signals | Open high privacy risks; rights/deletion failures; notice drift; retention failures; vendor review overdue; safeguarding escalation patterns. |
| Risks | Identifiable DNS history, misleading claims, missing UK route, unlawful transfer, excess data, child harm/false confidence. |
| Triggers | Real-user processing, new data/vendor/geography/feature, incident, law change, recurring payment, launch, material release. |
| Dependencies | All product/technical/data/vendor packages provide actual facts; owner/specialist authority. |
| Evidence requirements | Source-cited assessments, signed/approved records, config/test evidence, public-version snapshots, rights/deletion logs. |
| Condition for deliberate minimalism | Only applicable obligations and minimum records; no compliance theatre or invented legal certainty. |

### PKG-05 - Brand System & Visual Identity

| Charter field | Definition |
| --- | --- |
| Startup relevance | Direct trust/customer value after validation evidence |
| Purpose | Create a coherent, trustworthy, accessible brand system that supports both public discovery and the setup product. |
| Business/customer outcome | UseSafeWeb is recognizable, credible, calm, non-surveillance, and consistent across website, application, help, status, partner, and communication surfaces. |
| Scope | Positioning expression; promise; logo; typography; color; visual language; imagery; icons; voice/tone; trust language; layout; reusable templates; assets; usage/accessibility rules. |
| Explicit out of scope | Product positioning decision PKG-02; journey/content PKG-06; engineering implementation PKG-07; campaigns PKG-14. |
| Responsibility boundaries | Owns reusable brand system; does not replace UX research, product requirements, or campaign strategy. |
| Mandatory deliverable families | Brand strategy brief; identity system; verbal system; design tokens; asset library; guidelines; public/product templates. |
| Lifecycle obligations | Deliberately minimal before behavioral evidence; required before validated UI and launch assets are finalized. |
| Interfaces | Consumes product/trust/customer evidence; supplies approved tokens/assets/voice to UX, engineering, marketing, support. |
| Inputs | Positioning, customer evidence, trust/privacy constraints, accessibility criteria, surface inventory. |
| Outputs | Versioned editable brand assets, tokens, voice/trust language, guidelines, templates. |
| Primary owner/authority | Brand / Product Owner |
| AI autonomy target | A3 for exploration and production; A1 for final owner taste/identity decisions |
| Human authority boundaries | Final logo/identity/taste approval and material brand repositioning. |
| Quality requirements | Distinct but not decorative; accessible contrast/readability; editable masters; usage consistency; no misleading safety signals. |
| Acceptance/success criteria | All required surfaces can be built from one approved system; accessibility and small/mobile formats pass; asset ownership/versioning is clear. |
| KPIs/decision signals | Brand comprehension/trust feedback; inconsistent asset defects; accessibility failures; time to produce approved channel asset. |
| Risks | Premature polishing, generic AI aesthetic, trust mismatch, inaccessible color/type, asset drift. |
| Triggers | Behavioral proposition passes enough to justify final polish; new surface/locale; material repositioning. |
| Dependencies | PKG-02 positioning; PKG-03 evidence; PKG-04 claims; PKG-06 service/UX needs. |
| Evidence requirements | Approved brand board/guidelines, editable assets, accessibility tests, surface QA. |
| Condition for deliberate minimalism | Before validation, use only name/domain and functional trust copy; defer full identity polish until proposition evidence. |

### PKG-06 - UX, Service Design, Content & Accessibility

| Charter field | Definition |
| --- | --- |
| Startup relevance | Core direct customer value |
| Purpose | Turn the product into a near-zero-friction, self-service, truthful, accessible end-to-end experience. |
| Business/customer outcome | A normal parent can discover, configure, verify, understand, recover, and remove protection with minimal choices and no routine human support. |
| Scope | Journey/service blueprint; information architecture; onboarding; routing; setup; Protection Map; troubleshooting/recovery/removal; prototype; usability/comprehension; content system; accessibility; localization/RTL readiness. |
| Explicit out of scope | Brand identity PKG-05; code PKG-07; DNS mechanics PKG-08; support operations PKG-16; campaigns PKG-14. |
| Responsibility boundaries | Owns experience contract and content; engineering owns implementation; QA independently verifies acceptance. |
| Mandatory deliverable families | Journey maps; service blueprint; interaction/content requirements; prototypes; usability reports; design system components; instruction/help catalogue; accessibility/i18n specification. |
| Lifecycle obligations | Required from concierge design through Year-1 maintenance; final polish follows sufficient proposition evidence. |
| Interfaces | Consumes product, research, legal, platform, DNS, support evidence; supplies validated experience/content specifications to engineering and operations. |
| Inputs | JTBD, product requirements, platform paths, legal copy, brand system, defects/support root causes, localization requirements. |
| Outputs | Validated flows/prototypes/content, design system, accessibility/i18n requirements, help/recovery assets. |
| Primary owner/authority | UX / Service Design / Content |
| AI autonomy target | A3 for synthesis, design, content, and test support; A1 for owner taste and real-user study authorization |
| Human authority boundaries | Owner approval of major experience/taste choices; real-user research; material safety-language decisions. |
| Quality requirements | Every interaction justified; one-to-three meaningful actions where technically possible; verified vs confirmed truth; WCAG-oriented; mobile-first; maintainable/localizable content. |
| Acceptance/success criteria | Critical journeys pass usability/comprehension/accessibility testing; no false verification; recovery/removal works; content is versioned and platform-current. |
| KPIs/decision signals | Steps/time; abandonment; assistance; comprehension; accessibility defects; stale guidance; self-service resolution. |
| Risks | Friction, cognitive overload, false confidence, inaccessible UI, documentation drift, premature visual polish, unsupported cross-platform assumptions. |
| Triggers | New/changed platform path; repeated support issue; material product change; new locale; failed usability/accessibility threshold. |
| Dependencies | PKG-02/03/04/05/08 inputs; PKG-12 verification; PKG-16 feedback. |
| Evidence requirements | Prototype/version, study report, accessibility audit, content source/review record, journey acceptance evidence. |
| Condition for deliberate minimalism | At each stage, design only the validated current path plus recovery and truthful limits; avoid speculative screens/features. |

### PKG-07 - Web Experience & Application Engineering

| Charter field | Definition |
| --- | --- |
| Startup relevance | Direct customer value after validation |
| Purpose | Implement the public website and product/setup experience as secure, accessible, maintainable, accountless-by-default software. |
| Business/customer outcome | The two distinct surfaces - public discovery and product setup - perform their jobs reliably while sharing one design system and minimal data model. |
| Scope | Public website; setup application; accountless session/state; routing; native/service guidance; DNS activation/verification UI; Protection Map; help/recovery; APIs; optional future persistence only after trigger; CI/CD integration. |
| Explicit out of scope | DNS engine PKG-08; cloud platform PKG-09; security policy PKG-10; analytics definitions PKG-11; independent QA PKG-12. |
| Responsibility boundaries | Implements approved requirements and interfaces; does not invent major product/UX or add mandatory accounts during coding. |
| Mandatory deliverable families | Application architecture; public site; setup app; minimal APIs/state; integrations; tests; release artifacts; technical documentation. |
| Lifecycle obligations | Conditional before validation; required for definition/prototyping, build, verification, pilot, launch, and Year-1 maintenance. |
| Interfaces | Consumes product/UX/brand/legal/DNS/platform/security/data specifications; publishes deployable releases and runtime contracts. |
| Inputs | Frozen requirements, validated UI/content, API contracts, environment/config, security controls, test plan. |
| Outputs | Versioned source/builds, deployed surfaces, API/interface evidence, automated tests, rollback artifacts. |
| Primary owner/authority | Software / Frontend / Backend Engineering |
| AI autonomy target | A4 in tested non-production delivery; A2 for production deployment/data changes; A1 for irreversible external actions |
| Human authority boundaries | Production release authorization, credentials/domain/provider actions, destructive migrations, optional-account scope decision. |
| Quality requirements | Small vertical slices; secure defaults; no unnecessary auth/data; accessibility/performance; explicit failures; testable interfaces; rollback. |
| Acceptance/success criteria | All in-scope journeys and non-goals trace to code/tests; accountless value works; no unauthorized data/surveillance; release/rollback verified. |
| KPIs/decision signals | Critical journey success; error/performance; accessibility defects; escaped defects; deployment/recovery success; code/contract drift. |
| Risks | Premature build, auth/dashboard overbuild, IDOR if persistence added, inaccessible UI, coupling to AdGuard admin API, untested migrations. |
| Triggers | Positive behavioral gate; approved requirements/architecture; product/platform changes; defects/incidents. |
| Dependencies | PKG-02/04/05/06/08/09/10/11; PKG-12 acceptance. |
| Evidence requirements | Repository commit, CI results, release manifest, E2E evidence, security/accessibility/performance reports. |
| Condition for deliberate minimalism | Static/server-rendered public site plus lightweight accountless setup app and only necessary server functions; no conventional SaaS shell. |

### PKG-08 - DNS / AdGuard Service Engineering

| Charter field | Definition |
| --- | --- |
| Startup relevance | Core technical customer value |
| Purpose | Provide real, privacy-minimal, encrypted baseline DNS protection and technically correct platform-specific installation. |
| Business/customer outcome | Supported devices use the canonical UseSafeWeb DNS identity, filtering works, limits are truthful, and no identifiable browsing-history product exists. |
| Scope | AdGuard release/config; DoH endpoint; upstream Quad9 dns10; ECS off; privacy settings; filters/allowlists; client configuration methods; verification; abuse controls coordination; config export/versioning; recovery integration. |
| Explicit out of scope | Host/cloud PKG-09; security controls PKG-10; UX instructions PKG-06; application UI PKG-07; operations PKG-13. |
| Responsibility boundaries | Owns DNS service behavior/config; does not own parent identity, surveillance analytics, or unrestricted admin UI. |
| Mandatory deliverable families | DNS architecture; approved config; endpoint/cert contract; platform profiles/instructions; filter baseline; test sets; versioned recovery config. |
| Lifecycle obligations | Required from feasibility through all live stages; depth increases at pilot/production. |
| Interfaces | Consumes host/security/privacy/product requirements; supplies endpoint, configuration, verification, failure and recovery contracts. |
| Inputs | Frozen technical decisions, supported platforms, privacy requirements, filter evidence, environment/network/TLS. |
| Outputs | Operational resolver, approved config, client setup assets, DNS verification evidence, filter/change artifacts. |
| Primary owner/authority | Network / DNS Engineering |
| AI autonomy target | A4 for tested configuration generation/verification/recovery; A2 for production DNS/filter changes |
| Human authority boundaries | Production endpoint/filter policy approval when material, credentials/provider/domain actions, critical service disablement. |
| Quality requirements | Encrypted DNS; exact upstream; ECS disabled; query/file logging off; identifiable statistics off; anonymization where records exist; low false positives; reproducible config. |
| Acceptance/success criteria | External supported-device tests pass; configuration inspection proves privacy invariants; allowed/blocked/removal/recovery tests pass. |
| KPIs/decision signals | Resolution success/latency; filter regressions; false positives; persistence; configuration drift; recovery time. |
| Risks | Outage, abuse, overblocking, bypass/compatibility, stale AdGuard behavior, logging drift, certificate failure. |
| Triggers | AdGuard/filter/platform/upstream change; incident; new supported device/region; privacy drift; capacity threshold. |
| Dependencies | PKG-04/06/09/10/12/13. |
| Evidence requirements | Version/config hash, external test outputs, privacy inspection, regression results, recovery drill evidence. |
| Condition for deliberate minimalism | One canonical service identity, one approved baseline, only supported platform-specific methods, no per-family browsing data. |

### PKG-09 - Cloud Infrastructure & Platform Engineering

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory enabling control |
| Purpose | Provide the smallest secure Azure platform and a reproducible fresh-server recovery path within the accepted outage window. |
| Business/customer outcome | UseSafeWeb can be deployed, rebuilt, restored, observed, and cost-controlled without premature high availability. |
| Scope | Azure topology; Ubuntu 24.04 LTS host baseline; network/firewall; TLS/domain automation; IaC/configuration; secrets integration; deployment/recovery Bash script; environments; backups; capacity/cost; drift. |
| Explicit out of scope | AdGuard behavior PKG-08; application code PKG-07; security policy PKG-10; operations PKG-13. |
| Responsibility boundaries | Owns platform and automation; does not choose product scope or invent expensive HA without evidence. |
| Mandatory deliverable families | Architecture/ADR; Azure resources; hardened host; network/TLS; production-grade recovery script; backup/restore; environment/deployment pipeline; capacity/cost model. |
| Lifecycle obligations | Required from validation readiness through Year 1; feasibility stages remain minimal. |
| Interfaces | Consumes application/DNS/security/privacy/operations requirements; supplies stable runtime, deployment, recovery and environment contracts. |
| Inputs | Approved topology, Ubuntu version, configs, secrets, domain/DNS, budgets, RTO/RPO, test plan. |
| Outputs | Provisioned environments, versioned automation, recovery evidence, resource inventory, drift/cost reports. |
| Primary owner/authority | Cloud / Platform Engineering |
| AI autonomy target | A4 for IaC and rehearsed recovery in non-production; A2 for production provision/change/destroy |
| Human authority boundaries | Cloud account/billing/credential actions, production deploy/destroy, domain/registrar changes, material spend/topology decisions. |
| Quality requirements | Fresh Ubuntu 24.04 LTS to verified service in approximately 30 minutes end-to-end; idempotent; fail-closed; versioned; secret-safe; no unreviewed services. |
| Acceptance/success criteria | Clean-server drill provisions all required components and passes DNS/TLS/privacy/security/health tests inside accepted window; rollback/retry tested. |
| KPIs/decision signals | Measured RTO/RPO; deployment success; config drift; cost; patch state; backup/restore success; capacity headroom. |
| Risks | Non-reproducible recovery, hidden manual step, secret leakage, Azure region drift, cost creep, premature HA, dependency failure. |
| Triggers | Environment build/rebuild; release; incident; platform/OS change; capacity/cost threshold; recovery rehearsal cadence. |
| Dependencies | PKG-07/08/10/12/13/15. |
| Evidence requirements | IaC/script source hash, dry-run/clean-server transcript, timings, config/test report, Azure metadata, cost record. |
| Condition for deliberate minimalism | Single appropriately sized node/topology initially; invest in HA only when measured impact/risk justifies complexity/cost. |

### PKG-10 - Security & Abuse Protection

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory trust/safety control |
| Purpose | Prevent, detect, contain, and recover from compromise, abuse, unauthorized access, and unsafe failure modes. |
| Business/customer outcome | Public DNS and web surfaces operate with least privilege, safe defaults, verified controls, and actionable incident evidence. |
| Scope | Threat/abuse models; hardening; IAM/secrets; vulnerability/dependency management; secure coding review; auth if later justified; resolver abuse/rate limits; scans/tests; incident security; access review. |
| Explicit out of scope | Privacy/legal PKG-04; platform implementation PKG-09; DNS PKG-08; QA independent acceptance PKG-12; operations PKG-13. |
| Responsibility boundaries | Defines/verifies security controls and risk; owning engineering package implements; owner approves material residual risk. |
| Mandatory deliverable families | Threat model; security requirements; hardening/access baseline; abuse controls; security tests; vulnerability process; incident playbooks; access/secret reviews. |
| Lifecycle obligations | Required before real-user processing and continuously thereafter; scaled for synthetic/historical work. |
| Interfaces | Consumes architecture/data/exposure; supplies controls/tests/findings/acceptance to engineering, QA, legal, gates. |
| Inputs | Architecture, data flow, endpoints, code/config, identities/secrets, dependencies, abuse/capacity assumptions. |
| Outputs | Approved threat model/controls, findings, remediation evidence, residual-risk record, incident evidence. |
| Primary owner/authority | Security |
| AI autonomy target | A4 for scanning/monitoring and bounded remediation; A2 for access/secret/network production changes; A1 for material residual-risk acceptance |
| Human authority boundaries | Credential ownership, access approval, material risk acceptance, external notifications, irreversible emergency actions. |
| Quality requirements | Least privilege; no public admin; secret isolation; input validation; rate/abuse controls; timely patching; tested incident recovery. |
| Acceptance/success criteria | No unresolved critical/high blocker; attack paths/control tests pass; access/secrets are justified; incident runbook rehearsed. |
| KPIs/decision signals | Critical/high findings; remediation age; unauthorized access; abuse/cost anomalies; patch lag; control-test failures. |
| Risks | Open-resolver abuse, admin compromise, secret exposure, supply chain, injection/IDOR if accounts added, unsafe fail-open. |
| Triggers | New endpoint/data/vendor/release; vulnerability/advisory; abuse anomaly; incident; access/secret change; architecture gate. |
| Dependencies | PKG-04/07/08/09/12/13. |
| Evidence requirements | Threat model, scan/test outputs, access/secret inventory, remediation retest, incident/drill record. |
| Condition for deliberate minimalism | Threat-model and test only real attack surface; avoid enterprise tooling that does not materially improve detection or recovery. |

### PKG-11 - Data, Analytics & Measurement

| Charter field | Definition |
| --- | --- |
| Startup relevance | Decision-enabling, privacy-minimal |
| Purpose | Measure product value, quality, operations, acquisition, cost, and decisions with the minimum non-surveillance data. |
| Business/customer outcome | Every important decision has trustworthy definitions, denominators, sources, uncertainty, and privacy-safe evidence. |
| Scope | Measurement framework; event catalogue; validation/pilot datasets; product/operational/channel/cost metrics; data quality; dashboards; analysis; retention/deletion coordination; no browsing-history metrics. |
| Explicit out of scope | Privacy authority PKG-04; product decisions PKG-02; research protocols PKG-03; telemetry implementation PKG-07/09/13. |
| Responsibility boundaries | Defines and validates measurement; does not collect data merely because available or optimize addictive engagement. |
| Mandatory deliverable families | Metric dictionary; event/data contracts; experiment/pilot schema; dashboards/reports; data-quality controls; decision analyses. |
| Lifecycle obligations | Required wherever decisions or gates depend on evidence; continuous in Year 1. |
| Interfaces | Consumes decision questions/runtime events/cost/support/channel data; supplies reports/evidence to product, governance, operations, GTM, finance. |
| Inputs | Requirements, thresholds, data inventory, source systems, cohorts/releases, privacy/retention rules. |
| Outputs | Auditable metrics, anonymized datasets, analyses, alerts, KPI/gate evidence. |
| Primary owner/authority | Product Analytics |
| AI autonomy target | A4 for validated pipelines/monitoring; A3 for analysis; A2 for material metric/data-model change |
| Human authority boundaries | Approval of material new data collection; interpretation of strategic tradeoffs; sensitive data access. |
| Quality requirements | Minimum fields; explicit definitions/denominators; source/version/time window; data quality; uncertainty; no domain history/top-domain/activity profiling. |
| Acceptance/success criteria | Metrics reproduce from source; privacy review passes; missing/biased data stated; every KPI has action/owner, not vanity. |
| KPIs/decision signals | Data-quality failures; undefined metrics; privacy exceptions; decision latency; false/late alerts. |
| Risks | Vanity metrics, privacy creep, bad denominators, causal overclaim, dashboard engagement optimization, stale data. |
| Triggers | New decision/gate, experiment/release/channel, metric drift, data-quality alert, privacy change. |
| Dependencies | PKG-02/03/04/07/09/13/14/15/16. |
| Evidence requirements | Metric catalogue, schema/version, query/notebook, reconciliation report, dashboard snapshot, data-deletion proof. |
| Condition for deliberate minimalism | Collect only fields tied to named decisions/controls; prefer aggregate/synthetic telemetry; retire unused measures. |

### PKG-12 - Quality Assurance, Verification & Release Readiness

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory quality control |
| Purpose | Independently prove that deliverables meet acceptance criteria in the target environment before gates or releases pass. |
| Business/customer outcome | PASS means current evidence supports every criterion, not merely that an artifact exists or a developer says it works. |
| Scope | Master test strategy; functional/integration/E2E; device/network; UX/comprehension; accessibility; security/privacy coordination; performance/capacity; recovery; release acceptance; defect governance. |
| Explicit out of scope | Engineering implementation; owner gate decision; operational monitoring outside release acceptance. |
| Responsibility boundaries | Verifies independently from producer where practical; does not lower criteria to make a release pass. |
| Mandatory deliverable families | Test strategy/cases; fixtures; automation; compatibility matrix; acceptance reports; defect register; release evidence; regression suite. |
| Lifecycle obligations | Required from validation-readiness verification through every release and Year-1 maintenance. |
| Interfaces | Consumes requirements/artifacts/environments/controls; supplies verified results/defects/acceptance to producers and governance. |
| Inputs | Traceable requirements, acceptance criteria, builds/configs, supported matrix, risk model, production-like environment. |
| Outputs | Test evidence, defect dispositions, acceptance report, release recommendation, regression assets. |
| Primary owner/authority | QA / Release Acceptance |
| AI autonomy target | A4 for automated verification; A3 for test design/analysis; A1 for final owner acceptance where consequential |
| Human authority boundaries | Owner accepts material residual defects/risks; real-device/manual usability/accessibility judgement where automation is insufficient. |
| Quality requirements | Reproducible, target-environment, risk-based, independent, current to exact version/config, negative/failure/recovery coverage. |
| Acceptance/success criteria | All critical requirements have passing evidence; no unresolved severity-1/2 or control blocker; evidence version matches release. |
| KPIs/decision signals | Escaped defects; flaky tests; requirement coverage; defect age; acceptance rework; recovery/compatibility pass rates. |
| Risks | False PASS, local-only evidence, missing negative path, stale tests, inflated coverage, producer self-certification. |
| Triggers | Gate/release/change; defect/incident; platform/dependency update; risk/requirement change. |
| Dependencies | All producing packages; governance acceptance criteria; target environments/access. |
| Evidence requirements | Test logs/reports, screenshots where needed, version/config manifest, defect/retest record, signed acceptance index. |
| Condition for deliberate minimalism | Automate stable critical paths; use focused manual checks where human comprehension/accessibility/real devices matter. |

### PKG-13 - Service Operations, Reliability & Technical Support

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory enabling control |
| Purpose | Keep the service observable, recoverable, maintained, and diagnosable with exceptional technical escalation rather than routine staffed support. |
| Business/customer outcome | Ordinary failures are prevented or self-recovered; incidents are detected, contained, communicated, restored, and converted into verified corrective actions. |
| Scope | SLIs/SLOs; monitoring/alerts; runbooks; incident/change/release operations; backup/restore/DR; recovery rehearsal; patch/filter/cert/vendor operations; exceptional diagnostics; status communication coordination. |
| Explicit out of scope | Customer lifecycle/self-service PKG-16; engineering fixes PKG-07/08/09; legal incident obligations PKG-04. |
| Responsibility boundaries | Technical operations and exceptional escalation only; repeated ordinary user help is a product/UX automation defect. |
| Mandatory deliverable families | Observability; runbooks; incident/change/release system; backup/restore/DR; maintenance; capacity; technical knowledge; post-incident actions. |
| Lifecycle obligations | Required before real-user DNS and continuously thereafter. |
| Interfaces | Consumes deployed service/controls; supplies health/incidents/root causes/recovery evidence to engineering, product, governance, customer communications. |
| Inputs | Architecture, service inventory, SLIs, runbooks, access, releases, alerts, vendor status, recovery artifacts. |
| Outputs | Service state, incident/recovery evidence, maintenance records, capacity/cost signals, corrective actions. |
| Primary owner/authority | SRE / Operations |
| AI autonomy target | A4 for monitoring, diagnosis, runbook execution, safe recovery; A2 for production remediation; A1 for service-disable/incident authority where material |
| Human authority boundaries | Major service disablement, public incident statements, regulator/user notification, irreversible recovery decisions, emergency credential actions. |
| Quality requirements | Actionable privacy-safe telemetry; no browsing history; tested runbooks; measured end-to-end recovery; owner/backup; proportional postmortem. |
| Acceptance/success criteria | Critical probes/alerts/routes work; clean restore/rebuild passes; accepted RTO achieved; incident/change records reconcile to state. |
| KPIs/decision signals | Availability/error/latency; MTTD/MTTR; recovery drill time; alert quality; maintenance failures; repeat incidents. |
| Risks | Silent outage, alert fatigue, hidden manual recovery, key-person dependency, diagnostic privacy leakage, unsafe fail-open. |
| Triggers | Alert/incident; scheduled maintenance; release; certificate/domain/vendor change; capacity/cost threshold; recovery cadence. |
| Dependencies | PKG-04/07/08/09/10/11/12/15/16. |
| Evidence requirements | Monitoring/alert test, incident timeline, runbook transcript, recovery timing, postmortem/corrective-action retest. |
| Condition for deliberate minimalism | Only critical signals/runbooks/cadences; automate repeatable response; no 24x7 staffed support promise without evidence/resources. |

### PKG-14 - Marketing, Communications, Partnerships & Distribution

| Charter field | Definition |
| --- | --- |
| Startup relevance | Direct growth value after product evidence |
| Purpose | Earn trusted, low-cost distribution and communicate the product accurately without spreading effort across unproven channels. |
| Business/customer outcome | One evidence-backed primary acquisition engine and at most one serious challenger produce qualified activations within budget and trust constraints. |
| Scope | Channel strategy/tests; schools/transition; organic high-intent content/SEO; referrals; trusted organizations; brand handles; public/incident communications; bounded paid experiments; localization GTM. |
| Explicit out of scope | Brand system PKG-05; product content/UX PKG-06; product decisions PKG-02; customer support PKG-16; finance control PKG-15. |
| Responsibility boundaries | Does not fabricate evidence/claims, mass-produce low-quality AI SEO, or launch every social channel. |
| Mandatory deliverable families | Channel hypotheses/tests; primary-engine decision; partner/outreach packs; high-value content; referral; communication plans; performance reports. |
| Lifecycle obligations | Minimal before validation; controlled recruitment at L3; pilot channel tests; required launch and Year-1 operation. |
| Interfaces | Consumes product/brand/legal/evidence/budget; supplies qualified demand/channel evidence/communications to product, analytics, customer operations. |
| Inputs | Positioning, approved claims, brand assets, target cohort, channel evidence, budget, capacity/support constraints. |
| Outputs | Approved assets/outreach, channel pipeline, qualified activations, measured economics/effort, communication records. |
| Primary owner/authority | Growth / Communications / Partnerships |
| AI autonomy target | A3 for research/content/outreach preparation and measurement; A2 for public publishing/outreach; A1 for contracts/endorsements/material spend |
| Human authority boundaries | Partner contracts/endorsements, public launch messages, sensitive incident communication, paid-spend approval, strategic channel commitment. |
| Quality requirements | Original high-intent value; claims/source review; qualified activation not vanity reach; effort/cost measured; $20-50 monthly discretionary cap. |
| Acceptance/success criteria | Tests have hypotheses/caps/denominators; one primary engine selected from evidence; unsupported channels/content stopped; claims remain accurate. |
| KPIs/decision signals | Qualified starts/activation/persistence by source; effort; cash spend; support burden; partner conversion; content-to-value conversion. |
| Risks | Channel sprawl, school trust barriers, mass AI SEO, paid CAC incompatibility, misleading claims, unmeasured founder labor. |
| Triggers | Product/pilot evidence; channel threshold; new market/locale; reputation/incident; budget/operational capacity change. |
| Dependencies | PKG-02/03/04/05/06/11/15/16. |
| Evidence requirements | Channel protocol, source-tagged aggregate funnel, content/source review, outreach log, cost/effort calculation, decision record. |
| Condition for deliberate minimalism | Reserve priority handles; produce a small number of exceptional first-phone resources; run one primary and at most one challenger. |

### PKG-15 - Finance, Cost, Vendor & Administration

| Charter field | Definition |
| --- | --- |
| Startup relevance | Mandatory lean control |
| Purpose | Keep cash, costs, vendors, payments, records, renewals, and formalization decisions controlled with minimal administration. |
| Business/customer outcome | The bootstrapped service remains financially visible and sustainable without fundraising work or unnecessary corporate overhead. |
| Scope | Budget/scenarios; cost alerts; bookkeeping/reconciliation; supporter model/payment operations; vendors/procurement/renewals/exit; tax/admin/insurance assessment; asset ownership; formalization triggers. |
| Explicit out of scope | GTM execution PKG-14; vendor security/privacy assessment PKG-04/10; architecture choices PKG-09; product model PKG-02. |
| Responsibility boundaries | No fundraising program for first two years absent new owner decision; no assumed revenue; no procurement without actual need. |
| Mandatory deliverable families | Budget/cost model; financial controls; vendor register/renewals; supporter/payment operation; accounting/tax/admin records; formalization review. |
| Lifecycle obligations | Lean from inception; required before spending/contracting/live payments and throughout Year 1. |
| Interfaces | Consumes resource/vendor/channel/support evidence; supplies budgets/cost constraints/payment/vendor status to product, platform, GTM, governance. |
| Inputs | Prices/terms, resource plans, actual invoices/transactions, supporter events, owner thresholds, legal obligations. |
| Outputs | Approved budget, budget-vs-actual, unit economics, vendor/renewal records, payment reconciliation, formalization decision evidence. |
| Primary owner/authority | Project Owner / Finance |
| AI autonomy target | A3 for budgets/reconciliation/research; A2 for vendor configuration; A0/A1 for payments, contracts, tax filings, identity and banking |
| Human authority boundaries | Bank/payment identity, payments/refunds, contracts, tax/legal filings, large spend, insurance purchase, organizational formalization. |
| Quality requirements | Every number sourced/calculated; cash vs owner time separate; scenarios not forecasts; renewals/exit known; spend tied to value/control. |
| Acceptance/success criteria | Transactions/costs reconcile; alerts/thresholds work; no unknown critical vendor/renewal; supporter terms/refunds correct; Year-1 close complete. |
| KPIs/decision signals | Monthly spend/cash; cost per activation/active user; support cost; supporter net/renewal; vendor anomalies; budget variance. |
| Risks | Cost creep, hidden owner labor, weak supporter economics, missed renewal/tax, vendor lock-in, payment friction, premature formalization. |
| Triggers | Spend/contract/payment; budget threshold; launch; 500 active users or earlier material revenue/staff/partner/risk trigger; Year-end. |
| Dependencies | PKG-02/04/09/11/13/14/16. |
| Evidence requirements | Invoices/receipts/reconciliation, budget model, vendor terms/review, payment/refund records, formalization decision. |
| Condition for deliberate minimalism | Track only cash, committed cost, material owner time, renewals, vendors, obligations, and decision thresholds. |

### PKG-16 - Customer Experience Operations & Lifecycle Management

| Charter field | Definition |
| --- | --- |
| Startup relevance | Direct customer value / self-service |
| Purpose | Operate the customer lifecycle through product-led self-service, automated troubleshooting, recovery, and evidence-driven improvement. |
| Business/customer outcome | Parents obtain and retain value without routine human support; repeated issues become product/UX/automation fixes. |
| Scope | Self-service help; automated verification/troubleshooting; recovery/removal/reset; issue intake/classification; exceptional escalation; feedback; persistence/lifecycle events; content loop; optional future account lifecycle only if validated. |
| Explicit out of scope | Core UX/content PKG-06; technical operations PKG-13; engineering fixes PKG-07/08; research PKG-03; legal safeguarding PKG-04. |
| Responsibility boundaries | No routine staffed concierge model after validation; no account-management bureaucracy; urgent safeguarding is signposted/escalated within policy. |
| Mandatory deliverable families | Self-service support design; troubleshooting/recovery; knowledge base; issue/root-cause loop; feedback; lifecycle/persistence; exceptional escalation. |
| Lifecycle obligations | Begins with validation support measurement, becomes required before pilot/launch, and continues through Year 1. |
| Interfaces | Consumes product/service/operations/legal knowledge; supplies root causes, lifecycle evidence, and user feedback to all improvement packages. |
| Inputs | Journey/help, service status, issue taxonomy, privacy limits, runbooks, feedback, lifecycle events. |
| Outputs | Resolved self-service paths, exceptional case evidence, root-cause backlog, updated knowledge, persistence/lifecycle reports. |
| Primary owner/authority | Customer Experience / Product Operations |
| AI autonomy target | A4 for self-service assistance, classification, routing, and lifecycle automation; A2 for exceptional diagnostics/communications; A1 for safeguarding or sensitive escalations |
| Human authority boundaries | Safeguarding/urgent escalation, exceptional complex incident, personal identity/consent, discretionary remedy, sensitive communication. |
| Quality requirements | Minimum data; immediate point-of-need help; automated verification; removal/recovery clarity; root-cause closure; no surveillance or addictive engagement. |
| Acceptance/success criteria | Top ordinary issues resolve without human intervention; repeated case rate falls after fixes; exceptional cases are bounded and privacy-safe. |
| KPIs/decision signals | Self-service resolution; substantial-help rate/minutes; repeat issues; protection persistence; removal/recovery success; feedback-to-fix time. |
| Risks | Hidden manual support, unclear limits, stale help, diagnostic data creep, unresolved false positives, account bureaucracy. |
| Triggers | Repeated friction/case; device/platform change; outage/filter issue; lifecycle event; support threshold; new locale. |
| Dependencies | PKG-02/04/06/07/08/11/12/13/14/15. |
| Evidence requirements | Synthetic/self-service tests, issue records, root-cause/release link, knowledge version, persistence report, diagnostic deletion proof. |
| Condition for deliberate minimalism | Prioritize in-product prevention, automated checks, concise help and recovery; owner handles only exceptional incidents. |
