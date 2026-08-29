# TSK-0325 — End-to-End Parent Journey and Service Blueprint

**Version:** 1.0.0  
**Status:** internal L4 implementation/QA contract  
**Owner:** UX/UI  
**Action authority:** A3 / AUTO_ALLOWED  
**Sequencing:** DEC-0052 / CR-0005  
**Human-validation claim:** none; real-user validation remains deferred to L8 after LG-09 PASS.  
**Publication/release authority:** none.

## 1. Purpose and authority

This blueprint converts the frozen TSK-0309 implementation-ready experience baseline and the current TSK-0323 instruction catalogue into one end-to-end parent journey that engineering and QA can implement and test without inventing states, setup steps, persistence, account requirements, recovery behavior, support behavior, or protection claims.

Normative hierarchy for this artifact:

1. Current owner-frozen planning authority and DEC-0052 / CR-0005.
2. `prototype/TSK-0309/BASELINE.md` v1.0.0 — frozen journey/state/product boundary.
3. `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` and `CATALOGUE.json` v1.0.0 — current technical instruction authority.
4. TSK-0320 state semantics and TSK-0322 claims/terminology rules cited by those sources.
5. This blueprint for cross-touchpoint orchestration only.

This blueprint does not copy or replace device procedures. Where a technical action is required, implementation must consume the cited TSK-0323 instruction ID/version.

## 2. Binding product and interaction rules

- Accountless-first: no mandatory SafeWeb account, login, persistent parent identity, child account, customer-facing AdGuard administration, payment step, or browsing-history surface.
- Every interaction must be necessary under `REQ-0028`. No field, choice, confirmation, or account step may be added without an explicit need and current authority.
- Platform setup must use current reliable supported methods or explicit supported fallbacks under `REQ-0029`; unsupported paths stop rather than improvise.
- Parent confirmation never becomes system verification. `Verified` requires current qualifying technical evidence.
- Only the frozen states are permitted: `Verified`, `You confirmed this is set up`, `Action needed`, `Status uncertain`, `Not covered`, `Removed`.
- English, Turkish, and Arabic/RTL are first-release language capabilities under `CON-0017`; language availability must not be presented as non-UK market/legal/support activation.
- `SafeWeb` remains invariant Latin/LTR. Technical endpoints remain exact and untranslated.
- Global Help and Limitations are reachable from every critical path without mutating protection state.
- No routine human-support dependency is introduced. Ordinary support is self-service; exceptional human escalation belongs to later operational authority.
- Retry verification only after a changed condition. Repeating the same failed check without a changed condition is not a valid recovery step.
- No complete-safety, certification, surveillance, safety-score, or equivalent claim is permitted.

## 3. Service lanes

The implementation must preserve these lane responsibilities:

| Lane | Responsibility |
| --- | --- |
| Parent | Chooses platform, performs OS-owned actions, confirms only facts they can observe, decides whether a supported external service is relevant, can remove/reset. |
| SafeWeb UI | Routes, presents current instruction IDs, records ephemeral journey state, runs approved verification, renders truthful Protection Map, troubleshooting, help, limitations, removal/recovery. |
| OS / external platform | Owns Private DNS, profile installation/removal, native parental-control/account/security authorization. SafeWeb must not silently perform or bypass these actions. |
| SafeWeb DNS / verifier | Supplies qualifying technical evidence for DNS state only; it does not verify native safeguards or unsupported external-service states unless a separately approved verifier exists. |
| Content/instruction authority | TSK-0323 owns technical procedures, applicability, expected result, fallback and unsupported state. |
| QA | Tests each path, state transition, negative branch, recovery, accessibility/localization behavior and requirement trace below. |

## 4. Touchpoint catalogue and necessity trace

Every implementation touchpoint must correspond to one of these IDs. Adding another touchpoint requires a current necessity justification under REQ-0028.

| ID | Touchpoint | Necessary purpose | Instruction binding | Required trace |
| --- | --- | --- | --- | --- |
| `TP-01` | Discovery | Explain bounded proposition/limits and let parent intentionally start. | none | REQ-0028; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-02` | Platform router | Select Android, iPhone, or unsupported/other so only tested setup is shown. | `DEV-COMMON-NOT-COVERED` for unsupported | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-03` | Native safeguard status | Avoid duplicate work; distinguish already configured, needs action, uncertain/not covered. | `DEV-AND-NATIVE` or `DEV-IOS-NATIVE` | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-04` | DNS setup | Present exact supported encrypted-DNS procedure only. | `DEV-AND-DNS-SETUP` or `DEV-IOS-DNS-SETUP` | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-05` | DNS verify | Convert current qualifying technical evidence into truthful DNS state. | `DEV-AND-DNS-VERIFY` or `DEV-IOS-DNS-VERIFY` | REQ-0028; REQ-0029; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-06` | Optional external service | Route zero or one current supported relevant service; zero is valid. | `SVC-ONE-RELEVANT` | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-07` | Protection Map | Explain Phone / Internet / Service using evidence states, never a safety score. | state authority through TSK-0320/0322 | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-08` | Troubleshooting | Diagnose known conflicts and show one safe next action. | `DEV-COMMON-CONFLICT` | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-09` | Removal | Remove exact SafeWeb DNS configuration and withdraw active DNS protection claim. | `DEV-AND-DNS-REMOVE` or `DEV-IOS-DNS-REMOVE` | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-10` | Recovery check | Confirm ordinary connectivity after removal/reset without claiming SafeWeb protection. | `DEV-COMMON-RECOVERY` | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-11` | Reset/reconfigure | Return to a clean discovery state when state is intentionally reset/lost. | none | REQ-0028; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-12` | Global Help | Point-of-need self-service without changing journey/protection state. | current help/content authority only | REQ-0028; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-13` | Limitations | Explain unsupported/unverified scope without inventing workaround or strengthening claims. | `DEV-COMMON-NOT-COVERED` | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 |

## 5. Path A — Normal supported setup

**Entry:** parent starts from discovery on a currently supported Android phone or iPhone.

| Step | Parent | SafeWeb / platform behavior | State/output | Touchpoint |
| --- | --- | --- | --- | --- |
| A1 | Reads proposition/limits; chooses Start setup. | No account/payment/identity collection. | journey begins | TP-01 |
| A2 | Chooses Android or iPhone. | Route only to current supported family. | platform branch | TP-02 |
| A3 | Indicates whether relevant native safeguard is already configured or needs action; completes OS-owned flow if needed. | Consume `DEV-AND-NATIVE` or `DEV-IOS-NATIVE`; SafeWeb never collects OS/provider credentials. | S2 after parent confirmation; S4/S5 if unsupported/uncertain | TP-03 |
| A4 | Performs exact OS-owned DNS configuration. | Consume platform setup instruction; no S1 from configuration presence. | pending verification | TP-04 |
| A5 | Returns and requests verification. | Run approved technical check. | S1 only on qualifying evidence; otherwise branch to failed activation | TP-05 |
| A6 | Selects no service or one supported relevant service if one exists. | Zero services is valid. No named service may be invented. | S2/S4/S5 as evidence permits | TP-06 |
| A7 | Reviews Protection Map. | Render Phone / Internet / Service independently with textual state labels and limitations. | truthful map | TP-07 |

**Normal completion:** Internet may be `Verified`; native/service may be `You confirmed this is set up`, `Not covered`, or `Status uncertain` according to evidence. There is no overall “safe” score.

## 6. Path B — Already configured

**Entry:** parent reports that a native safeguard and/or SafeWeb DNS appears already configured.

1. At TP-03, do not force duplicate native setup. Consume the relevant native instruction and record only S2 when the parent confirms the setting; do not manufacture S1.
2. If SafeWeb DNS appears present, skip duplicate configuration only when the current platform tuple is identifiable enough to run the approved verifier safely.
3. At TP-05, verification determines DNS truth:
   - qualifying current evidence -> S1 `Verified`;
   - known repairable issue -> S3 `Action needed`;
   - inconclusive/conflicting evidence -> S5 `Status uncertain`;
   - unsupported tuple -> S4 `Not covered`.
4. Continue to TP-06/TP-07 without adding an account, identity, browsing history, or persistent device profile.

**QA assertion:** “already configured” is a friction-reduction branch, not a shortcut around verification truth.

## 7. Path C — Unsupported / not covered

**Entry:** unsupported platform/device/version/management/network tuple or missing current accepted instruction.

1. TP-02 or any later applicability check invokes `DEV-COMMON-NOT-COVERED`.
2. Stop the affected setup path; do not invent VPN/client/profile/service workarounds.
3. Show S4 `Not covered` or S5 `Status uncertain` with a concise reason and current limitation.
4. Global Help/Limitations may explain the boundary or link to official platform information for understanding only; such links do not create a SafeWeb support claim.
5. Do not expose Removal if SafeWeb DNS was never configured through the journey.
6. Parent may reset/reconfigure to another genuinely supported device branch.

**QA assertion:** unsupported always fails safely and cannot be converted to `Verified` through confirmation alone.

## 8. Path D — Failed activation / verification failure

**Entry:** setup was attempted but approved verification does not establish the intended SafeWeb encrypted-DNS path, or configuration breaks connectivity.

1. TP-05 renders S3 `Action needed` only when a proven repair exists; otherwise S5/S4.
2. TP-08 consumes `DEV-COMMON-CONFLICT` and identifies a current evidence-backed next action for known VPN, Private Relay, browser/app resolver, network block, captive portal, management or other accepted conflict classes.
3. Do not ask the parent to weaken required employer/school/security controls merely to obtain positive state.
4. A retry is offered only after a changed condition.
5. If SafeWeb configuration materially breaks resolution, route to TP-09/TP-10 using the exact platform removal instruction and `DEV-COMMON-RECOVERY`.
6. After removal, DNS state is S6 `Removed`; ordinary connectivity may be checked, but SafeWeb protection cannot remain asserted.

**QA assertion:** repeated identical failed verification is rejected as a recovery loop; state never silently advances.

## 9. Path E — False positive / legitimate content blocked

**Entry:** the encrypted DNS path may still be technically verified, but the parent reports a legitimate destination/service is blocked.

1. Preserve the distinction between **DNS path verification** and **filtering correctness**. A false positive does not automatically make technical-path evidence false, but it is a material service problem.
2. TP-12 presents current self-service false-positive guidance and current approved exception/report route only if that route is separately implemented and source-current. This blueprint does not invent a user-facing bypass control.
3. Do not recommend disabling required native safeguards or silently switching to an unreviewed resolver.
4. If the only safe immediate recovery is removal of SafeWeb DNS, use TP-09/TP-10 and set S6 `Removed`.
5. If SafeWeb remains configured while the issue is unresolved, the Protection Map must not imply that “Verified” means all legitimate content will work or all harmful content will be blocked.

**QA assertion:** no complete-safety/zero-error claim; false-positive help cannot mutate verified state without actual evidence/state change.

## 10. Path F — Resume after interruption

**Entry:** parent leaves a screen temporarily or navigates to Help/Limitations and returns.

1. Within the same active in-memory journey, preserve the current lawful transient state so Help/Limitations does not corrupt progress.
2. No `localStorage`, `sessionStorage`, cookie, service worker, persistent parent/device profile, or mandatory account is introduced by this blueprint.
3. If the browser/page process loses transient journey state, do **not** pretend persistent resume exists. Route to TP-11 clean reset/reconfigure.
4. On a clean restart, current device/platform facts and verification must be re-established before S1 is shown.
5. Previously remembered parent confirmation outside the active journey cannot become system verification.

**QA assertion:** resume behavior matches the frozen privacy boundary; persistence is not fabricated merely for convenience.

## 11. Path G — Removal and recovery

**Entry:** parent intentionally removes SafeWeb, activation failed materially, or recovery requires rollback.

1. TP-09 uses `DEV-AND-DNS-REMOVE` or `DEV-IOS-DNS-REMOVE` exactly for the active supported family.
2. OS-owned confirmation remains in the OS flow; SafeWeb does not silently alter settings.
3. Once the exact SafeWeb configuration is removed, Internet state becomes S6 `Removed` and active SafeWeb DNS protection wording is withdrawn.
4. TP-10 runs a neutral connectivity check where available.
5. If connectivity remains broken after removal, use ordinary network help/S5; SafeWeb must not falsely claim cause or successful recovery.
6. TP-11 may return to clean discovery for a later intentional reconfiguration.

**QA assertion:** removal is reversible and truthful; it cannot leave stale `Verified` state or a hidden plaintext “protected” fallback.

## 12. Path H — Support / help

**Entry:** Help is opened from any critical screen or a troubleshooting/support need is detected.

1. TP-12 is globally reachable and never changes protection state merely by being opened/closed.
2. Present point-of-need content based on current journey context without collecting browsing history, child identity, provider credentials or persistent diagnostics.
3. Use TSK-0323 current instruction IDs for technical help; never fork/copy technical semantics into help content.
4. Ordinary help is self-service. Do not make routine human support a prerequisite for successful setup/recovery.
5. When a path is unsupported or evidence is insufficient, TP-13 exposes the limitation instead of inventing a fix.
6. Exceptional security/legal/safeguarding/operational escalation remains outside this L4 blueprint and must follow its owning authority.

**QA assertion:** Help is state-neutral, privacy-minimal, source-current and does not become an undocumented support workflow.

## 13. State-transition invariants

Engineering and QA must enforce all of the following:

- configuration presence -> never directly S1;
- parent confirmation -> S2 at most, never S1;
- qualifying technical verifier success -> may establish S1 for the supported DNS layer only;
- failed known repair -> S3;
- unsupported scope -> S4;
- insufficient/conflicting evidence -> S5;
- exact SafeWeb DNS removal -> S6;
- S6 cannot become S1 without a new supported setup plus current qualifying verification;
- Help/Limitations navigation is state-neutral;
- reset clears transient journey state and returns to discovery;
- external-service completion is S2 unless a separately approved future verifier explicitly changes that contract;
- native-safeguard completion remains parent-confirmed unless separately approved technical evidence exists;
- no state transition is justified solely by color, copy optimism, elapsed time, or repeated unchanged retry.

## 14. Accessibility, responsive and localization acceptance

Every path must remain testable under the frozen TSK-0309 accessibility/responsive contract:

- mobile-first, including representative 320 px viewport without horizontal overflow;
- focus moves to current screen heading on screen transitions;
- explicit busy state settles correctly;
- buttons have explicit semantics;
- state meaning is textual, not color-only;
- English, Turkish and Arabic/RTL variants preserve the same path/state semantics;
- `SafeWeb` and technical endpoints remain LTR/untranslated inside RTL UI;
- localization may not strengthen a claim or imply market/legal/support activation.

## 15. QA acceptance matrix

TSK-0325 cannot PASS unless QA can deterministically assert all eight required paths:

| Path | Required terminal/asserted outcome |
| --- | --- |
| Normal | Supported branch reaches truthful Protection Map; S1 only from current technical evidence. |
| Already configured | Duplicate work skipped without bypassing DNS verification or upgrading parent confirmation to S1. |
| Unsupported | S4/S5 with explicit limitation; no speculative setup/removal. |
| Failed activation | S3/S5/S4 as evidence dictates; bounded corrective action; removal/recovery available when needed. |
| False positive | Filtering problem is represented without complete-safety claim or invented bypass; recovery remains truthful. |
| Resume | Same active in-memory state can resume; lost state cleanly restarts; no hidden persistence/account. |
| Removal | Exact SafeWeb DNS removed, S6 shown, active protection claim withdrawn, neutral connectivity checked. |
| Support | Help is state-neutral, source-current, self-service and privacy-minimal. |

Cross-cutting QA must additionally prove:

- every implementation touchpoint maps to the trace in section 4;
- no unlisted mandatory field/account step exists;
- all device/service technical actions resolve to current TSK-0323 IDs;
- no named external service is invented;
- all frozen state semantics remain exact;
- unsupported/uncertain cases fail safely;
- no human/user validation claim is made pre-L8;
- no release/publication/production/payment/market/launch authority is inferred.

## 16. Accepted source/version set

- `prototype/TSK-0309/BASELINE.md` v1.0.0 — blob `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`.
- `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` v1.0.0 — blob `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`.
- `content/TSK-0323/CATALOGUE.json` v1.0.0 — blob `842e18c5666a82d53e2d348715dd6b9198daa44c`.
- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` — blob `1146f7622f434590dde1253d11f14fb6a87e19de`.
- `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md` — blob `02b34756862a62091908e60d32b490059a84a67c`.
- Current WBS at CR-0005 — blob `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.
- Current risk `RSK-0002` remains open/non-blocking under DEC-0052/CR-0005; no behavioral evidence is claimed by this artifact.

## 17. Change control

This blueprint is the TSK-0325 L4 cross-touchpoint orchestration contract. A material change to journey order, state truth, technical setup mechanism, supported platform scope, persistence/account behavior, external-service scope, removal/recovery behavior, help/support dependency, claims, accessibility, or localization behavior requires impact review against the owning authority before reuse.

Contradictory current source/device/browser/security/privacy evidence reopens the affected path. This artifact cannot authorize production implementation, public release, participant processing, payment, market activation or launch by itself.
