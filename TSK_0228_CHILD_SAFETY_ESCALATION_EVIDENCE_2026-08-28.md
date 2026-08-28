# TSK-0228 — Child-Safety Concern and Disclosure Escalation Evidence

**Task:** TSK-0228  
**Acceptance:** ACC-0228  
**Evidence date:** 2026-08-28  
**Result:** PASS

## Authority and dependency proof

The exact canonical WBS row defines TSK-0228 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0219`. ACC-0228 requires the procedure to distinguish product support from urgent safeguarding, list emergency/referral routes appropriate to England, limit data capture, and define owner escalation.

Historical/planning predecessor labels were not accepted by themselves.

- Current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly re-proves the retention/deletion boundary underlying TSK-0219.
- Current `PILOT_PRIVACY_NOTICE.md`, blob `331f263388dfacfa73b6e9e556277d4230864ce8`, directly re-proves TSK-0219's parent/child transparency, protection-limit language, and release conditions.

## Accepted artifact

`CHILD_SAFETY_ESCALATION_PROCEDURE.md`, blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`.

ACC-0228 mapping:

1. **Product-support boundary:** the procedure states that UseSafeWeb is not an emergency, safeguarding-investigation, counselling, or surveillance service and separates ordinary DNS/setup/support faults from suspected abuse, neglect, exploitation/grooming, or immediate danger.
2. **England-appropriate routes:** immediate danger routes to 999; non-emergency safeguarding concerns route to the child's local council children's social care team, with 101/online police reporting where appropriate; adult advice routes to the NSPCC Helpline; child/young-person support routes to Childline; online child sexual-abuse/grooming concerns may route to CEOP, with 999 taking precedence for immediate danger.
3. **Data minimisation:** the procedure forbids collecting child browsing/domain history, messages, photos, social content, location history, contacts, or device contents merely to investigate a concern; necessary referral data stays in a restricted operational channel and raw/personal disclosures are excluded from GitHub/analytics.
4. **Owner escalation:** the Project Owner is the internal lean-pilot escalation authority; immediate danger receives the emergency direction first, then immediate owner escalation, while non-immediate concerns leave ordinary troubleshooting and escalate as soon as practicable.

## Current official-source verification

The routes were reverified on 2026-08-28 against current official sources; no material contradiction requiring an artifact change was found.

- GOV.UK, `https://www.gov.uk/report-child-abuse`: current page says to contact the child's local council children's social care team for risk/abuse concerns, call 999 for immediate risk, and use online crime reporting or 101 when it is not an emergency; it also says certainty is not required before reporting a suspicion.
- GOV.UK, `https://www.gov.uk/report-child-abuse-to-local-council`: current service is explicitly for England and locates the relevant children's social care team from a postcode.
- NSPCC, `https://www.nspcc.org.uk/about-us/our-services/nspcc-helpline/`: current page lists 0808 800 5000 for adults concerned about a child's safety/wellbeing and advises police/local Children's Services if concern increases. The project procedure intentionally tells maintainers to re-check live opening/contact details rather than freeze service hours in end-user UI.
- NSPCC Childline, `https://www.nspcc.org.uk/about-us/our-services/childline/`: current page lists Childline 0800 1111 and describes the service as free support for children and young people.
- CEOP Safety Centre, `https://www.ceop.police.uk/Safety-Centre/Should-I-make-a-report-to-CEOP-YP/Should-I-make-a-report-to-CEOP-concerned-adult/`: current page says CEOP handles concerns that a child is being sexually abused or groomed online, does not use that route for ordinary bullying/fake-account/hacking concerns, and directs immediate danger to police on 999.

## Independent repository verification

GitHub Actions run `33153607319`, job `98791113929`, completed successfully on the repository-scoped `adguardvm` runner using an exact `main` checkout, `contents: read`, and no persisted checkout credentials.

Audit output:

- `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`
- `TSK_0219_DIRECT_PREDECESSOR_PROOF=PASS`
- `TSK_0228_ACCEPTANCE_CLASSES=4/4`
- `TSK_0228_ARTIFACT_BLOB=18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`
- `TSK_0228_INDEPENDENT_REPOSITORY_AUDIT=PASS`

## Boundary

This PASS verifies a safeguarding-routing boundary and preparation procedure only. UseSafeWeb does not become a safeguarding authority or emergency service, no real disclosure or participant data was processed, and no recruitment/legal/provider/validation-readiness gate was changed.
