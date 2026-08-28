# TSK-0041 — Baseline DNS-Protection Activation Requirements

**Task:** TSK-0041 — Specify baseline DNS-protection activation requirements  
**Acceptance:** ACC-0041  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 DNS-ACTIVATION REQUIREMENTS / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0143 current phone-family routing + TSK-0408 DNS identity/platform contract + TSK-0409 support matrix + TSK-0406/0512 filtering evidence + TSK-0511/0514 install/removal evidence + TSK-0207 privacy persistence evidence + TSK-0320 truth-state contract + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

These requirements freeze the strongest technically supported activation behavior available from current direct UseSafeWeb evidence. They are **not** representative-parent usability/comprehension evidence and do not prove that setup is easy, that parents understand DNS limitations, or that the protection creates sufficient incremental value. `RSK-0002` remains OPEN.

This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real participants, legal completion, payment, public release or launch.

## 1. Activation objective

The DNS activation layer has one bounded purpose:

> Configure one currently supported phone to use the approved UseSafeWeb encrypted-DNS mechanism, establish through current controlled verification whether the intended UseSafeWeb filtering path is active, state uncertainty/unsupported conditions truthfully, and preserve a safe removal/recovery path without collecting browsing history.

DNS activation is a **domain-resolution safety layer**, not a complete-safety, app-control, monitoring or surveillance system.

## 2. Canonical DNS identity and endpoint format

One public service identity is frozen:

- Resolver hostname: `dns.usesafeweb.com`
- Apple DoH Server URL: `https://dns.usesafeweb.com/dns-query`
- Android native Private DNS transport: DoT to `dns.usesafeweb.com:853`

Requirements:

1. Never present `dns.usesafeweb.com` as a universal input format across platforms.
2. Android native Private DNS receives **hostname only**: `dns.usesafeweb.com`.
3. Apple DNS Settings profile receives the full HTTPS DoH Server URL: `https://dns.usesafeweb.com/dns-query`.
4. Do not ask a parent to choose DoH versus DoT when the platform route already determines the approved mechanism.
5. Do not expose AdGuard administration credentials, internal control URLs, server secrets or private infrastructure details in user-facing configuration.
6. A future endpoint/transport change requires its owning network/security change control and regression evidence; it is not an editorial copy change.

The legacy ACC phrase “DoH setup” is satisfied by the Apple DoH path and the overall encrypted-DNS activation requirements; it must **not** be interpreted as forcing Android away from the already accepted native DoT mechanism.

## 3. Supported activation combinations

Only combinations accepted by TSK-0409 may enter the normal activation path.

### Android phone

Current family baseline:

- Android 9+ phone;
- native `Private DNS provider hostname` capability present and usable;
- approved input `dns.usesafeweb.com`;
- intended encrypted transport DoT/853;
- current verifier must succeed before S1 `Verified` is allowed.

Android below 9, Android-derived untested device families, devices lacking usable Private DNS, managed/policy-blocked variants and unresolved transport/network conflicts are not silently routed through an alternative app/VPN workflow.

### iPhone

Current family baseline:

- iPhone/iOS 14+;
- approved manually installed Apple DNS Settings profile;
- profile uses DoH Server URL `https://dns.usesafeweb.com/dns-query`;
- current verifier must succeed before S1 `Verified` is allowed.

Other untested Apple device families and managed/supervised variants remain outside the current support claim unless separately accepted.

## 4. Activation state machine

Use the TSK-0320 truth states.

| Activation condition | Required state | Rule |
| --- | --- | --- |
| Supported route not yet configured | S3 `Action needed` | Show only the exact platform-specific next action. |
| Configuration/profile entered or installed but verifier has not succeeded | configured-unverified internal state or S2 only where parent confirmation is useful | Presence alone never yields S1. |
| Current approved verifier succeeds for exact supported tuple and no known conflict exists | S1 `Verified` | Claim only the bounded DNS mechanism/filtering state actually verified. |
| Supported path fails with a known repair | S3 `Action needed` | Provide exact repair/recheck; do not relabel unsupported. |
| Resolver path is conflicting/inconclusive | S5 `Status uncertain` | Do not preserve stale green state. |
| Current platform/network path is explicitly unsupported/not-yet-supported | S4 `Not covered` | Do not invent a fallback implementation. |
| UseSafeWeb DNS is removed/reset | S6 `Removed` | Withdraw UseSafeWeb DNS protection claim; confirm recovery separately. |

A finished journey may legitimately end with S3/S4/S5 if the truth is incomplete or unsupported.

## 5. Verification requirements

Activation is not complete merely because a setting/profile exists.

The approved implementation must provide a current controlled verification action that establishes, at minimum, whether the intended UseSafeWeb resolver/filtering path is functioning for the current supported tuple without depending on real browsing history.

### Required verification properties

1. Use controlled/synthetic DNS checks, not parent browsing history.
2. Verify the intended UseSafeWeb encrypted path, not merely that “DNS works.”
3. Include a known allowed-path check.
4. Include a controlled known blocked/filtering check where safe and technically appropriate.
5. Return one of verified / action-needed / uncertain / not-covered rather than forcing binary success.
6. Do not persist the tested domain/request as identifiable user history.
7. Re-run/re-evaluate after material network/resolver/profile/provider changes.
8. A previous S1 may not survive a current contradictory result.
9. Verification failure must not silently fall back to plain public DNS while retaining a UseSafeWeb protection claim.

Current direct project evidence already proves synthetic allowed/blocked/exception/rollback behavior on the live AdGuard baseline and proves the supported phone-family encrypted paths. The product activation verifier may reuse those **semantics**, but implementation still requires its own exact app/user-flow test before release.

## 6. Filtering baseline requirement

The active DNS protection claim is tied to the frozen conservative AdGuard filtering baseline, not to encrypted transport alone.

Current verified baseline:

- AdGuard filtering/protection enabled;
- exactly the approved AdGuard DNS filter active in the baseline evidence;
- narrow explicit exception mechanism available;
- no blanket “disable filtering” workaround for one false positive;
- Quad9 `dns10` upstream/ECS-off remains a separate frozen backend invariant;
- no complete-safety claim.

User-facing activation must therefore distinguish:

- **encrypted DNS transport reachable** from
- **UseSafeWeb filtering path verified**.

A transport-only result is insufficient for S1 if the activation acceptance is meant to assert working UseSafeWeb protection.

## 7. Fail-safe behavior

There is **no hidden fail-open/fail-closed promise** beyond what the exact platform actually does and current tests establish.

UseSafeWeb product requirements are:

1. If the approved encrypted endpoint cannot be reached/authenticated, do not call the device protected.
2. If the effective resolver path cannot be determined because of VPN, Private Relay, browser/app custom DNS, network policy or another conflict, use S5.
3. Do not silently instruct the device to use unencrypted/plain DNS as a UseSafeWeb fallback while retaining protection status.
4. If safe supported continuation is unavailable, offer removal/recovery to normal device DNS behavior and mark S6/S4/S5 as appropriate.
5. Do not tell a parent to weaken an unrelated employer/school/security/privacy control merely to obtain S1.
6. If the service itself is unhealthy, surface Action needed/uncertain and separate service outage from local setup failure where possible.
7. Retry only after a changed condition/new evidence; do not loop equivalent failed checks.

## 8. Private Relay, VPN, browser/app and network conflicts

TSK-0409 is authoritative for the current support matrix. TSK-0041 consumes it as an activation requirement.

### iCloud Private Relay

Current project evidence does not prove coexistence with the UseSafeWeb DNS profile. Apple confirms Private Relay includes DNS name-resolution handling. Therefore:

- active Private Relay with unresolved coexistence → S5;
- profile presence cannot override that uncertainty;
- do not claim definite compatibility or definite incompatibility without direct exact-version evidence;
- do not make disabling the privacy feature a default requirement.

### VPN

Android and Apple VPN APIs can control tunnel DNS. Therefore:

- generic VPN coexistence is not presumed supported;
- exact VPN configuration must be directly tested before S1 can extend to tunneled traffic;
- if DNS path is overridden/uncertain, use S5/S4 as the exact matrix dictates;
- managed/required VPNs are not bypassed to make UseSafeWeb appear successful.

### Browser/app custom DNS

A browser/app using its own secure resolver can bypass or alter the system DNS path.

- system DNS S1 must not be advertised as proof that every browser/app request is filtered;
- known custom resolver conflict is S5/not-covered for that traffic;
- no universal bypass detector is invented.

### Network limitations

- Android DoT requires the intended TCP 853 path to work; ordinary internet access does not prove this.
- Apple DoH requires the intended HTTPS endpoint path to work.
- captive portal, enterprise-managed, transport-blocked and IPv6-only/NAT64-only combinations remain unsupported/not-yet-supported where TSK-0409 says so.

## 9. False-positive requirements

A legitimate required site/service may be blocked by the baseline. The activation/support model must handle this without turning one issue into broad filtering disablement or browsing-history collection.

### Required workflow

1. Parent reports a specific symptom/required service through the approved help path.
2. Confirm the issue is within current product/support scope.
3. Reproduce with synthetic/non-participant evidence where possible.
4. Determine whether UseSafeWeb filtering is actually responsible rather than the site/app, upstream, device, network or other policy.
5. If a correction is justified, use the **narrowest safe explicit exception**.
6. Re-test the legitimate path and a relevant blocked regression so the correction does not silently remove baseline filtering.
7. Keep the change reversible and recorded in the owning configuration/change process.
8. Update the user-visible state truthfully; unresolved impact is S3/S5/S4, not S1 by convenience.

### Active accountless limitation

The current accountless baseline has no per-parent/per-device personalized allowlist/dashboard control plane. TSK-0041 therefore does **not** create a user-facing persistent personal exception feature. The accepted project evidence proves a narrow global technical exception mechanism; any future per-device exception model requires its own product/privacy/architecture authority.

Historical Experiment-1 false-positive guidance may be reused for its privacy-safe diagnostic/narrow-exception principles only. Real-participant intake/metrics remain deferred under CR-0003 and are not activated by this L4 requirement.

## 10. Removal and uninstall requirements

Removal is a first-class supported safety/recovery outcome.

### Android

1. Leave the custom `Private DNS provider hostname` configuration for UseSafeWeb.
2. Restore normal platform DNS policy, normally `Automatic` unless the parent independently chooses another setting.
3. Confirm ordinary DNS/internet recovery with neutral/synthetic checks.
4. Set UseSafeWeb DNS state S6 `Removed`.
5. Do not retain a protection claim after removal.

### iPhone

1. Identify the exact UseSafeWeb DNS profile.
2. Remove it through the current Apple profile-management path.
3. Confirm ordinary DNS/internet recovery with neutral/synthetic checks.
4. Set S6 `Removed`.
5. Do not infer that unrelated network problems after removal were caused by UseSafeWeb without evidence.

Direct project evidence already proves external-network removal/recovery for the accepted phone families. Release implementation must preserve this reversibility.

## 11. No-history privacy constraints

DNS activation/verification must not require persistent identifiable browsing/query history.

Mandatory baseline:

- persistent AdGuard query logging off;
- file query logging off;
- identifiable per-client statistics off;
- client-IP anonymisation remains enabled under the current backend baseline;
- no persistent child/family/device identity is created merely to activate/verify DNS;
- no browsing/domain history is copied into product/support/content analytics;
- no real-user domain list is required for routine verification;
- synthetic/reserved/neutral test inputs are preferred;
- exceptional request-level diagnostics, if ever genuinely necessary under later authority, must use the separately governed exceptional diagnostic process and deletion controls.

Current production persistence testing directly proves no persistent raw query/domain history, no identifiable client/statistics history and no unapproved raw backup copy in controlled project locations.

## 12. Endpoint/configuration error handling

The activation surface must classify errors instead of collapsing them into “setup failed.”

Minimum classes:

- invalid platform input format;
- endpoint unreachable;
- TLS/certificate/authentication failure;
- filtering verification failed;
- effective resolver path uncertain;
- VPN/Private Relay/browser/app conflict;
- unsupported/managed device/network;
- stale profile/instruction;
- service outage;
- removal/recovery failed;
- suspected false positive.

Each class must map to one truthful TSK-0320 state plus one next action or explicit unsupported result. Error telemetry/logging must stay inside the privacy boundary.

## 13. Reverification and staleness triggers

Reverification/review is required after material changes to:

- network context where TSK-0409 says behavior can differ;
- VPN/Private Relay/browser/app resolver state;
- DNS profile/provider configuration;
- supported OS/device family/version;
- resolver hostname/DoH URL/transport/port;
- TLS certificate/service topology;
- filtering baseline or exception rules;
- current verification method;
- source/vendor guidance;
- direct target evidence contradicting a current support claim.

No universal “verified for N hours” TTL is fabricated. Verification is a current-check claim in the accountless baseline.

## 14. Testable acceptance assertions

A later implementation/prototype/QA suite must prove:

1. Android receives only `dns.usesafeweb.com` as native Private DNS hostname.
2. Apple DoH profile uses `https://dns.usesafeweb.com/dns-query`.
3. User never chooses protocol when platform routing determines it.
4. Configuration/profile presence alone never yields S1.
5. Current approved verification is required for S1.
6. Verification includes controlled allowed and filtering evidence without browsing-history dependence.
7. Transport reachability alone cannot masquerade as working filtering if filtering is unproven.
8. Endpoint/verification failure never silently preserves a positive protection claim.
9. Private Relay uncertainty yields S5 until exact coexistence is proven.
10. Generic VPN coexistence is not treated as supported without exact evidence.
11. Browser/app custom DNS is not covered by a universal system-DNS protection claim.
12. Unsupported network/device states stop optimistic progression.
13. False positives use a narrow reproducible/reversible correction, never blanket filtering disablement.
14. No per-device persistent allowlist feature is invented in the current accountless baseline.
15. Android removal restores normal DNS policy and yields S6.
16. iPhone profile removal restores normal DNS behavior and yields S6.
17. Persistent query/file logs and identifiable statistics remain off.
18. Routine activation/verification stores no browsing/domain history or persistent child/device identity.
19. Material environment/configuration change triggers re-verification rather than stale S1.
20. No state/copy promises complete safety or universal app/network coverage.

## 15. Current project evidence index

- `TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md` — DNS identity/platform semantics.
- `TSK_0409_SUPPORTED_OS_DEVICE_NETWORK_LIMIT_MATRIX_2026-08-28.md` — current support/conflict matrix.
- `TSK_0511_SUPPORTED_DEVICE_VERIFICATION_COMPLETION_EVIDENCE_2026-08-28.md` — accepted Android/iPhone encrypted-DNS device evidence.
- `TSK_0514_EXTERNAL_ENDPOINT_COMPLETION_EVIDENCE_2026-08-28.md` — external cellular and removal/recovery evidence.
- `TSK_0406_FILTERING_POLICY_EVIDENCE_2026-08-27.md` — conservative filter policy and narrow exception mechanism.
- `TSK_0512_FILTER_REGRESSION_EVIDENCE_2026-08-28.md` — blocked/allowed/exception/rollback direct target verification.
- `TSK_0207_PRIVACY_PERSISTENCE_EVIDENCE_2026-08-28.md` — no persistent query/client-history evidence.
- `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md` — privacy-safe false-positive workflow principles only; participant branch remains deferred.
- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` — user-visible evidence-state truth rules.

## 16. ACC-0041 result

ACC-0041 requires endpoint format, DoH setup, filtering verification, fail-safe behavior, uninstall/removal, Private Relay/VPN conflicts, false positives, and no-history constraints.

This contract defines every required area while reconciling the legacy DoH wording to the current platform-specific contract: Apple uses DoH, Android native Private DNS uses the accepted DoT hostname mechanism. It consumes direct current filtering, device, removal and privacy evidence without expanding support or inventing user history/identity requirements.

**TSK-0041 result: PASS candidate subject to independent verification and runtime read-back.**
