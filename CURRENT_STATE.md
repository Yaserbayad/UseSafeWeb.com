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

**Status: IN PROGRESS / BLOCKED ON TWO OWNER FACT SETS + DEPLOYMENT VERIFICATION.**

### Newly resolved owner decisions

- Future pilot/production AdGuard server must be deployed with the privacy-minimal configuration defined in `VALIDATION_READINESS_GATE.md`; old/test settings are not authoritative.
- Production may use EU + USA hosting geography.
- **England Experiment 1 uses the EU node only**; the US node is excluded from the participant child-data path.
- No additional pilot CDN/proxy/email/scheduling/payment/analytics/research-data processor is currently selected.
- Controller type: **individual**.

### Upstream DNS decision

Selected upstream for development, Experiment 1 and production baseline:

`https://dns10.quad9.net/dns-query`

- provider: Quad9, Swiss public-benefit foundation;
- encrypted DoH;
- no threat blocking, keeping AdGuard as the sole product filtering/policy layer;
- DNSSEC validation enabled;
- **ECS disabled** in AdGuard; do not use Quad9 ECS endpoints;
- Quad9 June-2026 privacy policy states it does not collect or record user IP addresses;
- Switzerland is covered by UK adequacy regulations.

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

These are deployment acceptance requirements, not claims about any current/test server.

### Remaining owner facts

Only the following facts are still needed before the legal/processor assessment can be finalised:

1. **EU pilot hosting provider name/legal entity**.
2. **Controller country/main establishment**.
3. **Approximate staff count**.
4. **Approximate annual turnover band**.

Controller country is especially material because an individual controller outside the UK who offers services to UK users may have UK territorial/representative obligations; no country will be inferred from residence/nationality.

### Work after those facts

1. review hosting processor terms/subprocessors/transfer position;
2. resolve ICO fee and any UK-representative requirement;
3. finalise LIA/DPIA territorial/processor sections;
4. deploy/configure the EU pilot node;
5. directly verify mandatory AdGuard settings;
6. approve residual risks and mark Validation Readiness PASS;
7. only then begin Experiment 1 recruitment/activation.

## Current completion state

- Business evaluation #1–#42: **COMPLETE**.
- Validation-readiness design: **COMPLETE**.
- Upstream DNS selection: **COMPLETE**.
- Pilot data-geography decision: **COMPLETE**.
- Controller type: **COMPLETE — individual**.
- Hosting-provider/controller-territory facts: **OPEN**.
- Deployment/config verification: **NOT STARTED**.
- Experiment 1 protocol: **COMPLETE**.
- Experiment 1 execution: **NOT STARTED / NOT AUTHORISED until readiness PASS**.
- MCP implementation: **NOT AUTHORISED until behavioral validation passes**.
- Full launch: **NOT AUTHORISED**.

## Exact next authoritative action

Obtain the four remaining factual values from the owner:

- EU pilot hosting provider;
- controller country/main establishment;
- approximate staff count;
- approximate annual turnover band.

Then continue autonomously through processor/ICO/representative analysis and the deploy-and-verify readiness work.
