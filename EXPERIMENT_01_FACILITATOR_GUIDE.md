# UseSafeWeb — Experiment 1 Facilitator Guide and Intervention Taxonomy

**Task:** TSK-0165  
**Stage:** L2 preparation for Experiment 1  
**Status:** protocol artifact only — does not authorise recruitment/activation  
**Reviewed:** 2026-08-27

## Frozen hypothesis

Qualified parents at the first-smartphone transition will value one guided safety journey enough to complete real configuration changes when it coordinates native controls, activates baseline protection, and makes remaining coverage gaps understandable. The experiment is intended to disprove the hypothesis if the orchestration adds more work than it removes.

Do not change this hypothesis, the activation definition, or decision thresholds during a wave except where an immediate safety/privacy issue requires the session/path to stop.

## Facilitator role

The parent performs the real user actions. The facilitator may observe, ask neutral clarification questions, explain an instruction after the parent becomes blocked, and provide bounded help. The facilitator must **not silently complete setup for the parent** and must not turn a difficult self-service step into an unrecorded concierge success.

Every intervention that helps a parent move forward is timed and classified.

## Session opening

1. Confirm the participant meets the approved screener; do not collect exact child DOB/name.
2. Explain that the session tests the setup journey, not the parent.
3. State that the parent should try each step first and say aloud when wording or actions are unclear.
4. Explain that help is available if they become blocked, but help will be recorded because self-service burden is part of the experiment.
5. Remind the participant that UseSafeWeb does not provide complete online safety or surveillance.
6. Do not recruit or activate a participant unless the current LG-03/LG-04 gates authorise it.

## Journey script

Follow the approved sequence from `EXPERIMENT_01_CONCIERGE_VALIDATION.md`:

1. **Minimal intake** — age/stage, iPhone/Android, new/already-used phone, one relevant service.
2. Present the personalised **Phone → Internet → Service** plan.
3. **Native safeguards first** — skip a safeguard that is already correctly configured rather than forcing repetition.
4. **Baseline protection** — parent performs the real AdGuard-backed DNS activation using the approved supported method.
5. **One relevant service safeguard** — only when genuinely applicable; do not invent a substitute task.
6. **Protection Map** — classify each relevant layer as `Protected — verified`, `Configured — parent confirmed`, `Action needed`, or `Not covered`.
7. Ask the parent to explain at least **two material coverage gaps** in their own words.
8. End without a payment ask.

## Intervention rule

Before helping with a non-safety issue:

1. observe the parent attempt the step;
2. identify the actual block;
3. start the intervention timer;
4. give the smallest assistance needed;
5. keep the device/action with the parent;
6. stop the timer when the parent can continue;
7. record category, duration, reason and outcome.

If the facilitator must take control or perform an action because the parent cannot do it, record that explicitly as substantial assistance; do **not** count the result as silent self-service success.

## Intervention taxonomy

Use one primary category per intervention and optional secondary notes.

| Code | Category | Use when | Examples | Classification consequence |
|---|---|---|---|---|
| U1 | Wording / comprehension help | Parent does not understand the instruction or label. | Explain what a step means without doing it. | Usability assistance. |
| U2 | Navigation / discovery help | Parent understands the goal but cannot find the correct OS/app setting. | Point to the current settings area after observing the block. | Usability assistance; platform guidance candidate. |
| T1 | Technical setup help | Parent reaches the right flow but the technical configuration fails or needs bounded diagnosis. | DNS profile/configuration verification, certificate/network issue. | Technical assistance; record failure cause. |
| C1 | Compatibility / false-positive recovery | A platform/network/app conflict or filtering false positive prevents progress. | Captive portal, VPN/alternate DNS conflict, legitimate domain blocked. | Compatibility/reliability signal; use approved recovery path. |
| S1 | Safety/privacy correction | Continuing the observed action would create a privacy, security or misleading-safety problem. | Stop a request to expose raw browsing history; correct a complete-safety misunderstanding before proceeding. | **Safety correction**, not ordinary usability help. Record separately. |
| G1 | Safeguarding escalation | A disclosure/concern crosses the boundary in `CHILD_SAFETY_ESCALATION_PROCEDURE.md`. | Immediate danger, abuse/grooming concern. | Stop ordinary facilitation as needed; use safeguarding procedure. Do not investigate. |
| O1 | Other bounded intervention | Necessary help not captured above. | Rare exception with clear description. | Review after wave; do not use as a catch-all to hide recurrent problems. |

## Mandatory intervention record

For every intervention record:

```text
Participant ID:
Journey stage:
Intervention code:
Reason / observed block:
Safety correction?: yes/no
Facilitator action:
Parent action after help:
Start UTC/time marker:
End UTC/time marker:
Active assistance minutes:
Outcome: continued / paused / abandoned / safety-stop
Did facilitator perform the user's action?: yes/no
If yes, why and what action:
Candidate journey/instruction defect:
Non-sensitive notes:
```

Do not include child browsing/domain history, child name, exact DOB, messages, contacts, photos, location or unnecessary account identifiers.

## Safety correction vs usability help

A **usability intervention** helps the parent understand or perform an otherwise authorised step and counts toward assistance burden.

A **safety/privacy correction** prevents or stops an unsafe, privacy-invasive, security-invalid or materially misleading action/interpretation. It must still be recorded, but it is not treated as evidence that the original journey was usable. If the correction reveals a design defect, pause/repair the affected path before further sessions where appropriate.

A **safeguarding escalation** is neither usability help nor a product-success event. Follow `CHILD_SAFETY_ESCALATION_PROCEDURE.md`.

## Prohibited facilitator behavior

- no leading the participant toward positive feedback;
- no performing steps off-camera/behind the scenes and recording them as parent completion;
- no skipping a failed step simply to reach full activation;
- no adding an artificial safeguard when the relevant service is unsupported/irrelevant;
- no changing the activation definition mid-wave;
- no payment/supporter ask in Experiment 1;
- no claim of complete safety;
- no child browsing-history collection as an experiment metric;
- no conversion of `Configured — parent confirmed` into `Protected — verified` without direct evidence.

## End-of-session record

Record the protocol's minimum outcome fields, including full activation, time to activation, total active human-assistance minutes, assistance categories, pause/resume, abandonment stage/reason, false-positive/compatibility issue, coverage-gap comprehension and follow-up state. Distinguish what was directly verified from what the parent confirmed.

## Wave review

After Wave A, aggregate interventions by category and stage. Identify:

- biggest intervention/abandonment clusters;
- median/mean active help time;
- recurring wording/navigation defects;
- technical/compatibility failures;
- safety corrections;
- steps the facilitator had to perform for participants.

Make one coherent journey refinement; do not broaden product scope or change the core hypothesis merely to improve the result.

## Canonical baseline used

- `EXPERIMENT_01_CONCIERGE_VALIDATION.md` — hypothesis, journey, intervention rules, metrics and waves.
- `CHILD_SAFETY_ESCALATION_PROCEDURE.md` — safeguarding boundary and routes.
- `PROTECTION_CLAIMS_CHECKLIST.md` — truth labels and fail-safe coverage claims.
- Frozen WBS ACC-0165 / REQ-0013 / REQ-0014 / CON-0025 / CON-0009 / INT-0005.

## Acceptance result

This guide preserves the frozen hypothesis, requires every intervention's duration and reason, distinguishes safety/privacy correction from ordinary usability assistance and safeguarding escalation, and explicitly prevents silent facilitator completion of the parent's task.
