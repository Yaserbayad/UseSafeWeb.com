# TSK-0517 — Integrated Cross-Browser / Device / Network Acceptance Test Plan

**Task:** TSK-0517 — Define cross-browser/device/network functional, failure, privacy, accessibility, performance, recovery/removal, and no-auth tests  
**Acceptance:** ACC-0517 / VER-0517 / EVD-0517  
**Lifecycle:** L5 — Architecture, Security, Privacy & Operations  
**Version:** 1.0.0  
**Date:** 2026-09-01  
**Authority:** A3 / AUTO_ALLOWED under the current CR-0008 owner-frozen modular Master Planning System  
**Hard dependencies:** current `TSK-0354` PASS + current `TSK-0409` PASS  
**Controls:** REQ-0065; REQ-0066; CON-0023; CON-0029; RSK-0050; INT-0017  
**Status:** current acceptance-test-definition candidate; no downstream test execution, target-runtime PASS, build, release or production outcome is inferred.

## 1. Release acceptance rule

A release is test-eligible only when its exact source commit/build, runtime configuration, dependency lock state, environment, browser/device/OS versions, DNS/profile/config versions, verifier version and applicable feature flags are recorded. A passing result belongs only to that exact test subject. Artifact existence, local behavior, a prior release, a producer's own assertion, a parent/configuration confirmation or an unversioned `latest` environment never proves release acceptance.

Before release-to-operations, every applicable critical requirement and every applicable state transition must have an explicit test ID, expected result, evidence locator, severity/blocking rule and exact tested environment. Missing or stale evidence is a failed acceptance precondition, not an inferred PASS.

`INT-0017` handoff is not satisfied until operations can identify the exact running version and the accepted evidence includes monitoring, recovery, maintenance, alert/runbook and rollback expectations.

## 2. Frozen dated environment/version matrix

The following is the **2026-09-01 reference matrix** for this test definition. Later execution may move to a newer supported security release only by recording the exact replacement version and re-running every affected test; no floating `latest` label is accepted as evidence.

| Env ID | Surface | Exact dated reference | Required evidence at execution | Role |
|---|---|---|---|---|
| ENV-CI-01 | deterministic CI / synthetic web | GitHub-hosted `ubuntu-24.04`; runner image family observed in current project evidence as Ubuntu 24.04.4 / image `20260823.283.1` | runner image/version, source SHA, dependency lock hash, browser engine/build, command, result | non-production evidence only |
| ENV-CHR-01 | Chromium/Chrome-compatible desktop web | Chromium branch build `153.0.8010.24` dated 2026-08-31; Chrome 153 stable release line current on 2026-09-01 | exact installed browser full version + OS build + source/release SHA | browser functional/accessibility/privacy |
| ENV-FF-01 | Firefox desktop web | Firefox `155`, released 2026-09-01 | exact Firefox full version + OS build + source/release SHA | browser functional/accessibility/privacy + DoH cases |
| ENV-IOS-01 | iPhone core journey + DNS | iOS `26.6.1`, current Apple production release on 2026-09-01; supported iPhone 11 or later | device model, exact iOS build/version, Safari/system browser version where exposed, profile version, network class | primary Apple phone path |
| ENV-IPAD-01 | iPad responsive + DNS | iPadOS `26.6.1`, current Apple production release on 2026-09-01; supported iPad generation from current Apple list | device model, exact iPadOS build/version, browser/profile version, network class | Apple tablet/responsive path |
| ENV-SAFARI-01 | Safari desktop compatibility | Safari `26.6.1` on a currently supported macOS host; Safari 26.6.1 released 2026-08-18 | exact Safari + macOS versions + source/release SHA | desktop WebKit compatibility |
| ENV-AND-01 | Android core journey + DNS | Android `16` stable platform; Android 17 remains beta as of the dated source review | device/emulator model, API/OS build, exact Chrome/browser version, Private DNS config version, network class | primary Android path |
| ENV-IOS-CHR-01 | alternate iOS browser surface | Chrome Stable for iOS `153.0.8010.24`, released 2026-09-01, on iOS `26.6.1` | exact app + OS version and source/release SHA | alternate browser surface on Apple WebKit platform |

**Official dated source basis:** Apple Security Releases (iOS/iPadOS 26.6.1 and Safari 26.6.1); Mozilla Firefox 155 enterprise release notes; Chrome Releases / Chromium tag 153.0.8010.24; Android Developers latest platform page identifying Android 16 stable and Android 17 beta. These sources establish the dated test references only; they do not prove UseSafeWeb runtime behavior.

## 3. Evidence classes and non-production boundary

- `E-CI`: CI/browser automation evidence. Never labelled production/live-user evidence.
- `E-DEVICE`: physical-device or approved emulator evidence with exact device/OS/browser/config versions. Emulator evidence cannot replace a physical-device criterion when the criterion depends on real OS/network/profile behavior.
- `E-NET`: network/DNS verification evidence with exact network class, verifier/version and bounded result; never DNS-question/domain history.
- `E-SEC`: security/privacy negative-test evidence, including secret/API/admin exposure and prohibited data checks.
- `E-A11Y`: automated accessibility evidence plus required manual/assistive-technology checks where automation cannot prove the criterion.
- `E-PERF`: reproducible performance measurements with environment, release and threshold.
- `E-REC`: failure/recovery/removal/rollback evidence with before/failure/action/after state.
- `E-OPS`: operational handoff/rehearsal evidence required by INT-0017.

`CON-0023` is absolute: local, CI, mock, synthetic, preview, dry-run or other non-production evidence remains non-production evidence. `CON-0029` is absolute: autonomy/speed never substitutes for fresh independent acceptance and rollback proof.

## 4. Test-suite catalogue

| Suite | Coverage | Minimum evidence | Release blocker |
|---|---|---|---|
| TS-GOV | exact release/config/environment identity; requirement-to-test completeness; evidence freshness; no stale PASS reuse | E-CI + trace report | any critical requirement unmapped/stale |
| TS-NOAUTH | complete accountless start -> Phone -> Internet -> Services -> truthful Protection Map without login; refresh/resume/expiry/clear/back; public-to-setup handoff | E-CI + E-DEVICE | login required for core value or critical journey failure |
| TS-ACCOUNT | optional Google/Firebase account/session/dashboard boundaries without changing accountless core; ownership isolation; session expiry/revocation; account/device deletion/recovery | E-CI + E-SEC + target evidence when implemented | cross-parent access, mandatory-login regression, deletion/recovery defect |
| TS-DNS | TSK-0409 mechanisms, conflicts, bypasses, verification freshness, removal and unsupported states | E-DEVICE + E-NET | false `protected_verified`, unsupported path called protected, removal/recovery failure |
| TS-STATE | all six TSK-0320 states and every permitted evidence-driven transition/precedence/freshness rule | E-CI + E-DEVICE/E-NET where technical | confirmation/configuration masquerades as technical verification; impossible/untruthful state |
| TS-UX | critical route copy, errors, recovery, unsupported/limits, responsive behavior, interruption/resume, no deceptive complete-safety claim | E-CI + E-DEVICE | critical comprehension/truth/navigation defect |
| TS-A11Y | keyboard/focus, semantic structure, labels/names, contrast, zoom/reflow, reduced motion, screen-reader critical paths, error identification/status, touch target behavior | E-A11Y + E-DEVICE | applicable critical WCAG/interaction blocker |
| TS-PRIV | no domains/DNS questions/URLs/browsing/child activity/persistent analytics identity; accountless expiry/no-linkage; event allowlist; storage/log/network inspection | E-SEC + E-CI | prohibited data or linkage, excessive retention, unknown telemetry field |
| TS-SEC | authn/authz, IDOR/cross-parent, CSRF/session, XSS/injection, admin/API secret exposure, ClientID misuse, replay/tamper, rate/abuse, dependency/secrets | E-SEC | unresolved critical/high release-blocking finding |
| TS-PERF | web critical-path responsiveness, verifier latency/failure timeout, DNS/web health thresholds, resource regression and capacity/headroom acceptance | E-PERF | threshold breach without accepted remediation/rollback |
| TS-FAIL | auth/provider/datastore/AdGuard/DNS/upstream/network/browser/VPN/Private-Relay/captive-portal/timeouts/duplicate/stale-state failures | E-CI + E-DEVICE + E-NET | unsafe state, data leak, cross-parent access, unrecoverable critical path |
| TS-REC | retry/idempotency, profile/config recovery, account/device deletion/recovery, DNS removal, stale evidence downgrade, rollback and post-rollback verification | E-REC | rollback/removal/recovery cannot restore a truthful safe state |
| TS-OPS | exact release manifest, monitoring/alert visibility, known risks, runbook linkage, rollback artifact, operational rehearsal | E-OPS | operations cannot identify/monitor/recover exact accepted release |

## 5. Current critical-requirement coverage map

The current requirement register is the task-level source of truth. The following map covers every current requirement family; execution tooling must expand the family ranges to individual IDs and fail if any current `MUST`/critical requirement lacks at least one executable test/evidence mapping.

| Current requirement family | Primary suites | Mandatory decision/evidence outcome |
|---|---|---|
| `REQ-0001`–`REQ-0006` governance/authority/evidence | TS-GOV | canonical identity, traceability, no artifact-only PASS, write/read-back evidence |
| `REQ-0007`–`REQ-0012` product/core journey/account scope | TS-NOAUTH, TS-ACCOUNT, TS-UX, TS-STATE | accountless core preserved; optional account bounded; truthful Protection Map/non-goals |
| `REQ-0013`–`REQ-0017` validation/research evidence | TS-GOV, TS-UX, TS-OPS | synthetic evidence labelled correctly; reproducible evidence/uncertainty; no fabricated human validation |
| `REQ-0018` onward legal/privacy/data-readiness controls in PKG-04 | TS-PRIV, TS-GOV, TS-SEC | prohibited processing absent; exact applicable gate evidence; no legal conclusion inferred from software test |
| PKG-05 brand/design requirements | TS-UX, TS-A11Y | approved tokens/copy/limits and accessible presentation across surfaces |
| PKG-06 experience/service-design requirements | TS-NOAUTH, TS-ACCOUNT, TS-DNS, TS-STATE, TS-UX, TS-A11Y, TS-REC | all critical journeys/states/error/recovery/removal/i18n-accessibility criteria testable |
| PKG-07 application requirements | TS-NOAUTH, TS-ACCOUNT, TS-PRIV, TS-SEC, TS-FAIL, TS-REC, TS-PERF | production-capable dual-mode architecture behavior with server-only admin boundary and minimum data |
| `REQ-0042` onward PKG-08 DNS requirements | TS-DNS, TS-STATE, TS-FAIL, TS-REC, TS-PRIV | approved encrypted DNS/config/filter/privacy behavior and bypass/removal truth |
| PKG-09 platform/recovery requirements | TS-FAIL, TS-REC, TS-PERF, TS-OPS, TS-SEC | deployment/recovery/backup/rollback and environment identity independently proven |
| PKG-10 security requirements | TS-SEC, TS-FAIL, TS-REC, TS-OPS | threats/abuse/secrets/access controlled; release-blocking findings enforced |
| `REQ-0060`–`REQ-0064` measurement/data-quality requirements | TS-PRIV, TS-GOV | approved event schemas/formulas/denominators/quality only; no browsing/activity metrics |
| `REQ-0065`–`REQ-0066` QA/traceability requirements | all suites, led by TS-GOV | every critical requirement/state mapped; integrated coverage complete before release |

**Completeness algorithm:** at execution, parse `Plans/Master/Registers/REQUIREMENTS.md`; for every current row whose priority is binding (`MUST` or equivalent critical requirement), resolve its implementing task(s) and applicable test suites; emit a release trace matrix of `requirement -> task -> test ID -> environment -> evidence -> acceptance/gate`. Zero missing applicable requirements is required. Any newly added current requirement automatically becomes an acceptance blocker until mapped.

## 6. TSK-0409 device/network coverage — all 14 matrix cases

Every row below requires exact ENV/device/network versions and a before/action/verification/expected-state record.

| DNS case | Required tests | Expected truth behavior |
|---|---|---|
| Android Private DNS, no known override | DNS-01 happy; DNS-02 config-only; DNS-03 negative/error | config-only <= `configured_parent_confirmed`; positive technical proof -> `protected_verified`; negative/error -> truthful lower state |
| Android + Chrome system/current provider | DNS-04 browser-scope verify | protected only when browser effective path is proven |
| Android + Chrome custom non-UseSafeWeb Secure DNS | DNS-05 bypass | `not_covered` for Chrome until restored/reverified |
| Android + app-specific DoH/DoT/custom resolver | DNS-06 bypass | `not_covered` for that app |
| Android + VPN/DNS-changing app | DNS-07 connect/change/disconnect | fresh proof required after each resolver-affecting change; otherwise `not_covered`/`uncertain_error` |
| Apple DoH profile, no unresolved override | DNS-08 happy/config-only/negative | profile presence never technical proof; fresh effective-path verification required |
| Apple + Private Relay/Limit IP Address Tracking | DNS-09 conflict | no protected claim without current effective-path proof |
| Apple + VPN/app DNS/VPN profile | DNS-10 conflict | fresh proof or `not_covered`/`uncertain_error` |
| Firefox own differing DoH | DNS-11 bypass | `not_covered` until supported system behavior restored/reverified |
| Firefox default/disabled DoH through supported OS path | DNS-12 browser-scope verify | inherit only current proven effective path; indeterminate -> `uncertain_error` |
| Captive portal/sign-in network | DNS-13 transient | `uncertain_error` during portal; reverify after normal connectivity |
| Wi-Fi/cellular/SIM/VPN/profile/browser-resolver transition | DNS-14 freshness | invalidate affected stale verification immediately; recompute after fresh proof |
| Unsupported OS/version/unknown resolver/middleware | DNS-15 unsupported/unknown | known unsupported -> `not_covered`; indeterminate -> `uncertain_error` |
| Intentional removal | DNS-16 removal + residual mechanism check | `removed` only for evidence-backed target scope; other independently verified mechanism may remain |

## 7. TSK-0320 state and transition coverage

All six states are mandatory fixtures: `protected_verified`, `configured_parent_confirmed`, `action_needed`, `not_covered`, `uncertain_error`, `removed`.

Mandatory transition tests:

- ST-01 no evidence/unknown -> `uncertain_error` or applicable starting state; never optimistic protected state.
- ST-02 approved configuration/parent confirmation -> `configured_parent_confirmed`, never `protected_verified`.
- ST-03 fresh qualifying positive technical verifier -> `protected_verified`.
- ST-04 fresh technical negative with corrective action -> `action_needed`.
- ST-05 known unsupported/bypass -> `not_covered`.
- ST-06 verifier error/indeterminate/captive portal/stale effective-path evidence -> `uncertain_error` unless only current config evidence truthfully supports `configured_parent_confirmed`.
- ST-07 material resolver-affecting transition invalidates affected `protected_verified` freshness and requires re-verification.
- ST-08 technical contradiction outranks parent/configuration confirmation.
- ST-09 verified removal of target scope -> `removed`; account/device deletion or parent report alone cannot prove DNS removal.
- ST-10 recovery from `action_needed`/`uncertain_error`/`not_covered` can become `protected_verified` only after new qualifying technical evidence.
- ST-11 removal then reconfiguration remains configuration-only until technical re-verification.
- ST-12 independent layers are not globally upgraded/downgraded by evidence scoped to another layer.

Each transition test must assert both the state and the user-facing copy/next action. Negative tests must explicitly prove that configuration/profile/account/ClientID/ownership/parent confirmation/journey completion cannot masquerade as technical verification.

## 8. No-auth and optional-account critical journeys

### Accountless core — mandatory

- NA-01 public landing -> start setup without login/card/trial/payment.
- NA-02 Phone -> Internet -> Services sequence can complete without account creation.
- NA-03 anonymous journey state expires/clears according to current TSK-0229 rules; sign-in cannot retroactively link or extend it.
- NA-04 refresh/back/reopen/retry cannot silently duplicate irreversible actions or fabricate completion.
- NA-05 account prompt, if shown, is optional and cannot block core Protection Map value.
- NA-06 no-auth recovery/removal/self-service is available for applicable accountless functions.

### Optional account — mandatory where implemented

- AC-01 Google/Firebase sign-in success with secure server-side session boundary.
- AC-02 provider failure/cancel/timeout leaves accountless core usable.
- AC-03 session expiry/revocation returns to safe unauthenticated behavior.
- AC-04 every device operation enforces parent ownership server-side; cross-parent/IDOR negative tests must fail closed.
- AC-05 account/device deletion, revoke and recovery semantics are independently verifiable and never treated as DNS technical verification/removal.
- AC-06 ClientID/device ownership values are never browser-side authorization proof or unrestricted DNS administration capability.
- AC-07 account/dashboard contains no browsing/query/activity history.

## 9. Failure, privacy, security, performance and recovery matrix

Minimum failure injections: auth provider unavailable; datastore unavailable/timeout; AdGuard admin/API unavailable/malformed response; DNS verifier timeout/negative/indeterminate; Quad9/upstream failure; public DNS/web outage; stale/duplicate request; partial create/update/delete; stale ClientID; session revoked mid-operation; VPN/Private-Relay/browser-DoH change; captive portal; network switch; telemetry rejection; alerting/monitor failure.

For each: assert safe user state, bounded retry/idempotency, no cross-parent access, no secret/admin exposure, no browsing data, no false `protected_verified`, recoverability or explicit rollback, and post-recovery verification.

Privacy fixtures use synthetic bounded values only. **No real child browsing data, DNS question/domain/URL history, messages, contacts, photos, location or persistent child identity is permitted in fixtures or evidence.** Any test needing a domain-like syntax uses reserved documentation names such as `example.com` or local synthetic fixtures and never observed user history.

Performance tests must pin threshold + environment + release. A result without a frozen threshold is diagnostic only, not acceptance evidence. Exact thresholds remain owned by the applicable performance/capacity task; TSK-0517 defines the required test class and evidence shape rather than inventing downstream numbers.

## 10. Accessibility acceptance shape

Automated scanning alone cannot certify accessibility. Critical journeys require automated checks plus manual/assistive-technology evidence where the criterion is not machine-provable. At minimum cover keyboard/focus order/visibility; programmatic names/roles/states; headings/landmarks; forms/errors/status; contrast; 200%+ zoom/reflow; reduced motion; screen-reader announcement of protection states/errors; no color-only state; responsive touch targets; and modal/dialog escape/focus restoration.

Exact assistive-technology/browser pairs must be recorded at execution. The dated browser/OS matrix above is the minimum reference; if an accessibility requirement specifies a stricter pair, the stricter requirement controls.

## 11. Acceptance evidence record

Every executed test record must contain:

`test_id`, requirement/task IDs, exact release/source SHA, exact environment ID and actual full versions, fixture version, precondition, action, expected result, observed result, evidence locator/hash, timestamp, verifier/tool version, PASS/FAIL/BLOCKED disposition, defect/risk link, rerun reason if applicable.

Evidence must be reconstructable and privacy-safe. Screenshots/logs/traces are minimized and redacted of secrets or prohibited personal/browsing data. A re-run may replace failure only when the correction and new target evidence are explicit; old contrary evidence remains traceable.

## 12. Deterministic TSK-0517 acceptance assertions

TSK-0517 may be accepted as a **test-definition task** only when all are true:

1. Exact WBS metadata/dependencies/authority and ACC-0517 / VER-0517 / EVD-0517 are current.
2. TSK-0354 and TSK-0409 are current durable PASS dependencies.
3. REQ-0065/0066, CON-0023/0029, RSK-0050 and INT-0017 are explicitly bound.
4. Every current critical requirement family is mapped to an integrated test suite and execution must deterministically expand every current binding requirement to a concrete test/evidence row with zero unmapped applicable requirements.
5. Functional, browser/device/network, UX, accessibility, security/privacy, performance, failure/recovery, rollback and environment-specific classes are all defined.
6. All 14 TSK-0409 device/network cases and all six TSK-0320 states plus the mandatory transition set are covered.
7. Accountless core/no-auth and optional-account boundaries from current TSK-0354 are both covered; mandatory login and cross-parent access are negative blockers.
8. Exact dated environment/version references are specified, and later execution must record full actual versions rather than `latest`.
9. Fixtures/evidence contain no real child browsing data and no prohibited DNS/domain/activity history.
10. Non-production/synthetic evidence can prove the test plan and pre-release behavior only; it cannot masquerade as production/live-user evidence.
11. Release handoff cannot occur until the exact accepted release is traceable to monitoring/recovery/runbook/rollback evidence under INT-0017.
12. Full modular master-plan validation remains PASS and no canonical planning artifact is weakened or replaced.

**TSK-0517 result:** PASS candidate pending deterministic verification, GitHub read-back, full modular-plan validation and durable runtime reconciliation. No downstream test execution or release acceptance is inferred.