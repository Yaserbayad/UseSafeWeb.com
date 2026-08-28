# UseSafeWeb — Experiment 1 Participant Communication Templates

**Task:** TSK-0167  
**Stage:** L2 preparation for Experiment 1  
**Status:** INTERNAL PREPARATION ONLY — NOT FOR PARTICIPANT USE  
**Date:** 2026-08-28

## Release boundary

These templates prepare the invitation, scheduling, reminder, 14-day follow-up, and withdrawal communications required by TSK-0167. They do **not** authorize recruitment, participant processing, live facilitation, child-linked DNS activation, or public use.

Under CR-0002 / DEC-0049, the deferred TSK-0221 notice-approval/release dependency is conditionally satisfied only for this internal preparatory artifact through 2027-08-27. The final controller contact and UK-representative contact/approved exception route remain unresolved. Therefore:

- every participant-facing template below remains **INTERNAL / NOT FOR PARTICIPANT USE**;
- `{{CONTROLLER_CONTACT}}` must be replaced with the current approved controller contact before release;
- `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}` must be replaced with the current approved UK representative contact or the approved participant-facing route after a valid exception decision, where applicable;
- the final notice/release task must verify those contacts and approve participant use;
- no unresolved placeholder may be sent to a real participant.

**Current contact status at preparation time:** controller = individual established in the Netherlands; participant-facing controller contact = unresolved/deferred; UK representative/contact or approved Article-27 exception route = unresolved/deferred. This is the truthful current status and is not legal-compliance evidence.

## Common communication rules

All released versions must preserve the following rules:

1. participation is voluntary and the parent/caregiver may stop or withdraw;
2. there is **no payment, donation, subscription, supporter, or purchase ask** in Experiment 1;
3. the experiment tests the setup journey, not the parent;
4. the parent performs the real setup actions; support is bounded and recorded because assistance burden is part of the experiment;
5. UseSafeWeb does not provide complete online safety and is not a surveillance product;
6. never ask the participant to send passwords, authentication codes, private messages, contacts, photos, browsing/domain history, child name, or exact date of birth;
7. when a login is genuinely needed for a native/service safeguard, the parent enters credentials directly on their own device/service and does not disclose them to the facilitator;
8. use the approved qualification/recruitment route only after the applicable gates authorize it;
9. keep the 14-day follow-up and withdrawal/deletion route clear;
10. send only a version whose controller and UK-contact/approved-exception fields have been completed and release-approved.

---

## Template A — Invitation

**Internal subject/title:** Invitation to the UseSafeWeb first-phone setup study

Hello,

We are preparing a small UseSafeWeb study about making a child's first-smartphone safety setup simpler for parents/caregivers. The study focuses on a guided setup journey for supported iPhone and Android phones.

Taking part is voluntary. The study tests the setup journey, not you, and you can decide not to participate or stop later. There is no payment, donation, subscription, or purchase request in Experiment 1.

If you are invited through the approved recruitment process and choose to continue, you will first complete a short eligibility check. It asks only for broad setup information such as your caregiver role, first-phone stage, approximate phone timing, and iPhone/Android platform. It must not ask for the child's name, exact date of birth, school, precise location, messages, contacts, photos, social usernames, or browsing/domain history.

During a session, you will be asked to perform the relevant phone/service setup actions yourself. The facilitator may provide bounded help if you become blocked, but assistance is recorded because self-service burden is part of what the study measures. UseSafeWeb does not promise complete online safety and does not operate as a surveillance or browsing-history product.

A short follow-up is planned around 14 days after the setup session to check the protection state and the experience of keeping it in place.

To ask about the study or withdrawal, use the approved contact route below once this template has been released:

- Controller contact: `{{CONTROLLER_CONTACT}}`
- UK representative / approved participant-facing route where applicable: `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}`

**Internal release check:** Do not send while either required contact field is unresolved or while LG-03/LG-04/recruitment authorization is absent.

---

## Template B — Scheduling confirmation

**Internal subject/title:** UseSafeWeb study session — scheduling confirmation

Hello,

Your UseSafeWeb study session is scheduled for:

- Date/time: `{{SESSION_DATE_TIME}}`
- Session route/location: `{{APPROVED_SESSION_ROUTE}}`
- Expected duration: `{{EXPECTED_DURATION}}`

### What to prepare

Please have available:

- the supported iPhone or Android phone that is part of the approved study setup;
- the parent/caregiver access needed to change the relevant phone settings;
- access to the one relevant service/app if the approved journey requires a safeguard there;
- enough time to try the steps yourself without rushing.

Do **not** send us passwords, authentication codes, private messages, contacts, photos, browsing/domain history, or other unnecessary personal information. If a login is needed, enter it yourself on the relevant device/service.

Participation remains voluntary. You may cancel, reschedule, stop the session, or withdraw. There is no payment or purchase ask in Experiment 1.

The facilitator will let you try each step first. If you become blocked, bounded assistance may be provided and recorded. The facilitator must not silently complete your setup and count it as self-service success.

Questions, cancellation, or withdrawal:

- Controller contact: `{{CONTROLLER_CONTACT}}`
- UK representative / approved participant-facing route where applicable: `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}`

**Internal release check:** contacts populated and participant/recruitment gates actually satisfied before sending.

---

## Template C — Session reminder

**Internal subject/title:** Reminder — UseSafeWeb study session

Hello,

This is a reminder for your UseSafeWeb study session on `{{SESSION_DATE_TIME}}` via `{{APPROVED_SESSION_ROUTE}}`.

Please have the supported phone and the parent/caregiver access needed to change relevant settings. If a service login is required, enter it yourself on your own device. Do not send passwords, codes, private content, or browsing/domain history.

The study is voluntary and you may cancel, reschedule, stop, or withdraw. There is no payment, donation, subscription, or purchase ask.

During the session, you will try the setup steps yourself first. Bounded help may be provided if you become blocked, and that help is recorded as part of measuring how self-service the journey is. UseSafeWeb cannot provide complete online safety and does not inspect private messages or social feeds.

Questions, cancellation, or withdrawal:

- Controller contact: `{{CONTROLLER_CONTACT}}`
- UK representative / approved participant-facing route where applicable: `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}`

---

## Template D — 14-day follow-up

**Internal subject/title:** UseSafeWeb study — 14-day follow-up

Hello,

This is the planned follow-up around 14 days after your UseSafeWeb setup session.

The purpose is to check the approved study outcomes, such as whether the setup/protection state is still in place, whether you needed assistance, whether anything important was blocked or failed, and whether the main protection limits remain clear.

Please do **not** send browsing/domain history, private messages, screenshots containing unnecessary personal information, passwords, authentication codes, child name, exact date of birth, or other unrelated personal data. If a technical problem needs investigation, use the approved support/false-positive route so only the minimum necessary information is requested.

Participation remains voluntary. You may decline the follow-up or withdraw. There is no payment or purchase ask.

After the follow-up, parent contact details are retained only as long as needed for the follow-up and must be deleted promptly, no later than 30 days after that participant's follow-up, under the approved retention/deletion procedure. Participant-level pseudonymous metrics follow the separate Experiment-1 retention rule.

Questions or withdrawal:

- Controller contact: `{{CONTROLLER_CONTACT}}`
- UK representative / approved participant-facing route where applicable: `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}`

---

## Template E — Withdrawal acknowledgment

**Internal subject/title:** UseSafeWeb study — withdrawal acknowledged

Hello,

We acknowledge your request to stop/withdraw from the UseSafeWeb study.

No further study participation is required from you. If UseSafeWeb DNS protection is currently configured on the phone and you want to stop using it, follow the approved removal/reset instructions so normal DNS/internet resolution is restored. Withdrawal from the study and removal of the technical configuration are related but distinct actions; the participant's choice controls both where applicable.

Where applicable, you may request correction or deletion of participant/contact information that is still retained. The project must follow its approved retention/deletion procedure and record deletion verification without putting participant identity or private data into GitHub evidence.

Do not send passwords, authentication codes, private messages, contacts, photos, or browsing/domain history in connection with the withdrawal request.

There is no payment, cancellation fee, subscription, donation, or purchase consequence for withdrawing from Experiment 1.

Withdrawal/deletion contact route:

- Controller contact: `{{CONTROLLER_CONTACT}}`
- UK representative / approved participant-facing route where applicable: `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}`

---

## Template F — Reschedule / unable-to-attend acknowledgment

**Internal subject/title:** UseSafeWeb study — reschedule or cancel

Hello,

Your scheduled study session can be rescheduled or cancelled. Participation is voluntary and there is no penalty or payment consequence for cancelling.

If you want another session time, reply/use the approved scheduling route with a suitable availability window. Do not include unnecessary child or device personal information.

If you no longer want to take part, use the withdrawal route instead; no further participation is required.

Contact route:

- Controller contact: `{{CONTROLLER_CONTACT}}`
- UK representative / approved participant-facing route where applicable: `{{UK_REP_CONTACT_OR_APPROVED_EXCEPTION_ROUTE}}`

---

## Support boundary for all templates

Participant-facing communication, once legally/gate-approved, must describe support consistently with `EXPERIMENT_01_FACILITATOR_GUIDE.md` and `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`:

- ordinary help is bounded and recorded;
- the parent retains control of the device/action;
- assistance is not hidden as self-service success;
- technical/compatibility/false-positive issues use the approved narrow support route;
- genuinely necessary diagnostics use the exceptional diagnostic procedure rather than broad query-history collection;
- safety/privacy correction and safeguarding escalation are distinct from ordinary usability help;
- the project does not investigate safeguarding disclosures through product-support data collection.

## 14-day follow-up and retention boundary

- follow-up target: around 14 days after the setup session;
- parent contact details: delete promptly after follow-up and no later than follow-up + 30 days;
- participant-level pseudonymous metrics: aggregate/anonymise after experiment analysis and delete participant-level rows no later than Experiment-1 close + 90 days;
- GitHub: aggregate/anonymised findings only; no participant identity, contact information, credentials, or raw DNS/domain history.

## Withdrawal route boundary

A released version must give the participant a usable approved contact route for:

- cancelling before the session;
- stopping during a session;
- declining the 14-day follow-up;
- withdrawing from the experiment;
- requesting correction/deletion where applicable;
- obtaining approved removal/reset instructions if they want UseSafeWeb DNS protection removed.

Because the final controller and UK contact route are currently deferred, this artifact records the route structure and current status but **must not be used with real participants until those fields and the participant-facing release/gates are satisfied**.

## Canonical baseline used

- `EXPERIMENT_01_QUALIFICATION_SCREENER.md`, blob `d35d3e0abfc3882d648df3c0c7458e216853b592`.
- `EXPERIMENT_01_FACILITATOR_GUIDE.md`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`.
- `RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`.
- `PILOT_PRIVACY_NOTICE.md`, blob `331f263388dfacfa73b6e9e556277d4230864ce8`.
- CR-0002 / DEC-0049 legal-hold sequencing exception.
- WBS ACC-0167.

## ACC-0167 trace

| ACC-0167 requirement | Evidence in this artifact |
| --- | --- |
| Voluntary participation | Common rules and every relevant template |
| No payment ask | Common rules; invitation; scheduling; reminder; follow-up; withdrawal |
| What to prepare | Scheduling confirmation and reminder |
| Support boundaries | Common rules; scheduling/reminder; dedicated support-boundary section |
| 14-day follow-up | Invitation, follow-up template, retention section |
| Withdrawal route | Invitation, scheduling, reminder, follow-up, withdrawal acknowledgment, dedicated withdrawal section |
| Current contacts | Truthful current contact status is explicitly recorded; release placeholders define the exact contact fields still required. No fabricated controller/UK-representative contact is inserted. Under CR-0002 this is sufficient only for internal preparatory completion, not participant-facing release. |

**TSK-0167 acceptance disposition:** PASS candidate for internal preparatory scope under CR-0002, subject to independent audit and durable read-back. Participant-facing release remains prohibited until the deferred contact/notice/gate conditions are actually satisfied.
