# TSK-0334 — Support, False-Positive, Removal and Reconfiguration Flows — Candidate

**Version:** 1.0.0  
**Status:** HUMAN_ONLY decision candidate; not accepted / not PASS  
**Task:** `TSK-0334 — Design support, false-positive, removal, and reconfiguration flows`  
**Current sequencing:** `DEC-0052 / CR-0005`  
**Product boundary:** accountless-first; self-service ordinary path; exceptional escalation only  
**Visible product identity:** `SafeWeb`

## 1. Purpose and authority

This candidate formalizes the support/recovery interactions required downstream of the accepted TSK-0330 Phone → Internet → Services flow. It does not create a help-desk product, account system, browsing-history surface, user-facing DNS administration console, or unrestricted exception/bypass mechanism.

Pinned current sources:

- accepted TSK-0330 candidate `design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md`, blob `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7`;
- TSK-0325 service blueprint `prototype/TSK-0325/SERVICE_BLUEPRINT.md`, blob `1701f5f7b13ac8f7fa3092e39005b3da7627c89f`;
- TSK-0323 instruction catalogue `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md`, blob `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`;
- TSK-0324 UI/accessibility contract `prototype/TSK-0324/UI_COMPONENT_RULES.md`, blob `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`;
- TSK-0320 protection-state semantics as consumed by those contracts;
- owner-frozen `DEC-0052 / CR-0005`: no pre-product parent/user testing; first real-user validation remains L8 after LG-09.

## 2. Acceptance contract

TSK-0334 requires **each major support category** to provide:

1. an accessible path;
2. a minimal diagnostic request;
3. a clear protection consequence;
4. an escalation option;
5. a success state.

This candidate treats the major categories as:

- `SUP-01` verification/setup troubleshooting;
- `SUP-02` false positive / legitimate destination blocked;
- `SUP-03` SafeWeb DNS removal and connectivity recovery;
- `SUP-04` SafeWeb reconfiguration after removal/reset/change;
- `SUP-05` unsupported/uncertain state and limitations.

Global Help remains reachable from every critical screen and is state-neutral.

## 3. Global invariants

All support flows obey these rules:

- parent confirmation never becomes system verification;
- `Verified` requires current qualifying technical evidence;
- technical configuration presence alone is never `Verified`;
- unsupported or insufficient evidence becomes `Not covered` or `Status uncertain`, not a guessed workaround;
- retry only after a changed condition;
- Help/Limitations navigation never changes protection state by itself;
- no request for browsing history, raw DNS queries, child identity, provider password, SafeWeb account, persistent device identity, or unrestricted diagnostics;
- ordinary support is self-service; human escalation is exceptional and bounded;
- no support flow may recommend weakening employer/school/security controls merely to obtain a positive state;
- no user-facing arbitrary allowlist/bypass/DNS-admin capability is invented;
- removal withdraws the active SafeWeb DNS protection claim;
- reconfiguration cannot restore `Verified` without a new qualifying technical check;
- no overall safety score, `100% safe`, `fully protected`, certification, or equivalent complete-safety statement.

Authorized states remain exactly:

- `Verified`
- `You confirmed this is set up`
- `Action needed`
- `Not covered`
- `Status uncertain`
- `Removed`

## 4. Shared accessible support shell

Every support surface uses the accepted TSK-0324 component contract:

- semantic page/screen heading order with one `h1`;
- programmatic screen changes move focus to the current `h1`;
- keyboard-operable semantic controls with visible focus;
- explicit text state labels; color never carries meaning alone;
- primary action names the actual action (`Check again`, `Remove SafeWeb DNS`, `Start setup again`) rather than generic `Continue` when a specific label is available;
- required recovery/limitations actions are not hidden behind low-contrast or disabled dead ends;
- 320 px critical flow remains single-column without page-level horizontal overflow;
- target size and text-resize behavior remain within the accepted accessibility contract;
- English/Turkish/Arabic/RTL use the same semantic flow; `SafeWeb` and technical endpoints remain LTR/untranslated.

Global entry points:

- **Help** from every critical setup/map/support screen;
- contextual **Troubleshoot** from `Action needed` / applicable `Status uncertain` Internet states;
- **Remove SafeWeb DNS** when SafeWeb DNS is actually configured or partially configured;
- **Start setup again / Reconfigure** after removal/reset or when a changed condition makes another supported attempt appropriate;
- **Limitations** from unsupported/uncertain routes.

## 5. Minimal diagnostic envelope

The ordinary self-service flow should infer context from the current in-memory journey whenever possible rather than asking the parent to type it again.

When an explicit diagnostic request is necessary, request only the minimum fields from this allowlist:

- platform family: Android or iPhone;
- current instruction/test ID or support category;
- current visible protection state;
- coarse issue class selected by the parent (`verification failed`, `site/service blocked`, `internet broken after setup`, `want to remove`, `want to set up again`, `unsupported/other`);
- optional OS major version only when needed to choose current platform guidance;
- generated non-identifying error/reference code if an implementation already has one under approved telemetry/data authority.

Do **not** request by default:

- child/parent name or email;
- account credentials;
- browsing history or visited destinations beyond the single destination the parent voluntarily identifies for a false-positive report;
- raw DNS query logs;
- persistent device/customer identifier;
- screenshots containing unrelated personal data;
- full network configuration dumps.

Any future diagnostic persistence, telemetry or external ticketing requires its own current privacy/security/data authority and cannot inherit approval from TSK-0334.

## 6. SUP-01 — Verification/setup troubleshooting

**Entry:** DNS setup was attempted but the approved verifier returns `Action needed`, `Status uncertain`, or `Not covered`, or connectivity materially fails after setup.

### Accessible path

Protection Map / Verify → `Troubleshoot` → issue-specific support screen. Help remains available throughout.

### Minimal diagnostics

Use current in-memory platform, instruction ID and verifier result. Ask at most one coarse clarifier when needed to distinguish known classes such as VPN, Private Relay, browser/app resolver, captive portal, managed policy, blocked encrypted DNS, or ordinary connectivity failure.

### Flow

1. Preserve the current truthful state.
2. Consume `DEV-COMMON-CONFLICT` and the current platform instruction record; do not fork technical steps locally.
3. Explain the known conflict/uncertainty in plain language.
4. Present **one** current evidence-backed next action.
5. Offer `Check again` only after the relevant condition changed.
6. If configuration materially breaks resolution, offer `Remove SafeWeb DNS` and follow SUP-03.
7. If the tuple is unsupported or still unprovable, route to SUP-05 rather than looping.

### Protection consequence

- successful qualifying recheck → Internet may become `Verified`;
- known repair still incomplete → `Action needed`;
- evidence remains inconclusive → `Status uncertain`;
- unsupported tuple → `Not covered`;
- removal → `Removed`.

### Escalation option

Exceptional escalation is allowed only when a current approved self-service path cannot safely resolve a material product/operational issue. The escalation handoff contains only the minimal diagnostic envelope above plus the current instruction/test ID. It must not become a routine prerequisite for setup success.

### Success state

One of:

- qualifying re-verification produces the truthful current state;
- safe removal/recovery completes with `Removed` and ordinary connectivity checked;
- unsupported/uncertain disposition is clearly established with no misleading positive state.

## 7. SUP-02 — False positive / legitimate destination blocked

**Entry:** the parent reports that a legitimate destination/service appears blocked while SafeWeb DNS is configured.

### Accessible path

Protection Map / Help → `A site or service seems blocked` → false-positive support screen.

### Minimal diagnostics

Ask only for:

- the single destination/service the parent says is affected, when needed to investigate the report;
- current platform family if not already known in the active journey;
- current Internet state and relevant reference/instruction ID from the active journey.

Do not ask for browsing history, a list of visited domains, child identity, DNS logs, credentials, or a persistent account.

### Flow

1. Explain that DNS-path `Verified` means only that qualifying current evidence confirms the intended SafeWeb DNS path; it does not guarantee zero false positives or that all legitimate content works.
2. Keep the current Internet evidence state unchanged unless actual technical evidence changes.
3. Offer the current approved false-positive/report/exception route **only if separately implemented and current**; TSK-0334 does not create an arbitrary allowlist or bypass control.
4. If no current safe exception/report route exists, allow the parent to keep SafeWeb configured while the issue remains open, or intentionally remove SafeWeb DNS through SUP-03 when immediate access is more important.
5. Never recommend disabling unrelated native safeguards or switching silently to an unreviewed resolver.

### Protection consequence

- reporting a false positive alone does not change `Verified`/other evidence state;
- applying a separately approved exception may require the owning filter/config verification before any related status statement changes;
- removing SafeWeb DNS changes Internet state to `Removed`.

### Escalation option

A bounded false-positive report may be escalated to the owning filter/content/operations process when a current route exists. The report contains only the single volunteered destination/service plus the minimal diagnostic envelope; no history or child profile is attached.

### Success state

One of:

- separately approved exception/correction is applied and the relevant behavior is rechecked without weakening truth-state semantics;
- issue is acknowledged/reported while the current protection state remains truthful;
- parent chooses removal and SUP-03 completes with `Removed` plus neutral connectivity recovery.

No “problem reported” acknowledgement is treated as a protection-state upgrade.

## 8. SUP-03 — Removal and connectivity recovery

**Entry:** parent intentionally wants SafeWeb removed, setup materially breaks connectivity, or troubleshooting selects rollback.

### Accessible path

Protection Map / Help / Troubleshoot → `Remove SafeWeb DNS`.

### Minimal diagnostics

No typed diagnostics are normally required. Use the current platform family and active setup instruction from the in-memory journey.

### Flow — Android

1. Consume `DEV-AND-DNS-REMOVE`.
2. Open Android Private DNS.
3. Leave custom SafeWeb provider-hostname mode.
4. Restore normal platform policy, normally `Automatic`, unless the parent independently chooses another non-SafeWeb policy.
5. Run the neutral connectivity check where available.
6. Set Internet state to `Removed` and withdraw active SafeWeb DNS protection wording.

### Flow — iPhone

1. Consume `DEV-IOS-DNS-REMOVE`.
2. Open current profile-management path and identify the exact SafeWeb profile.
3. Remove that profile using iOS-owned confirmation.
4. If the device/profile is managed by another authority, stop rather than bypassing that management.
5. Run the neutral connectivity check where available.
6. Set Internet state to `Removed` and withdraw active SafeWeb DNS protection wording.

### Protection consequence

`Removed` is mandatory after exact SafeWeb DNS removal. Neutral connectivity success does not imply SafeWeb protection.

### Escalation option

If ordinary connectivity remains broken after exact SafeWeb removal, escalate only as a general network/operational issue with the minimum platform + removal-result context. SafeWeb must not claim it caused or fixed the remaining problem without evidence.

### Success state

- exact SafeWeb configuration/profile removed;
- Internet state `Removed`;
- neutral connectivity check completed where available;
- no stale `Verified` or hidden plaintext “protected” fallback remains.

## 9. SUP-04 — Reconfiguration / start setup again

**Entry:** SafeWeb was removed/reset; platform/network conditions changed; parent intentionally wants another supported attempt; or a previous unsupported/uncertain condition has materially changed.

### Accessible path

Protection Map (`Removed`) / Help / clean reset → `Start setup again`.

### Minimal diagnostics

Use only current platform choice and current support/applicability checks. Do not restore stale prior verification or confirmation from a previous journey as proof.

### Flow

1. Clear the in-memory journey state through the accepted reset behavior; do not silently alter OS settings merely by resetting the web flow.
2. Re-run platform/applicability routing.
3. Reuse TSK-0330 Phone → Internet → Services sequence and current TSK-0323 instruction IDs.
4. If native safeguard is still present, parent may reconfirm it; this remains `You confirmed this is set up`, not `Verified`.
5. Configure SafeWeb DNS only through the current supported platform mechanism.
6. Run a new qualifying technical verification before Internet can become `Verified`.
7. Re-render the Protection Map from current evidence only.

### Protection consequence

- `Removed` remains until current setup evidence changes it;
- configuration alone does not upgrade state;
- new qualifying verification may establish `Verified`;
- unresolved/unsupported current conditions remain `Action needed`, `Status uncertain`, or `Not covered`.

### Escalation option

If reconfiguration repeatedly reaches the same unchanged failure, stop looping. Use SUP-01 exceptional escalation only when a current approved route exists; otherwise preserve the truthful failure/limitation state.

### Success state

A newly generated truthful Protection Map based on current evidence, with Internet `Verified` only when the new technical check qualifies.

## 10. SUP-05 — Unsupported / uncertain / limitations

**Entry:** current platform/device/network/profile/service tuple is unsupported, source-current guidance is absent, management authority blocks the path, or evidence is insufficient/conflicting.

### Accessible path

Any applicability/verification/support screen → `See limitations` / Help.

### Minimal diagnostics

Use the current known tuple. Ask only for the specific platform/version fact necessary to determine whether a current supported route exists.

### Flow

1. Show `Not covered` for established unsupported scope or `Status uncertain` for insufficient/conflicting evidence.
2. Explain the boundary concisely.
3. Link to current official platform information for understanding only when useful; do not convert it into a SafeWeb support claim.
4. Do not invent a client, VPN, profile, provider or account workaround.
5. Offer `Start setup again` only if a material condition changed or another genuinely supported platform branch is available.

### Protection consequence

The affected layer stays `Not covered` or `Status uncertain`; no confirmation or Help navigation upgrades it.

### Escalation option

Source/platform-support review may be escalated to the owning content/network/product authority when there is evidence the support matrix may be stale. That review does not give the current user an interim `Verified` state.

### Success state

A truthful limitation/uncertainty disposition with one safe next action or a clear stop; no misleading positive completion.

## 11. Escalation interaction contract

The UI may expose an exceptional `Report a problem` / equivalent escalation control only when the downstream implementation has a current approved operational route. Until then, the design contract defines the handoff semantics without promising a live human help desk.

Required escalation behavior:

- self-service remains primary;
- explain what minimal information will be sent before submission;
- submit only the relevant support category, platform/version when necessary, current state, instruction/test/reference ID, and the single volunteered destination for a false-positive case when applicable;
- do not attach raw DNS/browsing history, child identity, credentials, or unrelated screenshots by default;
- submission/acknowledgement does not change protection state;
- security/legal/safeguarding incidents follow their owning authority rather than this ordinary support flow.

## 12. Deterministic support-path matrix

| Test ID | Scenario | Expected outcome |
| --- | --- | --- |
| `TC-0334-01` | Android verification failure with known repair | `Action needed`; one current repair action; retry only after change. |
| `TC-0334-02` | iPhone conflict with insufficient evidence | `Status uncertain`; no green state; current safe next check only. |
| `TC-0334-03` | Unsupported/managed route | `Not covered` / `Status uncertain`; no bypass; Limitations accessible. |
| `TC-0334-04` | False-positive report while Internet is `Verified` | Report does not itself downgrade/upgrade DNS-path evidence; one destination only; no history requested. |
| `TC-0334-05` | False positive with no current exception route | Keep truthful current state or offer intentional removal; no invented allowlist. |
| `TC-0334-06` | Android removal | Exact custom provider removed; neutral connectivity checked; state `Removed`. |
| `TC-0334-07` | iPhone removal | Exact SafeWeb profile removed; managed authority respected; state `Removed`. |
| `TC-0334-08` | Connectivity still broken after removal | No false recovery claim; minimal general-network escalation/Help path. |
| `TC-0334-09` | Reconfigure after removal | New supported setup required; no stale verification reused. |
| `TC-0334-10` | Reconfigure after unchanged repeated failure | Stop loop; preserve truthful state; exceptional escalation only if current route exists. |
| `TC-0334-11` | Help/Limitations keyboard/mobile path | Accessible semantic controls/focus/state text; navigation is state-neutral. |
| `TC-0334-12` | Escalation submission | Minimal data only; acknowledgement does not alter protection state. |

## 13. Acceptance mapping

TSK-0334 acceptance is satisfied in this candidate as follows:

| Acceptance element | Candidate coverage |
| --- | --- |
| accessible path | §4 plus each SUP-01…SUP-05 `Accessible path` |
| minimal diagnostic request | §5 plus each category `Minimal diagnostics` |
| clear protection consequence | each SUP-01…SUP-05 `Protection consequence` |
| escalation option | each category `Escalation option` plus §11 |
| success state | each category `Success state` |

The 12-case matrix in §12 provides deterministic representative review/test cases without claiming pre-product human evidence.

## 14. HUMAN_ONLY decision boundary

This file is a prepared candidate only. It does not mark TSK-0334 PASS and does not claim Project Owner approval.

Recommended owner disposition:

`APPROVE TSK-0334 SUPPORT FALSE-POSITIVE REMOVAL RECONFIGURATION FLOWS`

Alternative:

`REVISE TSK-0334: <specific change>`

Only explicit owner disposition may close the TSK-0334 HUMAN_ONLY boundary. Approval does not itself authorize TSK-0335, TSK-0333, LG-06, L5/L6, real-user testing, public publication, payment, market activation or launch.