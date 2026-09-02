# TSK-0353 — Current Authentication, Authorization, Session and Account-Lifecycle NFR Evidence

**Task:** TSK-0353 — Define authentication, authorization, session and account-lifecycle NFRs  
**Acceptance / Verification / Evidence:** ACC-0353 / VER-0353 / EVD-0353  
**Lifecycle / Priority / Capability / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Current accepted artifact

- `TSK_0353_POST_CR0008_AUTHORIZATION_SESSION_ACCOUNT_LIFECYCLE_NFRS_2026-09-02.md`
- version `1.0.0-post-CR0008`
- blob `3cb7c248b6d121e1c8d9db47accdf639998edc93`
- publication commit `5b12d4d78589c5c76013422dfa98ab8fab2ab64d`

The artifact defines the Version-1 optional-account authentication/session/authorization security boundary without implementing or activating a provider. The accountless core remains independent and login-free.

## 2. Canonical WBS / dependency / evidence contract

Independent VER-0353 parsed current WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and relationship graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032` against pre-reconciliation runtime blob `0a0fc742d3e0d54dbb07c29275b4d5e1358c4fd4`.

It proved:

- lifecycle `L4`;
- priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- hard dependencies exactly `TSK-0230; TSK-0484`;
- IDs exactly `ACC-0353 / VER-0353 / EVD-0353`;
- current ACC covers Firebase/Google token verification, `HttpOnly`/`Secure`/`SameSite` sessions, CSRF, revocation, account takeover, parent-to-device ownership/IDOR, rate limits, logout/deletion, provider outage and privacy-safe security audit events;
- current VER method: `Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.`;
- current EVD requirement: `Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.`

Markers:

- `TSK0353_INPUT_HASHES=PASS`;
- `TSK0353_CURRENT_WBS=PASS`;
- `TSK0353_CURRENT_PREDECESSORS=PASS`.

## 3. Current predecessor proof

VER-0353 independently parsed durable PASS records for:

- TSK-0230 current privacy/data-minimisation/retention/deletion NFR, artifact blob `eda85b062a3a7ba29544de35a8a813c9790092f2`;
- TSK-0484 current security/abuse NFR, artifact blob `285ee390499190137e8aac0fed976975fb79ed80`.

TSK-0044 current dual-mode AdGuard API/credential/failure artifact blob `9e2df58093c592621eb1531dc1c34393a247dd80` was additionally hash-bound as a compatible interface constraint; it is not a TSK-0353 hard dependency.

## 4. Current external source review

The NFR was checked against current first-party/security engineering sources on 2026-09-02:

1. Firebase `Verify ID Tokens` — `https://firebase.google.com/docs/auth/admin/verify-id-tokens` — current backend verification includes token format/signature/expiry and project/issuer/subject claim checks; ordinary verification does not itself prove revocation unless revocation checking is requested. Page current at review; surfaced last updated 2026-09-01 UTC.
2. Firebase `Manage Session Cookies` — `https://firebase.google.com/docs/auth/admin/manage-cookies` — supports server-created session cookies with custom expiry from 5 minutes to 2 weeks, cookie policy controls including `HttpOnly`/`Secure`, CSRF handling, recent `auth_time` checks and revocation-aware session verification. Surfaced last updated 2026-08-24 UTC.
3. Firebase `Manage User Sessions` — `https://firebase.google.com/docs/auth/admin/manage-sessions` — documents short-lived ID tokens, refresh-token revocation and `checkRevoked` verification behavior.
4. Google Identity Services `Verify the Google ID token on your server side` — `https://developers.google.com/identity/gsi/web/guides/verify-google-id-token` — validates the GIS double-submit CSRF token and requires server-side signature, audience, issuer and expiry verification; `sub` is the stable unique account identifier rather than email. Surfaced last updated 2025-12-22 UTC.
5. OWASP Session Management Cheat Sheet — `https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html` — current guidance covers `Secure`, `HttpOnly`, explicit `SameSite`, fixation prevention and reauthentication around high-risk events.
6. OWASP IDOR Prevention / Authorization Cheat Sheets — `https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html` and `https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html` — server-side object authorization is required for each operation; opaque identifiers do not replace access control.

No source required provider activation or contradicted the project’s accountless-first dual-mode boundary.

## 5. Token and provider verification disposition

VER-0353 proved the contract requires:

- Firebase ID token exchange only through a dedicated HTTPS server endpoint;
- backend Admin-SDK/equivalent validation of signature/key, `aud`, `iss`, `exp`, non-empty `sub`/UID and sane `iat`/`auth_time`;
- recent authentication `<=5 minutes` for session creation;
- revocation-aware checks where required;
- fail-closed deleted/disabled/revoked/invalid identities;
- no raw ID/refresh/access tokens or service credentials in product records/browser persistent storage/analytics/logs/evidence;
- direct GIS flow CSRF validation plus signature/audience/issuer/expiry checks;
- immutable Google `sub`, not email, as provider account identity;
- no automatic account merge/link from matching email.

Markers:

- `TSK0353_FIREBASE_TOKEN_VERIFICATION=PASS`;
- `TSK0353_GOOGLE_TOKEN_VERIFICATION=PASS`;
- `TSK0353_DATA_MINIMISATION=PASS`.

## 6. Session / CSRF / takeover disposition

VER-0353 proved:

- `Secure` + `HttpOnly` + explicit `SameSite=Lax` baseline, Path `/`, host scope/no Domain, `__Host-` preferred where compatible;
- no `SameSite=None` ordinary parent session;
- Version-1 absolute session lifetime maximum `7 days`, non-sliding;
- recent-auth `<=5 minutes` before session issue and high-risk operations;
- no bearer session token in localStorage/sessionStorage/URL/log;
- authenticated transition replaces pre-auth authority to prevent fixation;
- every unsafe cookie-authenticated request requires effective CSRF protection; SameSite is defense in depth only;
- provider/UID rather than email anchors account identity;
- token theft/revocation/disable/delete triggers reauthentication/invalidation;
- no local password/SMS/MFA functionality is falsely claimed.

Markers:

- `TSK0353_SESSION_COOKIE=PASS`;
- `TSK0353_CSRF=PASS`;
- `TSK0353_ACCOUNT_TAKEOVER=PASS`.

## 7. Authorization / IDOR / AdGuard boundary disposition

VER-0353 proved each account/device operation derives parent identity from the verified server session, scopes object lookup to that parent or performs equivalent explicit ownership authorization, denies ambiguous/missing ownership and rechecks authorization for consequential actions.

The contract includes deterministic A/B synthetic cross-parent negative fixtures for read/update/unlink/revoke/delete/recover operations. ClientID/UUID possession and identifier complexity never substitute for authorization. TSK-0352 remains the owning concrete AdGuard persistent-ClientID API/lifecycle contract.

Markers:

- `TSK0353_OWNERSHIP_IDOR=PASS`;
- `TSK0353_ADGUARD_INTERFACE_BOUNDARY=PASS`.

## 8. Logout, revocation and deletion disposition

The current contract distinguishes:

- current-browser logout: clear the current cookie, no false claim of remote-token revocation;
- global/security revocation: provider/server revocation sufficient for old sessions to fail subsequent protected-route verification;
- account deletion: recent-authenticated multi-domain operation with `deleting` state, session revocation, owned-device lifecycle handling, minimum local deletion, provider deletion where applicable, and explicit `complete / pending_reconciliation / failed_safe` truth;
- account/device deletion never implies physical DNS/profile removal without separate proof;
- backup/retry/provider return must not resurrect deleted/revoked authority.

Markers:

- `TSK0353_LOGOUT_REVOCATION=PASS`;
- `TSK0353_ACCOUNT_DELETION=PASS`.

## 9. Provider/datastore outage and accountless fallback

The verifier proved that provider failure establishes no new account authority; ambiguous/non-provable sessions fail closed for account-only operations; ownership datastore failure blocks ownership-changing mutations; stale cache is not authorization; ambiguous partial writes reconcile before retry.

The independently healthy accountless start/setup/verification/Protection Map/recovery/removal path remains available throughout provider/datastore account-only failure.

Marker: `TSK0353_PROVIDER_DATASTORE_OUTAGE=PASS`.

## 10. Rate limiting and security-event privacy

VER-0353 structurally proved five Version-1 rate-limit rows covering session exchange, CSRF/token-invalid exchange, authorization denials, device mutations and account deletion/global revocation. Keys are bounded/security-only; network limiting uses short-TTL keyed hashes rather than durable raw-IP analytics.

The security-event contract is operational/security-only, not product analytics. It defines bounded allowlisted event/reason/operation classes and prohibits tokens, cookies, email/profile payload, DNS/domain/URL history and arbitrary free text. Durable security-event collection fails closed until TSK-0230 has an exact necessary bounded retention/deletion contract.

Markers:

- `TSK0353_RATE_LIMITS=PASS`;
- `TSK0353_SECURITY_AUDIT_EVENTS=PASS`.

## 11. Protection-state and deterministic-test disposition

Identity/session/account/device/ClientID/dashboard presence is never technical protection evidence. The artifact contains exactly 30 deterministic future implementation assertions covering invalid/revoked token cases, cookie/CSRF/session fixation, IDOR, provider/datastore outage, logout/revocation/deletion, rate limits, audit privacy and Protection Map separation.

Markers:

- `TSK0353_PROTECTION_SEPARATION=PASS`;
- `TSK0353_ASSERTION_CATALOGUE=PASS`;
- `TSK0353_NON_INFERENCE=PASS`.

## 12. Independent VER-0353

Independent read-only verifier:

- script `.github/scripts/verify_tsk0353_current_nfr.py` — blob `9c60b5b087eaf9dd2a2a79e9440997bb89d7fa67`;
- workflow `.github/workflows/verify-tsk0353-current-nfr.yml` — blob `ef2bc9ac92ab11886859af397c91ae602f511b10`;
- workflow permissions: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- run `33589319072`;
- job `100119889794`;
- conclusion **SUCCESS**;
- responsible verifier: isolated GitHub Actions job executing the hash-locked structural verifier;
- deviations: none; no verifier weakening/correction cycle was required.

Final markers:

- `TSK0353_INPUT_HASHES=PASS`;
- `TSK0353_CURRENT_WBS=PASS`;
- `TSK0353_CURRENT_PREDECESSORS=PASS`;
- `TSK0353_STRUCTURE=PASS`;
- `TSK0353_SOURCE_REVIEW=PASS`;
- `TSK0353_FIREBASE_TOKEN_VERIFICATION=PASS`;
- `TSK0353_GOOGLE_TOKEN_VERIFICATION=PASS`;
- `TSK0353_DATA_MINIMISATION=PASS`;
- `TSK0353_SESSION_COOKIE=PASS`;
- `TSK0353_CSRF=PASS`;
- `TSK0353_OWNERSHIP_IDOR=PASS`;
- `TSK0353_ACCOUNT_TAKEOVER=PASS`;
- `TSK0353_LOGOUT_REVOCATION=PASS`;
- `TSK0353_ACCOUNT_DELETION=PASS`;
- `TSK0353_PROVIDER_DATASTORE_OUTAGE=PASS`;
- `TSK0353_RATE_LIMITS=PASS`;
- `TSK0353_SECURITY_AUDIT_EVENTS=PASS`;
- `TSK0353_PROTECTION_SEPARATION=PASS`;
- `TSK0353_ASSERTION_CATALOGUE=PASS`;
- `TSK0353_NON_INFERENCE=PASS`;
- `TSK0353_ADGUARD_INTERFACE_BOUNDARY=PASS`;
- `TSK0353_CURRENT_ACC=PASS`;
- `TSK0353_CURRENT_VER=PASS`;
- `TSK0353_CURRENT_EVD_READY=PASS`;
- `TSK0353_CURRENT_NFR=PASS`.

## 13. Acceptance disposition

**ACC-0353 = PASS. VER-0353 = PASS. EVD-0353 = SATISFIED.**

**TSK-0353 current authentication/authorization/session/account-lifecycle NFR: PASS, pending only guarded runtime reconciliation and exact GitHub read-back.**

## 14. Non-inference

This proves L4 NFR-definition acceptance only. It does not activate Firebase/Google, choose/approve a vendor plan, create or process user accounts, implement a session/auth/datastore/AdGuard adapter, create a legal basis, authorize real-user processing, pass a lifecycle gate, publish, activate a market, launch or infer successor PASS.
