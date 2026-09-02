# TSK-0308 — Dual-Mode Design-System Addendum

**Version:** 2.0.1-post-CR0008-copy-refresh  
**Date:** 2026-09-02 UTC  
**Task:** TSK-0308 — Create the shared responsive design system for public and product surfaces  
**Status:** current revalidation addendum; acceptance remains subject to independent VER-0308 and runtime reconciliation.

## 1. Purpose and preservation

This addendum preserves the owner-approved 2026-08-29 TSK-0308 candidate as immutable provenance and retains DS-01 through DS-13, `candidate.css`, the six evidence-state semantics, responsive/accessibility/localization rules, TSK-0300 token/primitive ownership and the SafeWeb identity.

It changes only the historical scope clauses that conflict with current `DEC-0053 / CR-0006`: optional parent account/session/lightweight dashboard/device management is now Version-1 scope while the complete core safety journey must remain usable without login.

The following historical clauses are superseded for current acceptance:

- blanket exclusion of Login / Account / Dashboard / Profile components;
- public navigation being permanently limited to the former six accountless-only intents;
- setup being prohibited from exposing any persistent account navigation;
- the statement that the current journey has no justified account field or account interaction;
- the statement that setup can never add a signup/account step.

They are replaced by the bounded dual-mode rules below. No historical file is rewritten.

## 2. Frozen invariants

1. **Accountless core remains complete.** Start setup, configuration, verification, Protection Map, troubleshooting, recovery and removal remain available without login.
2. **Account use is optional and non-coercive.** Sign-in/manage-devices entry may be available but cannot be a prerequisite for core value.
3. **Identity is not protection evidence.** Signed-in/session/device-ownership state never creates the technical `protected/verified` state or its primary user-facing copy `Protection verified`; only qualifying technical evidence may do so.
4. **No surveillance expansion.** No browsing/query/activity history, child account/profile, raw DNS administration, query log, arbitrary diagnostics or overall safety score is introduced.
5. **Lifecycle operations stay distinct.** Logout, session revocation, device unlink/revoke, dashboard-device-record deletion, account deletion, anonymous-state reset and physical SafeWeb DNS removal are separate operations with separate truthful outcomes.
6. **Provider/datastore failure preserves accountless continuation.** Auth/session/dashboard failure must expose a safe `Continue without signing in` / accountless route where the core journey is otherwise available.
7. **One token/primitive authority.** TSK-0300 `tokens.css` and `components.css` remain the sole shared token/primitive sources. This addendum introduces composition classes only and no palette/font/logo/token fork.
8. **SafeWeb identity remains owner-approved and unchanged.** `UseSafeWeb.com` remains the domain; `SafeWeb` remains parent-facing brand copy.

## 3. Current navigation rule

Public and product systems remain distinct but connected.

### Public

The existing public intents remain valid. A bounded optional account entry may additionally expose **Sign in / Manage devices**. It must be visually secondary to `Start setup`, must not imply that an account is required, and must not change public pages into an admin dashboard.

### Setup/product

Accountless setup remains task-first. An authenticated parent may additionally enter the lightweight dashboard/device-management area. Account chrome is not injected into every setup screen; account utilities appear only when relevant to the selected account route.

## 4. Additional current component patterns

### DS-14 — `OptionalAccountEntry`

**Purpose:** expose optional sign-in/manage-devices access without gating accountless setup.  
**Semantic base:** action group with explicit `Start setup` and secondary `Sign in / Manage devices`.  
**Required truth:** text states that sign-in is optional for core setup.  
**Failure state:** provider/session failure keeps an accountless continuation available.  
**Prohibited:** forced modal, dark pattern, disabled core CTA, claim that account improves/verifies protection by itself.

### DS-15 — `SessionStatus`

**Purpose:** expose signed-in/signed-out/session-expired/provider-unavailable state.  
**Semantic base:** ordinary status region with explicit text; urgent alert only for an immediate destructive/security condition.  
**Required truth:** `Signed in` describes session state only and never becomes a Protection Map state.  
**Actions:** sign out/retry/continue without sign-in as applicable.  
**Privacy:** no provider subject/token/session identifier is rendered in ordinary UI.

### DS-16 — `DeviceManagementList`

**Purpose:** show the minimum parent-owned device records needed for lightweight management.  
**Semantic base:** heading + list/cards + explicit per-device actions.  
**Each row:** parent-recognisable label if approved, lifecycle state, protection-verification state only when separately evidenced, and one bounded next action.  
**Required truth:** registered/owned/configured/`protected/verified` remain distinct facts; visible protection copy follows current TSK-0320/TSK-0300 semantics rather than historical labels.  
**Prohibited:** child profile/activity timeline, DNS query log, arbitrary AdGuard admin controls, overall safety score.

### DS-17 — `AccountLifecycleActions`

**Purpose:** present destructive/session/device/account operations without conflation.  
**Semantic base:** clearly labelled destructive/recovery section with separate controls.  
**Separate actions:** sign out, revoke/unlink device, delete dashboard device record, delete account, reset/delete anonymous web state, remove SafeWeb DNS.  
**Confirmation:** destructive confirmation describes exactly what will and will not change.  
**Post-action:** terminal state names the completed operation only; account deletion cannot claim physical DNS removal, and DNS removal cannot claim account deletion.

## 5. Responsive and localization requirements

- 320 px: one-column account entry, session status, device list and lifecycle actions; no page-level overflow.
- 768 px+: device rows may use bounded two-column metadata/action layout when DOM and reading order remain logical.
- 1024/1440 px+: dashboard may use restrained supporting columns, but never dense raw-admin/query-log chrome.
- EN/TR/AR+RTL: labels/actions wrap without clipping; device labels/content determine height; no fixed-width account strings; SafeWeb/domain/technical endpoints remain LTR-isolated where applicable.
- Logical CSS properties only for direction-sensitive spacing/alignment in the addendum layer.

## 6. Accessibility requirements

- native controls/links and explicit accessible names;
- logical heading/list structure for dashboard/device rows;
- visible focus inherited from TSK-0300 primitives;
- account/session state not conveyed by color alone;
- destructive controls are explicit and not adjacent ambiguous icon-only actions;
- provider/session errors expose text plus a safe next action;
- keyboard order follows DOM/reading order;
- 200% text resize and 320 px reflow without content/function loss;
- reduced-motion behavior remains inherited from the existing design system;
- RTL/LTR isolation remains deterministic.

## 7. Additive implementation artifacts

- `prototype/TSK-0308/dual-mode-addendum.css` — composition-only classes consuming existing `--sw-*` tokens.
- `prototype/TSK-0308/dual-mode-reference.html` — internal representative accountless + optional-account/session/dashboard/device-lifecycle surface for deterministic/browser verification.

These files do not replace the approved candidate artifacts and do not create a second design/token authority.

## 8. Acceptance relationship

For current TSK-0308 acceptance, the effective shared responsive design system is:

1. the historically approved TSK-0308 candidate for still-valid DS-01–DS-13 semantics;
2. this addendum for CR-0006 dual-mode scope reconciliation and current protection-state-copy binding;
3. current TSK-0300 shared tokens/primitives;
4. current TSK-0309 dual-mode experience baseline;
5. current TSK-0320 protection-state semantics for visible protection-state copy.

No identity reselection, token redesign, brand redesign or public deployment is performed by this addendum.
