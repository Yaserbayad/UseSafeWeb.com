# TSK-0412 — AdGuard Home Compatibility Reverification

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Task:** TSK-0412  
**Acceptance:** ACC-0412 / VER-0412 / EVD-0412  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Authority:** DEC-0054 / CR-0007 + DEC-0055 / CR-0008; A4 / AUTO_ALLOWED  
**Status represented:** PASS CANDIDATE pending independent automated verification and canonical read-back. This artifact changes no production server and infers no later task/gate PASS.

## 1. Decision

Keep **AdGuard Home v0.107.79** as the pinned UseSafeWeb DNS backend target. As of 2026-09-01, official AdGuard Home release authority still identifies v0.107.79 as the latest stable release, so there is no verified reason to reopen the frozen backend decision or change the current recovery bundle.

UseSafeWeb continues to integrate AdGuard Home as a **separate server process** with:

- versioned non-secret configuration owned by the recovery/configuration boundary;
- a private/restricted administrative control plane;
- a narrow server-side typed API adapter for the small subset of client/configuration operations required by the product;
- a separate encrypted DNS data plane used directly by managed devices;
- no Firebase/auth dependency inside AdGuard Home itself.

The optional parent-authentication capability remains an application concern. AdGuard Home must be operable, recoverable and verifiable without Firebase, Google sign-in or the application datastore.

## 2. Exact pinned build and current stable release

Official AdGuard Home release/tag evidence checked on 2026-09-01:

| Item | Current verified value |
|---|---|
| Latest stable release | `v0.107.79` |
| Release publication | `2026-08-18T15:45:27Z` |
| Exact annotated tag target commit | `05ba17b282da1c4393d6a4ba4db0cf519194a362` |
| Linux amd64 release asset | `AdGuardHome_linux_amd64.tar.gz` |
| Linux amd64 SHA-256 | `c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f` |
| Current recovery bundle config schema | `34` |

The existing project installer and TSK-0413 compatibility bundle already pin the same release, commit and schema. Therefore the current result is **no version drift / no upgrade required**.

A future AdGuard Home release does not automatically become the UseSafeWeb production target. Any version or schema change reopens this compatibility boundary before rollout.

## 3. Official source boundaries

Current verification uses the upstream AdGuard Home repository and exact v0.107.79 release/tag artifacts as source authority:

- releases: `https://github.com/AdguardTeam/AdGuardHome/releases`
- exact tag/API source: `https://github.com/AdguardTeam/AdGuardHome/tree/v0.107.79`
- exact OpenAPI contract: `https://github.com/AdguardTeam/AdGuardHome/blob/v0.107.79/openapi/openapi.yaml`
- exact GPL-3.0 license text: `https://github.com/AdguardTeam/AdGuardHome/blob/v0.107.79/LICENSE.txt`

The acceptance workflow independently re-fetches these exact official sources and downloads the release binary rather than trusting this prose.

## 4. API integration contract

The exact v0.107.79 OpenAPI contract uses base path `/control` with HTTP Basic authentication for the administrative API. UseSafeWeb therefore keeps the administrative API **server-side only** and never exposes an unrestricted browser proxy.

### 4.1 Narrow typed client lifecycle

The future application adapter may implement only explicitly approved, typed operations backed by documented endpoints. The current exact API includes:

- `POST /clients/add` — operation `clientsAdd`;
- `POST /clients/update` — operation `clientsUpdate`;
- `POST /clients/delete` — operation `clientsDelete`.

No raw customer-facing `/control/*` passthrough is permitted. The UseSafeWeb server validates authorization/ownership before any account-owned device operation; an AdGuard ClientID or device identifier is not authorization.

### 4.2 Per-client privacy fields

The exact client schema exposes `ignore_querylog` and `ignore_statistics`. These controls are material for UseSafeWeb privacy and must be **set and verified explicitly** by future provisioning/reconciliation code where a managed client exists. New client creation must not rely on upstream defaults to establish UseSafeWeb privacy policy.

The product does not use AdGuard query history or identifiable per-client statistics as a dashboard feature, analytics feature or protection-verification source.

### 4.3 Configuration API deprecation rule

The exact API exposes the current configuration update operations including:

- `PUT /querylog/config/update`;
- `PUT /stats/config/update`.

Older query-log/statistics configuration operations marked `deprecated: true` in the exact upstream OpenAPI contract are forbidden for new UseSafeWeb integration code. A later AdGuard release requires another exact API compatibility check before the adapter is changed.

## 5. Required current privacy configuration

The TSK-0413 bundle remains the current non-secret desired-state source for recovery and compatibility verification. Its verifier enforces:

- admin UI/API bind: `127.0.0.1:3000`, authenticated and not publicly exposed;
- DNS bind: loopback behind the approved encrypted-DNS proxy/service topology;
- upstream: exactly `https://dns10.quad9.net/dns-query`;
- fallback/private upstream: empty unless later authority explicitly changes them;
- EDNS Client Subnet: disabled;
- client-IP anonymization: enabled;
- persistent query log: disabled;
- file query log: disabled;
- identifiable per-client history/statistics: excluded by product policy and explicit client controls;
- operational statistics: enabled only as minimum anonymized aggregate statistics with `1d` retention;
- approved baseline filter: AdGuard DNS filter;
- initial allowlist and custom user rules: empty;
- AdGuard-native public TLS: disabled in the current topology because the separate approved proxy/service boundary owns public encrypted DNS/TLS;
- DHCP: disabled;
- no versioned administrator credential, private key, token, client identifier or query history.

This current `1d` anonymized aggregate-statistics baseline supersedes older helper-script assumptions that asserted statistics must be globally disabled.

## 6. Compatibility test contract

A compatible target is not proven by a version string alone. Before a release can be accepted for UseSafeWeb, the verifier must establish all applicable items below against the exact build and exact project bundle:

1. official latest-release/tag identity and exact release commit are known;
2. downloaded Linux amd64 asset SHA-256 matches the pinned value;
3. exact binary reports the expected `v0.107.79` version;
4. project `install-adguard.sh` pins the same version and SHA-256;
5. TSK-0413 `verify_bundle.py` passes and covers every file in the versioned bundle;
6. bundle compatibility is exactly v0.107.79 / schema 34 / commit `05ba17...`;
7. exact OpenAPI still exposes the required documented API surface and privacy-relevant fields;
8. current query-log/statistics configuration endpoints are available and deprecated endpoints are not selected for new code;
9. bundle privacy/upstream/filter/admin/TLS/DHCP assertions remain exact;
10. no auth/Firebase dependency is introduced into the DNS-service/recovery contract.

Target-environment behavior remains a separate later verification boundary; TSK-0412 does not substitute documentation checks for live DNS/TLS/privacy/recovery acceptance.

## 7. Upgrade policy

**No automatic AdGuard Home upgrades.**

When a later stable release is considered:

1. fetch the current official release/tag/commit and binary digest;
2. read the exact version-matched OpenAPI/configuration/migration/release notes;
3. compare required client/configuration/privacy fields and defaults;
4. inspect schema/config migration behavior and deprecated/removed API paths;
5. re-run the versioned bundle compatibility tests against a deliberately updated candidate bundle;
6. run non-production/static/synthetic tests required by the active lifecycle without introducing a separate mandatory staging lifecycle;
7. prove upgrade and rollback/recovery behavior under the current recovery acceptance plan;
8. update the production pin only after every current acceptance requirement passes.

A newer version number alone is never evidence that upgrade is safer or required.

## 8. Rollback and recovery constraints

The known-good rollback reference for the current baseline is the exact v0.107.79 release binary/digest plus a **current-compatible** desired-state/recovery bundle.

Rollback rules:

- retain exact release identity and SHA-256 so the known-good binary can be reacquired and verified;
- do not blindly restore an old raw AdGuard configuration when its schema/defaults/privacy semantics may differ;
- do not blindly downgrade a configuration written by a newer schema into an older binary;
- prefer deterministic rebuild/reconciliation from the known-good binary plus a bundle explicitly verified compatible with that binary/schema;
- when an upgrade has ambiguous partial effects, inspect the durable target before retry/rollback; do not assume a failed command means no mutation occurred;
- verify privacy, upstream, filter, admin exposure, DNS/TLS health and prohibited-history conditions after rollback/rebuild before declaring recovery successful.

This is consistent with TSK-0445/TSK-0446: exact target behavior and RTO are proven later on the target, not inferred here.

## 9. License boundary and specialist trigger

The exact v0.107.79 repository license is **GNU GPL Version 3**.

For current architecture, AdGuard Home remains a separate process/service and UseSafeWeb communicates with it over documented configuration/API/network boundaries. This task does not make a legal-compliance conclusion beyond identifying the upstream license and the product architecture.

Trigger specialist legal review before any materially different distribution model, especially if UseSafeWeb proposes to:

- modify AdGuard Home source/binaries and distribute/convey the modified covered work;
- bundle/convey AdGuard Home binaries or source to customers/partners as part of a distributed product;
- impose downstream terms or packaging that could conflict with GPL obligations;
- change from the current separately operated server-service model in a way that materially changes distribution/conveyance obligations.

Ordinary network interaction with an independently running server is not itself treated here as proof of a distribution obligation, but final licensing treatment remains subject to actual deployment/distribution facts and legal review when a trigger occurs.

## 10. No Firebase/auth dependency

AdGuard Home configuration, installation, recovery, DNS resolution, filtering, privacy controls and the future typed administrative adapter have **no Firebase or Google-auth runtime dependency**.

The optional parent account lives in the Next.js application boundary. If Firebase/auth is unavailable, persistent account/dashboard operations may degrade, but AdGuard Home continues to serve the DNS baseline and the accountless core must remain available wherever its own dependencies are healthy.

No AdGuard client identity may be treated as application authentication or parent authorization.

## 11. ACC-0412 mapping

| ACC-0412 requirement | Evidence in this artifact / independent verifier | Result |
|---|---|---|
| current official sources | Latest upstream release, exact tag/commit, exact v0.107.79 OpenAPI and exact GPL-3.0 license are independently fetched | PASS CANDIDATE |
| pinned target build | v0.107.79 Linux amd64 exact SHA-256 and binary version check | PASS CANDIDATE |
| separate-process/config/API integration | Sections 1, 4 and 10 preserve independent AdGuard service and server-only typed API/config boundary | PASS CANDIDATE |
| required privacy fields | Sections 4–6 plus TSK-0413 verifier cover client querylog/statistics controls, anonymization, ECS, logs and aggregate statistics | PASS CANDIDATE |
| compatibility tests | Section 6 defines exact release/binary/project-bundle/API checks and the acceptance workflow executes them | PASS CANDIDATE |
| upgrade/rollback path | Sections 7–8 require explicit version/schema re-verification and known-good deterministic rebuild/reconciliation | PASS CANDIDATE |
| specialist-license triggers | Section 9 binds GPL-3.0 and identifies distribution/modification/conveyance changes that trigger specialist review | PASS CANDIDATE |
| no Firebase/auth dependency | Sections 1 and 10 keep DNS service/recovery independent from optional application authentication | PASS CANDIDATE |

## 12. Non-inference

TSK-0412 does **not** prove or authorize:

- a production AdGuard upgrade or downgrade;
- production configuration mutation;
- implementation of the future typed adapter;
- live target DNS/TLS/privacy/recovery behavior;
- clean-server recovery or the TSK-0446 RTO;
- closure of any later security/privacy/recovery risk;
- LG-07, LG-08, LG-09, production activation or public launch PASS;
- final legal advice or a licensing conclusion for a future materially different distribution model.

**Result:** PASS CANDIDATE pending the independent current-source/build/bundle verification workflow and canonical remote read-back.