# UseSafeWeb.com — Experiment 1 Qualification Screener

**Task:** TSK-0168  
**Acceptance:** ACC-0168  
**Version:** 1.0.0  
**Status:** PRE-EXPERIMENT TEMPLATE — do not use for recruitment until the validation-readiness gate is PASS

## Purpose

This short screener determines whether an already-invited parent/caregiver fits the frozen Experiment-1 cohort. It is intentionally minimal and must not collect a child name, exact date of birth, address/postcode, school, child contact details, social usernames or browsing/domain history.

Experiment 1 remains limited to 20–30 qualified England parents/caregivers, with Wave A first 10 and Wave B remaining 10–20. Recruitment or real participant processing is not authorised by this template.

## Instructions to facilitator / approved screener channel

- Ask only the questions below.
- Record only the controlled answer/result needed for qualification.
- Do not ask for the child's name or exact date of birth.
- Do not collect an address, postcode, school or precise location in this screener.
- Do not collect free-text descriptions of the child's online activity, browsing, messages, contacts, photos or social accounts.
- If a participant volunteers unnecessary personal information, do not copy it into the experiment record.
- The England cohort/geography must be established through the approved recruitment process without storing precise location in the experiment metric record.

## Qualification questions

### Q1 — Caregiver setup responsibility

**Are you the parent/caregiver who is responsible for setting up or helping set up the child's phone?**

Allowed answers:
- `yes`
- `no`

Qualification rule: `yes` required.

### Q2 — First-phone life stage

**Is this around the child's first independently used smartphone / transition to more independent internet use, roughly the 10–12 age stage?**

Allowed answers:
- `yes_target_stage`
- `no_outside_target_stage`

Qualification rule: `yes_target_stage` required.

Do not ask for the child's exact age or date of birth. Do not ask for the child's name.

### Q3 — Phone timing

**Which best describes the phone timing?**

Allowed answers:
- `within_next_30_days`
- `within_previous_30_days`
- `outside_window`

Qualification rule: one of the first two values required.

Do not collect an exact purchase, birthday or activation date.

### Q4 — Platform

**Which phone platform will be used for the setup?**

Allowed answers:
- `iphone`
- `android`
- `other_or_unknown`

Qualification rule: `iphone` or `android` required for the current Experiment-1 protocol.

### Q5 — Willingness to make real appropriate changes

**During the guided session, are you willing to make real, appropriate safety-setting changes on the phone/services when they are relevant?**

Allowed answers:
- `yes`
- `no`

Qualification rule: `yes` required.

This does not authorise payment, surveillance, account creation or any change outside the approved Experiment-1 journey.

### Q6 — Non-surveillance fit

**Are you mainly looking for a sensible first-phone safety setup rather than covert monitoring, reading messages, tracking location, or maximising surveillance?**

Allowed answers:
- `yes_sensible_safety_setup`
- `no_primarily_surveillance_request`

Qualification rule: `yes_sensible_safety_setup` required.

If the participant is primarily seeking covert/maximal surveillance, mark the participant not qualified. Do not collect details of the surveillance request.

## Qualification decision

A participant is `qualified` only when all of the following are true:

1. caregiver setup responsibility = `yes`;
2. first-phone life stage = `yes_target_stage`;
3. phone timing is within the approved ±30-day window;
4. platform = `iphone` or `android`;
5. willingness for real appropriate changes = `yes`;
6. non-surveillance fit = `yes_sensible_safety_setup`;
7. the approved recruitment process has already established eligibility for the England cohort without adding precise-location data to the experiment metric record.

Otherwise the result is `not_qualified`.

## Minimum output to the pseudonymous metric record

Only the following controlled outputs are transferred to `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md`:

- `qualification_result`;
- `qualification_reason_code`;
- `caregiver_setup_responsibility`;
- `child_stage_band`;
- `phone_timing_band`;
- `device_family`;
- `willing_real_changes`;
- `non_surveillance_fit`.

No child name, exact DOB, school, child contact, precise location, messages, contacts, photos, social username, browsing history or domain history is transferred.

## Reason codes

For a non-qualified result, record at most one primary controlled reason code:

- `not_setup_caregiver`
- `outside_first_phone_stage`
- `outside_phone_timing_window`
- `unsupported_or_unknown_platform`
- `not_willing_real_changes`
- `surveillance_primary_goal`
- `recruitment_eligibility_not_met`

Do not add free-text rejection notes.

## Non-goals

This screener does not test or ask about:

- payment willingness or card details;
- paid acquisition;
- broad DNS features;
- a child account;
- full parental-control administration;
- browsing history/domain history;
- private messages, contacts, photos or social content.

## Gate statement

**Creating this template does not authorise recruitment or participant processing.** `VALIDATION_READINESS_GATE.md` must be PASS before this screener is used with a real England participant.

## Acceptance trace

| ACC-0168 requirement | Screener evidence |
| --- | --- |
| Caregiver responsibility | Q1 |
| Age/stage | Q2, broad first-phone stage only |
| Phone timing | Q3, bounded ±30-day categories without exact dates |
| Platform | Q4 |
| Willingness for real changes | Q5 |
| Non-surveillance fit | Q6 |
| No exact DOB | Explicitly prohibited in instructions and Q2 |
| No child name | Explicitly prohibited in instructions and Q2 |
