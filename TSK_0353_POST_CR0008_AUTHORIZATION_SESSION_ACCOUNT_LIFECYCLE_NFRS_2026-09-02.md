# TSK-0353 — Post-CR-0008 Authentication, Authorization, Session and Account-Lifecycle NFRs

**Task:** TSK-0353 — Define authentication, authorization, session and account-lifecycle NFRs  
**Acceptance / Verification / Evidence:** ACC-0353 / VER-0353 / EVD-0353  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0353, durable EVD-0353 publication, guarded runtime reconciliation and exact read-back.

## 1. Current authority and scope boundary

TSK-0353 depends exactly on current PASS predecessors TSK-0230 and TSK-0484.

Current Version-1 authority remains dual-mode:

- the complete core SafeWeb setup, verification, Protection Map, troubleshooting, recovery and removal path remains usable without login;
- an optional parent account, secure session, minimum parent/device ownership persistence and lightweight dashboard/device management are in scope;
- mandatory login for core value, child accounts, browsing/query/activity history, unrestricted customer DNS administration and identity-based protection claims remain prohibited.

This task defines **security NFRs only**. It does not activate Firebase/Google, choose a commercial plan, create users, implement cookies/endpoints/datastores, create AdGuard ClientIDs, process real participants, establish legal compliance or infer architecture/build/release/gate PASS.

The planned initial Google/Firebase route remains conditional on its later vendor/privacy/security/architecture and implementation gates. These NFRs specify the security contract that any accepted implementation of that route must prove.

## 2. Current authoritative inputs

Project-private inputs:

- `TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFRS_2026-09-01.md`, version `1.0.1-post-CR-0008`, blob `eda85b062a3a7ba29544de35a8a813c9790092f2`;
- `TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `285ee390499190137e8aac0fed976975fb79ed80`;
- current TSK-0044 AdGuard API/credential/failure NFR revalidation, blob `9e2df58093c592621eb1531dc1c34393a247dd80`, as a compatible downstream-interface/failure constraint but **not** a hard dependency.

Current first-party / security-source review on 2026-09-02:

1. Firebase, **Verify ID Tokens** — `https://firebase.google.com/docs/auth/admin/verify-id-tokens` — backend verification of signature/format/expiry and Firebase project/issuer/subject claims; ordinary `verifyIdToken` does not itself prove revocation unless revocation checking is requested.
2. Firebase, **Manage Session Cookies** — `https://firebase.google.com/docs/auth/admin/manage-cookies` — server-created session cookies, 5-minute to 2-week supported expiry range, `HttpOnly`/`Secure` policy, CSRF protection, recent-`auth_time` checks, server verification and revocation handling.
3. Firebase, **Manage User Sessions** — `https://firebase.google.com/docs/auth/admin/manage-sessions` — ID tokens are short-lived, refresh tokens are long-lived until defined invalidation/revocation conditions, and Admin SDK revocation/check-revoked mechanisms exist.
4. Google Identity Services, **Verify the Google ID token on your server side** — `https://developers.google.com/identity/gsi/web/guides/verify-google-id-token` — server must validate GIS CSRF token, signature, `aud`, `iss` and `exp`; use immutable `sub` rather than email as the unique Google account key.
5. OWASP Session Management Cheat Sheet — `https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html` — `Secure`, `HttpOnly`, explicit `SameSite`, fixation prevention, strict server-side session handling and reauthentication after high-risk events.
6. OWASP IDOR Prevention / Authorization guidance — server-side object authorization on every operation; random/opaque identifiers are defense in depth, never authorization.

These sources define current engineering facts; they do not activate a provider or create legal authority.

## 3. Identity-provider and token-verification NFRs

### 3.1 Firebase Authentication ID-token path

When the accepted implementation uses Firebase Authentication as the application identity layer:

1. the browser may send a freshly issued Firebase ID token **only to the dedicated HTTPS session-exchange endpoint**;
2. the backend verifies the token using the Firebase Admin SDK or an equivalently correct approved verifier before creating account authority;
3. verification must reject malformed, unsigned, wrong-algorithm/key, expired, wrong-project/audience, wrong-issuer or empty-subject tokens;
4. expected Firebase claims are checked consistently with the exact project: `aud` = approved Firebase project ID, `iss` = `https://securetoken.google.com/<projectId>`, non-empty `sub`/UID, valid signature/key and non-expired `exp`; `iat`/`auth_time` must not be in the future;
5. session establishment requires a **recent authentication**: `now - auth_time <= 5 minutes`; otherwise the user reauthenticates before a server session is issued;
6. session creation and consequential security-sensitive operations use revocation-aware verification (`checkRevoked=true` or an independently accepted mechanism with equal or stronger revocation truth);
7. disabled/deleted/revoked/invalid users/tokens fail closed and establish no account authority;
8. raw ID tokens, refresh tokens, provider access tokens and service-account credentials are never stored in product/account records, localStorage/sessionStorage, analytics, ordinary logs or evidence.

The Firebase UID/provider subject is identity input only. It is not device ownership, AdGuard authorization or technical protection evidence.

### 3.2 Direct Google Identity Services ID-token path

If a future accepted implementation receives a Google Identity Services ID token directly rather than only a Firebase ID token:

1. the server validates the GIS double-submit `g_csrf_token` before consuming the credential POST;
2. production validation uses a Google-supported client library or equivalently correct JWT verifier, not unverified token decoding;
3. signature, `aud`, `iss` and `exp` are validated; audience must match an approved application client ID and issuer must be Google’s accepted issuer;
4. `sub` is the unique provider identity key; email is **not** an ownership/authorization key because it may change;
5. `hd` is checked only if a separately approved product rule restricts access to a Google Workspace domain; no such restriction is created here;
6. a direct Google token never authorizes a device/AdGuard operation by itself; it must first enter the accepted server-side account/session/ownership model.

No automatic account merge/link is allowed solely because two provider identities share an email address.

## 4. Minimum identity and account persistence

TSK-0230 D14-D16 remains controlling.

The minimum persistent parent/account domain may contain only the fields required by the accepted downstream schema, such as:

- opaque internal parent ID;
- immutable approved provider subject/UID reference;
- minimum account lifecycle state (`active`, `deleting`, `disabled` or equivalent bounded enum);
- minimum server-session/revocation metadata;
- opaque parent-owned device identifiers and minimum device lifecycle/settings fields accepted by their owning contract.

Default exclusions:

- no child identity/profile;
- no browsing/DNS query/domain/URL history;
- no accountless J0/J1 history/linkage;
- no raw provider token, refresh token, session cookie or OAuth credential in the product record;
- no marketing profile, behavioral timeline or cross-device activity graph;
- email/display name/photo are not persisted merely because a provider supplied them; any field requires an explicit necessary purpose and TSK-0230 inventory entry.

Accountless J0/J1 state is never silently converted/promoted/copied into account state. Sign-in cannot extend anonymous retention.

## 5. Server-session cookie contract

### 5.1 Cookie properties

The Version-1 server session uses one host-scoped cookie with these minimum properties unless a later evidence-backed architecture proves a stronger equivalent:

- `Secure` — mandatory;
- `HttpOnly` — mandatory;
- explicit `SameSite=Lax` baseline; `Strict` is allowed when full sign-in/navigation compatibility is independently proven;
- `Path=/`;
- no `Domain` attribute for the primary host-scoped session;
- prefer the `__Host-` cookie-name prefix when the deployed host/path model permits it;
- never `SameSite=None` for the ordinary parent session;
- never expose the bearer session value to JavaScript, URLs, query strings, fragments, telemetry or logs.

`SameSite` is defense in depth and never replaces CSRF protection.

### 5.2 Lifetime and creation

- absolute session lifetime: **maximum 7 days** for Version 1; implementations may choose a shorter duration;
- no sliding extension merely because the dashboard is used;
- new session creation requires the <=5-minute recent-authentication check above;
- a new authenticated session replaces/clears any pre-auth/session candidate so session fixation cannot carry authority across the login boundary;
- the browser must not persist Firebase auth state in localStorage/sessionStorage when the server-session-cookie pattern is used; client persistence is `NONE` or an equivalent non-persistent mode after exchange.

Seven days is an internal security/product maximum inside Firebase’s supported session-cookie range, not a legal retention rule or customer SLA.

### 5.3 Protected-route verification

Every account-only server route:

1. reads identity only from the server-verified session, not a request-supplied parent ID;
2. verifies cookie validity/signature/expiry and required claims;
3. denies expired/invalid/revoked/disabled/deleted sessions;
4. baseline Version 1 uses revocation-aware verification on protected routes. Any future revocation cache requires separate evidence that its maximum stale-authorization window is bounded and accepted;
5. authorizes the requested resource/action independently after authentication.

Provider or revocation-check outage may make account-only routes unavailable, but cannot make the independently healthy accountless core unavailable.

## 6. CSRF and request-integrity contract

1. Safe HTTP methods (`GET`, `HEAD`, `OPTIONS`) do not mutate account/device/session state.
2. The GIS credential POST validates the provider’s double-submit `g_csrf_token` before token use when that direct GIS flow is applicable.
3. Every cookie-authenticated unsafe request (`POST`, `PUT`, `PATCH`, `DELETE`) uses an effective server-validated CSRF token or an independently accepted stronger equivalent.
4. CSRF tokens are high-entropy, bound to the intended session/origin, compared safely and never placed in URLs/logs/analytics.
5. `Origin` and, where needed, `Referer` validation are defense in depth for unsafe browser requests; absent/mismatched origins fail closed where the route is browser-only.
6. JSON/content-type constraints and CORS do not replace CSRF authorization.
7. SameSite does not replace the CSRF token.
8. Cross-site forged create/update/unlink/revoke/delete/account-delete/session operations must produce zero authorized effect.

## 7. Authorization and parent-to-device ownership / IDOR prevention

Authentication is not authorization.

For **every** account/device operation — read, list, create/register, update/rename/settings change, unlink, revoke, delete, replace, export if ever added, recovery and any AdGuard-backed operation — the server must:

1. derive current `parent_id` from the verified server session;
2. treat any request-supplied account/device/ClientID/reference only as an object candidate, never as authority;
3. load the target from a dataset already scoped to the authenticated parent or perform an equivalent explicit ownership check;
4. deny by default if ownership, lifecycle state or authorization is missing/ambiguous;
5. re-check authorization for each consequential operation even if the object was authorized earlier in the flow;
6. never authorize via obscurity/UUID entropy/ClientID possession;
7. never disclose whether another parent’s object exists beyond the minimum generic error boundary;
8. emit zero unauthorized data/effect on cross-parent negative cases.

Mandatory negative acceptance fixture: at least two independent synthetic parent accounts A/B and devices A1/B1. A must fail to read/update/unlink/revoke/delete/recover B1 by substituting every visible/internal object-reference class, and B must equivalently fail against A1.

AdGuard ClientID remains a server-side routing/control reference governed by TSK-0352/TSK-0044 and is never an authorization token or protection evidence.

## 8. Session fixation, theft and account-takeover controls

1. Successful login creates a new server session; pre-auth session state does not retain authenticated authority.
2. Session cookie values are not accepted if they were not generated by the accepted server/provider session mechanism.
3. High-risk operations require **recent authentication <=5 minutes**: account deletion, provider/account-link change if later added, security-sensitive ownership recovery/transfer, and any operation that would expose/replace account authority.
4. Device rename/settings changes may rely on a valid non-recent session only when ownership is freshly authorized and the operation is not classified high risk by its owning contract.
5. Provider subject/UID is the account identity anchor. Email/display name is never sufficient to link, recover, merge or transfer ownership.
6. Suspected token theft, explicit security revocation, account disable/delete or provider-reported major account change triggers session invalidation/re-authentication before further account authority.
7. No local password, password-reset credential or SMS authentication factor is introduced by this Version-1 NFR. Adding one reopens this contract.
8. MFA is not claimed as current Version-1 functionality. A later risk/gate may require it; absence of MFA cannot be silently presented as MFA protection.

## 9. Logout, revocation and session terminal truth

### 9.1 Current-browser logout

A current-browser logout:

- clears the host session cookie immediately;
- leaves the accountless product route available;
- does not claim that a copied session elsewhere was revoked unless server/provider revocation proves it;
- does not claim device/DNS removal or account deletion.

### 9.2 Global/security revocation

`Sign out all sessions`, security response, account disable and account deletion use provider/server revocation sufficient to make existing authenticated sessions fail subsequent protected-route verification. Under the current Firebase pattern this includes refresh-token revocation and revocation-aware session verification.

Because provider-wide refresh-token revocation affects all sessions, product copy/behavior must not silently represent that action as current-browser-only logout.

### 9.3 Failure truth

If provider revocation is ambiguous/unavailable, the account operation is `pending/uncertain` and account-only authority is blocked or restricted according to the owning lifecycle state until reconciliation. No terminal revocation success is shown from an API acknowledgement alone.

## 10. Account deletion lifecycle NFR

Account deletion is a high-risk, multi-domain operation and requires recent authentication <=5 minutes.

The implementation contract must provide one durable/reconstructable deletion operation state without retaining deleted content. At minimum:

1. accept a recent-authenticated delete request and create an opaque operation ID;
2. transition the account to `deleting` (or equivalent) so no new ownership-changing operations start;
3. invalidate/revoke active account sessions according to the accepted provider/server mechanism;
4. enumerate only the authenticated parent’s owned device records server-side;
5. invoke accepted device/ClientID unlink/revoke/delete/reconciliation semantics when TSK-0352 and implementation authority exist;
6. delete/minimise local parent/device/session state under TSK-0230;
7. delete/disable the provider identity if that is part of the accepted architecture and current operation scope;
8. read back each required domain and classify `complete`, `pending_reconciliation`, or `failed_safe`;
9. never claim physical DNS/profile removal merely because the account/device record was deleted;
10. never resurrect deleted account/device authority through backup, retry, reinstall or provider return.

Any minimal deletion/reconciliation completion evidence follows TSK-0230 D25: opaque operation/time/result/scope/version only, no deleted payload, with exact retention required before implementation processing is enabled.

## 11. Provider/datastore outage and recovery semantics

### Provider unavailable / invalid response

- no new account session is established;
- no failed provider response is treated as identity proof;
- existing protected routes that cannot prove valid/non-revoked authority fail closed;
- UI may state the optional account is temporarily unavailable and route to the complete accountless core;
- accountless setup/verify/Protection Map/recovery/removal stays usable when its independent dependencies are healthy;
- no fallback to shared credentials, anonymous persistent ClientID mutation or public AdGuard control.

### Ownership datastore unavailable / ambiguous

- no ownership-changing device/AdGuard operation proceeds without authoritative ownership state;
- stale cache is not authority for consequential mutation;
- account/dashboard reads degrade truthfully rather than disclosing cross-parent/stale data;
- ambiguous partial writes reconcile before retry;
- provider success alone cannot make a datastore/ownership failure successful.

### Recovery

Recovery does not bypass authentication/authorization. Restored account/device state must be ownership-correct, must not resurrect revoked/deleted sessions/devices, and must remain separate from accountless J0/J1 state and technical protection evidence.

## 12. Rate-limit and abuse-control NFRs

These are provisional Version-1 ceilings intended to make ACC-0353 measurable; implementation may tighten them, while materially relaxing them requires evidence-backed security review.

| Surface | Initial ceiling | Keying / privacy rule | Failure behavior |
|---|---:|---|---|
| Session/token exchange | 10 attempts / 5 min per ephemeral network bucket; after verified identity, 5 attempts / 5 min per provider subject | network key is memory/short-TTL keyed hash, not durable raw-IP analytics; provider key stays security-only | HTTP 429 + bounded retry hint; generic response; accountless route remains available |
| CSRF/token-invalid session creation failures | 10 / 5 min per network bucket | no raw token/body logging | 429 after ceiling; never reveal account existence |
| Cross-parent/object authorization denials | 20 / 5 min per authenticated parent plus bounded network bucket | security counter only; no object-name/content payload | throttle account-only operations and emit privacy-safe security event |
| Device ownership mutations | 30 / 5 min per authenticated parent | parent ID used only inside restricted authorization/rate limiter, not analytics | 429; no mutation after limit |
| Account deletion / global session revocation | 5 attempts / hour per authenticated parent | recent-auth required; no email/raw provider token in limiter | fail closed; require reauth/retry after window |

Rate limiting never proves authorization, never substitutes for CSRF, and never becomes a durable behavioral profile. Distributed deployment, if later introduced, must preserve these semantics through an accepted shared limiter without expanding personal-data retention.

## 13. Privacy-safe authentication/security audit events

Security/operational events are **not product analytics** and cannot reuse TSK-0497 KPI authority silently.

Allowed event classes, only when the implementation has a documented TSK-0230 data-inventory row and exact bounded retention:

- `auth_session_created`;
- `auth_session_rejected` with bounded reason class (`invalid`, `expired`, `revoked`, `csrf`, `provider_unavailable`);
- `auth_session_revoked`;
- `auth_logout_completed`;
- `authz_denied` with bounded operation class;
- `auth_rate_limited` with bounded surface class;
- `account_deletion_started`;
- `account_deletion_terminal` with bounded terminal class;
- `provider_dependency_state` with bounded dependency/outcome class.

Allowed fields are restricted to what the security purpose actually needs, for example:

- event name/time;
- deployment/auth-contract version;
- bounded route/operation/reason/outcome class;
- opaque correlation/deletion-operation ID where necessary;
- optional opaque internal parent security reference only when investigation/enforcement cannot be performed without it and TSK-0230 explicitly permits it.

Never log/store in these events:

- raw Firebase/Google ID token, refresh token, session cookie, OAuth access token, CSRF secret or service credential;
- email/name/photo/provider profile payload;
- raw IP as product/security analytics;
- AdGuard admin secret or raw ClientID unless a separately necessary restricted reconciliation record requires it;
- DNS query/qname/domain/URL/browsing/search/child-activity history;
- request bodies, arbitrary free text or support transcripts.

**Retention fail-closed rule:** TSK-0353 does not invent a legal/security retention period. Before a security event is durably stored, the implementation/data inventory must set the exact necessary bounded retention and deletion mechanism under TSK-0230 D24/D25. Undefined retention means durable collection is blocked. Short-lived in-memory rate-limit buckets expire at their explicit window and are not audit history.

## 14. Protection-state separation

The following facts never produce or strengthen technical `protected_verified` state:

- valid Google/Firebase identity;
- valid server session;
- account presence;
- device ownership;
- dashboard presence;
- stored ClientID/profile/configuration;
- parent confirmation.

Protection-state truth remains owned by the current Protection Map/evidence contract. Authentication and authorization only decide access to account/device functions.

## 15. Deterministic acceptance test catalogue

A future implementation must be able to prove at least these assertions:

1. malformed/expired/wrong-project/wrong-issuer Firebase token is rejected;
2. revoked Firebase token/session is rejected where revocation-aware verification is required;
3. session cannot be issued when `auth_time` exceeds the recent-auth window;
4. direct GIS flow rejects missing/mismatched `g_csrf_token`;
5. direct Google token rejects wrong signature/audience/issuer/expiry;
6. email alone cannot link/merge/recover/authorize an account;
7. Firebase/provider token is absent from localStorage/sessionStorage after session exchange;
8. session cookie is `Secure`, `HttpOnly`, explicit SameSite, Path `/`, host-scoped and absent from URLs/logs;
9. session lifetime is <=7 days and non-sliding;
10. login replaces pre-auth authority and prevents session fixation;
11. unsafe cookie-authenticated requests fail without valid CSRF protection;
12. cross-site forged state-changing requests have zero effect;
13. expired/invalid/revoked/disabled session cannot access protected routes;
14. Parent A cannot read Parent B account/device data by reference substitution;
15. Parent A cannot update/unlink/revoke/delete/recover Parent B device by reference substitution;
16. ClientID/opaque identifier possession alone cannot authorize an operation;
17. ownership authorization is rechecked for each consequential operation;
18. provider outage establishes no new account authority;
19. provider outage does not disable the independently healthy accountless core;
20. datastore outage prevents ownership-changing mutation and leaks no cross-parent state;
21. ambiguous datastore/control mutation reconciles before retry/success;
22. current-browser logout clears the cookie and makes that browser unauthenticated;
23. global/security revocation causes old sessions to fail protected-route verification;
24. account deletion requires recent authentication;
25. account deletion cannot claim DNS/profile removal unless separately verified;
26. backup/restore cannot resurrect deleted/revoked account/device/session authority;
27. rate limits engage at the defined ceilings without exposing account existence;
28. security events contain no token/cookie/email/DNS-history/free-text secret payload;
29. undefined security-event retention blocks durable collection;
30. authentication/account/device presence never produces technical `protected_verified`.

## 16. Change-control / reopen triggers

Reopen affected TSK-0353 evidence before relying on any material change to:

- identity provider or Firebase project/client IDs;
- token type/issuer/audience/verification library;
- session cookie format, lifetime, domain/path/SameSite policy or browser storage model;
- revocation behavior or revocation-cache design;
- account linking/merge/recovery mechanism;
- local password/SMS/MFA/passkey addition;
- parent/device ownership model;
- ClientID authorization relationship;
- CSRF/CORS/origin model;
- rate-limit ceilings/keying/store;
- security-event fields/retention/recipient;
- account deletion/revocation terminal semantics;
- provider/datastore outage fallback;
- anonymous-to-account data transfer/linkage;
- any mechanism that makes login mandatory for core value.

## 17. Acceptance disposition

The current candidate covers the full ACC-0353 boundary:

- Firebase/Google token verification;
- secure `HttpOnly` / `Secure` / explicit `SameSite` server session cookies;
- CSRF prevention;
- revocation/session fixation/account-takeover controls;
- parent-to-device ownership and IDOR prevention;
- measurable rate limits;
- truthful logout/revocation/account deletion;
- provider/datastore outage with accountless fallback;
- privacy-safe security audit events;
- strict separation of identity/ownership from Protection Map evidence.

No implementation/provider activation, legal-compliance conclusion, participant processing, market activation, release/gate or successor PASS is inferred.

**ACC-0353 current result candidate: PASS pending independent VER-0353, durable EVD-0353, guarded runtime reconciliation and exact GitHub read-back.**
