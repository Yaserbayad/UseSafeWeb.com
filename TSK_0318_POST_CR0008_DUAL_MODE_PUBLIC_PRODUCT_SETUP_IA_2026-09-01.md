# TSK-0318 — Dual-Mode Public Website and Product/Setup IA — Post-CR-0008

**Task:** TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems  
**Acceptance:** ACC-0318  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Priority:** HIGH  
**AI capability / Action Authority:** A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-cr0008  
**Date:** 2026-09-01  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE  
**Authority:** DEC-0053/CR-0006 dual-mode Version-1 scope; DEC-0054/CR-0007 autonomy/lifecycle; CR-0008 current action-authority/evidence model; current TSK-0315 dual-mode service blueprint; current TSK-0229 accountless-state separation; current TSK-0312 parent-auth/session requirements; current TSK-0142 lightweight dashboard/device-management requirements; current TSK-0320 protection-state semantics; current TSK-0331 account/device lifecycle; current TSK-0319 troubleshooting/recovery/help design.

## 1. Objective, supersession, and acceptance boundary

This artifact supersedes the account-exclusion-dependent parts of the historical `TSK_0318_PUBLIC_PRODUCT_SETUP_IA_DESIGN_CANDIDATE_2026-08-28.md` for current acceptance.

The historical artifact correctly separated public discovery from operational setup and correctly protected the accountless core, but its explicit prohibitions on Login, Dashboard and Account surfaces and its statement that no account/session lifecycle existed in navigation were invalidated by DEC-0053/CR-0006.

Current UseSafeWeb Version 1 is dual-mode:

1. **Accountless core:** the complete First Phone Safety Setup remains usable without login.
2. **Optional parent account:** sign-in/session continuity plus a lightweight dashboard and bounded device management are available as optional continuity features.

This IA defines information architecture only. It does not approve implementation architecture, authentication vendor acceptance, persistent schema/storage, legal/privacy completion, payment, publication, market activation or launch. No real-user behavioral evidence is claimed.

ACC-0318 requires every page/screen to have one purpose, entry/exit, content owner, SEO/index intent, privacy/accessibility requirement, and no duplicated or missing critical step. Sections 4–7 provide that mapping and Sections 8–12 define the cross-system rules used to test completeness and non-duplication.

## 2. IA invariants

1. **Public and product are distinct systems.** Public surfaces explain, establish trust and route. Product/setup surfaces perform stateful setup, verification, account continuity, device management, troubleshooting, removal and recovery.
2. **Core value never requires authentication.** Start, platform routing, native safeguard guidance, DNS setup/verification, relevant service guidance, Protection Map, troubleshooting, removal and recovery remain available without login.
3. **Optional account is visible but not coercive.** Sign in / Manage devices may be offered where useful, including a public sign-in entry and a post-core continuity choice, but cancel/failure/outage returns safely to an accountless-capable path.
4. **Anonymous and persistent domains are separate.** J0/J1 accountless state is never automatically joined, promoted, copied or extended by account sign-in. Any future explicit transfer requires its separately approved field-level data-flow contract.
5. **Dashboard presence is not protection proof.** Stored ownership/device/evidence metadata never becomes current technical verification by navigation alone.
6. **Destructive operations are distinct.** Logout, revoke/unlink, dashboard-record deletion, account deletion, anonymous-state deletion, and physical DNS removal are different journeys and cannot claim one another completed.
7. **No browsing/query/activity history or child account.** The IA contains no history, activity timeline, child profile/account, raw DNS query view, or surveillance surface.
8. **No broad DNS administration.** Customer product IA exposes curated setup/status/lifecycle controls only; it never exposes AdGuard administrator credentials, arbitrary `/control` functions, query logs or a general DNS console.
9. **Protection truth is explicit.** S1–S6 semantics remain owned by TSK-0320; IA provides places to render verified, parent-confirmed, action-needed, not-covered, uncertain and removed states without collapsing them into a safety score.
10. **Recovery is first-class.** State-specific help, verification, reinstall/reconfigure, reset, removal, provider-outage handling and post-removal recovery are reachable at point of need.
11. **Accessibility/localization are structural.** Every screen must support keyboard/focus order, semantic headings/landmarks, programmatic status/error association, reduced-motion-safe behavior, content expansion and RTL mirroring where applicable; English/Turkish/Arabic technical capability does not itself activate a market.
12. **No premature public claim.** A route existing in IA is not evidence that the capability, provider, market, payment, production or launch state is approved.

## 3. System boundaries and connection points

### 3.1 Public website system

Purpose: discovery, understanding, trust, compatibility/limits, privacy explanation, help/status discovery, and entry into either the accountless setup or optional parent-account continuity.

Public pages may link into product routes, but they do not own operational protection state.

### 3.2 Product/setup system

Purpose: execute the accountless setup and optional account/device lifecycle, display truthful evidence state, provide self-service troubleshooting/recovery, and preserve safe exits/removal.

Operational screens may link back to public explanatory/privacy/status content, but operational state remains product-owned.

### 3.3 Approved connection points

- Public **Start setup** → accountless product start.
- Public **Sign in / Manage devices** → optional account sign-in; never a prerequisite for Start setup.
- Product help/limits/privacy links → public explanatory pages in a new or safely resumable context.
- Accountless core completion → **Finish without account** or optional **Sign in to manage devices**.
- Auth/provider error → account-only failure state with a direct **Continue without account** / return path.
- Dashboard **Add device** → fresh supported setup flow; no automatic import of an existing J0/J1 journey.
- Device detail → current verification, reinstall/reconfigure, replace, revoke/unlink, delete record, and removal guidance as distinct actions.

## 4. Public website IA matrix

Logical route names are IA identifiers, not a frozen framework/router implementation.

| ID / logical route | One purpose | Primary entry | Primary exit / next action | Content owner | SEO / index intent | Privacy requirement | Accessibility requirement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 `/` Home | Explain bounded First Phone Safety Setup value and route to the next appropriate action. | Search/direct/referral. | Start setup; How it works; Compatibility; Sign in/manage. | Product + Content | INDEX; canonical public landing. | Informational only; no operational protection state required. | One clear H1; visible keyboard CTAs; no motion-dependent meaning; truthful link labels. |
| P02 `/how-it-works` | Explain Phone / Internet / Service model, evidence states and accountless-vs-optional-account boundary. | Home/search/contextual help. | Start setup; Compatibility; Privacy. | Product + Content | INDEX. | No identity/activity collection needed for content. | Structured headings/lists; text alternative for any diagrams; state distinctions not color-only. |
| P03 `/compatibility` | Explain supported/unsupported platform/network mechanisms and known limits. | Home/how-it-works/setup help. | Start supported setup; Help; return. | Product + Platform Content | INDEX when source-current. | No device fingerprint/history required merely to read. | Platform choices named programmatically; tables reflow; unsupported state announced clearly. |
| P04 `/protection-and-limits` | Explain verified/confirmed/uncertain/not-covered/removed semantics and material DNS limits. | Home/Protection Map/help. | Start; How it works; Help. | Product + Content | INDEX. | No individual protection status displayed here. | Status examples have text labels, not color alone; clear reading order. |
| P05 `/privacy` | Explain minimisation, no browsing/query/activity history, accountless/persistent separation and deletion concepts at approved claim level. | Global footer, setup/account links. | Return; Start; account/settings privacy entry. | Privacy + Content | INDEX when publication authority permits. | Never imply legal completion beyond current authority; no hidden tracking required to read. | Plain language, semantic sections, accessible policy navigation. |
| P06 `/help` | Route ordinary questions to source-current setup, verification, false-positive, reset/reinstall/remove and account/device lifecycle help. | Global nav, product help, search. | Specific help topic; Start; Status. | Customer Experience + Content | INDEX only for approved/source-current help topics; stale topics noindex/remove. | No browsing history request; issue intake remains minimal and separate. | Search/results keyboard operable; topic names descriptive; error/help states announced. |
| P07 `/status` | Report service/provider operational uncertainty without implying protected state. | Global footer, help, outage links. | Return; Help; removal/recovery. | SRE + Content | INDEX if approved public status surface exists; otherwise NOINDEX until publication authority. | Aggregate/synthetic service state only; no customer browsing history. | Live updates announced without focus theft; timestamps programmatic; status not color-only. |
| P08 `/sign-in` public transition | Explain optional parent-account continuity and enter authentication without making it a core prerequisite. | Header/manage CTA, post-core optional choice, account-only deep link. | Auth start; Continue without account; Home. | Product + Auth Content | INDEX only if a public sign-in landing is intentionally approved; auth mechanics/callbacks NOINDEX. | Minimum auth disclosure; no anonymous J0/J1 import promise. | Explicit optionality; cancel/continue-without-account visible and keyboard reachable. |
| P09 `/terms-or-required-notices` placeholder | Provide only currently approved public notices when separately authorized. | Footer / legally required entry. | Return. | Legal/Privacy + Content | INDEX/NOINDEX only under owning publication decision. | This IA does not assert legal completion. | Semantic long-form navigation and readable text. |

Public IA deliberately has **no dashboard, protection-history, child-profile, raw-query, admin-console or payment-gate route**.

## 5. Accountless product/setup IA matrix

| ID / logical route | One purpose | Primary entry | Primary exit / next action | Content owner | SEO / index intent | Privacy requirement | Accessibility requirement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 `/start` | Begin or safely restart the core setup without login. | Public Start setup; direct supported link. | Platform/context route. | Product + UX | NOINDEX; operational. | Initialize only approved J0/J1 state; no identity required. | Focus on page title; one primary Start action; reset warning programmatically associated. |
| C02 `/setup/route` | Capture only the minimum supported platform/setup context needed to choose instructions. | Start. | Native safeguard or supported/not-covered state. | UX + Product | NOINDEX. | Minimum routing fields only; no child identity. | Labels/instructions bound to controls; validation announced; choices work by keyboard. |
| C03 `/setup/native` | Present the relevant native phone safeguard step and truthful confirmation state. | Route. | DNS setup; Not covered/help. | UX + Platform Content | NOINDEX. | No activity/history collection; parent confirmation separate from system verification. | Step semantics, clear skip/not-covered text, accessible external-instruction links. |
| C04 `/setup/dns` | Guide exact supported platform-specific UseSafeWeb DNS configuration. | Native step or supported direct resume. | Verify; Troubleshoot; Remove/recovery. | UX + DNS/Network | NOINDEX. | No credentials/query history; only transient setup state. | Ordered instructions; code/host values selectable/readable; error/conflict instructions announced. |
| C05 `/setup/verify` | Run/display current approved technical verification and evidence state. | DNS setup, dashboard reverify, help. | Protection Map; Troubleshoot; Retry after changed condition; Remove. | DNS/Product | NOINDEX. | Controlled/synthetic verification only; no user browsing history. | Busy/live status accessible; final state announced; no infinite auto-retry. |
| C06 `/setup/service` | Present zero/one currently relevant approved external-service safeguard or explicit skip/not-covered. | Verify or route. | Protection Map. | Product + Content | NOINDEX. | No third-party credentials/activity history collected by this screen. | Skip and applicable action equally operable; unsupported reason readable. |
| C07 `/setup/protection-map` | Summarize current Phone / Internet / Service states and limits without a safety score. | Verify/service; dashboard device status. | Core finish; specific action/help; optional account choice. | Product + UX | NOINDEX. | Current evidence only; account ownership/stored state never upgrades verification. | Each layer has text state/actor/currentness; headings and status associations; not color-only. |
| C08 `/setup/complete` | Complete/exit accountless core and offer optional continuity without coercion. | Protection Map. | Finish without account; optional Sign in/manage; Home. | Product + UX | NOINDEX. | J0/J1 expiry/deletion rules remain independent of account choice. | Finish-without-account is clear first-class action; optional account explanation readable. |
| C09 `/setup/help/:issue` | Resolve one identified setup/verification/false-positive/network/reset/removal issue at point of need. | Any applicable product state. | Changed-condition recheck; previous step; removal/recovery; exceptional route. | Customer Experience + owning technical content | NOINDEX unless an equivalent public help article is separately published. | Minimal issue facts; no routine browsing/query history. | Decision tree has deterministic focus/order; errors/actions programmatically associated. |
| C10 `/setup/reset` | Clear/restart web journey state only, with explicit distinction from device DNS removal. | Help/settings/expired state. | Start. | Product + UX | NOINDEX. | Delete only applicable anonymous journey state; no account/device side effects. | Consequence text precedes confirm; cancel available; result announced. |
| C11 `/setup/remove` | Guide physical UseSafeWeb DNS removal for the current supported platform. | Help, Protection Map, dashboard device actions. | Post-removal recovery; Help. | DNS + UX | NOINDEX. | No browsing history required; deletion/revoke/account actions remain separate. | Destructive consequence explicit; platform instructions accessible; uncertain result not labelled Removed. |
| C12 `/setup/recovery` | Restore ordinary connectivity / route after failed setup or removal without false protection claims. | Remove/troubleshoot/verification failure. | Recheck; Help; Exit. | DNS + UX | NOINDEX. | Neutral/synthetic recovery checks only. | Recovery states announced; no automated focus churn; alternate action visible. |
| C13 `/setup/not-covered` | Explain unsupported platform/network/condition and safe alternatives without fabricating support. | Route/verify/help. | Help; Compatibility; Exit. | Product + Platform Content | NOINDEX operational; public compatibility owns indexable explanation. | No extra identity requested to compensate for unsupported state. | Reason and alternatives text-first; links descriptive. |
| C14 `/setup/status-uncertain` | Explain inconclusive/conflicting evidence and the exact next safe action. | Verification / conflict detection. | Troubleshoot; Recheck after change; Remove; Status. | Product + DNS | NOINDEX. | No history collection to improve confidence by default. | Uncertainty explicitly announced; retry is user-controlled/bounded. |

## 6. Optional parent-account and lightweight dashboard IA matrix

Authentication/product route names remain logical IA; exact provider callback mechanics are owned by downstream architecture.

| ID / logical route | One purpose | Primary entry | Primary exit / next action | Content owner | SEO / index intent | Privacy requirement | Accessibility requirement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A01 `/account/sign-in` | Start optional parent authentication for continuity/device management. | Public Sign in; post-core optional choice; protected account deep link. | Provider auth; Cancel/continue without account. | Auth + Product | NOINDEX. | Minimum approved provider/account fields only; no J0/J1 auto-link. | Optionality/cancel clear; auth error association; keyboard operable provider action. |
| A02 `/account/auth-result` | Resolve successful/cancelled/failed provider return into a known account-only state. | Provider callback. | Dashboard; retry; continue accountless. | Auth/App | NOINDEX. | Validate account/session state; do not expose provider tokens in URL/UI/log evidence. | Result announced; error recovery and accountless fallback visible. |
| A03 `/account` dashboard | Show the authenticated parent's minimum device list or empty state and account-only next actions. | Successful sign-in/valid session. | Device detail; Add device; Account settings; Logout. | Product + App | NOINDEX. | Only authorized parent-owned minimum records; no browsing/activity/query timeline. | Empty/list states semantic; device links distinguishable; session error announced. |
| A04 `/account/devices/add` | Start a fresh managed-device setup or explicitly authorized future transfer. | Dashboard. | Fresh setup route; Dashboard; cancel. | Product + App + UX | NOINDEX. | No implicit J0/J1 transfer; minimum device ownership context only. | Choice consequences readable; cancel preserves existing state. |
| A05 `/account/devices/:device` | Show one authorized managed device's lifecycle metadata, current evidence/currentness, and bounded actions. | Dashboard. | Reverify; reinstall; replace; revoke; delete record; removal help. | Product + App | NOINDEX. | Fail closed on ownership mismatch; no child profile/history; stored status not current proof. | Status/age/currentness text labels; action groups semantic; destructive actions separated. |
| A06 `/account/devices/:device/reverify` | Request/display current technical re-verification for that device context. | Device detail. | Device detail; Troubleshoot. | DNS/App + UX | NOINDEX. | Minimum context; no browsing history. | Same accessible status rules as C05. |
| A07 `/account/devices/:device/reinstall` | Guide a supported reinstall/reconfigure without changing ownership/lifecycle implicitly. | Device detail/help. | Reverify; Device detail; Recovery. | UX + DNS/App | NOINDEX. | No credential/query history exposure. | Ordered platform guidance and rollback path accessible. |
| A08 `/account/devices/:device/replace` | Mark lifecycle replacement intent and start a new-device flow without inheriting proof. | Device detail. | Add/fresh setup; Device detail. | Product + App | NOINDEX. | New device does not inherit S1/S2/history automatically. | Consequence/old-vs-new distinction explicit before confirm. |
| A09 `/account/devices/:device/revoke` | Revoke/unlink dashboard management association only. | Device detail. | Dashboard/device state result; physical removal help separately. | Auth/App + Product | NOINDEX. | Ownership association only; must not claim DNS removal. | Destructive confirmation, cancel, result/error announced. |
| A10 `/account/devices/:device/delete-record` | Delete the governed dashboard device record only. | Device detail. | Dashboard; physical removal guidance separately. | App + Privacy | NOINDEX. | Data deletion scope explicit; DNS config/J0/J1/account remain separate. | Scope/consequence explicit; pending/failed states announced. |
| A11 `/account/settings` | Expose only minimum account/session/privacy lifecycle controls. | Dashboard. | Logout; Account deletion; Privacy; Dashboard. | Product + Auth/Privacy | NOINDEX. | No unrelated profile enrichment or history. | Settings grouped semantically; destructive actions separate. |
| A12 `/account/logout` | End applicable authenticated session only. | Account settings/header. | Public/home or accountless-capable entry. | Auth/App | NOINDEX. | Session lifecycle only; DNS/account/device records unchanged. | Result announced; return path clear. |
| A13 `/account/delete` | Request and track account deletion, distinct from device DNS removal and anonymous-state deletion. | Account settings. | Deletion result; removal guidance; Home. | Auth/App + Privacy | NOINDEX. | Invalidate/handle account/device data only under owning contract; J0/J1 and physical DNS separate. | Scope, irreversibility/pending/error state explicit; confirm/cancel accessible. |
| A14 `/account/session-expired` | Explain expired/revoked/invalid session and fail closed for account-only actions. | Any protected account route. | Re-authenticate; Continue accountless; Home. | Auth/App + Product | NOINDEX. | Do not disclose account/device data before authorization. | Session state announced; focus on recovery choices; no redirect loop. |
| A15 `/account/provider-unavailable` | Contain auth/provider outage to account-only functions while preserving accountless core. | Sign-in or account action during provider outage. | Retry later; Continue without account; Status/help. | Auth/App + SRE Content | NOINDEX. | Do not collect extra identity/history to compensate. | Clear temporary-scope message and working alternative path. |

## 7. Exceptional/help lifecycle coverage matrix

This matrix proves that critical lifecycle states are not hidden inside generic Help or duplicated as conflicting owners.

| Need | Canonical IA owner | Secondary links allowed | Explicitly not owned here |
| --- | --- | --- | --- |
| Setup routing | C02 | P03 compatibility | Account ownership. |
| Native safeguard guidance | C03 | P06 help | DNS verification. |
| DNS configuration | C04 | A07 when account-managed context exists | Account sign-in. |
| Technical verification | C05 / A06 contextual wrapper | C09 troubleshooting | Ownership/dashboard presence. |
| Protection evidence summary | C07 / A05 contextual device view | P04 explanatory limits | Safety score/history. |
| False positive / ordinary issue | C09 | P06 public help | Raw query-log browser. |
| Web-journey reset | C10 | C09 | Physical DNS removal, account deletion. |
| Physical DNS removal | C11 | A05/A09/A10/A13 may link to it | Revoke/delete/account deletion. |
| Post-removal recovery | C12 | C09 | Protection claim. |
| Sign in/session | A01/A02/A14/A15 | P08 transition | Accountless core gating. |
| Dashboard/device list | A03 | — | Activity/browsing history. |
| Device lifecycle | A04–A10 | C04/C05/C09/C11 when technical action needed | Account deletion. |
| Account lifecycle | A11–A13 | P05 privacy | Physical DNS removal/J0-J1 deletion. |
| Anonymous-state expiry/delete | C01/C08/C10 behavior under TSK-0229 | P05 privacy explanation | Persistent account/device deletion. |

## 8. Entry/exit and navigation model

### 8.1 Public global navigation

Recommended semantic order:

`How it works | Compatibility | Protection & limits | Help | [Start setup] | Sign in`

Privacy and Status remain visible in footer/contextual navigation. **Start setup is primary; Sign in is secondary/optional.**

### 8.2 Accountless product navigation

Do not expose a broad website menu that encourages abandoning a stateful task. Product chrome may provide:

- current step / progress where useful;
- Help;
- Protection Map once meaningful;
- Exit safely / Start over where appropriate;
- optional Sign in/manage only at non-coercive connection points.

Back/exit behavior must not imply that device configuration was rolled back.

### 8.3 Authenticated product navigation

Authenticated chrome may provide:

`Devices | Add device | Help | Account`

It must not provide raw DNS administration, browsing/activity history or child-account navigation.

### 8.4 Deep-link rules

- Public content may be deep-linked freely when publication authority exists.
- Accountless operational deep links must validate required transient context and safely route to Start/Not covered rather than infer missing state.
- Account-only deep links validate session and authorization first; unauthenticated users go to A14/A01 with an accountless alternative, not to leaked content.
- Device deep links fail closed on ownership mismatch and expose no record metadata before authorization.

## 9. SEO and indexing contract

1. **Indexable by default only:** public informational pages P01–P07 when current/publication-authorized and source-current.
2. **Conditional index:** P08 sign-in landing and P09 notices only when the owning product/legal/publication decision explicitly requires it.
3. **NOINDEX:** all `/start`, `/setup/*`, `/account/*`, provider callback/result, device-management, reset, removal, recovery and account lifecycle screens.
4. Public help topics may be indexable only when independently source-current; operational issue screens remain NOINDEX.
5. Canonical public pages own explanatory content; operational screens link rather than clone large indexable explanations.
6. SEO metadata must not overstate safety, platform support, market availability, account/provider readiness or legal/privacy completion.

## 10. Privacy and security-by-IA contract

The IA must make prohibited data/surface expansion structurally difficult:

- no route for browsing/query/activity history;
- no child account/profile route;
- no raw AdGuard query/admin/filter-control console;
- no mandatory sign-in intercept before core setup;
- no J0/J1 automatic save-to-account route;
- no provider token/secret display route;
- no account/device record disclosure before authorization;
- no protection status inferred merely because a record exists;
- no combined destructive control that ambiguously means revoke + delete account + remove DNS;
- no account deletion wording that claims physical DNS configuration removal;
- no reset wording that claims account/device/DNS deletion beyond its owned scope.

Any implementation that adds such a route is a material divergence from this IA and requires separate current authority/acceptance.

## 11. Accessibility and localization-by-IA contract

Every public/product/account route must support, as applicable:

1. one descriptive page title and one clear H1;
2. landmark/heading hierarchy and logical DOM/focus order;
3. keyboard operation without pointer-only controls;
4. visible focus and programmatic control labels;
5. error, warning, pending, success and protection states associated with the affected control/region and not represented by color alone;
6. bounded live-region use for asynchronous verification/provider/deletion states without repetitive announcements;
7. explicit confirmation/cancel for destructive state changes;
8. text expansion and responsive reflow without obscuring the primary action;
9. externalized copy/locale fallback compatibility and RTL-safe directional layout where applicable;
10. no meaning encoded solely by icon orientation where RTL mirroring may change perception.

This IA does not claim native-speaker validation or market activation.

## 12. Duplicate/missing-step audit

### 12.1 No duplicated critical owner

- Public pages explain; operational screens perform.
- C05 owns accountless/current technical verification; A06 is only the authenticated device-context entry to the same owning verifier semantics.
- C11 owns physical DNS removal; A09/A10/A13 own revoke/device-record/account deletion and may only link to C11.
- C10 owns anonymous web-journey reset; it cannot delete account/device state or claim DNS removal.
- A13 owns account deletion; it cannot claim J0/J1 deletion or physical DNS removal unless separately executed by the owning workflows.
- P04 explains protection semantics; C07/A05 render actual applicable state.

### 12.2 No missing critical current Version-1 step

The IA includes all current required outcome classes:

- discover / understand / trust / compatibility / privacy / help / status;
- accountless start and route;
- native safeguard guidance;
- DNS configure and technical verify;
- zero/one relevant service guidance;
- Protection Map and limitations;
- ordinary troubleshooting / false positive / uncertainty;
- reset / reinstall/reconfigure / removal / recovery;
- optional sign-in, auth result, return/session expiry/provider outage;
- dashboard empty/list and device detail;
- add device, reverify, reinstall, replace, revoke/unlink, delete record;
- logout and account deletion;
- safe accountless continuation when account functions fail.

### 12.3 Explicitly absent by current scope

- mandatory login for core value;
- child accounts/profiles;
- browsing/query/activity history;
- raw/broad DNS administration;
- general social/community feed;
- payment gate before core value;
- overall safety score / all-clear page;
- market-specific activation merely because localized copy exists.

## 13. Current dependency and evidence impact

### TSK-0318 predecessor

`TSK-0315` is current PASS under the post-CR-0007 dual-mode service blueprint. This candidate consumes that current dual-mode boundary and does not revive the superseded accountless-only blueprint.

### Direct successors

- **TSK-0310:** its accepted accountless public-to-setup prototype remains evidence for the core path only. This IA does not claim that the historical prototype implements the optional account/dashboard branch; any successor/current gate requiring the complete dual-mode integrated experience must independently prove it.
- **TSK-0311:** its localization architecture may continue to own externalization/fallback mechanics, but account/dashboard copy added by implementation must also obey those mechanics; this IA does not mark TSK-0311 PASS or fail by itself.

No successor becomes PASS merely because this candidate exists.

## 14. Deterministic ACC-0318 assertions

Independent verification must fail this candidate unless all assertions pass:

1. Public and product/setup systems are explicitly distinct and connected.
2. Accountless core starts and completes without login.
3. Optional sign-in exists but is never a prerequisite for core value.
4. Sign-in cancel/failure/provider outage leaves an accountless-capable continuation.
5. Dashboard empty/list/device detail/add-device routes exist.
6. Session expired/revoked/invalid state exists and fails closed for account-only data.
7. Device reverify/reinstall/replace/revoke/delete-record routes are represented distinctly.
8. Logout, device revoke, device-record delete, account delete, anonymous-state delete/reset and physical DNS removal are distinct.
9. No automatic J0/J1-to-account linkage/promotion exists.
10. No browsing/query/activity-history or child-account route exists.
11. No raw AdGuard admin/query-log/broad DNS administration route exists.
12. Protection Map/current evidence semantics do not equate account ownership or stored status with current technical verification.
13. Public indexable pages have explicit SEO intent and operational/account routes are NOINDEX.
14. Every matrix row contains purpose, entry, exit, owner, SEO intent, privacy and accessibility requirements.
15. Accessibility requirements cover keyboard/focus, semantic structure, programmatic errors/status and non-color-only state.
16. Localization/RTL structural requirements are explicit without claiming market activation.
17. Troubleshooting, reset, removal, recovery and not-covered/uncertain states are reachable at point of need.
18. Duplicate/missing-step audit covers all current Version-1 critical journey and lifecycle classes.
19. Historical account-exclusion language is explicitly superseded rather than silently overwritten.
20. No architecture/provider/legal/privacy/payment/publication/launch PASS is inferred.

## 15. Candidate disposition

This artifact is the current TSK-0318 design candidate for independent acceptance. It repairs the CR-0006-invalidated account-exclusion assumptions while preserving the complete accountless core, privacy minimisation, technical protection truth, accessibility/localization structure, self-service recovery, and explicit separation between public discovery, operational setup, optional account continuity and destructive lifecycle actions.

**TSK-0318 remains non-PASS until independent verification, durable evidence publication, runtime reconciliation, and exact GitHub read-back succeed.**
