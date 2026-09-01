# TSK-0041 — Post-CR-0008 Current Requalification Amendment

**Task:** TSK-0041 — Specify baseline DNS-protection activation requirements  
**Acceptance:** ACC-0041 / VER-0041 / EVD-0041  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 2.0.0-post-CR-0008 amendment  
**Date:** 2026-09-01  
**Authority:** current CR-0008 / DEC-0055 owner-frozen modular Master Planning System; current TSK-0143 routing; current TSK-0320 truth-state contract; current TSK-0409 supported-device/network matrix; current accepted TSK-0408 endpoint/mechanism semantics.  
**Base contract preserved:** `TSK_0041_BASELINE_DNS_PROTECTION_ACTIVATION_REQUIREMENTS_2026-08-28.md`, blob `95a5292223f1d2c3c8f79d4c889ad91e917478b2`.  
**Status:** current-requalification candidate only; no implementation, LG-07, build, production, market, launch or real-user outcome is inferred.

## 1. Requalification decision

The 2026-08-28 TSK-0041 contract remains the base requirements contract. Its endpoint-format, encrypted-DNS, filtering-verification, fail-safe, removal/recovery, false-positive and no-history rules remain technically and product-semantically valid.

Four bounded areas are superseded by this amendment because the old wording no longer fully represents current authority:

1. static OS minimums are replaced by the current versioned support catalogue/matrix rule;
2. the old Private Relay statement is narrowed to the currently source-supported network/filtering conflict boundary;
3. the historical accountless-only / CR-0003 lifecycle wording is updated to the current dual-mode Version-1 and integrated-product-first/production-only lifecycle;
4. historical TSK-0409 and TSK-0320 evidence references are replaced by their current post-CR-0008 accepted contracts.

Everything not explicitly superseded below remains preserved from the base contract.

## 2. Current authority and dependency

Current governing facts:

- CR-0008 / DEC-0055 remains the owner-frozen planning/evidence/action-authority normalization and does not weaken acceptance, scope or dependencies.
- TSK-0041 remains L4 / MEDIUM / A3 / `AUTO_ALLOWED` with hard dependency TSK-0143 under the current WBS; exact metadata must be independently checked before PASS.
- Current TSK-0143 is PASS and requires versioned support routing, explicit already-configured handling, truthful parent-confirmed versus technically verified separation, unsupported/not-applicable/stale paths and fail-closed uncertainty.
- Current TSK-0320 is PASS and permits `protected_verified` only from fresh qualifying technical evidence. Configuration/profile/ClientID/account/dashboard/parent-confirmation/journey-completion evidence cannot substitute.
- Current TSK-0409 is PASS and owns the supported-device/network/bypass matrix. TSK-0041 consumes that matrix and does not independently expand platform support.
- Current TSK-0408 mechanism semantics remain the accepted endpoint basis: Android native Private DNS uses the hostname `dns.usesafeweb.com` with DoT semantics; the Apple approved encrypted-DNS profile path uses the HTTPS Server URL `https://dns.usesafeweb.com/dns-query`.

## 3. Superseded support-range wording

The base contract's broad static family statements `Android 9+` and `iPhone/iOS 14+` are no longer sufficient by themselves to call a current platform/version supported.

Current rule:

> A device/platform/version enters the normal TSK-0041 activation path only when the current TSK-0409 matrix plus the versioned instruction/guidance catalogue classify that exact mechanism/path as supported or conditional with a defined verification/recovery contract.

Therefore:

- Android uses the approved system `Private DNS provider hostname` mechanism only when that mechanism is currently present, usable and supported for the observed device/version/context.
- Apple uses the approved DoH profile/Server-URL mechanism only when the current platform/version/profile path is supported by the current matrix/catalogue.
- Generic similarity to an older supported major version is not support evidence.
- Newly released, unknown, managed, vendor-modified or otherwise unclassified combinations are `uncertain_error` or `not_covered` until current support evidence exists.
- No unsupported combination is silently routed into an app/VPN/browser-specific fallback.

The base endpoint strings remain unchanged:

- Android native input: `dns.usesafeweb.com`
- Apple approved DoH Server URL: `https://dns.usesafeweb.com/dns-query`

## 4. Current truth-state mapping

The base S1-S6 labels are retained only as human-readable aliases. Current canonical state semantics are:

| Base alias | Current canonical state | Current evidence rule |
|---|---|---|
| S1 Verified | `protected_verified` | Fresh qualifying technical evidence proves the effective UseSafeWeb DNS/filtering path for the claimed scope. |
| S2 Parent confirmed/configured | `configured_parent_confirmed` | Configuration/profile/parent evidence only; never technical verification. |
| S3 Action needed | `action_needed` | Supported path needs a known corrective action or setup step. |
| S4 Not covered | `not_covered` | Known unsupported/bypassed combination or no approved path. |
| S5 Status uncertain/error | `uncertain_error` | Effective resolver cannot currently be established, evidence is stale/contradictory, or an unclassified conflict/error exists. |
| S6 Removed | `removed` | Evidence-backed removal of the target UseSafeWeb mechanism/scope; account/device-record deletion alone is not DNS-removal proof. |

Every material DNS-path change invalidates stale technical-verification freshness for the affected scope. Sign-in, account ownership, dashboard/device persistence or parent confirmation cannot strengthen a DNS protection state.

## 5. Current platform/bypass truth

### Android Private DNS

Google's current Android Help continues to expose `Off`, `Automatic`, and `Private DNS provider hostname`, and states that Private DNS protects DNS questions/answers only. TSK-0041 therefore preserves hostname-only Android routing and the DNS-layer-only claim boundary.

Current source: https://support.google.com/android/answer/9654714

### Chrome Secure DNS

Current Chrome Help states that Chrome Secure DNS can use the current service provider or another/custom provider, and that automatic mode may fall back to unencrypted lookup when Chrome has lookup problems. The system Android Private DNS setting therefore cannot by itself prove Chrome traffic uses UseSafeWeb.

Current source: https://support.google.com/chrome/answer/10468685

Current consequence: a custom non-UseSafeWeb Chrome resolver is `not_covered` for that browser scope; an indeterminate Chrome resolver path is `uncertain_error`; any positive browser-scope claim requires fresh technical verification.

### Firefox DoH

Current Mozilla documentation confirms Firefox DoH can select its own resolver; current Mozilla VPN guidance states Firefox DoH takes priority over the resolver configured in the Mozilla VPN application. Mozilla also documents that DoH can bypass filtering supplied by a network/default resolver.

Current sources:
- https://support.mozilla.org/en-US/kb/firefox-dns-over-https
- https://support.mozilla.org/en-US/kb/dns-over-https
- https://support.mozilla.org/en-US/kb/how-will-dns-work-when-using-vpn-extension
- https://support.mozilla.org/en-US/kb/configuring-networks-disable-dns-over-https

Current consequence: no system-DNS `protected_verified` state automatically extends to Firefox when Firefox uses an independently selected resolver.

### Apple encrypted DNS

Current Apple deployment documentation continues to support encrypted DNS settings using HTTPS or TLS and defines the HTTPS Server URL semantics for the DNS Settings payload. The base Apple DoH endpoint semantics remain compatible with current platform documentation.

Current source: https://support.apple.com/en-gb/guide/deployment/dep86469ba99/web

### iCloud Private Relay

The base contract statement that Apple directly confirms Private Relay "includes DNS name-resolution handling" is not required for ACC-0041 and is superseded here by the narrower current first-party fact: Apple states that some networks/services performing network-based filtering may be incompatible with Private Relay and documents per-network control through `Limit IP Address Tracking`.

Current source: https://support.apple.com/en-ie/102022

Current consequence: Private Relay is a resolver/network-path conflict boundary for UseSafeWeb claims. While active, `protected_verified` requires fresh technical evidence for the exact claimed scope. If the effective UseSafeWeb DNS path cannot be proven, state is `uncertain_error` or `not_covered` according to the current matrix. UseSafeWeb does not make disabling Private Relay a default requirement merely to obtain a green state.

### VPN/app/custom resolver and network changes

The current TSK-0409 matrix remains authoritative. VPNs, app-specific resolvers, captive portals, Wi-Fi/cellular transitions, browser resolver changes, profile changes and other DNS-affecting transitions require current re-verification or explicit `not_covered` / `uncertain_error` handling. Prior successful verification may not be carried across a materially changed effective DNS path.

## 6. Filtering verification, fail-safe and false-positive rules preserved

The following base-contract requirements are preserved unchanged in substance:

- encrypted transport reachability alone is insufficient for `protected_verified` when filtering is unproven;
- controlled/synthetic allowed and filtering checks are required rather than routine real browsing history;
- endpoint/authentication/effective-resolver uncertainty cannot retain a positive UseSafeWeb protection claim;
- no hidden unencrypted/plain-DNS fallback may retain a UseSafeWeb protection state;
- safe removal/recovery remains a first-class outcome;
- one false positive must use the narrowest justified reversible correction and regression re-test, never blanket filtering disablement;
- no complete-safety, universal-app/network, surveillance or monitoring claim is permitted.

AdGuard remains the frozen backend filtering/policy layer. Quad9 `dns10` with ECS disabled remains a separate frozen server-side invariant under its owning controls; TSK-0041 does not change it.

## 7. Dual-mode Version-1 scope correction

The base contract's "active accountless limitation" is preserved only for the **core activation path**. Current Version 1 is dual-mode:

- the complete core DNS setup/verification/recovery/removal journey remains usable without login;
- an optional parent account/lightweight dashboard/device-management surface is in approved scope;
- account/device/dashboard persistence never creates DNS technical-verification evidence;
- no automatic anonymous-state-to-account promotion/linkage is authorized outside its separately approved data-flow contract;
- no persistent per-parent/per-device DNS allowlist or unrestricted/raw AdGuard administration is created by TSK-0041;
- browsing/query/activity history and child surveillance profiles remain excluded.

A later separately approved persistent exception feature, if ever added, must have its own product/privacy/security/architecture authority and cannot be inferred from the existing global narrow technical exception mechanism.

## 8. Current lifecycle/evidence boundary

Historical CR-0003 language in the base artifact/evidence is provenance only where superseded.

Current sequencing:

- DEC-0052 / CR-0005 excludes pre-product human/user validation from L4-L7 progression; no behavioral evidence is claimed here.
- DEC-0053 / CR-0006 authorizes the dual-mode Version-1 scope described above.
- DEC-0054 / CR-0007 maximizes evidence-driven autonomy and uses the production-only active lifecycle after integrated readiness; no mandatory pilot/staging lifecycle is reintroduced here.
- DEC-0055 / CR-0008 governs proportional evidence and current action authority.
- LG-06 is already current PASS from separate evidence. TSK-0041 requalification neither caused nor reopens that PASS unless a contradiction is found.
- TSK-0041 remains an L4 requirements contract. It does not infer LG-07, implementation, build, release, production activation, market activation, launch, legal-compliance completion or real-user validation.
- RSK-0002 remains OPEN and non-blocking before L8; first real-user validation remains after LG-09 and applicable prerequisites.

## 9. Current evidence references

Current requalification consumes:

- base TSK-0041 contract blob `95a5292223f1d2c3c8f79d4c889ad91e917478b2`;
- base 2026-08-28 evidence blob `66cdc50ae2fbb9ec4501b408837d01aafcba876d` as historical provenance for preserved clauses;
- current TSK-0143 routing artifact `TSK_0143_NATIVE_DEVICE_SAFEGUARD_ROUTING_REQUIREMENTS_2026-09-01.md`, blob `7eca238090738f282db2b43c7f988a7ff716df19`;
- current TSK-0320 truth-state artifact `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md`, blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`;
- current TSK-0409 support/bypass artifact `TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md`, blob `3aa832777276115912e4f3990b30cb541c458f4f`;
- accepted TSK-0408 endpoint/mechanism contract `TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md`, blob `52860ce167fc8a31962cd412772e428d280c8184`, only for still-current endpoint/mechanism semantics;
- current CR-0008 WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and Layer-5 blob `2097d83961affaa69850e41a5ffcd72a660d69cd`.

## 10. ACC-0041 current clause disposition

ACC-0041 requires endpoint format, DoH setup, filtering verification, fail-safe behavior, uninstall/removal, Private Relay/VPN conflicts, false positives and no-history constraints.

| ACC-0041 clause | Current disposition | Basis |
|---|---|---|
| Endpoint format | PASS candidate | Android hostname-only and Apple HTTPS Server URL remain current and platform-specific. |
| DoH setup | PASS candidate | Apple approved path remains DoH; Android remains native Private DNS/DoT rather than a fabricated universal DoH workflow. |
| Filtering verification | PASS candidate | Fresh effective-path + filtering evidence required; configuration/transport alone cannot produce `protected_verified`. |
| Fail-safe behavior | PASS candidate | Unverified/failed/conflicting path cannot retain a positive protection claim; no hidden plain-DNS protected fallback. |
| Uninstall/removal | PASS candidate | Removal remains evidence-backed, reversible and distinct from account/device-record deletion. |
| Private Relay/VPN conflicts | PASS candidate | Current TSK-0409 plus current Apple/Google/Mozilla sources preserve conservative re-verification/not-covered/uncertain semantics. |
| False positives | PASS candidate | Narrow, reproducible, reversible correction + regression; no blanket filtering disablement or invented personal DNS-admin surface. |
| No-history constraints | PASS candidate | Routine verification requires no browsing/query/domain history, child activity or persistent identity linkage. |

## 11. Independent verification requirements

TSK-0041 may be reconciled to current PASS only if an independent deterministic verifier confirms all of the following against current `main`:

1. exact current WBS metadata, dependency `TSK-0143`, A3/AUTO_ALLOWED, ACC-0041/VER-0041/EVD-0041;
2. current CR-0008 WBS and Layer-5 blobs are unchanged;
3. current TSK-0143, TSK-0320 and TSK-0409 accepted-state markers are present;
4. exact base/amendment/current-dependency artifact blobs are read back from GitHub;
5. every ACC-0041 clause is represented by explicit current requirements;
6. static OS-minimum support claims no longer govern current support selection;
7. parent/configuration/account/dashboard evidence cannot create `protected_verified`;
8. Private Relay/Chrome/Firefox/VPN/custom-resolver conflicts fail closed to current verification or explicit unsupported/uncertain handling;
9. accountless core plus optional-account scope is preserved without browsing/query/activity history, child accounts/profiles, persistent personal DNS allowlist or unrestricted DNS administration;
10. no pre-L8 human validation, LG-07, implementation/build/release/production/market/launch PASS is inferred;
11. full modular Master Plan validation remains PASS;
12. only after all checks pass may `CURRENT_STATE.md` receive a current TSK-0041 accepted-stable-state entry, followed by exact GitHub commit/blob read-back.

**Requalification result:** PASS candidate pending independent deterministic verification, full modular-plan validation, durable state write and GitHub read-back.