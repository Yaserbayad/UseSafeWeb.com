# TSK-0329 — Parent Authentication and Account Interaction Prototype

**Version:** 1.0.0-post-cr0007  
**Status:** current L4 candidate for independent acceptance  
**Task:** TSK-0329 — Design and prototype Google sign-in, first-session account creation, and signed-in return interactions  
**Acceptance:** ACC-0329  
**Owner:** UX/UI  
**Action authority:** A4 / AUTO_ALLOWED  
**Date:** 2026-08-31  
**Build/provider/security approval:** none

## 1. Purpose and authority

This is the current interaction prototype for the optional Version-1 parent account branch. It consumes:

1. current accepted TSK-0328 information architecture/navigation model;
2. current accepted TSK-0312 parent authentication/account/session/minimal-intake requirements;
3. current CR-0006/DEC-0053 accountless-core + optional-account scope;
4. current CR-0007/DEC-0054 autonomous detailed-account-UX authority;
5. REQ-0028, REQ-0029, CON-0010, CON-0017 and INT-0009/INT-0010.

It prototypes product interactions only. Google/Firebase remains the planned sign-in route, not an approved provider/security/vendor architecture. Exact OAuth/OIDC/Firebase mechanics, cookies/tokens, CSRF implementation, storage schema, authorization, retention, backup, provider configuration, legal consent, implementation and production behavior remain downstream authority.

## 2. Binding interaction rules

1. **Account is optional.** A parent can start, configure, verify, understand, troubleshoot, recover and remove the complete core without login.
2. **Google sign-in is the only planned Version-1 account entry.** No UseSafeWeb password, SMS or child login is introduced.
3. **First-session account creation is explicit and minimal.** No child identity, demographic questionnaire or unnecessary provider-profile data is requested.
4. **No automatic J0/J1 promotion or linkage.** Sign-in/account creation never silently imports, joins, converts or extends anonymous journey state.
5. **Account state is protection-state neutral.** Sign-in success, valid session, account ownership or dashboard presence never creates technical `Verified` evidence.
6. **Provider/session failure is account-only.** Already configured DNS/core truth remains unchanged and signed-out core/help remains available.
7. **Ambiguous identity fails closed.** Never silently create a duplicate account, merge identities or fall back to password/SMS.
8. **Lifecycle actions are distinct.** Logout, account deletion, dashboard/device-record deletion, J0/J1 deletion and physical DNS removal are different operations.
9. **Data use is explained at the point of first account creation and remains reachable later.** The prototype does not invent a legal-consent requirement or compliance claim.
10. **All states are mobile-first, keyboard-accessible, screen-reader understandable and localizable to English/Turkish/Arabic+RTL without implying non-UK market activation.**

## 3. Entry contexts and exits

The account branch can begin from three justified contexts:

| Context | Entry | Why it exists | Safe signed-out exit |
| --- | --- | --- | --- |
| Public optional account access | Public `Sign in` → `AUTH-ENTRY` | Returning parent wants continuity/dashboard access. | Back to public page or Start setup. |
| Post-core optional continuity | `SCR-MAP` → `AUTH-ENTRY` | Parent has already received core value and optionally wants future continuity. | Exit/continue signed out; completed core remains unchanged. |
| Expired/revoked session | Account-only action → `AUTH-REAUTH` | Re-establish authorization for an account-only action. | Signed-out Help or Start setup; no DNS-state change. |

No account entry is a predecessor to `Start setup`.

## 4. Logical prototype screens

Each screen is a logical interaction state, not a commitment to a separate URL. Provider/session identifiers must never appear in user-visible URLs, analytics or copy.

| Screen ID | Purpose / user goal | Primary control | Secondary / escape | Requirement trace |
| --- | --- | --- | --- | --- |
| `AUTH-ENTRY` | Understand optional continuity and choose whether to sign in. | **Continue with Google** | **Continue without account**; Back | REQ-0028; CON-0010; CON-0017; TSK-0328; TSK-0312; INT-0009; INT-0010 |
| `AUTH-PROVIDER-PENDING` | Understand that browser/provider handoff is in progress. | Provider handoff / wait | Cancel/back where provider allows | REQ-0028; CON-0010; TSK-0312; INT-0009; INT-0010 |
| `AUTH-CALLBACK-RESOLVING` | Resolve provider result to one known account/session outcome without duplicate creation. | Automatic resolution | Safe error/accountless fallback | REQ-0028; CON-0010; TSK-0312; INT-0009; INT-0010 |
| `AUTH-FIRST-SESSION` | Understand minimum account data use before first product-account creation. | **Create my account** | **Not now** → signed-out return | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `AUTH-CREATE-PENDING` | Prevent duplicate actions while first product-account creation resolves. | Pending state | No duplicate submit; safe error if outcome unknown | REQ-0028; CON-0010; TSK-0312; INT-0009; INT-0010 |
| `AUTH-ERROR` | Explain provider/sign-in/account/session failure factually and preserve core access. | **Try again** when safe | **Continue without account**; Help | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `AUTH-RETURN` | Resolve an existing signed-in/returning parent to the authorized dashboard state. | **Go to devices** / automatic safe return | Start new setup; Help | REQ-0028; CON-0010; CON-0017; TSK-0328; TSK-0312; INT-0009; INT-0010 |
| `AUTH-REAUTH` | Re-establish authorization after expiry/revocation before account-only actions. | **Continue with Google** | Signed-out Help; Start setup | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `AUTH-ACCOUNT` | Understand account/session options and reach data-use, logout or deletion entry. | Contextual account action | Back to Dashboard | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `AUTH-DATA-USE` | Revisit what account capability stores/does not store and what remains separate. | Back to account/first-session context | Privacy | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |
| `AUTH-LOGOUT-PENDING` | Resolve logout to success or uncertainty without false claims. | Pending | Help/retry on uncertain failure | REQ-0028; CON-0010; TSK-0312; INT-0009; INT-0010 |
| `AUTH-DELETE-ENTRY` | Understand account-deletion scope before entering the downstream deletion flow. | **Continue to delete account** | Cancel/back | REQ-0028; CON-0010; CON-0017; TSK-0312; INT-0009; INT-0010 |

## 5. Screen prototype details

### 5.1 `AUTH-ENTRY` — optional sign-in choice

**Heading:** Keep your devices easier to manage  
**Body:** UseSafeWeb works without an account. Sign in only if you want to manage saved device records and return to them later.  
**Primary:** Continue with Google  
**Secondary:** Continue without account  
**Utility:** Learn what account data is used

Interaction requirements:

- `Continue without account` returns to the exact safe prior accountless/public context.
- The signed-out option must be visually normal and fully usable; it must not look like an error or degraded safety path.
- No email/password/phone/child-name fields appear.
- Sign-in does not promise that the current device will automatically appear in Dashboard.

### 5.2 `AUTH-PROVIDER-PENDING` — provider handoff

**Heading:** Continue with Google  
**Body:** A Google sign-in window/page is being used for your optional parent account.  
**Status:** In progress

Interaction requirements:

- repeated activation is disabled while the same initiation is pending;
- browser/provider cancel returns to a known signed-out state;
- no raw provider token, internal ID or callback detail is displayed;
- if the provider cannot be reached, route to `AUTH-ERROR` with accountless continuation.

### 5.3 `AUTH-CALLBACK-RESOLVING` — known outcome boundary

This is an internal-facing loading/resolution state with accessible status text such as **Finishing sign-in…**.

Possible resolved outcomes only:

1. known existing parent account → establish valid session → `AUTH-RETURN`;
2. valid provider identity with no product account → `AUTH-FIRST-SESSION`;
3. user/provider cancellation → safe signed-out prior context;
4. provider/network/error → `AUTH-ERROR`;
5. identity/account binding ambiguous → fail closed → `AUTH-ERROR` with recovery guidance.

The interaction must be idempotent from the user perspective: reload/back/retry cannot silently create multiple product accounts or apply a destructive action twice.

### 5.4 `AUTH-FIRST-SESSION` — first-session account creation

**Heading:** Create your optional UseSafeWeb account  
**Body:** Your account is for returning to saved device records and account-only controls. Core setup and protection do not require an account.

**What this account needs:**

- an internal account reference;
- Google as the authentication provider;
- the minimum provider-bound identity reference required to recognize the same parent account;
- account/session lifecycle metadata needed for secure account access.

**Not required for account creation:**

- child name/account/age/birth date;
- phone number/SMS login;
- UseSafeWeb password;
- browsing, DNS-query, visited-domain or activity history;
- device nickname before the parent explicitly chooses Add device;
- provider profile image/display name/email merely because the provider offers them.

**Primary:** Create my account  
**Secondary:** Not now  
**Link:** How account data is used → `AUTH-DATA-USE`

Rules:

- `Not now` creates no product account and returns safely signed out.
- Creating the account does not import J0/J1 or create a device record automatically.
- Creating the account does not change any Phone/Internet/Services protection state.
- No legal-consent checkbox is invented by this task; later legal/privacy authority may add an actually required consent without changing the accountless-core rule unless owner authority changes scope.

### 5.5 `AUTH-CREATE-PENDING` — first-session mutation pending

**Heading:** Creating your account…  
**Accessible status:** Account creation is still being confirmed.

Rules:

- disable duplicate creation submission;
- if completion is confirmed, establish the authorized session and go to `AUTH-RETURN` / empty `DASH-HOME`;
- if failure is confirmed, `AUTH-ERROR` may offer a safe retry;
- if outcome is unknown, do not claim success or create another account blindly; require resolution/recovery first.

### 5.6 `AUTH-ERROR` — provider/account failure

Use one error surface with a factual reason class, not sensitive technical detail.

| Error class | User-facing meaning | Primary recovery | Core effect |
| --- | --- | --- | --- |
| Provider unavailable | Google sign-in is temporarily unavailable. | Try again later / retry when safe | None; Start setup/core remains available. |
| User cancelled | Sign-in was cancelled. | Return / try again | None. |
| Network interrupted | Sign-in outcome could not yet be confirmed. | Resolve current state, then retry | None; no duplicate account. |
| Identity/account binding ambiguous | Account access cannot be safely established. | Supported recovery/help | Account-only fails closed. |
| Session creation failed | Sign-in did not produce a usable UseSafeWeb session. | Safe retry/recovery | DNS/core unchanged. |
| Account/provider revoked/disabled | Account-only access is unavailable. | Re-auth/recovery if supported | DNS/core unchanged. |

Every error screen provides **Continue without account** or equivalent access back to public/core setup/help where context permits.

### 5.7 `AUTH-RETURN` — signed-in return

**Heading:** Welcome back  
**Body:** Your account is signed in. Device records are management references; their presence does not prove current protection.  
**Primary:** Go to devices  
**Secondary:** Start new setup  
**Utility:** Account / Help

Rules:

- valid session/ownership is required for account-only device data;
- returning to a saved device never upgrades its Protection Map state;
- stale/contradictory technical evidence must remain stale/uncertain/action-needed until the owning verifier updates it;
- if session validity becomes uncertain, route to `AUTH-REAUTH` before any account-only action.

### 5.8 `AUTH-REAUTH` — expiry/revocation

**Heading:** Sign in again to continue  
**Body:** Your account session has ended or cannot be used. This does not mean UseSafeWeb DNS stopped on any device.  
**Primary:** Continue with Google  
**Secondary:** Start setup / Help

On successful re-authentication, return only to a safe authorized account destination. Preserve non-sensitive navigation intent where possible; never replay a pending destructive action automatically.

### 5.9 `AUTH-ACCOUNT` — account/session hub

Account-only controls:

- Account data use → `AUTH-DATA-USE`
- Logout
- Delete account → `AUTH-DELETE-ENTRY`
- Back to Dashboard

No browsing/activity history, child profile, raw provider payload or AdGuard administration appears.

### 5.10 `AUTH-DATA-USE` — reusable data-use explanation

The explanation is concise and available both before first account creation and later from Account.

**Used for the optional account:** minimum provider identity binding, account/session lifecycle and explicit parent-owned device records/settings allowed by downstream contracts.  
**Not used as account product data:** browsing/query/activity history, child account/profile, raw DNS logs or unrestricted AdGuard administration.  
**Separate:** anonymous J0/J1 journey state, physical DNS configuration/removal and technical verification evidence remain governed by their own lifecycles.

The screen links to the current approved Privacy surface but does not claim legal compliance, no-logs status or provider approval.

### 5.11 Logout interaction

From `AUTH-ACCOUNT`, **Log out** initiates `AUTH-LOGOUT-PENDING`.

Success result:

- authenticated account access ends;
- account record/device records are not deleted;
- J0/J1 is not described as deleted;
- physical DNS is not described as removed;
- signed-out core/public Help/Start setup remains available.

Failure/uncertainty:

- account-only sensitive actions fail closed until session state is resolved;
- the UI does not claim successful logout without evidence;
- recovery may re-authenticate or resolve the session state.

### 5.12 `AUTH-DELETE-ENTRY` — deletion entry only

**Heading:** Delete your account  
**Body:** This starts removal of your UseSafeWeb account and account-owned device-management data under the approved deletion process. It does not remove UseSafeWeb DNS from a phone and does not automatically delete unrelated anonymous J0/J1 state.  
**Primary:** Continue to delete account  
**Secondary:** Cancel

This task prototypes the **entry and consequence explanation**. Exact destructive confirmation, deletion execution, retention/backup handling, provider unlink behavior and completion evidence remain with downstream owning deletion/data/security tasks.

## 6. First-session intake field/state prototype

This task does not choose database columns; it defines what the UI/product may request or expose.

| Semantic item | UI state | First-session rule | Error state |
| --- | --- | --- | --- |
| Google provider authentication | system/provider interaction | Required for optional account route | Provider unavailable/cancel/error → `AUTH-ERROR`. |
| Provider-bound stable identity reference | hidden system necessity | Retain only as required by approved downstream auth architecture | Missing/invalid/ambiguous → fail closed; no account creation. |
| Internal parent account ID | hidden system necessity | Created after confirmed first-session account creation | Creation unknown/failure → do not claim account exists. |
| Provider type | hidden system value | `Google` for current Version-1 route | Unknown provider is unsupported unless later approved. |
| Account/session lifecycle metadata | hidden system necessity | Minimum only under downstream session architecture | Invalid/revoked/expired → `AUTH-REAUTH` / account-only denial. |
| Email | not requested by default | Not product-required merely because provider may supply it | Do not invent a required email field. |
| Display name/profile image | not requested by default | Not product-required | Do not persist/display merely because available. |
| Child identity fields | prohibited | Never required for parent account creation | Presence/request is a defect. |
| Phone/SMS/password | prohibited route | No local password/SMS auth | Presence is a scope defect. |
| Device nickname | not part of account creation | Requested only later on explicit Add device when needed; safe generic default allowed | No child identity required. |

Unknown/unapproved intake fields are defects and must not silently expand persistence.

## 7. Back, refresh, retry and resume behavior

| Situation | Required prototype behavior |
| --- | --- |
| Back from `AUTH-ENTRY` | Return to exact safe prior public/core context; no account mutation. |
| Back/cancel during provider handoff | Resolve to signed-out/cancelled state; no silent account creation. |
| Refresh callback/resolving state | Resolve the same attempt idempotently to one known outcome; no duplicate account. |
| Refresh `AUTH-FIRST-SESSION` before create | Still no product account; minimum data explanation remains. |
| Retry after confirmed provider error | New safe sign-in initiation allowed; prior uncertain attempt must not cause duplicate account. |
| Network loss after Create my account | Show pending/unknown until authoritative outcome resolves; never blind-create again. |
| Session expires on account page | `AUTH-REAUTH`; safe non-sensitive return destination may be preserved. |
| Session expires before destructive action | Re-authenticate first, then require the destructive action to be intentionally re-entered; never auto-replay. |
| Anonymous J0/J1 expires while sign-in/account exists | Anonymous state expires independently; account session does not extend or recover it automatically. |
| Browser returns to core setup after account flow | Re-establish truthful accountless state/evidence as required; account sign-in cannot manufacture resume state. |

## 8. Data-use and privacy copy constraints

Permitted factual concepts:

- optional account for continuity/device-management;
- minimum account/session identity binding;
- explicitly managed device records;
- no account requirement for core setup;
- no browsing/query/activity-history product;
- technical verification remains separate.

Prohibited unsupported claims:

- “no logs” without owning evidence;
- “fully private”, “100% safe”, “Google-approved” or legal-compliance claims;
- “your child is protected” based on account/sign-in/device presence;
- claims that logout/account deletion removes device DNS unless that separate workflow is actually completed and verified.

## 9. Accessibility, responsive and RTL interaction contract

All logical states inherit WCAG 2.2 AA target and mobile-first behavior.

- Primary/secondary actions are native controls with visible focus and usable accessible names.
- Provider pending, account creation pending and callback resolving use `role=status`/equivalent live status without trapping focus on an indefinite spinner.
- Error summary receives programmatic attention after a failed transition and identifies the next corrective action without exposing sensitive details.
- Destructive account-deletion entry has explicit textual consequences before the downstream destructive confirmation.
- Keyboard order follows visual/task order; Back/Cancel is always reachable without pointer input.
- No state meaning is communicated by color alone.
- English/Turkish/Arabic strings are localizable; RTL reverses directional layout/icons where semantic direction requires it but does not reverse logical progress meaning.
- Provider brand rendering must follow later approved provider guidelines; this task does not invent Google branding assets.

## 10. Deterministic interaction cases

| Test ID | Scenario | Expected prototype outcome |
| --- | --- | --- |
| `AUTH-P01` | Parent ignores Sign in and starts setup | Core remains fully reachable/completable signed out. |
| `AUTH-P02` | Parent opens optional account entry | `AUTH-ENTRY` explains continuity and offers equal safe signed-out escape. |
| `AUTH-P03` | Existing parent completes Google sign-in | Known account/session resolves to `AUTH-RETURN` then Dashboard; no password/SMS path. |
| `AUTH-P04` | New provider identity signs in | Route reaches `AUTH-FIRST-SESSION` before product-account creation; minimal data use is explained. |
| `AUTH-P05` | New parent chooses Not now | No product account/device record is created; safe signed-out return. |
| `AUTH-P06` | New parent creates account | Exactly one product-account creation resolves; no J0/J1 import/device auto-add/protection upgrade. |
| `AUTH-P07` | Provider unavailable | `AUTH-ERROR`; retry/help/accountless continuation; DNS/core unchanged. |
| `AUTH-P08` | User cancels provider | Signed-out known state; no silent account creation. |
| `AUTH-P09` | Callback/network outcome uncertain | Pending/resolution state; no duplicate account/retry mutation until authoritative outcome known. |
| `AUTH-P10` | Identity binding ambiguous | Account access fails closed; no merge/duplicate/password/SMS fallback. |
| `AUTH-P11` | Returning session is valid | `AUTH-RETURN`/Dashboard available; device presence does not imply current `Verified`. |
| `AUTH-P12` | Session expires/revokes on account-only action | `AUTH-REAUTH`; core/help still reachable; DNS state unchanged. |
| `AUTH-P13` | Re-auth succeeds after expiry | Return to safe authorized destination; no pending destructive action auto-replayed. |
| `AUTH-P14` | Parent logs out | Session access ends only; account/device records/J0-J1/DNS removal are not claimed. |
| `AUTH-P15` | Logout outcome uncertain | Account-only sensitive actions fail closed; no false success. |
| `AUTH-P16` | Parent opens account deletion | `AUTH-DELETE-ENTRY` explains account/device-management scope vs J0/J1 and physical DNS separation. |
| `AUTH-P17` | Minimal-intake audit | No child identity, phone/SMS/password, browsing/query/activity data, or unnecessary provider-profile field is requested. |
| `AUTH-P18` | Back/refresh/retry across sign-in/create | One known state is recovered; no duplicate account or silent mutation. |
| `AUTH-P19` | English/Turkish/Arabic+RTL and keyboard/screen-reader review | All logical states remain understandable/operable and no non-UK market-readiness claim is inferred. |
| `AUTH-P20` | Data-use explanation review | Explains minimum account purpose/data and separation truth without unsupported privacy/legal/provider claims. |

## 11. ACC-0329 coverage

Current ACC-0329 requires the prototype to cover Google sign-in, first-session account creation, signed-in return, errors/provider outage, logout, session expiry, account deletion entry, intake field states, back/resume and data-use explanation with minimal identity collection.

This prototype covers each clause through explicit logical screens, transitions, error/recovery behavior, field-state rules and 20 deterministic cases while preserving:

- complete login-free core value;
- Google-only planned Version-1 sign-in route without password/SMS expansion;
- minimum identity collection and no child/surveillance data;
- no automatic J0/J1 linkage/expiry extension;
- account/device state neutrality relative to technical protection verification;
- truthful lifecycle separation;
- accessible mobile-first and RTL-ready interaction behavior.

**Candidate disposition:** ACC-0329 is ready for independent post-publication verification. TSK-0329 remains non-PASS until the exact persisted prototype and structured interaction model are independently verified, evidence is durably recorded, and `CURRENT_STATE.md` is reconciled/read back.
