# TSK-0417 — Vendor removal/revocation source research and non-live source evidence — 2026-09-03

## Disposition

**SOURCE / MOCK CHECKPOINT ONLY — TSK-0417 REMAINS NON-PASS.**

No live-device, target service-revocation, profile-removal, certificate-removal, deployment, participant processing, telemetry, activation, market, launch, `TSK-0374 PASS`, `TSK-0499 PASS`, or `TSK-0417 PASS` action is authorized, performed, or inferred by this artifact.

Canonical task evidence remains `ACC-0417 / VER-0417 / EVD-0417`. Current WBS links remain `REQ-0042`, `REQ-0043`, `CON-0002`, `CON-0003`, `RSK-0004`, and `INT-0013`; this source checkpoint does not mutate planning authority.

## Canonical implementation surface

Current canonical `main` source identifies the concrete profile platform as Apple iPhone/iOS:

- `website/src/lib/ios-doh-profile.ts`, canonical `main` blob `9a342cce55a7a0c4769e61861e9d81d5837f3141`.
  - payload type `com.apple.dnsSettings.managed`;
  - DoH server URL `https://dns.usesafeweb.com/dns-query`;
  - profile identifier `com.usesafeweb.profile.doh`;
  - DNS payload identifier `com.usesafeweb.profile.doh.dns`;
  - no `PayloadCertificateUUID`, ClientID, authorization token, identity certificate, or other per-device service credential.
- `website/src/app/api/ios-doh-profile/route.ts`, canonical `main` blob `53b67ea8bbc03f29dc732591150a25ae748a7071`.
  - delivery is disabled unless explicitly enabled;
  - server-owned UUID metadata and exact SHA-256 binding are required;
  - route contains no per-device revocation handle or credential.
- `website/tests/contract/tsk0360.test.mjs` is the existing profile-generation/delivery contract suite.
- `website/src/lib/core-state-machine.ts`, canonical `main` blob `8bebd5f429cdaf03c416c9c64e93fc7ed804ee6a`, permits `recover:REMOVE_CONFIGURATION -> removed` directly before the isolated TSK-0417 branch change.
- `website/src/app/[locale]/recover/page.tsx`, canonical `main` blob `259bdc82727af6371dd260ad311361bb4e48eb5d`, exposes `REMOVE_CONFIGURATION` directly before the isolated TSK-0417 branch change.
- `website/src/content/instruction-bindings.json`, canonical `main` blob `32441b56f5b2daf2c9924584685fd35fb416438e`, states that iPhone profile removal removes profile-owned DNS configuration but does not delete a SafeWeb account/device record or anonymous web state.

The canonical implementation therefore has a concrete Apple profile-cleanup surface but **no concrete service-side revocation API, credential, ClientID, certificate identity, or target executor to call**. TSK-0417 source work must not invent such an external interface.

## Current official Apple documentation verified 2026-09-03

1. Apple Developer — DNSSettings
   https://developer.apple.com/documentation/devicemanagement/dnssettings
   - `com.apple.dnsSettings.managed` is the encrypted-DNS profile payload.
   - Apple currently documents manual install support on iOS.
   - Apple marks this payload deprecated for iOS 27+ and points to declarative `com.apple.configuration.network.dns-settings`. Deprecation is not treated here as removal of current source support.

2. Apple Developer — DNSSettings.DNSSettings
   https://developer.apple.com/documentation/devicemanagement/dnssettings/dnssettings-data.dictionary
   - `DNSProtocol` supports HTTPS/TLS.
   - `PayloadCertificateUUID` is optional and references an identity certificate when used.
   - Current SafeWeb source does not use that property; therefore the present iPhone artifact has no identity-certificate cleanup surface.

3. Apple Support — Install or remove configuration profiles on iPhone
   https://support.apple.com/guide/iphone/iph6c493b19/ios
   - Installed profiles are visible in Settings > General > VPN & Device Management.
   - Deleting a profile also deletes the settings, apps, and data associated with that profile.

4. Apple Support — Review and delete configuration profiles
   https://support.apple.com/guide/personal-safety/review-and-delete-configuration-profiles-ips327569a75/1.0/web/1.0
   - Removing an iPhone/iPad profile removes the profile's settings and information.
   - Apple directs the user to Settings > General > VPN & Device Management, select the profile, Delete Profile, and restart the device.

## Source implementation result

Isolated branch: `feature/tsk-0417-removal-ordering-20260903`.
Draft PR: `#86` — intentionally open, draft, and unmerged.
Verified final code/test head before this documentation-only publication: `27b5be186218e1cb111cf3a68305f75740a24dff`.
Canonical base remained `e05fd1d94f388d32ecae64bff74cd64791d792b9`.

The isolated branch now enforces the non-live source contract without creating a service-side revocation mechanism:

- `core-state-machine.ts` adds a `cleanup` phase and `SERVICE_REVOCATION_RESULT` event.
- direct `recover -> REMOVE_CONFIGURATION` is rejected.
- only exact qualifying evidence with `removal === 'REVOKED'` advances `recover -> cleanup`.
- only `cleanup -> REMOVE_CONFIGURATION` advances to `removed`.
- the recovery UI no longer exposes Apple/profile removal instructions or a removal control.
- removal UI lives behind a browser-session cleanup-phase gate; server/pre-hydration rendering exposes no removal instruction/action.
- direct cleanup deep links without matching accountless session state fail closed to setup.
- browser acceptance seeds `cleanup` only as an explicitly documented **mock post-revocation state**. It does not claim that service revocation occurred and creates no server-side revocation call.
- existing TSK-0358, TSK-0359, TSK-0374, TSK-0376, profile-delivery, content-delivery, accessibility, routing, and browser contracts were retained or retargeted only where their old expectation encoded the now-invalid pre-revocation removal surface.

## Test-first evidence chronology

1. **UI ordering RED** — run/job `33750299454 / 100632079598`.
   - failure was the existing recovery page exposing removal before revocation evidence.
2. **Initial source/UI GREEN** — run/job `33750457608 / 100632580996`.
   - canonical WBS hash check, repository structure, master-plan validation, and focused TSK-0417 contract passed.
3. **Inherited regression discovery** — run/job `33750460418 / 100632585323`.
   - TSK-0376's own contract passed; older TSK-0359/TSK-0374 assertions still expected removal on `recover`. Those assertions were corrected to preserve the same localization/versioned-content guarantees on `cleanup`.
4. **Direct-route disclosure RED** — run/job `33750949224 / 100634117444`.
   - proved server-rendered cleanup still disclosed removal content before browser-session phase proof.
5. **Client-gated cleanup GREEN series** on intermediate head `cf561be1e52d2cde046786a2f2cc7aa506bb5023`:
   - focused TSK-0417 `33751288584 / 100635188345` — success;
   - PR-focused TSK-0417 `33751293672 / 100635204302` — success;
   - TSK-0360 profile delivery `33751293901 / 100635205417` — success;
   - TSK-0376 state machine `33751293877 / 100635205272` — success;
   - TSK-0374 versioned content `33751293677 / 100635204011` — success;
   - TSK-0243 source/build boundary `33751293813 / 100635205200` — source/build checks passed.
6. **Inherited browser regression discovery** — job `100635204475` on the intermediate head.
   - 98 source contracts, lint, typecheck, production build, and audits passed;
   - browser failure was an obsolete assertion that removal instructions remained on `/recover`.
7. **First browser retarget** — code head `0a47fb95c33cdc0aa8bd05c349aa73800e4fee3d`.
   - new TSK-0359 browser acceptance passed, but inherited TSK-0358 browser acceptance still waited for `[data-core-remove]` on `/recover`; run/job `33751603680 / 100636187551` correctly failed that inherited stale expectation.
8. **Final inherited-browser correction** — code/test head `27b5be186218e1cb111cf3a68305f75740a24dff`.
   - `recover` is explicitly proven to expose no removal control;
   - the browser then seeds only a non-live post-revocation `cleanup` state, proves the removal instruction/control appears there, performs only the local state transition to `removed`, and asserts no persistent/unapproved server mutation.
   - decisive TSK-0359 + inherited TSK-0358 browser acceptance: run/job `33751884196 / 100637066363` — **SUCCESS**.
   - focused TSK-0417 source gate: `33751884329 / 100637066087` — **SUCCESS**.
   - TSK-0360 profile-delivery gate: `33751884262 / 100637066025` — **SUCCESS**.
   - TSK-0376 state-machine gate: `33751884214 / 100637065684` — **SUCCESS**.
   - TSK-0374 versioned-content gate: `33751884290 / 100637065924` — terminal clean on the exact head.
   - TSK-0375 intake/routing gate: `33751884246 / 100637065869` — terminal clean on the exact head.
   - TSK-0629 browser/accessibility gate: `33751884203 / 100637065459` — terminal clean on the exact head.
   - TSK-0243 browser/orchestration gate: `33751884175 / 100637065419` — terminal clean on the exact head.
   - TSK-0369 gate: `33751884198 / 100637065294` — terminal clean on the exact head.
   - TSK-0499 regression gate: `33751884316 / 100637066006` — terminal clean on the exact head; this is regression evidence only and does not create or reassert a new TSK-0499 PASS.
   - exact-head reconciliation returned 11 check runs, with no failure, queued, or in-progress result.

## Acceptance boundary and remaining work

This evidence proves only a **source/mock ordering checkpoint**:

`service revocation evidence required -> cleanup eligible -> profile cleanup eligible`.

It does **not** prove service revocation happened on a real target, that a real service-side association/credential was removed, that Apple profile removal occurred on a device, or that no residual target access/artifact exists afterward.

`ACC-0417 / VER-0417 / EVD-0417` therefore remain incomplete. TSK-0417 must remain `WAITING`/non-PASS until a concrete current target service-removal/revocation executor exists and actual-target evidence independently proves, in order:

1. service association/access is removed or revoked;
2. profile/certificate cleanup follows;
3. configuration diff/target observation confirms cleanup;
4. negative verification proves no residual access, stale dependency, credential/association, active profile, or active certificate remains.

## Fences preserved

- no service-side revocation API/interface was invented;
- no live service revocation was executed;
- no live device/profile/certificate removal was executed;
- no deployment or activation was executed;
- no participant or telemetry action was executed;
- no launch/market action was executed;
- no TSK-0374 PASS, TSK-0499 PASS, or TSK-0417 PASS was created;
- draft PR `#86` is the isolated source checkpoint and is not authority until a separately authorized, verified canonical publication occurs.
