# TSK-0487 — Anonymous Journey and Public Application Threat Model

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Task:** TSK-0487  
**Acceptance:** ACC-0487 / VER-0487 / EVD-0487  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Authority:** DEC-0054 / CR-0007 + DEC-0055 / CR-0008; A3 / AUTO_ALLOWED  
**Status represented:** PASS CANDIDATE pending independent security-contract verification and canonical read-back. No implementation, penetration-test, production, user, or later-gate PASS is inferred.

## 1. Security decision

The complete UseSafeWeb core must remain usable without login. Anonymous access is therefore treated as a deliberate product/security boundary, not an exception to security.

Use these principles:

1. **No identity requirement for core value.** Abuse controls must not silently turn anonymous setup into mandatory authentication.
2. **Opaque capability/state references only.** Browser-controlled identifiers never imply authorization, ownership, verification, or backend object identity.
3. **Minimize anonymous server state.** Prefer J0 browser/session state; if J1 is required, use an unguessable opaque token, hard non-sliding expiry of at most 24 hours, narrow purpose, early deletion, and no automatic linkage to persistent account state.
4. **Every public endpoint is an untrusted boundary.** Validate method, media type, size, shape, enum/range, origin where applicable, and server-side authorization/capability before work with side effects or cost.
5. **Separate public product endpoints from administration.** Browser traffic can never proxy or select arbitrary AdGuard `/control/*`, datastore administration, filesystem paths, internal URLs, or privileged operations.
6. **Bound resource consumption before expensive work.** Rate, concurrency, payload, response, timeout, retry, and downstream-call budgets must be enforced without collecting a persistent browsing/identity profile.
7. **Truthful verification.** A verification endpoint proves only the current supported technical fact it actually observed and returns a bounded product state; it never exposes raw DNS/query/admin data or turns a client-supplied ID into proof.
8. **Fail closed on integrity/authorization ambiguity.** Invalid, expired, replayed, malformed, cross-session, cross-origin, over-budget, or ownership-ambiguous requests fail without mutation.

This model is derived from the accepted TSK-0354 architecture, the TSK-0229 accountless data contract, `REQ-0055`, `REQ-0059`, `CON-0009`, `INT-0012`, and `INT-0015`.

## 2. Assets to protect

| Asset | Security objective |
|---|---|
| Anonymous J0/J1 setup state | Confidentiality/minimization, integrity, expiry, non-linkability |
| Setup/profile/config delivery | Correct artifact for the intended flow; no arbitrary profile generation or secret exposure |
| Protection-verification state | Integrity and truthful current-state semantics; no spoofing/oracle leakage |
| Optional parent session/account/device records | Server-side authorization; no cross-parent access or anonymous escalation |
| AdGuard administrative control plane | Never browser-exposed; no arbitrary proxy; least privilege |
| DNS service availability/cost | Bounded public abuse/resource consumption |
| Web/app VM and internal network | No SSRF/path/command/template injection or origin-to-admin pivot |
| Secrets/tokens/private keys | Server-only; never logs/browser/Git/error bodies |
| Privacy boundary | No browsing/query/activity history, persistent child identity, fingerprinting, or unnecessary IP retention |
| Product trust state | Parent confirmation cannot masquerade as technical verification |

## 3. Trust boundaries and entry points

### TB-A — Internet/browser → reverse proxy → Next.js public surface

Entry points include public pages, accountless start/routing, J1 creation/resume/reset if implemented, setup/profile/config delivery, Protection Map verification, self-service/support endpoints, and optional auth/session exchange.

Controls start at the reverse proxy and continue in the Route Handler/server layer. No endpoint is trusted merely because it is called by first-party browser code.

### TB-B — Anonymous browser state ↔ J1 transient server state

If J1 is implemented, the browser presents an opaque bearer-style journey token. Possession permits only the exact narrow anonymous journey operation scoped to that token. It grants no account/device ownership and no AdGuard administration authority.

### TB-C — Public app → internal application services

Public request parameters are converted to typed internal commands. Internal services never accept raw request objects, arbitrary URLs, arbitrary file paths, arbitrary AdGuard endpoint names, or dynamic command fragments.

### TB-D — Next.js server → private AdGuard control plane

Only the server-side typed AdGuard adapter may cross this boundary. The adapter uses a fixed allowlist of product operations after the required capability/session/ownership checks. ClientID/device IDs are references only.

### TB-E — Optional auth/session → persistent ownership domain

Firebase/Google auth is optional for persistent parent features only. Current official Firebase guidance supports server-created session cookies, CSRF protection during session exchange, secure/HttpOnly cookie policy, server-side verification, and revocation checks. Next.js guidance requires Route Handlers/Server Actions to be treated like public API endpoints with server-side authorization.

## 4. Threat and control matrix

| ID | Threat | Attack path | Required preventive controls | Required detection / test | Residual disposition |
|---|---|---|---|---|---|
| TM-01 | **Enumeration of J1/profile/config resources** | Guess/iterate token, numeric ID, device ID, ClientID, path, or response differences | Cryptographically strong opaque tokens with at least 128 bits of entropy; no sequential/public backend IDs; constant bounded not-found/expired response class; no token in URL where avoidable; no directory/list endpoint | Large invalid-token corpus; adjacent/structured-ID probes; response body/status/timing-size comparison within practical tolerance; verify no resource list/leak | Controlled; implementation/test required |
| TM-02 | **Replay of state-changing anonymous request** | Capture/resubmit create/confirm/config/revoke/reset operation | Explicit idempotency key or server-issued one-time/operation nonce for non-idempotent mutations; token scope binds allowed operation; state transition validates expected current version/state; duplicate request returns same safe result or deterministic rejection | Repeat exact request concurrently/sequentially; delayed replay after transition; replay after expiry/reset; prove no duplicate device/config/control mutation | Controlled; implementation/test required |
| TM-03 | **Token theft / cross-session use** | Exfiltrate J1 token through URL, logs, referrer, browser storage or another session | Prefer secure same-site cookie or protected request body/header over URL; `Secure`, `HttpOnly` where cookie is usable; `SameSite` policy appropriate to flow; `Referrer-Policy`; no token in analytics/logs; hard expiry; early reset/delete; optional token rotation after sensitive transition | Inspect browser/network/logs/referrers; reuse from clean session; reuse after reset/expiry; verify no persistent token sink | Controlled; implementation/test required |
| TM-04 | **Tampering with journey/protection state** | Change client JSON, hidden field, local storage, step state, “verified” flag, platform/device choice | Server treats all browser state as claims; allowlisted schema; server derives allowed transition; technical verification generated server-side; parent confirmation and technical verification use separate types/states | Modify every client-controlled state field; illegal transition/property injection; forged verified state; stale version; prove rejection/no privilege elevation | Controlled; implementation/test required |
| TM-05 | **Object-level authorization / cross-parent access** | Authenticated parent changes device/account ID or ClientID | Server verifies Firebase session for account-only routes; load object by `(parent_id, opaque_device_id)` or equivalent ownership scope; never authorize by ClientID alone; deny-by-default object lookup; no mass assignment | Two-account negative matrix for read/update/delete/revoke; random/known foreign IDs; stale/deleted ownership; verify 404/403 policy without leakage | Controlled; implementation/test required |
| TM-06 | **Function-level/admin escalation** | Call hidden/admin endpoint, arbitrary AdGuard route, method change, debug route | No browser-accessible generic admin proxy; fixed route allowlist; server-only admin secret; per-route method/content-type validation; production debug/admin routes disabled or separately restricted | Route inventory; method fuzz; arbitrary `/control/*` payload attempts; verify no admin credential/raw AdGuard response | Controlled; implementation/test required |
| TM-07 | **Injection** | Malformed JSON/form/header/path causes command, shell, template, header, log, query or config injection | Typed schemas; strict enums/ranges/lengths; parameterized datastore access; no shell/eval/dynamic command; fixed filesystem/network destinations; output encoding; structured logs; reject control characters in identifiers/labels where not required | Property-based/fuzz corpus; SQL/NoSQL/meta-character strings; CRLF; template/script strings; path traversal; verify no execution, query-shape change or log forging | Controlled; implementation/test required |
| TM-08 | **SSRF / internal-network pivot** | Submit URL/hostname that backend fetches, or coerce verification/profile generator into arbitrary target | Public APIs accept identifiers/enums, not arbitrary upstream/admin URLs; fixed server-side endpoint registry; no user-controlled scheme/host/port; DNS verification checks only approved UseSafeWeb endpoint/known mechanisms | localhost/link-local/private/cloud-metadata URL corpus; redirects/DNS rebinding where a fetch exists; prove request never reaches arbitrary target | Controlled; implementation/test required |
| TM-09 | **Profile/config misuse** | Mass-generate configs, alter target/client identity, distribute stale/revoked artifact, use config as cross-account control token | Config content contains no admin secret; generation requires scoped anonymous capability or authenticated ownership according to flow; immutable/explicit version metadata; short-lived download capability if sensitive; integrity validation/signing where platform format requires it; revoke/replace semantics separate from account identity | Attempt generation without capability, foreign account, expired token, tampered parameters, stale/revoked version; inspect artifact for secrets/IDs beyond contract | Controlled; implementation/test required |
| TM-10 | **Verification oracle / spoofing** | Query arbitrary identifier or submit expected result to learn status or forge Protected | Verification route accepts only supported opaque journey/device reference scoped server-side; ignores client `verified=true`; returns finite product state (`protected`/`action-needed`/`uncertain`/`not-covered` etc.) without raw backend details; no browsing/query lookup | Foreign/random ID matrix; forged success body; repeated timing/status comparison; backend unavailable/contradictory evidence test | Controlled; implementation/test required |
| TM-11 | **Anonymous denial of service / cost exhaustion** | Burst J1 creation, verification, profile generation, expensive parsing/provider calls | Reverse-proxy connection/body/time limits; endpoint-specific token-bucket/leaky-bucket rate limits; per-operation concurrency cap; hard payload/output bounds; cache/static serve cheap data; bounded downstream timeouts/retries; global circuit breaker/budget guard for expensive provider/control calls | Load/burst tests below/above threshold; concurrency saturation; slow-body/large-body; provider failure; verify intended low-volume user succeeds while abusive path is throttled/degraded | Controlled; exact thresholds are capacity-test inputs, not invented here |
| TM-12 | **Rate-limit evasion / privacy-invasive defense** | Rotate token/IP/user-agent; defense starts fingerprinting users | Combine short-lived coarse network/endpoint counters with token-specific limits and global service budget; keep counters operational/ephemeral; no stable fingerprint or marketing identity; do not persist IP as product/account field | Rotate token and source within test harness; inspect telemetry schema/retention; prove no persistent identity/profile created | Controlled; implementation/privacy test required |
| TM-13 | **CSRF / cross-origin state mutation** | Malicious site triggers session login, device mutation, J1 mutation through ambient cookie | SameSite cookie policy; explicit CSRF token for Firebase session exchange as official guidance requires; Origin/Referer same-origin enforcement for browser state-changing routes where applicable; CORS deny-by-default/no wildcard credentials; non-cookie bearer capabilities are not accepted from URL query | Cross-origin form/fetch cases, null/forged Origin, missing/mismatched CSRF, preflight/CORS tests | Controlled; implementation/test required |
| TM-14 | **CORS/origin misconfiguration** | Attacker origin reads authenticated/accountless state or verification output | Default no cross-origin API access; explicit allowlist only if a real use case appears; never `Access-Control-Allow-Origin: *` with credentials; origin validation independent of Host/X-Forwarded-* unless trusted proxy normalizes them | Browser-based hostile-origin suite; spoofed forwarding headers; preflight matrix | Controlled; implementation/test required |
| TM-15 | **Session replay/invalid session** | Stolen Firebase session cookie used after logout/revocation/account change | Server verifies session before protected data; sensitive route can use revocation check; clear invalid cookie; bounded cookie duration; recent-auth requirement where downstream action warrants it; logout/recovery contract revokes as designed | Expired/revoked/deleted/disabled-user session tests; replay after logout/account deletion; session fixation checks | Controlled; exact session policy owned by TSK-0356 |
| TM-16 | **Mass assignment / unexpected properties** | Send internal fields such as owner, verified, role, ClientID, status, retention or admin flags | Per-route input DTO allowlist; reject or ignore unknown properties according to one documented policy; ownership/verified/admin fields server-generated only | Add every privileged/internal field to valid requests; nested object/property pollution corpus | Controlled; implementation/test required |
| TM-17 | **Prototype pollution / parser edge abuse** | Crafted object keys/nested payload exploit JS merge/config behavior | No untrusted deep merge into config/state; schema strips/rejects `__proto__`, `constructor`, `prototype` and unsupported nesting; use plain typed structures | Dedicated pollution payload tests; confirm global/object prototypes unchanged | Controlled; implementation/test required |
| TM-18 | **Sensitive error/data leakage** | Trigger exceptions to obtain stack, token, provider/admin response, internal path or state | Production error mapper with stable public codes; detailed logs remain privacy-minimal and secret-redacted; no raw provider/AdGuard response to browser; disable dev stack exposure | Forced dependency errors/malformed requests; inspect response/logs; secret-canary test | Controlled; implementation/test required |
| TM-19 | **Log/diagnostic privacy drift** | Security debugging starts retaining token/IP/domain/query/payload history | Normal logs exclude full J1 token, auth token, secret, raw DNS query/domain, browsing/activity history and unnecessary personal data; diagnostic mode separately authorized, minimum, time-boxed, access-controlled and deletion-verified per REQ-0059 | Schema/log inspection; canary query/token test; diagnostic expiry/deletion test | Controlled; release blocker if violated |
| TM-20 | **Expiry bypass / state resurrection** | Sliding access extends J1, account login refreshes J1, backup restores expired state, stale token reopens flow | Hard non-sliding J1 `expires_at`; read/update cannot extend it; account auth does not change it; completion/reset deletes early; backup excludes J1 by default; restore rejects expired transient state | Requests just before/after expiry; repeated activity; sign-in during J1; backup/restore fixture; reset/complete then replay | Controlled; implementation/test required |
| TM-21 | **Forced authentication as abuse workaround** | Engineering responds to abuse by requiring account before setup | Rate/cost/capability controls are independent of identity; degraded mode may temporarily deny an abusive operation but must not convert core journey to login-required; account remains optional | Anonymous full-core E2E under normal conditions; auth-provider outage; over-limit source vs clean source; verify clean anonymous user can proceed | Controlled by product/security acceptance |
| TM-22 | **Backend ambiguity causing duplicate/unsafe control action** | Timeout after AdGuard/device mutation leads blind retry | Idempotency/reconciliation key and observed-current-state check around material mutations; bounded retry only for proven transient/idempotent operation; ambiguous result returns `uncertain` until reconciled | Inject timeout before/after backend commit; duplicate request; verify no duplicate ClientID/device and no fabricated success | Controlled; implementation/failure injection required |

## 5. Anonymous token/capability contract

If a J1 token or setup/download capability is required, implementation must satisfy all of these:

- generated by a CSPRNG with at least 128 bits of entropy;
- opaque: no parent, child, device, ClientID, platform, timestamp, locale or state encoded for the browser to interpret;
- scoped server-side to a narrow purpose and allowed state transitions;
- hard absolute expiry; J1 maximum remains 24 hours and does not slide on activity;
- stored only as a one-way digest/HMAC-derived lookup value where practical so a datastore disclosure does not automatically expose live bearer tokens;
- full token absent from URL, logs, analytics, error messages and support records;
- invalid/expired token produces a bounded generic response and no state mutation;
- reset/completion deletes or invalidates it early;
- no token → parent-account linkage unless the separately approved explicit transfer contract is later created.

A token is a narrow capability to an anonymous workflow state, **not authentication** and not a customer identity.

## 6. Rate, resource and cost-abuse contract

OWASP API Security 2023 identifies unrestricted resource consumption as a direct availability/cost risk. UseSafeWeb controls this without persistent identity collection:

### Layer 1 — reverse proxy

- maximum request header/body sizes;
- request/header/body timeouts and connection limits;
- request-rate/concurrency protection for public dynamic routes;
- reject malformed encodings/media types before Next.js application work;
- trusted proxy/header normalization so client-controlled forwarding headers cannot bypass controls.

### Layer 2 — application route

- endpoint-specific rate/concurrency budget based on actual work cost;
- token-specific budget for J1/config/verification where a capability exists;
- coarse source/network budget may be maintained ephemerally for abuse defense but is not a persistent product/profile field;
- fixed maximum batch/list cardinality; preferably no anonymous batch endpoints;
- bounded parse/compute/output work and downstream timeouts;
- no unbounded retry, recursion, pagination, archive generation, external URL fetch or user-selected expensive query.

### Layer 3 — downstream protection

- typed adapter enforces operation allowlist and per-operation timeouts;
- circuit breaker/degraded response when AdGuard/provider/datastore is failing;
- global service cost/volume alerts independent of customer identity;
- expensive/unsafe mutation disabled before an overload cascades into the DNS protection service.

Exact numeric thresholds are **not frozen by TSK-0487** because target capacity and traffic evidence are owned by capacity/performance work. Acceptance requires explicit tested values before release and evidence that reasonable intended use still succeeds.

## 7. Injection and input-boundary contract

Every Route Handler/Server Action receiving external data must have a route-specific schema covering:

- exact HTTP method and media type;
- maximum body and field sizes;
- required/optional field allowlist;
- enum/range/format validation;
- unknown-field policy;
- normalization before comparison, with no lossy transformation that changes security meaning;
- parameterized datastore operations;
- output encoding by context;
- no dynamic command/shell/eval;
- no arbitrary filesystem path or URL destination;
- no untrusted object merge into internal configuration.

Security tests use malicious-but-synthetic fixtures only; no real child browsing data is required.

## 8. Origin, browser and session controls

- Serve application only over HTTPS in production.
- Session cookies are `Secure` and `HttpOnly`; SameSite/domain/path/expiry are intentionally bounded by the eventual TSK-0356 session contract.
- Firebase session exchange validates CSRF as current official Firebase guidance requires and verifies server-side token/session state.
- Authenticated mutations also require object/function-level authorization after authentication; auth alone is insufficient.
- Browser state-changing routes using ambient cookies enforce origin/CSRF controls.
- Route Handlers/Server Actions are treated as public API endpoints and perform their own authorization.
- No wildcard credentialed CORS.
- Server secrets stay in server-only modules/environment and never enter browser bundles.

## 9. Profile/config delivery security

The profile/config surface is treated as security-sensitive even when no account exists.

Required rules:

1. A request maps only to a supported product/platform/config variant; no arbitrary template path, remote URL, hostname, DNS server, admin route or command fragment.
2. Generated content contains only values required by the setup contract and no AdGuard admin credential, Firebase Admin credential, account secret or long-lived cross-user identifier.
3. Any user-selectable label/value is encoded/validated for the target format and cannot inject additional directives/profile sections.
4. A sensitive/generated artifact is delivered only to the scoped valid anonymous capability or authenticated owner path that requested it.
5. Cache policy prevents cross-user artifact reuse where output is user/session-specific.
6. Artifact version/integrity metadata is explicit so stale/revoked content can be rejected or replaced.
7. Removal/revocation semantics are separate from account deletion and are represented truthfully.

## 10. Verification endpoint security

A verification endpoint must not become a browsing-history oracle or an object-enumeration API.

- It tests only the approved current UseSafeWeb protection condition for the scoped journey/device.
- Browser does not choose an arbitrary domain/IP/ClientID/account ID to query.
- Response is a finite product state and reason class; no raw query log, resolver history, admin object or another user's status.
- Backend timeout/disagreement becomes `uncertain`/`action-needed`, never fabricated protected state.
- Verification is independently rate-limited and cannot be used for high-volume DNS probing.
- Account/device existence never substitutes for technical verification.

## 11. Required security test catalogue

Before the affected implementation can pass release security acceptance, automated or independently executed tests must cover at least:

### Enumeration and authorization

- random/structured/adjacent J1 tokens;
- expired/deleted tokens;
- two independent anonymous sessions;
- two distinct parent accounts and foreign device IDs;
- arbitrary ClientID/profile/config identifiers;
- hidden/admin/function endpoint and method enumeration.

### Replay and state integrity

- duplicate concurrent mutation;
- delayed replay;
- stale version/nonce;
- reset/completion then replay;
- tampered state transition and forged verification state;
- ambiguous downstream timeout before and after commit.

### Injection

- oversize body/field/nesting;
- malformed JSON/form/multipart as applicable;
- SQL/NoSQL/meta characters;
- CRLF/log forging;
- path traversal;
- HTML/script/template strings;
- `__proto__`/`constructor`/`prototype` pollution;
- arbitrary URL/private/link-local/cloud-metadata target attempts.

### Abuse/resource

- burst and sustained anonymous requests;
- token rotation and source rotation;
- concurrent expensive verification/config generation;
- slow body/connection;
- downstream outage/timeout;
- global budget/circuit-breaker behavior;
- verify normal clean anonymous flow remains usable.

### Browser/session/origin

- missing/mismatched CSRF on session exchange;
- hostile Origin, null Origin and CORS preflight;
- invalid/expired/revoked session;
- logout/account-delete replay;
- browser cache/cross-session leakage;
- token/referrer/log leakage inspection.

### Expiry/privacy

- non-sliding J1 expiry under repeated activity;
- account sign-in does not extend/link J1;
- reset/complete early invalidation;
- backup/restore does not resurrect J1;
- normal logs contain no full token, secret, raw DNS query/domain or browsing/activity history;
- diagnostic mode expires and deletion is verified.

## 12. Release-blocking criteria

The affected implementation cannot pass its security/release gate while any of these remains unresolved without a current authorized risk disposition and adequate compensating control:

- cross-session/cross-parent read or mutation;
- browser-visible/admin credential or unrestricted `/control/*` proxy;
- forged Protection Map `protected` state;
- anonymous token enumeration/replay enabling material mutation;
- arbitrary URL/internal-network fetch or command/query injection;
- unbounded resource/cost path capable of materially degrading web/DNS service;
- persistent browsing/query/activity history or unnecessary stable identity/fingerprinting introduced as abuse defense;
- expired/reset J1 state remaining usable or restored;
- mandatory login introduced for normal core safety value;
- critical/high finding under the current security acceptance policy without authorized disposition.

## 13. ACC-0487 mapping

| ACC-0487 requirement | Threat-model evidence | Result |
|---|---|---|
| enumeration | TM-01, TM-05, TM-10; token contract; enumeration test matrix | PASS CANDIDATE |
| replay | TM-02, TM-03, TM-22; idempotency/nonce/reconciliation tests | PASS CANDIDATE |
| tampering | TM-04, TM-09, TM-10, TM-16, TM-17 | PASS CANDIDATE |
| injection | TM-07, TM-08, TM-17; input-boundary and SSRF test catalogue | PASS CANDIDATE |
| denial/cost abuse | TM-11, TM-12; three-layer rate/resource contract | PASS CANDIDATE |
| profile misuse | TM-09 and Section 9 | PASS CANDIDATE |
| origin/admin separation | TM-06, TM-13, TM-14; TB-A/TB-D and Section 8 | PASS CANDIDATE |
| safe expiry | TM-20; token contract and expiry/privacy tests | PASS CANDIDATE |
| without mandatory auth | TM-21; explicit accountless security decision and normal-flow test | PASS CANDIDATE |

No acceptance criterion is satisfied by asserting that a future framework/provider will handle security automatically; all controls remain implementation/test obligations.

## 14. Current source check

Current source review on 2026-09-01 used:

- Firebase Authentication session cookies: https://firebase.google.com/docs/auth/admin/manage-cookies — server-created session cookies, CSRF protection for session exchange, cookie policy, server verification and revocation handling.
- Next.js authentication guide: https://nextjs.org/docs/app/guides/authentication — server-only session handling and the rule that Route Handlers/Server Actions require authorization like public API endpoints.
- OWASP API Security Top 10 2023: https://owasp.org/API-Security/editions/2023/en/0x11-t10/ — object-level authorization, authentication, property/function-level authorization and unrestricted resource consumption.
- OWASP API4:2023 Unrestricted Resource Consumption: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/ — request/resource/cost abuse as an API availability and financial risk.

These sources support the security control categories. Exact library/framework versions and implementation APIs remain downstream implementation work and must be matched to the then-pinned dependencies.

## 15. Non-inference

This model does **not** prove that:

- any `/website` security control is implemented;
- a datastore/provider/reverse-proxy rate-limit product or exact numeric threshold is selected;
- J1 will necessarily exist;
- penetration/fuzz/load/browser security tests have run;
- Firebase/auth has final vendor/privacy/security approval;
- no vulnerabilities remain in future code;
- `REQ-0059` diagnostic deletion is implemented;
- any critical/high future finding is accepted;
- LG-07, LG-08, LG-09, production activation, real-user validation or public launch is PASS.

**Result:** PASS CANDIDATE at the threat-model definition boundary only, pending independent current-contract verification and canonical read-back.