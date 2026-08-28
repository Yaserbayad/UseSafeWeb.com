# TSK-0138 — Unresolved Product Assumptions and Owner Decisions Register

**Task:** TSK-0138 — Register unresolved product assumptions and owner decisions  
**Acceptance:** ACC-0138  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** ACTIVE PROVISIONAL DECISION CONTROL / INTERNAL  
**Date:** 2026-08-28  
**Authority:** TSK-0141 + TSK-0139 + DEC-0050/CR-0003  

## 1. Control rule

Every unresolved item in the provisional L4 path must have:

1. a named accountable owner/decision authority;
2. the exact evidence needed to resolve it;
3. a deterministic deadline, gate or trigger;
4. a conservative safe default while unresolved;
5. the consequence of continued deferral;
6. a clear statement of whether AI/engineering may prepare evidence or whether a human decision is required.

**AI/engineering may not silently make a Project Owner decision, convert missing behavioral evidence into a positive result, activate a deferred exception, or treat a safe default as proof that the underlying assumption is true.**

## 2. Settled decisions that are not open assumptions

The following are current authority and must not be re-opened merely because L3 is deferred:

- `UseSafeWeb.com` public identity/domain — DEC-0001;
- UseSafeWeb First Phone Safety Setup framing — DEC-0002;
- AdGuard backend — DEC-0003;
- encrypted DNS requirement — DEC-0004;
- SAFE INDEPENDENCE job framing — DEC-0007;
- non-surveillance/simple-guardrails trust posture — DEC-0008;
- native-first → baseline protection → one relevant service → truthful Protection Map operating shape — DEC-0009, subject to later behavioral correction but not silent scope expansion;
- accountless-first — DEC-0042 / TSK-0146;
- brand/UX as first-class work — DEC-0044;
- English/Turkish/Arabic technical content capability with separate market activation — DEC-0045;
- self-service operating model — DEC-0048;
- L3 real-participant deferral/provisional L4 authorization — DEC-0050 through 2027-08-27 unless superseded.

A current decision can still be reopened by its own defined trigger or later explicit owner authority; it is not an unresolved assumption merely because future evidence could eventually change it.

## 3. Unresolved assumptions and decisions

| ID | Unresolved assumption / decision | Current state | Accountable owner / authority | Evidence needed to resolve | Deadline / gate / trigger | Safe default while unresolved | Consequence of deferral | AI / engineering authority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UPA-001 | Real parents at the first-phone transition will complete enough of the proposed journey for the orchestration to be worthwhile | **UNKNOWN / RSK-0002** | Project Owner + Product/Research evidence | Authorized real L3 cohort; frozen completion definition; Wave A/B results; abandonment and contrary evidence | **2027-08-27 or earlier L3 reactivation; LG-05** | Keep product minimum, reversible and provisional; do not build/claim around assumed high completion | LG-05 stays non-PASS; any downstream task needing this result remains deferred; provisional scope may later be reworked/pivoted | AI may prepare designs/measurement only; may not decide the behavioral outcome |
| UPA-002 | The current parent/caregiver first-phone cohort definition is the right target segment | **PROVISIONAL / UNVALIDATED** | Project Owner; Product/Research prepares evidence | Real qualification funnel, completion/value by cohort, contrary-segment evidence | L3 reactivation / LG-05 or explicit owner segment review | Design for the frozen current segment without claiming demand/fit | Segment remains assumption; no expansion/generalisation | AI may design to current segment; only owner can materially change target segment |
| UPA-003 | Native-safeguards-first reduces duplication rather than adding work | **UNKNOWN** | Product/Research; Project Owner at gate | Real abandonment/duplication reasons, assistance, already-configured frequency, qualitative/structured evidence | L3 / LG-05 | Preserve skip/already-configured behavior; remove avoidable steps; label rationale provisional | Cannot claim orchestration advantage over native controls | AI may simplify reversibly; cannot claim observed reduction in work |
| UPA-004 | One relevant external/service safeguard creates meaningful incremental value beyond DNS/native controls | **UNKNOWN** | Product/Research; Project Owner at gate | Real incremental non-DNS safeguard completion/value and relevance evidence | L3 / LG-05 | Keep exactly one relevant service and allow not-applicable/not-covered | Do not broaden service catalogue; value proposition remains uncertain | AI may prepare one-service flows; cannot expand catalogue based on assumption |
| UPA-005 | Parents understand the Protection Map and material coverage limits | **UNKNOWN** | UX/Product Research; Project Owner for material claims changes | Real comprehension testing under the approved protocol or later authorized user research | L3/LG-05; later LG-06 usability evidence where applicable | Use simplest truthful state labels; separate verified vs parent-confirmed; surface uncertainty | Any task whose AC requires real comprehension stays deferred; no comprehension claim | AI may refine wording synthetically; cannot mark comprehension proven |
| UPA-006 | Parents can self-serve the setup without excessive live assistance | **UNKNOWN** | Product/UX + Operations; Project Owner if operating model changes | Real assistance minutes/categories, failure clusters, later usability testing | L3/LG-05 and applicable LG-06 evidence | Preserve self-service design, explicit help/recovery, minimal steps; no routine staffed-support build | Routine human-support requirement remains unsupported; difficult paths stay hypotheses | AI may automate/simplify; cannot decide to create a staffed support model without EXC-0008/owner authority |
| UPA-007 | Baseline protection remains active after 14 days often enough to support the persistence proposition | **UNKNOWN** | Product/Research | Real authorized follow-up state and removal/breakage causes | L3/LG-05 | Design easy recovery/removal and avoid engagement gimmicks; do not claim persistence | Persistence/value claims remain unavailable; downstream evidence tasks stay deferred | AI cannot infer persistence from technical uptime or synthetic rehearsal |
| UPA-008 | Real false-positive/compatibility burden is acceptable for the target cohort | **UNKNOWN beyond bounded technical/synthetic tests** | Product/Network/Support; Project Owner if material scope change | Real issue rate/categories, network/platform patterns, intervention burden and safe resolutions | L3/LG-05; later pilot gates | Keep conservative filtering, narrow reversible exception path, privacy-minimal diagnostics and truthful unsupported states | No cohort reliability/supportability claim; product path may need reduction later | AI/network may run synthetic regression and prepare fixes; cannot fabricate real burden rate |
| UPA-009 | Accountless-first remains sufficient once users need persistence, multi-device management, recovery or supporter features | **DEFERRED EXCEPTION / EXC-0001** | Project Owner | Validated persistence/multi-device/recovery/supporter need; proof accountless alternatives inadequate; privacy/security/architecture/UX review | Exact EXC-0001 trigger; later owner decision | **No mandatory account/authentication/persistent dashboard** | Persistent features stay out; design must deliver immediate value accountlessly | AI may research/prepare alternatives; cannot activate account/dashboard/auth vendor |
| UPA-010 | A persistent parent dashboard/device list is necessary | **DEFERRED EXCEPTION / unproven** | Project Owner | Same EXC-0001 evidence plus exact dashboard job/necessity and minimisation case | EXC-0001 | No persistent dashboard/device list | Dashboard-dependent tasks remain deferred or must be reconciled to accountless baseline | AI cannot restore historical dashboard-first architecture |
| UPA-011 | The current public/product language and brand system produces trust and clarity with real parents | **UNKNOWN beyond owner/design review** | Project Owner for brand approval; Brand/UX research for evidence | Current brand/design work plus later authorized usability/trust evidence | Applicable L4 task/owner gate; real-user evidence when required | Use calm, non-alarmist, non-technical, truthful language; avoid irreversible/high-volume brand production before owner approval | Brand preference/trust claims stay provisional; HUMAN_ONLY approval remains required where WBS says so | AI may develop/evaluate directions; cannot fabricate user preference or owner approval |
| UPA-012 | English/Turkish/Arabic technical product capability should correspond to official market support outside the UK | **NO — activation unresolved** | Project Owner via LG-16 | Named-market research; current legal/privacy/safeguarding/support/channel/content evidence | LG-16 per market | Languages may exist technically; **official non-UK activation = NO** | No non-UK official targeting/support/legal claim | AI may prepare locale capability; cannot activate market or claim official support |
| UPA-013 | Optional supporter payment should be enabled | **CONDITIONAL / NOT AUTHORIZED NOW** | Project Owner | Demonstrated product value; current consumer/tax/privacy/security/provider readiness; eligible cohort; provider reconciliation | DEC-0011/DEC-0029 later gate/owner authorization | Core free; no payment ask or checkout in current provisional minimum | No revenue/payment evidence; checkout work remains outside current authorization | AI may prepare later analysis; cannot activate Stripe/PayPal/payment collection or spend |
| UPA-014 | High availability / additional DNS nodes are necessary | **DEFERRED EXCEPTION / EXC-0004** | Project Owner | Measured outage/capacity/RTO/SLA or risk evidence justifying complexity/cost | EXC-0004 trigger | Single lean recoverable topology; approximately 30-minute recovery model | No HA build/cost; recovery remains the protection strategy | AI may monitor/analyse; cannot add HA/multi-node architecture without trigger/authority |
| UPA-015 | The deferred legal/privacy/contact conditions are satisfied for real participants or public operation | **UNRESOLVED / DEFERRED** | Project Owner / applicable legal/privacy authority | Current LIA/DPIA approval; notice/contact release; ICO/UK-representative outcome or verified non-applicability; any other current mandatory evidence | 2027-08-27 or earlier reactivation; LG-03 and later applicable gates | No real participants; no legal-compliance attestation; no public launch based on the deferral | Participant/public actions remain fenced | AI may prepare non-consequential material; cannot make legal attestations, appointments, payments or treat the hold as compliance |
| UPA-016 | L4 provisional definition/design is sufficient to pass LG-06 and enter architecture/build | **NO CURRENT DECISION / NOT AUTHORIZED BY CR-0003** | Project Owner at LG-06 and later gates | Every applicable LG-06 evidence item, including any required usability/comprehension evidence; explicit deviations and risk disposition | LG-06 | L4 artifacts may progress internally; **LG-06 remains non-PASS until separately decided with evidence** | No L5/L6 progression by inference | AI may prepare eligible L4 evidence; cannot self-certify LG-06 or build authority |
| UPA-017 | Integrated product build may start before real behavioral validation | **NO under current CON-0025/DEC-0050** | Project Owner only through a new material baseline change, subject to actual safety/technical constraints | Explicit new owner instruction plus impact analysis and updated gates/acceptance; ideally real behavioral evidence | Before any L5/L6/build dispatch | No integrated build | Build tasks remain unavailable | Engineering/AI must stop at the build boundary |
| UPA-018 | Public UK launch may occur | **BLOCKED / NOT AUTHORIZED** | Project Owner | Later real product/pilot/legal/privacy/security/operations/economics evidence and LG-11/LG-12/LG-13 | LG-11→LG-13 | No public launch | Project remains internal/preparatory | AI cannot launch or publish consequential production activation without required authority |
| UPA-019 | Deferred advanced scope (GROW, native app, child account, school portal, broad DNS admin, community/UGC) should enter the product | **DEFERRED / EXC-0005** | Project Owner | Validated material customer value plus safety/privacy/security/cost/support evidence and explicit scope decision | EXC-0005 | Exclude | Keeps minimum scope small; no work package depends on speculative expansion | AI cannot add these features as “helpful” extras |
| UPA-020 | Real user evidence later contradicts a provisional L4 PASS | **FUTURE RECONCILIATION CONDITION** | Project Governance + owner where decision authority is required | Direct current user evidence and trace to affected assumptions/tasks/ACs | Any new contradictory evidence; mandatory at L3 reactivation/expiry | Current provisional PASS may stand only while its evidence remains valid; mark reliance explicitly | Affected PASS must reopen; no sunk-cost protection | AI must surface contradiction and reopen affected work; cannot reconcile it away |

## 4. Decision-deadline hierarchy

Where several triggers could resolve an item, the **earliest applicable** trigger controls:

1. immediate safety/security/privacy/technical contradiction;
2. new explicit Project Owner instruction;
3. earlier authorized real-user evidence;
4. the relevant named gate/exception trigger;
5. **2027-08-27** CR-0003/L3 reactivation deadline.

The 2027-08-27 date is a review/reactivation boundary, not evidence that any unresolved assumption becomes true on that date.

## 5. Safe-default principles

Until evidence resolves an assumption:

- choose the smaller/reversible/accountless/privacy-minimal design;
- prefer `unknown`, `not covered`, `action needed` or equivalent truthful states to false certainty;
- do not add persistent identity or data solely for implementation convenience;
- do not broaden product/service/market/support scope;
- do not create a human-support operation to hide UX friction;
- do not build or launch merely because internal design artifacts exist;
- keep HUMAN_ONLY/HUMAN_APPROVAL_REQUIRED authority intact;
- preserve the ability to delete/rework provisional design after real evidence.

## 6. Escalation rule

Escalate to the Project Owner only when an actual current decision is required to proceed safely and the WBS/action authority says the act is owner-controlled. Do **not** escalate merely because a future owner decision exists in this register; continue every eligible AUTO_ALLOWED task until its first genuine boundary.

If the safe default lets internal L4 work continue without prejudicing the future decision, continue under the safe default and keep the item open.

## 7. ACC-0138 traceability

ACC-0138 requires each item to have an owner, evidence needed, decision deadline/gate, safe default and consequence of deferral, while ensuring no critical owner decision is silently made by engineering.

- Every `UPA-*` row contains all five required control fields plus explicit AI/engineering authority.
- Owner-only decisions are explicitly named and fenced.
- Behavioral gaps remain UNKNOWN rather than inferred from synthetic evidence.
- Legal/participant/build/launch boundaries default to **NO / DEFER / NOT AUTHORIZED** until their actual evidence and authority exist.
- The escalation rule allows autonomous preparation to continue without turning future decisions into unnecessary interruptions.

**TSK-0138 result: PASS candidate subject to independent verification and runtime read-back.**
