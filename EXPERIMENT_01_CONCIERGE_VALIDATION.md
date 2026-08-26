# UseSafeWeb.com — Experiment 1: Concierge Behavioral Validation

**Date:** 2026-08-26  
**Status:** READY AS PROTOCOL; EXECUTION BLOCKED UNTIL `VALIDATION_READINESS_GATE.md` = PASS.  
**Purpose:** test the riskiest business assumption before building the MCP.

## 1. Hypothesis

Qualified parents at the first-smartphone transition will value one guided safety journey enough to complete real configuration changes when it coordinates native controls, activates baseline protection, and makes remaining coverage gaps understandable.

The experiment is designed to disprove the hypothesis if the orchestration adds more work than it removes.

## 2. Cohort

Recruit **20–30 qualified parents/caregivers in England**.

Qualification:
- responsible for setting up the child’s phone;
- child roughly 10–12, centred on the first independently used smartphone / transition to independent internet use;
- phone being obtained within about 30 days or obtained within about the previous 30 days;
- iPhone or Android;
- willing to make real appropriate safety-setting changes;
- not primarily seeking covert surveillance/maximal monitoring.

The 20–30 cohort is a directional behavioral-validation sample, not a statistically representative UK prevalence sample.

## 3. What is being tested

One job only:

> Help me set up my child’s first phone with sensible safeguards without making me figure out several disconnected systems myself.

Do not test:
- broad DNS features;
- full parental control;
- GROW/lifecycle automation;
- child app/account;
- payment willingness;
- paid acquisition;
- multi-child administration.

## 4. Concierge format

The product may be manually simulated behind the scenes. The parent must still perform the real user actions.

Sequence:

1. Minimal intake: age/stage, iPhone/Android, new/already-used phone, one relevant service.
2. Produce a personalised three-layer plan: **Phone → Internet → Service**.
3. Native safeguards first; skip anything already correctly configured.
4. Activate real AdGuard-backed baseline protection.
5. Configure one genuinely relevant service safeguard if applicable.
6. End with the Protection Map:
   - Protected — verified;
   - Configured — parent confirmed;
   - Action needed;
   - Not covered.
7. Ask the parent to explain at least two major coverage gaps in their own words.
8. End quietly; no payment ask in Experiment 1.

Human help is allowed only when the parent becomes blocked. The facilitator must not silently complete the setup for the parent.

## 5. Mandatory measurements

Per participant, record only structured minimum data:

- participant ID;
- qualification pass/fail;
- device family;
- new/existing-phone path;
- whether native safeguards were already present;
- whether at least one previously missing native/service safeguard was completed;
- baseline protection activation success;
- full activation yes/no;
- time to full activation;
- active human-assistance minutes;
- assistance category;
- pause/resume occurrence;
- abandonment stage/reason;
- whether parent says UseSafeWeb duplicated/added work;
- comprehension of at least two material coverage gaps;
- immediate baseline false-positive/compatibility issue;
- 14-day baseline-protection state;
- reason for disabling/breakage if not active.

Do not record browsing history or the domains visited by the child as experiment metrics.

## 6. Activation definition

Full activation requires all applicable items:

1. short intake complete;
2. real baseline protection active;
3. relevant native safeguard completed or correctly already present and confirmed;
4. at least one relevant external/service safeguard completed when applicable;
5. Protection Map reached.

Account creation, reading guidance, or DNS activation alone is not full activation.

## 7. Existing promising criteria

The experiment looks promising if the existing project gates are met:

- **≥60%** of qualified starters reach full activation;
- **≥50%** of activated users configure at least one previously missing native/external safeguard;
- **≥70%** still have baseline protection active after 14 days;
- **≤25%** abandon primarily because UseSafeWeb adds/duplicates work;
- **≥80%** correctly understand at least two major coverage gaps;
- **≤30%** require substantial live assistance after basic refinement.

These are project decision thresholds, not industry benchmarks.

## 8. Strong failure/kill evidence

After the initial test and one materially improved iteration:

- **<40%** full activation → strong pivot/no-go signal;
- **<25%** complete any previously missing non-DNS safeguard → orchestration value likely weak;
- majority of abandoners say Apple/Google/native controls are already sufficient or UseSafeWeb adds work → pivot/no-go;
- **>30%** require substantial live assistance after basic refinement → self-service model failing;
- **>30%** remove baseline protection within 14 days because of blocking/compatibility/friction → current protection implementation failing;
- serious privacy/security incident involving identifiable child DNS/browsing data → immediate stop.

## 9. Facilitation rules

- Do not lead participants toward positive responses.
- Do not explain a feature before observing whether the parent understands the current step, unless needed for safety/correct execution.
- Record each intervention and its duration.
- If the parent already configured something correctly, skip it rather than forcing repetition.
- If a service is irrelevant/unsupported, mark it accordingly; do not substitute an artificial task merely to complete the flow.
- Never claim complete online safety.
- Keep `verified` distinct from `parent-confirmed`.
- Do not collect child browsing history for debugging unless the readiness gate’s exceptional diagnostic procedure explicitly permits the minimum time-boxed data.

## 10. Experiment sequence

### Wave A — first 10 qualified participants

Objective: expose obvious journey and instruction failures.

Do not change the core hypothesis or activation definition mid-wave. Fix only clear usability/instruction defects after the wave unless a safety/privacy problem requires immediate stop.

### Controlled iteration

Review:
- biggest abandonment stage;
- assistance categories/minutes;
- redundant steps;
- platform-specific failures;
- false positives/compatibility;
- comprehension failures.

Make one coherent refinement of the journey. Do not add broad features.

### Wave B — remaining 10–20 qualified participants

Run the materially improved journey with the same primary metrics and decision gates.

## 11. Decision output

At completion produce:

1. cohort count and qualification funnel;
2. activation rate;
3. incremental-safeguard rate;
4. assistance rate and median/mean active help minutes;
5. primary abandonment reasons;
6. coverage-gap comprehension;
7. 14-day protection persistence;
8. device/platform failure breakdown;
9. whether the critical assumption passed, failed, or remains ambiguous;
10. explicit recommendation: continue to minimal MCP / modify and repeat / pivot / stop.

All canonical project results must be aggregate/anonymised. Do not commit participant identities or child-level browsing data to GitHub.

## 12. Current execution state

**DO NOT RECRUIT OR ACTIVATE REAL CHILD DNS PROCESSING YET.**

Execution begins only after `VALIDATION_READINESS_GATE.md` reaches PASS, including direct verification of deployed DNS logging/statistics settings, processors/upstream, controller/ICO-fee position and approval of the final LIA/DPIA.
