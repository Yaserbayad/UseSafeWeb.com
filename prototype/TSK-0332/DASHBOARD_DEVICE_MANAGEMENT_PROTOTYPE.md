# TSK-0332 — Lightweight Parent Dashboard and Device-Management Prototype

**Version:** 1.0.0-post-cr0007  
**Task:** TSK-0332  
**Acceptance:** ACC-0332  
**Lifecycle:** L4  
**Action authority:** A4 / AUTO_ALLOWED  
**Date:** 2026-08-31  
**Status:** current candidate pending independent verification and runtime reconciliation

## 1. Purpose

This prototype translates current accepted TSK-0329 account interactions and TSK-0142 dashboard/device-management requirements into one polished, mobile-first parent experience. It covers the optional signed-in dashboard only; the complete core setup, verification, troubleshooting, recovery and removal journey remains usable **without login**.

The dashboard is a continuity and bounded management surface, not a child-monitoring product, raw network-administration console or source of technical protection truth. Record presence, sign-in, session validity and dashboard presence never establish **Verified** protection.

## 2. Parent-language design rules

1. Use parent-facing language: **Protection**, **Needs attention**, **Not covered**, **Status uncertain**, **Removed**, **Check again**, **Continue setup**, **Get help**.
2. Do not expose implementation/vendor administration terminology on the normal dashboard. Technical setup instructions may explain the exact supported setting only when the parent enters that setup flow.
3. Show one primary next action per device state; secondary management actions sit behind a clearly labelled Manage area.
4. Never collapse Phone / Internet / Services into a single safety score.
5. Never use color alone for status. Every state has visible text and an accessible label.
6. Destructive or lifecycle actions state their consequence before continuation.
7. Provider/session/account errors affect account-only access; they do not alter configured protection truth.
8. Device-record deletion is distinct from physical UseSafeWeb protection removal.
9. The prototype contains no browsing/query/activity history, child profile, top-sites surface, raw administration, broad per-domain controls or customer query logs.
10. English, Turkish and Arabic/RTL capability is supported without implying non-UK market activation.

## 3. Mobile-first shell

### Header
- Brand: **UseSafeWeb**.
- Page title: **Your devices**.
- Account menu: **Account**.
- No technical administration link is present.

### Primary navigation
On mobile the dashboard is a single-column flow. At larger widths, the device list and contextual detail may form a two-column layout, but information order remains identical.

Primary surfaces:
- Devices
- Add device
- Help
- Account

The minimum supported viewport is 320px wide. Controls preserve visible focus, readable labels and touch-friendly spacing. Reduced-motion preference disables non-essential transitions.

## 4. Empty dashboard

### `DASH-EMPTY` — empty dashboard

**Heading:** Your devices  
**Empty heading:** No saved devices yet  
**Body:** Add a device only if you want to return to its setup and protection status later. You can still use UseSafeWeb without saving a device.  
**Primary:** Add device  
**Secondary:** Start setup without saving  
**Contextual help:** What does saving a device do?

Rules:
- no child name/profile is requested;
- no history or activity placeholder is shown;
- account creation does not silently create a device record;
- an empty dashboard is a valid state, not an error.

## 5. Device list and card

Each device card contains only:
- parent-chosen nickname or safe generic device label;
- supported platform/family where useful;
- truthful Protection Map summary;
- evidence freshness wording when currentness matters;
- one primary next action;
- **Manage** and **Help** secondary controls.

Example card:

**Family iPhone**  
Protection status: **Needs attention**  
Internet protection: **Check again**  
Last confirmed result: **Earlier result — check again to know current status**  
Primary: **Check again**  
Secondary: **Manage** · **Help**

The card never displays child identity, visited sites, search history, domain history, activity duration or location.

## 6. Protection Map presentation

Every managed device can open **Protection Map** with three independently truthful layers:

| Layer | Example status | Parent meaning |
| --- | --- | --- |
| Phone | Protected / Set up / Needs attention / Not covered / Status uncertain / Removed | Device-level safeguard state. |
| Internet | Protected / Set up / Needs attention / Not covered / Status uncertain / Removed | UseSafeWeb protection state based on current allowed evidence. |
| Services | Protected / Set up / Needs attention / Not covered / Status uncertain / Removed | Supported service-level safeguard state. |

State rules:
- **Protected** is used only when the owning verifier has current qualifying technical evidence.
- **Set up** is parent-confirmed where allowed and is never labelled Verified.
- **Needs attention** provides one concrete repair/next action.
- **Not covered** states the unsupported boundary without invented fallback.
- **Status uncertain** replaces stale/contradictory positive claims when current status cannot be established.
- **Removed** withdraws the active protection claim for that layer.
- One layer never upgrades another.

## 7. Core device states

### `DASH-DEVICE-PROTECTED`
Primary message: **Protection confirmed**.  
Secondary evidence line identifies current verification context without exposing diagnostic internals.  
Primary action: **View Protection Map**.  
Secondary: **Check again**.

### `DASH-DEVICE-PARENT-CONFIRMED`
Primary message: **Set up — parent confirmed**.  
Never display this as system-verified.  
Primary: **View Protection Map**.

### `DASH-DEVICE-ACTION`
Primary message: **Needs attention**.  
Show the exact supported repair or **Continue setup**.  
After repair, the parent must **Check again** before a stronger technical state appears.

### `DASH-DEVICE-NOT-COVERED`
Primary message: **Not covered**.  
Explain what is unsupported and provide Help; do not expose raw configuration workarounds.

### `DASH-DEVICE-UNCERTAIN`
Primary message: **Status uncertain**.  
Explain that current protection could not be confirmed.  
Primary: **Check again** when a verifier exists; otherwise show the safest supported recovery/help step.

### `DASH-DEVICE-REMOVED`
Primary message: **UseSafeWeb protection removed**.  
Do not imply the dashboard record was deleted.  
Offer **Set up again** and **Remove from dashboard** as distinct actions.

## 8. Add device and setup continuation

### `DASH-ADD`
**Heading:** Add a device  
**Body:** Choose the device type you want to manage. Saving a device does not mean protection is already set up.  
Supported choices route only to currently supported setup paths.  
No child identity is required. A safe generic nickname is allowed.

### `DASH-CONTINUE-SETUP`
Show:
- current supported step;
- what remains to be completed;
- **Continue setup**;
- **Back to device**;
- **Help**.

Do not skip technical verification because a device record exists.

## 9. Verify / re-verify

### `DASH-VERIFY`
**Heading:** Check protection  
**Body:** UseSafeWeb will check the supported protection signal needed for this device.  
**Primary:** Check now

Outcomes:
- qualifying current evidence → allowed stronger state;
- repairable failure → **Needs attention** + exact next action;
- unsupported → **Not covered**;
- conflict/stale/unknown → **Status uncertain**;
- removed → **Removed**.

A stored device record, account ownership or earlier positive result cannot substitute for current qualifying evidence.

## 10. Curated Manage controls

The Manage surface contains only bounded controls required by the approved product journey:

- Rename device
- Continue setup
- Verify / reverify
- Reinstall or reconfigure
- Replace device
- Unlink from dashboard
- Remove UseSafeWeb protection
- Remove from dashboard
- Account
- Logout
- Help

No raw administration, filter-list editor, broad per-domain allow/block controls, query logs or activity-history controls appear.

## 11. Reinstall / reconfigure

### `DASH-RECONFIGURE`
Explain that reconfiguration may make an earlier protection result no longer current.  
Primary: **Continue reconfiguration**  
Secondary: **Cancel** · **Help**

After configuration, do not restore a stronger positive state until the required confirmation/verification succeeds.

## 12. Replace device

### `DASH-REPLACE`
**Heading:** Replace this device  
**Body:** The new device starts with its own setup and protection status. It does not inherit this device’s verified or parent-confirmed state.  
Primary: **Start replacement**  
Secondary: **Cancel**

No activity history is copied. Any later approved field-level transfer remains separately governed.

## 13. Unlink dashboard management

### `DASH-UNLINK`
**Heading:** Unlink this device from your dashboard?  
**Body:** This ends this account’s management link. It does not remove UseSafeWeb protection from the physical device.  
Primary: **Unlink device**  
Secondary: **Cancel**

Unknown outcome: account-only management fails closed and the UI shows **We could not confirm the unlink result** until resolved.

## 14. Remove physical protection

### `DASH-REMOVE-PROTECTION`
**Heading:** Remove UseSafeWeb protection  
**Body:** Follow the supported steps on the physical device. Removing protection is separate from removing this saved dashboard record.  
Primary: **Show removal steps**  
Secondary: **Cancel** · **Help**

Only the owning removal evidence/confirmation may produce **Removed**.

## 15. Remove dashboard record

### `DASH-REMOVE-RECORD`
**Heading:** Remove from dashboard?  
**Body:** This removes the saved device record from your account under the approved deletion process. It does not remove UseSafeWeb protection from the physical device.  
Primary: **Remove from dashboard**  
Secondary: **Cancel**

Pending/failed/uncertain deletion never shows false completion.

## 16. Contextual help

### `DASH-HELP`
Help is available from every ordinary state and requests the minimum information needed.

Categories:
- Finish setup
- Protection check failed
- Status uncertain
- Device or network not covered
- Reinstall or reconfigure
- False positive / site blocked unexpectedly
- Remove protection
- Account or session problem
- Device record problem

Routine help never asks for browsing/query/activity history. Technical detail is revealed only when needed to complete a supported action.

## 17. Account/session/error states

### `DASH-SESSION-EXPIRED`
**Heading:** Sign in again to manage saved devices  
**Body:** Your account session ended. This does not mean protection stopped on your devices.  
Primary: **Continue with Google**  
Secondary: **Start setup without account** · **Help**

### `DASH-ACCOUNT-ERROR`
Distinct reasons include:
- provider/account unavailable;
- unauthorized or ownership mismatch;
- device record missing/deleted/revoked;
- deletion/revocation result uncertain.

Account-only access fails closed. Signed-out core and Help remain available where applicable. No account error rewrites the current physical protection state.

## 18. Accessibility and localization

Target: **WCAG 2.2 AA**.

- semantic headings and landmarks;
- visible keyboard focus using `:focus-visible`;
- status changes announced through an `aria-live` region;
- status text is not color-only;
- destructive controls use explicit consequence text;
- focus moves to the new state heading after in-prototype navigation, while initial page load preserves normal keyboard order;
- minimum 320px mobile layout with no horizontal page scrolling;
- desktop enhancement at larger widths without changing reading order;
- `prefers-reduced-motion` removes non-essential transitions;
- English, Turkish and Arabic are supported; Arabic uses RTL layout while state meaning and control order remain semantically correct.

## 19. Deterministic acceptance scenarios

| ID | Scenario | Expected outcome |
| --- | --- | --- |
| D32-01 | Signed in with no saved devices | Empty dashboard + Add device; no invented history/profile. |
| D32-02 | Add supported device | Explicit add flow; record presence never establishes Verified. |
| D32-03 | Protected/current evidence | Protected appears only with qualifying current evidence. |
| D32-04 | Parent-confirmed safeguard | Set up / parent confirmed remains distinct from verified. |
| D32-05 | Repairable problem | Needs attention + one next action. |
| D32-06 | Unsupported combination | Not covered + Help; no invented admin fallback. |
| D32-07 | Stale/conflicting evidence | Status uncertain replaces stale optimistic status. |
| D32-08 | Reverify success | Current truthful state updates from new evidence. |
| D32-09 | Reconfigure | Earlier verification is not silently retained. |
| D32-10 | Replace device | New record inherits no S1/S2 or history. |
| D32-11 | Unlink device | Management link ends; no physical-removal claim. |
| D32-12 | Remove physical protection | Separate removal flow; Removed only with required evidence. |
| D32-13 | Remove dashboard record | Record deletion makes no physical-removal claim. |
| D32-14 | Session expiry | Re-auth for account-only access; physical protection truth unchanged. |
| D32-15 | Ownership mismatch | Account-only action fails closed. |
| D32-16 | Help from error | Privacy-minimal contextual recovery available. |
| D32-17 | 320px viewport | No horizontal page scrolling; controls remain usable. |
| D32-18 | Keyboard | All controls reachable; visible focus; state change focus announced. |
| D32-19 | Arabic | RTL layout without semantic/control inversion. |
| D32-20 | Scope audit | No browsing/query/activity history, child profile, raw administration or broad per-domain controls. |

## 20. Non-inference boundary

This L4 prototype does not approve or infer provider/vendor/security/privacy architecture, persistent schema/storage/retention/backup/authz implementation, production account deletion, build/deployment behavior, real-parent behavioral evidence, LG-06 or any later gate PASS. `RSK-0002` remains OPEN/non-blocking before L8.
