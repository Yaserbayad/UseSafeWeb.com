# UseSafeWeb.com — Authoritative Business Evaluation State

**Last updated:** 2026-08-26  
**Canonical repository:** `Yaserbayad/UseSafeWeb.com`  
**Branch:** `main`

## Frozen project constraints

- This evaluation is for the business/product opportunity, not backend selection or infrastructure design.
- **AdGuard is the frozen backend technology decision** unless verified evidence establishes a critical blocker.
- The product follows the validated customer problem rather than presenting itself as DNS software.
- Core customer: parents/caregivers around the child's transition to independent internet use, centered on roughly ages 10–12 / first smartphone.
- Core JTBD: **SAFE INDEPENDENCE** — establish sensible, age-appropriate guardrails quickly without invasive surveillance or technical administration.
- Product identity: lightweight family digital-safety setup/orchestration around the first-smartphone transition.
- Core experience: **SET UP → PROTECT → GROW**. The MCP initially implements SET UP + minimal PROTECT only.
- Native Apple/Google/platform controls should be coordinated rather than recreated.
- Trust posture: **Simple guardrails. Clear limits. No invasive monitoring.** Minimum child data, no behavioral monetisation, no complete-safety claims, and explicit protection gaps.

## Master-plan status

1. Business Thesis & Evaluation Scope — COMPLETE
2. Customer Problem Validation — COMPLETE
3. Target Customer & Life-Stage Segmentation — COMPLETE
4. Jobs-to-Be-Done Definition — COMPLETE
5. Current Customer Behavior & Workarounds — COMPLETE
6. Pain Severity & Urgency Assessment — COMPLETE
7. Demand & Adoption Evidence — COMPLETE
8. Competitive & Substitute Landscape — COMPLETE
9. Market Gap / Unmet-Need Validation — COMPLETE
10. Differentiation & Unique Value Proposition — COMPLETE
11. Product Concept & Ideal Product Shape — COMPLETE
12. Minimum Compelling Product Definition — COMPLETE
13. Customer Experience & Onboarding Model — COMPLETE
14. Trust, Privacy & Safety Positioning — COMPLETE
15. Geographic Market Selection — COMPLETE
16. Market Size & Realistic Opportunity Assessment — **COMPLETE**
17. Customer Willingness-to-Pay / Free-Service Validation — **NEXT**
18–42. Pending

## Key frozen decisions through phase 15

### MCP

For a parent setting up a roughly 10–12-year-old child's first independently used smartphone, provide an immediate, registration-free guided setup that:

1. creates a minimal three-layer safety plan;
2. uses/coordinates the relevant native device safeguards rather than replacing them;
3. activates real AdGuard-backed baseline internet protection;
4. guides one genuinely relevant external service safeguard; and
5. finishes with a truthful Protection Map distinguishing system-verified, parent-confirmed, action-needed, and not-covered states.

Do not add GROW automation, surveillance, child accounts, comprehensive dashboards, full screen-time management, location/message monitoring, or broad feature development before demand is proven.

### Geography

- **First behavioral validation:** England.
- **Initial commercial market if validation succeeds:** United Kingdom.
- Current expansion order: United States, Australia, then Germany/broader European localisation, subject to later economics/legal/distribution phases.
- The external-service step remains service-agnostic because UK under-16 social-media restrictions are expected to change the platform context in 2027.

## Phase 16 — Market Size & Realistic Opportunity Assessment

### Decision

The correct market unit is a **replenishing annual first-smartphone / independent-internet life-stage flow**, not all UK parents or all UK children.

The UK is clearly large enough to run meaningful behavioral validation and could support a focused/niche service if adoption and economics later validate. Current evidence does **not** establish that UK-only demand is large enough for a venture-scale business, and exact-product adoption remains unknown.

### Population basis

The latest full UK age-specific official population series available during this phase is mid-2024; 2025 single-year estimates are not yet complete for the whole UK because Northern Ireland's 2025 release remains pending. For a transparent current target-stage proxy, use UK birth cohorts that roughly map to ages 10–12 in 2026:

- 2014 live births: **776,352**
- 2015 live births: **777,165**
- 2016 live births: **774,835**
- Three-year average: **776,117** children per cohort
- Approximate three-cohort 10–12 stage stock: **2,328,352** child-cohort places

This is a birth-cohort proxy, not an exact 2026 resident-population count; migration and deaths alter resident cohort sizes.

### Annual acquisition-event proxy

Ofcom 2026 reports:

- mobile-phone ownership: **56% at age 10**;
- mobile-phone ownership: **83% at age 11**;
- **96%** of children who own a mobile phone have a smartphone.

The 27 percentage-point ownership gap is **cross-sectional, not longitudinal**. It therefore must not be described as a measured annual first-phone acquisition rate.

Used only as a central event-flow proxy:

`776,117 × (83% − 56%) × 96% = 201,170`

So the project's central proxy is approximately **201,000 first-smartphone-transition child-events per year** around the strongest 10→11 trigger.

The true total annual number of first-smartphone acquisitions across the broader 9–12 window cannot currently be confirmed from longitudinal evidence.

### Behaviorally serviceable envelope

Ofcom 2026 reports:

- **35%** of all parents say they use parental controls specifically;
- **82%** of parents of 8–12-year-olds report device-management methods such as parental controls and screen-time limits.

Applying those two different behavior indicators to the 201,170 event-flow proxy gives a **heuristic behaviorally serviceable envelope**, not a demand forecast:

- Explicit parental-control indicator: `201,170 × 35% = 70,409` child-events/year.
- Broad 8–12 device-management indicator: `201,170 × 82% = 164,959` child-events/year.

Therefore use approximately **70,000–165,000 annual child-events** as the current behavioral serviceability envelope. It does not measure willingness to install UseSafeWeb or willingness to pay.

### Early reachable planning scenarios

Before distribution/CAC is evaluated, obtainable-market share cannot be confirmed. The following are scenario calculations only:

| Share of behavioral envelope | Annual activated-family-equivalent scenario* |
|---:|---:|
| 0.5% | ~350–825 |
| 1.0% | ~700–1,650 |
| 2.0% | ~1,400–3,300 |
| 5.0% | ~3,500–8,250 |

\*Child-events are not exactly unique households/families. Multiple same-age children can make child counts exceed unique families, while later siblings can create repeat lifecycle opportunities. Exact household deduplication is not currently established.

These scenarios are not forecasts and must not be used as expected sales/adoption numbers.

### Demographic pressure

- Average 2014–2016 birth cohort used above: **776,117**.
- UK births in the year to mid-2024: **662,100**, about **14.7% lower**.
- Provisional UK births in the year to mid-2025: **653,000**, about **15.9% lower**.

This indicates downward demographic pressure on future child cohorts if other factors are unchanged. It is **not** a forecast of an equivalent future market decline because migration and future fertility can alter cohort sizes.

### Scope exclusions from phase 16 sizing

Do not inflate the initial UK opportunity by counting:

- all UK parents;
- all children aged 0–17;
- the secondary 13–15 segment as primary acquisition TAM;
- schools/institutions;
- US/Australia/Germany expansion;
- multi-year retained users;
- siblings as separate immediate paying customers;
- unvalidated willingness to install or pay.

Revenue sizing is deliberately deferred until willingness-to-pay and business-model work (#17–#19).

### Phase-16 authoritative conclusion

- **Broad target-stage stock proxy:** ~2.33 million UK 10–12 child-cohort places.
- **Central annual first-smartphone transition proxy:** ~201,000 child-events/year.
- **Behaviorally serviceable envelope:** ~70,000–165,000 child-events/year.
- **Exact-product obtainable market:** **UNCONFIRMED**.
- **Realistic early scale before distribution evidence:** plan in hundreds to low-thousands of annual activations, not tens/hundreds of thousands.
- **UK market sufficiency:** large enough for validation and potentially a focused sustainable service; not yet proven sufficient for a large standalone business.

## Material open uncertainties after phase 16

1. Exact-product willingness to adopt remains unvalidated.
2. Willingness to pay versus expectation of free service remains unknown.
3. Child-event counts are not identical to unique households.
4. The 27-point age ownership gap is not longitudinal acquisition evidence.
5. Distribution/reachable share remains unknown until phase 20.
6. Retention and multi-year accumulated user base remain unknown until phase 21.
7. Economics/revenue cannot be responsibly calculated before phases 17–19.

## Next authoritative step

**Phase 17 — Customer Willingness-to-Pay / Free-Service Validation.**

Determine whether the exact target parent expects this orchestration service to be free, will pay for it, or will support it through another funding mechanism. Separate stated willingness from behavioral/payment evidence and determine the strongest price/free hypotheses to validate before business-model selection.

## Primary evidence used for phase 16

- ONS, UK live births 2000–2016: https://www.ons.gov.uk/aboutus/transparencyandgovernance/freedomofinformationfoi/annualbirthratesfrom2000to2016
- ONS, UK mid-2024 population estimates: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2024
- ONS, provisional UK mid-2025 population estimate: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/provisionalpopulationestimatefortheuk/latest
- Ofcom, Children and Parents Media Use and Attitudes Report 2025–6: https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/media-literacy-research/children/2026-children-and-parents-report/children-and-parents-media-use-and-attitudes-report-2025-6.pdf
- DfE, Parent, pupil and learner voice: March 2026: https://www.gov.uk/government/publications/parent-pupil-and-learner-voice-omnibus-surveys-for-2025-to-2026/parent-pupil-and-learner-voice-march-2026
