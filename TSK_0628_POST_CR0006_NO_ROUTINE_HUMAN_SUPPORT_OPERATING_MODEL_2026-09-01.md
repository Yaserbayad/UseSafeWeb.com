# TSK-0628 — Post-CR-0006 No-Routine-Human-Support Operating Model

**Task:** `TSK-0628`  
**Acceptance:** `ACC-0628`  
**Authority:** `DEC-0053 / CR-0006`, `DEC-0054 / CR-0007`  
**Date:** 2026-09-01  
**Status:** candidate current L4 operating contract pending independent verification.

## Operating rule

Version 1 remains self-service by default across both modes:

1. the complete accountless setup/protection/recovery path works without login; and
2. optional parent account/sign-in/session, minimum parent/device ownership persistence, lightweight dashboard/device management, and account/device lifecycle operations are supported without making routine human support a dependency.

The ordinary sequence is `prevent -> privacy-safe automatic check -> truthful state -> issue-specific in-product help -> bounded AI assistance -> safe recovery/removal/deletion or truthful unsupported state`. A human/operator route is exceptional, criterion-driven, and excluded from self-service-success claims.

No browsing/query/activity history, child profile, raw DNS history, unrestricted DNS administration, credentials, or unnecessary diagnostic identity is introduced by this model. Account ownership never substitutes for technical protection verification. Anonymous J0/J1 state remains separate from persistent account state; sign-in does not silently promote/link anonymous state or extend its expiry.

## Ordinary issue matrix

| Issue class | Prevention / automatic check | In-product / AI help | Recovery / terminal state | Human route |
| --- | --- | --- | --- | --- |
| Accountless setup / routing | Current supported tuple and source-backed instructions; service/path checks before repeated changes. | Explain exact current step and evidence state only. | Restart valid journey, safe DNS removal/recovery, `Status uncertain` or `Not covered`. | No, except managed/security/privacy boundary. |
| DNS verification / filtering / compatibility | Service-health, support-tuple, DNS-path/filter/conflict checks using privacy-safe evidence. | One issue-specific branch; retry only after changed condition. | Reverify, truthful uncertain/not-covered, or remove/recover. | Exceptional operator route only for service/configuration incident or governed false-positive change. |
| Sign-in / provider return | Prevent mandatory login; preserve accountless escape path; distinguish provider pending/cancel/error/success. | Explain provider state without asking for credentials or fabricating access. | Retry after changed condition, return accountless, or truthful provider/account error. | Only for provider/security/privacy incident outside ordinary user control. |
| Session expiry / revocation / logout | Explicit session state, expiry and reauthentication boundary; no destructive replay after unknown result. | Explain why reauthentication is required and what operation was not completed. | Reauthenticate, logout, revoke, return accountless, or stop safely. | Only security/privacy/provider incident. |
| Dashboard access | Signed-in ownership required; dashboard is optional and never required for core protection. | Explain saved-device state separately from current technical protection state. | Reverify device, reinstall, manage record, return accountless. | No ordinary route. |
| Add / save / manage device | Explicit save intent; minimum device ownership data only; no silent J0/J1 import. | Explain saved-record vs physical/configuration state. | Reverify, reinstall, replace, revoke/unlink, delete record, or remove DNS. | Only governed security/ownership anomaly. |
| Device replacement / revoke / record deletion | Confirm operation, authority and target before change; unknown results are not replayed blindly. | Explain exact consequence and distinction from physical DNS removal. | Applied / not-applied / unknown requiring deterministic reconciliation. | Exceptional only when ownership/security or platform authority cannot be resolved safely. |
| Account deletion | Explicit destructive confirmation; account-domain deletion is distinct from anonymous-state deletion and DNS removal. | State what is and is not deleted; no claim that device DNS was removed unless separately evidenced. | Account deleted / not-applied / unknown; accountless core remains available. | Exceptional privacy/security/identity dispute only. |
| Removal / recovery | Removal remains reachable without dashboard/account dependency. | Explain protection withdrawal and ordinary-connectivity recovery. | Exact platform removal plus neutral recovery check. | Only managed-device/admin or platform defect boundary. |
| Stale guidance / outage | Detect source/service condition before device changes. | Withhold stale instruction; explain current uncertainty. | Stable reference, removal/recovery, or wait for service/source repair. | Content/technical owner or operator route, not routine customer completion. |
| Unsupported / other | Do not widen scope. | Explain why no safe supported branch exists. | `Not covered`, `Status uncertain`, safe exit/removal. | No routine human completion. |

## AI assistance boundary

AI may classify an issue into an approved branch, explain current instructions/states, ask the minimum non-sensitive routing fact, and direct to current recovery/removal/deletion flows. AI may not request passwords/provider credentials/raw history, invent support paths, mutate production DNS/admin state from ordinary support, claim remote inspection, declare technical verification from account ownership or user wording, replay ambiguous destructive actions, or silently promise human support.

## Exceptional routes

Human/operator handling is reserved for security/privacy/safeguarding incidents, provider/infrastructure outages needing operator repair, managed-device/network authority outside the user, governed global filtering changes, exceptional authorized diagnostics, material stale-source correction, ownership/identity disputes that cannot be safely resolved automatically, or legal/scope decisions. These cases remain outside the self-service-success numerator.

## Testable acceptance assertions

A current review must prove:

- ordinary accountless setup, verification, troubleshooting, recovery and removal have self-service routes;
- ordinary sign-in/provider, session, dashboard and device-management issues have self-service routes;
- account deletion, device-record deletion/revoke/replace, DNS removal and anonymous-state deletion are distinct and truthfully described;
- unknown destructive-operation outcomes stop automatic replay and require reconciliation;
- account presence/device ownership never creates `Verified` protection state;
- human escalation is exceptional, named and criterion-driven;
- no routine support path requires browsing/query/activity history, raw DNS history, child identity, credentials or broad DNS administration;
- no routine case is counted self-service if a human/operator materially completes it.

This artifact is L4 operating-model design evidence only. It does not implement support automation, activate telemetry or staffed support, prove real-user supportability, complete provider/privacy/security architecture, authorize production/publication/payment/launch, or make LG-06 PASS by itself.