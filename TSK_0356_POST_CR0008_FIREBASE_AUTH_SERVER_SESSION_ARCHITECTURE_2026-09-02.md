# TSK-0356 — Post-CR-0008 Firebase Authentication and Server-Session Architecture

**Task:** TSK-0356 — Select and freeze the initial authentication and server-session architecture  
**Acceptance / Verification / Evidence:** ACC-0356 / VER-0356 / EVD-0356  
**Lifecycle / Priority / Authority:** L5 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date / source review:** 2026-09-02 UTC  
**Gate:** contributes to LG-07 Architecture, Security, Privacy and Delivery Readiness  
**Direct predecessors:** TSK-0235 current PASS; TSK-0585 current PASS

## 1. Decision

Freeze the Version-1 optional-parent-account authentication architecture as follows:

1. **Provider:** base Firebase Authentication on the no-cost Spark plan, with **Google as the only initially enabled sign-in provider**.
2. **No Identity Platform upgrade initially.** Upgrade remains an evidence-triggered option, not an implementation prerequisite.
3. **No password, email-password, phone/SMS sign-in, SMS MFA, SAML or OIDC expansion** in Version 1 without separate owner-approved scope and security/privacy/vendor re-review.
4. **Accountless core remains independent and complete.** Discover/start/setup/verify/Protection Map/troubleshooting/recovery/removal may not require authentication.
5. **Browser sign-in:** use the supported Firebase JavaScript SDK with `GoogleAuthProvider`. Use **in-memory Firebase Auth persistence (`inMemoryPersistence`)** so the Firebase browser credential is not retained as the application session.
6. **Application session:** after Google/Firebase sign-in, the browser sends a fresh Firebase ID token only to a dedicated HTTPS session-exchange endpoint. The server verifies it with the Firebase Admin SDK, enforces `auth_time <= 5 minutes`, then creates a Firebase **server-side session cookie**.
7. **Session cookie:** one host-scoped application cookie, preferably `__Host-` prefixed, `Secure`, `HttpOnly`, explicit `SameSite=Lax`, `Path=/`, no `Domain`; Version-1 absolute lifetime **maximum 7 days**, with no sliding extension merely from ordinary use.
8. **Protected account routes:** verify the server session cookie with revocation checking and perform server-side parent/resource authorization on every account/device operation. Authentication never substitutes for ownership authorization.
9. **Provider outage:** no new account authority is created when Firebase identity/session validity cannot be established. Account-only functions fail closed/degrade truthfully while the independently healthy accountless core remains usable.
10. **Revocation:** current-browser logout clears the local application session cookie. Security/global sign-out, account disable/delete and other global invalidation use Firebase refresh-token revocation plus revocation-aware session verification. Product copy must distinguish local logout from global revocation.
11. **Identity anchor:** Firebase UID/provider subject is identity input only. It is not device ownership, AdGuard ClientID authority, technical protection evidence, or a reason to store unnecessary Google profile data.
12. **Data boundary:** do not persist raw Firebase ID tokens, refresh tokens, Google OAuth access tokens, session-cookie values, browsing/query/activity history, child profiles, or unnecessary provider profile fields in product records/logs/analytics.

This is an L5 architecture freeze only. It does **not** configure a Firebase project/provider, create users, accept vendor/legal terms for the owner, create billing, deploy software, process real users, pass LG-07, or authorize L6.

## 2. Current authority and predecessor reconciliation

### 2.1 TSK-0353 security/NFR contract

Current TSK-0353 requires, among other controls:

- complete core value without login;
- server verification of Firebase identity before account authority;
- recent authentication (`auth_time <= 5 minutes`) before server-session creation and high-risk operations;
- server session cookie `Secure`, `HttpOnly`, explicit `SameSite`, host-scoped where possible, Version-1 maximum 7-day lifetime;
- no Firebase auth token persistence in browser local/session storage for the server-session pattern;
- revocation-aware verification for protected account routes;
- CSRF protection on unsafe cookie-authenticated requests;
- server-side authorization/ownership checks on every account/device operation;
- provider/datastore failure must fail account authority closed while preserving healthy accountless operation;
- no child account, browsing/query/activity history, local password or SMS expansion.

This architecture adopts those requirements without relaxation.

### 2.2 TSK-0585 dated vendor/cost/terms contract

Current accepted TSK-0585 established on 2026-09-02 that:

- Spark requires no payment method and supports the planned social-auth route without an authentication-service charge under the current vendor pricing page;
- Firebase Authentication with Identity Platform is an optional upgrade, not required for this initial route;
- current upgraded Identity Platform Spark limits include 3,000 Tier-1 DAU / 2 Tier-2 DAU, while Blaze uses MAU pricing/no-cost tiers;
- phone/SMS authentication is separately billed and is excluded from current scope;
- Firebase Authentication is currently operated only from US data centers and processes data exclusively in the United States;
- Firebase Terms were last modified May 1, 2026 and list Firebase Authentication under Google Cloud Platform Terms of Service;
- pricing, quota, terms, processing-location, legal/privacy, outage, feature and material-spend changes are explicit re-review/exit triggers.

This task does not reinterpret those legal/vendor facts or convert them into legal approval.

## 3. Dated official-source register

Rechecked 2026-09-02 UTC:

| Official source | URL | Architecture fact consumed |
| --- | --- | --- |
| Firebase pricing | `https://firebase.google.com/pricing` | Spark is no-cost/no payment method; “Other Authentication services” are available; Phone Auth is separately billed; Identity Platform has separate plan/usage boundaries. |
| Firebase pricing-plan guide | `https://firebase.google.com/docs/projects/billing/firebase-pricing-plans` | Most Authentication options/social sign-in are no-cost on Spark; linking billing can change plan state. |
| Firebase Authentication | `https://firebase.google.com/docs/auth` | Identity Platform is an optional upgrade; upgraded Spark/Blaze usage-limit model is distinct. |
| Firebase Auth limits | `https://firebase.google.com/docs/auth/limits` | Identity Platform Spark instrumentless Tier-1 limit is 3,000 DAU and Tier-2 is 2 DAU; limits/abuse controls may change. |
| Google sign-in with Firebase JS SDK | `https://firebase.google.com/docs/auth/web/google-signin` | Firebase supports Google sign-in through `GoogleAuthProvider` with popup or redirect flows. |
| Firebase Auth JS reference | `https://firebase.google.com/docs/reference/js/auth` | `inMemoryPersistence` is Persistence type `NONE`; `setPersistence`/`initializeAuth` allow explicit persistence selection. |
| Redirect best practices | `https://firebase.google.com/docs/auth/web/redirect-best-practices` | Redirect sign-in on browsers blocking third-party storage requires one of Firebase’s documented mitigations; popup is an explicit alternative. |
| Verify Firebase ID tokens | `https://firebase.google.com/docs/auth/admin/verify-id-tokens` | Server validation includes signature/key plus project `aud`, issuer, non-empty subject/UID, expiry and authentication-time claims. |
| Manage Firebase session cookies | `https://firebase.google.com/docs/auth/admin/manage-cookies` | Server session cookies support 5-minute to 2-week expiration; server verification and optional revocation checking are supported; revocation checking adds a network request. |
| Manage Firebase user sessions | `https://firebase.google.com/docs/auth/admin/manage-sessions` | ID tokens are short-lived; refresh tokens are long-lived until defined invalidation conditions; Admin SDK supports refresh-token revocation and revocation-aware verification. |
| Firebase privacy/security | `https://firebase.google.com/support/privacy` | Firebase Authentication currently processes data exclusively in US data centers. |
| Firebase Terms | `https://firebase.google.com/terms/` | Current page says last modified May 1, 2026 and lists Firebase Authentication under Google Cloud Platform Terms of Service. |

No third-party blog or unauthoritative pricing source is used to freeze this architecture.

## 4. Threat model and trust boundaries

### 4.1 Assets

Protect:

- parent authentication/session authority;
- parent-to-device ownership and lifecycle state;
- server-side Firebase Admin credentials/configuration;
- future datastore/AdGuard administrative credentials;
- optional-account availability without compromising accountless availability;
- privacy boundary excluding browsing/query/activity history and child identity.

### 4.2 Trust boundaries

1. **Browser -> Google/Firebase:** untrusted browser initiates provider sign-in.
2. **Browser -> session exchange:** fresh Firebase ID token crosses into the application backend.
3. **Session cookie -> protected backend route:** bearer session proves authentication only after server verification.
4. **Authenticated parent -> owned resource:** every device/dashboard/AdGuard-backed operation crosses an authorization boundary.
5. **Backend -> Firebase Admin/Auth service:** external provider dependency may fail, throttle, change terms or return errors.
6. **Backend -> future ownership store / AdGuard adapter:** authenticated identity must not bypass ownership or control allowlists.

### 4.3 Primary abuse cases and mandatory design response

| Threat | Abuse case | Frozen response |
| --- | --- | --- |
| Spoofing | forged/expired/wrong-project Firebase token | Admin SDK verification; reject invalid audience/issuer/signature/expiry/subject/auth-time |
| Session fixation | pre-login browser state becomes authenticated authority | create a fresh server session after recent verified authentication; pre-auth state carries no account authority |
| Session theft | copied cookie reused | Secure/HttpOnly host cookie, finite lifetime, revocation-aware protected routes, high-risk reauthentication, global revocation path |
| CSRF | forged state-changing browser request | explicit CSRF token/equivalent server check on unsafe cookie-authenticated requests; Origin/Referer defense in depth |
| IDOR / elevation | parent A supplies parent B device ID/ClientID | derive parent identity from verified server session and enforce server-side ownership on every operation; ClientID never authorization |
| Provider outage | Firebase unavailable during login/revocation check | no new/uncertain account authority; account-only fail closed; accountless core remains independently available |
| Token leakage | raw provider/session tokens leak to logs/storage | no token persistence in product data/logs/analytics/URLs; server-side credential isolation |
| Privacy overcollection | provider profile becomes product profile | persist only fields later proven necessary by approved schema; no default email/photo/display-name retention |
| Availability coupling | optional auth failure breaks public/core journey | architecture boundary forbids auth dependency on accountless core routes |

## 5. Browser sign-in architecture

### 5.1 Initialization and persistence

Use the Firebase JS SDK only for the short-lived sign-in exchange. Initialize/set Firebase Auth persistence to **in-memory / NONE** before sign-in.

Reason:

- Firebase’s browser default is persistent local storage unless changed;
- current TSK-0353 explicitly prohibits using Firebase browser persistence as the application session in the server-cookie architecture;
- the server cookie becomes the only ordinary application bearer session after exchange.

After successful server-session creation, sign out/clear the browser Firebase user state as required by implementation so a persistent Firebase client session is not accidentally retained.

Do **not** use Firebase’s preview `browserCookiePersistence` as the production application session for Version 1; the current Firebase JS reference labels that API Public Preview. The accepted server session is the stable Admin-SDK session-cookie mechanism governed by TSK-0353.

### 5.2 Google provider and interaction method

- Enable only `GoogleAuthProvider` initially.
- Request no extra Google OAuth scopes unless a later approved requirement proves necessity. The product does not need contacts, calendar, Drive or other Google API access for authentication.
- Desktop-capable browsers may use `signInWithPopup` where it passes the approved UX/device matrix.
- Mobile/redirect UX may use `signInWithRedirect` **only with one of Firebase’s current documented production-safe redirect configurations** for browsers that block third-party storage (for example an approved same-domain/proxy/custom-auth-domain pattern appropriate to the final hosting design).
- The exact popup/redirect choice is an implementation/device-compatibility decision subordinate to this security architecture; neither method may introduce a second persistent browser auth store.
- Account-collision/ambiguous-provider errors fail closed. Do not silently merge identities by matching email.

## 6. Session-exchange contract

Define one dedicated HTTPS endpoint, conceptually `POST /api/auth/session` (exact route name may be adjusted during implementation without changing this ADR), with this contract:

1. Accept only the expected Firebase ID token and CSRF/request-integrity material; reject unrelated body fields.
2. Apply request size/content-type and abuse/rate controls from current NFRs.
3. Verify the Firebase ID token server-side with the Admin SDK for the configured Firebase project.
4. Require valid signature/key, expected project `aud`, expected issuer, non-empty UID/subject, valid expiry/time claims and `auth_time` not older than 5 minutes.
5. Use revocation-aware verification for session establishment.
6. Create a Firebase session cookie with configured maximum age <=7 days (within Firebase’s current 5-minute-to-2-week supported range).
7. Set the application cookie as `Secure; HttpOnly; SameSite=Lax; Path=/`, no Domain attribute, with `__Host-` prefix when deployment permits.
8. Do not return the cookie value or provider token in JSON, logs, analytics or error details.
9. Clear/replace any previous application session so authentication cannot inherit prior bearer authority.
10. Return only minimal success/failure state needed by the UI.

No parent/device ownership record is created merely because Firebase authentication succeeded. First-account persistence remains a separate downstream operation under the approved data/ownership model.

## 7. Protected-route and authorization contract

Every account-only request must:

1. obtain identity only from the verified server session;
2. verify session signature/expiry/claims and revocation under the current TSK-0353 baseline;
3. reject disabled/deleted/revoked/invalid sessions;
4. perform explicit server-side resource authorization after authentication;
5. derive the current parent identity from the verified provider/session-to-parent mapping, never from a request-supplied parent ID;
6. never treat Firebase UID, email, device ID, AdGuard ClientID, possession of a profile/configuration URL, or dashboard record existence as sufficient ownership/protection evidence;
7. expose generic unauthorized/not-found behavior sufficient to avoid cross-parent information disclosure;
8. keep account/dashboard state separate from technical Protection Map verification state.

## 8. Session lifetime, logout, reauthentication and revocation

### 8.1 Ordinary session

- absolute maximum Version-1 server-session lifetime: **7 days**;
- shorter deployment setting is allowed without reopening this ADR;
- ordinary activity does not silently slide/extend the lifetime;
- expired session routes the user to optional reauthentication while the accountless core remains available.

### 8.2 Recent authentication

Require `auth_time <= 5 minutes` at least for:

- initial server-session creation;
- account deletion;
- provider/account linking or identity-transfer functionality if later authorized;
- security-sensitive ownership recovery/transfer;
- other operations classified high-risk by the owning downstream contract.

### 8.3 Logout vs global revocation

**Current-browser logout:**

- clear the application session cookie immediately;
- clear Firebase client in-memory state;
- do not claim all other sessions are revoked;
- do not delete account/device/DNS state.

**Global/security revocation:**

- call Firebase Admin refresh-token revocation for the UID when the owning operation requires global invalidation;
- protected-route revocation-aware verification must reject the affected session thereafter;
- account disable/delete and security-compromise response use the global path;
- if revocation outcome is ambiguous because the provider is unavailable, fail account authority closed or mark the lifecycle operation pending reconciliation; do not display terminal success without evidence.

Firebase documents that revocation checking adds a network request to session verification. The baseline accepts this cost because TSK-0353 explicitly requires revocation-aware protected routes. A future bounded revocation cache or different architecture requires security evidence for its maximum stale-authorization window before replacing this baseline.

## 9. Provider outage and degraded-mode architecture

| Condition | Accountless core | New sign-in/session | Existing account route | Mutation / high-risk action | User truth |
| --- | --- | --- | --- | --- | --- |
| Firebase healthy | available if its own dependencies are healthy | allowed after all checks | allowed after session + ownership checks | allowed after all relevant checks | normal |
| Google/Firebase sign-in unavailable | **must remain available** | unavailable | existing route only if current server verification contract can prove authority | fail closed if authority/revocation cannot be proven | “Account sign-in temporarily unavailable”; no protection-state change |
| Revocation check unavailable/ambiguous | **must remain available** | no uncertain authority | fail closed under current baseline | fail closed | account function unavailable/uncertain; never claim revoked/authorized without proof |
| Firebase user disabled/deleted/revoked | **must remain available** | deny | deny/clear session | deny | reauthenticate/support as appropriate; no DNS-state inference |

Provider failure must never fall back to a shared password, public AdGuard admin access, a request-supplied parent ID, ClientID possession, or automatic accountless-to-account linkage.

## 10. Firebase/Identity Platform plan boundary

### 10.1 Initial plan

Freeze **base Firebase Authentication on Spark** for the initial optional Google-account route because the current official pricing sources support social Authentication on Spark without a payment method and current requirements do not require an Identity Platform-only capability.

Do not activate:

- Identity Platform upgrade;
- Blaze billing solely for authentication;
- phone/SMS auth or SMS MFA;
- SAML/OIDC;
- local/password authentication.

This is a planning/architecture selection, not a Firebase-console action.

### 10.2 Mandatory re-review / migration triggers

Reopen TSK-0356 and/or the applicable vendor/privacy/security/architecture authority before relying on the current provider pattern if any of these occurs:

1. Google social sign-in is no longer supported on the intended Firebase/Spark path;
2. Firebase Authentication pricing or Spark/no-cost status materially changes;
3. Identity Platform becomes necessary for an owner-approved security/feature/SLA/support requirement;
4. actual usage approaches a current provider quota/abuse boundary or provider throttling becomes material;
5. phone/SMS/MFA, SAML/OIDC or another provider is proposed;
6. Firebase Authentication processing location changes from the current US-only statement;
7. legal/privacy authority determines the US processing/transfer or vendor arrangement is unacceptable/unresolved for the intended real-user market;
8. Firebase/Google terms, DPA/security terms, material subprocessors or service-specific obligations change materially;
9. provider outage/revocation latency/availability prevents the accepted account-only NFR while the accountless-core separation cannot be preserved;
10. session-cookie/Admin SDK behavior, supported algorithms/claims or relevant API is deprecated or materially changes;
11. provider identity export/migration/deletion constraints prevent the approved lifecycle/recovery model;
12. a new billing/payment/contract/material-spend commitment becomes necessary outside current owner authority.

A trigger causes review, not an automatic provider migration. Migration must preserve the internal ownership boundary and must not silently merge accounts by email or resurrect deleted/revoked authority.

## 11. Data, privacy and legal boundaries

Current official Firebase privacy documentation says Firebase Authentication is US-only. This is an **architecture/privacy input**, not legal acceptance.

Therefore:

- keep account data minimum and provider-independent where practical;
- store only the accepted provider identity reference plus later-approved minimal parent/device lifecycle fields;
- do not persist Google access tokens or request extra Google API scopes for authentication;
- do not persist provider profile fields merely because Firebase exposes them;
- keep accountless J0/J1 state unlinked from account identity unless a later explicitly approved operation with a defined purpose authorizes a bounded transfer;
- no browsing/query/activity history enters Firebase Authentication or the application account model;
- the owner-deferred legal/ICO/UK-representation/DPIA-LIA completion remains unresolved and is not bypassed by this architecture PASS.

## 12. Secrets and operational configuration

Implementation must keep:

- Firebase Admin credentials/service identity server-side only and outside Git;
- OAuth/provider configuration and authorized domains/redirects limited to exact deployment needs;
- secrets/tokens out of browser-readable configuration except vendor-defined public Firebase web configuration fields that are explicitly designed to be public and are not authorization secrets;
- session cookie values, ID tokens, refresh tokens and OAuth access tokens out of logs/evidence/analytics;
- errors generic to the client while retaining privacy-safe operational diagnostics;
- production origins/redirects and cookie security settings versioned/configured through the accepted deployment path.

No service-account key file is required by this ADR; use the least-secret/least-privilege supported server identity mechanism available in the final deployment environment. Any static credential introduced later must be separately controlled and rotated.

## 13. Verification obligations for L6

Before any later implementation can claim the architecture is correctly realized, tests must cover at least:

1. Google sign-in success/cancel/provider/network/ambiguous-account cases;
2. in-memory Firebase client persistence and absence of auth bearer values from localStorage/sessionStorage/application logs;
3. ID-token wrong-project/wrong-issuer/expired/malformed/revoked/disabled-user failures;
4. recent-auth requirement for session creation/high-risk actions;
5. session-cookie Secure/HttpOnly/SameSite/host/lifetime properties;
6. CSRF negative cases on session exchange and every unsafe cookie-authenticated route;
7. expired/revoked/deleted/disabled session denial;
8. cross-parent/IDOR tests for every device/resource-reference class;
9. current-browser logout distinct from global revocation;
10. provider/revocation-check outage with accountless-core continuity and account-only fail-closed behavior;
11. no browsing/query/activity history or unnecessary provider profile/token storage;
12. account deletion/revocation partial-failure/reconciliation behavior once those downstream contracts exist;
13. popup/redirect behavior on the approved browser/device matrix, including Firebase’s current third-party-storage requirements for redirect flows.

## 14. Alternatives considered and rejected for Version 1

| Alternative | Current disposition | Reason |
| --- | --- | --- |
| Mandatory login before core setup | Rejected | conflicts with accountless-first owner authority and CON-0010 |
| Local email/password auth | Rejected | unnecessary credential/password lifecycle and not approved scope |
| Phone/SMS auth or SMS MFA | Rejected initially | separate cost/processing/abuse surface; no current requirement |
| Identity Platform upgrade at inception | Deferred | no current feature/scale requirement justifies upgrade; introduces different limits/plan boundary |
| Persist Firebase browser auth in localStorage as the app session | Rejected | conflicts with accepted server-session security contract |
| Client-only Firebase auth as resource authorization | Rejected | authentication is not ownership authorization; IDOR boundary must be server-side |
| Direct Google token as device/AdGuard authority | Rejected | provider identity is not device ownership or technical protection evidence |
| Longest available 2-week session | Rejected | current NFR freezes a stricter <=7-day Version-1 maximum |
| Revocation-unaware protected routes | Rejected under current baseline | conflicts with TSK-0353; a future cache needs explicit stale-authorization evidence |
| Silent merge/link by email | Rejected | mutable/non-authoritative identity key; cross-account risk |
| Firebase preview browser-cookie persistence as production session | Rejected | preview API is not needed; stable server Admin-SDK cookie model is already selected |

## 15. ACC-0356 trace

| ACC-0356 requirement | Evidence | Disposition |
| --- | --- | --- |
| Selects base Firebase Authentication Spark | Sections 1, 3, 10 | SATISFIED |
| Google provider | Sections 1, 5 | SATISFIED |
| no Identity Platform upgrade/SMS initially | Sections 1, 10, 14 | SATISFIED |
| server-validated identity | Sections 6–7 | SATISFIED |
| secure server-managed session cookie | Sections 1, 6–8 | SATISFIED |
| dated pricing evidence | Sections 2.2–3; current 2026-09-02 official Firebase pricing sources | SATISFIED |
| quota evidence | Sections 2.2–3, 10.2; official auth/limits sources | SATISFIED |
| term/location evidence | Sections 2.2–3, 11; current Terms/privacy sources | SATISFIED, with legal acceptability explicitly unresolved |
| provider outage behavior | Section 9 | SATISFIED |
| revocation behavior | Sections 7–9 | SATISFIED |
| migration/review trigger | Section 10.2 | SATISFIED |

## 16. Candidate stable disposition

**Candidate ACC-0356 = PASS**, subject to current VER-0356 read-back/reviewer inspection of this exact artifact and durable runtime synchronization.

The candidate PASS means the initial authentication and server-session architecture is selected and evidence-backed at the L5 design boundary. It does **not** mean Firebase/Google has been configured, legal/privacy transfer readiness is approved, user identity data has been processed, any paid plan is activated, implementation tests have run, LG-07 has passed, or L6 build is authorized.
