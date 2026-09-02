# TSK-0311 — Post-CR-0008 Dual-Mode Localization / Content Architecture Revalidation

**Task:** TSK-0311 — Define translation keys/files, locale metadata, plural/date rules, content ownership, localized instruction variants, and fallback behavior  
**Acceptance / Verification / Evidence:** ACC-0311 / VER-0311 / EVD-0311  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0311, durable EVD-0311 and guarded runtime reconciliation.

## 1. Revalidation decision

The historical TSK-0311 localization architecture remains valid for its core design: semantic externalized keys, locale manifest, deterministic fallback, separate schema/content versioning, source-backed instruction bindings, CLDR/Unicode-equivalent plural/number/date behavior, Arabic RTL and technical-literal isolation, accessibility/localization interaction, content ownership, privacy boundaries and testable implementation assertions.

It is stale only where its 2026-08-29 scope says it externalizes the provisional **accountless first-phone product** and its namespace/key inventory omits the optional parent-account/session/dashboard/device-lifecycle surfaces that current TSK-0318 now requires.

Current acceptance therefore preserves the historical architecture as immutable provenance and extends the key/file/ownership/test model to the current dual-mode Version-1 IA. It does not redesign localization infrastructure, activate a market, claim native-speaker validation or implement production locale files.

## 2. Current authority and immutable provenance

Current direct predecessor:

- `TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md` — blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3` — current PASS.

Historical TSK-0311 provenance:

- `TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md` — blob `ef746d64c7878eb7d0f1b8fdf2356721728041c4`, publication commit `7eb43368af724887405cf3be9cf9363465834b02`;
- `TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_EVIDENCE_2026-08-29.md` — blob `b9e7770faa0fa94a35d98d8141dec367583233f7`.

Current source-backed instruction authority is the separately current TSK-0307 catalogue; localization continues to bind source-owned setup/verification/removal semantics by stable instruction ID rather than independently rewriting them.

## 3. Preserved locale baseline and manifest contract

The locale baseline remains:

| Locale | Role | Direction | Status | Market implication |
| --- | --- | --- | --- | --- |
| `en-GB` | canonical authored semantic baseline | LTR | baseline | none; publication remains gated |
| `tr-TR` | localized variant | LTR | provisional | no Turkish-market activation |
| `ar` | localized Arabic variant | RTL | provisional | no Arabic-market/region activation |

Minimum manifest fields remain machine-testable:

- `locale`;
- `language`;
- `region` where applicable;
- `direction`;
- `fallback`;
- `status`;
- `marketActivation=false`;
- `contentVersion`;
- `lastVerified`;
- `owner`.

Locale selection changes presentation only. It cannot change platform support, verification evidence, account ownership, device ownership, market activation or legal status.

## 4. Current externalized file model

The logical file model is extended, not replaced:

```text
locales/
  locale-manifest.json
  en-GB/
    common.json
    navigation.json
    setup.json
    verification.json
    protection-map.json
    troubleshooting.json
    removal-recovery.json
    accessibility.json
    account.json
    session.json
    dashboard.json
    device-management.json
    account-lifecycle.json
  tr-TR/
    ...same namespaces...
  ar/
    ...same namespaces...
content/
  instruction-bindings.json
  content-versions.json
```

Hard rule: no user-facing production sentence, button label, status label, help heading, validation error, setup instruction, auth/session message, dashboard/device-management label, destructive lifecycle consequence or recovery instruction may be embedded directly in component/source code except explicitly exempt immutable technical literals.

## 5. Preserved semantic key model

Stable keys continue to use semantic intent rather than English wording:

```text
<surface>.<context>.<element>[.<variant>]
```

Historical namespaces remain valid. Current dual-mode additions are below.

## 6. Current dual-mode key inventory

### Public/navigation additions

| Current IA purpose | Representative keys | Owning semantic source |
| --- | --- | --- |
| Optional public sign-in/manage entry | `navigation.sign_in_manage_devices`, `account.entry.optional_explanation`, `account.entry.continue_without_account` | TSK-0318 + Product/Auth content |
| Accountless completion choice | `setup.complete.finish_without_account`, `setup.complete.sign_in_to_manage_devices`, `setup.complete.account_optional_note` | TSK-0318 + UX |

### Authentication/session

| Current IA purpose | Representative keys | Owning semantic source |
| --- | --- | --- |
| Optional sign-in start | `account.sign_in.title`, `account.sign_in.provider_action`, `account.sign_in.optional_note`, `account.sign_in.cancel` | TSK-0318 + Auth/Product |
| Auth callback/result | `account.auth_result.success`, `account.auth_result.cancelled`, `account.auth_result.failed`, `account.auth_result.continue_without_account`, `account.auth_result.retry` | TSK-0318 + Auth/App |
| Session state | `session.expired.title`, `session.expired.reauthenticate`, `session.provider_unavailable.title`, `session.provider_unavailable.continue_without_account`, `session.logout.action`, `session.logout.result` | TSK-0318 + Auth/App |

### Dashboard/device management

| Current IA purpose | Representative keys | Owning semantic source |
| --- | --- | --- |
| Dashboard | `dashboard.title`, `dashboard.empty.title`, `dashboard.add_device`, `dashboard.account_settings`, `dashboard.logout` | TSK-0318 + Product/App |
| Device detail | `device.detail.title`, `device.status.ownership`, `device.status.configuration`, `device.status.verification`, `device.action.reverify`, `device.action.reinstall`, `device.action.replace`, `device.action.revoke`, `device.action.delete_record`, `device.action.remove_dns` | TSK-0318 + Product/App/DNS |
| Add device | `device.add.title`, `device.add.fresh_setup`, `device.add.cancel`, `device.add.no_implicit_transfer` | TSK-0318 + Product/UX |
| Reverify/reinstall/replace | `device.reverify.title`, `device.reinstall.title`, `device.replace.title`, `device.replace.no_implicit_status_transfer` | TSK-0318 + DNS/App/UX |

### Destructive account/device lifecycle

| Operation | Required consequence keys | Owning semantic source |
| --- | --- | --- |
| Revoke/unlink device | `device.revoke.title`, `device.revoke.consequence`, `device.revoke.confirm`, `device.revoke.result` | TSK-0318 + Account/device lifecycle |
| Delete dashboard record | `device.delete_record.title`, `device.delete_record.consequence`, `device.delete_record.confirm`, `device.delete_record.result` | TSK-0318 + Account/device lifecycle |
| Delete account | `account.delete.title`, `account.delete.consequence`, `account.delete.dns_not_removed`, `account.delete.anonymous_state_not_implied`, `account.delete.confirm`, `account.delete.result` | TSK-0318 + Account lifecycle/Privacy |
| Reset anonymous state | `anonymous.reset.title`, `anonymous.reset.consequence`, `anonymous.reset.account_not_deleted`, `anonymous.reset.dns_not_removed`, `anonymous.reset.confirm`, `anonymous.reset.result` | TSK-0318 + TSK-0229 boundary |
| Remove SafeWeb DNS | existing removal keys plus `removal.account_not_deleted`, `removal.device_record_not_deleted` | TSK-0318 + current TSK-0307/0317 |

## 7. Current truth and separation rules

Localization must preserve these semantic distinctions in every locale:

1. **Optional account is optional.** Translation may not turn “Sign in / Manage devices” into a prerequisite for core setup.
2. **Accountless fallback remains explicit.** Auth cancel/failure/provider outage must preserve a localized `Continue without account` route where current IA permits it.
3. **Session/account/device ownership is not protection evidence.** Localized `Signed in`, `Registered`, `Saved`, `Owned` or equivalent wording must never translate to or imply `Verified` protection.
4. **Destructive operations are not synonyms.** Logout, revoke/unlink, device-record deletion, account deletion, anonymous-state reset/deletion and physical DNS removal must have independent keys and consequence/result copy.
5. **No automatic J0/J1 linkage.** Localized account copy may not promise that account sign-in imports/promotes/copies anonymous journey state.
6. **No surveillance expansion.** No locale adds browsing/query/activity history, child profile/account, raw DNS admin/query-log or overall-safety-score concepts absent from current authority.
7. **SafeWeb visible identity is stable.** Parent-facing brand copy uses `SafeWeb` / `SafeWeb DNS`; technical `usesafeweb.com` hostnames/URLs remain exact LTR-isolated technical literals and are never translated.

## 8. Source-backed instruction binding remains single-authority

The existing nine TSK-0307 instruction IDs remain bound to setup/verification/removal/recovery keys. Current TSK-0307 source refreshes invalidate affected localized variants for publication until the bound row is rechecked; the localization layer cannot silently retain an older instruction string as authoritative.

Optional account/session/dashboard/device-management product copy is **not** added to the TSK-0307 instruction catalogue unless it is genuinely platform/source-owned. Product/auth/account lifecycle semantics remain owned by their current product/IA/lifecycle sources.

## 9. Deterministic fallback contract — preserved and extended

Fallback remains:

1. exact requested locale when a current eligible value exists;
2. `en-GB` baseline;
3. visible controlled missing-key failure in non-production/testing.

Additional dual-mode rules:

- a missing auth/session/destructive-operation consequence may not silently render an empty/ambiguous action;
- critical destructive consequence copy falls back to current `en-GB` rather than machine translation;
- a provisional locale indicator must not imply that account/session/device-lifecycle copy is complete when critical keys are falling back;
- no runtime machine translation is accepted for authoritative setup, verification, privacy, security, auth/session recovery or destructive lifecycle copy.

## 10. Plural/number/date/time rules — preserved

Use CLDR/Unicode-equivalent locale-aware runtime behavior. English-specific branching remains prohibited.

Account/dashboard additions follow the same rule:

- device counts use locale plural categories;
- session expiry/last-verification/currentness dates use semantic date/time values and locale-aware presentation;
- technical/audit timestamps stay ISO-8601 UTC internally;
- device IDs, provider IDs, DNS hostnames, URLs, versions and checksums are never localized;
- account email/provider identifiers, where an approved downstream UI genuinely displays them, are data values rather than translation strings and require safe bidi isolation.

## 11. RTL and accessibility — preserved and extended

For Arabic, document/container direction remains RTL while technical literals and applicable identity/data values use directional isolation.

Current dual-mode additions must also preserve:

- logical DOM/focus order through sign-in, errors, dashboard rows and destructive confirmations;
- programmatic association between auth/session errors and recovery actions;
- device-list rows with localized accessible names that distinguish devices without exposing prohibited identity/history;
- destructive controls whose accessible names state the actual operation;
- text expansion/reflow without hiding accountless fallback, consequences, removal or recovery actions;
- state/ownership/verification distinctions conveyed in text, not color/icon alone.

## 12. Current content ownership

Historical ownership remains and is extended:

| Content class | Accountable owner | Required review owner |
| --- | --- | --- |
| Public/navigation/general UI | UX/Content | Product where product meaning changes |
| DNS setup/verification/removal | UX/Content | Network Engineering + TSK-0307 source owner |
| Protection-state labels/explanations | Product/UX | TSK-0320 semantic owner |
| Troubleshooting/recovery | Support/UX | Network Engineering; Privacy/Security where applicable |
| Optional account entry/auth/session | Product/Auth Content | Auth/App/Security where behavior changes |
| Dashboard/device management | Product/UX | App/Auth + owning device-lifecycle source |
| Account/device destructive lifecycle | Product/UX | Auth/App/Privacy + owning lifecycle source |
| Privacy/non-surveillance | Privacy + Product | Legal only where legal conclusion is actually required |
| Accessibility-specific copy | UX | Accessibility review |
| Localized variants | UX/Content | Native/qualified language review when publication becomes eligible |

AI may draft provisional locale values but cannot claim native-speaker, legal or representative-parent validation.

## 13. Schema/content versioning — preserved

Two independent versions remain mandatory:

1. localization schema version for key/file/metadata contract;
2. per-locale content bundle semantic version.

This dual-mode extension is a **minor-compatible schema/content expansion** because it adds namespaces/keys without removing the still-valid accountless keys. A future implementation must migrate/version any actual bundle atomically enough that UI code never references a current key absent from the baseline locale.

## 14. Current testable acceptance assertions

A later implementation must be able to prove at least:

1. `en-GB`, `tr-TR`, `ar` bundles parse successfully.
2. Every user-facing key referenced by current TSK-0318 public/accountless/account/session/dashboard/device-lifecycle IA exists in `en-GB`.
3. No current UI component hard-codes user-facing copy outside explicitly exempt immutable technical literals/data values.
4. `tr-TR` and `ar` keys either contain an eligible value or deterministically fall back to `en-GB`.
5. Critical TSK-0307 setup/verification/removal keys bind to the current instruction ID, not copied stale text.
6. Missing keys fail visibly in test/dev rather than rendering empty UI.
7. Arabic declares RTL; technical literals/data values are directionally isolated.
8. Plural/number/date/session-expiry/currentness behavior uses the locale runtime rather than English branching.
9. Locale content/schema versions are readable/diffable and changed keys are attributable.
10. Localization cannot change support, protection evidence, account ownership, market activation or destructive-operation semantics.
11. Accessibility names/status/error relationships survive locale switching.
12. No locale bundle contains user/device identity, browsing/query/activity history, credentials, tokens or raw diagnostics as localization content.
13. Public optional account entry and post-core account choice retain a first-class accountless alternative in all locales.
14. Auth/provider failure exposes a localized accountless fallback where the current IA requires it.
15. Account/session/device ownership labels cannot reuse or alias the protection `Verified` key.
16. Logout, revoke/unlink, delete-device-record, delete-account, anonymous-state reset and DNS removal have distinct keys and consequence/result copy.
17. Account deletion copy explicitly does not claim DNS removal; DNS removal copy does not claim account/device-record deletion.
18. SafeWeb visible brand and exact technical endpoints survive locale switching without translation or bidi corruption.

## 15. Acceptance reconciliation

ACC-0311 requires: **English baseline uses externalized content; no hard-coded UI copy blocks Turkish/Arabic; locale fallback and content versioning are testable.**

Current result:

- English semantic baseline remains externalized and now covers the full current dual-mode IA.
- Turkish/Arabic remain structurally unblocked because the same stable namespaces/keys/fallback model covers all new account/session/dashboard/device-lifecycle surfaces.
- Fallback remains deterministic and now includes explicit rules for auth/session/destructive critical copy.
- Content/schema versioning remains independently testable.
- The historical accountless architecture remains valid provenance; only its incomplete current surface inventory is superseded.

## 16. Non-inference

This is L4 localization/content architecture evidence only. It does not implement production locale files, certify Turkish/Arabic linguistic quality, claim native-speaker or representative-parent validation, activate a market, implement authentication/session/dashboard/device ownership, complete legal/privacy review, publish, process participants, activate payment, pass LG-06, launch or infer successor PASS.

**TSK-0311 current result candidate: PASS subject to independent VER-0311, durable EVD-0311, guarded runtime reconciliation and exact read-back.**
