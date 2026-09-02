# TSK-0516 — Master Verification and Acceptance Test Plan

**Version:** 1.0.0  
**Date:** 2026-09-02  
**Authority:** Derived verification plan. Canonical task/acceptance/dependency authority remains `Plans/Master/WBS/master-wbs.csv`.  
**Predecessor:** `TSK-0048` accepted vertical implementation backlog.

## Purpose

Define one evidence-complete verification contract for the Version-1 implementation so LG-07 can approve a build plan without weakening downstream LG-08/LG-09 runtime acceptance. This plan does not execute L6 tests and creates no implementation PASS.

## Standing invariants

1. The complete accountless core must remain usable without login.
2. Optional Google/Firebase identity and server session may add parent-owned device persistence/dashboard value but may not gate core setup/protection value.
3. No browsing/query/activity history is collected or exposed as product analytics or dashboard data.
4. Child accounts and unrestricted customer DNS administration remain excluded.
5. Verified protection evidence is never inferred from parent confirmation or client-only state.
6. Every ownership-sensitive path must fail closed across parents/devices and opaque IDs are never authorization.
7. Secrets/admin credentials remain server-side/external to Git; tests/evidence must redact them.
8. CR-0009/DEC-0056 legal/regulatory/compliance conclusions remain owner-external and are not asserted by this plan.

## Evidence rules

- Every executed test records: test ID, source commit/config/content version, exact environment, fixture identity class, expected result, actual result, timestamp, verifier, and evidence reference.
- Fixtures must be synthetic or approved non-sensitive test data; never use real child browsing/query history.
- Negative/security/privacy/recovery tests are blocking when their mapped acceptance says fail closed, preserve privacy, or recover safely.
- Producer-only self-certification is insufficient for security/privacy/recovery controls where independent evidence is required by their canonical task.
- Any severity-1/2, Critical/High control failure, cross-parent access, secret exposure, false verified-protection claim, destructive unrecoverable state, or mandatory-login regression blocks promotion.

## Master test matrix

| ID | Verification area | Required scenario | Expected acceptance | Primary implementation anchors | Evidence |
|---|---|---|---|---|---|
| VAT-001 | Accountless happy path | Fresh anonymous user completes public → intake → Phone/Internet/Services → DNS setup → verification → Protection Map → completion without authentication | Core value completes without login; state is truthful and privacy-minimal | TSK-0357, TSK-0358, TSK-0361, TSK-0375, TSK-0376, TSK-0381, TSK-0337, TSK-0370 | E2E trace + screenshots/DOM assertions + state assertions |
| VAT-002 | Accountless expiry/resume | Anonymous state expires, is lost, resumed where allowed, or restarted | No cross-journey disclosure; expired state fails safely; user can restart | TSK-0357, TSK-0358 | Functional + negative state tests |
| VAT-003 | Mandatory-login regression | Exercise every accountless core route while signed out and with auth provider unavailable | No core route redirects to mandatory login | TSK-0358, TSK-0361, TSK-0395 | Route/UI assertions |
| VAT-004 | Google sign-in happy path | Valid provider token → server verification → session → dashboard entry → logout | Secure server session created; minimal identity only; logout invalidates session | TSK-0377, TSK-0394 | Auth integration + cookie/session assertions |
| VAT-005 | Provider failure | Google/Firebase unavailable, invalid token, callback error, timeout | Fails safely; accountless core remains available; no partial authenticated state | TSK-0377, TSK-0394, TSK-0366 | Failure injection evidence |
| VAT-006 | Session lifecycle | Expiry, idle timeout if applicable, revocation, logout, replay of expired/revoked session | Expired/revoked sessions denied; safe return path; CSRF/session controls remain intact | TSK-0377, TSK-0373 | Negative session tests |
| VAT-007 | CSRF | Mutating authenticated actions without/with invalid anti-CSRF proof | Requests fail closed with no state change | TSK-0377, TSK-0367, TSK-0363, TSK-0364 | Security request/response evidence |
| VAT-008 | IDOR/cross-parent isolation | Parent A attempts read/update/delete/revoke of Parent B device/client IDs including guessed/opaque identifiers | Every path denied; no metadata leakage or side effect | TSK-0367, TSK-0363, TSK-0364, TSK-0387, TSK-0388 | Authz negative suite |
| VAT-009 | Parent/device datastore | CRUD, duplicate names, concurrent update/delete, stale mapping | Minimum data only; ownership constraints and concurrency rules enforce safe state | TSK-0367 | Datastore tests + schema inspection |
| VAT-010 | ClientID provisioning | Create/retry same device; concurrent submission; invalid platform/input | One intended persistent client; high-entropy opaque ClientID; idempotent reconciliation | TSK-0365, TSK-0378, TSK-0385 | API/AdGuard state diff + entropy/format checks |
| VAT-011 | ClientID lifecycle | Reinstall, revoke, remove, reset, replacement, stale/duplicate mapping | Old identifiers/clients are dispositioned; UI status becomes truthful; retries recover | TSK-0364, TSK-0388, TSK-0417 | Lifecycle E2E + reconciliation evidence |
| VAT-012 | Restricted AdGuard adapter | Allowlisted operations, invalid inputs/responses, arbitrary `/control` proxy attempts, timeouts/retries | Only typed allowlisted operations work; secrets never leave server; failures bounded | TSK-0362 | Adapter contract + negative tests |
| VAT-013 | DNS endpoint/configuration | Supported DoH profile/instructions, correct endpoint, TLS, upstream, baseline policy | Valid supported config resolves/filters as approved without secret exposure | TSK-0360, TSK-0418, TSK-0419, TSK-0420, TSK-0421, TSK-0422 | DNS/TLS/config assertions |
| VAT-014 | DNS verification truth | Allowed/blocked synthetic tests, timeout, cache, conflict, unsupported state | Deterministic working/failed/uncertain outcome; no query history; no client-only spoofing | TSK-0243, TSK-0372, TSK-0629 | Synthetic DNS + state assertions |
| VAT-015 | Network conflict guidance | Private Relay, VPN, secure DNS, incompatible network conditions | Detectable/undetectable distinction is truthful; safe recovery guidance; no universal-enforcement claim | TSK-0416, TSK-0381 | Device/network matrix evidence |
| VAT-016 | Protection Map truth model | Verified, parent-confirmed, configured, action-needed, not-covered, uncertain, removed states | States match frozen evidence rules; verified is never inferred; gaps stay visible | TSK-0371, TSK-0337, TSK-0390 | State-machine + UI assertions |
| VAT-017 | Native safeguard flow | Supported/unsupported/already-configured/skip/error paths | Versioned guidance is applicable, accessible and does not falsely claim system verification | TSK-0374, TSK-0382 | Functional/content-version evidence |
| VAT-018 | External-service safeguard | Relevant selection, irrelevant/unsupported route, confirmation | Only relevant flow appears; confirmation remains distinct from verification | TSK-0383 | Functional/state evidence |
| VAT-019 | Account deletion | Reauthentication/confirmation → account/device/client/session cleanup; provider or AdGuard partial failure | Approved cascade completes or reconciles safely; deleted content is not retained in evidence | TSK-0241, TSK-0373, TSK-0384, TSK-0366 | Deletion/recovery E2E |
| VAT-020 | Retention/DSR workflows | Expiry/deletion across primary/cache/export/support/backup-designed handling | Approved retention/deletion behavior works; authority checks proportionate; evidence contains no deleted content | TSK-0242 | Data lifecycle test evidence |
| VAT-021 | Privacy-minimal telemetry | Inspect logs/statistics/product events during happy/failure/account flows | No browsing/query/activity history or prohibited identifiers; diagnostics bounded; approved events only | TSK-0244, TSK-0448, TSK-0499 | Log/event inspection + negative assertions |
| VAT-022 | Support/troubleshooting | Common setup/verification/removal/false-positive/compatibility failures | Contextual self-service resolves or escalates; diagnostic fields minimal and time-bounded | TSK-0369, TSK-0391, TSK-0393, TSK-0630 | Scenario walkthrough + schema checks |
| VAT-023 | Accessibility | Keyboard, focus, screen reader, semantics, contrast, resize, responsive states for public/account/dashboard/error paths | Applicable WCAG 2.2 AA acceptance passes; no critical/high accessibility blocker | TSK-0361, TSK-0386, TSK-0394, TSK-0385 | Automated + manual accessibility evidence |
| VAT-024 | Localization | English/Turkish/Arabic, RTL Arabic, fallback and locale-specific instructions | Correct localized content/layout; no silent applicability mismatch | TSK-0359 | Locale/RTL snapshots + assertions |
| VAT-025 | Performance/degradation | Critical web journeys, DNS latency/availability, dependency outage/degraded state | Defined NFRs met or safe degradation shown; capacity/health signals available | TSK-0414, TSK-0386 | Performance + synthetic health evidence |
| VAT-026 | Secrets/privileged access | Secret scan, runtime injection, file permissions, error/log redaction, rotation/revocation | No production secret committed/exposed; least privilege; break-glass/rotation behavior tested | TSK-0457, TSK-0490 | Secret scan + permission/rotation tests |
| VAT-027 | Build/CI reproducibility | Clean checkout, deterministic commands, lint/type/test/security gates, SBOM | Build/test commands deterministic; failures block; dependency inventory/SBOM reproducible | TSK-0380, TSK-0453, TSK-0489, TSK-0491 | CI logs + generated SBOM |
| VAT-028 | Deployment rollback | Failed/superseded deploy, config migration, health-gate failure, rollback | Rollback returns web/DNS/config to known-good state; effects and timing recorded | TSK-0452, TSK-0519, TSK-0447 | Deployment/rollback transcript |
| VAT-029 | AdGuard/server recovery | Clean Ubuntu 24.04 LTS owner-provided VM, script idempotency, trusted source/version checks, backup/restore | Rebuild/recovery deterministic; secrets external; service/config/health acceptance passes | TSK-0455, TSK-0456, TSK-0457, TSK-0447 | Clean-server independent evidence |
| VAT-030 | Partial-failure reconciliation | Auth/datastore/AdGuard create/update/delete outages and duplicates | Bounded retries converge to documented safe state; no orphan grants access or false protection | TSK-0366 | Failure-injection + final-state proof |
| VAT-031 | Monitoring/alerts/runbooks | Synthetic outages, threshold breach, alert route, runbook execution | Privacy-safe actionable alert has owner/severity/runbook; urgent/durable routes work as designed | TSK-0379, TSK-0541, TSK-0540 | Alert delivery + runbook evidence |
| VAT-032 | Non-goal regression | Attempt to expose history, child account, unrestricted DNS admin, mandatory login | Functionality is absent/inaccessible and no data path silently implements it | Cross-cutting | Negative product/security inspection |

## Execution sequence

1. **Foundation qualification:** VAT-026–VAT-029 before relying on automated environment evidence.
2. **Accountless vertical slice:** VAT-001–VAT-003, VAT-013–VAT-018.
3. **Optional account/device slice:** VAT-004–VAT-012, VAT-019–VAT-020.
4. **Cross-cutting quality:** VAT-021–VAT-025, VAT-030–VAT-032.
5. Re-run affected tests after any implementation/config/content/vendor-version change that can invalidate prior evidence.

## Blocking and disposition rules

- **BLOCK:** any failed security/privacy ownership boundary; secret exposure; false verified-protection state; mandatory-login regression; destructive unrecovered deletion/revocation; failed clean-server/rollback evidence; severity-1/2 defect; unresolved Critical/High control failure.
- **RETEST REQUIRED:** any fix or dependency/config/content/version change touching the failed or dependent path.
- **LOWER-SEVERITY RESIDUAL:** may proceed only when canonical acceptance permits it and impact, workaround, owner, target date, and explicit disposition are durable.
- Test evidence is release-specific; historical PASS cannot satisfy a changed implementation/config/version without current applicability proof.

## LG-07 boundary

This plan is an L5 verification design artifact. It proves that required implementation outcomes have mapped acceptance tests; it does **not** prove those tests have executed, does not mark any L6 task PASS, and does not itself satisfy LG-07. Actual L6 build begins only after LG-07 is independently PASS under current authority.
