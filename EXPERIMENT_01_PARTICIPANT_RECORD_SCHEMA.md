# UseSafeWeb.com — Experiment 1 Pseudonymous Participant Record & Metric Schema

**Task:** TSK-0166  
**Acceptance:** ACC-0166  
**Version:** 1.0.0  
**Status:** PRE-EXPERIMENT TEMPLATE — contains no participant records  
**Applies to:** Experiment 1 concierge behavioral validation only

## 1. Purpose and boundary

This schema records only the minimum pseudonymous evidence needed to test whether qualified parents can complete the frozen UseSafeWeb first-phone setup journey without excessive duplication or facilitator assistance.

It implements the measurement contract in `EXPERIMENT_01_CONCIERGE_VALIDATION.md` and the minimum-dataset boundary in `VALIDATION_READINESS_GATE.md`.

This file is a **schema/template, not a data store**. No real participant record may be created until the validation-readiness gate authorises real England participants.

## 2. Record identity

Each real experiment record, when authorised, uses one opaque pseudonymous identifier generated for the experiment. The identifier must not encode a name, email address, phone number, exact date of birth, location or other identifying fact.

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `participant_id` | opaque pseudonymous string | yes | Join the participant's allowed experiment measurements without storing identity in this record. |
| `wave` | `A` or `B` | yes | Preserve the frozen two-wave design. |
| `qualification_result` | `pass`, `fail` | yes | Qualification funnel denominator. |
| `qualification_reason_code` | controlled non-identifying code or `not_applicable` | yes | Explain qualification outcome without free-text personal detail. |

A participant's contact details or identity-to-ID mapping, if operationally necessary for approved recruitment/follow-up, **must not be stored in this metric record or GitHub** and is governed by the separate privacy/retention controls.

## 3. Qualification and route fields

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `caregiver_setup_responsibility` | `yes`, `no` | yes | Confirm the participant is responsible for phone setup. |
| `child_stage_band` | `roughly_10_12_first_phone_transition`, `outside_target` | yes | Target the approved life stage without exact age/DOB. |
| `phone_timing_band` | `within_next_30_days`, `within_previous_30_days`, `outside_window` | yes | Qualification timing without exact purchase/date data. |
| `device_family` | `iphone`, `android` | yes | Device route. |
| `phone_state` | `new_phone`, `already_used_phone` | yes | Setup path. |
| `willing_real_changes` | `yes`, `no` | yes | Confirm willingness to perform real appropriate configuration changes. |
| `non_surveillance_fit` | `yes`, `no` | yes | Exclude requests primarily seeking covert/maximal monitoring. |
| `relevant_service_category` | controlled allowlisted service/app category or `none_applicable` | yes | Route one genuinely relevant service safeguard without account identifiers/usernames. |

## 4. Safeguard-state fields

Use only the controlled state values below. Do not add URLs, domains, account identifiers, screenshots containing personal data, or narrative browsing/activity evidence.

Allowed safeguard-state values:

- `already_present_parent_confirmed`
- `completed_during_session`
- `action_needed`
- `not_applicable`
- `not_covered`
- `failed`

| Field | Type | Required | Measurement purpose |
| --- | --- | --- | --- |
| `native_safeguard_state` | controlled safeguard-state value | yes | Native phone safeguard state/completion. |
| `baseline_dns_protection_state` | `activated_verified`, `activation_failed`, `not_attempted_stop`, `removed_during_session` | yes | Real AdGuard-backed baseline protection activation. |
| `service_safeguard_state` | controlled safeguard-state value | yes | One relevant external/service safeguard when applicable. |
| `protection_map_reached` | `yes`, `no` | yes | Required full-activation step. |
| `incremental_non_dns_safeguard_completed` | `yes`, `no`, `not_applicable` | yes | Test incremental orchestration value beyond DNS. |

`parent-confirmed` state is not technical verification. The record must preserve that distinction.

## 5. Activation, time and assistance

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `full_activation` | `yes`, `no` | yes | Primary activation outcome using the frozen activation definition. |
| `time_to_full_activation_minutes` | non-negative integer or `not_activated` | yes | Measure elapsed setup effort. |
| `active_assistance_minutes` | non-negative integer | yes | Measure facilitator burden. |
| `assistance_category` | `none`, `navigation_clarification`, `instruction_clarification`, `technical_troubleshooting`, `safety_correction`, `other_controlled` | yes | Classify intervention without narrative personal data. |
| `facilitator_completed_parent_action` | must be `no`; any `yes` invalidates the session for normal completion analysis and requires review | yes | Enforce REQ-0015: assistance must not silently complete the parent's task. |
| `pause_resume_occurred` | `yes`, `no` | yes | Identify journey interruption. |

If an intervention occurs, its active duration is counted in `active_assistance_minutes`; assistance is not hidden inside general session time.

## 6. Abandonment and duplication

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `abandoned` | `yes`, `no` | yes | Determine completion/abandonment. |
| `abandonment_stage` | controlled journey stage or `not_applicable` | yes | Locate friction without collecting narrative personal data. |
| `abandonment_reason_category` | `usesafeweb_added_or_duplicated_work`, `native_controls_sufficient`, `technical_failure`, `instruction_confusion`, `time_or_interruption`, `privacy_or_trust_concern`, `service_not_relevant`, `other_controlled`, `not_applicable` | yes | Test the primary duplication/friction risk. |
| `parent_reports_duplicated_or_added_work` | `yes`, `no` | yes | Direct RSK-0002 measurement. |

## 7. Comprehension

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `coverage_gap_1_understood` | `yes`, `no`, `not_tested_stop` | yes | First material gap comprehension. |
| `coverage_gap_2_understood` | `yes`, `no`, `not_tested_stop` | yes | Second material gap comprehension. |
| `two_gap_comprehension_pass` | `yes`, `no`, `not_tested_stop` | yes | Frozen comprehension metric. |

Do not store verbatim participant explanations in this record. The facilitator records only the structured comprehension result.

## 8. False-positive / compatibility evidence

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `immediate_false_positive_or_compatibility_issue` | `yes`, `no` | yes | Detect baseline-protection friction. |
| `issue_category` | controlled privacy-safe category or `not_applicable` | yes | Classify issue without domain/query history. |
| `support_case_id` | opaque case identifier or `not_applicable` | yes | Link to an approved privacy-safe support process when necessary. |
| `baseline_disabled_during_session_due_to_issue` | `yes`, `no` | yes | Measure removal/breakage impact. |

**Do not record the child's queried domain, browsing history, URL, account identifier, screenshot, message, location or other content in this metric schema.** Any genuinely necessary exceptional diagnostic process is separate, time-boxed and governed by the approved diagnostic-logging procedure.

## 9. Fourteen-day state

| Field | Type / allowed values | Required | Measurement purpose |
| --- | --- | --- | --- |
| `followup_14d_completed` | `yes`, `no`, `withdrawn` | yes | Define 14-day follow-up denominator. |
| `baseline_protection_14d_state` | `active`, `disabled`, `broken`, `unknown_no_followup`, `withdrawn` | yes | Frozen persistence metric. |
| `baseline_not_active_reason_category` | `blocking_or_false_positive`, `compatibility_or_network`, `user_choice`, `device_reset_or_replacement`, `technical_failure`, `other_controlled`, `not_applicable` | yes | Understand persistence failure without browsing data. |

No domain-level history is collected to prove the 14-day state; verification/parent confirmation must use the approved privacy-safe mechanism for the experiment.

## 10. Derived metrics — aggregate only

The following are computed from authorised participant records and reported only in aggregate/anonymised form in the canonical repository:

1. qualification funnel and cohort count;
2. full activation rate;
3. incremental non-DNS safeguard completion rate;
4. assistance rate plus median/mean active assistance minutes;
5. abandonment rate and primary reason categories;
6. duplicated/added-work rate;
7. two-gap comprehension rate;
8. immediate false-positive/compatibility issue rate;
9. 14-day baseline-protection persistence rate;
10. device-family failure breakdown.

The frozen behavioral thresholds remain those in `EXPERIMENT_01_CONCIERGE_VALIDATION.md`; this schema does not alter them.

## 11. Explicit prohibited fields

The participant metric record must contain **none** of the following:

- child name;
- exact child date of birth;
- school;
- child email address or phone number;
- precise or routine location;
- contacts/address book;
- messages or message content;
- photos/images of the child or device content;
- social usernames/handles or social-content history;
- browsing history, DNS query history, visited-domain history, URLs, top-domain lists or per-domain activity;
- parent/child advertising profiles;
- payment/card data;
- raw diagnostic logs;
- free-text notes capable of becoming an uncontrolled personal-data field.

The schema also does not include a child account or persistent behavioral profile.

## 12. Data handling and repository rule

- Real participant records are not committed to GitHub.
- GitHub receives only this empty schema/template, verification evidence and aggregate/anonymised findings.
- Pseudonymous participant-level metrics, once real-participant processing is authorised, are retained only through experiment analysis/decision and deleted within the approved retention window after Experiment 1 closes.
- Contact data, if needed for approved recruitment/follow-up, is kept outside this metric schema and deleted under the separate retention schedule.
- No collection starts merely because this template exists.

## 13. Acceptance trace

| Control | Implementation in this schema |
| --- | --- |
| ACC-0166 | Participant ID, qualification, device/path, safeguard states, activation, time, assistance, abandonment, comprehension, false-positive/compatibility and 14-day fields are all present; prohibited fields are explicitly excluded. |
| REQ-0013 | Wave A/B field and frozen protocol/threshold reference preserve the approved 20–30-participant experiment design. |
| REQ-0014 | No payment, paid-acquisition, broad DNS-feature, child-account or full-parental-control measurement is introduced. |
| REQ-0015 | Assistance duration/category is mandatory and `facilitator_completed_parent_action` must remain `no`. |
| CON-0025 | This remains a behavioral-validation artifact; it authorises no integrated product build. |
| CON-0009 | No invasive surveillance or behavioral monetisation fields are present. |
| INT-0005 | The record measures the frozen research decision question and smallest ethical evidence path. |
| RSK-0002 | Activation, abandonment and duplicated-work fields directly measure the primary validation risk. |

## 14. Gate statement

**Template preparation is permitted; real participant use is not.**

`VALIDATION_READINESS_GATE.md` must reach PASS before recruitment/activation or any real England participant record is created. This artifact does not change that gate, the frozen experiment protocol, or any legal/privacy requirement.
