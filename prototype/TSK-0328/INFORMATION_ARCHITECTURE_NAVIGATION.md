# TSK-0328 — Information Architecture and Navigation Model

**Version:** 2.0.0-post-cr0007  
**Status:** current L4 candidate for independent acceptance  
**Owner:** UX/UI  
**Action authority:** A3 / AUTO_ALLOWED  
**Sequencing:** DEC-0052/CR-0005 + DEC-0053/CR-0006 + DEC-0054/CR-0007  
**Human-validation claim:** none; real-user validation remains deferred to L8 after LG-09 PASS  
**Build/publication authority:** none

## 1. Purpose, supersession and authority

This contract defines the current information architecture and navigation model for UseSafeWeb. It supersedes TSK-0328 v1.0.0 where that version explicitly excluded Login, Account and Dashboard. Those exclusions are stale under DEC-0053/CR-0006 because Version 1 now includes an optional parent account/session, minimum parent/device ownership persistence and lightweight dashboard/device management while preserving the complete accountless core.

Current source order for this artifact:

1. current owner-frozen WBS, graph, decisions, constraints and runtime authority;
2. current accepted TSK-0315 dual-mode end-to-end service blueprint;
3. current accepted TSK-0325 parent journey/touchpoint blueprint;
4. current accepted TSK-0312 parent authentication/account/session/minimal-intake requirements;
5. current accepted TSK-0142 lightweight dashboard/device-management requirements;
6. TSK-0229 accountless/persistent-domain separation and current technical/evidence-state contracts;
7. still-compatible public/setup structure from historical TSK-0328 v1.0.0;
8. this artifact for current route, screen and navigation ownership.

This IA does not approve provider architecture, persistent schema/storage, authentication implementation, implementation/build, legal/privacy compliance, publication, launch, behavioral validation or any gate PASS.

## 2. Binding architecture rules

1. **Core value is accountless:** the full start → configure → verify → understand → troubleshoot/recover/remove path is navigable without login.
2. **Account continuity is optional:** Sign in / Dashboard is a separate continuity branch and never a prerequisite for Start setup or technical protection value.
3. **Three connected experience systems:** public information, accountless operational setup, and optional authenticated continuity/dashboard.
4. **No automatic anonymous-to-account stitching:** entering/signing into an account does not import, promote, join or extend J0/J1 automatically.
5. **Technical verification stays technical:** account/device presence, ownership, dashboard state and historical status never create `Verified`.
6. **Lifecycle actions remain distinct:** logout, revoke/unlink, dashboard-record deletion, account deletion, J0/J1 deletion and physical DNS removal are separate operations.
7. **No unnecessary gates:** identity, payment, marketing, survey or account screens are never inserted into the signed-out core path.
8. **No surveillance/admin expansion:** no browsing/query/activity history, child account/profile, raw AdGuard administration or broad per-domain control is introduced.
9. **Every screen/action has necessity:** every logical screen below maps to a user goal and current requirement trace under REQ-0028.
10. **Language is not market authority:** English/Turkish/Arabic+RTL capability does not imply official non-UK market/legal/support readiness.

## 3. Experience-system model

UseSafeWeb has exactly three connected experience systems in current Version 1.

### A. Public information system

Purpose: discover, understand, trust, decide and start. It explains proposition, limits, compatibility, privacy and help. It never creates protection state.

### B. Accountless operational setup system

Purpose: start, route, configure, verify, understand, troubleshoot, recover, remove and reset/reconfigure. It is the complete core product journey and remains usable signed out.

### C. Optional authenticated continuity system

Purpose: optional Google sign-in/session continuity, dashboard/device list, bounded device management and account lifecycle. It adds continuity only; it cannot replace technical setup/verification truth.

Primary handoffs:

- `Public → Start setup → accountless setup shell`
- `Public → Sign in → optional account/session → Dashboard`
- `Protection Map / explicit continuity choice → Sign in → Dashboard`
- `Dashboard → Add/continue/reverify/reinstall/remove → appropriate supported setup/management flow`

No handoff automatically migrates J0/J1 into persistent account/device state.

## 4. Global navigation model

### 4.1 Public primary navigation

- **Home**
- **How it works**
- **Compatibility & limits**
- **Privacy**
- **Help**
- **Start setup** — primary action

Optional account access is secondary:

- signed out: **Sign in**
- signed in: **Dashboard** and **Account**

`Start setup` remains available regardless of sign-in state. Sign in is never visually or structurally placed as a required predecessor to Start setup.

### 4.2 Setup-shell navigation

The setup shell is task-driven and does not show the full public navigation. Contextual utilities only:

- Help
- Limitations
- Exit
- Start over / reset when meaningful
- Remove UseSafeWeb DNS when applicable
- Optional **Save/manage with account** only at a justified continuity point; it is never the primary next action required to finish the core.

A progress indicator may communicate position but shall not become unrestricted navigation that bypasses required routing, configuration or verification preconditions.

### 4.3 Dashboard navigation

The authenticated continuity system remains deliberately small:

- **Devices** — list/empty state
- **Add device**
- **Account**
- **Help**
- **Start new setup** — routes to the same core setup capability without implying a device is already protected

No History, Activity, Queries, Child profiles, Admin, Integrations marketplace, broad Filter controls or safety-score section exists.

## 5. Route-family model

Exact implementation routing remains downstream, but the IA owns these semantic route families:

| Route family | Purpose | State/data rule | Index intent |
| --- | --- | --- | --- |
| `/` + public informational routes | Public discovery/explanation/help | No product/protection state required | Index only after publication authority. |
| `/setup` | Accountless operational shell | Transient current journey state; no identity required | Noindex/operational. |
| `/account` | Optional sign-in/session/account-lifecycle shell | Auth/account state only; provider/session secrets never user-visible | Noindex/private. |
| `/dashboard` | Optional authenticated device continuity shell | Authorized parent-owned records only | Noindex/private. |

Implementation may use internal child routes or state identifiers, but:

- session/token values shall never appear in user-visible URLs;
- child identity shall never be required in routes;
- public URLs shall not expose device/protection/error facts;
- any dashboard record identifier used in a private route must be opaque and independently authorized by downstream architecture; the IA does not require a persistent device identifier in the URL.

## 6. Public route inventory

| ID | Route intent | User goal | Primary next action | Required trace |
| --- | --- | --- | --- | --- |
| `PUB-HOME` | `/` | Decide whether UseSafeWeb is relevant and understand the bounded first-phone proposition. | Start setup; secondary How/Compatibility/Privacy/Help/Sign in. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 |
| `PUB-HOW` | `/how-it-works` | Understand Phone / Internet / Services and truthful Protection Map concepts. | Start setup; Compatibility. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 |
| `PUB-COMPAT` | `/compatibility` | Understand current supported/unsupported boundaries before or during setup. | Start setup when supported; Help otherwise. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `PUB-PRIVACY` | `/privacy` | Understand accountless-first, minimum-account and non-surveillance boundaries. | Start setup; return. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 |
| `PUB-HELP` | `/help` | Find stable self-service setup/account/recovery guidance without exposing private journey data. | Relevant help branch; Start setup; Sign in when the problem is account-only. | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 |
| `PUB-NOTICES` | controlled required-notices slot | Read actually approved required notices when they exist. | Return to origin. | REQ-0028; CON-0017; owning legal/privacy control |

Public duplication controls:

- Home summarizes; How it works owns conceptual explanation.
- Compatibility owns descriptive support/limit truth.
- Privacy owns privacy/non-surveillance detail.
- Help links to owning technical/account sources rather than duplicating them.
- Public content never creates `Verified`, setup completion or account authorization.

## 7. Logical screen inventory — accountless core

Logical screens may be visually combined only when doing so reduces friction without hiding state, weakening evidence, changing requirement ownership or bypassing a required transition.

| Screen ID | Logical screen | User goal | TSK-0325 touchpoint | Required trace | Main exits |
| --- | --- | --- | --- | --- | --- |
| `SCR-START` | Setup start/router | Begin intentionally and select a supported platform/path. | TP-01 + TP-02 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Native safeguard; Not covered; Help; Exit. |
| `SCR-NATIVE` | Native safeguard | Set/confirm the applicable native safeguard without confusing parent confirmation with system verification. | TP-03 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | DNS setup; Not covered/uncertain; Help; Exit. |
| `SCR-DNS-SETUP` | UseSafeWeb DNS setup | Perform the exact current supported encrypted-DNS action. | TP-04 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Verify; Help; Remove when applicable; Exit. |
| `SCR-VERIFY` | DNS verification | Learn what current technical evidence says about UseSafeWeb DNS. | TP-05 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Service/Map; Action needed; Uncertain; Not covered; Help; Remove. |
| `SCR-SERVICE` | Relevant service safeguard | Configure or skip zero/one approved relevant service without inventing another service. | TP-06 | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 | Protection Map; Help. |
| `SCR-MAP` | Protection Map | Review Phone / Internet / Services evidence and limits independently. | TP-07 | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 | Fix item; Help; Remove; Exit; optional account entry. |
| `SCR-TROUBLESHOOT` | Action-needed troubleshooting | Apply one known evidence-backed corrective action. | TP-12 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Recheck after changed condition; Remove/recovery; Help; Exit. |
| `SCR-NOT-COVERED` | Unsupported/not covered | Understand that current scope is unsupported and stop optimistic progression. | TP-02 + TP-16 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Compatibility; Help; Start over; Exit. |
| `SCR-UNCERTAIN` | Status uncertain | Understand what cannot currently be established and the next safe check when one exists. | TP-05 + TP-12 + TP-16 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Help; recheck after changed condition; Remove; Exit. |
| `SCR-FALSE-POSITIVE` | Legitimate-content blocked help | Resolve/report an apparent false positive without inventing broad bypass controls. | TP-12 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Return; narrow approved correction; Remove/recovery; Exit. |
| `SCR-HELP` | Contextual help | Get source-current self-service guidance without changing protection state. | TP-16 | REQ-0028; REQ-0029 where technical; CON-0010; CON-0017; INT-0009; INT-0010 | Return to prior screen; Limitations; applicable recovery; Exit. |
| `SCR-LIMITS` | Contextual limitations | Understand current support/evidence boundary without changing journey state. | TP-16 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Return; public Compatibility; Help; Exit. |
| `SCR-REMOVE` | Remove UseSafeWeb DNS | Remove the exact configured UseSafeWeb DNS mechanism and withdraw the active DNS claim. | TP-13 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Recovery check; Help. |
| `SCR-RECOVERY` | Post-removal recovery | Confirm ordinary connectivity after removal without presenting that as UseSafeWeb protection. | TP-14 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | Start over; Help; Exit. |
| `SCR-RESET-LOST` | Reset/reconfigure/lost transient state | Return to a clean routing state when current transient state is unavailable or intentionally reset. | TP-15 | REQ-0028; REQ-0029; CON-0010; CON-0017; INT-0009; INT-0010 | `SCR-START`. |

No standalone completion screen is mandatory. `SCR-MAP` is the truthful core end-of-journey review; the parent can exit without creating an account.

## 8. Logical screen inventory — optional account and dashboard

| Screen ID | Logical screen | User goal | TSK-0325 touchpoint | Required trace | Main exits |
| --- | --- | --- | --- | --- | --- |
| `ACC-ENTRY` | Optional account entry | Understand the bounded continuity benefit and choose Sign in or continue signed out. | TP-08 | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 | Sign in; return/continue accountless. |
| `ACC-SIGNIN` | Google sign-in initiation/pending | Start the planned account route and reach a known signed-in/signed-out outcome. | TP-09 | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 | Dashboard on success; accountless return on cancel; error/retry. |
| `ACC-ERROR` | Sign-in/provider/account error | Understand a factual account-only failure without changing DNS/core truth. | TP-09 + TP-16 | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 | Retry; Help; Start setup; return signed out. |
| `ACC-REAUTH` | Session expired/revoked/re-authentication | Restore authorized account access without creating a duplicate account or blocking core value. | TP-09 | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 | Re-authenticate; Dashboard; Start setup; signed-out Help. |
| `DASH-HOME` | Dashboard empty/list | Identify explicitly managed device records and the strongest truthful status/next action. | TP-10 | REQ-0028; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 | Add device; device detail; Account; Help; Start new setup. |
| `DASH-ADD` | Add device | Explicitly start management/setup for a supported device without silent J0/J1 import. | TP-11 | REQ-0028; REQ-0029; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 | Fresh supported setup/device flow; cancel to Dashboard. |
| `DASH-DEVICE` | Device detail / Protection Map | Understand one managed record, current/last-known evidence and the next bounded action. | TP-10 + TP-11 | REQ-0028; REQ-0029; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 | Verify; continue/reinstall; manage; Help; physical removal flow. |
| `DASH-MANAGE` | Bounded device management | Rename, continue, reverify, reinstall/reconfigure, replace or revoke/unlink within approved scope. | TP-11 + TP-17 | REQ-0028; REQ-0029; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 | Device detail; setup/verify; unlink status; record-delete confirmation. |
| `DASH-RECORD-DELETE` | Delete dashboard record | Delete only the governed dashboard record and understand that physical DNS is separate. | TP-17 | REQ-0028; CON-0010; CON-0017; TSK-0142; INT-0009; INT-0010 | Confirm/cancel; Dashboard; optional physical removal separately. |
| `ACC-ACCOUNT` | Account/session settings | Understand account status and perform logout or enter account deletion. | TP-17 | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 | Logout; deletion entry; Dashboard; Help. |
| `ACC-DELETE` | Account deletion confirmation/status | Explicitly request account deletion and see pending/success/error truth without a DNS-removal claim. | TP-17 | REQ-0028; CON-0010; CON-0017; TSK-0312; TSK-0142; INT-0009; INT-0010 | Confirm/cancel; signed-out state after completion; Help/recovery on pending/error. |

## 9. Canonical normal paths

### 9.1 Signed-out accountless core

`PUB-HOME / other public page → Start setup → SCR-START → SCR-NATIVE → SCR-DNS-SETUP → SCR-VERIFY → [SCR-SERVICE when applicable] → SCR-MAP → Exit`

Rules:

- zero external services is valid;
- no Sign in, Account, Dashboard, payment or marketing screen is required;
- already-configured branches may skip duplicate configuration only when technical truth still routes through appropriate verification;
- `Verified` appears only from qualifying current technical evidence.

### 9.2 Optional continuity after core value

`SCR-MAP → ACC-ENTRY → ACC-SIGNIN → DASH-HOME`

The parent may instead choose `Exit` or continue signed out. Sign-in cancellation/error returns safely without invalidating completed accountless value.

### 9.3 Returning signed-in parent

`Public Sign in or valid account session → DASH-HOME → DASH-DEVICE → current bounded action`

A stored device record can route to setup/verification but cannot skip technical verification or manufacture current protection evidence.

### 9.4 Signed-in parent starts new setup

`DASH-HOME → Start new setup / DASH-ADD → current supported setup route`

A fresh flow does not inherit `Verified`, S2, J0/J1 state or another device's status automatically.

## 10. Exception-path navigation

### Already configured

`SCR-START → SCR-NATIVE [skip duplicate setting when truthful] → [skip duplicate DNS configuration only when safe] → SCR-VERIFY → SCR-MAP`

Dashboard/account presence does not bypass `SCR-VERIFY`.

### Unsupported / not covered

`SCR-START or later applicability check → SCR-NOT-COVERED → Compatibility / Help / Start over / Exit`

Signed-in users receive the same technical truth; account ownership never converts unsupported scope to supported.

### Failed activation / verification

`SCR-VERIFY → SCR-TROUBLESHOOT or SCR-UNCERTAIN → changed condition → SCR-VERIFY`

If rollback/removal is needed:

`SCR-TROUBLESHOOT / SCR-UNCERTAIN → SCR-REMOVE → SCR-RECOVERY`

No unchanged-condition retry loop is introduced.

### False positive

`SCR-MAP / DASH-DEVICE / Help → SCR-FALSE-POSITIVE → narrow approved correction + truthful recheck`

or, where removal is the safe recovery:

`SCR-FALSE-POSITIVE → SCR-REMOVE → SCR-RECOVERY`

No broad dashboard allow/block administration is invented.

### Account sign-in cancellation/error/provider outage

`ACC-SIGNIN → ACC-ERROR or signed-out return → Start setup / Help / retry later`

Account-only failure never changes configured DNS truth and never blocks the signed-out core.

### Session expiry/revocation

`Dashboard/account-only action → ACC-REAUTH → re-authenticate or continue signed out`

Account-only actions fail closed; accountless setup/help/removal remains reachable.

### Lost accountless state / resume

- truthful current transient state may resume;
- lost/expired J0/J1 routes to `SCR-RESET-LOST` and re-establishes current evidence;
- signing in cannot extend anonymous expiry or silently import anonymous state.

### Physical removal

`SCR-MAP / DASH-DEVICE / troubleshooting / Help → SCR-REMOVE → SCR-RECOVERY`

Dashboard record/account lifecycle remains separate.

### Dashboard record deletion

`DASH-DEVICE / DASH-MANAGE → DASH-RECORD-DELETE → Dashboard`

The result says only what happened to the record. It does not claim physical DNS removal.

### Revoke/unlink

`DASH-MANAGE → revoke/unlink action → truthful success/pending/error → Dashboard/device state`

It ends account management association only unless the separately owned physical removal flow is also performed and verified.

### Account deletion

`ACC-ACCOUNT → ACC-DELETE → truthful pending/success/error`

Account deletion does not claim J0/J1 deletion or physical DNS removal.

## 11. Navigation/back/refresh rules

### Public

- normal browser navigation is allowed between public informational pages;
- public navigation carries no protection or private device state;
- Start setup is the primary public-to-operational transition;
- Sign in is always optional relative to core value.

### Accountless setup

- primary task action advances only through a valid state transition;
- Help/Limitations are state-neutral utility detours;
- Back/return-from-OS never upgrades evidence;
- if current transient state is lost, route to `SCR-RESET-LOST` rather than fabricating persistent resume;
- Start over resets web journey state only; it does not remove DNS.

### Account/dashboard

- account-only screens require a valid authorized account/session under downstream implementation;
- session expiry/revocation routes to `ACC-REAUTH`, not to a false device/protection failure;
- Dashboard Back returns to the prior authorized account surface or device list without mutating protection state;
- a current contradictory verifier result overrides historical optimistic dashboard status;
- logout ends session access only.

## 12. Lifecycle-separation contract

The IA shall keep the following as separately named and separately navigated outcomes:

| Operation | What it changes | What it must not claim |
| --- | --- | --- |
| Logout | Authenticated session access | Account deletion, device-record deletion, J0/J1 deletion or DNS removal. |
| Revoke/unlink | Dashboard management association | Physical DNS removal or account deletion. |
| Delete dashboard record | Persistent dashboard record under downstream data contract | Physical DNS removal or anonymous-state deletion. |
| Delete account | Account/session/device-ownership data under downstream contract | Physical DNS removal or automatic J0/J1 deletion. |
| J0/J1 expiry/deletion | Anonymous journey state | Account/device deletion or DNS removal. |
| Remove UseSafeWeb DNS | Physical device DNS configuration / active DNS claim | Dashboard/account deletion. |

No combined button/route may claim multiple operations completed unless the owning downstream workflows actually perform and verify each operation independently.

## 13. Protection-evidence and state rules

- account/device ownership, record existence, valid session or prior setup never directly establishes `Verified`;
- parent confirmation remains parent-confirmed at most where allowed;
- current qualifying technical verifier success may establish `Verified` only for the supported mechanism/context;
- known repairable failure → `Action needed`;
- unsupported → `Not covered`;
- inconclusive/conflicting/stale → `Status uncertain`;
- physical removal → `Removed` only with owning evidence/confirmation;
- one Phone/Internet/Services layer never upgrades another;
- Help, Sign in, Dashboard navigation, logout and account lifecycle actions are protection-state neutral unless they explicitly route to an owning technical setup/removal/verification action.

## 14. Necessity and duplication controls

Every interaction must satisfy REQ-0028. Specifically:

- public Sign in exists only to enter optional continuity;
- ACC-ENTRY exists only to explain the optional continuity choice and preserve a clear signed-out exit;
- dashboard exists only for device identification, truthful status/next action and bounded lifecycle management;
- device nickname is optional parent convenience and never requires child identity;
- account/device screens do not duplicate technical instructions; they route to the owning current setup/verification/removal content;
- no route exists solely for analytics, SEO, onboarding ceremony, newsletter capture, waitlist, demographic intake or marketing conversion;
- no duplicate Compatibility, Privacy, Protection Map or technical support matrix is maintained inside Dashboard.

## 15. Accessibility, responsive and localization inheritance

All public, setup, account and dashboard screens inherit the project WCAG 2.2 AA target, responsive mobile-first behavior and English/Turkish/Arabic+RTL technical capability.

- status meaning cannot depend on color alone;
- account errors, session expiry, destructive confirmations, pending/unknown states and recovery controls require accessible labels/focus/error association in downstream interaction specs;
- navigation order and directional icons must remain correct in RTL;
- translation shall preserve evidence strength and optional-account meaning;
- language availability does not imply official non-UK market/legal/support activation.

No real-user comprehension/usability claim is made by this L4 IA.

## 16. Minimum deterministic/synthetic IA acceptance cases

| Test ID | Scenario | Expected IA result |
| --- | --- | --- |
| `IA-T01` | Signed-out parent completes core | A complete route reaches `SCR-MAP` and Exit without Sign in/Dashboard. |
| `IA-T02` | Public signed-out navigation | Start setup is primary; Sign in is optional/secondary and cannot gate setup. |
| `IA-T03` | Parent chooses continuity after core | `SCR-MAP → ACC-ENTRY → ACC-SIGNIN → DASH-HOME`; decline/cancel preserves completed core. |
| `IA-T04` | Provider cancel/error/outage | Account-only error/retry is shown; Start setup/Help/accountless continuation remains reachable and DNS truth is unchanged. |
| `IA-T05` | Returning parent with valid session | Dashboard list/empty state is reachable; record presence is not technical verification. |
| `IA-T06` | Expired/revoked session | Account-only action routes to `ACC-REAUTH`; signed-out core/help remains available. |
| `IA-T07` | Empty dashboard | `DASH-HOME` offers Add device and explains optional continuity without inventing history/profile content. |
| `IA-T08` | Managed device detail | `DASH-DEVICE` shows truthful current/last-known status and routes to bounded actions only. |
| `IA-T09` | Add device while J0/J1 exists | Flow requires explicit Add device; no automatic anonymous-state promotion/linkage is navigated or implied. |
| `IA-T10` | Dashboard device needs verification | Route goes to owning verification flow; dashboard ownership cannot skip or replace technical verification. |
| `IA-T11` | Unsupported/failure/false-positive | Distinct Not covered, Action needed/uncertain and false-positive routes remain reachable with truthful recovery. |
| `IA-T12` | Physical DNS removal | `SCR-REMOVE → SCR-RECOVERY`; dashboard/account records are not claimed deleted. |
| `IA-T13` | Delete dashboard record only | `DASH-RECORD-DELETE` completes only record lifecycle; no DNS-removal claim. |
| `IA-T14` | Revoke/unlink only | Management association ends/changes only; no DNS-removal or account-deletion claim. |
| `IA-T15` | Account deletion | `ACC-DELETE` distinguishes account deletion from J0/J1 deletion and physical DNS removal. |
| `IA-T16` | Logout | Session access ends only; configured DNS and records are not falsely reported removed/deleted. |
| `IA-T17` | Privacy/scope audit | No browsing/query/activity history, child profile/account, raw AdGuard admin or broad per-domain control route exists. |
| `IA-T18` | Locale/accessibility audit | Public/setup/account/dashboard logical screens are localizable to English/Turkish/Arabic+RTL and retain accessible navigation/state semantics without inferring market readiness. |

## 17. Current ACC-0328 coverage

ACC-0328 requires architecture that supports normal and exception paths for the accountless core plus optional account sign-in/return/dashboard/account lifecycle, avoids unnecessary gated steps, keeps login optional for core value, and maps each screen to a user goal and requirement.

This v2 artifact provides:

- the complete signed-out normal path and all current TSK-0325 exception/recovery paths;
- optional account entry, sign-in, provider/error, re-authentication, dashboard list/empty, device detail/management, record deletion, account settings and account deletion architecture;
- explicit provider-outage/account-error continuation to accountless core;
- an explicit no-gate rule and no identity/payment/marketing predecessor for core setup;
- screen-by-screen user goals, touchpoint ownership and requirement/interface traces;
- lifecycle separation and truthful technical-evidence boundaries;
- privacy, accessibility, mobile and RTL scope fences.

**Candidate disposition:** ACC-0328 is ready for independent post-publication verification. TSK-0328 remains non-PASS until the exact persisted artifact and structured acceptance projection are independently verified and the result is durably reconciled into `CURRENT_STATE.md`.
