# TSK-0323 — Device and Service Instruction Catalogue Acceptance Evidence

**Task:** `TSK-0323 — Create versioned device and service instruction catalogue`  
**Acceptance:** `ACC-0323`  
**Verification:** `VER-0323`  
**Evidence:** `EVD-0323`  
**Lifecycle:** L4  
**Owner:** Content  
**Action authority:** A3 / AUTO_ALLOWED  
**Date:** 2026-08-29  
**Disposition:** PASS

## 1. Acceptance contract

ACC-0323 requires every instruction to have platform/version applicability, source reference, last verified date, owner, expected result, fallback and test case, with unsupported states explicit.

VER-0323 requires review against current approved product/claim/accessibility/source/surface authority and representative task checks where applicable. Under current `DEC-0052 / CR-0005`, pre-product parent/user/participant validation is excluded from the L4–L7 critical path and is not claimed here; technical/source/scenario/content verification remains applicable and was performed.

EVD-0323 requires artifact/version, exact source/environment, test/review output, date, responsible verifier, deviations and disposition.

## 2. Accepted artifacts

| Artifact | Version | Publication commit | Git blob |
| --- | --- | --- | --- |
| `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` | 1.0.0 | `412946c850640d95e3bc46e9b7bdec6c49a527f3` | `bbe9ed90b205f2ca852ebdaefedf054446dd7f91` |
| `content/TSK-0323/CATALOGUE.json` | 1.0.0 / schema `usesafeweb.device-service-instructions.v1` | `db04be14f428e81b7e78ed8a3ee89b0abc9a1d30` | `842e18c5666a82d53e2d348715dd6b9198daa44c` |

The catalogue contains 12 unique current records covering Android/iPhone DNS setup, verification and removal; common conflict/not-covered/recovery behavior; iPhone/Android native-safeguard routing; and the bounded zero-or-one external-service route.

## 3. Project-owned source pins

The successful verifier independently recomputed Git blobs and matched all pinned current project-owned inputs:

| Source | Git blob |
| --- | --- |
| TSK-0307 source-backed instruction catalogue | `d717c9b3f66197abe1f3e73361633f222b817e7c` |
| TSK-0317 platform setup/removal/recovery design | `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d` |
| TSK-0409 supported OS/device/network matrix | `09318534ec097849cbe8c7391e2a1acc3ba5a79a` |
| TSK-0143 native-device safeguard routing | `20b588c27bc0d71249bec2c83f33cf551afa4ff0` |
| TSK-0144 one-relevant-service routing | `f7821c8ef50aa517753c31477b383d660de11f40` |
| TSK-0320 protection-state/copy contract | `1146f7622f434590dde1253d11f14fb6a87e19de` |
| TSK-0322 product language policy | `d12c1e707f0390915002b27bf3a5073d0135d466` |
| TSK-0319 troubleshooting/recovery/help design | `86de353dd8446f02ed48c80638391a3caa852e59` |

## 4. Current external-source review

First-party source currency was rechecked on 2026-08-29 before acceptance. The catalogue records the exact URLs and check date.

- Google Android Help — Private DNS: `https://support.google.com/android/answer/9654714?hl=en` — current provider-hostname/Automatic semantics and DNS-only scope remain supported.
- Google Chrome Help — Secure DNS: `https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DAndroid&hl=en` — browser-level Secure DNS can use automatic/another provider and therefore remains a resolver-conflict consideration.
- Apple Platform Deployment — DNS Settings: `https://support.apple.com/en-gb/guide/deployment/dep86469ba99/1/web/1.0` — HTTPS/TLS DNS payload semantics remain supported.
- Apple iPhone User Guide — Install/remove configuration profiles: `https://support.apple.com/en-euro/guide/iphone/iph6c493b19/ios` — user permission/profile-management semantics remain supported.
- Apple Personal Safety — Profile removal: `https://support.apple.com/guide/personal-safety/review-and-delete-configuration-profiles-ips327569a75/1.0/web/1.0` — removal removes associated settings and management authority remains relevant.
- Apple Support UK — Screen Time / parental controls: `https://support.apple.com/en-gb/105121` — current native parental-control family remains supported.
- Google Android Help — current Android parental controls: `https://support.google.com/android/answer/16766047?hl=en` — current Android 17+ on-device parental controls remain a conditional route.
- Google For Families — Family Link supported devices: `https://support.google.com/families/answer/9116646?hl=en` — Android supervision remains supported where applicable; most supervision tools remain unavailable on iPhone/iPad.

No reviewed first-party fact contradicted the current conservative TSK-0409/TSK-0143 support/routing model.

## 5. Deterministic verification

**Environment:** self-hosted GitHub Actions runner `adguardvm`, Linux x64.  
**Successful workflow:** `.github/workflows/verify-tsk0323.yml` at commit `83e36025f14fd235672a5e315ed823e3bb6bcfd2`.  
**Run:** `33268849558`.  
**Job:** `99143590468`.  
**Checkout/head:** `83e36025f14fd235672a5e315ed823e3bb6bcfd2`.

Terminal evidence:

- `SCHEMA=PASS`
- `IDENTITY_VERSION=PASS`
- `SEQUENCING=PASS`
- `CR0005_HUMAN_VALIDATION_DISPOSITION=PASS`
- `RECORD_SET=PASS`
- all 12 `FIELDS_*`, `VERSION_DATE_*`, and `TEST_BINDING_*` checks PASS
- `UNIQUE_TEST_CASES=PASS`
- all eight `SOURCE_BLOB_*` checks PASS
- `CATALOGUE_MD_BLOB=PASS`
- `CATALOGUE_JSON_BLOB=PASS`
- `SOURCE_BLOB_PINS=PASS`
- `WBS_AUTHORITY=PASS`
- `PREDECESSOR_RUNTIME_PASS=PASS`
- all 12 scenario checks PASS
- `SCENARIO_TESTS=12/12 PASS`
- all explicit unsupported-class checks PASS
- `NO_HARDCODED_NAMED_SERVICE=PASS`
- `NO_MANDATORY_ACCOUNT_CLAIM=PASS`
- `PRIVACY_FENCE=PASS`
- `I18N_RTL_FENCE=PASS`
- all prohibited-claim guards PASS
- `CLAIMS_PRIVACY_I18N=PASS`
- all eight current external-source records PASS structural/date checks
- `CATALOGUE_JSON=PASS`
- `RECORD_COUNT=12`
- `TSK0323_VERIFICATION=PASS`
- `REPOSITORY_CLEAN=PASS`

## 6. Representative task results

| Scenario | Result |
| --- | --- |
| Supported Android DNS setup | PASS — exact hostname-only input, user-controlled OS action, no S1 from configuration alone. |
| Android verification with resolver/VPN conflict | PASS — positive state is not preserved beyond evidence; S5/S4/repair semantics are explicit. |
| Android removal/recovery | PASS — normal policy recovery and S6/claim withdrawal are explicit. |
| Supported iPhone profile setup | PASS — exact DoH URL, explicit OS approval, no silent install/no S1 from profile presence. |
| iPhone verification with unresolved conflict | PASS — S5 rather than inferred verification. |
| iPhone profile removal | PASS — exact profile removal, S6, management boundary preserved. |
| Common conflict handling | PASS — S3 only with proven repair; otherwise S5/S4 and safe fallback. |
| Unsupported device/network tuple | PASS — S4/S5 and no guessed setup. |
| Connectivity recovery | PASS — exact SafeWeb config removed/reset; protection claim withdrawn. |
| iPhone native safeguard | PASS — already-configured shortcut/S2, Apple-owned setup, blocked/unmatched S4/S5. |
| Android native safeguard | PASS — exact applicable Android 17+/Family Link route only, S2 not S1, no credentials. |
| External service | PASS — zero-service is valid; no named service is invented; at most one future current approved service branch. |

## 7. Deviation/retry record

Initial verifier run `33268817512`, job `99143510591`, stopped at `NO_MANDATORY_ACCOUNT_CLAIM` after all earlier structural/source/WBS/scenario/unsupported checks had passed. Root cause was a verifier guard that banned the phrase `mandatory SafeWeb account` even when used inside the required prohibition sentence `No instruction adds a mandatory SafeWeb account`. No catalogue/source/runtime mutation resulted from that failure. The verifier was corrected to positively require the prohibition; the materially different corrected run `33268849558` then passed all remaining and previously passed checks. This is a closed harness defect, not a product/catalogue defect.

## 8. Scope, privacy and current limitations

- No parent/user/participant evidence was collected or fabricated; such evidence is non-applicable to this pre-product L4 acceptance under DEC-0052/CR-0005.
- No mandatory SafeWeb account, persistent dashboard, browsing/DNS history, child identity profile, Apple/Google/provider credential, token or MFA collection is introduced.
- No named external service is hard-coded in v1.0.0. A provider becomes supported only through a later current provider-specific record satisfying TSK-0144/current-source requirements.
- Unsupported/unproven platform, management, network and resolver combinations remain S4/S5 rather than inferred support.
- This evidence does not authorize implementation, public publication, production release, payment, real-user activity or launch by itself.

## 9. Disposition

`ACC-0323`, `VER-0323` and `EVD-0323` are satisfied by the exact v1.0.0 artifacts and successful deterministic verification above.

**TSK-0323: PASS.**
