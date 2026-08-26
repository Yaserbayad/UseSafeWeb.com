# UseSafeWeb — Experiment 1 Privacy & Protection Notice

**Status:** PRE-PILOT DRAFT — content complete except final controller/UK-representative contact details and deployed logging verification.

## Parent notice

### What UseSafeWeb does

UseSafeWeb helps you set up sensible safeguards for a child's first independently used smartphone. It coordinates relevant Apple/Google settings, one relevant service safeguard, and baseline domain-level DNS filtering.

### What it does not do

UseSafeWeb is not a surveillance product. It does not read private messages, track location, inspect social feeds, or promise complete online safety. Some harmful content inside apps and websites cannot be blocked by DNS filtering.

### DNS processing

When baseline protection is enabled, the child's device sends DNS requests to the UseSafeWeb AdGuard resolver so domains can be resolved and filtered. The Experiment-1 design does not require persistent identifiable DNS/domain history and does not provide a browsing-history dashboard.

Before the first participant, the deployed server must be verified to have:
- persistent identifiable query logging OFF;
- file query logging OFF;
- identifiable per-client statistics OFF/excluded unless specifically justified;
- client-IP anonymisation ON wherever an operational record can contain addresses;
- EDNS Client Subnet OFF;
- Quad9 `https://dns10.quad9.net/dns-query` as the encrypted upstream.

Do not publish a generic “no logs” claim; describe only the configuration that has actually been verified.

### Experiment information collected

The experiment records only what is needed to determine whether the setup is useful and self-service, such as:
- participant ID;
- child age band/stage, not exact date of birth;
- iPhone/Android and new/existing-phone path;
- whether relevant safeguards were already present or completed;
- baseline-protection activation;
- support/intervention minutes and reason;
- abandonment reason;
- understanding of major protection gaps;
- 14-day protection state.

It does not use the child's browsing/domain history as an experiment metric.

### Retention

- identifiable DNS/domain history: not retained as an Experiment-1 product/research record;
- diagnostic DNS logs: only if necessary for a specific fault, time-boxed and deleted after resolution;
- parent contact details: retained only through the 14-day follow-up, then deleted promptly and no later than 30 days after that participant's follow-up;
- pseudonymous participant-level metrics: retained through experiment analysis, then aggregated/anonymised and participant-level records deleted within 90 days after Experiment 1 closes;
- only aggregate/anonymised findings may be retained in the project repository.

### Who receives the data

Experiment-1 child-linked DNS traffic is limited to:
1. the UseSafeWeb AdGuard resolver hosted on Microsoft Azure West Europe (Netherlands); and
2. Quad9's non-ECS encrypted DNS upstream.

No US UseSafeWeb node is used for Experiment 1. No separate advertising, analytics, payment, CDN/proxy, email/scheduling or research-data SaaS processor is currently part of the pilot.

### Protection Map labels

- **Protected — verified:** UseSafeWeb can directly verify the protection state.
- **Configured — parent confirmed:** you confirm that a native/service safeguard is configured.
- **Action needed:** a relevant safeguard still requires action.
- **Not covered:** UseSafeWeb cannot provide or verify that protection.

### Your choices

Participation is voluntary. You can stop using the service or leave the experiment. Where applicable, you can ask for correction or deletion of participant/contact information that is still retained. Removing the DNS configuration stops UseSafeWeb baseline DNS protection on that device.

### Controller and UK representative

Controller: **individual established in the Netherlands**.  
Controller contact: **[insert before pilot]**.  
UK representative: **[insert before pilot, or document a valid Article-27 exception before use]**.

These contact details must be completed before the first real England participant.

## Child-readable explanation

**Your parent has turned on some safety settings for this phone.**

UseSafeWeb can block some websites at the domain level and helps your parent set up other phone/app safety controls. It does **not** read your messages, track your location, or look inside your social-media posts. It also cannot block every harmful thing online.

For this test, UseSafeWeb is designed not to keep a personal list of the websites/domains you visit. If something breaks, a small amount of technical information may sometimes be used briefly to fix the problem and then deleted.

If something you need is blocked or you want to understand what the protection does, tell your parent so the setting can be reviewed.

## Release gate

This notice becomes **READY** only after:
1. controller contact details are inserted;
2. UK-representative details are inserted or a valid documented exception is approved;
3. the deployed Azure/AdGuard configuration is directly verified;
4. the wording about logging/recipients is checked against that verified configuration.
