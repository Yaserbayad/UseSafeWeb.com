# TSK-0484 — Post-CR-0008 Security NFR Revalidation Acceptance Evidence

**Task:** TSK-0484 — Define security and abuse-resistance NFRs  
**Acceptance / Verification / Evidence:** ACC-0484 / VER-0484 / EVD-0484  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and independent read-back.

## 1. Current accepted artifact

- `TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `285ee390499190137e8aac0fed976975fb79ed80`
- publication commit `45ce41549d878fcf7875d880803a9134d075555f`

The artifact preserves the historical resolver/admin/CI/privacy/recovery security contract while adding the authentication/session/ownership/persistent-data/provider trust boundaries activated by `DEC-0053 / CR-0006`.

## 2. Exact current contract and dependency

Independent VER-0484 parsed current WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032` and proved:

- lifecycle `L4`;
- priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- sole hard dependency `TSK-0230`;
- `ACC-0484 / VER-0484 / EVD-0484`;
- current ACC requires mapping to identified threats, measurable controls and verification while keeping public resolver abuse distinct from user-data security.

Pre-reconciliation runtime blob: `a09b3c3a9dece3ec19c21d5bf5f1fdd2f004b482`.

Verifier outputs:

- `TSK0484_IMMUTABLE_INPUT_HASHES=PASS`;
- `TSK0484_CURRENT_WBS_CONTRACT=PASS`;
- `TSK0484_CURRENT_DEPENDENCY_AND_SCOPE=PASS`.

## 3. Historical self-reopen trigger proved

Historical accepted contract:

- `TSK_0484_SECURITY_ABUSE_RESISTANCE_NFR_2026-08-28.md`
- blob `ebd146f88f51cae67b9515fb94133bcd74c8cf28`.

That contract explicitly states that introducing an account/authentication system or persistent customer datastore creates a new trust boundary and reopens TSK-0484 before implementation/release. Current dual-mode Version 1 subsequently introduced optional parent authentication/session and minimum persistent parent/device ownership/dashboard state.

Verifier output: `TSK0484_HISTORICAL_SELF_REOPEN_TRIGGER=PASS`.

This is therefore a genuine acceptance-boundary requalification, not a date-only refresh.

## 4. Current threat / trust-boundary model

Current source:

- `TSK_0485_END_TO_END_THREAT_ABUSE_MODEL_2026-09-01.md`
- version `1.0.0`
- blob `373ac62ba1f244328e7d8e52ae6648d72e5a5ed7`.

Independent VER-0484 proved all 10 current trust boundaries:

`TB-WEB`, `TB-ANON`, `TB-AUTH`, `TB-OWN`, `TB-ADG`, `TB-DNS`, `TB-OPS`, `TB-CI`, `TB-EXT`, `TB-REC`.

It also proved the complete `TM-01` through `TM-30` threat set, including separate parent authentication/account ownership and technical protection-verification semantics; `ClientID` as a non-authentication/non-authorization opaque DNS-control reference; DNS-history logging prohibition; and release-blocking implementation/retest status for High/Critical current-release paths.

Verifier output: `TSK0484_CURRENT_30_THREAT_10_BOUNDARY_MODEL=PASS`.

## 5. Current privacy/data boundary

Current dependency contract:

- `TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFRS_2026-09-01.md`
- version `1.0.1-post-CR-0008`
- blob `eda85b062a3a7ba29544de35a8a813c9790092f2`.

VER-0484 checked the optional parent-account domain, server-managed session metadata, parent/device ownership, AdGuard ClientID treatment, no identifiable browsing history, accountless/account separation and truthful distinct deletion operations.

Verifier output: `TSK0484_CURRENT_PRIVACY_BOUNDARY=PASS`.

## 6. Current NFR acceptance boundary

The accepted current artifact defines 16 security NFRs:

- `SEC-RES-01`, `SEC-RES-02`;
- `SEC-WEB-01`, `SEC-WEB-02`;
- `SEC-AUTH-01`;
- `SEC-SESS-01`;
- `SEC-AUTHZ-01`;
- `SEC-DATA-01`;
- `SEC-PROV-01`;
- `SEC-ADG-01`;
- `SEC-PRIV-01`;
- `SEC-ANON-01`;
- `SEC-TRUTH-01`;
- `SEC-CI-01`;
- `SEC-REC-01`;
- `SEC-GUIDE-01`.

The independent verifier structurally parsed every Markdown table row and proved each NFR has:

1. an identified `TM-*` threat mapping;
2. an identified `TB-*` trust-boundary mapping;
3. a material security requirement; and
4. an observable/measurable verification condition.

Verifier outputs:

- `TSK0484_CURRENT_SECURITY_INVARIANTS=PASS`;
- `TSK0484_16_NFR_THREAT_CONTROL_VERIFICATION_MAP=PASS`.

Resolver abuse/availability remains explicitly separate from application/user-data security.

## 7. Current first-party source review

The artifact records current source review on 2026-09-02 against:

- OWASP ASVS: `https://owasp.org/www-project-application-security-verification-standard/`;
- OWASP Authorization Cheat Sheet: `https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html`;
- OWASP Session Management Cheat Sheet: `https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html`;
- OWASP CSRF Prevention Cheat Sheet: `https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html`;
- Firebase ID-token verification: `https://firebase.google.com/docs/auth/admin/verify-id-tokens`;
- Firebase session cookies: `https://firebase.google.com/docs/auth/admin/manage-cookies`;
- Firebase session/revocation management: `https://firebase.google.com/docs/auth/admin/manage-sessions`;
- AdGuard Home configuration: `https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration`.

These source bindings inform engineering requirements only; they do not prove implementation, provider activation, compliance or certification.

Verifier output: `TSK0484_CURRENT_SOURCE_BINDINGS=PASS`.

## 8. Downstream ownership preserved

Current WBS was independently checked so TSK-0484 does not absorb or self-certify downstream specialized work:

- TSK-0353 remains the detailed owner of Firebase/Google token verification, session/cookie/CSRF/revocation/account-takeover/IDOR/auth-rate-limit/logout/deletion/provider-outage/security-event mechanics;
- TSK-0352 remains the detailed owner of the typed/allowlisted server-side AdGuard API and persistent ClientID lifecycle/authorization contract.

Verifier output: `TSK0484_DOWNSTREAM_OWNERSHIP_BOUNDARY=PASS`.

No TSK-0352 or TSK-0353 PASS is inferred.

## 9. Independent VER-0484

Final verifier:

- `.github/workflows/verify-tsk0484-current-revalidation.yml`;
- final workflow blob `b12ec1801dee4afe633fafb8830fc2be7498a07d`;
- GitHub-hosted Ubuntu 24.04;
- `contents: read` only;
- final run/job `33579079770 / 100089332047`;
- conclusion **SUCCESS**.

Final observed terminal markers:

- `TSK0484_IMMUTABLE_INPUT_HASHES=PASS`;
- `TSK0484_CURRENT_WBS_CONTRACT=PASS`;
- `TSK0484_CURRENT_DEPENDENCY_AND_SCOPE=PASS`;
- `TSK0484_HISTORICAL_SELF_REOPEN_TRIGGER=PASS`;
- `TSK0484_CURRENT_30_THREAT_10_BOUNDARY_MODEL=PASS`;
- `TSK0484_CURRENT_PRIVACY_BOUNDARY=PASS`;
- `TSK0484_CURRENT_SECURITY_INVARIANTS=PASS`;
- `TSK0484_16_NFR_THREAT_CONTROL_VERIFICATION_MAP=PASS`;
- `TSK0484_CURRENT_SOURCE_BINDINGS=PASS`;
- `TSK0484_DOWNSTREAM_OWNERSHIP_BOUNDARY=PASS`;
- `TSK0484_CURRENT_ACCEPTANCE_ASSERTIONS=PASS`;
- `TSK0484_CURRENT_ACC=PASS`.

## 10. Diagnostic-only verifier failures

Three prior read-only runs are retained only as verifier-shape diagnostics:

1. run/job `33578799321 / 100088481431` failed because Markdown emphasis split the historical self-reopen phrase;
2. run/job `33578879992 / 100088736847` passed the semantic self-reopen check and failed because it expected two separately owned TSK-0485 security statements as one synthetic sentence;
3. run/job `33579013088 / 100089132000` passed through the 30-threat/10-boundary model and security invariants, then failed because its Markdown-table parser treated the trailing `|` delimiter as an empty verification cell.

No failed run changed governed state or weakened acceptance. The corrections moved the verifier toward canonical semantic ownership and structural parsing.

## 11. Final acceptance disposition

1. Current dependency and WBS contract — **PASS**.
2. Historical account/auth/persistent-storage self-reopen trigger — **PASS**.
3. Current dual-mode privacy/data boundary — **PASS**.
4. Current complete 30-threat / 10-boundary threat model — **PASS**.
5. Sixteen current threat-mapped measurable security NFRs — **PASS**.
6. Resolver abuse versus user-data/application-security separation — **PASS**.
7. Authentication versus authorization / parent-device ownership / ClientID boundaries — **PASS**.
8. Session/CSRF/revocation/provider-failure outcome requirements — **PASS**.
9. No browsing/query/activity-history backdoor through account/dashboard/analytics/diagnostics/backup — **PASS**.
10. High/Critical implementation/retest release-blocking boundary preserved — **PASS**.
11. TSK-0352 and TSK-0353 downstream ownership preserved — **PASS**.
12. Current external engineering-source bindings recorded — **PASS**.

**ACC-0484 = PASS. VER-0484 = PASS. EVD-0484 = SATISFIED.**

**TSK-0484 current security and abuse-resistance NFR revalidation: PASS.**

## 12. Non-inference

This proves current L4 security-NFR definition acceptance only. It does not prove application/authentication/datastore implementation, provider activation, target-environment High/Critical security-path retest, production security, legal/privacy compliance, TSK-0352, TSK-0353, any successor, LG-06, publication, participant processing, payment, market activation or launch.
