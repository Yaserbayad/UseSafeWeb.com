# TSK-0320 — Protection State Model and Copy Rules

**Task:** TSK-0320 — Freeze the protection-state model and copy rules  
**Acceptance:** ACC-0320  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 STATE/COPY CONTRACT / IMPLEMENTATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0315 service blueprint + TSK-0229 accountless data contract + TSK-0408 DNS evidence contract + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

This contract freezes a **truthful provisional evidence/state vocabulary**, not behaviorally validated wording. Real-participant L3 remains deferred through 2027-08-27 or earlier explicit owner reactivation. No representative-parent evidence currently proves that these labels are optimally understood, that the Protection Map improves comprehension, or that the states/copy minimize abandonment/support burden. `RSK-0002` remains OPEN.

This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, participant processing, legal completion, payment, public release or launch.

## 1. Core principle

The Protection Map is an **evidence map, not a safety score**.

It must answer, for each applicable layer:

1. What state is this layer in now?
2. What evidence supports that state?
3. What can UseSafeWeb truthfully claim?
4. What is the next action, if any?
5. What limitation remains?

There is no overall “safe / unsafe” or “100% protected” state. Completion of the setup journey does not force every layer into a positive state.

## 2. Canonical user-visible state model

The following six user-visible states are frozen for the provisional L4 baseline. Internal implementation enums may differ later, but must preserve these semantics exactly.

### S1 — Protected — verified

**Meaning:** UseSafeWeb has current technical evidence that the intended supported protection mechanism is active for this layer in the current supported context.

**Minimum evidence rule:**

- an owning technical capability defines a valid verifier for the exact supported platform/mechanism;
- current verification succeeds against that mechanism;
- no current evidence known to the verifier contradicts the result;
- the state is not inferred merely from parent confirmation, profile/configuration presence, DNS resolution through an unknown path, or a previous session.

**Current permitted use:** the accepted DNS layer on exact supported/tested combinations when the TSK-0408/TSK-0409 verification contract is satisfied. Other layers may use S1 only after their owning task proves an equivalent system-verification method.

**Default primary copy:** `Verified`

**Supporting copy:** `UseSafeWeb verified this protection step is active on your current setup.`

**Prohibited copy:** `Fully protected`, `Safe`, `Everything is blocked`, `Your child is protected`, or any wording that extends beyond the verified mechanism.

### S2 — Set up — parent confirmed

**Meaning:** The parent states that the safeguard/configuration is set up, or the setup step was completed, but UseSafeWeb does not hold sufficient technical evidence to call the protection state verified.

**Evidence rule:**

- parent confirmation or completion of the instructed action is present;
- system verification is unavailable, not applicable, or has not successfully completed;
- there is no known contradiction that requires S5 Uncertain/error.

**Default primary copy:** `You confirmed this is set up`

**Supporting copy:** `UseSafeWeb has not independently verified this setting.`

**Prohibited copy:** `Verified`, `Protected`, `Confirmed by UseSafeWeb`, or an equivalent system-verification implication.

This is the normal positive state for native-device or external-service safeguards where the current product cannot technically verify the resulting platform/service state.

### S3 — Action needed

**Meaning:** The layer is applicable, but the required safeguard is not currently complete/active, verification failed in a way with a known corrective path, or the user has not completed the necessary step.

**Evidence rule:** at least one is true:

- applicable setup has not started/completed;
- the user skipped/declined an applicable required step;
- a deterministic failure has a safe known next action;
- a previously active configuration was changed and needs reconfiguration/reverification.

**Default primary copy:** `Action needed`

**Supporting copy:** `Finish this step before relying on this protection layer.`

Where a specific corrective action is known, replace generic supporting copy with the exact action.

**Prohibited copy:** any positive protection/verification claim.

### S4 — Not covered

**Meaning:** UseSafeWeb does not provide or currently support this protection capability for the applicable device/service/path, or no approved relevant safeguard exists for this branch.

**Evidence rule:**

- current supported-scope/matrix explicitly excludes the combination/capability; or
- the relevant service step has no approved applicable safeguard; or
- the capability is intentionally outside current product scope.

**Default primary copy:** `Not covered`

**Supporting copy:** `UseSafeWeb does not cover this on your current setup.`

When the reason is simply not applicable rather than unsupported, use reason-specific supporting copy such as `No supported safeguard applies to this step.` while retaining S4 semantics.

**Prohibited copy:** presenting Not covered as a technical failure, or implying that another layer compensates for the missing protection unless directly proven.

### S5 — Status uncertain / error

**Meaning:** UseSafeWeb cannot safely determine whether the intended protection mechanism is currently active, or current evidence is conflicting/incomplete because of an error, bypass possibility, unsupported interaction, timeout or environmental change.

**Evidence rule:** at least one is true:

- verification is inconclusive;
- current evidence conflicts;
- a VPN/app/browser/network/device-management path may override or bypass the intended mechanism and current detection is insufficient;
- a technical error prevents trustworthy classification;
- a previously verified context materially changed and has not been reverified.

**Default primary copy:** `Status uncertain`

**Supporting copy:** `We can’t verify this protection right now. Check it before relying on this layer.`

For a known technical error, a concise reason may replace the first sentence, but the copy must still avoid a protection claim.

**Prohibited copy:** retaining S1/S2 merely because setup previously succeeded.

### S6 — Removed

**Meaning:** The safeguard/UseSafeWeb configuration was intentionally removed/reset or evidence establishes that the formerly configured layer is no longer active.

**Evidence rule:**

- an approved removal/reset operation completed; or
- the user confirmed removal where system verification of removal is unavailable, with no contrary evidence.

**Default primary copy:** `Removed`

**Supporting copy for UseSafeWeb DNS:** `UseSafeWeb DNS is no longer active on this device.`

**Supporting copy for another layer:** `This protection step is no longer active.`

**Prohibited copy:** continuing to show verified/parent-confirmed protection after removal.

S6 is intentionally distinguishable from S3 during the current journey so the user understands that protection was actively removed. Because the baseline is accountless, a later fresh journey need not persist historical “removed” status; it re-evaluates current applicable state from available evidence.

## 3. Internal `not_started` state

`not_started` may exist as an internal journey state before an applicable layer has been attempted. In the user-facing Protection Map it maps to **S3 — Action needed** when the layer is applicable.

Do not create a seventh positive/neutral label merely to make an incomplete applicable layer look less consequential.

## 4. State precedence

When more than one candidate state could apply, use this precedence so the UI cannot preserve an optimistic stale state:

1. **S6 Removed** — when current evidence establishes intentional removal.
2. **S5 Status uncertain/error** — when current evidence conflicts or trustworthy classification is unavailable.
3. **S1 Protected—verified** — only with current qualifying system evidence and no contradiction.
4. **S2 Set up—parent confirmed** — positive parent/configuration evidence without system verification and without contradiction.
5. **S3 Action needed** — applicable but incomplete/failed with known next action.
6. **S4 Not covered** — unsupported/out-of-scope/not-applicable branch as defined by current supported-scope rules.

S4 is scope classification rather than a chronological state; apply it before presenting setup actions when the current combination/capability is explicitly unsupported. The precedence above governs competing operational evidence, not a requirement to attempt an unsupported branch.

## 5. Allowed transitions

### Generic applicable layer

- `not_started` → S3 Action needed
- S3 → S2 after parent-confirmed completion where no system verifier exists
- S3 → S1 only after a valid system verifier succeeds
- S2 → S1 if later system verification succeeds
- S1/S2/S3 → S5 if evidence becomes conflicting/inconclusive or context changes materially
- S5 → S1 if re-verification succeeds
- S5 → S2 only when the contradiction/error is resolved and the remaining evidence is parent confirmation rather than system verification
- S1/S2/S3/S5 → S6 after approved removal/reset
- S6 → S3 when the user explicitly starts configuring the layer again
- Any applicable state → S4 only when authoritative scope/support rules are changed/re-evaluated to make the branch unsupported/not covered; do not use S4 to hide a failed supported setup

### DNS-specific transitions

For exact TSK-0408/TSK-0409 supported DNS mechanisms:

- entered/installed configuration → S2 or an internal configured-unverified state; never S1 from presence alone;
- successful current synthetic/technical verification of the intended supported path → S1;
- deterministic failed verification with known repair → S3;
- bypass/conflict/timeout or inability to determine intended resolver path → S5;
- profile/provider removal/reset → S6;
- after S6, normal DNS working does **not** restore S1; it confirms recovery only.

## 6. Reverification triggers

A previous S1 state must not be treated as indefinitely durable. Re-evaluate when the current evidence context materially changes, including when detectable/applicable:

- device/platform mechanism changes;
- UseSafeWeb DNS profile/provider is reinstalled, replaced or removed;
- VPN, browser/app secure DNS, Private Relay or equivalent network-control context changes;
- network/environment changes where the supported-matrix contract says behavior can differ;
- certificate/service configuration changes;
- verifier reports a conflicting or failed result.

No fabricated universal time-to-live for “verified” is introduced here. In the accountless baseline, verification is primarily a current-session/current-check truth claim rather than durable per-device history.

## 7. Layer-specific truth rules

### Phone / native safeguard layer

- Default positive state is S2 unless an owning platform capability later proves system-verifiable evidence.
- “Already configured” can become S2 only after explicit parent confirmation or approved evidence; it is not silently assumed.
- Unsupported OS/device policy becomes S4.
- Conflicting/unknown state becomes S5.
- Turning the safeguard off/removing it becomes S6 if known in the current journey.

### Internet / UseSafeWeb DNS layer

- S1 is permitted only for exact supported mechanisms with current TSK-0408/TSK-0409-compliant verification.
- Android native Private DNS hostname entry and Apple profile presence alone are not S1.
- VPN/browser/app/network bypass possibility with insufficient detection is S5, not S1.
- Unsupported device/network/mechanism is S4.
- Removal/reset is S6 and withdraws the UseSafeWeb DNS protection claim.

### Services layer

- Default positive state is S2 because service safeguards are normally parent-confirmed unless a later approved technical verifier exists.
- No approved relevant safeguard / unsupported service is S4.
- Known incomplete applicable step is S3.
- Conflicting or stale guidance that prevents safe classification is S5.
- Parent undo/removal during the current journey may become S6.

## 8. Protection Map composition rule

The Protection Map displays each applicable layer independently. It does **not** collapse states into a single score or overall safety badge.

Recommended structure:

- layer name;
- one of S1–S6;
- one sentence explaining evidence/limitation;
- one next action when action is possible;
- a short “what this does not cover” disclosure when material.

### Overall completion copy

If the journey reaches its end, use copy such as:

`Setup complete. Review what UseSafeWeb verified, what you confirmed, and what is not covered.`

Do not use:

- `Your child is safe`;
- `Fully protected`;
- `Protection complete` when material S3/S4/S5 states remain;
- an all-green visual treatment that makes S2 look equivalent to S1.

Completion is a journey event, not evidence that every protection layer is active.

## 9. Copy grammar rules

1. **Name the evidence actor.** Use `UseSafeWeb verified...` only for S1; use `You confirmed...` for S2.
2. **Use present tense only for current evidence.** Do not turn a historical setup event into a current protection claim.
3. **Do not overclaim outcomes.** Prefer `DNS filtering is verified active` over claims about everything a child can access.
4. **State uncertainty explicitly.** Do not bury S5 behind a success icon or generic “try again later.”
5. **Treat unsupported as honest scope.** S4 is not a defect that must be cosmetically converted to success.
6. **Explain removal consequence.** S6 states that the layer is no longer active.
7. **Separate setup completion from protection evidence.** A completed journey can contain S2/S3/S4/S5/S6.
8. **Avoid surveillance language.** No copy implies UseSafeWeb watches browsing, messages, location, contacts, photos or social content.
9. **Avoid universal platform language.** DNS copy must remain compatible with Android DoT-hostname and Apple DoH-profile asymmetry.
10. **Locale parity:** translated copy must preserve evidence strength and limitation semantics; translation must not strengthen a claim.
11. **No legal/market implication from language:** Turkish/Arabic copy cannot imply official Turkish/Arabic-market support absent the separate activation gate.
12. **No behaviorally validated claim:** until L3 evidence exists, copy/design rationale must not say users “understand”, “prefer”, “find easy”, or equivalent proven-behavior wording.

## 10. Testable assertions

A later implementation/QA suite must be able to prove at least these assertions:

1. Parent confirmation alone never yields S1.
2. Profile/provider presence alone never yields S1.
3. A successful approved system verifier can yield S1 only for its exact supported combination.
4. Conflicting/inconclusive evidence demotes a positive state to S5.
5. Removal immediately removes the active protection claim and yields S6 in the current journey.
6. Unsupported combinations display S4 and do not expose fake setup steps.
7. Failed supported setup with a repair path displays S3 rather than S4.
8. A completed journey may contain any mixture of S1–S6 consistent with evidence.
9. The UI never renders parent-confirmed S2 using copy that says `Verified`.
10. DNS verification never requires storing user browsing/query history or persistent device identity.
11. A network/device mechanism change invalidates stale S1 when the owning supported-matrix contract requires re-verification.
12. Fresh accountless journeys do not rely on persistent historical protection-state profiles.
13. Every translated label/supporting sentence preserves the same evidence strength.
14. No state/copy implies complete safety or surveillance capability.

## 11. Owner/governance boundaries

This state contract does not authorize:

- adding a new supported OS/network/service combination;
- inventing a verifier for native/service controls;
- retaining per-device protection history/account dashboards;
- weakening/removing Not covered or uncertainty disclosures for conversion reasons;
- approving legal/safeguarding claims or residual risks;
- public production profile/app release;
- real-participant activation;
- LG-05/LG-06/build/launch progression.

Material change to evidence strength, state semantics, account persistence, or complete-safety claims requires impact review and current authority.

## 12. ACC-0320 result

ACC-0320 requires exact evidence and transition rules for protected/verified, configured/parent-confirmed, action-needed, not-covered, uncertain/error and removed, with no confirmation masquerading as verification.

This contract defines all six states, evidence thresholds, state precedence, generic and DNS-specific transitions, reverification triggers, layer-specific usage, exact default copy, prohibited copy, composition rules and fourteen testable assertions. Parent confirmation and system verification remain structurally distinct.

**TSK-0320 result: PASS candidate subject to independent verification and runtime read-back.**
