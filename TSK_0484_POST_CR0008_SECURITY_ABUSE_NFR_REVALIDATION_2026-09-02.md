# TSK-0484 — Post-CR-0008 Security and Abuse-Resistance NFR Revalidation

**Task:** TSK-0484 — Define security and abuse-resistance NFRs  
**Acceptance / Verification / Evidence:** ACC-0484 / VER-0484 / EVD-0484  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0484 current PASS pending independent VER-0484 and guarded runtime reconciliation.

## 1. Why current revalidation is mandatory

The accepted 2026-08-28 TSK-0484 contract explicitly required TSK-0484 to reopen before implementation/release if an account/authentication system or persistent customer datastore was introduced. `DEC-0053 / CR-0006` subsequently activated Version-1 optional parent authentication/session, minimum parent/device ownership persistence and a lightweight dashboard/device-management surface while preserving a complete accountless core.

That change activates new `TB-AUTH`, `TB-OWN`, persistent datastore and provider trust boundaries. The historical TSK-0484 resolver, administration, CI/supply-chain, anonymous-state, privacy and recovery requirements remain valid where unchanged, but the complete current ACC-0484 cannot rely on the pre-account threat boundary alone.

Current WBS authority remains:

- lifecycle `L4`;
- priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- hard dependency exactly `TSK-0230`;
- ACC-0484: requirements map to identified threats, include measurable controls and verification, and distinguish public resolver abuse from user-data security;
- VER-0484: independent review against current source baseline, dependency, acceptance and evidence;
- EVD-0484: artifact/version, source/environment, review output/date/verifier/deviations/disposition.

Current TSK-0230 is PASS and now explicitly covers separate J0/J1 anonymous, optional parent account/session, parent-owned device, DNS control-plane, telemetry and backup domains. No dependency or gate blocks this current L4 revalidation.

## 2. Current authority consumed, without duplicating ownership

This L4 contract defines the **umbrella security/abuse NFR boundary**. It does not steal ownership from later specialized tasks.

Current authoritative inputs:

- `TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFRS_2026-09-01.md`, version `1.0.1-post-CR-0008`, blob `eda85b062a3a7ba29544de35a8a813c9790092f2` — current privacy/data-domain boundary;
- `TSK_0485_END_TO_END_THREAT_ABUSE_MODEL_2026-09-01.md`, version `1.0.0`, blob `373ac62ba1f244328e7d8e52ae6648d72e5a5ed7` — current 30-row end-to-end threat/abuse catalogue and 10 trust boundaries;
- historical TSK-0484 contract `TSK_0484_SECURITY_ABUSE_RESISTANCE_NFR_2026-08-28.md`, blob `ebd146f88f51cae67b9515fb94133bcd74c8cf28`, retained for unchanged resolver/admin/CI/privacy/recovery requirements;
- historical TSK-0484 evidence `TSK_0484_SECURITY_ABUSE_RESISTANCE_NFR_EVIDENCE_2026-08-28.md`, blob `15ad7e97f13210737e014499820690c30232a952`;
- current WBS TSK-0353 remains the later detailed owner of Firebase/Google token verification, cookie/session, CSRF, revocation, account takeover, ownership/IDOR, rate-limit, logout/deletion, provider-outage and privacy-safe security-event details;
- current WBS TSK-0352 remains the later detailed owner of the typed/allowlisted AdGuard API, high-entropy ClientID, authorization, rollback/reconciliation and privacy booleans.

This TSK-0484 revalidation establishes the security conditions those downstream designs/implementations must satisfy. It does not mark TSK-0352 or TSK-0353 PASS.

## 3. Current external engineering-source review

Current official sources were rechecked on 2026-09-02:

1. OWASP ASVS — https://owasp.org/www-project-application-security-verification-standard/ — current stable ASVS is 5.0.0 and is suitable as a requirements/verification yardstick.
2. OWASP Authorization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html — deny by default, least privilege, permissions on every request and server-side object authorization remain current guidance.
3. OWASP Session Management Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html — secure/HttpOnly/SameSite cookie properties, opaque unpredictable server-side session state, fixation prevention, expiry/revocation and no session IDs in URLs remain current guidance.
4. OWASP CSRF Prevention Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html — SameSite is defense in depth, state-changing requests require an effective CSRF defense, and CSRF secrets must not be leaked in URLs/logs.
5. Firebase Authentication — Verify ID Tokens — https://firebase.google.com/docs/auth/admin/verify-id-tokens — server-side backends must verify Firebase ID-token integrity/authenticity before using the resulting UID as authenticated identity.
6. Firebase Authentication — Manage Session Cookies — https://firebase.google.com/docs/auth/admin/manage-cookies — server-managed session cookies and logout/session invalidation are supported by the Admin SDK pattern.
7. Firebase Authentication — Manage User Sessions — https://firebase.google.com/docs/auth/admin/manage-sessions — Firebase ID tokens are short lived, refresh tokens are long lived until defined revocation conditions, and Admin SDK revocation/check-revoked mechanisms exist.
8. AdGuard Home configuration — https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration — `ratelimit`, IPv4/IPv6 aggregation and `refuse_any` remain current anti-abuse/anti-amplification controls.

These sources inform measurable engineering requirements. They do not establish production implementation, Firebase architecture approval, legal/privacy compliance or certification.

## 4. Current security assets and trust boundaries

The current TSK-0485 asset/boundary model is adopted as the security baseline rather than recreated inconsistently.

Current trust boundaries:

- `TB-WEB` — Internet/browser ↔ public application;
- `TB-ANON` — browser ↔ J0/J1 anonymous journey state;
- `TB-AUTH` — browser ↔ optional authentication/session;
- `TB-OWN` — authenticated parent ↔ parent/device ownership and persistent state;
- `TB-ADG` — application server ↔ typed/allowlisted AdGuard control boundary;
- `TB-DNS` — Internet/client resolver ↔ encrypted DNS/upstream path;
- `TB-OPS` — runtime ↔ logs/metrics/alerts/recovery/admin operations;
- `TB-CI` — repository/dependency/action ↔ build/deployment credentials/artifacts;
- `TB-EXT` — application ↔ authentication provider/datastore/DNS/upstream providers;
- `TB-REC` — live state ↔ delete/backup/restore/rollback/disaster recovery.

Critical assets include truthful `protected_verified` state, parent identity/session, parent-device ownership, server-only ClientID mapping/admin credentials, DNS availability/configuration, J0/J1 non-linkage, minimum persistent account/device state, delete/revoke/recovery state, source/CI/deployment credentials, privacy-safe operational evidence and domain/TLS identity.

## 5. Security invariants

1. **Resolver abuse and user-data/application security are separate domains.** DNS rate limiting cannot prove account/data security; logging minimisation cannot prove resolver availability.
2. **Accountless core remains independent.** Auth/provider/datastore failure may disable account-only operations but must not turn core setup/protection/removal into mandatory-login functionality.
3. **Authentication is not authorization.** A valid Firebase/Google identity proves only authenticated identity; every parent/device/account operation requires server-side ownership authorization.
4. **ClientID is never a credential or authorization token.** It is a server-only opaque control reference resolved only after parent/device authorization.
5. **Account/device presence is never protection evidence.** Account ownership, dashboard presence, stored configuration, profile presence or parent confirmation cannot produce `protected_verified`.
6. **No browsing/query/activity-history store.** Persistent identifiable DNS query/file logging and identifiable per-client statistics remain OFF/excluded; account capability cannot create a surveillance backdoor.
7. **Anonymous and account domains stay separate.** J0/J1 does not silently link/promote into parent/device state, and sign-in cannot extend anonymous retention.
8. **Secrets stay server-side and outside Git/browser/evidence/logs.** AdGuard admin credentials, Firebase service credentials, session secrets and private keys are externally injected, minimum-scoped and revocable.
9. **Ambiguous consequential mutations fail closed and reconcile before replay.** Account/device/ClientID/delete/revoke operations cannot report success while outcome is unknown.
10. **High/Critical active-release paths are release-blocking until implementation plus blocking verification succeeds.** A design row is not implementation proof.

## 6. Current NFR catalogue

| NFR | Threats / boundaries | Current requirement | Measurable verification / PASS condition |
|---|---|---|---|
| SEC-RES-01 | TM-10/TM-11; TB-DNS/TB-WEB | Preserve bounded resolver/request rate, size, timeout, concurrency and cost controls; public plain DNS remains closed unless separately approved; `refuse_any`/engine anti-abuse remains explicitly configured where applicable. | Current DoH boundary low-rate and abuse/flood tests show legitimate baseline succeeds, configured limits engage, resources/cost remain bounded and service recovers healthy. |
| SEC-RES-02 | TM-20/TM-27; TB-DNS/TB-EXT | DNS/upstream/domain/TLS failure or compromise must never retain a false positive protection claim. | Wrong/expired TLS, DNS misroute and upstream timeout/error fixtures fail verification or downgrade truthfully; recovery restores only approved topology and fresh verification. |
| SEC-WEB-01 | TM-01/TM-21/TM-29; TB-WEB | All route/query/body/device-label/error inputs are schema/type/length/enum validated; datastore operations are parameterized/typed; rendering remains escaped; unsafe arbitrary HTML/command/control construction is prohibited; production errors are generic. | Seed XSS, structured injection, oversized/malformed and error-path fixtures; no script/command/query/control execution and no stack/secret/internal identifier disclosure. |
| SEC-WEB-02 | TM-28/TM-02; TB-WEB/TB-AUTH | HTTPS/HSTS and anti-framing controls apply to authenticated surfaces; no state mutation on safe GET; cookie-authenticated state-changing operations use an effective CSRF defense in addition to SameSite. | Header scan passes; unapproved framing fails; cross-site forged create/update/delete/revoke requests fail while valid same-origin operations work. |
| SEC-AUTH-01 | TM-03/TM-04/TM-22; TB-AUTH/TB-EXT | Backend must verify provider/Firebase identity before establishing authority; invalid, expired, wrong-project or revoked identity cannot authenticate. Authentication endpoints are abuse-limited and non-enumerating where identity-sensitive. | Invalid/expired/wrong-project/revoked token fixtures fail; repeated auth/recovery attempts reach safe limits without revealing whether another account exists; legitimate baseline remains usable. |
| SEC-SESS-01 | TM-02/TM-03; TB-AUTH | Authenticated session is server-managed, opaque/unpredictable, never placed in URL/localStorage, and transported only in Secure + HttpOnly + explicit SameSite cookie; fixation is prevented; expiry/logout/revocation are server-enforced. Prefer `__Host-` cookie scope where deployment allows. | Unknown/fixed/expired/revoked cookies fail; login/risk transition replaces prior session; logout/revoke invalidates subsequent use; browser storage inspection finds no bearer session token. |
| SEC-AUTHZ-01 | TM-05/TM-06; TB-OWN/TB-ADG | Deny by default and authorize every account/device operation against authenticated parent ownership server-side; opaque IDs/ClientID are not authorization. | Parent A cannot read/change/delete/recover Parent B by modifying object/device/ClientID identifiers; every negative cross-parent case returns no data/effect. |
| SEC-DATA-01 | TM-08/TM-15/TM-25/TM-26; TB-OWN/TB-REC | Persistent account/device mutations use uniqueness, concurrency/idempotency and bounded reconciliation rules; deletion/revoke/backup/restore cannot create orphan/cross-parent/resurrected authority. | Inject timeout, duplicate, concurrent, delete/revoke and restore faults; final state is deterministic, ownership-correct, no orphan privileged ClientID/session remains and deleted authority is not resurrected. |
| SEC-PROV-01 | TM-07; TB-AUTH/TB-EXT | Authentication/provider/datastore outage fails closed for account-only operations and fails open only to the **accountless product path**, never to account authorization. | Simulated provider/datastore timeout/invalid response grants no account access; accountless setup/verify/remove remains usable; ambiguous sessions are rejected/reconciled. |
| SEC-ADG-01 | TM-06/TM-09/TM-25; TB-ADG | AdGuard admin/control remains non-public/server-side; browser never receives admin credential; only typed allowlisted operations after parent-device authorization; arbitrary `/control/*` proxying prohibited. | Public/browser attempts cannot reach admin or arbitrary control API; secret scan passes; modified ClientID cannot target another parent; allowlisted intended operation only. |
| SEC-PRIV-01 | TM-16; TB-OPS/TB-DNS/TB-OWN | Logs/events/errors/backups/dashboard data exclude DNS/domain browsing history, raw tokens/session secrets and unnecessary identity; current TSK-0230 retention/access/deletion constraints apply. | Runtime/config/schema/log/cache/backup samples contain no prohibited query/domain history, identifiable client statistics, session secret or unapproved anonymous↔account linkage. |
| SEC-ANON-01 | TM-17; TB-ANON | J0/J1 identifiers remain high-entropy, scoped, expiry-enforced, non-reusable across other journeys/accounts and never promoted automatically into account identity. | Guess/replay/tamper/cross-session attempts cannot access/change another journey; expired state cannot be revived or linked through sign-in. |
| SEC-TRUTH-01 | TM-18/TM-19/TM-30; TB-ANON/TB-DNS/TB-OWN | `protected_verified` requires fresh qualifying technical evidence; account/device/config/profile/parent-confirmation-only state remains below verified; resolver/network changes invalidate stale proof. | Account-only, confirmation-only, profile/config-only, VPN/custom-resolver/network-change and stale fixtures never produce/retain verified state without fresh qualifying evidence. |
| SEC-CI-01 | TM-12/TM-13/TM-14/TM-23; TB-CI/TB-OPS | One authoritative dependency/lockfile path; third-party actions/dependencies reviewed/pinned as applicable; workflow permissions/secrets least privilege; untrusted inputs never receive production secrets; technical root privilege never expands Action Authority. | Dependency/action/workflow policy checks, secret scans and malicious/untrusted workflow fixtures cannot obtain protected secrets or unauthorized write/deploy/owner action. |
| SEC-REC-01 | TM-15/TM-26/TM-27; TB-REC | Recovery material is integrity-protected, access-limited and privacy-bounded; J1 is excluded from durable backup; account/device restore cannot resurrect deleted/revoked authorization; DNS/domain/TLS recovery preserves truthful status. | Backup inspection/restore/delete/revoke test confirms no J1/DNS history/secrets, no resurrected authority, and known-good endpoint identity after recovery. |
| SEC-GUIDE-01 | TM-24; TB-WEB | Security-sensitive setup/recovery guidance is versioned/source-backed and suppressed when stale/unsupported rather than shown as safe. | Stale/unsupported content fixture routes to stale/uncertain/not-covered state and cannot produce an actionable unsafe step or protected claim. |

## 7. Authentication boundary versus TSK-0353

This contract intentionally defines **outcomes and blocking tests**, not the final Firebase/session architecture.

TSK-0353 remains responsible for selecting/freezing detailed Version-1 authentication/session NFR mechanics under its own ACC, including Firebase/Google token verification, exact session-cookie policy, CSRF implementation, revocation, account takeover handling, parent/device authorization/IDOR tests, auth endpoint rate limits, logout/deletion, provider outage and privacy-safe security events.

TSK-0484 requires that TSK-0353 satisfy SEC-AUTH-01, SEC-SESS-01, SEC-AUTHZ-01, SEC-PROV-01 and the cross-cutting privacy/recovery invariants. TSK-0484 does not infer TSK-0353 PASS.

## 8. AdGuard boundary versus TSK-0352

TSK-0352 remains responsible for the exact typed/allowlisted server-side AdGuard API and persistent ClientID lifecycle contract. TSK-0484 requires that design to satisfy SEC-ADG-01 plus authorization, concurrency/reconciliation, privacy, secret and recovery NFRs. `ClientID` remains a non-secret opaque technical reference and never replaces authenticated parent-device ownership authorization.

## 9. Current gap/deviation preservation

Historical TSK-0484 implementation gaps remain visible unless separately closed by later direct evidence:

- public encrypted resolver abuse/rate/concurrency behavior requires current target-path verification before release where not already separately evidenced;
- custom/operational logging permissions and runtime privacy state must meet current TSK-0230/INT-0007 evidence at release time;
- root-capable/self-hosted workflow and repository credential exposure must follow least privilege and current CR-0008 evidence/security controls;
- current TSK-0485 High/Critical paths remain `CONTROL PLAN DEFINED; IMPLEMENTATION/RETEST REQUIRED` unless another accepted task supplies direct implementation evidence.

No current security incident or compromise is inferred from a design/deviation record.

## 10. Current acceptance assertions

1. Every current NFR maps to identified TSK-0485 threat classes/trust boundaries.
2. Every NFR has an observable blocking verification condition.
3. Public resolver abuse/availability remains separated from application/user-data security.
4. CR-0006 account/auth/session/device/dashboard/persistent-state boundaries are now included.
5. Current TSK-0230 privacy/data-minimisation/retention/deletion constraints are inherited rather than weakened.
6. Firebase/Google identity is not accepted without backend verification; authentication never substitutes for authorization.
7. Every account/device operation requires server-side ownership authorization; ClientID cannot authorize.
8. Cookie-session, CSRF, expiry, logout and revocation outcomes are security requirements, while exact detailed architecture remains TSK-0353.
9. Provider/datastore failure never grants account authority and never blocks the complete accountless core path.
10. Persistent data concurrency/delete/restore semantics fail closed and reconcile before replay.
11. AdGuard admin credentials/control remain private/server-side and arbitrary control proxying remains prohibited.
12. Privacy logging/history prohibitions remain intact across account, dashboard, analytics, diagnostics and backup paths.
13. Only fresh technical evidence may create `protected_verified`; account/configuration presence cannot.
14. CI/supply-chain/secret/root-governance controls remain explicit and independently verifiable.
15. High/Critical current-release paths remain release-blocking until implemented and retested.
16. No account implementation, provider activation, datastore implementation, public release, user processing, legal completion or later-task PASS is inferred.

## 11. Candidate disposition

**ACC-0484 current candidate: PASS pending independent current VER-0484.**

The historical contract remains valid evidence for unchanged resolver/admin/CI/privacy/recovery facts. This post-CR-0008 artifact is the current acceptance candidate because it closes the explicit account/authentication/persistent-storage trust-boundary gap without duplicating downstream TSK-0352/TSK-0353 implementation ownership.
