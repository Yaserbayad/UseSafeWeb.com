# TSK-0312 — Parent Authentication, Account/Session and Minimal Intake Requirements

**Task:** TSK-0312 — Specify parent authentication, account/session, and minimal intake requirements  
**Acceptance:** ACC-0312  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Package:** PKG-06  
**Version:** 1.0.0  
**Date:** 2026-08-31  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE  
**Authority:** current TSK-0140 PASS + DEC-0053/CR-0006 + DEC-0054/CR-0007 + REQ-0028/0029/0034 + CON-0010/0017 + INT-0009/0010

## 1. Purpose and boundary

This artifact defines the Version-1 product/UX requirements for the optional parent authentication branch, account/session lifecycle and minimum intake. It is an implementation contract input, not the L5 authentication/provider/security architecture and not an implementation result.

The complete core First Phone Safety Setup journey remains usable without login. The account branch adds bounded continuity and device-management value only. It must not become a prerequisite for core safety value, technical DNS protection, or Protection Map verification.

No real-parent/user behavioral evidence is claimed. Under current sequencing, real-user validation begins only after LG-09; this L4 artifact uses current product authority plus objective product/privacy/security/accessibility review.

## 2. Authentication method requirement

### AUTH-01 — Planned Version-1 sign-in route

- Version 1 shall provide **Google social sign-in** as the planned parent authentication route.
- Google/Firebase remains a planned provider route only. Provider selection/terms/quotas/pricing, transfer/subprocessor/privacy review, exact OAuth/OIDC/Firebase mechanics, server-side session architecture, secrets, migration/exit and production configuration remain L5+ acceptance work.
- No local password authentication is introduced.
- No SMS/phone-number authentication is introduced.
- Adding password, SMS, another identity provider, mandatory login, or child authentication requires its own later authority where applicable.

### AUTH-02 — Account branch is optional

- A parent may complete the accountless core before ever signing in.
- Sign-in failure, cancellation, provider unavailability or session expiry shall not invalidate already completed accountless setup or falsely report DNS protection as removed.
- Account-required controls shall be visibly distinguished from accountless core controls.

## 3. Minimum parent identity and account record

The product requirement is **data minimisation by allowlist**. Downstream architecture may choose different field names, but it shall not expand the semantic data set without an owning requirement/decision.

| Required semantic field | Necessity | Product rule |
| --- | --- | --- |
| Opaque internal parent-account identifier | Stable internal ownership/authz reference without using human-readable identity as the primary key | Required after account creation; not exposed as a meaningful public identifier. |
| Authentication provider type | Distinguishes the approved sign-in route and supports lifecycle/migration logic | Required; Version 1 value is `Google` unless later authority changes it. |
| Provider-bound stable identity reference | Prevents ambiguous account binding and supports re-authentication | Required only in the form needed by the approved L5 provider architecture; raw provider payloads are not retained merely because available. |
| Account lifecycle status | Supports active, deletion-pending/deleted, revoked/disabled and recovery/error semantics | Required; exact storage representation is downstream. |
| Creation/update lifecycle timestamps | Supports lifecycle integrity, deletion/revocation/recovery and audit of account-state changes | Required only at account/lifecycle level; not a browsing/activity timeline. |
| Minimum session-control metadata | Supports session validity, revocation and re-authentication | Required only as defined by the approved L5 session architecture; no browsing/activity data. |

### Optional/conditional identity data

- Email address, display name or profile image shall **not** be product-mandatory merely because the identity provider can supply them.
- A human-readable email/name may be retained only when a downstream approved requirement establishes a necessary account/recovery/contact/display purpose and the privacy/data-flow contract authorizes it.
- The UI shall not require a child name, child email, child account, birth date, precise age, phone number, address, location, contacts, social identity or other child/family profile data for parent sign-in.

## 4. Minimum intake requirements

### INTAKE-01 — Sign-in/account creation

Before or during optional account creation, the product may collect only:

1. the provider authentication response needed by the approved authentication architecture;
2. the minimum account lifecycle fields above; and
3. explicit parent choices strictly necessary to create/use the optional account capability.

No survey, demographic profile or first-phone questionnaire is required merely to create an account.

### INTAKE-02 — Device-management intake

When the parent explicitly chooses to add/manage a device, the minimum product intake may include only fields required by the owning device-management requirements, such as a parent-chosen device nickname and supported-platform/setup context. The product shall not require a child identity to own/manage a device record.

Exact persistent device schema and ownership mechanics are downstream tasks. Account ownership or a stored device record never substitutes for technical DNS/protection verification.

### INTAKE-03 — Accountless-state separation

- Anonymous/accountless J0/J1 state remains governed by the accepted TSK-0229 contract.
- No automatic J0/J1-to-account join, conversion, promotion or linkage is authorized by this task.
- Signing in shall not extend anonymous-state expiry.
- Any future intentional transfer from anonymous journey state to an account requires a separately approved dual-mode data-flow contract.

## 5. Explicit prohibited data and behavior

The parent authentication/account intake shall not collect, create or expose as Version-1 product scope:

- password credentials managed by UseSafeWeb;
- SMS/phone-number authentication data;
- child accounts or child login credentials;
- browsing history, DNS-query history, visited/top domains, app/activity history or engagement profiling;
- persistent child/family behavioral profiles;
- messages, contacts, photos, precise location or social-content monitoring;
- unrestricted/raw AdGuard administrative access or credentials;
- payment/card data as a condition of account creation or core safety value;
- automatic anonymous-state-to-account linkage;
- unnecessary identity-provider profile data;
- identity fields whose necessity is undocumented.

Unknown/unapproved intake fields shall be treated as defects, not silently accepted as product scope.

## 6. Account and session lifecycle

The UX and downstream implementation shall represent at least these product states distinctly:

1. **Accountless / signed out** — core journey remains available.
2. **Sign-in initiated** — provider handoff/pending state; repeated initiation must not create duplicate product accounts silently.
3. **Sign-in cancelled** — return safely to the prior accountless/account surface without loss of core journey state.
4. **Sign-in failed** — factual error with retry and accountless continuation; no false protection-state change.
5. **Authenticated / session active** — account-only dashboard/device functions available subject to authorization.
6. **Session expired / invalid** — account-only functions require re-authentication; core accountless journey remains available.
7. **Provider/account revoked or disabled** — fail closed for account-only access and provide a truthful recovery/re-authentication path where supported.
8. **Signed out** — local/account session access ends; logout does not claim that DNS configuration was removed from a device.
9. **Deletion requested/in progress** — prevent ambiguity about whether the account record, anonymous journey data or device DNS configuration is being removed.
10. **Account deleted** — active account/session access is no longer available; any separately configured DNS removal remains a separate user action unless the owning implementation requirement explicitly proves otherwise.
11. **Recovery/re-authentication required** — clear path back to an authenticated state without creating an unauthorized duplicate account.

Exact idle/absolute session duration values are **not invented by this L4 task**; L5 security/privacy architecture shall choose and justify them, and the UX shall handle those expiry semantics explicitly.

## 7. Logout, revocation and deletion requirements

### ACCOUNT-01 — Logout

- Logout shall terminate the applicable UseSafeWeb authenticated session according to the approved implementation.
- Subsequent account-only requests shall require valid authentication.
- Logout shall not be represented as account deletion, anonymous-state deletion or device DNS removal.

### ACCOUNT-02 — Revocation/invalid session

- Revoked, expired, invalid or otherwise unusable sessions shall fail closed for account-only operations.
- The user shall receive a non-sensitive error and a re-authentication/recovery path.
- The product shall not downgrade security by silently creating a new account when identity binding is uncertain.

### ACCOUNT-03 — Account deletion

- Account deletion shall be an explicit, understandable action with confirmation appropriate to its consequence.
- It shall invalidate active account sessions and initiate removal of account/device-ownership data governed by the downstream approved storage/retention/deletion contract.
- Account deletion shall not be described as deleting unrelated anonymous J0/J1 state unless that state is actually within the same deletion operation and the approved data-flow contract proves it.
- Account deletion shall not be described as removing DNS configuration from a phone unless that technical removal is actually performed and verified by its owning workflow.

## 8. Validation and input rules

- Every account/intake field shall have a documented necessity traceable to this artifact or a later approved owning requirement.
- Client-side validation may improve UX but shall not be the sole security/integrity control; downstream implementation shall enforce authoritative validation at the trusted application boundary.
- Inputs shall have explicit type/format/length/allowed-value rules in the implementation specification before build.
- Unknown fields and unsupported state transitions shall fail safely rather than expand persistence silently.
- User-facing validation errors shall identify the corrective action without exposing secrets, tokens, internal identifiers or security-sensitive detail.
- Repeated/retried account actions shall be designed to avoid unintended duplicate accounts or duplicate destructive actions.

This section defines outcomes; exact schemas, libraries, cookie settings, token handling and validation code remain L5/L6 work.

## 9. Session and CSRF security requirements

These are mandatory acceptance outcomes for downstream architecture/build; this L4 task does not choose the concrete implementation:

- Authenticated account operations shall use a secure session design approved by L5 security/privacy architecture.
- State-changing authenticated browser operations shall include implementation-appropriate CSRF protection or an independently justified architecture that is not susceptible to cross-site request forgery.
- Session identifiers/tokens shall not be exposed in user-visible URLs, analytics events, logs or content.
- Session validity and account authorization shall be checked server-side/trusted-side for account-only operations; UI visibility alone is not authorization.
- Session revocation/expiry shall take effect for account-only access according to the approved architecture.
- Authentication shall not grant raw AdGuard administration.
- Parent/account/device ownership shall not be treated as proof of DNS/protection state.

Concrete cookie attributes, token formats, provider SDKs, key management, CSRF mechanism, session storage and expiration values remain L5/L6 decisions and must be independently security-tested before release.

## 10. Error, resume and expiry behavior

| Situation | Required product behavior |
| --- | --- |
| Provider unavailable | Show factual temporary failure; allow retry and accountless core continuation. |
| User cancels sign-in | Return to safe prior state; no account silently created. |
| Identity/account binding is ambiguous | Fail closed for account access; do not merge/create identity automatically. |
| Session expires during dashboard use | Preserve non-sensitive UI context where safe; require re-authentication before account-only action; do not imply DNS protection stopped. |
| Network interruption during sign-in | Resolve to a known signed-in/signed-out state before accepting an account-only action; safe retry permitted. |
| Logout succeeds | Account-only access ends; accountless core remains available. |
| Logout/revocation fails or state is uncertain | Fail closed for sensitive account actions and present recovery guidance; do not claim successful logout/revocation without evidence. |
| Account deletion is interrupted | Represent deletion as pending/failed/unknown as appropriate; never claim completion without verified downstream result. |
| Provider identity changes/vanishes | Require the approved recovery/migration behavior; no insecure fallback to password/SMS or silent duplicate account. |

## 11. Accessibility, localization and content requirements

- Sign-in, consent/choice, account states, errors, logout, deletion, recovery and re-authentication surfaces inherit the project WCAG 2.2 AA target and responsive mobile-first requirement.
- Every control shall have a clear accessible name, purpose, focus behavior and error association in the downstream interaction specification.
- Authentication/account strings and error states shall be localizable for English, Turkish and Arabic, including RTL layout capability.
- Technical availability of Turkish/Arabic shall not be presented as official non-UK market/legal/support readiness without LG-16.
- Security/privacy wording shall remain factual and shall not claim complete safety, no-logs, legal compliance, provider approval or protection verification without evidence.

## 12. Required deterministic/synthetic test cases

Real-user testing is not a prerequisite for this task. The following cases are minimum objective acceptance inputs for later design/build verification:

| Test ID | Scenario | Expected result |
| --- | --- | --- |
| AUTH-T01 | Complete core journey without login | Core safety setup remains accessible and completable without account creation. |
| AUTH-T02 | Successful Google-route sign-in | One authorized account session is established; no password/SMS path appears. |
| AUTH-T03 | Cancel provider sign-in | No account silently created; user returns safely and can continue accountless. |
| AUTH-T04 | Provider/sign-in error | Clear retry/error state; accountless core remains usable. |
| AUTH-T05 | Repeated sign-in initiation/retry | No unintended duplicate product account or duplicate destructive action. |
| AUTH-T06 | Expired/invalid/revoked session | Account-only request fails closed and requires re-authentication/recovery. |
| AUTH-T07 | Logout then account-only action | Account-only action is denied until valid re-authentication. |
| AUTH-T08 | CSRF attempt against state-changing account action | Request is rejected or architecture is independently proven not susceptible under the approved L5 design. |
| AUTH-T09 | Unauthorized other-account/device access attempt | Access is denied; ownership isolation remains intact. |
| AUTH-T10 | Session/token leakage inspection | No session/token value appears in URL, analytics, logs or user-visible content under approved implementation. |
| AUTH-T11 | Account deletion flow | Explicit confirmation; sessions invalidated; truthful pending/success/error state; no false DNS-removal claim. |
| AUTH-T12 | Sign in while J0/J1 exists | No automatic J0/J1-to-account promotion/linkage; anonymous expiry is not extended. |
| AUTH-T13 | Account deletion vs DNS removal | UI distinguishes the two operations and does not claim one completes the other. |
| AUTH-T14 | Minimal intake audit | Every stored/collected account/intake field has documented necessity; prohibited/unknown fields are absent/rejected. |
| AUTH-T15 | English/Turkish/Arabic + RTL rendering | All auth/account/error/deletion/recovery states are localizable and layout remains usable; market-readiness claim is not inferred. |
| AUTH-T16 | Keyboard/screen-reader/error flow | Auth/account controls and errors meet the owning accessibility acceptance criteria when implemented. |

## 13. Traceability to current authority

| Authority | TSK-0312 requirement carried forward |
| --- | --- |
| TSK-0140 current product brief | Accountless core + optional parent account; planned Google/Firebase route; no mandatory login/history/child account/raw DNS admin; truthful lifecycle and downstream security/privacy boundaries. |
| DEC-0053 / CR-0006 | Optional Version-1 parent account, secure session requirements, minimum parent/device ownership persistence and lightweight dashboard/device management are in scope. |
| DEC-0054 / CR-0007 | Detailed in-scope account/dashboard design work is autonomous; no ceremonial owner checkpoint is added. |
| REQ-0028 | Every interaction/field/account step has documented necessity. |
| REQ-0029 | Setup automation/fallback remains technically correct; account scope does not override platform setup truth. |
| REQ-0034 | Both accountless core and optional-account path, lifecycle, deletion/recovery/help/unsupported states are specified without surveillance. |
| CON-0010 | Account scope stays minimum/privacy-safe/non-surveillant and never becomes mandatory for core value. |
| CON-0017 | English/Turkish/Arabic + RTL technical capability is preserved without implying non-UK market activation. |
| INT-0009 | Engineering receives exact states/errors/recovery/accessibility and acceptance criteria rather than inventing them during build. |
| INT-0010 | QA receives objective testable experience outcomes. |
| TSK-0229 accepted contract | Accountless J0/J1 remains separate; no automatic linkage/promotion or expiry extension. |

## 14. Downstream ownership / non-approval boundary

This artifact does **not** approve or complete:

- Firebase/Google vendor selection acceptance, terms/quotas/pricing, transfers/subprocessors or provider configuration;
- exact OAuth/OIDC/Firebase protocol implementation;
- database/schema/storage/retention/backup architecture;
- concrete cookie/token/session/CSRF implementation;
- authentication/authorization/IDOR/ClientID security test results;
- dashboard interaction design beyond the requirements above;
- implementation, deployment or production behavior;
- LG-06 or any later gate;
- legal/privacy/consent compliance conclusion;
- real-user usability, comprehension, trust or account-uptake evidence.

Those remain with their owning L4/L5/L6/L7 tasks and gates.

## 15. ACC-0312 coverage statement

ACC-0312 requires requirements that define Google social sign-in; account/session lifecycle; minimal required identity fields; logout/revocation/deletion; intake fields; prohibited data; validation; errors; resume/expiry behavior; CSRF/session protections; and test cases, with no password or SMS authentication introduced without a later decision.

Every clause is explicitly specified above. No material product-scope change is introduced and no downstream acceptance is inferred.

**Candidate disposition:** ACC-0312 is ready for independent post-publication verification; TSK-0312 remains non-PASS until that verification and durable runtime reconciliation succeed.
