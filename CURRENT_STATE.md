# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-26  
**Branch:** `main`  
**Status authority:** This file is the current checkpoint. Detailed business evidence is in `BUSINESS_EVALUATION.md`, `BUSINESS_PHASES_17_22.md`, and `BUSINESS_PHASES_23_42.md`. Validation readiness is governed by `VALIDATION_READINESS_GATE.md`; Experiment 1 is governed by `EXPERIMENT_01_CONCIERGE_VALIDATION.md`.

## Frozen project identity

- Public domain: **UseSafeWeb.com**.
- Backend: **AdGuard**, frozen unless verified critical blocker.
- Initial market: **United Kingdom**; first behavioral validation concentrated in **England**.
- Core segment: parent/caregiver around a child's first independently used smartphone, centered roughly ages 10–12.
- Core JTBD: **SAFE INDEPENDENCE**.
- Customer-facing product: **UseSafeWeb — First Phone Safety Setup**.
- MCP: accountless guided setup coordinating native device safeguards + real AdGuard-backed baseline protection + one relevant external-service safeguard + truthful Protection Map.
- Trust posture: **Simple guardrails. Clear limits. No invasive monitoring.**
- Initial funding hypothesis: free core + optional £20/year or £2/month supporter contribution after value; no payment test in Experiment 1.

## Business evaluation

**Phases 1–42: COMPLETE.**

Final decision: **MODIFY — PROCEED TO VALIDATION, NOT FULL LAUNCH.**

Internal decision score: **64/100** (project heuristic, not probability).

The original broad family-DNS proposition is superseded. The surviving hypothesis is a lightweight first-phone safety orchestration utility with DNS invisible underneath.

## Validation objective

### Validation Readiness Gate — IN PROGRESS / BLOCKED ON OPERATIONAL EVIDENCE

Completed and persisted in `VALIDATION_READINESS_GATE.md`:

- intended pilot data-flow map;
- minimum data inventory;
- provisional lawful-basis map;
- draft legitimate-interests assessment;
- draft DPIA/risk register;
- mandatory DNS privacy/logging requirements;
- parent/child transparency requirements;
- ICO-fee assessment logic;
- processor/international-transfer checklist;
- decision to keep payment/marketing disabled in Experiment 1.

The gate is **NOT PASS** and real child-linked DNS processing for the validation experiment is not authorised yet.

### Blocking evidence required to close the gate

1. Directly verify deployed AdGuard Home settings for query logging, file logging, statistics, client exclusions and client-IP anonymisation.
2. Identify the actual server/hosting provider and processing country/region.
3. Identify the configured upstream DNS provider/resolver and its privacy/retention/role.
4. Identify any CDN/proxy, experiment/contact-data store, email/scheduling provider or other processor used for the pilot.
5. Establish the actual controller/legal-entity facts needed for the ICO data-protection-fee assessment (entity type, relevant staff/turnover band, exemption position).
6. Set final retention periods from verified operational need.
7. Insert items 1–6 into the LIA/DPIA and formally approve the residual-risk decision before the pilot.

No matching deployed-environment configuration or provider facts were found in the canonical repository, and prior recoverable project context did not establish them.

## Required experiment privacy posture

For participant child devices in Experiment 1:

- persistent identifiable query logging: OFF;
- file query logging: OFF;
- identifiable per-client statistics: OFF/excluded unless a necessary non-identifying aggregate is justified;
- client-IP anonymisation: ON wherever an operational log/statistic can still contain addresses;
- no browsing-history/top-domain product or research metric;
- exceptional diagnostic logging only when necessary, time-boxed and deleted after resolution;
- GitHub contains only aggregate/anonymised experiment results, never participant identities or child browsing data.

AdGuard Home supports these relevant controls, but the deployed instance has not yet been inspected and therefore compliance is not claimed.

## Experiment 1 protocol

`EXPERIMENT_01_CONCIERGE_VALIDATION.md` is **READY AS A PROTOCOL but BLOCKED FROM EXECUTION until the readiness gate passes**.

Planned cohort: **20–30 qualified England parents/caregivers** around the first-smartphone transition.

Primary existing decision gates:

- ≥60% qualified-starter full activation;
- ≥50% configure at least one previously missing native/external safeguard;
- ≥70% baseline protection active after 14 days;
- ≤25% abandon primarily because UseSafeWeb adds/duplicates work;
- ≥80% understand at least two major coverage gaps;
- ≤30% require substantial live assistance after basic refinement.

Strong failure evidence after one materially improved iteration:

- <40% full activation;
- <25% complete any previously missing non-DNS safeguard;
- majority of abandoners say native controls are sufficient / UseSafeWeb adds work;
- >30% require substantial live assistance after refinement;
- >30% remove protection within 14 days because of blocking/compatibility/friction;
- serious child-data/privacy incident → immediate stop.

## Current completion state

- Business evaluation #1–#42: **COMPLETE**.
- Validation Readiness design/documentation: **COMPLETE**.
- Validation Readiness operational verification: **BLOCKED / OPEN**.
- Experiment 1 protocol: **COMPLETE**.
- Experiment 1 execution/recruitment: **NOT STARTED — prohibited until readiness PASS**.
- Minimal MCP implementation: **NOT AUTHORISED until behavioral experiment passes**.
- Full launch: **NOT AUTHORISED**.

## Exact next authoritative action

Close the operational evidence portion of the **Validation Readiness Gate** by inspecting/providing the minimum environment facts listed above. Once verified, finalise/approve the LIA/DPIA and mark the gate PASS. Only then begin Experiment 1 recruitment and real participant activation.
