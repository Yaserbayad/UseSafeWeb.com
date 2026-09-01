# TSK-0408 — Post-CR-0007 DNS identity/platform endpoint revalidation

**Task:** TSK-0408
**Acceptance:** ACC-0408
**Verification:** VER-0408 source/contract/adversarial revalidation
**Evidence:** EVD-0408
**Date:** 2026-09-01
**Status:** PASS candidate pending independent CI verification and authoritative runtime read-back

## Purpose

Revalidate the accepted TSK-0408 DNS identity/platform mechanism contract after CR-0006/CR-0007 without rewriting unchanged technical evidence. The 2026-08-28 contract remains historical evidence for unchanged facts. Its former controlled-pilot / mandatory environment-separation lifecycle framing is superseded by DEC-0054.

## Current authority

- DEC-0053: Version 1 retains the complete accountless core and adds only an optional bounded parent account/dashboard/device-management capability; mandatory login, browsing/activity history, child accounts and unrestricted DNS administration remain outside V1.
- DEC-0054: there is no mandatory pilot or staging lifecycle/environment. The project targets one live production service after launch. Local/dev/CI, ephemeral environments, preview surfaces, mocks, synthetic data, dry-run diagnostics and bounded staging when a specific risk requires it remain valid verification mechanisms but are not customer workflow or production evidence.

## Preserved unchanged technical facts

The following accepted TSK-0408 facts remain current because neither CR-0006 nor CR-0007 changes them:

1. Human-facing service identity: `UseSafeWeb DNS`.
2. Canonical resolver hostname: `dns.usesafeweb.com`.
3. Approved DoH endpoint identity: `https://dns.usesafeweb.com/dns-query`.
4. Android native Private DNS consumes the hostname via DoT; the HTTPS URL/path is not pasted into the Android hostname field.
5. Apple/iOS DoH configuration consumes the HTTPS Server URL through the DNS Settings profile mechanism.
6. TLS identity must be valid for `dns.usesafeweb.com` on supported encrypted transports.
7. `verified` cannot be inferred from parent confirmation, profile presence, generic DNS resolution, or an unsupported/bypassed path.
8. Verification uses synthetic/controlled DNS checks and must not create or retain browsing/query history.
9. Removal/recovery returns the platform to normal DNS behavior and ends the UseSafeWeb DNS protection claim until reconfigured and reverified.
10. No platform instruction may treat hostname, HTTPS URL/path, port, profile or generic FQDN workflow as interchangeable.

## Superseded lifecycle/environment semantics

The following 2026-08-28 statements are historical only and no longer control current execution:

- `dns.usesafeweb.com` as a "controlled-pilot" endpoint;
- a mandatory pilot -> test/staging -> future-production lifecycle;
- a requirement to create environment-specific live resolver hostnames merely because a staging/pilot phase exists;
- production profile naming being blocked on a mandatory pilot/staging promotion sequence.

## Current environment/evidence contract

1. `dns.usesafeweb.com` is the sole canonical UseSafeWeb DNS production service identity. Its existence/technical acceptance does not itself authorize public launch; applicable launch/readiness gates still control activation.
2. There is no mandatory separate pilot or staging service.
3. Local/dev/CI/ephemeral/preview/mock/synthetic/dry-run verification evidence must identify itself as non-production validation evidence and must never be represented as real customer usage or production observation.
4. A staging or bounded ramp may be introduced only when a specific verified risk requires it; that does not create a permanent product identity or second customer workflow.
5. Public instructions must use only an officially published and verified service endpoint/profile value. No FQDN, path, profile identifier, callback URL or support endpoint may be invented to fill an unavailable value.
6. Optional account/dashboard/device-management work introduced by DEC-0053 does not alter the DNS transport identity above. Account/session/dashboard routes are implementation/interface work and are not invented by TSK-0408.
7. Protected AdGuard administrative/API mechanisms remain server-side/operator-only. A browser/customer path must never become an arbitrary `/control` proxy or expose an administrator secret.
8. Non-production validation cannot satisfy production-only observation criteria where a later acceptance criterion explicitly requires production evidence.

## ACC-0408 mapping

| ACC-0408 element | Current evidence/disposition |
| --- | --- |
| Sole UseSafeWeb customer DNS identity | Satisfied: `UseSafeWeb DNS` / `dns.usesafeweb.com` preserved. |
| Approved setup mechanisms | Satisfied: Android DoT hostname and Apple DoH profile/Server URL remain protocol-distinct. |
| Platform callback/support/admin boundaries | Satisfied by non-invention: only already-proven AdGuard control-plane mechanisms are retained; customer account/dashboard/API routes are not fabricated here. |
| Environment separation | Satisfied under DEC-0054: production is the sole live service identity; CI/ephemeral/preview/mock/synthetic/dry-run evidence is explicitly non-production; staging is conditional on a specific risk, not mandatory. |
| No false universal FQDN workflow | Satisfied: platform-specific input forms remain explicit and non-interchangeable. |
| Privacy/truth | Satisfied: no browsing/query history; no false protected/production/customer state inferred. |

## Adversarial checks

- **Attempt to preserve old mandatory pilot/staging model:** rejected as superseded by DEC-0054.
- **Attempt to call CI/preview evidence production evidence:** rejected.
- **Attempt to invent a new production callback/account/dashboard route:** rejected; later interface/implementation authority must publish exact values.
- **Attempt to expose AdGuard `/control` or an admin credential to customers:** rejected.
- **Attempt to use account functionality to make core DNS protection login-dependent:** rejected by DEC-0053.
- **Attempt to infer browsing/activity history from DNS verification:** rejected.

## Current external technical-source check

Checked 2026-09-01 against AdGuard Home's official configuration documentation. Current configuration still models upstream DNS, ECS, query log, statistics and anonymization as explicit configuration fields/sections, and the project may therefore build a versioned secret-free configuration baseline without changing the service-identity rules above. This source check validates technical compatibility only; it does not create owner decisions or production evidence.

Source: `https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration`

## Decision

No current acceptance-relevant contradiction remains after replacing the obsolete lifecycle/environment framing with DEC-0054. Historical technical evidence remains valid only for the unchanged facts enumerated above.

**Candidate result: TSK-0408 = PASS, subject to independent verifier success and post-write runtime read-back.**
