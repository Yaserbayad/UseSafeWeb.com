# TSK-0316 — Dual-Mode Friction Budget and Interaction Challenge — Post-CR-0008

**Task:** TSK-0316 — Define a friction budget and challenge every click, field, choice, confirmation, account, and manual step  
**Acceptance / Verification / Evidence:** ACC-0316 / VER-0316 / EVD-0316  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-cr0008  
**Date:** 2026-09-02  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE  
**Current dependency:** TSK-0315 current dual-mode service blueprint PASS  
**Authority:** DEC-0053/CR-0006 dual-mode Version 1; DEC-0054/CR-0007 autonomy/production lifecycle; DEC-0055/CR-0008 proportional evidence/action-authority normalization; current TSK-0229 accountless separation; current TSK-0299 SafeWeb verbal system; current TSK-0320 protection-state semantics.

## 1. Supersession and objective

This artifact supersedes `TSK_0316_FRICTION_BUDGET_AND_INTERACTION_CHALLENGE_2026-08-28.md` for current acceptance where the historical contract assumed an accountless-only product and therefore could not challenge the now-approved optional parent-account/session/dashboard/device-management lifecycle.

The retained core rule remains:

> **An interaction earns a place only when a current user decision, platform action, truth/evidence requirement, bounded continuity choice, consequential lifecycle action, or recovery need cannot be satisfied safely with less user work. Otherwise its friction budget is zero.**

This is a design-minimisation contract, not a fabricated universal click-count, completion-time or conversion target. `RSK-0002` remains OPEN; no representative-parent usability preference/comprehension is inferred before the authorized L8 sequence.

## 2. Current product boundary the budget must preserve

1. **Complete accountless core:** discovery → setup → verification → Protection Map → troubleshooting/removal/recovery can complete without login.
2. **Optional account is bounded continuity:** sign-in/session/dashboard/device management is available only when the parent chooses it; it is never required for core value or stronger protection.
3. **No automatic J0/J1 linkage:** sign-in/account creation does not silently import, join, promote or extend anonymous journey state.
4. **Minimum persistence only:** optional account/device records contain only separately approved identity/session/ownership/settings/lifecycle/evidence metadata; no browsing/query/activity history.
5. **No child account/profile:** a minimum managed-device record is not a child identity or behavioral profile.
6. **Truthful evidence:** account ownership, dashboard presence, device registration, stored configuration and parent confirmation never substitute for qualifying current technical verification.
7. **Lifecycle operations stay distinct:** reset anonymous journey, logout, revoke/unlink management, delete device record, delete account, reinstall/reconfigure, and physically remove SafeWeb DNS are separate actions with separate consequences.
8. **Current visible brand:** parent-facing generic product copy uses `SafeWeb` / `SafeWeb DNS`; `UseSafeWeb.com` and `dns.usesafeweb.com` may appear only when they are actual technical identifiers.
9. **Provider failure is contained:** authentication-provider outage blocks account-only functions, not the configured DNS truth or accountless setup/help/removal path.
10. **No raw DNS administration:** no AdGuard credentials, broad `/control` proxy, query-log console, browsing history or unrestricted filter administration.

## 3. Friction budget classes

Every retained user interaction must map to one class below. A screen may contain multiple system outputs, but each required user action needs one current reason.

### B1 — Irreducible product decision

Use only where the service cannot safely select the user's intended branch.

Examples: Start; choose/confirm platform when ambiguous; choose optional account continuity; choose replace/remove/reset.

### B2 — Irreducible platform/security action

Use only where Android/Apple/service/provider security boundaries require explicit user action that SafeWeb cannot truthfully perform itself.

Examples: entering the exact approved Android Private DNS hostname, approving an Apple profile workflow, native safeguard action, provider sign-in/consent.

### B3 — Truth/evidence interaction

Use only where user input is genuinely required to distinguish parent-confirmed from technically verified state or to request a fresh check after a changed condition.

Parent confirmation can produce only the parent-confirmed state; it never manufactures technical verification.

### B4 — Conditional routing detail

Ask only when the answer changes supported instructions and cannot be reliably derived without privacy-invasive fingerprinting.

Examples: platform/version band, setup context, relevant service category.

### B5 — Optional continuity/account action

Use only after explicit parent choice to enter account continuity or when already authenticated and performing an account-only management action.

Examples: Sign in, open dashboard, add/manage an explicitly owned device record. This class never becomes mandatory in the accountless core.

### B6 — Consequential lifecycle/destructive action

Use when the parent intentionally changes/removes persisted ownership/session/data or device protection and the object/consequence must be unambiguous.

Examples: revoke/unlink, delete device record, delete account, physically remove SafeWeb DNS, replace device where old/new lifecycle changes.

### B7 — Recovery/help action

Use only after failure, uncertainty, user-invoked help, provider outage or repair/removal need.

Examples: Retry after changed condition, reinstall/reconfigure, issue-specific help, recovery check, exceptional escalation.

## 4. Zero-budget friction — prohibited by default

The current design has zero budget for:

- mandatory login/sign-up/account creation before or after core value;
- forcing the optional-account branch before the parent can finish/exit accountless;
- identity/contact collection merely to start or complete core setup;
- local password/SMS account expansion where the current product requires the planned provider route only;
- a child account/profile or mandatory child name/age/school/location;
- collecting browsing/query/activity history, visited domains, app history or real browsing examples to prove protection;
- creating a persistent device record silently from J0/J1 or sign-in alone;
- automatically importing/promoting/linking/extending J0/J1 on account entry;
- marketing newsletter, push/engagement, rating/review/referral or generic survey prompts in setup;
- forced onboarding carousels or a mandatory standalone trust screen when point-of-need content is sufficient;
- repeated confirmations of known state;
- asking a user to choose DoH versus DoT when the supported platform path determines the mechanism;
- a universal DNS hostname/URL field that erases platform differences;
- mandatory Protection Map acknowledgement or `I understand` checkbox without an owning requirement;
- an extra Finish click when no current technical/legal consequence requires it;
- confirmation dialogs for ordinary reversible navigation;
- duplicate provider sign-in after a valid session is already known;
- dashboard/device-management steps for a parent who chose accountless completion;
- adding device nickname/metadata fields unless the current account use case needs them;
- treating managed-device record ownership as protection verification;
- unrestricted free-text support or broad DNS-admin fields by default;
- retry loops without changed conditions/new evidence;
- forcing unsupported/uncertain paths through more steps to resemble success.

## 5. Interaction-by-interaction challenge against current TSK-0315

| TSK-0315 stage / interaction | Current disposition | Budget | Current reason and minimized rule |
| --- | --- | --- | --- |
| 0 Discover / trust | **System content; one Start action retained** | B1 | Public information is not operational state. One primary Start; no login/payment gate or forced trust carousel. |
| 1 Start core | **Retain Start only** | B1 | Explicitly enters setup/J0. Do not ask identity/contact. |
| 2 Minimal route | **Auto where reliable; ask only ambiguity-changing facts** | B4 | Platform/support differences can change instructions. No fingerprinting or universal version questionnaire. |
| 3 Native safeguard | **Retain only when applicable** | B2/B3 | Platform action may be required; one parent confirmation only where no verifier exists, yielding parent-confirmed state rather than verified. |
| 4 DNS configure | **Retain unavoidable platform action** | B2 | Route directly to the approved platform mechanism; do not ask protocol knowledge. Exact technical identifiers may be shown literally. |
| 5 DNS verify | **Automate when possible; otherwise one Check/Recheck** | B3 | Required to prevent configuration presence/confirmation from masquerading as protection. Retry only after changed condition/new evidence. |
| 6 Relevant service | **Conditionalize to zero/one approved relevant safeguard** | B4/B2/B3 | No service catalogue. Ask only the minimum applicability fact; skip/not-covered when none applies. |
| 7 Protection Map | **Render automatically; no acknowledgement click** | System output | Evidence/gaps must be visible but require no ceremonial confirmation. |
| 8 Core finish / optional continuity choice | **Accountless Finish/Exit always first-class; optional account choice explicit** | B1/B5 | Core completion cannot depend on account choice. `Continue without account` / `Finish without account` stays visible and functional. |
| 9 Optional account entry | **Only on explicit parent choice** | B5/B2 | One Sign in/Save-manage action may start the planned provider flow. Cancel/error/outage returns safely to accountless core; no J0/J1 import. |
| 10 First-session account creation | **Provider-driven only after successful chosen sign-in** | B5 | Do not add local password/SMS or duplicate profile questions. Resolve ambiguous/duplicate account state before retry. |
| 11 Signed-in return/session | **Auto-use valid session; prompt re-auth only when needed** | B5 | Do not ask sign-in when current valid session proves identity. Invalid/revoked session fails closed for account-only actions while accountless remains available. |
| 12 Dashboard empty/list | **System output after authenticated entry** | System output | Show only authorized parent-owned records. No mandatory dashboard visit after accountless core. |
| 13 Add/manage device | **Explicit account-only action; minimize fields** | B5/B4 | Create/manage a record only on deliberate choice. No silent J0/J1 transfer; nickname/generic label only if needed. |
| 14 Reverify/reinstall/reconfigure | **Contextual, not default path** | B3/B7 | Trigger only when currentness/repair is needed. Do not preserve stale positive state. |
| 15 Replace device | **Explicit lifecycle branch** | B6 | New device does not inherit protection/history automatically. Explain old/new record consequence once. |
| 16 Revoke/unlink management | **Explicit consequential action** | B6 | Ends account-management association only. Do not imply DNS removal. Confirmation only if needed to prevent mistaken target/action. |
| 17 Delete dashboard device record | **Explicit destructive data action** | B6 | Deletes the managed record under owning contract only. Physical DNS remains separate. One clear consequence/target confirmation; no repeated dialogs. |
| 18 Account logout | **Single action; no DNS warning theatre** | B6 | Ends authenticated session only. Accountless core remains available and configured DNS truth is unchanged. |
| 19 Account deletion | **Explicit high-consequence action with clear object/consequence** | B6 | Governed account/device-data deletion only; separate from J0/J1 and physical DNS. Require only confirmation actually needed to avoid accidental irreversible deletion. |
| 20 False positive / ordinary help | **On demand / issue-specific** | B7 | Keep off happy path. Request minimum reproducible/synthetic issue facts; no browsing history by default. |
| 21 Remove SafeWeb DNS | **Explicit on-demand platform action** | B6/B2 | Use platform-specific removal. Parent-facing generic CTA is `Remove SafeWeb DNS`; exact technical identifiers remain literal where necessary. |
| 22 Post-removal recovery | **Automate neutral/synthetic check where possible** | B7/system | No mandatory browsing task. Ask user only when automation cannot conclude. |
| 23 Provider outage | **No compensating identity friction** | B7/system | Explain account-only limitation, keep accountless setup/verification/help/removal usable, offer later retry only. |
| 24 Exit / reset / lost state | **Exit zero-friction; reset contextual** | Zero/B6/B7 | Exit never trapped. Reset affects anonymous journey only and must not claim DNS/account deletion. Lost state routes to verify/remove rather than identity collection. |

## 6. Resulting minimum accountless path

This is a logical interaction budget, not a promised fixed click count:

1. Parent reads concise proposition/limits and selects **Start setup**.
2. Locale/platform context is derived where safe; parent is asked only when ambiguity changes routing.
3. Applicable native safeguard instruction appears; parent performs an unavoidable platform action and confirms only where no system verifier exists.
4. SafeWeb routes directly to the approved platform-specific DNS setup; parent completes the OS-required action.
5. Verification runs automatically where possible; otherwise one deliberate Check/Recheck is shown.
6. Zero/one relevant approved service safeguard appears only if applicable.
7. Protection Map renders with evidence-matched states.
8. Parent can **Finish without account / Exit** with no account branch required.

Help, retry, reset, reinstall and removal remain conditional, not happy-path friction.

## 7. Optional continuity path budget

Only a parent who chooses continuity enters this branch:

`Choose account continuity → provider sign-in if no valid session → account/session result → dashboard → [optional explicit device-management action]`

Rules:

- one explicit account choice; never preselect or force it as the only completion route;
- no duplicate email/name/password/SMS fields when the approved provider result supplies the necessary account identity;
- no implicit transfer of J0/J1 into persistent account/device state;
- no automatic managed-device record solely because sign-in succeeded;
- valid session suppresses redundant sign-in;
- dashboard list/empty is output, not a form step;
- device metadata fields exist only where current ownership/management use needs them;
- provider outage/cancel returns to the accountless core rather than demanding another identity route;
- stored device/dashboard presence never changes a technical protection state without qualifying evidence.

## 8. Field/data friction budget

### Accountless core

Default required identity/contact fields: **zero**.

Ask only a routing/support field that changes current instructions and cannot be safely derived. The TSK-0229 allowlist is an upper bound, not a form template.

### Optional account

The provider/auth and later persistent data contracts own the exact fields. This task permits only minimum fields necessary for:

- account/session identity/lifecycle;
- parent-owned managed-device identification/ownership;
- minimal nickname/generic label where it materially helps distinguish records;
- supported routing/settings/lifecycle/evidence metadata explicitly authorized downstream.

This task prohibits adding fields merely for analytics, marketing, personalization, engagement, future use or perceived completeness.

### Explicitly no-budget data

- child account/profile identity;
- exact DOB/child age unless a later owning requirement proves it necessary (none is established here);
- school/location;
- service usernames/passwords;
- device serial/fingerprint solely for convenience;
- browsing/query/activity history;
- raw unrestricted diagnostics;
- raw AdGuard administrative credentials/control fields.

## 9. Confirmation budget

A confirmation is retained only when it changes truth or prevents a meaningful consequence.

**May be required once:**

- parent-confirmed safeguard where no verifier exists;
- deleting an account/device record where the destructive target/consequence must be explicit;
- revoke/unlink/replace/reset/removal where the user must distinguish the object being changed;
- exceptional security/privacy/legal action owned elsewhere.

**Zero budget:**

- `I understand` after ordinary instructions;
- repeated `Done?` after a verifier can determine state;
- `Are you sure?` for ordinary reversible navigation;
- account/dashboard confirmations used only for funnel analytics;
- confirmation that implies a stronger protection state than its evidence supports.

## 10. Platform and one-click truth constraints

The friction budget cannot optimize away platform/security actions that current accepted technical contracts require.

- Android Private DNS uses the current approved provider-hostname path; the exact current technical hostname may be shown literally as `dns.usesafeweb.com` when needed. Do not claim a web page silently changes the OS setting.
- Apple encrypted-DNS/profile installation retains the OS/profile authorization boundary. Do not claim silent universal installation or treat profile presence as protection verification.
- VPN/browser/app/network conflicts or unsupported states must stop optimistic progression when they prevent reliable verification.
- Authentication-provider consent/sign-in is an external security boundary; account continuity must not invent a password/SMS bypass to reduce friction.

Allowed outcome-specific labels include `Start setup`, `Sign in` when optional continuity is chosen, `Copy DNS hostname`, `Check protection`, and `Remove SafeWeb DNS`.

Prohibited unsupported claims include `Protect in one click`, `Turn on SafeWeb automatically` where OS action remains, `Works on every Android/iPhone`, `Install and forget`, and `Fully protected`.

## 11. Retry and ambiguous-effect policy

- Automatic/read-only checks may retry only under their owning safe/idempotent policy.
- User-facing retry is shown only after a changed condition, transient failure or new evidence can matter.
- Ambiguous account creation, unlink, delete, replacement or removal results must be reconciled to known state before replay; never blind-retry a potentially duplicated/destructive effect.
- Repeated equivalent failure exits to truthful error/help rather than looping.

## 12. Deterministic ACC-0316 assertions

A later IA/prototype/build audit must be able to prove all of the following:

1. every mandatory interaction maps to B1–B7 and a current decision/technical/truth/continuity/consequence/recovery reason;
2. any interaction without a current reason is absent from the default path;
3. the complete core can finish without login/account/contact/payment;
4. optional account entry never blocks accountless finish/exit on cancel/error/outage;
5. sign-in does not automatically link/import/promote/extend J0/J1;
6. successful sign-in does not automatically create a managed-device record without an explicit authorized action/data-flow rule;
7. a valid session suppresses redundant sign-in;
8. dashboard empty/list is system output, not mandatory form friction;
9. account/device fields are minimum-purpose and do not create a child profile/history domain;
10. device-record ownership/dashboard presence never counts as technical protection verification;
11. locale/platform/version/setup questions appear only when they change routing;
12. the user is never asked to choose DoH versus DoT where platform routing determines it;
13. Android/Apple platform-required security actions remain explicit and are not marketed as universal one-click setup;
14. parent confirmation is requested only where it changes evidence state and never yields technical verification by itself;
15. DNS verification runs automatically where feasible or exposes only one deliberate Check/Recheck per changed condition;
16. irrelevant external-service friction is absent;
17. Protection Map has no mandatory acknowledgement checkbox;
18. help/retry/reset/reinstall/removal remain conditional rather than mandatory happy-path steps;
19. logout, unlink/revoke, device-record deletion, account deletion, anonymous reset and physical DNS removal are distinct operations with no cross-claim of completion;
20. account deletion/revoke/device-record deletion confirmations identify the actual target/consequence without repeated confirmation theatre;
21. provider outage adds no compensating identity collection and leaves the accountless core available;
22. no field is retained for hypothetical analytics/marketing/future use;
23. no browsing/query/activity history, broad DNS admin or raw AdGuard control surface is introduced;
24. generic visible brand copy uses `SafeWeb` / `SafeWeb DNS`; exact `UseSafeWeb.com`/`dns.usesafeweb.com` appears only as an actual technical identifier;
25. unsupported/uncertain states stop optimistic progression instead of adding friction to manufacture success;
26. retries do not loop equivalent failures or blindly replay ambiguous consequential actions.

## 13. Current acceptance candidate

ACC-0316 requires each retained interaction to have a decision/technical/safety reason, removable steps to be removed, platform constraints to be explicit, and unsupported one-click claims to be absent.

This current contract:

- challenges all 25 current TSK-0315 dual-mode stages;
- preserves the shortest safe accountless core;
- adds bounded friction rules for the now-approved optional account/session/dashboard/device lifecycle;
- removes mandatory/redundant identity, confirmation, dashboard and analytics friction;
- preserves platform/security/evidence actions that cannot truthfully be removed;
- separates managed-device continuity from child profiling and protection verification;
- preserves current SafeWeb naming and technical-identifier distinction;
- defines 26 deterministic acceptance assertions.

**Candidate disposition:** TSK-0316 may be PASS only after independent VER-0316 confirms the current WBS/dependency contract, dual-mode matrix, zero-budget removals, platform/one-click truth, account/lifecycle separation, privacy/data constraints, SafeWeb naming, retry rules and non-inference.

## 14. Non-inference

This is L4 friction-design acceptance only. It does not prove real-parent usability, implementation, provider/auth architecture, persistent schema/storage, legal/privacy completion, public publication, payment, production behavior, LG-06 or launch. It does not make any successor PASS.
