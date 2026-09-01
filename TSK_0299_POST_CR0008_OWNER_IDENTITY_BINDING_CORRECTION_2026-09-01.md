# TSK-0299 — Owner-Identity Binding Correction — Post-CR-0008

**Task:** TSK-0299  
**Applies to:** `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`  
**Version:** 2.0.1-post-cr0008  
**Date:** 2026-09-01  
**Authority:** Project Owner identity approval `TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md`, blob `66f4b545c03571649a8baa4c0fe3d1df564b5949`; current ACC-0299; DEC-0053/CR-0006; DEC-0055/CR-0008.  
**Status:** CURRENT BINDING CORRECTION pending independent TSK-0299 re-verification and runtime reconciliation.

## 1. Reason for correction

Frontier recomputation exposed a higher-authority identity constraint that the first post-CR-0008 TSK-0299 candidate did not bind explicitly enough.

The Project Owner previously and explicitly approved:

- visible brand name: **`SafeWeb`**;
- `UseSafeWeb.com` as the project/domain/repository identity;
- the `Use` prefix is **not** part of the visible brand wordmark and **must not be reused as brand copy or logo text**.

That owner decision remains current. Therefore the first post-CR-0008 TSK-0299 candidate is not independently sufficient wherever it uses `UseSafeWeb` as a visible parent-facing product/brand token. Its tone, dual-mode, claims, lifecycle, localization and protection-evidence semantics remain compatible and are preserved.

This correction is binding over the base candidate for current TSK-0299 acceptance. Historical and first-pass artifacts remain traceable evidence; they are not silently rewritten.

## 2. Canonical visible naming contract

1. **Visible product/brand name:** `SafeWeb`.
2. **Project/domain/repository identity:** `UseSafeWeb.com`.
3. **Actual technical identifiers** may display their exact real value when technically necessary, including an approved domain, resolver hostname, URL or profile identifier; do not cosmetically rename a technical identifier.
4. **Generic parent-facing product references** use `SafeWeb`, not `UseSafeWeb`.
5. **Generic parent-facing DNS feature references** use `SafeWeb DNS` unless the UI is displaying an exact technical hostname/domain/value that contains `UseSafeWeb.com` or another approved literal identifier.
6. `UseSafeWeb` without `.com` is not a visible brand token and must not be introduced into headings, CTAs, status copy, marketing copy, help copy, account/dashboard copy or generic explanatory prose.
7. Logo/wordmark text remains exactly `SafeWeb`; this correction does not redesign or reselect the owner-approved identity.

## 3. Binding lexical normalization for the base verbal system

In `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`, interpret and implement visible parent-facing generic product references as follows:

| First-pass token/example | Current binding form |
| --- | --- |
| `UseSafeWeb` as product/brand noun | `SafeWeb` |
| `UseSafeWeb DNS` as generic feature label | `SafeWeb DNS` |
| `Remove UseSafeWeb DNS` as generic CTA | `Remove SafeWeb DNS` |
| `UseSafeWeb verified this protection step for this setup.` | `SafeWeb verified this protection step for this setup.` |
| `UseSafeWeb does not cover this on your current setup.` | `SafeWeb does not cover this on your current setup.` |
| `This setup is no longer enrolled through UseSafeWeb.` | `This setup is no longer enrolled through SafeWeb.` |
| `Setup complete. Review what UseSafeWeb verified, what you confirmed, what needs action, and what is not covered.` | `Setup complete. Review what SafeWeb verified, what you confirmed, what needs action, and what is not covered.` |
| `You can complete the core setup without a UseSafeWeb account.` | `You can complete the core setup without a SafeWeb account.` |
| `UseSafeWeb is not a child browsing or activity monitoring product.` | `SafeWeb is not a child browsing or activity monitoring product.` |
| generic `UseSafeWeb` physical-DNS removal wording | generic `SafeWeb DNS` removal wording |

This is a **brand-token correction only**. It does not weaken or rename the canonical state IDs or evidence classes.

## 4. Protection-state semantic preservation

Current TSK-0320 remains the semantic owner of:

- S1 `protected/verified` — primary label `Protection verified`;
- S2 `configured/parent-confirmed` — primary label `Setup confirmed` plus explicit not-technically-verified meaning;
- S3 `action-needed` — `Action needed`;
- S4 `not-covered` — `Not covered`;
- S5 `uncertain/error` — `Protection status could not be verified`;
- S6 `removed` — `Removed`;
- all evidence/transition rules, including that account ownership, dashboard/device registration, configuration presence and parent confirmation never substitute for qualifying technical verification.

Where a TSK-0320 supporting-copy example contains the obsolete visible token `UseSafeWeb`, current TSK-0299 parent-facing rendering applies the higher-authority owner identity token `SafeWeb` while preserving the sentence's evidence strength, actor, scope, uncertainty and transition meaning. This correction does not claim to rewrite TSK-0320's authoritative artifact or change ACC-0320.

## 5. Dual-mode and lifecycle semantics unchanged

The following first-pass TSK-0299 rules remain current without substantive change:

- complete accountless core remains usable without login;
- optional parent account adds bounded continuity/session/dashboard/device management, never stronger protection;
- `Continue without account` and `Finish without account` remain first-class accountless exits;
- no automatic J0/J1 import/link/promotion/TTL extension on sign-in;
- no browsing/query/activity history, child account/profile or broad DNS administration;
- dashboard/device-record presence is not protection verification;
- Start over, logout, unlink/revoke, device-record deletion, account deletion and physical DNS removal remain distinct operations;
- ambiguous consequential results require reconciliation before retry;
- English/Turkish/Arabic+RTL localization preserves evidence strength, actor, optionality, scope and destructive-operation object semantics;
- language availability does not activate a market;
- `RSK-0002` remains OPEN and no pre-L8 representative-parent validation or deferred legal completion is inferred.

## 6. Cross-surface application

Current visible naming is consistent across:

- public website and how-it-works copy: `SafeWeb`;
- accountless setup/product headings and instructions: `SafeWeb` / `SafeWeb DNS`;
- Protection Map supporting copy: `SafeWeb` with unchanged state/evidence semantics;
- optional account/sign-in/dashboard/device-management copy: `SafeWeb account`, `SafeWeb dashboard` only where a product noun is needed;
- help/status/recovery/removal copy: `SafeWeb` / `SafeWeb DNS` except when showing an exact technical identifier;
- privacy/settings explanations: `SafeWeb` as visible brand, exact `UseSafeWeb.com` only where the actual domain/project/technical identifier is relevant;
- English/Turkish/Arabic interfaces: `SafeWeb` remains Latin-script, LTR and untranslated in the brand token, consistent with the owner-approved identity system.

## 7. Deterministic correction assertions

Current TSK-0299 acceptance must prove:

1. the owner identity approval blob is present and unchanged;
2. visible brand name is exactly `SafeWeb`;
3. `UseSafeWeb.com` remains domain/project/technical identity only;
4. generic `UseSafeWeb` is prohibited as visible brand copy;
5. generic parent-facing DNS copy uses `SafeWeb DNS` unless showing an exact technical identifier;
6. current TSK-0320 state/evidence semantics remain unchanged while brand-token examples render as `SafeWeb`;
7. dual-mode/accountless/account/dashboard/lifecycle/privacy/localization rules from the base candidate remain intact;
8. TSK-0485 and synchronized TSK-0318/TSK-0319 runtime PASS sections are not modified by this correction;
9. TSK-0301 owner-approved identity is preserved rather than reselected or overwritten;
10. no downstream task/gate becomes PASS from this lexical correction alone.

## 8. Non-inference

This correction does not prove implementation, parent comprehension, legal/privacy completion, provider acceptance, market activation, publication, payment, production behavior, LG-06 or launch. It does not modify the TSK-0301 owner identity decision or the TSK-0320 evidence-state transition model.

**TSK-0299 current PASS must be reverified and runtime-reconciled against this binding correction before it can remain accepted.**
