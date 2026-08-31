# TSK-0335 — Post-CR-0007 Dual-Mode Protection Map Amendment — HUMAN_ONLY Candidate

**Version:** 1.0.0-post-cr0007  
**Task:** TSK-0335 — Design Protection Map and coverage-limit interactions  
**Acceptance:** ACC-0335  
**Status:** HUMAN_ONLY current-scope amendment candidate; **not approved / not PASS**  
**Date:** 2026-08-31

## 1. Purpose and supersession

This amendment updates only the scope assumptions of the previously owner-approved `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`, for the current Version-1 product: complete accountless core plus optional parent account/session/minimum device persistence/lightweight dashboard.

The historical candidate remains normative for the six-state Protection Map evidence model, confirmation-versus-verification distinction, material-gap timing, deterministic truth-state behavior, no-score rule, accessibility/RTL behavior and later-L8 comprehension hooks except where this amendment explicitly supersedes stale product-scope text.

This amendment supersedes these historical assumptions only:

- `no persistent dashboard` as a whole-product boundary;
- old pre-CR-0006 source pins that excluded account/dashboard surfaces;
- visible product identity `SafeWeb` where the current product identity is `UseSafeWeb`.

It does **not** weaken any truth, privacy, accessibility or no-human-validation requirement.

## 2. Current authoritative sources

Current-scope interpretation is grounded in:

- current WBS/graph/runtime authority under DEC-0053/CR-0006 and DEC-0054/CR-0007;
- current post-CR-0007 TSK-0328 information architecture, blob `527436958a1cd75fc91057410f4347ad56a3f53a`;
- current TSK-0332 dashboard/device-management prototype, blob `7b19f726fefd4675f55fcad2ffb5fbf4e1c4aa2d`;
- current TSK-0331 account/device lifecycle design and corrective dependency-complete evidence;
- current TSK-0334 support lifecycle base+amendment and dependency-complete evidence;
- current-qualified TSK-0330 Phone → Internet → Services setup-flow contract;
- current TSK-0320 Protection State Model and TSK-0324 component/accessibility rules where unchanged.

No provider/vendor/security/privacy architecture, storage schema, production implementation, publication or gate PASS is approved here.

## 3. Current dual-mode Protection Map rule

The Protection Map remains one evidence model used in two allowed contexts:

1. **Accountless core:** the parent reaches the Protection Map directly through the signed-out setup/verification journey and can understand, troubleshoot, remove or exit without creating an account.
2. **Optional signed-in continuity:** a parent-owned saved device record may open a device-detail Protection Map from the lightweight dashboard.

The signed-in surface is a continuity view, not a stronger source of truth. The same evidence-strength and material-gap rules apply in both contexts.

Login is never required to obtain or understand the core Protection Map.

## 4. Account / dashboard truth invariants

The following are binding additions to the historical candidate:

1. **Saved record != verification.** A dashboard device record, account ownership, account session, device nickname or record presence never creates S1 `Verified`.
2. **Persisted/last-known state is not automatically current.** When a dashboard shows an earlier result, freshness must be explicit. A stale positive result must route to current recheck or truthful uncertainty rather than remain visually current.
3. **Current S1 still requires current qualifying technical evidence.** The dashboard may display S1 only when the owning verifier's evidence is current for that layer/context and no contradiction exists.
4. **Account/provider/session failures are account-only.** Sign-in cancellation, provider outage, session expiry/revocation or account unavailability must not upgrade, downgrade or remove physical Protection Map truth by themselves.
5. **No anonymous-to-account promotion.** Signing in or saving a device does not import/promote/extend J0/J1 or transform parent-confirmed state into technical verification.
6. **Lifecycle actions remain distinct.** Logout, unlink/revoke, dashboard-record deletion, account deletion, anonymous J0/J1 deletion and physical UseSafeWeb DNS removal are separate operations.
7. **Physical `Removed` remains evidence-owned.** S6 `Removed` may represent physical protection removal only after the owning physical-removal outcome supports it; account/data deletion is insufficient.
8. **No history expansion.** Optional dashboard continuity does not authorize browsing/query/activity history, top-sites surfaces, child profiles, raw DNS logs, unrestricted AdGuard administration or broad per-domain controls.
9. **No safety score.** Dashboard cards or detail pages may summarize the strongest truthful current/last-known state but may not collapse Phone / Internet / Service into an overall score, certification or whole-child safety claim.
10. **One layer never certifies another.** Account/dashboard context does not change the historical independent-layer model.

## 5. Dashboard presentation contract

When Protection Map is opened from `DASH-DEVICE` or another approved signed-in device-detail surface:

- show Phone / Internet / Service independently when applicable;
- preserve the six historical user-visible state meanings and evidence-strength distinctions;
- show evidence freshness when currentness matters;
- identify an earlier/stored result as earlier/last-known unless current evidence re-establishes it;
- keep S2 parent-confirmed text explicitly non-verified;
- show S3/S4/S5/S6 gaps without hiding them behind a positive device-card summary;
- expose at most one immediate next action per layer;
- route repair/recheck/help/removal/reconfigure actions to their owning current flows;
- do not require sign-in to reach an equivalent accountless recovery/help route for physical-device protection.

A dashboard card may use parent-facing summary language such as **Protection confirmed**, **Set up — parent confirmed**, **Needs attention**, **Not covered**, **Status uncertain**, or **Removed** only when its underlying layer evidence supports that summary. The detailed Protection Map remains the place where independent layer truth is exposed.

## 6. Current material-gap timing

The historical timing contract remains unchanged and now also applies to signed-in continuity surfaces:

- a known gap discovered during accountless setup is shown when discovered and remains visible on the map;
- a stale/contradictory dashboard result is not presented as current positive truth;
- session/provider/dashboard availability problems are shown as account-only access problems, not protection-state changes;
- a missing/unlinked/deleted dashboard record does not imply physical removal;
- a confirmed physical removal withdraws the active protection claim even if the dashboard record still exists;
- account/device-record deletion does not withdraw physical protection unless the separate physical removal flow also succeeds.

No account surface may postpone or suppress a material protection limitation merely to create a positive dashboard experience.

## 7. Deterministic current-scope additions

The historical 16-case deterministic matrix remains valid. Add these current-scope cases:

| ID | Scenario | Required result |
| --- | --- | --- |
| `TC-0335-17` | Signed-in saved record with no current verifier result | Record presence does not create S1; show earlier/unknown truth and a bounded recheck/continue action. |
| `TC-0335-18` | Earlier S1 stored in dashboard, evidence now stale | Do not present as current S1; show freshness warning and recheck/uncertain state according to owning verifier contract. |
| `TC-0335-19` | Session/provider failure while physical protection was previously verified | Account access fails independently; physical Protection Map truth is not rewritten by provider/session failure. |
| `TC-0335-20` | Dashboard record deleted while device remains configured | Record disappears from dashboard; physical protection is not labelled Removed from record deletion alone. |
| `TC-0335-21` | Physical DNS removal succeeds while dashboard record remains | Internet layer becomes S6/Removed under owning removal evidence; saved record may remain as continuity metadata until separately deleted. |
| `TC-0335-22` | Sign in after accountless Protection Map | No automatic J0/J1 import/promotion; account/device presence does not upgrade any state. |
| `TC-0335-23` | Signed-out parent views/fixes Protection Map | Full core map/help/recovery remains usable without login. |
| `TC-0335-24` | Optional dashboard rendered on mobile/RTL | Same evidence strength, gap visibility and no-score rules as accountless map. |

## 8. Later L8 comprehension hooks

The original `L8-PT-01` through `L8-PT-08` remain preserved. Current integrated product must additionally leave observable surfaces from which later L8 validation can test whether parents understand that:

- a saved device/account/dashboard record is not technical verification;
- an earlier result may require rechecking to know current protection;
- deleting/unlinking account-side data is different from physically removing UseSafeWeb protection.

These are future validation hooks only. No human comprehension evidence is claimed or fabricated at L4.

## 9. Branding and terminology normalization

Where the historical candidate uses `SafeWeb` as the visible product identity, current integrated product copy uses **UseSafeWeb**. Technical domains/endpoints and independently owned source terms remain unchanged.

This naming normalization changes no evidence semantics.

## 10. Privacy / accessibility / scope fences

The historical privacy and accessibility safeguards remain binding. Current dual-mode scope additionally requires:

- dashboard/private routes are noindex/private and authorization-owned downstream;
- no cross-account device details are exposed on ownership mismatch;
- no provider secret, raw DNS history or child identity is required to interpret the Protection Map;
- accountless Protection Map remains fully available signed out;
- material limitations remain textual and in reading/focus order, not color-only or hover-only;
- English/Turkish/Arabic+RTL preserve evidence strength and destructive/lifecycle distinctions;
- no L5/L6/production/legal/vendor/security/storage conclusion is inferred.

## 11. Current ACC-0335 mapping

ACC-0335 remains unchanged:

> Prototype never labels parent confirmation as verification, exposes material gaps at the right time, supports deterministic internal/automated truth-state checks, and preserves the interaction points needed for later L8 human comprehension validation.

Current mapping:

- parent confirmation vs verification: historical candidate §§3–4 plus this amendment §4;
- material gaps: historical candidate §§5–7 plus this amendment §§5–6;
- deterministic truth-state checks: historical candidate §§9–10 plus current-scope cases `TC-0335-17..24`;
- later L8 interaction points: historical candidate §11 plus this amendment §8;
- accountless + optional dashboard consistency: this amendment §§3–7.

## 12. HUMAN_ONLY decision boundary

This amendment is prepared evidence only. It does not itself re-accept TSK-0335.

The previously approved historical candidate remains evidence for unchanged Protection Map semantics. Because this amendment changes the task's product-scope interpretation from accountless-only to accountless core plus optional dashboard continuity, explicit current Project Owner approval is required before TSK-0335 can become current-qualified PASS.

Recommended exact approval after deterministic verification:

`APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT`

Alternative:

`REVISE TSK-0335: <specific change>`
