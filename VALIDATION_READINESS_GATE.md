# UseSafeWeb.com — Validation Readiness Gate

**Date:** 2026-08-26  
**Status:** IN PROGRESS — most design decisions resolved; two human/environment facts remain.  
**Purpose:** prerequisite to Experiment 1. No real child-linked DNS processing is authorised until this gate is PASS.

## 1. Gate completion criteria

PASS requires:

1. pilot data flow/data inventory documented;
2. LIA/DPIA completed against the actual pilot environment;
3. lawful basis documented per purpose;
4. deployed AdGuard privacy settings verified against the mandatory configuration below;
5. parent/child privacy and protection-limit notice ready;
6. controller/ICO fee and UK-representative position resolved;
7. hosting/upstream/other recipients and transfers reviewed;
8. payments/marketing disabled for Experiment 1.

## 2. Owner-approved decisions now resolved

- **AdGuard privacy posture:** the pilot/production server will be configured to the privacy-minimal settings in this gate; an old/test server configuration is not treated as authoritative.
- **Production hosting geography:** EU + USA may exist in production.
- **Experiment 1 geography decision:** England-pilot child-linked DNS traffic will use the **EU node only**. The US node is excluded from the Experiment-1 child-data path because it adds no validation value and would add avoidable transfer/contract complexity.
- **Other pilot processors/services:** none selected/planned at this stage beyond the server host and upstream DNS. Payments and marketing are disabled.
- **Controller type:** **individual**.

Still required from the owner before PASS:

1. **hosting provider name** for the EU pilot server;
2. **controller country/main establishment**, plus approximate staff count and annual-turnover band sufficient to resolve ICO fee/UK-representative applicability.

## 3. Upstream DNS — authoritative selection

**Selected:** Quad9 privacy-first, no-threat-blocking, non-ECS encrypted DNS-over-HTTPS:

`https://dns10.quad9.net/dns-query`

Configuration principle:

- AdGuard Home remains the sole product filtering/policy layer;
- Quad9 is used only for recursive DNS + DNSSEC, avoiding hidden/double malware filtering that would complicate attribution and false-positive debugging;
- **EDNS Client Subnet (ECS) must be disabled** in AdGuard Home so participant/client subnet information is not intentionally forwarded upstream;
- do not use Quad9 ECS endpoints (`dns11`/`dns12`) for the pilot.

Why Quad9:

- Quad9 is a Swiss public-benefit foundation;
- its June 2026 privacy policy states it does not collect or record user IP addresses;
- its current service matrix provides a no-threat-blocking, non-ECS endpoint;
- as of June 15, 2026, DNSSEC validation is enabled across all Quad9 service endpoints;
- Switzerland is covered by UK adequacy regulations, simplifying the transfer position compared with an unnecessary US upstream relationship.

Primary sources:
- https://quad9.net/privacy/policy/
- https://docs.quad9.net/services/
- https://quad9.net/news/blog/quad9-enables-dnssec-on-all-service-endpoints/
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/adequacy-regulations/is-the-restricted-transfer-covered-by-adequacy-regulations/

## 4. Experiment-1 data flow

Parent browser → UseSafeWeb setup journey → pseudonymous experiment record.

Child device → encrypted UseSafeWeb/AdGuard DNS endpoint on **EU pilot server** → Quad9 `dns10` DoH upstream → DNS response → child device.

No US node is in the Experiment-1 child-data path.

Minimum experiment data:
- participant ID;
- age band/stage, not DOB;
- device family;
- new/existing-phone state;
- one relevant service/app;
- setup/protection states;
- support minutes/reason;
- abandonment reason;
- coverage-gap comprehension;
- 14-day protection state.

Do not collect by default:
- child name/exact DOB;
- school;
- child email/phone;
- contacts/location/messages/photos;
- social usernames;
- browsing-history/domain-history reports.

GitHub receives only aggregate/anonymised experiment results.

## 5. Provisional lawful basis / LIA

**Provisional UK GDPR Article 6(1)(f) legitimate interests**, subject to final LIA/DPIA approval against the actual controller and hosting environment.

Purpose: provide parent-requested first-phone setup and baseline DNS protection.

Necessary:
- minimal setup-routing inputs;
- transient DNS processing required to resolve/filter requests;
- minimum service-security data;
- pseudonymous experiment metrics needed to decide whether the product should exist.

Not necessary and prohibited for Experiment 1:
- persistent identifiable DNS/browsing history;
- child behavioral profiling;
- location/messages/contacts;
- targeted advertising;
- sale of family data;
- payment/marketing profiling.

Balancing safeguards:
- high-privacy defaults;
- no surveillance/history product;
- no ECS;
- no child profiling;
- clear parent/child explanation;
- explicit coverage gaps;
- easy removal;
- minimal retention;
- EU-only pilot data plane.

**LIA state:** draft substantively complete; final territorial/controller section remains blocked on controller country and hosting provider.

## 6. Mandatory AdGuard configuration for pilot/production

This is a deployment acceptance requirement, not a claim about any old/test server.

For Experiment-1 participant traffic:

1. persistent identifiable query logging: **OFF**;
2. file query logging: **OFF**;
3. identifiable per-client statistics: **OFF/excluded** unless a specifically justified non-identifying aggregate is required;
4. client-IP anonymisation: **ON** wherever an operational log/statistic can contain addresses;
5. EDNS Client Subnet: **OFF**;
6. upstream DNS: `https://dns10.quad9.net/dns-query`;
7. no browsing-history/top-domain parent feature;
8. no browsing/domain history as experiment metrics;
9. diagnostic logging only when genuinely necessary, time-boxed and deleted after resolution;
10. no WHOIS/rDNS/client-enrichment solely for analytics.

**Verification rule:** before the first real participant, inspect the deployed configuration and confirm these requirements directly. A planned setting is not execution evidence.

## 7. DPIA risk status

| Risk | Required mitigation | State |
|---|---|---|
| identifiable DNS history | query/file log off; no history feature | design resolved; deployment verification pending |
| client/IP statistics | exclude/disable + anonymise | design resolved; deployment verification pending |
| client subnet disclosed upstream | ECS off | resolved requirement; deployment verification pending |
| upstream privacy/retention | Quad9 `dns10`; privacy policy reviewed; Swiss adequacy | RESOLVED |
| US transfer during England pilot | EU-only pilot node | RESOLVED |
| extra pilot processors | none currently selected | RESOLVED subject to no scope change |
| hosting processor terms/location | identify actual EU host/provider and terms | BLOCKED on provider name |
| controller territorial/ICO/representative position | determine from controller country/main establishment | BLOCKED on controller facts |
| false safety confidence | verified/confirmed/action-needed/not-covered states | READY |
| overblocking | sensible baseline + remedy + measure removals | READY |
| child transparency | age-appropriate explanation | READY |
| sensitive inference | no profiling/inference from DNS | READY |

## 8. Parent/child transparency minimum

Before activation state plainly:

- UseSafeWeb coordinates phone/service safeguards and provides domain-level baseline filtering;
- DNS requests are processed to answer/filter them but UseSafeWeb is not a browsing-history product;
- it does not read messages, track location, inspect social feeds or guarantee complete safety;
- some harmful content inside apps/services is outside DNS protection;
- `Protected — verified` is distinct from `Configured — parent confirmed` and `Not covered`;
- explain experiment data, purpose, retention, recipients and deletion/withdrawal handling;
- provide a child-readable explanation of what filtering does and does not monitor.

Do not claim generic “no logs”; state the specific verified retention/logging posture after deployment verification.

## 9. Controller / ICO / UK-representative assessment

Resolved: controller type = **individual**.

Still unknown: controller country/main establishment and staff/turnover band.

This is material because:
- UK GDPR can apply to overseas controllers offering services to people in the UK;
- an overseas controller without a UK establishment may need a UK representative unless a narrow exception applies;
- ICO fee applicability/tier depends on the controller circumstances and exemptions.

No assumption will be made from the owner’s residence or nationality; the controller facts must be explicitly confirmed.

Primary sources:
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/
- https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/data-protection-fee-faqs/

## 10. Hosting / transfers

Owner-approved production geography: **EU + USA**.

Experiment-1 rule: **EU server only**.

The actual EU hosting provider remains unknown. Before PASS:
- record provider legal entity and EU processing region;
- review processor/data-protection terms and subprocessors;
- confirm whether any provider-controlled access/transfer leaves the UK-adequate region;
- if the provider uses a US legal entity/US subprocessors, assess the actual transfer mechanism rather than assuming geographic EU hosting alone removes transfer obligations.

No CDN/proxy, email/scheduling, payment, analytics, or separate research-data processor is currently selected. If one is added, this gate must be updated before use.

## 11. Payment gate

No £2/month or £20/year supporter payment in Experiment 1. Payment willingness is tested only after behavioral value is demonstrated; subscription-law obligations are re-checked at that later stage.

## 12. Current gate result

**NOT READY FOR REAL PARTICIPANTS YET, but the blocker is now narrow.**

Resolved:
- data flow/data minimisation;
- privacy-minimal AdGuard target configuration;
- EU-only England-pilot data plane;
- upstream provider and exact DoH endpoint;
- ECS off;
- no extra pilot processors;
- controller type = individual;
- draft LIA/DPIA substance;
- transparency requirements;
- payment exclusion.

Remaining before PASS:
1. hosting provider name/legal entity for the EU pilot server;
2. controller country/main establishment + approximate staff count/turnover band;
3. review the resulting processor/territorial/ICO/UK-representative implications;
4. deploy the pilot server to the mandatory configuration and directly verify it;
5. insert the verified environment facts into the LIA/DPIA and approve residual risks.

## 13. Exact next evidence needed from owner

Reply with only:

- **EU pilot hosting provider:** [name]
- **Controller country/main establishment:** [country]
- **Approximate staff count:** [number/band]
- **Approximate annual turnover:** [band; exact figure not required]

No credentials or secrets are required.
