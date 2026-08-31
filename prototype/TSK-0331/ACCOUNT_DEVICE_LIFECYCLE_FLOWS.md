# TSK-0331 — Account and Device Lifecycle Interaction Prototype

**Version:** 1.0.0-post-cr0007  
**Task:** TSK-0331 — Design account/device deletion, reinstall, revoke, replacement and recovery flows  
**Acceptance:** ACC-0331  
**Action authority:** A4 / AUTO_ALLOWED  
**Date:** 2026-08-31  
**Status:** current candidate pending independent verification and runtime reconciliation

## 1. Purpose and scope

This prototype defines the Version-1 parent-facing lifecycle interactions that sit between the accepted TSK-0329 account experience, TSK-0332 dashboard/device-management experience, and current TSK-0334 support/recovery contract.

It covers account deletion, device-record deletion, unlink/revoke, physical UseSafeWeb protection removal, reinstall/reconfigure, replacement, logout/session expiry, provider failure, ownership mismatch, partial failure, unknown result and safe recovery.

The core service remains usable **without login**. Account/device lifecycle actions are management/data actions unless the flow explicitly enters the separate physical protection-removal path. Account deletion, record deletion or logout **does not remove UseSafeWeb protection** from a physical device.

This L4 interaction design does not choose Firebase/OAuth mechanics, database schema, backup retention, legal retention periods, storage vendor, authorization implementation or production deletion executor.

## 2. Security and truth invariants

1. Every destructive account/device mutation requires an explicit consequence screen before execution.
2. Ownership mismatch fails closed. The UI never exposes or mutates another account's device record.
3. Session expiry before or during a destructive action stops the mutation. Reauthentication may restore account access, but there is **no automatic replay** of the destructive operation.
4. Unknown destructive outcomes are not blindly retried. The product resolves authoritative current state first.
5. Provider failure, session expiry, account deletion, record deletion and unlinking do not change physical Protection Map truth by themselves.
6. Physical protection removal is a distinct flow and may show `Removed` only after the owning physical-removal result is confirmed.
7. Replacement creates a new device lifecycle. A new replacement device inherits no Verified or parent-confirmed state.
8. J0/J1 anonymous journey state remains separate from account and device-record deletion.
9. Routine flows request no browsing/query/activity history, raw DNS logs, child identity, provider password/token or broad network dump.
10. Cancellation must be safe and leave the pre-action state unchanged.

## 3. Lifecycle consequence matrix

| Action | Explicit confirmation | What changes on confirmed success | What does **not** change | Unknown/partial result |
| --- | --- | --- | --- | --- |
| Logout | No destructive-data confirmation; clear account-access consequence | Current authenticated session access ends | Account, device records, J0/J1, physical protection | Account-only access fails closed until session state is known |
| Delete account | Yes | Account and account-owned management data are removed according to the owning deletion contract; active account access ends | Physical protection; unrelated anonymous J0/J1 | Show `Result not confirmed`; resolve authoritative account state before retry |
| Remove dashboard record | Yes | Selected saved device record/management metadata is removed | Physical protection; account; other records; J0/J1 | Keep record state uncertain until authoritative read-back |
| Unlink/revoke device management | Yes | Account-to-device management association/revocable access is ended | Physical protection; unrelated records; J0/J1 | No automatic replay; resolve current association state |
| Remove UseSafeWeb protection | Yes | Physical UseSafeWeb configuration is removed when owning removal evidence confirms it; Protection Map may become `Removed` | Account/device record unless separately removed | Preserve prior/uncertain state until removal outcome is known |
| Reinstall/reconfigure | Consequence acknowledgement | Starts a new current setup/verification attempt | Earlier positive evidence is not silently reused | Failed/partial setup routes to support/recovery |
| Replace device | Yes | New device record/setup journey starts | Old device truth is not copied; no history/S1/S2 inheritance | Old record remains unchanged until explicit later action |

## 4. Deleted versus retained metadata semantics

This task defines product-visible semantic obligations, not a storage schema or legal retention period.

### 4.1 Confirmed account deletion

The owning downstream deletion implementation must remove or irreversibly disassociate the account-domain data required to make the account cease to function, including:

- the UseSafeWeb parent account record;
- account-owned device records and parent-chosen device nicknames;
- account-to-device management associations;
- account-scoped settings created solely for the optional account/dashboard;
- active UseSafeWeb account sessions;
- provider binding material only to the extent the approved authentication/data architecture stores and owns it.

The completion screen may say **Account deleted** only after that owning implementation returns authoritative completion.

### 4.2 Data not implied deleted by account deletion

Account deletion does not claim deletion/removal of:

- physical UseSafeWeb DNS configuration on a phone/device;
- anonymous J0/J1 state unless its separate lifecycle independently deletes it;
- data that a future approved legal/security/data contract explicitly requires to be retained for a limited purpose/period.

If the downstream data contract requires retained backup/audit/legal material, the production UI must state that precise retained category/purpose/period. TSK-0331 invents no retention exception or duration.

### 4.3 Confirmed dashboard-record deletion

Delete only the selected saved device-management record and its record-owned metadata under the owning data contract. Do not claim physical protection removal.

### 4.4 Unlink/revoke

End only the account-to-device management association or revocable account-side access represented by that action. Do not delete unrelated account data and do not claim physical protection removal.

## 5. Account deletion flow

### `LIFE-ACCOUNT`
Account hub exposes **Delete account**, **Log out**, Help and Back to devices.

### `LIFE-DELETE-ENTRY`
**Heading:** Delete your account  
Explain exactly what the account lifecycle covers and that it does not remove UseSafeWeb protection from devices.  
Primary: **Continue**. Secondary: **Cancel**.

### `LIFE-DELETE-CONFIRM`
**Heading:** Permanently delete your UseSafeWeb account?  
Show a compact checklist:

- account and account-owned saved device records will be removed under the approved deletion process;
- signed-in account access will end;
- UseSafeWeb protection on physical devices is separate and will not be removed;
- anonymous J0/J1 state follows its own expiry/deletion lifecycle.

Primary destructive control: **Delete account**.  
Secondary: **Cancel**.

### `LIFE-DELETE-PENDING`
Disable duplicate submission. Accessible status: **Deleting account — result being confirmed.**

Possible outcomes:

- confirmed success → `LIFE-DELETE-SUCCESS`;
- confirmed failure → `LIFE-DELETE-FAILED`;
- timeout/network/provider/unknown response → `LIFE-DELETE-UNKNOWN`.

### `LIFE-DELETE-SUCCESS`
Say **Account deleted** only after authoritative completion. Explain narrowly that physical UseSafeWeb protection is unchanged and may be removed separately.

### `LIFE-DELETE-FAILED`
No completion claim. Preserve the known account state and offer safe retry only after the failure cause is classified/corrected, or Help.

### `LIFE-DELETE-UNKNOWN`
Say **We could not confirm whether the account was deleted.** Disable another destructive submission until authoritative account state is resolved. Primary: **Check account status**. Never create a duplicate account or automatically retry deletion.

## 6. Device record and revoke/unlink flows

### `LIFE-DEVICE`
Device-management hub shows current management record and truthful Protection Map reference. Record presence is not technical verification.

### `LIFE-UNLINK-CONFIRM`
Explain: **Unlinking ends this account's management link. It does not remove UseSafeWeb protection from the physical device.**  
Primary: **Unlink device**. Secondary: Cancel.

`LIFE-UNLINK-PENDING` disables duplicate submit. Success → `LIFE-UNLINK-SUCCESS`; unknown → `LIFE-UNLINK-UNKNOWN` and authoritative read-back before retry.

### `LIFE-REMOVE-RECORD-CONFIRM`
Explain: **Removing this saved device record does not remove UseSafeWeb protection.**  
Primary: **Remove from dashboard**. Secondary: Cancel.

Confirmed success → `LIFE-REMOVE-RECORD-SUCCESS`. The physical protection state is explicitly unchanged.

## 7. Physical protection removal

### `LIFE-REMOVE-PROTECTION-CONFIRM`
This is the separate physical lifecycle. Explain that the parent is about to remove UseSafeWeb configuration from the physical device, which withdraws the active UseSafeWeb protection claim when the owning removal flow confirms success.

Primary: **Show removal steps** / execute only through the owning platform-specific removal flow. Secondary: Cancel.

### `LIFE-REMOVE-PROTECTION-SUCCESS`
Only after authoritative physical-removal confirmation: **UseSafeWeb protection removed**. The saved dashboard record/account remain unless separately changed.

A connectivity check proves connectivity only; it does not re-establish protection.

## 8. Reinstall / reconfigure recovery

### `LIFE-RECONFIGURE`
**Heading:** Reinstall or reconfigure  
Explain that previous protection evidence may no longer be current. Start a fresh supported setup path and require the owning technical check before a new Verified state appears.

Failure/partial setup routes to TSK-0334 support with truthful `Needs attention`, `Status uncertain` or `Not covered`; no stale green state is preserved.

## 9. Replacement flow

### `LIFE-REPLACE-CONFIRM`
**Heading:** Replace this device?  
Explain that the new device starts independently and the old device record/protection state will not be silently copied.  
Primary: **Start replacement**. Secondary: Cancel.

### `LIFE-REPLACE-NEW`
Create/open the new device setup journey with an unverified fresh status. The replacement inherits no Verified or parent-confirmed state and no browsing/query/activity history.

The old device remains unchanged until separately unlinked, removed from dashboard or physically deconfigured.

## 10. Session expiry and provider failure

### `LIFE-SESSION-EXPIRED`
If a session expires before a destructive action completes, stop that account-only mutation. Explain: **Sign in again to continue managing your account. The action was not automatically repeated.**

After reauthentication, return to a safe account state. The parent must explicitly reopen and reconfirm any destructive action.

### `LIFE-PROVIDER-ERROR`
Provider/account access failures affect account-only access. They do not alter current physical protection truth. Offer **Continue without account**, Help and safe later reauthentication.

## 11. Ownership mismatch

### `LIFE-OWNERSHIP-MISMATCH`
Fail closed with parent-facing copy: **This saved device cannot be managed from this account.**

Do not reveal another account identity, record detail, provider identifier or internal authorization reason. Support cannot override ownership. Available actions: Back to own devices, Start setup without account, Help.

## 12. Recovery controller

### `LIFE-RECOVERY`
Recovery is state-based:

1. read authoritative current account/device operation state;
2. classify confirmed success, confirmed failure, still-pending or unknown;
3. render that result narrowly;
4. enable retry only when the prior outcome is known and retry is safe/idempotent;
5. never infer physical protection changes from account/device management state.

This controller is the required recovery path for account deletion, unlink/revoke and record-deletion unknown outcomes.

## 13. Partial/provider failure matrix

| Failure | Required behavior | Forbidden behavior |
| --- | --- | --- |
| Provider unavailable before mutation | Keep action unexecuted; accountless core remains | Claim deletion/revoke success |
| Session expires at confirmation | Reauthenticate for account access; require fresh confirmation | Automatically replay destructive action |
| Network drops after submit | Treat result as unknown; authoritative read-back | Blind duplicate request |
| Server reports confirmed failure | Preserve known state; show cause class/recovery | Display success |
| Ownership mismatch | Fail closed | Expose/mutate cross-account record |
| Physical removal partially completed | Route to owning removal recovery; state uncertain until proven | Mark Removed without evidence |
| Replacement setup fails | New device remains unverified/action-needed | Copy old Verified state |

## 14. Accessibility / localization

Target WCAG 2.2 AA interaction behavior:

- semantic landmarks/headings;
- visible keyboard focus;
- skip link to main content;
- state changes announced with `aria-live`;
- destructive confirmation names the consequence and does not rely on color;
- state transition moves focus to the new state heading;
- minimum 320px mobile layout with no page-level horizontal overflow;
- English/Turkish/Arabic+RTL capability without changing consequence semantics;
- reduced-motion support.

## 15. Deterministic acceptance cases

| ID | Scenario | Required result |
| --- | --- | --- |
| D31-01 | Cancel account deletion | Account/device/protection state unchanged. |
| D31-02 | Confirm account deletion | Explicit confirmation before mutation; pending state prevents duplicate submit. |
| D31-03 | Account deletion success | Narrow account/data success; no physical-removal claim. |
| D31-04 | Account deletion failure | No success claim; safe recovery. |
| D31-05 | Account deletion unknown | Authoritative read-back before retry. |
| D31-06 | Session expires before destructive action | Reauth; no automatic replay; fresh confirmation required. |
| D31-07 | Provider failure | Account-only failure; core/protection truth unchanged. |
| D31-08 | Ownership mismatch | Fail closed; no cross-account disclosure/mutation. |
| D31-09 | Unlink success | Management link removed only. |
| D31-10 | Unlink unknown | Block duplicate; resolve authoritative state. |
| D31-11 | Remove dashboard record | Record removed only; physical protection unchanged. |
| D31-12 | Remove physical protection | Separate confirmed removal path; record/account unchanged. |
| D31-13 | Reconfigure | Earlier positive evidence not silently retained. |
| D31-14 | Replace device | New device inherits no Verified/parent-confirmed state/history. |
| D31-15 | J0/J1 | Account/device deletion never claims J0/J1 deletion. |
| D31-16 | Privacy | No browsing/query/activity history, raw DNS logs, child identity or provider secret requested. |
| D31-17 | 320px | No horizontal page overflow. |
| D31-18 | Keyboard | Skip link and state controls work with visible focus. |
| D31-19 | Arabic RTL | Same lifecycle semantics under RTL. |
| D31-20 | Unknown destructive outcome | No blind retry or false completion. |

## 16. Non-inference boundary

This L4 prototype does not approve provider/vendor/security/privacy architecture, storage schema, authorization implementation, backup/legal retention policy, production deletion executor, production DNS removal, build/deployment behavior, real-user validation, TSK-0333 or LG-06. `RSK-0002` remains OPEN/non-blocking before L8.
