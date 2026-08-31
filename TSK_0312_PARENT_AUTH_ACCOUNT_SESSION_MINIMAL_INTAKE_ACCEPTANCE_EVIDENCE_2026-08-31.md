# TSK-0312 — Parent Authentication Requirements Acceptance Evidence

**Task:** TSK-0312 — Specify parent authentication, account/session, and minimal intake requirements  
**Acceptance:** ACC-0312  
**Verification:** VER-0312  
**Evidence:** EVD-0312  
**Date:** 2026-08-31  
**Verifier:** Governed post-publication analytical verification, separate from artifact authoring  
**Result:** PASS CANDIDATE PENDING DETERMINISTIC VERIFICATION AND RUNTIME RECONCILIATION

## 1. Exact artifact under review

- Path: `TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md`
- Version: `1.0.0`
- Blob read back from `main`: `8dd71bccbd24ac5f62d5c536e644e7d9209b5832`
- Publication commit: `f2f383c0c7b01b72b1eb708e0522bf13bb415369`

The exact persisted artifact was read back before this review.

## 2. Eligibility and current authority inspected

- Current WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Focused WBS preflight run/job `33397362264 / 99504989788` on self-hosted `adguardvm` confirmed the exact TSK-0312 row: L4, `PLANNED`, WBS snapshot `WAITING`, priority MEDIUM, sole hard dependency `TSK-0140`, A3 / `AUTO_ALLOWED`, ACC-0312 / VER-0312 / EVD-0312, risk RSK-0002, interfaces INT-0009/INT-0010, requirements REQ-0028/0029/0034 and constraints CON-0010/0017.
- `CURRENT_STATE.md` runtime blob at preflight: `7d337793c68b72f5001b305905acc606c1f839c7`; it records TSK-0140 current post-CR-0007 PASS and contains no current TSK-0312 PASS section.
- TSK-0140 current product brief: `TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md`, blob `8ed698b3e34540aefac617e5f6754e20d9dfbdc3`.
- Requirements register blob: `a2212059f69c4602eb0c05961d5d1639e3543f83`.
- Constraints register blob: `9464720bff94fd569e3b939568996a26eed83ca1`.
- Interfaces register current baseline inspected: INT-0009 and INT-0010 require implementation-ready states/errors/recovery/accessibility criteria and objective QA-testable outcomes.
- Accepted TSK-0229 separation amendment: `TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md`, blob `2955c2762e726f95ec67c33b9abbc5e4b25cb84a`.
- DEC-0053/CR-0006 and DEC-0054/CR-0007 remain current: optional-account scope is active and detailed in-scope account design is autonomous; neither decision itself creates task PASS.

**Eligibility result:** PASS. TSK-0140 is current PASS, TSK-0312 is AUTO_ALLOWED, and this internal L4 requirements definition performs no real-user, provider-contract, production, payment, legal-attestation or other retained human act.

## 3. Exact ACC-0312

Current ACC-0312 requires:

> Requirements define Google social sign-in, account/session lifecycle, minimal required identity fields, logout/revocation/deletion, intake fields, prohibited data, validation, errors, resume/expiry behavior, CSRF/session protections and test cases; no password or SMS authentication is introduced without a later decision.

## 4. Clause-by-clause acceptance review

| ACC-0312 clause | Persisted artifact evidence | Result |
| --- | --- | --- |
| Google social sign-in | Section 2 AUTH-01 requires Google social sign-in as the planned Version-1 route while keeping Google/Firebase provider/architecture acceptance downstream. | PASS |
| No password authentication | AUTH-01 and prohibited-data section explicitly exclude local password authentication absent later authority. | PASS |
| No SMS authentication | AUTH-01 and prohibited-data section explicitly exclude SMS/phone-number authentication absent later authority. | PASS |
| Account/session lifecycle | Section 6 defines 11 distinct product states from accountless/sign-in through active/expired/revoked/logout/deletion/recovery. | PASS |
| Minimal required identity fields | Section 3 provides a semantic allowlist with necessity for internal account ID, provider type, provider-bound identity reference, lifecycle status/timestamps and minimum session-control metadata. | PASS |
| Avoid unnecessary provider identity data | Email/display name/photo are conditional rather than mandatory; child identity/profile fields are not required for sign-in. | PASS |
| Logout | ACCOUNT-01 requires session termination, denial of later account-only access without re-authentication and truthful distinction from deletion/DNS removal. | PASS |
| Revocation | ACCOUNT-02 requires fail-closed account access, non-sensitive recovery/re-authentication and no uncertain silent identity merge/account creation. | PASS |
| Deletion | ACCOUNT-03 requires explicit action/confirmation, session invalidation, downstream governed account/device-data deletion and truthful separation from J0/J1 deletion and DNS removal. | PASS |
| Intake fields | Section 4 restricts sign-in/account intake to approved provider response, minimum account lifecycle fields and strictly necessary explicit choices; device intake remains bounded and child identity is not required. | PASS |
| Prohibited data | Section 5 explicitly prohibits password/SMS auth data, child accounts, browsing/query/activity history, surveillance data, raw AdGuard admin, payment-before-value, automatic anonymous linkage and undocumented identity fields. | PASS |
| Validation | Section 8 requires documented necessity, trusted-boundary authoritative validation, explicit format/length/value rules before build, safe handling of unknown fields/states and non-sensitive corrective errors. | PASS |
| Errors | Sections 6 and 10 define cancelled, failed, provider unavailable, ambiguous binding, invalid/revoked session, uncertain logout/revocation and interrupted deletion behavior. | PASS |
| Resume behavior | Section 10 requires safe return/retry, preservation only of non-sensitive context where safe, and resolution to known auth state before account-only action. | PASS |
| Expiry behavior | Sections 6/10 require re-authentication for account-only functions on expiry while preserving accountless core and not implying DNS protection stopped; exact session-duration values are deliberately deferred to L5 rather than invented. | PASS |
| CSRF protections | Section 9 requires implementation-appropriate CSRF protection for state-changing authenticated browser operations or an independently justified non-susceptible architecture. | PASS |
| Session protections | Section 9 requires secure L5-approved session design, trusted-side validity/authz checks, revocation/expiry enforcement and no token leakage in URL/analytics/log/content. | PASS |
| Test cases | Section 12 defines 16 deterministic/synthetic cases covering login-free core, sign-in success/cancel/error/retry, expiry/revocation, logout, CSRF, ownership isolation, token leakage, deletion, no-linkage, intake minimization, i18n/RTL and accessibility. | PASS |

## 5. Requirement / constraint / interface review

### REQ-0028 — documented necessity

The artifact contains an identity allowlist with a necessity column, limits account creation intake to necessary inputs and treats undocumented fields as defects. **PASS.**

### REQ-0029 — technically correct supported setup

The account requirements do not replace or alter platform DNS setup mechanisms and repeatedly preserve technical protection verification as separate from account ownership. Detailed platform automation remains with its owning tasks. **No contradiction found.**

### REQ-0034 / CON-0010 — dual-mode product scope

The artifact keeps the core safety journey fully usable without login and defines the optional parent account as bounded continuity/device-management scope. Mandatory login, child accounts, browsing/activity history and raw DNS administration are excluded. **PASS.**

### CON-0017 — multilingual/RTL technical capability

Auth/account/error/deletion/recovery strings and states are required to be localizable for English, Turkish and Arabic/RTL without implying official non-UK market activation. **PASS.**

### INT-0009 — implementation-ready UX contract

The artifact specifies lifecycle states, error/recovery/expiry behavior, input/data boundaries, security outcomes and downstream test cases. It intentionally leaves concrete L5/L6 mechanisms out while making required outcomes explicit. **PASS.**

### INT-0010 — QA-testable experience contract

Sixteen deterministic/synthetic test cases provide objective outcomes for accountless continuity, auth lifecycle, CSRF/session/ownership boundaries, deletion truth, localization and accessibility. **PASS for TSK-0312 scope.**

## 6. TSK-0229 no-linkage reconciliation

The artifact preserves the current accountless/persistent-domain separation:

- no automatic J0/J1-to-account join/conversion/promotion/linkage;
- account sign-in does not extend anonymous-state expiry;
- future transfer requires a separately approved dual-mode data-flow contract;
- account/device ownership does not substitute for technical protection verification;
- account deletion, anonymous-state deletion and DNS configuration removal remain separate operations.

No contradiction with current TSK-0229 was found.

## 7. Security/privacy boundary review

The artifact is deliberately a requirements-level contract, not a security architecture decision. It requires security outcomes without asserting an unproven implementation:

- secure session design remains L5-owned;
- concrete cookie/token/CSRF/session-store choices remain L5/L6;
- authorization and cross-account/device isolation must be enforced at the trusted boundary and later security-tested;
- provider terms/quotas/pricing/data transfers/subprocessors/privacy/production configuration remain downstream;
- no legal/privacy compliance conclusion is claimed.

This separation is consistent with current TSK-0140 and prevents TSK-0312 from silently passing later architecture/build/security tasks.

## 8. Behavioral/accessibility/source-evidence limits

- RSK-0002 remains open; no parent/user usability, comprehension, trust or account-uptake outcome is invented.
- Under current DEC-0052 sequencing, real-user testing does not block L4-L7 and begins after LG-09.
- Accessibility requirements are specified as downstream objective acceptance outcomes; no implemented WCAG pass is claimed by this requirements artifact.
- Current vendor/provider operational facts are not asserted beyond the canonical planned Google/Firebase route; provider currency review remains with the L5 provider/architecture task.

## 9. Contrary-evidence review

No current canonical source inspected contradicts the persisted TSK-0312 artifact. The artifact does not:

- make login mandatory;
- introduce password/SMS auth;
- authorize child accounts/history/surveillance/raw DNS admin;
- link anonymous J0/J1 automatically to an account;
- invent exact session duration/cookie/token/provider mechanics;
- claim provider/legal/privacy/security/build/release acceptance;
- claim real-user evidence;
- infer LG-06 PASS.

## 10. Deviations and unresolved downstream work

The following remain intentionally unresolved and do not block the bounded ACC-0312 requirements acceptance because their owning tasks occur downstream:

- current Google/Firebase terms/quotas/pricing/vendor/privacy/transfer/subprocessor review;
- exact OAuth/OIDC/Firebase integration and server-side session architecture;
- exact persistent schema/storage/retention/backup/deletion implementation;
- exact cookie/token/CSRF/session values/mechanisms;
- detailed dashboard/device interaction design;
- implementation and runtime security tests;
- real-user evidence;
- LG-06 and all later gates.

## 11. Analytical disposition

Every explicit ACC-0312 clause is present in the exact persisted artifact; its sole hard dependency is current PASS; current product/privacy/security/accessibility constraints are preserved; and no unresolved acceptance-blocking contradiction was found.

**Analytical result: ACC-0312 PASS candidate.**

TSK-0312 shall not be marked runtime PASS until a separate deterministic verification of the exact persisted artifact/current authority succeeds and that evidence is durably recorded/read back.
