# TSK-0319 — Current Automated Verification, Troubleshooting, Recovery and Point-of-Need Help Design

**Task:** `TSK-0319 — Design automated verification, issue-specific troubleshooting, safe reset/reinstall/remove, and point-of-need help`  
**Acceptance:** `ACC-0319 / VER-0319 / EVD-0319`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Priority:** HIGH  
**Version:** `2.0.0-post-CR-0008`  
**Date:** 2026-09-01  
**Authority:** `DEC-0053/CR-0006`, `DEC-0054/CR-0007`, `DEC-0055/CR-0008`; current `TSK-0315` dual-mode service blueprint; current `TSK-0320` protection-state/copy contract; current account/session/device lifecycle and no-routine-human-support contracts.  
**Status:** current L4 design candidate pending independent acceptance verification; no implementation, deployment, gate PASS or public release is inferred by this artifact alone.

## 1. Current Version-1 boundary

Version 1 has two interoperable but non-collapsed modes:

1. **complete accountless core** — discovery, setup, technical verification, troubleshooting, recovery and removal remain usable without login; and
2. **optional parent-account mode** — parent sign-in/session, minimum parent/device ownership persistence, lightweight dashboard/device management, and account/device lifecycle operations may be used without becoming prerequisites for core protection.

Troubleshooting must preserve that split. Sign-in, account ownership, dashboard registration, stored device state or parent confirmation never substitutes for current technical protection evidence. Anonymous J0/J1 state is not silently imported into persistent account state and account return does not extend expired anonymous state.

This design authorizes no browsing/query/activity history, raw DNS history, child account/profile, unrestricted DNS administration, browser-visible AdGuard administration secret, credentials collection, or surveillance-like diagnostic persistence.

## 2. Deterministic troubleshooting rules

1. **Classify before remedy.** Route by current issue/state, not a generic retry loop.
2. **System evidence before device blame.** Check service/verifier/provider state where privacy-safe evidence can rule out needless device changes.
3. **Truthful protection state is invariant.** Use the current TSK-0320 states: `protected/verified`, `configured/parent-confirmed`, `action-needed`, `not-covered`, `uncertain/error`, `removed`.
4. **Only current qualifying technical evidence may produce `protected/verified`.** Account/session/dashboard/device ownership is context, never protection proof.
5. **Retry only after changed evidence.** A materially equivalent failed attempt cannot loop.
6. **Unknown consequential results stop replay.** Destructive or ownership-changing operations with unknown outcome require deterministic reconciliation before retry.
7. **Recovery remains reachable without login.** Account/provider/dashboard failure cannot trap a parent inside the core DNS removal/recovery path.
8. **No unrelated-security weakening.** Do not instruct disabling required work/school/security management, VPN or privacy controls merely to obtain a green state.
9. **No surveillance diagnostics.** Routine diagnosis uses synthetic tests, approved state/configuration facts and minimum routing information only.
10. **Human/operator involvement is exceptional.** Ordinary completion remains self-service; exceptional routes are named and criterion-driven.

## 3. Privacy-safe automatic-check contract

| Check | Purpose | Minimum permitted evidence | Result classes | Prohibited inference/data |
| --- | --- | --- | --- | --- |
| `CHK-SVC-HEALTH` | Detect service/verification outage before changing user configuration. | Non-identifying service health and synthetic endpoint evidence. | healthy / degraded / unavailable / unknown | No user request history; unknown is not healthy. |
| `CHK-SUPPORT-TUPLE` | Determine whether the current device/OS/network path is covered. | Necessary device family/coarse OS/support facts and current known conflict facts. | supported / conditional / not-covered / unknown | No device fingerprint, serial, child identity or broad inventory. |
| `CHK-DNS-PATH` | Test whether the intended approved encrypted resolver path is active for the supported tuple. | Controlled/synthetic request to approved verification endpoints. | verified-path / failed / uncertain | Presence of a profile/provider/ClientID is not verification. |
| `CHK-FILTER` | Test approved allow/block semantics. | Controlled synthetic fixtures only. | pass / fail / uncertain | No real browsing/domain history. |
| `CHK-CONFLICT` | Identify a known resolver/tunnel/context conflict where safely observable. | Minimum non-invasive state or parent-confirmed current fact. | known-class / none-determined / unknown | No unrelated traffic inspection. |
| `CHK-PROVIDER` | Classify optional sign-in/provider-return condition. | Provider/session result code and nonce/state validity needed for the current flow. | pending / cancelled / failed / returned / unknown | Never request provider password/token or infer success from redirect alone. |
| `CHK-SESSION` | Classify current optional account session. | Minimum current session validity/revocation/expiry evidence. | active / expired / revoked / absent / unknown | Session presence is not protection evidence. |
| `CHK-OWNERSHIP` | Verify authorization for a persistent device-management operation. | Minimum parent/device ownership reference and operation target. | authorized / denied / stale / unknown | Ownership does not prove physical DNS state. |
| `CHK-RECOVERY` | Confirm ordinary connectivity after physical UseSafeWeb DNS removal/reset. | Neutral synthetic connectivity/DNS check. | normal-restored / still-failed / uncertain | Normal recovery does not mean UseSafeWeb protection remains active. |
| `CHK-JOURNEY-STATE` | Decide whether anonymous J0/J1 can resume. | Current permitted J0/J1 state/token only. | resume / restart / expired-deleted | No recovery via email/IP/fingerprint/account linkage. |

All checks are design contracts for later implementation/verification. They do not claim an implemented remote inspection capability.

## 4. Common triage sequence

For every ordinary issue:

1. Preserve the current truthful TSK-0320 state; never optimistically promote it.
2. Determine whether the issue is accountless-core, optional-account/session/dashboard, ownership/lifecycle, service/provider, compatibility, or removal/recovery.
3. Run only privacy-safe checks that materially reduce ambiguity.
4. Select the smallest issue-specific branch below.
5. Permit recheck only after a material state/configuration/service/provider change.
6. If no safe supported repair remains, end in `uncertain/error`, `not-covered`, or `removed` rather than guessing.
7. Keep Help/Exit/physical DNS removal reachable regardless of optional-account state.

## 5. Accountless-core decision trees

### DT-01 — Unsupported or unknown device/OS/path

- Run `CHK-SUPPORT-TUPLE`.
- `not-covered` -> show `Not covered`, exact boundary and safe exit; do not invent another resolver/VPN/profile.
- `unknown` -> request only the one necessary routing fact, then one re-evaluation.
- unresolved -> `Protection status could not be verified` or `Not covered` according to current support evidence.
- supported -> route to the exact current platform setup path.

### DT-02 — Android Private DNS cannot be applied or verified

- Confirm the current approved hostname/instruction rather than URL/port improvisation.
- Run `CHK-SVC-HEALTH` before repeated device changes.
- Service degraded/unavailable -> stop configuration loop; show truthful service condition and removal option.
- Service healthy -> run `CHK-DNS-PATH`; route known network/tunnel conflict to DT-06.
- Managed/locked setting -> current `not-covered`/authority boundary; never bypass management.
- Permit one source-backed setting correction followed by one recheck after the change.
- Continued failure -> `uncertain/error` + issue-specific help + physical DNS removal.

### DT-03 — iPhone profile install/verification failure

- Require the exact current separately verified profile artifact; do not substitute a guessed profile.
- Run `CHK-SVC-HEALTH` before reinstall loops.
- If iOS/device-management/security policy blocks installation, show current supported/authority boundary without weakening unrelated security.
- Profile presence alone remains non-verified; use `CHK-DNS-PATH`.
- Route resolver/VPN/Private Relay uncertainty to DT-06/DT-07.
- Allow one reinstall only after the prior UseSafeWeb profile is removed and only if the source/profile remains current.
- Continued failure -> `uncertain/error` + Help/Remove; never green state.

### DT-04 — Resolver reachable but approved filter verification fails

- Keep `action-needed`/`uncertain/error`; never state Verified.
- Run current `CHK-SVC-HEALTH` and one `CHK-FILTER` using approved synthetic fixtures.
- Service/filter regression -> stop user-device changes and route the service/configuration incident.
- Resolver-path ambiguity -> DT-06/DT-07.
- False-positive/exception issue -> governed exception procedure, not broad filter disablement.
- Unresolved -> issue-specific help and safe removal; no real visited-domain collection.

### DT-05 — Captive portal or network pre-authentication

- Do not claim protection while ordinary network access is unresolved.
- Complete normal network authorization first where possible.
- If UseSafeWeb DNS configuration prevents required portal access and no accepted coexistence path exists, offer physical DNS removal/reset.
- After normal connectivity, permit one fresh configuration/verification attempt.
- Continued encrypted-DNS blocking -> truthful `uncertain/error` or `not-covered` for that network.

### DT-06 — VPN / managed tunnel / custom resolver conflict

- Establish only the minimum fact that a competing path may exist.
- If current coexistence cannot be proven, use `uncertain/error` for affected scope.
- Never instruct disabling required employer/school/security management merely to obtain success.
- Explain scope and allow Exit/physical DNS removal.
- Recheck only after independently changed condition or new accepted compatibility evidence.

### DT-07 — Private Relay / browser or app secure-DNS uncertainty

- Do not claim compatibility beyond current evidence.
- Use `uncertain/error` where the effective path cannot be established.
- Explain that another app/browser/privacy path may resolve differently; do not claim whole-device coverage.
- Never weaken unrelated privacy controls just to make status positive.

### DT-08 — Stale or contradictory instruction

- Stop presenting an instruction whose current source/platform behavior is materially contradicted.
- Mark affected route `uncertain/error`/`not-covered` until the owning source is reverified.
- Do not ask the parent to experiment through guessed settings.
- Preserve only the last current safe removal path when applicable.

### DT-09 — Android physical DNS removal/recovery

- Distinguish web journey reset, account/device-record operations and physical DNS removal.
- Guide out of the UseSafeWeb custom Private DNS setting via the current accepted platform route.
- Withdraw the UseSafeWeb protection claim once removal is confirmed; state becomes `removed` for that scope.
- Run `CHK-RECOVERY`; unresolved connectivity remains separate and must not be falsely attributed.
- Managed/locked removal -> exact external authority boundary; no bypass.

### DT-10 — iPhone physical DNS profile removal/recovery

- Distinguish anonymous-state reset, account/device-record deletion and physical profile removal.
- Remove the exact UseSafeWeb DNS profile through the current accepted platform route.
- Withdraw the protection claim immediately after confirmed removal.
- Run `CHK-RECOVERY`; persistent connectivity failure is separate.
- Managed/blocked removal -> exact management boundary; no improvised deletion.

### DT-11 — Anonymous J0/J1 state missing/expired

- Run `CHK-JOURNEY-STATE`.
- Valid permitted J0/J1 -> resume only allowed minimal state; reverify protection before positive status.
- Missing/expired/deleted/invalid -> restart necessary accountless step(s).
- Never recover anonymous state from account/email/IP/fingerprint or silently import it after sign-in.

### DT-12 — Service/verification outage

- Run `CHK-SVC-HEALTH` before more device troubleshooting.
- Degraded/unavailable -> `action-needed`/`uncertain/error`, stop repeated user changes.
- Offer physical DNS removal/recovery when current configuration disrupts ordinary connectivity.
- Recheck only after service evidence changes.

## 6. Optional parent-account/session/dashboard decision trees

### DT-13 — Sign-in start/provider return fails, cancels or is unknown

- Accountless core remains available throughout.
- Run `CHK-PROVIDER` using only current provider/session result evidence; never request credentials.
- Cancelled -> return to the prior safe accountless/product state without implying account creation.
- Failed -> state sign-in failed and allow bounded retry only after changed provider/network/session condition.
- Unknown/ambiguous return -> do not create a session or replay consequential account/device action; reconcile provider/session state first.
- Provider outage -> accountless path remains available; optional dashboard may be unavailable without affecting already configured DNS protection claims.

### DT-14 — Session expired, revoked, absent or inconsistent

- Run `CHK-SESSION`.
- Expired/revoked -> require reauthentication before protected persistent-account operations; do not replay an operation whose outcome is unknown.
- Absent -> offer sign-in only for optional persistent features; core help/removal remains login-free.
- Inconsistent/unknown -> clear positive account-operation completion claims and stop at a safe reconciliation state.
- Logout/revocation affects account access, not the truth of physical DNS configuration or technical protection verification.

### DT-15 — Dashboard unavailable or saved state differs from current technical state

- Require a valid optional account session for dashboard access, but never for core DNS troubleshooting/removal.
- Treat saved device/status as context, not E1 technical verification.
- If stored state is stale/conflicts with current verification, display current truthful TSK-0320 state, normally `uncertain/error` until reverified.
- Offer reverify/reinstall/manage-record/return-accountless routes as applicable.

### DT-16 — Add/save/manage device fails

- Require explicit save/manage intent and `CHK-OWNERSHIP` for the target persistent operation.
- Never silently import anonymous J0/J1 state or infer device ownership from ClientID/profile presence.
- Authorization denied/stale -> do not mutate; explain account/device ownership boundary.
- Unknown write outcome -> stop automatic replay; reconcile whether the record exists/changed before retry.
- Physical DNS status remains independent of persistent record success.

### DT-17 — Device replace, revoke, unlink or record deletion

- Confirm operation type, target and ownership before the action.
- Distinguish persistent device record from physical DNS configuration.
- Applied -> report only the exact persistent consequence; do not claim physical DNS removal unless separately evidenced.
- Not applied -> preserve prior authoritative state.
- Unknown -> no blind replay; deterministic read-back/reconciliation required before another attempt.
- Replacement never inherits `protected/verified` from the old device; new device requires its own setup and qualifying verification.

### DT-18 — Account deletion

- Account deletion is distinct from anonymous-state deletion, saved-device record deletion, session revocation and physical DNS removal.
- Require the owning destructive confirmation/authorization contract at implementation time.
- Applied -> account/session/persistent ownership consequences only; accountless core remains available.
- Unknown -> stop replay and reconcile current account/provider state before any repeat.
- Never claim device DNS was removed solely because an account was deleted.

### DT-19 — Sign-in/account unavailable during DNS incident

- Diagnose DNS/service/device path using the accountless-core trees; login is not a prerequisite.
- Existing technical protection state changes only from current technical evidence, not account availability.
- Physical DNS removal/recovery remains reachable without account/dashboard access.
- Account-specific data/action may wait until session/provider recovery; no broadening of diagnostics to compensate.

## 7. Security, privacy and safeguarding exception trees

### DT-20 — Privacy/security anomaly

Examples include prohibited query-history persistence, secret exposure, unsafe diagnostic collection, ownership bypass, deletion-verification failure or unsupported protection claim.

- Stop the affected ordinary path.
- Preserve minimum privacy-safe evidence; no raw sensitive/query data enters GitHub or routine analytics.
- Route to the owning privacy/security incident process.
- Resume only after the owning risk/evidence boundary is satisfied.

### DT-21 — Safeguarding disclosure/concern

- Exit ordinary product troubleshooting for the disclosure/concern.
- Do not solicit unnecessary detail or place personal/raw disclosure in project evidence.
- Follow the dedicated safeguarding/emergency authority boundary.
- Product status cannot close a safeguarding matter.

## 8. Point-of-need help placement

Help is contextual rather than a forced tour or generic FAQ dump:

| State/surface | Required help |
| --- | --- |
| Unsupported/unknown router result | Exact compatibility boundary + safe exit. |
| Android/iPhone setup | Current source-backed instruction + common value/profile mistake + physical removal route. |
| `action-needed` | One branch tied to the current failed check and concrete next action. |
| `uncertain/error` | State what cannot be established, one safe changed-evidence route, and removal/exit where applicable. |
| `not-covered` | Explain current scope without speculative workaround. |
| Protection Map | Help attaches to the exact layer/evidence state. |
| Optional sign-in/session | Explain provider/session state, retain accountless escape path, never request credentials. |
| Dashboard/device management | Explain persistent record/ownership separately from current protection evidence. |
| Replace/revoke/delete | Exact target/consequence + unknown-result reconciliation rule. |
| Physical DNS removal | Platform-specific removal + neutral recovery check. |
| Post-removal connectivity failure | Clarify that UseSafeWeb removal and remaining connectivity fault are separate. |

## 9. Retry and convergence budget

- Initial automatic checks are allowed where technically reliable and privacy-safe.
- One recheck is allowed after each **materially changed condition**: corrected configuration, completed OS action, provider/session change, network change, reinstall/removal, service recovery, ownership correction, or another evidence-producing change.
- No changed condition -> no equivalent retry loop.
- After two materially different bounded repairs fail for one supported ordinary issue, default to truthful unresolved state plus removal/recovery or a named exceptional route only when its criteria apply.
- Unknown consequential operation result always overrides the retry budget: reconcile first; never replay blindly.

## 10. Diagnostic/data boundary

Routine troubleshooting may use only current transient journey/protection state, minimum support-tuple facts, synthetic endpoint/filter/connectivity tests, non-identifying service/provider/session state needed for the immediate branch, minimum persistent ownership references needed for an authorized account/device action, and minimum parent confirmation where the system cannot observe an OS action.

Routine troubleshooting must not collect browsing/domain history, raw DNS queries, persistent child identity, device fingerprint/serial merely for support, passwords/provider tokens, unrestricted free-text diagnostic dumps, or a persistent support-case identity merely to remember ordinary failures.

## 11. Recovery/deletion truth contract

A recovery/lifecycle flow is complete only when the exact target operation is proven or truthfully classified as not-applied/unknown. These operations are distinct and cannot be inferred from one another:

- anonymous J0/J1 reset/deletion;
- logout/session revocation;
- persistent device-record unlink/revoke/delete/replace;
- account deletion;
- physical Android Private DNS change;
- physical iPhone DNS-profile removal;
- neutral ordinary-connectivity recovery;
- new technical protection verification.

No account/device lifecycle operation produces `protected/verified`; a new/reinstalled/replaced device needs current qualifying technical evidence.

## 12. ACC-0319 acceptance mapping

| ACC-0319 requirement | Current design proof |
| --- | --- |
| Top expected failures have bounded issue-specific decision trees | DT-01 through DT-21 cover accountless setup/verification/compatibility/outage/removal plus sign-in/session/dashboard/device lifecycle, privacy/security and safeguarding exceptions. |
| Privacy-safe automatic checks where appropriate | Section 3 defines minimum-input checks and prohibited data/inference. |
| Retries require changed evidence | Sections 2 and 9 prohibit materially equivalent retries and blind destructive replay. |
| Verification truth is preserved | Sections 1–4 bind all troubleshooting to the current TSK-0320 evidence states; account ownership cannot become technical verification. |
| Reset/reinstall/remove and Android/iPhone recovery explicit | DT-02/03/09/10 plus Sections 9 and 11. |
| Point-of-need help bounded | Section 8 maps help to the current issue/state instead of generic or routine staffed support. |
| Privacy limits explicit | Sections 1, 3 and 10 prohibit browsing/query history, raw DNS history, credentials, fingerprinting and unnecessary child data. |
| Exceptional escalation bounded | DT-20/21 and the ordinary trees reserve operator/human handling for named security/privacy/safeguarding/provider/authority exceptions. |
| Current optional-account scope included without mandatory login | DT-13 through DT-19 cover sign-in/session/dashboard/device/account lifecycle while all core troubleshooting/removal remains accountless. |
| Consequential account/device operations fail closed | DT-13/16/17/18 and Section 9 require outcome reconciliation before retry. |

## 13. Evidence and scope limitations

This is **internal L4 design evidence**, not implemented troubleshooting automation, provider integration, production diagnostics, a support SLA, real-user usability/supportability evidence, privacy/legal compliance proof, L5/L6/L7 implementation, or launch authority.

`RSK-0002` remains unresolved until the current lifecycle permits real-user evidence. Any later contradictory platform, security, privacy, production or real-user evidence reopens the affected design rather than being reconciled away.

This artifact specifically supersedes the accountless-only assumptions in the prior TSK-0319 design for current acceptance. Historical evidence remains traceable for unchanged accountless troubleshooting facts only.
