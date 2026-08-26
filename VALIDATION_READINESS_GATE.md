# UseSafeWeb.com — Validation Readiness Gate

**Date:** 2026-08-26  
**Status:** IN PROGRESS — owner/environment facts substantially resolved; remaining blockers are minimum UK representation/fee handling plus deployment verification.  
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

## 2. Owner-approved operating decisions

- **AdGuard privacy posture:** the pilot/production server will be deployed to the privacy-minimal settings in this gate; old/test settings are not authoritative.
- **Production hosting geography:** EU + USA may exist later in production.
- **Experiment 1:** England-pilot child-linked DNS traffic uses the **EU node only**; the US node is excluded from the pilot data path.
- **Hosting provider:** Microsoft Azure.
- **EU pilot Azure region:** **West Europe (`westeurope`), Netherlands**. Microsoft currently identifies West Europe as a Netherlands Azure region.
- **Other pilot processors/services:** none selected/planned beyond Microsoft Azure and the upstream DNS provider. Payments, marketing, CDN/proxy, third-party analytics and separate research-data SaaS are not part of Experiment 1.
- **Controller:** individual, main establishment **Netherlands**.
- **Current turnover:** **0 / pre-revenue**.
- **Staff information:** intentionally not recorded at this stage. It is not needed to identify the lowest ICO fee tier because turnover is already below the current Tier-1 threshold if a fee is due.
- **Owner simplicity objective:** run the early stage as a lean friends/family validation project and defer non-essential commercial/organisational formalisation until **500 active users**.
- **500-user clarification:** this is an internal scale-up review milestone, **not a legal threshold**. Minimum GDPR/UK-GDPR duties that apply to the pilot cannot be deferred merely because the service is free, pre-revenue, friends/family, or below 500 users.

Primary sources:
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Microsoft DPA: https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa
- EU GDPR applicability: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en
- UK GDPR territorial scope: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/who-does-the-uk-gdpr-apply-to/

## 3. Upstream DNS — authoritative selection

**Selected:** Quad9 privacy-first, no-threat-blocking, non-ECS encrypted DNS-over-HTTPS:

`https://dns10.quad9.net/dns-query`

Configuration principle:

- AdGuard Home remains the sole product filtering/policy layer;
- Quad9 supplies recursive DNS + DNSSEC only, avoiding hidden/double malware filtering;
- **EDNS Client Subnet (ECS) must be disabled** in AdGuard Home;
- do not use Quad9 ECS endpoints (`dns11`/`dns12`) for the pilot.

Why Quad9:

- Swiss public-benefit foundation;
- June-2026 privacy policy states it does not collect or record user IP addresses;
- current service matrix provides a no-threat-blocking, non-ECS endpoint;
- DNSSEC validation is enabled across Quad9 service endpoints;
- Switzerland is covered by UK adequacy regulations.

Primary sources:
- https://quad9.net/privacy/policy/
- https://docs.quad9.net/services/
- https://quad9.net/news/blog/quad9-enables-dnssec-on-all-service-endpoints/
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/adequacy-regulations/is-the-restricted-transfer-covered-by-adequacy-regulations/

## 4. Experiment-1 data flow

Parent browser → UseSafeWeb setup journey → pseudonymous experiment record.

Child device → encrypted UseSafeWeb/AdGuard DNS endpoint on **Azure West Europe (Netherlands)** → Quad9 `dns10` DoH → DNS response → child device.

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

## 5. Lawful basis / LIA

**Provisional basis:** legitimate interests under Article 6(1)(f), subject to final LIA/DPIA approval immediately before live participant processing.

Purpose: provide parent-requested first-phone setup and baseline DNS protection while testing whether the service removes more work than it creates.

Necessary:
- minimal setup-routing inputs;
- transient DNS processing required to resolve/filter requests;
- minimum service-security data;
- pseudonymous experiment metrics required by the validation plan.

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

### Territorial position

- The controller is established in the **Netherlands**, so EU GDPR applies to the controller's relevant processing.
- The pilot intentionally offers a service to families in **England**, so UK GDPR also applies to that UK-targeted processing even though the controller is outside the UK.
- The personal/household exemption cannot safely be used for this product-validation service. Official EU/UK guidance limits that exemption to purely personal/household activity without professional/commercial connection; the project is explicitly testing a service intended for later public use/funding.
- There is no 500-user exemption or delayed-compliance threshold.

Primary sources:
- https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/who-does-the-uk-gdpr-apply-to/

**LIA state:** substantively complete; final approval remains tied to deployment verification and the UK representative/fee decision below.

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

**Verification rule:** before the first real participant, inspect the deployed configuration and confirm every requirement directly. Planned settings are not execution evidence.

## 7. Hosting / processor / transfer review

### Microsoft Azure

Selected provider: **Microsoft Azure**. Pilot region: **West Europe, Netherlands**.

Microsoft's current Products and Services Data Protection Addendum provides the standard processor/data-protection terms for Azure, and Microsoft documents that Azure customer data can be provisioned at rest within selected geographic regions, subject to the DPA/Product Terms and service-specific exceptions. Microsoft also provides contractual transfer safeguards for relevant cross-border processing.

This is sufficient for the **design-stage processor selection**, but deployment acceptance still requires verifying that the actual pilot VM/resources are created in `westeurope` and that no optional service added to the pilot creates an unreviewed data flow.

Primary sources:
- https://learn.microsoft.com/en-us/compliance/regulatory/gdpr-dpia-azure
- https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa
- https://learn.microsoft.com/en-us/compliance/regulatory/offering-eu-model-clauses

### Quad9

Quad9 remains the selected upstream as documented above.

### Other processors

None currently selected. If CDN/proxy, third-party analytics, email/scheduling, payment or separate research-data services are later added, this gate must be updated before use.

## 8. Retention policy for Experiment 1

- identifiable DNS/domain history: **not retained**;
- diagnostic DNS logs: only if genuinely required for a specific fault, time-boxed and deleted immediately after resolution;
- parent contact details needed for the 14-day follow-up: keep only until follow-up is completed, then delete promptly and no later than 30 days after that participant's follow-up;
- participant-level pseudonymous experiment metrics: retain only through experiment analysis/decision, then aggregate/anonymise and delete participant-level records no later than 90 days after Experiment 1 closes;
- aggregate/anonymised business findings may remain in the canonical repository.

## 9. DPIA risk status

| Risk | Required mitigation | State |
|---|---|---|
| identifiable DNS history | query/file log off; no history feature | design resolved; deployment verification pending |
| client/IP statistics | exclude/disable + anonymise | design resolved; deployment verification pending |
| client subnet disclosed upstream | ECS off | resolved requirement; deployment verification pending |
| upstream privacy/retention | Quad9 `dns10`; privacy policy reviewed; Swiss adequacy | RESOLVED |
| US transfer during England pilot | EU-only Azure node | RESOLVED |
| Azure hosting processor | West Europe + Microsoft DPA/transfer terms | design RESOLVED; deployment region verification pending |
| extra pilot processors | none currently selected | RESOLVED subject to no scope change |
| UK representative | resolve before pilot unless a defensible Article-27 exception is established | OPEN/BLOCKING |
| ICO fee | zero turnover means Tier 1 if fee due; applicability/self-assessment still to close | OPEN, low burden |
| false safety confidence | verified/confirmed/action-needed/not-covered states | READY |
| overblocking | sensible baseline + remedy + measure removals | READY |
| child transparency | age-appropriate explanation | READY |
| sensitive inference | no profiling/inference from DNS | READY |

## 10. UK representative / ICO position

### UK representative

Current ICO guidance states that a controller based outside the UK with no UK establishment that offers goods/services to people in the UK must appoint a UK representative unless the processing is **only occasional, low risk**, and does not involve large-scale special-category/criminal data.

UseSafeWeb should **not rely on that exception without specialist confirmation**: the pilot deliberately targets England, processes child-linked DNS traffic, and the DPIA already treats identifiable DNS exposure as potentially high impact. Therefore the safe gate is:

> **Before the first real England participant, appoint a UK representative or obtain a defensible documented conclusion that the Article-27 exception applies.**

A UK representative can be a person, company or organisation established in the UK and must be authorised in writing. This can remain operationally simple; no large compliance structure is required.

Primary source:
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/

### ICO data-protection fee

Current turnover is **0**, so if the UK data-protection fee is due the controller falls within the current **Tier 1 (£52)** turnover threshold. Staff information is therefore unnecessary for tier selection.

The service should not treat friends/family status or fewer than 500 users as a fee exemption. ICO guidance says controllers must pay unless an exemption applies and provides a specific extraterritorial-organisations assessment route. The personal/household exemption is not a safe fit for this service-validation activity.

**Gate rule:** complete the ICO fee self-assessment before the first real England participant and record the result; if due, pay the Tier-1 fee. This is a one-time low-burden compliance action, not a reason to create a company or formal staff structure.

Primary sources:
- https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/
- https://ico.org.uk/for-organisations/data-protection-fee/paying-a-data-protection-fee-what-do-you-need-to-know/extraterritorial-organisations/
- https://ico.org.uk/for-organisations/data-protection-fee/paying-a-data-protection-fee-what-do-you-need-to-know/activities-of-households-sector/

## 11. Parent/child transparency minimum

Before activation state plainly:

- UseSafeWeb coordinates phone/service safeguards and provides domain-level baseline filtering;
- DNS requests are processed to answer/filter them but UseSafeWeb is not a browsing-history product;
- it does not read messages, track location, inspect social feeds or guarantee complete safety;
- some harmful content inside apps/services is outside DNS protection;
- `Protected — verified` is distinct from `Configured — parent confirmed` and `Not covered`;
- explain experiment data, purpose, retention, recipients and deletion/withdrawal handling;
- provide a child-readable explanation of what filtering does and does not monitor.

Do not make a generic “no logs” claim; state the specific verified logging/retention posture after deployment verification.

## 12. Payment gate

No £2/month or £20/year supporter payment in Experiment 1. Payment willingness is tested only after behavioral value is demonstrated; subscription-law obligations are re-checked at that later stage.

## 13. Current gate result

**NOT READY FOR REAL PARTICIPANTS YET, but owner/environment fact collection is complete.**

Resolved:
- data flow/data minimisation;
- privacy-minimal AdGuard target configuration;
- Azure as hosting provider;
- Azure West Europe (Netherlands) as the pilot region;
- EU-only England-pilot data plane;
- Quad9 `dns10` upstream and ECS-off requirement;
- no extra pilot processors;
- controller = individual established in Netherlands;
- turnover = 0 / pre-revenue;
- staff information not required at this stage;
- draft LIA/DPIA substance;
- retention rules;
- transparency requirements;
- payment exclusion;
- 500 active users retained only as an internal formalisation/scale-review milestone, not a legal threshold.

Remaining before PASS:
1. complete ICO fee self-assessment and pay Tier 1 if the assessment says a fee is due;
2. appoint a UK representative, or obtain a defensible documented Article-27 exception conclusion;
3. deploy/configure the Azure West Europe pilot node to the mandatory AdGuard requirements;
4. directly verify the deployed Azure region and AdGuard privacy/upstream/ECS settings;
5. issue the final parent/child privacy notice with the actual controller/UK-representative contact information;
6. approve final LIA/DPIA residual risks after steps 1–5.

## 14. Exact next authoritative step

The next human-only issue is **UK representation**. The simplest compliant path is to nominate a trusted person/entity established in the UK to act as the pilot's UK representative under a short written authorisation, while keeping the project otherwise informal and pre-revenue.

In parallel, all technical readiness work may proceed: provision an Azure `westeurope` pilot VM, deploy AdGuard to the mandatory settings, then inspect and record the resulting configuration evidence.
