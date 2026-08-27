# UseSafeWeb — Child-Safety Concern and Disclosure Escalation Procedure

**Task:** TSK-0228  
**Gate:** LG-03 Validation Readiness  
**Scope:** England pilot  
**Status:** operational boundary  
**Official routes reverified:** 2026-08-27

## Purpose and boundary

UseSafeWeb is a product/setup/support service, **not an emergency service, safeguarding investigation service, counselling service, or surveillance system**. Normal product support handles setup, DNS filtering, false positives, removal, compatibility and service faults. A concern or disclosure indicating possible abuse, neglect, sexual exploitation/grooming, or immediate danger is routed out of normal product support promptly.

The support role is to recognise the boundary, avoid obstructing or investigating the concern, give the appropriate official route, escalate internally to the Project Owner, and minimise personal-data collection.

## Triage

### A. Immediate danger or emergency

If a child is at immediate risk or urgent police/medical intervention is needed:

1. Tell the person to call **999** immediately.
2. Do not delay that instruction while gathering support details or troubleshooting UseSafeWeb.
3. Escalate the event to the Project Owner immediately after the emergency direction is given.
4. Record only the minimum non-sensitive operational fact that an emergency route was provided, unless further personal data is genuinely necessary for an authorised referral.

GOV.UK states to call 999 if the child is at immediate risk.

### B. Suspected abuse/neglect or child-safety concern that is not an immediate emergency

Route the parent/caregiver/adult to the **children's social care team at the child's local council**. GOV.UK's England service locates the appropriate council from a postcode. Where a non-emergency crime report is appropriate, GOV.UK also identifies **101** / online police reporting.

Do not require the person to prove abuse before giving the route. GOV.UK states that a suspicion can be reported.

### C. Adult wants safeguarding advice

An adult concerned about a child may contact the **NSPCC Helpline: 0808 800 5000**. The NSPCC states that its child-protection specialists advise people concerned about a child's safety or wellbeing and can take necessary action. Current opening/contact details must be checked on the live NSPCC page before publishing them in end-user UI because service hours can change.

### D. Child or young person wants confidential support

Direct the child/young person to **Childline: 0800 1111** and the current Childline online service. Childline describes the service as free and confidential for children and young people. Do not present UseSafeWeb support as a substitute.

### E. Online sexual abuse or grooming concern

For a concern that a child is being sexually abused or groomed online, the **CEOP Safety Centre** is an appropriate specialist reporting route for a concerned adult. CEOP states that it does not handle ordinary bullying, fake accounts, or account hacking through that reporting route. If the child is in immediate danger, use 999 instead.

## Product support vs safeguarding examples

| Situation | Route |
|---|---|
| Site is incorrectly blocked / DNS setup fails / profile needs removal | Normal UseSafeWeb product support. |
| Parent asks what DNS filtering can and cannot protect | Normal support + Protection Map / protection-claims checklist. |
| Parent reports disturbing content but no indication of abuse/danger | Normal support for product behavior; give appropriate general safety resource if requested, without investigating. |
| Parent or child says someone is abusing, exploiting, grooming, threatening, or neglecting a child | Safeguarding boundary: use the routes above; escalate to Project Owner. |
| Immediate threat/danger | 999 first; do not make UseSafeWeb support a gate. |
| Online sexual abuse/grooming | CEOP / police / local children's social care as appropriate; 999 if immediate danger. |

## Internal owner escalation

The **Project Owner** is the internal escalation authority during the lean pilot.

- Immediate danger: emergency direction first, then immediate owner escalation.
- Non-immediate safeguarding disclosure/concern: stop ordinary troubleshooting on the disclosure itself, provide the relevant official route, and escalate to the Project Owner as soon as practicable.
- If the concern also reveals a UseSafeWeb privacy/security incident, handle that technical incident separately; do not let technical incident handling replace the safeguarding route.
- Do not make unsupported legal conclusions about whether abuse occurred. Preserve the concern accurately and route it.

## Data-minimisation rules

1. Do not ask for child browsing/domain history to assess a safeguarding concern.
2. Do not solicit messages, photos, social-media content, location history, contacts, or device contents merely to investigate the allegation.
3. Do not ask for more identifying information than is necessary to provide the route or make an authorised referral.
4. If personal details are genuinely needed for a referral, keep them in the approved restricted operational channel, **not GitHub**.
5. The GitHub/evidence record may contain only a non-identifying event ID, date/time, broad category, route provided, owner escalation status, and non-sensitive disposition.
6. Do not promise confidentiality that UseSafeWeb cannot guarantee. Explain that an external safeguarding/emergency service may need relevant information when the person contacts it.
7. Do not preserve screenshots or raw disclosures in general product analytics or experiment datasets.

## Minimal internal record template

```text
Event ID:
UTC date/time:
Source: parent / child / other adult / unknown
Broad category: immediate danger / suspected abuse-neglect / online sexual abuse-grooming / other safeguarding concern
Immediate danger indicated: yes/no/unclear
Official route provided: 999 / local children's social care / 101-police / NSPCC / Childline / CEOP / other
Project Owner escalated UTC:
Any personal data retained outside GitHub because necessary for referral?: yes/no
If yes, restricted location/retention owner (no personal data here):
Product/privacy/security incident also opened?: yes/no + non-sensitive reference
Disposition / follow-up boundary:
```

## Current official England/UK sources

Reverified 2026-08-27:

- GOV.UK — Report child abuse: `https://www.gov.uk/report-child-abuse`
- GOV.UK — Report child abuse to a local council (England): `https://www.gov.uk/report-child-abuse-to-local-council`
- NSPCC — NSPCC Helpline: `https://www.nspcc.org.uk/about-us/our-services/nspcc-helpline/`
- NSPCC / Childline: `https://www.nspcc.org.uk/about-us/our-services/childline/`
- CEOP Safety Centre — concerned adult reporting guidance: `https://www.ceop.police.uk/Safety-Centre/Should-I-make-a-report-to-CEOP-YP/Should-I-make-a-report-to-CEOP-concerned-adult/`

Because contact routes and service hours can change, reverify these official sources before pilot activation and whenever the procedure is materially used after a long interval.

## Acceptance result

This procedure distinguishes normal product support from urgent safeguarding, provides current England-appropriate emergency/referral routes, minimises data capture, keeps personal/raw disclosures out of GitHub, and assigns internal escalation to the Project Owner. It therefore implements ACC-0228 without claiming that UseSafeWeb itself performs safeguarding investigations or emergency response.
