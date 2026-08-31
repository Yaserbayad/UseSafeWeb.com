# TSK-0315 — Dual-Mode End-to-End Service Blueprint — Post-CR-0007

**Task:** TSK-0315 — Create the dual-mode end-to-end service blueprint for accountless core and optional parent-account lifecycle  
**Acceptance:** ACC-0315  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 2.0.0-post-cr0007  
**Date:** 2026-08-31  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE  
**Authority:** current TSK-0149 + TSK-0229 + TSK-0142; current TSK-0312/0140/0041/0313/0320 compatible inputs; DEC-0053/CR-0006 + DEC-0054/CR-0007

## 1. Objective and supersession

This blueprint supersedes the pre-CR-0006 accountless-only `TSK_0315_ACCOUNTLESS_END_TO_END_SERVICE_BLUEPRINT_2026-08-28.md` as the current service-design candidate.

UseSafeWeb Version 1 is dual-mode:

- the complete core First Phone Safety Setup remains usable **without login**; and
- an **optional parent account** adds bounded continuity, session/account lifecycle and lightweight device management.

The blueprint maps frontstage experience, backstage service behavior, minimum data domain, responsible owner, failure and recovery across both modes. It does not approve implementation architecture, provider/vendor acceptance, persistent schema/storage, legal/privacy compliance, release or production behavior.

No real-user behavioral evidence is claimed. RSK-0002 remains open/non-blocking before L8 under current sequencing.

## 2. Service invariants

1. **Accountless core is complete:** login is never required for start, native safeguard, DNS setup/verification, service guidance, Protection Map, troubleshooting, removal or recovery.
2. **Optional account is continuity, not a gate:** sign-in/dashboard may be entered when useful, but failure/cancellation/outage leaves the accountless core available.
3. **No automatic J0/J1 linkage:** account sign-in/account creation does not automatically join, copy, promote or extend accountless J0/J1 state.
4. **Minimum persistence only:** persistent account/device data is limited to approved identity/session/ownership/settings/lifecycle/evidence metadata; no browsing/query/activity history.
5. **Truthful protection evidence:** parent confirmation, stored ownership, dashboard presence and historic state never masquerade as current technical verification.
6. **Protocol/platform truth:** Android native Private DNS and Apple DoH/profile mechanisms retain their owning supported technical requirements.
7. **Reversible lifecycle:** reinstall/reconfigure, revoke/unlink, dashboard-record deletion, account deletion and physical DNS removal are distinct operations with truthful outcomes.
8. **Provider failure is contained:** authentication/provider outage blocks only account-only functions; it does not invalidate configured DNS or the accountless core.
9. **No raw DNS administration:** curated product controls only; no AdGuard admin credentials, arbitrary `/control` proxy, query logs or broad DNS console.
10. **No complete-safety/surveillance claim:** Phone / Internet / Services remain bounded evidence layers.
11. **Self-service first:** ordinary failures have state-specific help/recovery; exceptional security/privacy/legal/safeguarding conditions escalate separately.
12. **Language is not market authority:** English/Turkish/Arabic+RTL technical capability does not activate a named non-UK market.

## 3. Data domains

| Domain | Allowed purpose | Minimum classes | Explicit exclusions |
| --- | --- | --- | --- |
| Public informational | Explain/route only | No product state required | No protection state, child profile, browsing history or mandatory identity. |
| J0 accountless local/session | Active core journey | Minimum routing/current-step/current evidence state | No persistent parent/child/device identity or browsing/query/activity history. |
| J1 optional anonymous transient | Only if downstream architecture proves necessity | Current TSK-0229 allowlist; non-sliding expiry/deletion rules | No account/provider/customer/device-ownership ID, no automatic join, no history. |
| Persistent parent account | Optional continuity/account lifecycle | Minimum provider/account/session lifecycle classes authorized by TSK-0312 | No local password/SMS expansion, child account or history. |
| Persistent managed-device | Optional device continuity | Minimum ownership, nickname/generic label, supported routing context, lifecycle and authorized evidence metadata | No child identity requirement, browsing/query/activity timeline, raw DNS admin or verification-by-ownership. |
| Diagnostics | Exceptional/current issue only | Minimum approved synthetic/error facts | No routine unrestricted raw browsing/query history; time-boxed controls remain separately governed. |

Account activity cannot extend J1 expiry. Any future explicit transfer from an active accountless journey to persistent account/device state requires the separately approved downstream field-level dual-mode data-flow contract; this blueprint authorizes no implicit migration.

## 4. End-to-end dual-mode service blueprint

| Stage | Frontstage — parent experience | Backstage — service/system behavior | Data boundary | Responsible owner | Failure / uncertainty | Recovery / next safe action |
| --- | --- | --- | --- | --- | --- | --- |
| 0. Discover / trust | Parent views proposition, limits, compatibility/privacy/help and decides whether to start. | Serve informational content only; no protection-state mutation. | Public informational; no identity required. | Product + Content | Parent expects surveillance or complete safety. | Clarify bounded Phone/Internet/Services model and limits before Start. |
| 1. Start core | Parent selects **Start setup** without login/payment. | Enter operational setup context; initialize J0; J1 only if later proven necessary. | J0 preferred; no persistent identity. | Product + UX | Session unavailable/lost. | Restart safely; never fabricate persistent resume. |
| 2. Minimal route | Parent selects only necessary platform/setup context. | Validate supported values and route to supported/not-covered path. | Minimum accountless routing fields only. | UX + Product | Unsupported/unknown platform/network. | Show Not covered/uncertain and safe exit/help; do not ask for identity to compensate. |
| 3. Native safeguard | Parent follows/acknowledges applicable native phone safeguard. | Present current approved instruction; preserve parent-confirmed versus system-verified distinction. | Current journey state only unless separately authorized. | UX + Platform content | Setting unavailable, managed device, parent unsure/declines. | Truthful S2/S3/S4/S5 path; contextual help. |
| 4. DNS configure | Parent configures approved platform-specific UseSafeWeb encrypted DNS. | Present exact current Android/iPhone mechanism; do not infer success from presence. | No browsing history; transient setup state. | DNS + UX | Endpoint/profile/network/VPN/Private Relay/browser conflict. | Action needed/uncertain/not covered; safe troubleshooting or removal. |
| 5. DNS verify | Parent runs current verification. | Use approved controlled/synthetic checks for intended resolver/filtering path. | Minimum verification result; no user browsing/domain history. | DNS + Product | Failed, inconclusive, service outage or bypass conflict. | S3/S5/S4 as evidence supports; retry only after changed condition or remove/recover. |
| 6. Relevant service | Parent configures or skips zero/one currently relevant approved service safeguard. | Present only applicable supported guidance; system verification only if separately proven. | No service credentials/content/activity history. | Product + Content | No relevant service, stale/unsupported instruction, insufficient authority. | Not covered/skip/parent-confirmed state; do not invent a second service. |
| 7. Protection Map | Parent reviews Phone / Internet / Services evidence and limitations. | Render current S1–S6 semantics independently; never aggregate into a safety score. | Current evidence state; historical account state cannot manufacture current S1. | Product + UX | Mixed, stale, uncertain, removed or unsupported layer. | Show exact evidence actor/currentness and next action/help. |
| 8. Core finish / optional continuity choice | Parent can finish/exit core or choose optional account continuity. | Core completion remains valid regardless of account choice. | Accountless state follows TSK-0229 expiry/deletion. | Product | Parent declines/cancels sign-in. | Finish/exit accountless; no loss of core value. |
| 9. Optional account entry | Parent chooses Sign in / Save/manage with account. | Initiate planned Google sign-in route under TSK-0312 requirements; do not import J0/J1 automatically. | Provider response + minimum account lifecycle fields only. | Auth/Product | User cancels, provider unavailable, ambiguous identity binding. | Return safely to accountless state; retry later; fail closed for account-only access. |
| 10. First-session account creation | Parent completes successful provider sign-in. | Establish one account/session under downstream approved auth architecture; create no password/SMS path. | Minimum parent/provider/session lifecycle classes. | Auth/App | Duplicate/retry/partial account creation. | Resolve to known account state; avoid silent duplicate/merge. |
| 11. Signed-in return / session | Returning parent authenticates and reaches account continuity. | Validate session/account authorization before account-only data/actions. | Session-control metadata only as authorized. | Auth/App | Expired/revoked/invalid session or provider outage. | Re-authenticate or continue accountless core; no false DNS-removal claim. |
| 12. Dashboard empty/list | Parent sees no devices or minimum list of explicitly managed device records. | Return only authorized parent-owned records and truthful evidence/currentness metadata. | Minimum device ownership/nickname/platform/lifecycle/evidence metadata. | App + Product | Unauthorized/ownership mismatch, missing/revoked record. | Fail closed; show empty/error/recovery without exposing another account. |
| 13. Add/manage device | Parent explicitly adds a device, renames it, continues setup or requests verification. | Start a fresh account-owned setup/device flow, or use an explicit transfer only after the downstream field-level data-flow contract is approved. | Persistent minimum device domain; no implicit J0/J1 transfer. | App + UX | Transfer not authorized, unsupported platform or incomplete setup. | Start fresh supported flow; preserve accountless state independently. |
| 14. Reverify / reinstall / reconfigure | Parent requests current check or repairs configuration. | Apply owning technical verifier/setup rules; invalidate stale optimistic status when context changed. | Minimum current/historical evidence metadata as later authorized. | DNS/App + UX | Verification fails, context conflicts or setup cannot be determined. | S3/S4/S5; exact repair/recheck; do not preserve stale S1. |
| 15. Replace device | Parent marks a device replaced and starts a new device flow. | New record does not inherit S1/S2/history automatically; old record changes lifecycle truthfully. | Minimum old/new lifecycle refs; no browsing/activity transfer. | App + Product | Replacement interrupted or transfer rules absent. | Keep old state explicit; start new supported flow without optimistic inheritance. |
| 16. Revoke/unlink management | Parent removes account management association. | Revoke authorized association; account-only access to record ends. | Ownership/lifecycle metadata only. | App/Auth | Unlink uncertain/failed. | Fail closed for management; do not claim physical DNS removal. |
| 17. Delete dashboard device record | Parent explicitly deletes a managed record. | Delete under downstream data contract; keep physical DNS configuration a separate concern. | Device record deletion lifecycle. | App + Privacy | Deletion pending/failed/unknown. | Show truthful pending/error; never claim DNS was removed. |
| 18. Account logout | Parent logs out. | Terminate applicable authenticated session; deny later account-only actions. | Session lifecycle. | Auth/App | Logout/revocation uncertain. | Fail closed for sensitive account actions; accountless core remains available. |
| 19. Account deletion | Parent explicitly requests account deletion. | Invalidate sessions and initiate governed account/device-ownership deletion. | Account/device lifecycle only; J0/J1 and physical DNS remain separate. | Auth/App + Privacy | Deletion interrupted/pending/failed. | Show truthful state; provide recovery/escalation under owning contract; never claim DNS removal. |
| 20. False positive / ordinary help | Parent reports a blocked legitimate service or setup issue. | Use current state-specific self-service and narrow reproducible correction process. | Synthetic/minimum issue facts; no routine history. | UX + DNS/Support | Root cause uncertain or repeated failure. | Reproduce safely, narrow correction, reverify; exceptional diagnostics only when governed. |
| 21. Remove UseSafeWeb protection | Parent removes Android Private DNS or Apple profile. | Guide exact supported removal; withdraw current UseSafeWeb DNS claim when evidence/confirmation supports removal. | No history required. | DNS + UX | Removal blocked/uncertain. | Platform-specific recovery/help; never mark S6 without supporting evidence. |
| 22. Post-removal recovery | Parent verifies ordinary connectivity after removal. | Use neutral/synthetic recovery checks; distinguish recovery from UseSafeWeb protection. | Minimum current recovery result. | DNS + UX | Normal connectivity still fails for unrelated reason. | Separate root cause; avoid unsupported attribution; continue general recovery. |
| 23. Provider outage branch | Parent attempts account-only action while provider/auth is unavailable. | Block account-only operation, preserve configured DNS and accountless service routes. | No new identity/history collected to compensate. | Auth/App | Outage persists. | Explain temporary account limitation, allow accountless setup/verification/help/removal, retry later. |
| 24. Exit / reset / lost state | Parent exits, starts over or returns after transient state loss. | Clear/end accountless state per TSK-0229; authenticated state follows its own session/account lifecycle. | Separate J0/J1 and account domains. | Product + App | Device config remains while web state is lost/reset. | Distinguish journey reset from DNS removal; route to current verification/removal as needed. |

## 5. Normal path and branches

### 5.1 Accountless core normal path

`Discover → Start → Route → Native safeguard → DNS configure → DNS verify → [zero/one service] → Protection Map → Finish/Exit`

No login or account is required anywhere in this path.

### 5.2 Optional continuity branch

From an appropriate downstream-designed entry point:

`Optional account entry → Google sign-in → account/session → Dashboard → Add/manage device → Verify/reinstall/replace/revoke/remove as needed`

Sign-in does not automatically migrate J0/J1. Exact entry placement and any explicit save/transfer are downstream IA/data-flow decisions.

### 5.3 Returning signed-in parent

`Sign in/valid session → Dashboard list/empty → selected device → current status/Protection Map → next management action`

Stored status is historical unless the owning verifier establishes currentness; account ownership is never S1 evidence.

### 5.4 Provider outage

`Account entry/action → provider unavailable → account-only error → accountless core/help/removal remains available → retry account later`

### 5.5 Recovery/removal

`Any applicable supported failure → contextual help/troubleshoot → changed condition/reverify OR remove protection → post-removal recovery → exit/start over`

### 5.6 Account/device lifecycle separation

- **Logout** ends session access only.
- **Revoke/unlink device** ends dashboard management association only.
- **Delete device record** deletes governed dashboard data only.
- **Delete account** deletes governed account/device-ownership data only.
- **Remove UseSafeWeb protection** changes physical device DNS configuration.
- **J0/J1 expiry/deletion** affects anonymous journey state only.

No one operation may claim another completed unless its owning workflow actually performed and verified it.

## 6. Frontstage/backstage ownership boundary

This blueprint defines service outcomes, not implementation architecture:

- Product/UX owns journey/state presentation and necessity.
- DNS/network owns supported mechanisms, technical verification, removal/recovery and false-positive technical truth.
- Auth/App owns authenticated session and account/device authorization behavior after the L5 architecture is approved.
- Privacy/data work owns actual persistent schema, retention, deletion, recipients, transfers and backup rules.
- Content/platform owners own current instructions/source currency.
- QA owns later implementation-level test execution against the frozen acceptance contracts.

No owner listed here self-certifies a later gate or expands its Action Authority.

## 7. Failure-state rules

1. A supported known-repair failure is Action needed, not Not covered.
2. Unsupported scope is Not covered, not a fake fallback flow.
3. Inconclusive/conflicting/stale protection evidence is Status uncertain/error, not stale S1/S2.
4. Provider/account outage cannot change physical DNS truth.
5. Account/session uncertainty fails closed only for account-only actions.
6. A failed persistent operation cannot silently mutate J0/J1 or create hidden linkage.
7. Destructive actions show pending/failed/unknown when completion is not proven.
8. Retry requires a changed condition/new evidence or an idempotent safe operation; do not loop equivalent failure.

## 8. Explicit prohibited service behavior

The blueprint does not permit:

- mandatory account/login for core value;
- local password or SMS authentication expansion;
- automatic accountless-to-account stitching/promotion;
- browsing, DNS-query, visited/top-domain, app/activity history;
- child accounts or persistent child behavioral profiles;
- customer-facing raw AdGuard administration/query logs/broad filter control;
- account/device ownership as technical protection verification;
- broad service catalogue or arbitrary integrations;
- payment/card requirement before core value;
- complete-safety/surveillance claims;
- a routine staffed-support dependency.

## 9. Deterministic blueprint assertions

A downstream IA/prototype/build/QA review must be able to prove:

1. The public discover/trust/start outcome is distinct from operational setup state.
2. The full core journey can finish without login.
3. Optional Google account entry exists without blocking accountless continuation on cancel/error/outage.
4. Account/session return and expiry/revocation states are represented.
5. Dashboard empty/list/device-management states are represented.
6. Native safeguard routing retains parent-confirmed versus system-verified truth.
7. DNS setup uses current platform-specific mechanism semantics.
8. DNS S1 requires qualifying current technical verification.
9. Zero/one relevant service guidance and Not covered are valid outcomes.
10. Protection Map keeps Phone/Internet/Services evidence independent.
11. False-positive/support uses privacy-minimal self-service and narrow correction.
12. Reinstall/reconfigure invalidates stale optimistic status where required.
13. Replacement does not inherit prior S1/S2/history automatically.
14. Revoke/unlink is distinct from physical DNS removal.
15. Device-record deletion is distinct from physical DNS removal.
16. Account deletion is distinct from J0/J1 deletion and physical DNS removal.
17. Provider outage blocks account-only functions but leaves accountless setup/help/removal available.
18. J0/J1 is never automatically joined/promoted to a persistent account/device record.
19. No browsing/query/activity history is required by any stage.
20. No mandatory login, child account, raw DNS admin or safety paywall is introduced.
21. Each mapped stage identifies frontstage, backstage, data boundary, owner, failure and recovery.
22. Unsupported/uncertain/action-needed/removed states remain truthful rather than coerced to success.
23. Exit/reset distinguishes web journey state from physical DNS configuration.
24. No implementation/provider/legal/privacy/LG-06 or later-gate PASS is inferred from this blueprint.

## 10. ACC-0315 disposition

ACC-0315 requires a blueprint covering discover/start, accountless setup, optional account entry/return/session, lightweight dashboard/device management, native safeguard routing, DNS activation/verification, relevant service guidance, Protection Map, false-positive/support, account/device deletion/revoke/reinstall/replacement, recovery/removal, provider outage and exit, with frontstage/backstage/data/owner/failure/recovery mapped and no browsing/activity history or mandatory login.

Sections 1–9 map every required dimension and reconcile the pre-CR-0006 accountless blueprint into the current dual-mode Version-1 product boundary without inventing downstream implementation acceptance.

**Candidate disposition:** ACC-0315 is ready for independent post-publication verification. TSK-0315 remains non-PASS until that verification and durable runtime reconciliation succeed.
