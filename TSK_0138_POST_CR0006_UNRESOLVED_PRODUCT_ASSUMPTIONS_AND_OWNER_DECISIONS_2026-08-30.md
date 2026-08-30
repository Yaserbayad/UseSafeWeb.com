# TSK-0138 — Current Unresolved Product Assumptions and Owner Decisions

**Task:** TSK-0138 — Register unresolved product assumptions and owner decisions  
**Acceptance:** ACC-0138  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** CURRENT POST-CR-0006 DECISION CONTROL / INTERNAL  
**Date:** 2026-08-30  
**Authority:** current TSK-0141 PASS + DEC-0052/CR-0005 + DEC-0053/CR-0006 + current legal/launch/payment/exception controls  

## 1. Control rule

Every unresolved item must carry: accountable owner/authority; evidence needed; deterministic deadline/gate/trigger; conservative safe default; deferral consequence; and explicit AI/engineering authority. AI/engineering may prepare evidence and execute AUTO_ALLOWED work but may not fabricate behavioral evidence, silently make owner decisions, infer a gate PASS, activate consequential participant/public/payment/legal action, or expand product scope beyond current authority.

## 2. Current settled decisions — not open assumptions

The following are current authority and are not unresolved merely because future evidence may later trigger reconsideration:

- UseSafeWeb.com identity/domain, First Phone Safety Setup framing, AdGuard backend, encrypted DNS, SAFE INDEPENDENCE, non-surveillance/simple-guardrails posture, native-first/baseline-protection/one-relevant-service/truthful-Protection-Map product shape, multilingual capability with separately gated market activation, self-service operating model, and constrained/earned-first GTM remain governed by their current decisions.
- **DEC-0052 / CR-0005:** no parent/user/participant validation is required or permitted as a pre-product gate. L4-L7 product/architecture/build/integrated verification proceeds first; first real-user validation is L8 only after LG-09 PASS. No behavioral evidence is inferred from this sequencing choice.
- **DEC-0053 / CR-0006:** Version 1 includes an **optional parent account**, secure sign-in/session requirements, minimum parent/device ownership persistence and a lightweight dashboard/device-management experience; the complete core setup/protection journey remains usable without login.
- `EXC-0001` is **ACTIVATED_V1_SCOPE** for that bounded account capability. Mandatory login, browsing/query/activity history, child accounts/profiles and unrestricted/raw DNS administration remain outside the activation.
- Google/Firebase remains the planned initial authentication route only, subject to its current L5 vendor/privacy/security/architecture verification; this register does not approve that downstream gate.
- Integrated L6 build is no longer prohibited merely because behavioral evidence is absent; it still requires current product/architecture/build-entry gate evidence, including LG-06 and LG-07 as required by DEC-0024/DEC-0052.

## 3. Historical items resolved or superseded by current owner authority

| Historical ID | Prior issue | Current disposition |
| --- | --- | --- |
| UPA-009 | Whether accountless-first is sufficient if persistence/multi-device/recovery is needed | **RESOLVED/SUPERSEDED:** DEC-0053 requires an optional V1 account while preserving the complete accountless core. Account usefulness remains behaviorally unvalidated, but account inclusion is not an open owner decision. |
| UPA-010 | Whether a persistent parent dashboard/device list is necessary | **RESOLVED/SUPERSEDED:** DEC-0053 requires a bounded lightweight V1 dashboard/device-management experience. Expansion beyond that minimum remains unauthorized without later evidence/owner change. |
| UPA-017 | Whether integrated product build must wait for real behavioral validation | **RESOLVED/SUPERSEDED:** DEC-0052 says **no**. Build/integrated verification proceeds before real-user testing, subject to current LG-06/LG-07 and all other applicable product/architecture/security/privacy/build gates. |

The historical 2026-08-28 register remains evidence of the earlier state only. Its account-deferral and pre-build-human-validation clauses no longer control current execution.

## 4. Current unresolved assumptions and decisions

| ID | Unresolved assumption / decision | Current state | Accountable owner / authority | Evidence needed to resolve | Deadline / gate / trigger | Safe default while unresolved | Consequence of deferral | AI / engineering authority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UPA-001 | Real parents at the first-phone transition will complete enough of the integrated journey for the orchestration to be worthwhile | **UNKNOWN / RSK-0002** | Project Owner + Product/Research evidence | Authorized L8 real-user cohort after LG-09; frozen completion definition; abandonment/contrary evidence | L8 after LG-09 and all participant/legal prerequisites | Keep product minimum, reversible and provisional; make no behavioral-value claim | Later validation/launch/value decisions remain unavailable; product may require rework | AI may design/measure synthetically; cannot decide the behavioral outcome |
| UPA-002 | The current parent/caregiver first-phone cohort is the right target segment | **PROVISIONAL / UNVALIDATED** | Project Owner; Product/Research prepares evidence | L8 qualification/completion/value by cohort plus contrary-segment evidence | L8 after LG-09 or earlier explicit owner segment review | Design to frozen current segment without claiming fit/demand | No segment expansion/generalisation | AI may design to current segment; only owner changes strategic segment |
| UPA-003 | Native-safeguards-first reduces duplication rather than adding work | **UNKNOWN** | Product/Research; owner for material product-shape change | L8 task completion, duplication/abandonment/assistance evidence | L8 after LG-09 | Preserve skip/already-configured behavior and minimize avoidable steps | No observed-efficiency claim; later flow may need rework | AI may simplify reversibly; cannot claim observed reduction |
| UPA-004 | One relevant service safeguard creates meaningful incremental value beyond DNS/native controls | **UNKNOWN** | Product/Research; owner for scope change | L8 service-relevance/completion/value evidence | L8 after LG-09 | Keep exactly one genuinely relevant service and allow not-applicable/not-covered | Do not broaden service catalogue; value proposition remains provisional | AI may prepare/test one-service flows; cannot expand catalogue by assumption |
| UPA-005 | Parents understand the Protection Map and material coverage limits | **UNKNOWN** | UX/Product Research; owner for material claim/model change | L8 comprehension/task evidence and contrary findings | L8 after LG-09 | Use simplest truthful labels; separate verified/parent-confirmed/unknown/not-covered states | No comprehension claim; later wording/model may require rework | AI may run automated/accessibility/heuristic checks; cannot fabricate user comprehension |
| UPA-006 | Parents can self-serve setup without excessive live assistance | **UNKNOWN** | Product/UX + Operations; owner if operating model changes | L8 assistance minutes/categories, failure clusters, recovery success | L8 after LG-09 | Preserve self-service, in-product help/recovery, exceptional escalation only | No claim of low support burden; repeated ordinary help must become product/UX work | AI may automate/simplify; cannot create routine staffed support without EXC-0008/owner authority |
| UPA-007 | Protection remains active after 14 days often enough to support persistence/value claims | **UNKNOWN** | Product/Research | L8 authorized follow-up state and removal/breakage causes | L8 after LG-09 | Design easy recovery/removal; optimize persistence rather than engagement; make no persistence claim | Retention/value claims remain unavailable | AI cannot infer human persistence from technical uptime or synthetic tests |
| UPA-008 | Real false-positive/compatibility burden is acceptable for the target cohort | **UNKNOWN beyond current technical/synthetic evidence** | Product/Network/Support; owner for material scope/policy change | L8 issue rate/categories, platform/network patterns, intervention burden and safe resolutions | L8 after LG-09; earlier verified critical blocker immediately controls | Conservative filtering, narrow reversible exception path, privacy-minimal diagnostics, truthful unsupported states | No cohort supportability/reliability claim; product/filtering path may need reduction | AI/network may run synthetic regression and fix proven defects; cannot fabricate real burden rate |
| UPA-011 | Current public/product language and brand system produces trust and clarity with real parents | **UNKNOWN beyond owner/design/automated review** | Project Owner for brand decisions; Brand/UX research for evidence | Current design/accessibility evidence plus L8 trust/comprehension evidence | Current HUMAN_ONLY brand decisions where applicable; real-user evidence in L8 | Calm, non-alarmist, truthful language; avoid unsupported trust claims | Brand preference/trust remains provisional | AI may develop/evaluate directions; cannot fabricate user preference or owner approval |
| UPA-012 | Technical English/Turkish/Arabic capability should correspond to official non-UK market support | **NO — activation unresolved** | Project Owner via LG-16 | Named-market legal/privacy/safeguarding/support/channel/content evidence | LG-16 per market | Languages may exist technically; official non-UK activation remains NO | No non-UK official targeting/support/legal commitment | AI may prepare locale capability; cannot activate market |
| UPA-013 | Optional supporter payment should be enabled | **CONDITIONAL / NOT AUTHORIZED NOW** | Project Owner | Demonstrated product value plus current consumer/tax/privacy/security/provider readiness and eligible cohort | DEC-0011/DEC-0029 later gate/owner authorization | Core free; no payment ask/checkout until gate/authority | No revenue/payment evidence; consequential payment work remains fenced | AI may prepare later analysis/tests; cannot activate payment collection or spend |
| UPA-014 | High availability/additional DNS nodes are necessary | **DEFERRED EXCEPTION / EXC-0004** | Project Owner | Measured outage/capacity/RTO/SLA/risk evidence justifying added complexity/cost | EXC-0004 trigger | Single lean recoverable topology and current recovery model | No HA build/cost | AI may monitor/analyse; cannot add HA architecture without trigger/authority |
| UPA-015 | Deferred legal/privacy/contact conditions are satisfied for real participants or public operation | **UNRESOLVED / OWNER-DEFERRED** | Project Owner / applicable legal/privacy authority | Current required legal/privacy/contact/registration/representation/notice evidence or verified non-applicability | 2027-08-27 or earlier explicit owner reactivation; before any applicable participant/public action | No real participant/public/legal-compliance attestation while prerequisites remain unresolved | Participant/public/legal actions stay fenced | AI may prepare non-consequential work; cannot make legal attestations, appointments or payments |
| UPA-016 | The revised dual-mode L4 baseline is ready to pass LG-06 | **NOT YET DECIDED** | Project Owner via TSK-0052 / LG-06 | Every current applicable LG-06/ACC-0052 item including account-inclusive requirements/UX/prototype/accessibility/self-service/traceability and unresolved-risk disposition | LG-06 after revised account-inclusive L4 evidence is complete | LG-06 stays non-PASS; continue eligible AUTO_ALLOWED L4 work | Work requiring LG-06 remains unavailable | AI may prepare/verify evidence; cannot self-certify HUMAN_ONLY LG-06 |
| UPA-018 | Public UK launch may occur | **BLOCKED / NOT AUTHORIZED** | Project Owner | Later L8+ product/persistence/support/reliability/security/privacy/legal/operations/economics evidence plus LG-11/LG-12/LG-13 | LG-11 → LG-13 | No public launch | Project remains internal/preparatory | AI cannot launch consequential production/public operation without required authority |
| UPA-019 | Deferred advanced scope (GROW, native app, child account/profile, school portal, broad DNS admin, community/UGC) should enter the product | **DEFERRED / EXC-0005** | Project Owner | Validated material customer value plus safety/privacy/security/cost/support evidence and explicit scope decision | EXC-0005 | Exclude | Keeps V1 bounded; no speculative expansion | AI cannot add these features as helpful extras |
| UPA-020 | Future direct user/production evidence contradicts a current provisional PASS | **FUTURE RECONCILIATION CONDITION** | Project Governance + owner where decision authority is required | Direct current contradictory evidence traced to affected tasks/ACs/decisions | Any new contradiction; mandatory when L8 evidence arrives | Preserve current PASS only while evidence still proves current semantics | Affected PASS/gate must reopen; no sunk-cost protection | AI must surface contradiction and reopen affected work; cannot reconcile it away |

## 5. Decision-deadline hierarchy

Earliest applicable trigger controls:

1. immediate safety/security/privacy/legal/technical contradiction;
2. new explicit Project Owner instruction;
3. required current gate/acceptance evidence;
4. L8 real-user evidence after LG-09 when legally/operationally eligible;
5. named exception/market/payment/launch trigger;
6. 2027-08-27 owner legal-hold review/reactivation boundary where still applicable.

No date or gate makes an unknown assumption true automatically.

## 6. Safe-default principles

Until evidence resolves an assumption:

- choose the smaller, reversible, privacy-minimal implementation inside the **current dual-mode V1 scope**;
- preserve the complete accountless core while implementing only the minimum authorized optional-account/dashboard capability;
- never convert account ownership into proof of DNS/protection state;
- prefer truthful unknown/not-covered/action-needed states to false certainty;
- do not add browsing/query/activity history, child profiles or broad/raw DNS administration;
- do not broaden product/service/market/support/payment scope without its trigger and authority;
- do not create routine staffed support to hide UX defects;
- continue current L4-L7 automated/technical/product work without fabricating pre-product human evidence;
- keep HUMAN_ONLY/HUMAN_APPROVAL_REQUIRED decisions intact.

## 7. ACC-0138 traceability

ACC-0138 requires every open item to have an owner, evidence needed, decision deadline/gate, safe default and deferral consequence, while preventing engineering from silently making critical owner decisions.

- Every current `UPA-*` row above carries all required control fields and explicit AI/engineering authority.
- Historical UPA-009/010/017 are explicitly removed from the open set because DEC-0053/DEC-0052 resolved or superseded them.
- Real-behavior unknowns are moved to the current L8-after-LG-09 validation boundary rather than treated as pre-product blockers or fabricated evidence.
- Account inclusion is frozen, but detailed account requirements/vendor/privacy/security/architecture/UX/build acceptance remains owned by downstream tasks and gates.
- Legal/participant/public/payment/launch and HUMAN_ONLY boundaries remain explicit.

**TSK-0138 result: PASS candidate subject to independent verification and canonical runtime read-back.**
