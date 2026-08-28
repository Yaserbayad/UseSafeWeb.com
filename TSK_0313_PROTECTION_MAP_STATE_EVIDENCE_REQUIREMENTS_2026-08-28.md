# TSK-0313 — Protection Map State and Evidence Requirements

**Task:** TSK-0313 — Specify Protection Map state and evidence requirements  
**Acceptance:** ACC-0313  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 PRODUCT REQUIREMENTS / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0041 DNS activation requirements + TSK-0144 service-guidance requirements + TSK-0146 accountless-first freeze + TSK-0320 canonical state/copy semantics + TSK-0229 accountless data contract + TSK-0315 service blueprint + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

This requirements contract defines how the Protection Map must represent evidence. It does **not** prove representative-parent comprehension, trust, usefulness or optimal wording/layout. `RSK-0002` remains OPEN and later contradictory L3 evidence must reopen affected assumptions.

This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real participants, legal completion, payment, public release or launch.

## 1. Authority split — avoid duplicate mutable state definitions

The Protection Map has two complementary authoritative contracts:

- **TSK-0320** owns the exact six-state semantic/copy model, precedence and transition meaning.
- **TSK-0313** owns the product requirement for applying those states across Phone / Internet / Services, including entry evidence, persistence/device boundary, unsupported behavior and testable examples.

TSK-0313 must not create competing labels or weaker evidence thresholds. If its examples conflict with TSK-0320, TSK-0320's exact state semantics govern and TSK-0313 must be corrected.

## 2. Protection Map purpose

The Protection Map is an **evidence summary**, not a safety score.

For each applicable layer it must show:

1. what protection/setup state the product can truthfully establish now;
2. what evidence actor supports that state — UseSafeWeb system evidence versus parent confirmation versus scope/unsupported evidence;
3. the key limitation that prevents a stronger claim;
4. the next action when one exists;
5. removal/recovery consequence where relevant.

The Map must never collapse Phone / Internet / Services into one green “safe” badge or imply complete online safety.

## 3. Required state set

Every applicable layer must resolve to one of the TSK-0320 semantic states:

- **S1 — Protected / Verified**
- **S2 — Set up / Parent confirmed**
- **S3 — Action needed**
- **S4 — Not covered**
- **S5 — Status uncertain / error**
- **S6 — Removed**

Internal implementation enums may differ, but user-visible meaning and evidence strength may not.

An internal `not_started` state is allowed before an applicable step is attempted; when shown in the Protection Map it maps to S3, not to a neutral/positive seventh state.

## 4. Entry/evidence rules by state

### S1 — Verified

Entry requires **current approved system evidence** for the exact supported mechanism/state and no known contradiction.

Never enter S1 from:

- parent confirmation alone;
- profile/provider/app/account/menu presence alone;
- prior-session history;
- journey completion alone;
- DNS success as evidence for native/service controls;
- an unsupported platform extrapolation.

Current strongest S1 use is the UseSafeWeb DNS layer on exact TSK-0041/0409-supported tuples after the approved verification semantics succeed.

### S2 — Parent confirmed

Entry requires parent confirmation that the relevant approved native/service safeguard is set up where no approved UseSafeWeb verifier exists and no contradiction is known.

S2 must explicitly communicate that UseSafeWeb did not independently verify the setting. Native Apple/Google controls and the current external-service safeguard use S2 as their strongest normal positive state unless a later separately approved verifier exists.

### S3 — Action needed

Entry when an applicable supported step is incomplete, skipped/declined, or has a deterministic failure with a safe known repair.

S3 must include the exact next action when known. It is not used for clearly unsupported scope; that is S4.

### S4 — Not covered

Entry when current authoritative product/support rules say the capability/device/service/path is unsupported, not applicable or outside the product scope.

S4 must not be used to hide a failure in a supported path. It also must not imply another layer automatically compensates for the gap.

### S5 — Status uncertain / error

Entry when evidence is inconclusive/conflicting or the product cannot safely determine the effective state, including unresolved VPN, Private Relay, browser/app custom DNS, network, device-management, stale-guidance or verification conflicts.

S5 must dominate stale optimistic state until the conflict is resolved and the relevant evidence is re-established.

### S6 — Removed

Entry when a previously active/configured safeguard is intentionally removed/disabled in the current journey, based on the strongest available removal evidence/confirmation.

S6 immediately withdraws the active protection/setup claim. Reconfiguration begins from S3 rather than restoring a historical positive state.

## 5. Layer-specific evidence requirements

### Phone — native safeguard

Source contract: TSK-0143.

- current positive default: S2 parent-confirmed;
- S1 unavailable unless a future native-control verifier separately passes its technical/privacy/accuracy requirements;
- already-configured parent confirmation may enter S2 without duplicate setup;
- `not sure` / unmatched current guidance enters S5 or a minimal check route;
- unsupported/policy-blocked device state enters S4/S5;
- disabling/removing the safeguard in the current journey enters S6 when known.

The Map must not imply that UseSafeWeb can see Screen Time, Family Link, messages, apps, location or other native-device state unless an approved capability actually provides that evidence.

### Internet — UseSafeWeb DNS

Source contracts: TSK-0041, TSK-0408, TSK-0409.

- configuration presence alone: not S1;
- current controlled verification of exact supported UseSafeWeb encrypted/filtering path: S1;
- known repairable supported failure: S3;
- unsupported device/network: S4;
- unresolved VPN/Private Relay/browser/app/network conflict: S5;
- profile/provider removal/reset: S6;
- ordinary DNS working after removal is recovery evidence, not UseSafeWeb protection evidence.

### Services — one relevant external service

Source contract: TSK-0144.

- zero service is a valid not-applicable outcome;
- relevant supported service not configured: S3;
- parent-confirmed approved safeguard: S2;
- no current supported relevant service / age-policy inapplicable / stale unsupported instruction: S4;
- ambiguous/stale/conflicting service state: S5;
- safeguard disabled/removed in current journey: S6;
- S1 is unavailable without a separately approved technical verifier.

No service is inserted merely to make the Map appear complete.

## 6. Parent-facing copy requirements

TSK-0320 remains the exact copy-semantic owner. TSK-0313 requires every rendered state to provide:

1. one concise state label preserving the exact TSK-0320 evidence strength;
2. one sentence naming the evidence actor/limitation;
3. one next action when action is possible;
4. one material coverage limitation when necessary to avoid overclaiming.

Mandatory copy behavior:

- S1 identifies UseSafeWeb/system verification, bounded to the verified mechanism;
- S2 identifies the parent as the confirmation actor and states lack of independent verification;
- S3 says what must be done before relying on that layer;
- S4 says UseSafeWeb does not currently cover/apply this branch;
- S5 says the state cannot currently be verified and should not be relied upon as protected;
- S6 says the safeguard/UseSafeWeb DNS is no longer active.

Prohibited across all states:

- `Your child is safe`;
- `Fully protected`;
- an all-green treatment that makes S2 equivalent to S1;
- language implying surveillance/history visibility;
- language strengthening technical language availability into official non-UK market/support readiness;
- claims that wording/UX is parent-validated while RSK-0002 remains open.

## 7. Transition requirements

Implementations must support at least these transitions without optimistic state leakage:

- `not_started` → S3 when an applicable step is displayed;
- S3 → S2 after valid parent-confirmed completion where no system verifier exists;
- S3 → S1 only after approved current system verification;
- S2 → S1 only if a later approved verifier actually succeeds;
- S1/S2/S3 → S5 when evidence becomes conflicting/inconclusive or context changes materially;
- S5 → S1 after current verification resolves the conflict;
- S5 → S2 when the conflict is resolved but only parent evidence remains;
- S1/S2/S3/S5 → S6 after valid removal/disablement;
- S6 → S3 when the parent begins reconfiguration;
- operational states → S4 only when current scope/support rules actually make the branch unsupported/not applicable.

A completed overall journey does not change any layer's state merely to create a positive final screen.

## 8. Unsupported and partial-coverage behavior

The Map must support mixed results, including examples such as:

- Phone S2 / Internet S1 / Services S4;
- Phone S5 / Internet S1 / Services S2;
- Phone S2 / Internet S5 / Services S4;
- Phone S2 / Internet S6 / Services S2 after DNS removal.

Requirements:

1. mixed states are normal and must not be hidden;
2. unsupported is not a user failure;
3. uncertainty is not silently converted to Action needed unless a deterministic repair exists;
4. one verified layer cannot upgrade another layer;
5. an unsupported service/native layer does not invalidate a separately verified DNS layer;
6. a removed DNS layer immediately withdraws the Internet-layer protection claim even if Phone/Services remain configured;
7. the final journey may complete with gaps when that is the truthful supported outcome.

## 9. Persistence scope

Source contract: TSK-0229.

The Protection Map is **current journey state**, not a persistent child/device safety profile.

### J0 default

- preferred accountless browser/session state;
- can hold/derive the current layer states during the active journey;
- disappears with session destruction/reset;
- cannot be cited later as durable evidence that a device remains protected.

### Optional J1

Only if later architecture proves transient server state technically necessary:

- may store the controlled native/DNS/service/Protection Map states already allowed by TSK-0229;
- fixed hard expiry ≤24 hours from creation, non-sliding;
- prompt deletion on completion/reset/exit, synchronously where possible or within the approved ≤15-minute bound;
- no browsing/DNS/domain history, persistent parent/child/device identity or cross-session linkage;
- cannot become an account/dashboard/device history by implementation convenience.

The Map itself creates no new data fields beyond the TSK-0229 allowlist without a material data-contract review.

## 10. Device versus journey-state boundary

A Protection Map state is not the same thing as durable device truth.

Requirements:

1. a state displayed in one journey describes evidence available for that current journey/check;
2. a fresh accountless journey must not silently restore S1/S2 from an old browser/server record after its authorized lifetime;
3. current platform/configuration must be re-evaluated where the owning contract requires it;
4. absence of persistent history is a product/privacy property, not an error;
5. no stable device/customer identifier is required to render the current Map;
6. no Map history/dashboard is introduced under the active baseline;
7. if a future EXC-0001 account/persistence model is activated, it requires a new ownership/persistence decision rather than reusing J1 history as a customer record.

## 11. Testable examples

### Example A — fully evidenced current DNS path, native confirmed, no service

- Parent confirms current approved native safeguard → Phone S2.
- Supported UseSafeWeb DNS verifier succeeds → Internet S1.
- No relevant supported service → Services S4/not applicable.
- Final Map may show all three simultaneously; it must not convert S2/S4 into S1.

### Example B — VPN conflict

- Native safeguard parent-confirmed → Phone S2.
- UseSafeWeb profile/provider present, but current VPN makes effective DNS path unproven → Internet S5.
- Supported relevant service parent-confirmed → Services S2.
- Journey can finish with explicit Internet uncertainty; no “protected” aggregate badge.

### Example C — repairable DNS failure

- Supported device/route selected.
- Current DNS verification deterministically fails with known repair → Internet S3.
- After repair and successful current verifier → Internet S1.

### Example D — unsupported device/network

- Current authoritative matrix excludes the DNS combination → Internet S4.
- Product must not show setup steps for a fabricated fallback and must not obtain “confirmation” to turn it green.

### Example E — removal

- Internet was S1 during the current journey.
- Parent removes UseSafeWeb DNS and normal DNS recovery succeeds → Internet S6.
- Phone/service states remain whatever their own evidence supports.
- Reinstall begins Internet S3 and requires new verification before returning to S1.

### Example F — stale native/service guidance

- Parent sees a platform/service path that no longer matches current source/applicability and state cannot safely be determined → S5 or S4 according to current owning contract.
- Historical parent confirmation cannot preserve S2 against current contradictory evidence.

## 12. Accessibility and visual evidence-strength requirement

Future visual design must preserve the semantic distinction even without color.

- S1 and S2 must not differ only by hue.
- S3/S4/S5/S6 must have text/icon/structure sufficient to distinguish them without color alone.
- status label, evidence sentence and next action must remain understandable with screen-reader/keyboard/text-resize requirements when those design tasks are active.
- animation or celebratory completion treatment must not override mixed/uncertain/unsupported truth.

This task does not freeze final icons/colors/components; it freezes the evidence-strength requirement those designs must satisfy.

## 13. No account-ownership assumption

The active Map must work without:

- login;
- parent/customer account;
- child profile;
- persistent device registry;
- account-to-device ownership mapping;
- per-device AdGuard client identity;
- browsing/query history.

A parent can complete the immediate accountless journey and see the current Map using only the minimum transient state allowed by TSK-0229.

## 14. Testable acceptance assertions

A later implementation/QA suite must prove:

1. every Phone/Internet/Services layer resolves to S1–S6 or internal not-started→S3 semantics;
2. parent confirmation never yields S1;
3. profile/provider presence never yields S1;
4. current verified DNS can yield S1 only on exact supported tuples;
5. VPN/Private Relay/browser/app conflict produces S5 when unresolved;
6. repairable supported failure uses S3, not S4;
7. unsupported scope uses S4, not a fake setup flow;
8. removal yields S6 and withdraws the active claim;
9. one layer cannot upgrade another layer's evidence strength;
10. mixed state combinations render without an overall “safe” score;
11. journey completion does not force positive states;
12. parent-facing copy names the correct evidence actor/limitation;
13. S1 and S2 are visually/semantically distinct without relying only on color;
14. fresh accountless journeys do not restore expired historical Map state as current truth;
15. J1 state, if used, stays inside the TSK-0229 schema/TTL/deletion/no-linkage contract;
16. no account/device ownership model is required;
17. no browsing/DNS history is needed to render/verify the Map;
18. stale/contradictory evidence demotes optimistic state;
19. translations preserve evidence strength and do not imply official non-UK market activation;
20. no complete-safety or surveillance claim appears in any state.

## 15. ACC-0313 result

ACC-0313 requires every Protection Map state to have entry/evidence rules, parent-facing copy, transition rules, unsupported behavior, persistence scope, device/journey-state boundary and testable examples; parent-confirmed and system-verified states must never be conflated; no account ownership model may be assumed.

This contract directly defines each required dimension while keeping TSK-0320 as the exact state/copy semantic owner and TSK-0229 as the data/persistence owner. It adds no competing state vocabulary or persistent profile model.

**TSK-0313 result: PASS candidate subject to independent verification and runtime read-back.**
