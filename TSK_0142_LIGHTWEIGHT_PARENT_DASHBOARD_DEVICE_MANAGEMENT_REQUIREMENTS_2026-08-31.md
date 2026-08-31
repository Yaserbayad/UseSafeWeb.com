# TSK-0142 — Lightweight Parent Dashboard and Device-Management Requirements

**Task:** TSK-0142 — Specify lightweight parent dashboard and device-management requirements  
**Acceptance:** ACC-0142  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Package:** PKG-02  
**Version:** 1.0.0  
**Date:** 2026-08-31  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE  
**Authority:** current TSK-0312 PASS + current compatible TSK-0041 DNS-activation requirements + DEC-0053/CR-0006 + DEC-0054/CR-0007 + current TSK-0140 brief + TSK-0229 separation rules + TSK-0313/TSK-0320 evidence-state semantics

## 1. Purpose and scope boundary

Version 1 includes a **lightweight optional parent dashboard/device-management experience** for continuity. It is not a surveillance console, raw DNS administration interface, child account/profile system, or prerequisite for core safety value.

The complete First Phone Safety Setup core remains usable without login. A parent who chooses an account may use the dashboard to identify their own saved device records, continue supported setup/recovery work, request current verification, understand truthful Protection Map status, and perform bounded lifecycle actions.

This task defines product requirements only. It does not approve persistent schema/storage architecture, authentication implementation, provider configuration, device-side code, AdGuard control-plane exposure, production behavior, or LG-06.

No real-parent/user behavioral evidence is claimed; RSK-0002 remains open and non-blocking before L8 under current sequencing.

## 2. Dashboard product objective

The dashboard shall answer five bounded questions for an authenticated parent:

1. **Which device records have I explicitly chosen to manage?**
2. **What is the strongest truthful current/last-known protection evidence for each device?**
3. **What action is needed next, if any?**
4. **How do I verify, repair, reinstall/reconfigure, replace, revoke/unlink or remove safely?**
5. **What does UseSafeWeb not know or cover?**

It shall not answer “what did my child browse?”, “what apps/messages/location did my child use?”, or expose unrestricted AdGuard administration.

## 3. Dashboard entry and accountless-core rule

### DASH-01 — Optional entry

- Dashboard entry requires a valid parent account/session under TSK-0312.
- Login/dashboard shall never be required to start, configure, verify, understand, recover or remove the complete accountless core protection journey.
- A sign-in/session/provider failure shall not make already configured DNS disappear or convert a technical protection state into a false failure/success claim.
- Dashboard-only controls shall be visibly distinguished from accountless core controls.

### DASH-02 — No silent accountless promotion

- Creating/signing into an account shall not automatically import J0/J1 accountless journey state.
- Adding a device to the dashboard is an explicit parent action governed by the downstream approved dual-mode data-flow design.
- Until such transfer semantics are explicitly approved, account creation and accountless journey data remain separate under TSK-0229.

## 4. Minimum device-list model

The product requires a **minimum semantic device record**. Exact field names/types/storage remain downstream, but no implementation may expand the semantic data set merely for convenience.

| Semantic field/class | Necessity | Requirement |
| --- | --- | --- |
| Opaque device-record ID | Stable dashboard record/reference | Required; not a public/human identity. |
| Parent-account ownership reference | Enforces which parent may manage the record | Required under approved authz architecture. |
| Parent-chosen device nickname or safe generic default | Lets the parent distinguish multiple devices | Required as a display concept; child name is not required. |
| Supported platform/family context | Routes correct setup/recovery instructions | Minimum supported context only; avoid unnecessary device fingerprinting. |
| Device-record lifecycle state | Distinguishes active/replaced/revoked-unlinked/removed states | Required for truthful management. |
| Setup/protection state references needed for the approved dashboard | Supports continue/verify/repair and Protection Map display | Minimum only; must preserve evidence actor/currentness and may not become browsing/activity history. |
| Verification/evidence freshness metadata where required by owning verifier | Prevents stale S1 from masquerading as current proof | Store/display only what downstream privacy/security/data-model work authorizes; no universal TTL is invented here. |

### Nickname requirements

- Parent may rename a device record.
- The UI shall not require a child name, email, birth date or other child identity as the nickname.
- A generic default such as the supported platform/device family is acceptable if the parent supplies no personal label.
- Nickname input shall be bounded/validated under downstream UX/schema rules and shall not be reused as diagnostics, analytics or a hidden child profile.

## 5. Device list presentation

For each device record, the dashboard shall present only the minimum information needed to identify status and next action:

- nickname/generic device label;
- supported platform/family indicator where useful;
- device-record lifecycle state when not active;
- Protection Map summary or truthful status requiring attention;
- evidence actor/freshness context sufficient to avoid treating historical status as current proof;
- one primary next action when needed;
- compact access to bounded management/help actions.

The list shall not display browsing/query/domain/activity history, “top sites,” child activity scores, time spent, location, messages, contacts, photos or social content.

## 6. Protection Map and truthful protection status

### 6.1 State semantics retained

TSK-0320 remains the semantic owner for the six evidence-strength states:

- **S1 — Protected / Verified**
- **S2 — Set up / Parent confirmed**
- **S3 — Action needed**
- **S4 — Not covered**
- **S5 — Status uncertain / error**
- **S6 — Removed**

TSK-0313 remains the product contract for applying those semantics across Phone / Internet / Services. CR-0006 supersedes only the earlier assumption that no account/dashboard persistence exists; it does **not** weaken the evidence thresholds, copy semantics, state precedence or transition truth.

### 6.2 Dashboard persistence must not create false verification

- Account/device ownership, a device-record row, dashboard presence or historical setup completion never yields S1.
- DNS S1 requires current qualifying technical evidence under TSK-0041/owning verifier rules and no known contradiction.
- If a previously verified context has materially changed or current evidence cannot establish validity, the dashboard shall use S5/S3 or an explicitly historical “last verified” presentation rather than stale current S1.
- Parent confirmation may support S2 only where the owning state contract allows it; it shall never be relabeled as system verification.
- S6 immediately withdraws the active protection claim for the removed safeguard.
- One layer never upgrades another layer. The dashboard shall not collapse Phone/Internet/Services into one “safe” score.

### 6.3 Historical versus current evidence

If downstream architecture persists a prior verification result for continuity:

- the UI shall identify it as historical when currentness cannot be established;
- it shall preserve the evidence actor and time/context needed by the owning verifier to determine whether re-verification is required;
- it shall not invent a universal “verified for N hours/days” TTL;
- any owning re-verification trigger overrides a stored optimistic state;
- a direct current contradictory result reopens/demotes the displayed state immediately.

## 7. Required device-management actions

### DEV-01 — Add device

- Parent explicitly chooses **Add device**.
- Product routes only into currently supported setup paths.
- A new managed device record shall not be created from anonymous J0/J1 state by silent linkage.
- Any explicit save/transfer from an active accountless journey requires the approved downstream data-flow contract.
- Adding a record does not mean protection is configured or verified.

### DEV-02 — Setup / continue setup

- Resume the appropriate supported Phone → Internet → Service/Protection Map path using only authorized saved state.
- Do not skip required technical verification because the device is already in the dashboard.
- Unsupported combinations use truthful Not covered/uncertain behavior rather than invented fallback setup.

### DEV-03 — Verify / re-verify

- Provide a clear **Verify** action where an approved technical verifier exists.
- For UseSafeWeb DNS, use the current TSK-0041 semantics: configuration presence alone is insufficient; controlled technical/filtering evidence is required for S1.
- Re-verification shall update displayed state according to current evidence, including downgrade to S3/S4/S5/S6 when justified.
- Routine verification shall not require browsing-history collection.

### DEV-04 — Reinstall / reconfigure

- Offer the current supported platform-specific reinstall/reconfiguration route.
- Starting reconfiguration invalidates any stale optimistic state as required by the owning state contract.
- Successful configuration still requires the appropriate confirmation/technical verification before positive state is restored.

### DEV-05 — Replace device

- Parent can mark a managed device as replaced and start a new device flow.
- A replacement record is not allowed to inherit S1/S2 merely because the prior device had that state.
- No browsing/activity history is copied.
- Any settings/state transfer requires an explicitly approved field-level downstream transfer rule; otherwise the new device starts from current setup requirements.
- The old record shall remain truthfully marked replaced/removed/unlinked according to the chosen lifecycle action until its downstream deletion rule completes.

### DEV-06 — Revoke / unlink dashboard management

- **Revoke/unlink** means ending the account’s management/ownership association for that dashboard device record according to the approved data model/authz architecture.
- It shall not be described as removing UseSafeWeb DNS from the physical device unless the technical removal is separately performed and verified.
- After successful unlink, the account shall not retain unauthorized management access to that record.
- If revocation status is uncertain, account-only management fails closed and the UI states uncertainty rather than success.

### DEV-07 — Remove UseSafeWeb protection from device

- The dashboard may route the parent to the approved platform-specific removal flow.
- Android/iPhone removal semantics follow TSK-0041 and current device-support requirements.
- A device shall show S6 only when the owning removal evidence/confirmation supports it.
- Removing protection from the phone and removing/unlinking the dashboard record are separate operations.

### DEV-08 — Remove/delete dashboard device record

- Parent may explicitly remove a device record from the dashboard under the approved data-deletion contract.
- Deleting the record does not claim DNS/configuration removal from the physical phone.
- If product design offers both “Remove protection” and “Remove from dashboard,” the copy and confirmation must make the difference explicit before execution.

## 8. Curated controls — allowed surface

The Version-1 dashboard may expose only bounded product controls that serve the approved journey/lifecycle, including:

- rename device;
- add device;
- continue setup;
- verify/re-verify;
- view Protection Map/current limitations;
- troubleshoot a current issue;
- reinstall/reconfigure;
- replace device;
- revoke/unlink management association;
- remove UseSafeWeb protection through approved device instructions;
- remove/delete dashboard device record;
- account/session/logout/deletion entry points governed by TSK-0312;
- contextual help.

Exact interaction placement remains downstream UX work.

## 9. Explicit dashboard non-goals

The dashboard shall **not** expose or create:

- browsing history, DNS-query history, visited/top domains or app/activity history;
- surveillance timelines, child location/messages/contacts/photos/social content;
- child accounts or child behavioral profiles;
- raw/unrestricted AdGuard administration;
- AdGuard admin credentials;
- upstream DNS configuration controls;
- arbitrary filter-list management;
- customer-facing query logs;
- broad per-domain allow/block administration;
- a persistent personalized allowlist merely because accounts exist;
- complete-safety scores or “your child is safe” claims;
- account/device ownership as technical protection proof;
- mandatory login for core safety value;
- payment/paywall controls required for safety value.

A future material expansion of controls requires its own authority and privacy/security/product evidence.

## 10. Help and self-service requirements

Every ordinary dashboard failure/action shall have a privacy-minimal self-service path:

- setup incomplete → continue exact supported step;
- verification failed with known repair → show the repair and re-check;
- status uncertain → explain what cannot currently be established and provide a safe next action when one exists;
- unsupported device/network → explain Not covered without fabricating fallback;
- suspected false positive → use the narrow TSK-0041 support/exception process; no blanket filtering disablement;
- session/account problem → use TSK-0312 re-authentication/recovery behavior;
- remove/reinstall/reconfigure → platform-specific current instructions;
- record/account deletion → truthful pending/success/error state.

Routine support shall not require parents to submit browsing history. Exceptional diagnostics remain separately governed and time-limited.

## 11. Account lifecycle interactions

- Logout ends authenticated dashboard access but does not delete the account, device records or DNS configuration.
- Session expiry/revocation requires re-authentication before account-only actions; it does not imply DNS protection stopped.
- Account deletion initiates deletion of account/device-ownership data under the downstream data contract and invalidates sessions, but does not itself claim physical DNS configuration removal.
- Device-record deletion, account deletion, anonymous J0/J1 deletion and DNS configuration removal remain distinct operations.
- If account deletion is pending/failed/uncertain, the dashboard shall not show a false completed state.

## 12. Error and recovery states

The product shall represent at least these dashboard errors distinctly:

- session expired/invalid;
- provider/account unavailable;
- unauthorized/ownership mismatch;
- device record missing/deleted/revoked;
- supported setup incomplete;
- technical verification failed with known repair;
- protection status uncertain/conflicting/stale;
- unsupported device/network path;
- reinstall/reconfigure failure;
- revoke/unlink failure or uncertain result;
- physical protection-removal failure/uncertainty;
- dashboard-record deletion failure/uncertainty;
- account deletion pending/failure.

Errors shall fail closed for account-only authority while preserving truthful accountless core/recovery access where applicable.

## 13. Data-minimisation requirements

- Dashboard persistence is limited to the minimum parent/account/device ownership/settings/lifecycle/protection-state metadata authorized by downstream data/privacy architecture.
- No browsing/query/domain/activity history is required or permitted as dashboard content.
- No child identity is required to identify a device record.
- Device nickname is a parent convenience field, not a child profile.
- Technical verification data shall be synthetic/minimum and shall not become a history product.
- Accountless J0/J1 remains separate unless a later explicit transfer contract is approved.
- Diagnostics/logs/backups shall not become a hidden history path.

## 14. Accessibility, responsive and localization requirements

- Dashboard/device-management surfaces inherit the WCAG 2.2 AA target and responsive mobile-first requirements.
- Status cannot be communicated by color alone; S1/S2 and S3/S4/S5/S6 must remain semantically distinguishable by accessible text/structure.
- Device actions, destructive confirmations, errors, pending/unknown states and recovery controls require clear labels, focus behavior and accessible error association in downstream UX specs.
- English, Turkish and Arabic/RTL technical capability applies to dashboard/account/status/help surfaces.
- Translations must preserve evidence strength and shall not imply official non-UK market/support/legal readiness without LG-16.

## 15. Minimum deterministic/synthetic acceptance cases

| Test ID | Scenario | Expected result |
| --- | --- | --- |
| DASH-T01 | Complete core journey while signed out | Core remains fully usable without dashboard/login. |
| DASH-T02 | Sign in with no saved devices | Empty dashboard explains optional continuity and offers Add device; no history/profile is invented. |
| DASH-T03 | Add supported device | Explicit flow starts; record presence alone does not show Verified. |
| DASH-T04 | Rename device | Parent can distinguish device without being required to enter child identity. |
| DASH-T05 | DNS setup present but unverified | Internet layer is not S1 solely from record/config presence. |
| DASH-T06 | Current DNS verifier succeeds | S1 is allowed only for exact verified supported mechanism; evidence actor is UseSafeWeb/system. |
| DASH-T07 | Parent confirms non-verifiable native/service safeguard | S2 is shown and is not labeled Verified. |
| DASH-T08 | VPN/Private Relay/browser/network conflict makes DNS path uncertain | S5 replaces stale positive state until resolved. |
| DASH-T09 | Supported repairable verification failure | S3 with exact next action; successful recheck can restore S1. |
| DASH-T10 | Unsupported device/network | S4/Not covered; no fabricated fallback/admin control. |
| DASH-T11 | Reinstall/reconfigure | Stale current-verification claim is withdrawn until qualifying evidence returns. |
| DASH-T12 | Replace device | New device does not inherit prior S1/S2 or history automatically. |
| DASH-T13 | Revoke/unlink dashboard association | Account loses management association; UI does not claim DNS was removed. |
| DASH-T14 | Remove UseSafeWeb protection | Approved physical removal flow yields truthful S6 only with required evidence/confirmation; record deletion remains separate. |
| DASH-T15 | Remove dashboard record only | Record is removed per data contract; UI does not claim physical DNS removal. |
| DASH-T16 | Logout/session expiry | Dashboard access ends/re-auth is required; configured DNS/protection is not falsely reported as removed. |
| DASH-T17 | Account deletion | Sessions/account/device ownership data follow deletion contract; DNS removal remains separate. |
| DASH-T18 | Browsing/query/history inspection | No history/top-domain/activity surface or data requirement exists. |
| DASH-T19 | Raw DNS/admin inspection | No AdGuard credentials, upstream/filter-list/query-log/unrestricted admin surface exists. |
| DASH-T20 | English/Turkish/Arabic + RTL and non-color state distinction | All required states/actions/errors are localizable/accessibly distinguishable without implying market activation. |

## 16. Reconciliation of pre-CR-0006 accountless-only clauses

Current TSK-0313/TSK-0320 evidence-state semantics were originally written when persistent account/dashboard scope was excluded. CR-0006 changes only that product-persistence assumption for the bounded optional parent account.

Therefore:

- **SUPERSEDED for account scope:** statements that no dashboard/device registry may exist at all.
- **RETAINED:** S1–S6 evidence thresholds, parent-confirmed versus system-verified distinction, state precedence, unsupported/uncertain/removed semantics, mixed-layer truth, no aggregate safety score, no surveillance/history, and re-verification when evidence context changes.
- **RETAINED:** TSK-0041 DNS activation/verification/removal/conflict/no-history semantics.
- **RETAINED:** TSK-0041’s no broad/per-device persistent allowlist assumption unless a future separately authorized feature changes it.
- **NEW bounded capability from CR-0006:** minimum persistent parent/device ownership/settings/lifecycle state and lightweight dashboard/device management.
- **NOT inferred:** history reporting, child profile, raw DNS admin, current verification from ownership, or any L5/L6/L7 acceptance.

## 17. ACC-0142 coverage statement

ACC-0142 requires requirements for parent device list/nickname; add/setup/verify/reinstall/replace/revoke/remove; truthful protection status; Protection Map; curated controls; help and account lifecycle; with browsing/query/activity history and unrestricted DNS administration as explicit non-goals.

Every required dimension is specified above with testable outcome semantics and explicit privacy/security/evidence boundaries.

**Candidate disposition:** ACC-0142 is ready for independent post-publication verification. TSK-0142 remains non-PASS until that verification and durable runtime reconciliation succeed.
