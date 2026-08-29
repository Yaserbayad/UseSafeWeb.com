# TSK-0311 — Localization, Translation-Key and Content-Version Architecture

**Task:** `TSK-0311 — Define translation keys/files, locale metadata, plural/date rules, content ownership, localized instruction variants, and fallback behavior`  
**Acceptance:** `ACC-0311`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Action authority:** `AUTO_ALLOWED`  
**Status:** **PROVISIONAL INTERNAL L4 DESIGN / IMPLEMENTATION AND PUBLICATION NOT AUTHORIZED**  
**Date:** 2026-08-29

## 1. Authority and scope

This contract externalizes all current user-facing copy for the provisional accountless first-phone product without activating markets or widening supported devices/services.

Authoritative inputs:

- approved TSK-0318 public/product IA;
- TSK-0307 source-backed instruction/content catalogue;
- TSK-0320 protection-state/copy rules;
- TSK-0559 content quality/source/update/localization standard;
- TSK-0314 accessibility requirements;
- TSK-0229 accountless data/no-linkage rules;
- DEC-0050/CR-0003 provisional-L4 boundary.

`RSK-0002` remains OPEN. Language variants are not representative-parent validation. `REQ-0022` remains unresolved. Language availability does not activate a market, jurisdiction, legal claim, payment path or launch.

## 2. Locale baseline

| Locale | Role | Direction | Status | Market implication |
| --- | --- | --- | --- | --- |
| `en-GB` | Canonical authored baseline | LTR | **ACTIVE DESIGN BASELINE** | None; publication still gated. |
| `tr-TR` | Localized variant | LTR | **PROVISIONAL** | No Turkish-market activation. |
| `ar` | Localized Arabic variant | RTL | **PROVISIONAL** | No Arabic-market activation or region assumption. |

Rules:

1. `en-GB` is the canonical semantic source for ordinary UI copy unless a source-controlled instruction row explicitly owns the content.
2. `tr-TR` and `ar` may never broaden support, remove limitations or turn provisional evidence into verified fact.
3. Locale is presentation metadata only. Product support remains controlled by TSK-0409 and state truth by TSK-0320.
4. Arabic direction is RTL at the document/container level while technical literals such as hostnames, URLs, version strings and IDs remain isolated in their natural direction.

## 3. Externalized file model

No user-facing production UI sentence, button label, status label, help heading, validation error, setup instruction or recovery instruction may be embedded directly in component/source code.

Recommended logical file layout:

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
  tr-TR/
    ...same namespaces...
  ar/
    ...same namespaces...
content/
  instruction-bindings.json
  content-versions.json
```

The exact repository/framework implementation may differ later, but the following invariants are mandatory:

- same stable translation key exists across supported locale files;
- application/UI code references keys, never hard-coded user-visible copy;
- source-controlled technical instruction copy is bound by catalogue/content ID rather than independently rewritten in UI code;
- missing locale values resolve through the defined fallback chain, never blank UI or invented machine copy;
- locale files are version-controlled and independently diffable.

## 4. Key taxonomy

Stable keys use semantic intent, not English wording, so copy can change without renaming the key.

Pattern:

```text
<surface>.<context>.<element>[.<variant>]
```

Required namespaces and representative keys:

| Namespace | Representative keys | Owning semantic source |
| --- | --- | --- |
| `common` | `common.action.continue`, `common.action.back`, `common.action.exit`, `common.action.help`, `common.action.start_over` | UX |
| `navigation` | `navigation.home`, `navigation.how_it_works`, `navigation.compatibility`, `navigation.privacy`, `navigation.help`, `navigation.start_setup` | TSK-0318 |
| `setup` | `setup.router.title`, `setup.android.private_dns.title`, `setup.iphone.profile.title`, `setup.external_safeguard.title` | TSK-0318 + TSK-0307 |
| `verification` | `verification.checking`, `verification.retry_after_change`, `verification.service_issue` | TSK-0319 + TSK-0320 |
| `protection_map` | `protection.verified.label`, `protection.parent_confirmed.label`, `protection.action_needed.label`, `protection.not_covered.label`, `protection.uncertain.label`, `protection.removed.label` | TSK-0320 |
| `troubleshooting` | `troubleshooting.unsupported.title`, `troubleshooting.vpn_conflict.title`, `troubleshooting.private_relay.title`, `troubleshooting.stale_guidance.title` | TSK-0319 |
| `removal_recovery` | `removal.android.title`, `removal.iphone.title`, `recovery.normal_restored`, `recovery.still_failed`, `recovery.uncertain` | TSK-0317 + TSK-0319 |
| `accessibility` | `accessibility.status_prefix`, `accessibility.progress_step`, `accessibility.external_link_suffix` | TSK-0314 |

Key renaming is a schema change and requires migration or compatibility aliasing. Copy edits alone are content-version changes, not key changes.

## 5. Source-backed instruction binding

TSK-0307 remains the owner of current source-backed setup/verification/removal instruction semantics. The localization layer must not create a second mutable instruction authority.

`content/instruction-bindings.json` conceptually maps:

```json
{
  "setup.android.private_dns.body": "INS-AND-SETUP-01",
  "verification.android.body": "INS-AND-VERIFY-01",
  "removal.android.body": "INS-AND-REMOVE-01",
  "setup.iphone.profile.body": "INS-IOS-SETUP-01",
  "verification.iphone.body": "INS-IOS-VERIFY-01",
  "removal.iphone.body": "INS-IOS-REMOVE-01",
  "verification.uncertain.body": "INS-COMMON-UNCERTAIN-01",
  "setup.not_covered.body": "INS-COMMON-NOTCOVERED-01",
  "recovery.connectivity.body": "INS-COMMON-RECOVERY-01"
}
```

For those keys:

- `en-GB` value is the current catalogue baseline;
- `tr-TR`/`ar` values use the catalogue's provisional variants when present;
- any later translation change must preserve the source row's applicability, known limits and truth state;
- a TSK-0307 review trigger invalidates affected localized variants for publication until rechecked.

## 6. Locale manifest

`locale-manifest.json` must make status and fallback machine-testable.

Minimum fields per locale:

```json
{
  "locale": "en-GB",
  "language": "en",
  "region": "GB",
  "direction": "ltr",
  "fallback": null,
  "status": "baseline",
  "marketActivation": false,
  "contentVersion": "1.0.0",
  "lastVerified": "2026-08-29",
  "owner": "UX/Content"
}
```

For `tr-TR` and `ar`, `status` is `provisional`, `fallback` is `en-GB`, and `marketActivation` remains `false`.

## 7. Fallback contract

Fallback is deterministic:

1. exact requested locale, if an eligible current value exists;
2. `en-GB` baseline value;
3. controlled internal missing-key failure in non-production/testing.

Hard rules:

- never silently fall back from a missing safety/privacy/legal/critical limitation string while displaying a locale indicator that falsely implies complete localization;
- when a provisional locale lacks a critical current translation, present the `en-GB` value and expose a non-user-identifying internal fallback event for QA if later implementation authorizes telemetry/logging;
- no runtime machine translation is used as a fallback for authoritative setup, safety, privacy, legal, verification or recovery copy;
- missing key/value must never become an empty button, unlabeled control or hidden limitation.

## 8. Plural, number and date/time rules

Use locale-aware platform/runtime internationalization based on CLDR/Unicode locale data or an equivalent standards-conformant implementation. Do not implement English-specific plural logic in application code.

Rules:

- plural/select behavior uses locale categories supported by the runtime (`one`, `few`, `many`, `other`, etc. as applicable);
- counts/numbers use locale-aware formatting rather than concatenated English punctuation;
- dates use locale-aware formatting with explicit semantic date/time values, not preformatted English strings;
- machine/audit timestamps and evidence remain ISO-8601 UTC internally; localized presentation may format them for the UI where needed;
- relative-time phrases, if later used, are generated through locale-aware formatting, not hard-coded suffix/prefix rules;
- technical identifiers, DNS hostnames, URLs, version numbers and checksums are never localized.

Current accountless setup should avoid unnecessary dates/counts; these rules prevent later UI additions from hard-coding English assumptions.

## 9. RTL and accessibility rules

For `ar`:

- page/container direction is `rtl`;
- layout must use logical properties (`start`/`end`) rather than hard-coded left/right assumptions where implementation supports them;
- icons with directional meaning mirror only when meaning requires it; neutral product/status icons do not mirror automatically;
- hostnames/URLs/code literals use directional isolation;
- keyboard/focus order follows semantic DOM/task order, not visual mirroring hacks.

Across all locales:

- translated labels must preserve accessible names and programmatic relationships;
- status meaning may not depend on color or icon;
- localized text expansion/reflow must not hide controls, limitations or recovery actions;
- screen-reader text is externalized under the same locale/key contract.

## 10. Content ownership

| Content class | Accountable owner | Required technical/review owner |
| --- | --- | --- |
| General navigation/product UI | UX/Content | Product when product meaning changes |
| DNS setup/verification/removal instructions | UX/Content | Network Engineering + TSK-0307 source owner |
| Protection-state labels/explanations | Product/UX | TSK-0320 semantic owner |
| Troubleshooting/recovery help | Support/UX | Network Engineering; Privacy/Security where applicable |
| Privacy/non-surveillance copy | Privacy + Product | Legal only where legal conclusion is required |
| Accessibility-specific copy | UX | Accessibility review |
| Localized variants | UX/Content | Native/qualified language review when publication later becomes eligible |

AI may draft/maintain provisional locale values but cannot claim native-speaker or representative-parent validation.

## 11. Content versioning

Use two independent versions:

1. **Schema version** — key/file/metadata contract, e.g. `localizationSchemaVersion: 1`.
2. **Content version** — locale content bundle semantic version, e.g. `1.0.0`.

Version rules:

- patch: wording/source-refresh that preserves semantics and key contract;
- minor: added keys/surfaces or backwards-compatible locale content;
- major: removed/renamed keys, fallback-contract change, or semantic incompatibility requiring coordinated UI migration.

Each locale release record must include content version, source baseline/relevant catalogue IDs, last verified date, owner/reviewer and changed keys. No user identity or behavioral history is stored in this registry.

## 12. Testable acceptance assertions

A later implementation must be able to prove at least:

1. `en-GB`, `tr-TR` and `ar` locale bundles parse successfully.
2. Every user-facing UI key referenced by the current IA exists in `en-GB`.
3. No current UI component contains a hard-coded user-facing sentence/label outside explicitly exempt technical literals.
4. Every `tr-TR` and `ar` key either has an eligible value or deterministically falls back to `en-GB`.
5. Critical setup/verification/removal values bind to the correct TSK-0307 instruction ID.
6. Missing keys fail visibly in test/dev rather than silently rendering empty UI.
7. Arabic declares RTL and technical literals remain directionally isolated.
8. Plural/number/date behavior uses the locale runtime rather than English branching.
9. Locale content versions and schema version are readable and diffable.
10. Localized copy cannot change support/verification state or market activation.
11. Accessibility names/status semantics survive locale switching.
12. No locale bundle contains user/device identity, browsing/query history, credentials or raw diagnostics.

## 13. Current bounded result

TSK-0311 defines a complete, testable localization architecture for the current IA. The English baseline is externalized by contract, Turkish/Arabic cannot be blocked by hard-coded UI copy, and fallback/content-version behavior is deterministic.

This is **design evidence only**. It does not implement locale files in a production application, prove translations are linguistically/publication-ready, activate Turkish/Arabic markets, prove representative-parent comprehension, or authorize public release.