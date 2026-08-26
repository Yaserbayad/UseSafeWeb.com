# UseSafeWeb.com — Business Evaluation Phases 17–22

**Date:** 2026-08-26  
**Authority:** Canonical project business-evaluation continuation.  
**Depends on:** `BUSINESS_EVALUATION.md` through phase 16.

## Phase 17 — Customer Willingness-to-Pay / Free-Service Validation — COMPLETE

### Evidence

Current substitutes create a strong zero-price anchor:

- Apple parental controls are built into iPhone/iPad/Mac through Screen Time and Family Sharing.
- Google Family Link and child Google accounts can be created/managed at no separate charge.
- CleanBrowsing offers an accountless free Family Filter.
- NextDNS offers a free tier and currently prices Personal Pro in GBP at **£1.79/month or £17.90/year**.

Paid parental-control products prove that some parents pay for broader functionality, but they are materially more feature-rich than the UseSafeWeb MCP:

- Qustodio: Basic **$59.95/year**; Complete **$104.95/year**.
- CleanBrowsing Family paid plan: **$75/year**.
- Canopy: **$99.99/year** for one device and higher plans above that.
- Bark sells monitoring/control subscriptions at materially higher prices, but Bark is not currently a UK consumer app market comparator and is surveillance-oriented, unlike UseSafeWeb.

### Decision

**Do not paywall the MCP or require a card/trial before value.** Exact willingness to pay for UseSafeWeb is unconfirmed.

Strongest behavioral price hypothesis to test after successful activation:

- **Use free:** full MCP remains available.
- **Support annually:** **£20/year**.
- **Support monthly:** **£2/month**.

The supporter payment must not unlock core safety functionality during validation. It tests whether the service creates enough perceived public/family value that some users voluntarily fund it.

Do not infer willingness from survey answers. The required evidence is actual completed payment behavior from qualified, activated first-phone parents.

### Interpretation thresholds

These are project decision thresholds derived from the phase-19 economics below, not industry benchmarks:

- **<5% supporter conversion at ~£20/year:** supporter funding is weak as a primary model at early scale.
- **5–10%:** useful supplementary funding but probably insufficient for a labor-heavy operation.
- **10–20%:** potentially viable for a highly automated, low-overhead service.
- **>20%:** strong supporter behavior, subject to renewal and support-cost validation.

## Phase 18 — Business Model & Revenue/Funding Options — COMPLETE

### Options evaluated

1. **Hard subscription for core safety:** rejected for initial launch. Free native controls and free DNS alternatives create a strong substitute set, while exact-product demand is still unproven.
2. **Conventional freemium with core safety features gated:** rejected initially. It would distort the MCP and create pressure to manufacture premium features before demand is proven.
3. **Free core + voluntary supporter contribution:** **SELECTED initial model**.
4. **One-time setup fee:** not selected initially; it adds friction at the acquisition trigger while the service incurs ongoing protection costs.
5. **Institutional sponsorship / grants / B2B2C funding:** viable later as supplementary funding, but should not be required to validate the consumer proposition.
6. **Advertising / sale or monetisation of child/family behavioral data:** prohibited by phase 14.

### Authoritative initial model

> **Free-to-use family safety service with optional supporter funding.**

- Full MCP safety outcome stays free.
- Support contribution is offered only after the parent has received value.
- Initial supporter hypothesis: £20/year or £2/month.
- No essential protection advantage for paying users during validation.
- No behavioral advertising, child-data monetisation, or surveillance upsell.
- Future paid convenience/advanced features may only be considered after demand is proven and only if they represent genuine incremental value/cost rather than deliberately weakening the free safety baseline.

This model is selected because it best preserves adoption, trust, and the original public-benefit intent while allowing real payment behavior to test sustainability.

## Phase 19 — Unit Economics & Cost Sustainability — COMPLETE

### Confirmed payment economics

Stripe UK standard domestic-card pricing is currently **1.5% + £0.20 per successful charge**.

For a £20 annual supporter payment:

`£20 - (1.5% × £20) - £0.20 = £19.50 net before tax/refunds/other costs.`

At the selected supporter price, average annual net revenue per activated family is therefore:

- 5% supporter conversion: `0.05 × £19.50 = £0.975`.
- 10%: `0.10 × £19.50 = £1.95`.
- 20%: `0.20 × £19.50 = £3.90`.

### Hosting-cost reference, not architecture decision

OVHcloud UK currently lists a VPS-2 at **£7.55/month including VAT** with 4 vCores, 8 GB RAM, daily backup and unmetered traffic. This is used only as a current UK public infrastructure-cost reference; it is **not** a capacity claim or an approved production topology.

Annual reference costs:

- 1 VPS-2: `£7.55 × 12 = £90.60`.
- 2: `£181.20`.
- 3: `£271.80`.

At £19.50 net per annual supporter, approximately 14 supporters cover the three-VPS reference cost (`£271.80 / £19.50 = 13.94`) before all other costs.

This demonstrates that raw VPS hosting is unlikely to be the primary early economic risk. Actual AdGuard capacity, redundancy architecture, monitoring, email, domain, security, support, tax and other operating costs remain unverified and must not be inferred from this benchmark.

### Support/labor is the dominant economic uncertainty

The UK National Living Wage for adults 21+ is **£12.71/hour** from April 2026. Even at this conservative labor-cost floor:

- 5% supporter conversion produces £0.975 average net revenue per activation, equivalent to only about **4.6 minutes** of labor before infrastructure/other costs.
- 10% produces £1.95, about **9.2 minutes**.
- 20% produces £3.90, about **18.4 minutes**.

Therefore a supporter-funded model at this price requires the product to be highly self-service. Repeated live setup assistance would overwhelm the economics.

### Scale scenarios

At £20/year and £19.50 net/supporter:

| Annual activations | 5% supporters | 10% supporters | 20% supporters |
|---:|---:|---:|---:|
| 500 | £488 | £975 | £1,950 |
| 1,000 | £975 | £1,950 | £3,900 |
| 3,000 | £2,925 | £5,850 | £11,700 |
| 5,000 | £4,875 | £9,750 | £19,500 |

Rounded to nearest pound.

### Phase-19 conclusion

- **Infrastructure-level sustainability:** plausible at modest scale.
- **Full business sustainability:** unconfirmed because CAC, retention, support burden, tax/legal costs and actual production capacity are not yet known.
- **Primary economic risk:** human operations/support, not DNS compute cost.
- Supporter-only funding is plausible for a very lean service but cannot yet support a conventional staffed SaaS assumption.

## Phase 20 — Distribution & Customer-Acquisition Strategy — COMPLETE

### Direct evidence from the selected England cohort

The March 2026 DfE parent survey asked where parents would seek advice about screen/social-media use and online safety. Among primary parents:

- **School: 50%**
- **Family and friends: 46%**
- **Government sites: 45%**
- **Children's charities: 21%**
- **AI tools/apps: 20%**
- **Social media: 16%**

The product's acquisition trigger also coincides with the transition toward secondary school and the sharp 10→11 phone-ownership change established in phase 15.

### Authoritative initial distribution order

1. **School / primary-to-secondary transition channel — primary.** Provide a simple parent-facing first-phone safety resource/setup link that schools can include in transition communications, parent evenings or digital-safety material. The school is a distribution/trust channel, not the customer or technical administrator.
2. **Organic search / first-phone intent content — secondary.** Target the event itself (first phone, first smartphone, child phone setup, safe phone setup), not generic DNS or broad online-safety content.
3. **Referral / family-and-friend sharing — secondary.** The completed Protection Map/setup should be easy to recommend to another parent without referral incentives that compromise trust.
4. **Trusted safety organisations / charities / public-information referrals — later partnership channel.** Useful for credibility and reach after product evidence exists.
5. **Social media — supporting only.** Parent social-media reach may help, but DfE evidence places it well below schools, government sites and family/friends as an advice source.
6. **Paid performance advertising — deferred.** Current supporter economics cannot justify assuming meaningful paid CAC before revenue and conversion improve.

### CAC implication

At 10% supporter conversion and £20/year, average net first-year supporter revenue is only **£1.95 per activated family** before costs. Therefore an acquisition model dependent on multi-pound paid CAC is structurally incompatible with the current funding hypothesis.

Initial validation must therefore prioritize **near-zero marginal-cost, trusted distribution**: school/transition partnerships, organic discovery and referrals.

Exact CAC remains unconfirmed until real channel experiments run.

## Phase 21 — Retention, Engagement & Long-Term Value — COMPLETE

### Decision

UseSafeWeb must not optimize for app engagement. The product's own earlier principle remains authoritative: success may mean the parent rarely opens it.

### Retention definition

Primary retention is **protection persistence**, not dashboard MAU:

- baseline protection remains active;
- required native/platform safeguards remain configured or are re-checked when materially relevant;
- the parent understands current coverage gaps;
- the family returns only for meaningful events such as a new device, relevant service change, legitimate exception/problem, or later maturity review.

### Required retention evidence

Track separately:

1. baseline protection active at 14/30/90 days;
2. reasons protection is removed or breaks;
3. percentage of users needing reconfiguration after device/network changes;
4. supporter renewal at 12 months if the supporter model is tested;
5. later sibling/new-device reuse as lifecycle value, without counting it as proven today.

The existing phase-12 threshold remains: **≥70% of activated users should still have baseline protection enabled after 14 days** for the MCP to look promising.

No 90-day or annual threshold is frozen yet because there is no behavioral retention dataset from this exact product. Inventing one would create false precision.

### Long-term value hypothesis

Long-term value may come from quiet continued baseline protection plus occasional life-stage/device reviews rather than daily use. GROW remains conceptually relevant but must not be built until SET UP + PROTECT demand and persistence are proven.

## Phase 22 — Operational & Support Burden Assessment — COMPLETE

### Confirmed category evidence

Support burden is real in adjacent products:

- Qustodio sells/adds **Care Plus** for priority phone support, setup troubleshooting, check-ins and personalised help.
- CleanBrowsing states that it provides setup assistance, including remote TeamViewer sessions, and maintains extensive device-specific setup documentation.

This does not quantify UseSafeWeb's support burden, but it confirms that cross-device parental-control/filtering setup can require material assistance.

### Project-specific support drivers

Expected burden concentrates in:

1. Apple/Google family-account prerequisites and changing native UI paths;
2. device/OS/version differences;
3. baseline DNS/profile activation and verification failures;
4. false positives / legitimate blocks;
5. device replacement or reset;
6. users changing network/security settings;
7. unsupported external services;
8. confusion between verified, parent-confirmed and not-covered protection;
9. documentation drift as Apple/Google/platform controls change.

### Operating model

- MCP must remain self-service by default.
- Pilot human assistance is allowed only to diagnose friction and must be measured, not hidden.
- Do not promise live concierge support as the default service.
- Every support incident should be classified by root cause so recurring friction can be removed from onboarding.

### Support metrics / decision gates

Preserve the existing phase-12 red flag: if **>30% of users require substantial live intervention after basic usability refinement**, the orchestration layer is likely creating too much administration.

Add an economic red flag from phase 19:

> If routine activation/support consistently consumes materially more than about **5–10 active human minutes per activation** while supporter conversion remains around 10% at £20/year, the selected funding model cannot plausibly support the service without more automation, higher/other funding, or a model change.

The 5–10 minute boundary is not an industry benchmark; it is derived from the project's current average net revenue and the 2026 UK minimum-wage floor.

### Phase-22 conclusion

Operational feasibility is plausible **only if the guided setup truly removes work**. Support burden is now one of the highest-priority quantities to measure in the behavioral MCP, alongside activation and willingness to pay.

## State after this tranche

Phases **1–22 COMPLETE** as business-evaluation analyses. Exact-product behavioral demand, payment conversion, retention and support burden remain unvalidated in the real world; completion means the relevant business assessment/decision framework is complete, not that customer behavior has been proven.

## Next authoritative step

**Phase 23 — Legal / Regulatory Business Risk Assessment.**

This is now the first incomplete dependency. It must assess the actual UK/England legal applicability and business risk for the defined parent-facing, non-surveillance, AdGuard-backed MCP, including UK GDPR/Data Protection Act, Children's Code applicability, Online Safety Act implications where applicable, children's data, parental consent/account structure, DNS/query-data treatment, consumer claims, and the planned 2027 under-16 social-media regime. It must distinguish binding requirements from conservative design choices and avoid turning into implementation architecture.

## Primary evidence used

- Apple parental controls: https://support.apple.com/en-euro/105121
- Google Family Link: https://support.google.com/families/answer/7101025?hl=en-en
- NextDNS pricing: https://nextdns.io/nl/pricing
- CleanBrowsing pricing/free service: https://cleanbrowsing.org/pricing ; https://cleanbrowsing.org/learn/free-vs-paid
- Qustodio plans: https://www.qustodio.com/en/parental-control-plans/
- Canopy pricing: https://support.canopy.us/portal/en/kb/articles/how-much-does-canopy-cost-can-i-try-it-for-free
- Stripe UK pricing: https://stripe.com/gb/pricing
- OVHcloud UK VPS pricing: https://www.ovhcloud.com/en-gb/vps/vps-uk/
- UK National Living Wage 2026: https://www.gov.uk/government/news/national-living-wage-increases-to-1271-per-hour
- DfE Parent, Pupil and Learner Voice March 2026: https://www.gov.uk/government/publications/parent-pupil-and-learner-voice-omnibus-surveys-for-2025-to-2026/parent-pupil-and-learner-voice-march-2026
