# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-26  
**Branch:** `main`  
**Status authority:** current checkpoint. Detailed business evidence remains in `BUSINESS_EVALUATION.md`, `BUSINESS_PHASES_17_22.md`, and `BUSINESS_PHASES_23_42.md`. Validation readiness is governed by `VALIDATION_READINESS_GATE.md`; Experiment 1 by `EXPERIMENT_01_CONCIERGE_VALIDATION.md`.

## Frozen project identity

- Public domain: **UseSafeWeb.com**.
- Backend: **AdGuard**, frozen unless verified critical blocker.
- Initial market: UK; first behavioral validation in England.
- Core segment: parent/caregiver around a roughly 10–12-year-old child's first independently used smartphone.
- Product: **UseSafeWeb — First Phone Safety Setup**.
- Trust posture: **Simple guardrails. Clear limits. No invasive monitoring.**

## Business evaluation

**Phases 1–42 COMPLETE.**

Final decision: **MODIFY — PROCEED TO VALIDATION, NOT FULL LAUNCH.**

## Validation Readiness Gate

**Status: IN PROGRESS — OWNER/ENVIRONMENT FACT COLLECTION COMPLETE; UK REPRESENTATION/ICO + DEPLOYMENT VERIFICATION REMAIN.**

### Authoritative environment/owner decisions

- Future pilot/production AdGuard must be deployed to the privacy-minimal requirements in `VALIDATION_READINESS_GATE.md`; old/test settings are not authoritative.
- Hosting provider: **Microsoft Azure**.
- Production may later use EU + USA geography.
- **Experiment 1 uses Azure West Europe (`westeurope`), Netherlands only** for child-linked DNS processing; the US node is excluded from the pilot path.
- No additional pilot CDN/proxy/email/scheduling/payment/analytics/separate-research-data processor is currently selected.
- Controller: **individual, main establishment Netherlands**.
- Current turnover: **0 / pre-revenue**.
- Staff information is intentionally not recorded at this stage and is not needed for the current fee-tier determination because turnover is below the Tier-1 threshold if a fee is due.
- Owner intends to keep the first stage as a simple friends/family project and use **500 active users** as the point for broader organisational/commercial formalisation.
- **500 users is an internal scale-review milestone only, not a GDPR/UK-GDPR threshold.** Minimum legal/privacy duties applicable to the pilot cannot be deferred on that basis.

### Upstream DNS

Selected upstream for development, Experiment 1 and production baseline:

`https://dns10.quad9.net/dns-query`

- encrypted DoH;
- no threat blocking, keeping AdGuard as the sole product filtering/policy layer;
- DNSSEC validation;
- **ECS disabled** in AdGuard; do not use Quad9 ECS endpoints;
- Swiss upstream with published no-user-IP-recording posture.

### Mandatory pilot AdGuard target configuration

Before first real participant, directly verify:

- persistent identifiable query logging OFF;
- file query logging OFF;
- identifiable per-client statistics OFF/excluded unless specifically justified;
- IP anonymisation ON wherever operational records can contain addresses;
- EDNS Client Subnet OFF;
- upstream = `https://dns10.quad9.net/dns-query`;
- no browsing-history/top-domain product or experiment metric;
- diagnostic logs only when necessary, time-boxed and deleted after resolution.

### Territorial/compliance result

- Netherlands establishment means EU GDPR applies to relevant processing.
- Deliberately offering the pilot to England brings the UK-targeted processing within UK GDPR territorial scope.
- The friends/family or personal/household exemption is not relied upon for this product-validation service.
- A Netherlands-based controller with no UK establishment should not rely on the UK-representative exception without specialist confirmation because the exception requires processing to be only occasional and low risk; the project DPIA treats child-linked DNS exposure as materially sensitive/high-impact if mishandled.
- Safe gate: **appoint a UK representative before first real England participant, or obtain a defensible documented conclusion that the Article-27 exception applies.**
- With turnover 0, if the UK data-protection fee is due the controller falls within the current **Tier 1 (£52)** turnover threshold. Complete the ICO self-assessment before the first real participant; pay if required.

### Azure processor position

- Pilot region selected: **West Europe, Netherlands**.
- Microsoft Azure is accepted as the design-stage hosting processor under Microsoft's current Products and Services Data Protection Addendum and transfer safeguards.
- Deployment must still verify that the actual pilot resources are provisioned in `westeurope` and that no optional service creates an unreviewed data flow.

### Experiment-1 retention

- identifiable DNS/domain history: not retained;
- fault diagnostics: only when necessary, time-boxed, deleted after resolution;
- participant contact details: only through the 14-day follow-up, then delete promptly and no later than 30 days after that participant's follow-up;
- pseudonymous participant metrics: only through analysis/decision, then aggregate/anonymise and delete participant-level records within 90 days after Experiment 1 closes;
- canonical GitHub retains aggregate/anonymised findings only.

## Current completion state

- Business evaluation #1–#42: **COMPLETE**.
- Validation-readiness design: **COMPLETE**.
- Owner/environment fact collection: **COMPLETE**.
- Hosting provider/region selection: **COMPLETE — Azure West Europe, Netherlands**.
- Upstream DNS selection: **COMPLETE — Quad9 `dns10` DoH**.
- Controller facts: **COMPLETE — individual, Netherlands, turnover 0**.
- Staff information: **not required / intentionally omitted**.
- UK representative decision/action: **OPEN / BLOCKING before England pilot**.
- ICO fee self-assessment: **OPEN / low-burden pre-pilot action**.
- Pilot Azure/AdGuard deployment: **NOT STARTED**.
- Deployment/config verification: **NOT STARTED**.
- Experiment 1 protocol: **COMPLETE**.
- Experiment 1 execution: **NOT STARTED / NOT AUTHORISED until readiness PASS**.
- MCP implementation: **NOT AUTHORISED until behavioral validation passes**.
- Full launch: **NOT AUTHORISED**.

## Exact next authoritative action

Two branches may proceed without changing product scope:

1. **Human-only legal minimum:** nominate a person/entity established in the UK as the pilot UK representative, or obtain specialist confirmation that the Article-27 exception applies; complete the ICO fee self-assessment and pay Tier 1 if required.
2. **Technical readiness:** provision the Azure `westeurope` pilot node, deploy AdGuard with the mandatory privacy configuration, and directly verify region/logging/statistics/anonymisation/ECS/upstream settings.

After both branches pass, issue the final privacy notice with actual contact details, approve the LIA/DPIA residual risk, mark Validation Readiness PASS, and begin Experiment 1 recruitment/activation.
