# TSK-0335 — Protection Map and Coverage-Limit Interactions — Candidate

**Version:** 1.0.0  
**Status:** HUMAN_ONLY decision candidate; not accepted / not PASS  
**Task:** `TSK-0335 — Design Protection Map and coverage-limit interactions`  
**Current sequencing:** `DEC-0052 / CR-0005`  
**Visible product identity:** `SafeWeb`  
**Product boundary:** accountless-first; no overall safety score; no persistent dashboard/history

## 1. Purpose and authority

This candidate defines the interaction contract for the SafeWeb Protection Map and its coverage-limit disclosures. It does not create a new state model, safety score, dashboard, analytics profile, participant study, or implementation authority.

Pinned current sources:

- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md`, blob `1146f7622f434590dde1253d11f14fb6a87e19de` — six-state evidence semantics and precedence;
- `prototype/TSK-0324/UI_COMPONENT_RULES.md`, blob `0b7012a12070f7eccf45a1bbb2f453fde8507ff6` — Protection Map component, accessibility, responsive and no-score rules;
- `prototype/TSK-0325/SERVICE_BLUEPRINT.md`, blob `1701f5f7b13ac8f7fa3092e39005b3da7627c89f` — end-to-end journey and touchpoint ownership;
- `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md`, blob `4efb624005061e242e427994953d0fc00fcd745f` — `SCR-MAP`, Help, Limitations, removal/recovery and operational route behavior;
- accepted TSK-0330 flow candidate `design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md`, blob `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7` — Phone → Internet → Services truth and completion rules;
- accepted TSK-0334 support/recovery candidate `design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md`, blob `44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f` — support, false-positive, removal and reconfiguration interactions;
- `DEC-0052 / CR-0005` — no pre-product parent/user testing; later human comprehension validation begins only at L8 after LG-09.

## 2. Acceptance contract

TSK-0335 requires the prototype design to satisfy all of the following:

1. **Parent confirmation is never presented as verification.**
2. **Material gaps are exposed at the right time**, not hidden until after a misleading completion moment.
3. **Truth-state behavior is deterministic and internally/automatically testable.**
4. **Later L8 human-comprehension interaction points are preserved** without performing or fabricating human validation now.

This candidate defines the normative interaction and test contract needed to satisfy those requirements.

## 3. Protection Map information model

The Protection Map is an **evidence map, not a safety score**.

The visible map contains exactly the applicable current layers:

- `Phone`
- `Internet`
- `Service`

Each visible layer item contains, in this order:

1. **Layer name** — `Phone`, `Internet`, or `Service`.
2. **Exact state label** — one of the six frozen labels below.
3. **Evidence sentence** — what fact/evidence supports the state.
4. **Coverage/limitation sentence** — what the state does not establish when a material limitation exists.
5. **At most one immediate next action** — only when a safe/useful action exists.

The six visible states remain exactly:

| State | Visible label | Evidence meaning | Interaction consequence |
| --- | --- | --- | --- |
| S1 | `Verified` | Current qualifying SafeWeb technical evidence exists for this layer/context. | May show evidence basis; never imply whole-device/whole-child safety. |
| S2 | `You confirmed this is set up` | Parent completed/confirmed a step but SafeWeb has not independently verified it. | Must explicitly disclose non-verification; must not reuse S1 semantics. |
| S3 | `Action needed` | Applicable protection is incomplete/failed with a known safe next action. | Show one corrective action when known. |
| S4 | `Not covered` | Current capability/combination is unsupported, out of scope or has no approved safeguard. | Explain boundary; do not portray as technical failure or compensated gap. |
| S5 | `Status uncertain` | Current evidence is conflicting/incomplete or trustworthy classification is unavailable. | Explain uncertainty and safe next check when known; never retain stale positive emphasis. |
| S6 | `Removed` | The relevant SafeWeb/safeguard configuration was intentionally removed/reset or is known inactive. | Withdraw active protection wording and expose reconfiguration separately. |

No seventh user-visible completion/success state is introduced.

## 4. Confirmation versus verification interaction rule

S1 and S2 must remain unmistakably different in **text, evidence description and interaction behavior**.

### S1 — `Verified`

Required supporting pattern:

- state label: `Verified`;
- evidence sentence identifies the current qualifying SafeWeb evidence;
- where relevant, disclose that verification applies only to that layer/mechanism;
- action is normally absent unless recheck/troubleshooting is materially useful.

### S2 — `You confirmed this is set up`

Required supporting pattern:

- state label: `You confirmed this is set up`;
- evidence sentence states the parent completed/confirmed the step;
- mandatory disclosure: `SafeWeb has not independently verified this setting.` or an equivalent source-approved sentence with identical evidence strength;
- no verification icon/copy/badge/ARIA label may imply S1;
- the item cannot be promoted to S1 without separately qualifying technical evidence.

### Prohibited equivalence patterns

The design must not:

- use `Verified`, `SafeWeb confirmed`, `Protected`, or equivalent technical-proof wording for S2;
- render S1 and S2 with identical success copy/icon semantics that imply equal evidence strength;
- collapse both into a generic `Done`/`Complete` state;
- allow parent acknowledgement, navigation, elapsed time or page reload to promote S2 to S1.

## 5. Material-gap timing contract

A **material gap** is any current state or limitation that would change whether a reasonable user should rely on a protection layer or understand its scope. At minimum this includes S3, S4, S5, S6 and material limitations attached to S1/S2.

### 5.1 During setup

Do not defer a known material gap merely to preserve journey momentum.

- known supported repair needed → show `Action needed` when discovered;
- unsupported/out-of-scope tuple → show `Not covered` when applicability is established;
- conflicting/inconclusive evidence → show `Status uncertain` when detected;
- completed removal → show `Removed` immediately after the approved removal outcome;
- S2 non-verification limitation → disclose at the point the state is shown, not only in a footer or later help page.

The affected layer may continue independently from other layers only when the owning flow permits it. Continuing another layer must not visually erase or downgrade the gap.

### 5.2 On `SCR-MAP`

The final map must show every applicable layer independently, including mixed states. It must not:

- hide S3/S4/S5/S6 rows;
- sort positive rows above gaps in a way that implies an overall positive result;
- replace gaps with an all-green completion summary;
- require an extra `Finish` acknowledgement before material limitations become visible;
- show `Setup complete`, `All done`, `Fully protected`, `Safe`, `100% safe`, a score, shield/certification badge or equivalent whole-product success claim.

### 5.3 Before exit

If any material gap remains, the map itself is the disclosure point before exit. The user may still exit; SafeWeb must not force remediation solely to obtain a positive-looking completion screen.

When one safe immediate action exists, show at most one layer-specific action. Otherwise expose `Help` or `Limitations` without inventing a fix.

## 6. Layer-specific interaction rules

### 6.1 Phone

- parent-confirmed native safeguard normally displays S2;
- S2 always includes the non-verification disclosure;
- unsupported native safeguard displays S4;
- conflicting/unknown state displays S5;
- known disabled/removed state uses S6 where current journey evidence supports it;
- Phone state never certifies Internet or Service.

### 6.2 Internet

- S1 is allowed only from current qualifying SafeWeb DNS technical evidence;
- profile/hostname presence alone is never S1;
- VPN/Private Relay/browser/app resolver/managed policy/network conflicts with insufficient evidence use S5 or other source-authorized non-positive state;
- known repairable verification failure uses S3;
- unsupported route uses S4;
- approved removal produces S6 immediately and removes active SafeWeb DNS protection wording;
- neutral post-removal connectivity success does not restore S1.

### 6.3 Service

- zero current approved named services is valid;
- no-applicable/currently unsupported service path uses the source-authorized S4 outcome;
- parent-completed external-service setup is S2 unless a future approved technical verifier exists;
- service state never upgrades Phone/Internet state;
- no service name/recommendation is invented by this task.

## 7. Coverage-limit disclosure hierarchy

Use the smallest disclosure that preserves truth without hiding material scope.

### Level A — layer-local mandatory disclosure

Displayed within the affected map item when it changes interpretation of that state. Examples:

- S2: SafeWeb has not independently verified the setting;
- S1 Internet: verification establishes the intended SafeWeb DNS path, not complete content correctness or whole-device safety;
- S4: current setup/capability is not covered;
- S5: current evidence is insufficient/conflicting;
- S6: SafeWeb DNS is no longer active.

### Level B — contextual `Limitations`

Used when the user needs more detail about support scope, bypass possibilities or what a layer does/does not cover. Opening/closing Limitations is state-neutral.

### Level C — stable public compatibility/help

Used for durable general explanation that should not duplicate session-specific evidence. Navigation to/from stable public content must not manufacture or mutate protection state.

No material limitation may exist only at Level C if it is necessary to interpret the current map item truthfully.

## 8. Action contract

Each layer item exposes **zero or one** immediate action.

Permitted examples:

- S3: `Fix this step` / source-specific corrective action;
- S5: `Check this` or `Troubleshoot` when a current safe diagnostic exists;
- S4: `See limitations` when useful;
- S6: `Set up again` / `Reconfigure`;
- false-positive context while Internet remains technically verified: `Get help with a blocked site or service` without downgrading/upgrading the technical state merely from the report.

Actions must never:

- skip required verification;
- turn acknowledgement into evidence;
- silently mutate another layer;
- create an unrestricted bypass/allowlist;
- repeat an unchanged-condition verification loop;
- require a login/account/payment step before the current map can be understood.

## 9. Deterministic truth-state contract

The implementation must expose a deterministic internal state representation sufficient for automated checks without collecting participant/browsing history.

Minimum per-layer test representation:

- `layer`: `phone | internet | service`;
- `state`: `S1 | S2 | S3 | S4 | S5 | S6`;
- `evidence_class`: current system verification, parent confirmation, incomplete/repairable, unsupported/out-of-scope, conflicting/inconclusive, or removed;
- `reason_code`: stable non-personal code identifying the current rule/path;
- `primary_action`: zero or one deterministic action identifier;
- `material_limit_present`: boolean;
- `source_instruction_or_rule_id`: owning source ID when applicable.

### State precedence assertions

When competing evidence exists, automated logic must preserve the TSK-0320 precedence and scope rules:

1. S6 when current evidence establishes intentional removal;
2. S5 when current evidence conflicts or trustworthy classification is unavailable;
3. S1 only with current qualifying verification and no contradiction;
4. S2 with parent confirmation and no contradiction;
5. S3 when applicable/incomplete with a known action;
6. S4 for authoritative unsupported/out-of-scope classification.

S4 applicability is resolved before offering setup when authoritative support rules already establish the branch is unsupported.

### No optimistic persistence

A previous positive state must not survive a current contradiction, removal, material context change or lost transient state merely because the earlier screen showed success.

## 10. Deterministic test matrix

| ID | Scenario | Required result |
| --- | --- | --- |
| `TC-0335-01` | Phone parent-confirmed | Phone=S2; explicit non-verification disclosure; never S1. |
| `TC-0335-02` | Internet qualifying technical verification succeeds | Internet=S1 with bounded evidence sentence; no overall safety claim. |
| `TC-0335-03` | DNS configured/present but not technically verified | Internet must not be S1; use current truthful non-S1 state. |
| `TC-0335-04` | Known repairable verification failure | Internet=S3; one corrective action; gap visible immediately and on map. |
| `TC-0335-05` | Conflicting VPN/resolver/network evidence | Internet=S5; stale S1 removed; safe check/help only. |
| `TC-0335-06` | Unsupported device/service tuple | Affected layer=S4; no speculative workaround; limitation visible at discovery point and map. |
| `TC-0335-07` | SafeWeb DNS removed | Internet=S6; active DNS-protection wording withdrawn; reconfigure separate. |
| `TC-0335-08` | Removal followed by neutral connectivity success | Internet remains S6; connectivity recovery does not become S1. |
| `TC-0335-09` | Zero approved external services | Service=S4/source-authorized not-covered outcome; journey may complete with mixed states. |
| `TC-0335-10` | Mixed Phone=S2, Internet=S1, Service=S4 | All three labels/evidence remain independently visible; no combined success score/badge. |
| `TC-0335-11` | Help/Limitations opened and closed | State representation unchanged; return to prior map context. |
| `TC-0335-12` | False-positive report while DNS path remains verified | Report acknowledgement alone does not mutate S1; filtering limitation/support path remains explicit. |
| `TC-0335-13` | Parent clicks acknowledgement/next/exit | No state promotion; acknowledgement is not evidence. |
| `TC-0335-14` | Material context change after earlier S1 | Reverification/uncertainty rule applies; optimistic stale S1 cannot persist. |
| `TC-0335-15` | Lost transient journey state | No prior S1/S2 reconstructed from hidden persistence; clean restart/re-evaluation. |
| `TC-0335-16` | RTL/mobile rendering of mixed states | Same labels/evidence strength/actions; no color-only meaning or hidden limitation. |

## 11. Later L8 human-comprehension interaction points

This task does **not** perform human testing. It preserves stable interaction points so later L8 validation can test comprehension on the fully working product without redesigning the evidence model first.

The following interaction points must remain observable in the integrated product unless later owner-approved authority changes them:

- `L8-PT-01` — distinguish `Verified` from `You confirmed this is set up`;
- `L8-PT-02` — identify which layer has a material gap in a mixed-state map;
- `L8-PT-03` — explain what `Not covered` means without assuming another layer compensates;
- `L8-PT-04` — explain what `Status uncertain` means and what action is safe next;
- `L8-PT-05` — understand that DNS-path `Verified` is not a whole-device/whole-child safety guarantee;
- `L8-PT-06` — understand the consequence of `Removed` and that neutral connectivity recovery is not SafeWeb verification;
- `L8-PT-07` — distinguish false-positive/content-correctness support from DNS-path technical verification;
- `L8-PT-08` — find the appropriate next action/Help/Limitations path without the interface hiding the gap.

These identifiers are **future validation hooks**, not evidence that comprehension has occurred. TSK-0335 cannot PASS based on assumed user understanding.

## 12. Accessibility, responsive and localization contract

Protection Map acceptance must preserve current TSK-0324 behavior:

- explicit textual state labels; color/icon is supplemental only;
- logical heading/order and keyboard focus behavior;
- 320 px single-column usability and no page-level horizontal overflow;
- text usable at 200% resize;
- target sizes/focus indicators preserved;
- English/Turkish/Arabic/RTL preserve evidence strength and state distinctions;
- `SafeWeb`, domains and technical endpoints remain LTR/untranslated where they appear;
- material limitations remain in reading/focus order and are not hidden in hover-only/tool-tip-only UI.

Future production shell work must also retain the already-recorded integrated-product accessibility notes for live-region scoping and bypass/skip navigation when repeated navigation exists.

## 13. Privacy and instrumentation boundary

Deterministic truth-state/test markers are implementation/QA identifiers, not user tracking.

This design does not authorize:

- persistent per-user/device Protection Map history;
- browsing/DNS-query history collection;
- child/parent identity collection;
- analytics profiles or cross-session stitching;
- telemetry merely to prove later comprehension;
- public/session-specific status URLs.

Any later analytics/telemetry or human-study instrumentation requires its own current authority. L8 validation may observe the interaction points through approved study methods after LG-09; this task does not pre-authorize those methods.

## 14. Acceptance mapping

Current TSK-0335 WBS acceptance is covered as follows:

- **never labels parent confirmation as verification:** §§4, 6, 9, TC-0335-01/03/13;
- **exposes material gaps at the right time:** §§5–7, TC-0335-04/05/06/07/10;
- **supports deterministic internal/automated truth-state checks:** §§9–10;
- **preserves interaction points needed for later L8 human comprehension validation:** §11;
- **claims/accessibility/source currency/surface review basis:** §§1, 12–13.

## 15. HUMAN_ONLY decision boundary

This file is a prepared candidate only. It does not mark TSK-0335 PASS and does not claim Project Owner approval.

Recommended exact owner disposition:

`APPROVE TSK-0335 PROTECTION MAP COVERAGE-LIMIT INTERACTIONS`

Alternative:

`REVISE TSK-0335: <specific change>`

Until explicit owner disposition is received, TSK-0335 remains **WAITING / non-PASS**.