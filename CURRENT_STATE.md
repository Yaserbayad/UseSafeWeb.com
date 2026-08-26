# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-26  
**Branch:** `main`  
**Status authority:** This file is the current checkpoint and supersedes older status lines in `BUSINESS_EVALUATION.md` while preserving that file as the detailed record through phase 16. See `BUSINESS_PHASES_17_22.md` for the completed commercial/distribution/operations tranche.

## Frozen project identity

- Public domain: **UseSafeWeb.com**.
- Backend: **AdGuard**, frozen unless verified critical blocker.
- Initial market: **United Kingdom**; first behavioral validation concentrated in **England**.
- Core segment: parent/caregiver around a child's first independently used smartphone, centered roughly ages 10–12.
- Core JTBD: **SAFE INDEPENDENCE**.
- Product: lightweight first-smartphone family digital-safety setup/orchestrator, not DNS software and not a surveillance suite.
- MCP: registration-free guided setup coordinating native device safeguards + real AdGuard-backed baseline protection + one relevant external service safeguard + truthful Protection Map.
- Trust posture: **Simple guardrails. Clear limits. No invasive monitoring.**

## Master plan status

1–16. **COMPLETE** — see `BUSINESS_EVALUATION.md`.

17. Customer Willingness-to-Pay / Free-Service Validation — **COMPLETE**
18. Business Model & Revenue/Funding Options — **COMPLETE**
19. Unit Economics & Cost Sustainability — **COMPLETE**
20. Distribution & Customer-Acquisition Strategy — **COMPLETE**
21. Retention, Engagement & Long-Term Value — **COMPLETE**
22. Operational & Support Burden Assessment — **COMPLETE**
23. Legal / Regulatory Business Risk Assessment — **NEXT**
24–42. Pending

## New authoritative decisions from phases 17–22

### Commercial model

- Do **not** paywall the MCP before demand is proven.
- Strongest WTP hypothesis: full service remains free; after activation offer optional supporter contribution at **£20/year or £2/month**.
- Actual completed payments, not survey intent, are required to validate WTP.
- Selected initial business model: **free-to-use core + voluntary supporter funding**.
- No core-safety feature gating during validation; no behavioral advertising or child-data monetisation.

### Economics

- Current Stripe UK standard domestic-card fee: **1.5% + £0.20**.
- £20 annual supporter payment nets approximately **£19.50** before tax/refunds/other costs.
- Average net revenue per activation at £20/year: **£0.975 at 5% supporter conversion; £1.95 at 10%; £3.90 at 20%**.
- Raw infrastructure is plausibly low-cost relative to support; a current UK VPS benchmark is £7.55/month incl. VAT for OVHcloud VPS-2, but this is not a production topology or capacity claim.
- Primary economic risk: **human support/operations**, not basic VPS cost.

### Distribution

Initial channel priority:

1. **School / primary-to-secondary transition channel**.
2. Organic first-phone-intent search/content.
3. Family/friend referral.
4. Trusted safety organisations/charities/public-information referrals after evidence exists.
5. Social media only as a supporting parent channel.
6. Paid performance acquisition deferred until monetisation can support it.

England DfE 2026 evidence: primary parents would seek online-safety advice from schools 50%, family/friends 46%, government sites 45%, children's charities 21%, AI tools/apps 20%, social media 16%.

### Retention

- Optimize for **protection persistence**, not app engagement/MAU.
- Existing MCP threshold remains: ≥70% of activated users still have baseline protection enabled after 14 days.
- Measure 30/90-day persistence and 12-month supporter renewal, but do not invent thresholds before real data.
- GROW remains deferred until SET UP + PROTECT demand/persistence are proven.

### Operations/support

- MCP must be self-service by default; pilot human assistance is diagnostic and must be measured.
- Existing red flag: >30% of users requiring substantial live intervention after basic usability refinement.
- Economic red flag: if routine activation/support consumes materially more than about **5–10 active human minutes per activation** while supporter conversion remains around 10% at £20/year, supporter-only economics are not plausible without automation, higher/other funding, or model change.

## Open uncertainties

1. Exact-product behavioral adoption is still unvalidated.
2. Actual supporter conversion and preferred monthly/annual option are unvalidated.
3. Actual production AdGuard capacity and full operating cost remain unverified.
4. Real CAC is unmeasured.
5. 30/90/365-day retention is unmeasured.
6. Actual support minutes/ticket rate are unmeasured.
7. UK legal/regulatory applicability and business risk for the exact MCP remain to be assessed in phase 23.

## Next authoritative step

**23 — Legal / Regulatory Business Risk Assessment.**

Assess current UK/England legal and regulatory exposure specifically for the defined parent-facing, non-surveillance, AdGuard-backed MCP. Distinguish binding requirements from conservative product choices; cover UK GDPR/Data Protection Act, Children's Code applicability, child/parent data, DNS query data, consumer/safety claims, Online Safety Act implications where applicable, and the planned 2027 under-16 social-media regime. Do not move into technical implementation architecture.
