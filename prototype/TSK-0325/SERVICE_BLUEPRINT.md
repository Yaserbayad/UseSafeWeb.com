# TSK-0325 — End-to-End Parent Journey and Service Blueprint

**Version:** 2.0.0-post-cr0007  
**Status:** current L4 candidate; implementation/QA contract input only  
**Owner:** UX/UI  
**Action authority:** A3 / AUTO_ALLOWED  
**Sequencing:** DEC-0052/CR-0005 + DEC-0053/CR-0006 + DEC-0054/CR-0007  
**Human-validation claim:** none; real-user validation remains deferred to L8 after LG-09 PASS.  
**Publication/release authority:** none.

## 1. Purpose and authority

This artifact is the current **parent-journey view** of the accepted post-CR-0007 TSK-0315 dual-mode service blueprint. It owns the ACC-0325 path taxonomy and touchpoint-to-requirement trace; it does not duplicate the full service-lane/data/owner/failure matrix already owned by TSK-0315.

It supersedes v1.0.0 where that version treated persistent parent/device continuity as absent. Current Version 1 remains accountless-first **and** includes an optional parent account/session/lightweight dashboard. Login is never required for core safety value.

Normative hierarchy for this artifact:

1. current WBS/decisions/constraints and runtime authority;
2. current TSK-0315 dual-mode service blueprint;
3. TSK-0312 account/session/minimal-intake requirements and TSK-0142 dashboard/device-management requirements;
4. TSK-0229 accountless/persistent-domain separation;
5. current technical instruction/state contracts including TSK-0320 and source-backed platform/DNS instructions;
6. this artifact for parent path/touchpoint orchestration.

## 2. Binding journey rules

- The full core path remains usable without login, parent identity, child identity or payment.
- Optional account entry is continuity/management only; cancel/error/provider outage returns safely to accountless operation.
- No automatic J0/J1-to-account/device join, promotion or expiry extension is authorized.
- Every field, choice, confirmation and account step needs an explicit necessity under REQ-0028.
- Supported platform setup uses current reliable source-backed methods/fallbacks under REQ-0029; unsupported paths stop rather than improvise.
- Parent confirmation never becomes system verification; stored account/device ownership never becomes system verification.
- Current evidence states remain: `Verified`, `You confirmed this is set up`, `Action needed`, `Status uncertain`, `Not covered`, `Removed`.
- Browsing/query/activity history, child accounts/profiles and raw/unrestricted AdGuard administration remain excluded.
- English/Turkish/Arabic+RTL technical capability does not imply non-UK market activation.
- Global Help/Limitations remain state-neutral; ordinary support is self-service.
- Retry requires a changed condition/new evidence or an independently safe idempotent operation.
- No complete-safety, certification, surveillance or aggregate safety-score claim is permitted.

## 3. Current touchpoint catalogue and necessity trace

Every implemented journey touchpoint must correspond to one of these IDs or receive a new documented necessity review. TSK-0315 owns the full service-stage mapping; this table owns the parent-facing journey trace.

| ID | Touchpoint | Necessary purpose | Required trace |
| --- | --- | --- | --- |
| `TP-01` | Discovery / Start | Explain bounded proposition/limits and intentionally enter setup. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-02` | Platform router | Select a supported platform/path or stop truthfully. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-03` | Native safeguard status | Avoid duplicate work and preserve parent-confirmed vs verified truth. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-04` | DNS setup | Present the exact supported encrypted-DNS procedure. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-05` | DNS verify | Establish current qualifying technical DNS/filtering evidence. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-06` | Relevant service | Route zero or one supported relevant service; zero is valid. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-07` | Protection Map | Explain Phone/Internet/Services using truthful evidence strength. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-08` | Optional account entry | Offer bounded continuity without gating core value. | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `TP-09` | Sign-in / session | Establish or restore an authorized account session; handle cancel/error/expiry. | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `TP-10` | Dashboard / device list | Show only explicitly managed device records and truthful evidence/currentness. | REQ-0028; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 |
| `TP-11` | Device management | Add/rename/continue/verify/reinstall/replace/revoke/remove within approved scope. | REQ-0028; REQ-0029; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 |
| `TP-12` | Troubleshooting / false positive | Diagnose known issues and show one safe evidence-backed next action. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-13` | Physical DNS removal | Remove exact UseSafeWeb DNS configuration and withdraw active claim. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-14` | Recovery check | Confirm ordinary connectivity/recovery without claiming UseSafeWeb protection. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-15` | Reset / reconfigure | Restart accountless journey or current device setup without conflating web reset with DNS removal. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-16` | Global Help / Limitations | Provide source-current, privacy-minimal help without mutating protection state. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `TP-17` | Account/device lifecycle | Logout, revoke/unlink, delete device record, delete account; keep each distinct from physical DNS removal. | REQ-0028; CON-0010; CON-0017; TSK-0312; TSK-0142; INT-0009; INT-0010 |

## 4. Path A — Normal supported accountless setup

`TP-01 → TP-02 → TP-03 → TP-04 → TP-05 → TP-06 → TP-07`

1. Parent starts without login/payment/identity collection.
2. Platform route selects only current supported instructions.
3. Native safeguard is parent-confirmed unless an approved verifier exists.
4. DNS configuration presence alone never yields `Verified`.
5. Current qualifying DNS verification can establish `Verified` only for its supported mechanism/context.
6. Zero or one relevant external service is valid.
7. Protection Map renders each layer independently; no overall safe score.
8. Parent may finish/exit here with no account.
9. Optional continuity may be offered only after/alongside the core without making it a gate.

**Terminal:** truthful Protection Map and completed core journey; optional account remains optional.

## 5. Path B — Already configured

1. At TP-03, skip duplicate native setup where the parent can truthfully confirm an existing setting; strongest default is parent-confirmed, not system-verified.
2. If UseSafeWeb DNS appears configured, skip duplicate configuration only when current platform/context can safely proceed to verification.
3. TP-05 determines DNS truth: qualifying evidence → `Verified`; known repair → `Action needed`; conflict/inconclusive → `Status uncertain`; unsupported → `Not covered`.
4. Existing account/dashboard records do not bypass current verification or upgrade evidence.
5. Continue to TP-06/TP-07 and optionally TP-08–TP-11 without automatic J0/J1 migration.

**Terminal:** duplicate work avoided without weakening verification or privacy rules.

## 6. Path C — Unsupported / not covered

1. Any current applicability check can stop an unsupported platform/device/network/service branch.
2. Render `Not covered` or `Status uncertain` with the current reason; do not invent VPN/client/profile/service fallbacks.
3. Help/Limitations may explain the boundary without creating a support claim or changing state.
4. Parent may reset to another genuinely supported branch.
5. If the parent is signed in, dashboard presence still cannot convert unsupported scope to supported/verified.

**Terminal:** truthful unsupported/uncertain outcome and safe exit/re-route.

## 7. Path D — Failed activation / verification failure

1. TP-05 uses `Action needed` only for a known repair; otherwise `Status uncertain`/`Not covered` as evidence dictates.
2. TP-12 provides an evidence-backed correction; repeated unchanged retry is not a recovery plan.
3. Do not ask the parent to weaken required school/employer/security/privacy controls merely to obtain a positive state.
4. If configuration materially breaks resolution or safe recovery requires rollback, route TP-13 → TP-14.
5. Signed-in users receive the same technical truth; account ownership cannot preserve stale `Verified`.

**Terminal:** corrected and reverified, or truthful unresolved state, or removed/recovered.

## 8. Path E — False positive / legitimate content blocked

1. Keep DNS-path verification distinct from filtering correctness.
2. TP-12 uses the current narrow reproducible exception/report process where separately implemented; do not invent a broad per-domain dashboard control.
3. Do not recommend disabling unrelated required safeguards or silently changing to an unreviewed resolver.
4. After a justified narrow correction, re-test the legitimate path and relevant blocked regression under the owning technical process.
5. If the safe immediate recovery is removal, use TP-13/TP-14 and withdraw the active UseSafeWeb claim.
6. No browsing/query history is collected as a convenience for this path.

**Terminal:** narrow correction + truthful recheck, unresolved help state, or removal/recovery.

## 9. Path F — Resume after interruption

### Accountless core
- Same-active-session context may resume from authorized transient J0/J1 state.
- Lost/expired accountless state must not be fabricated as durable history; route to TP-15 and re-establish current evidence.
- Account sign-in/activity cannot extend J1 expiry.

### Optional account continuity
- A valid authenticated account may resume only the minimum account/device lifecycle state authorized by downstream architecture.
- Account/device records may route the parent to a device/setup step, but historical status is not automatically current verification.
- No automatic J0/J1-to-account/device import is authorized; any future explicit transfer requires the approved downstream field-level data-flow contract.

**Terminal:** resume from legitimate current state, or clean restart/reverification when currentness is unavailable.

## 10. Path G — Removal and recovery

1. TP-13 uses exact current platform-specific removal for the configured UseSafeWeb mechanism.
2. Once supporting evidence/confirmation establishes removal, Internet state becomes `Removed`; active UseSafeWeb DNS wording is withdrawn.
3. TP-14 checks neutral ordinary connectivity/recovery where available.
4. If connectivity still fails, show an evidence-bounded recovery state; do not fabricate root cause.
5. Dashboard record deletion/revoke/account deletion are separate operations and must not claim physical DNS removal.
6. Reinstall begins from `Action needed`/setup and requires new qualifying evidence before returning to `Verified`.

**Terminal:** truthful `Removed` plus recovery result, or explicit unresolved recovery state.

## 11. Path H — Support / help

1. TP-16 is reachable from critical accountless and account/device paths and is state-neutral when opened/closed.
2. Use current source-backed instructions and issue-specific decision trees first.
3. Do not collect browsing history, child identity, provider credentials or unrestricted diagnostics as ordinary help input.
4. Account/session problems use TSK-0312 recovery; device-management problems use TSK-0142 lifecycle requirements; technical DNS failures use owning technical rules.
5. Provider outage blocks account-only functions but leaves accountless setup/verification/help/removal available.
6. Exceptional security/privacy/legal/safeguarding incidents remain outside routine L4 self-service and follow their owning authority.

**Terminal:** self-service resolution, truthful unsupported/uncertain state, or separately governed exceptional escalation.

## 12. Optional account/device continuity overlay

This overlay is not a ninth mandatory core path; it is an optional branch available from an appropriate downstream-designed entry point.

`TP-08 → TP-09 → TP-10 → TP-11 / TP-17`

Required behavior:

- Google social sign-in is the planned current route; no local password/SMS flow is introduced.
- cancel/error/provider outage returns safely to the accountless experience.
- dashboard list/empty states expose only authorized parent-owned device records.
- add/manage/reverify/reinstall/replace/revoke/remove actions preserve TSK-0142 truth semantics.
- logout/session expiry only affects account access, not configured DNS.
- device-record deletion/account deletion/J0-J1 deletion/physical DNS removal remain separate.
- stored ownership/history never yields technical `Verified`.

## 13. State-transition invariants

- configuration presence → never directly `Verified`;
- parent confirmation → parent-confirmed at most;
- qualifying current verifier success → may establish `Verified` for the exact supported mechanism;
- known repairable failure → `Action needed`;
- unsupported → `Not covered`;
- inconclusive/conflicting/stale → `Status uncertain`;
- removal → `Removed` and active claim withdrawn;
- Help/Limitations navigation is state-neutral;
- reset/reconfigure does not itself remove physical DNS;
- account/session/dashboard presence cannot strengthen evidence;
- current contradictory evidence overrides historical optimistic state.

## 14. Accessibility/localization/claims inheritance

All touchpoints inherit the project WCAG 2.2 AA target, mobile-first responsive behavior and English/Turkish/Arabic+RTL technical capability. State meaning must not depend on color alone. Translation must preserve evidence strength. Language availability does not imply named-market readiness. No user-tested/comprehension claim is made before L8.

## 15. ACC-0325 current disposition

ACC-0325 requires the map to cover normal, already-configured, unsupported, failed-activation, false-positive, resume, removal and support paths, with every touchpoint mapped to requirements.

This v2 artifact retains all eight required path classes and expands the touchpoint trace from 13 to 17 to reconcile current optional-account/session/dashboard/device-lifecycle scope. It consumes rather than duplicates the full accepted TSK-0315 service blueprint and preserves the login-free core, no-linkage, no-history and truthful-evidence boundaries.

**Candidate disposition:** ACC-0325 is ready for independent post-publication verification. TSK-0325 remains non-PASS under current CR-0006/0007 semantics until that verification and durable runtime reconciliation succeed.
