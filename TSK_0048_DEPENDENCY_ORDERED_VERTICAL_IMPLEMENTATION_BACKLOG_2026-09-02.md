# TSK-0048 — Dependency-Ordered Vertical Implementation Backlog

**Version:** 1.0.0  
**Date:** 2026-09-02  
**Authority:** Derived execution view from canonical `Plans/Master/WBS/master-wbs.csv`; WBS remains the sole task/dependency/acceptance authority.  
**Scope:** Current non-PASS L6 implementation work only. No task ID, dependency, gate, acceptance criterion, runtime state, product scope, or authority boundary is changed by this artifact.

## Guardrails

- Preserve the complete **accountless core**; mandatory login is prohibited for core value.
- Optional Version-1 scope may include Google sign-in/server session, minimum parent/device ownership persistence, lightweight dashboard/device management, and deletion/recovery only within frozen scope.
- Excluded: browsing/query/activity history, child accounts, unrestricted customer DNS administration, and unapproved product expansion.
- CR-0009/DEC-0056 legal/regulatory/compliance work remains owner-external for sequencing only; this backlog makes no legal conclusion or legal PASS claim.
- Production, spend, secrets, target-environment actions, and human-only decisions remain subject to their own gates and Action Authority.

## Backlog summary

- Current non-PASS L6 tasks represented: **76**.
- Dependency-ordered execution slices: **55**; each slice contains at most 4 canonical tasks and is grouped by topological wave plus user/operational outcome lane.
- Ordering rule: a task never appears before any non-PASS L6 dependency. Dependencies outside L6 must independently satisfy their own current gate/state before execution.
- Size is a derived execution estimate (`S`/`M`) only; canonical task semantics remain in WBS. Risk is represented by canonical risk reference, plan priority, and critical-path flag.

## Slice 01 — Wave 0 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 2 | `TSK-0361` — Implement the public/customer website from approved IA, brand, content, accessibility, performance, SEO, privacy, and conversion requirements | Software | TSK-0354; TSK-0308; TSK-0307 | ACC-0361: `/website` builds as the approved TypeScript + Next.js full-stack app; critical public/start pages work on mobile/desktop in English/Turkish/Arabic including RTL; approved component library/CMS integration works; WCAG 2.2 AA, performance/security/SEO and no-premature-claims acceptance pass; no unnecessary local database is introduced. | VER-0361: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement the public/customer website from approved IA, brand, content, accessibility, performance, SEO, privacy, and conversion requirements". | M | RSK-0045; priority HIGH; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |
| 14 | `TSK-0395` — Implement public landing page and primary first-phone CTA | Frontend Engineering | TSK-0322; TSK-0324 | ACC-0395: Copy matches approved claims; primary CTA is clear; no DNS-led positioning; privacy/limits/support links are present; responsive/accessibility/performance checks pass. | VER-0395: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement public landing page and primary first-phone CTA". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 02 — Wave 0 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 18 | `TSK-0454` — Create approved source, infrastructure, configuration, test, and documentation structure | Software Engineering | TSK-0050 | ACC-0454: Clean checkout documents/builds the canonical monorepo structure including top-level `/website` for the full-stack application and `/infrastructure/adguard-server` for AdGuard/server deployment/recovery; ownership, generated files, artifact locations and secret exclusions are explicit; no duplicate authority is created. | VER-0454: Use the approved checklist/test procedure against the exact artifact/environment; retain reproducible outputs and reviewer result. | Versioned artifact, decision, configuration, result, or evidence record for "Create approved source, infrastructure, configuration, test, and documentation structure". | M | RSK-0048; priority MEDIUM; critical-path NO | Development → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |
| 41 | `TSK-0455` — Implement the complete production-grade Ubuntu 24.04 LTS deployment/recovery Bash script | Cloud | TSK-0445 | ACC-0455: One versioned direct-host executable system under `/infrastructure/adguard-server` starts from an owner-provided Ubuntu 24.04 LTS VM and performs prerequisite checks, OS baseline/packages, pinned AdGuard install, approved server-managed config application/recovery, firewall/network, DNS/TLS endpoints, privacy/filter state, services, backup/restore hooks, health and acceptance tests with deterministic exit codes. | VER-0455: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement the complete production-grade Ubuntu 24.04 LTS deployment/recovery Bash script". | M | RSK-0048; priority CRITICAL; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 03 — Wave 0 — Privacy, transparency, support and product events

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 1 | `TSK-0357` — Implement privacy-minimal anonymous journey state, expiry, deletion, and safe resume behavior | Software | TSK-0354 | ACC-0357: No identity is required; state is scoped/unpredictable, expires/deletes as approved, cannot expose another journey, and contains no browsing history. | VER-0357: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement privacy-minimal anonymous journey state, expiry, deletion, and safe resume behavior". | S | RSK-0045; priority HIGH; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 04 — Wave 1 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 3 | `TSK-0358` — Implement routing, setup, verification, Protection Map, troubleshooting, recovery/removal, and completion without mandatory login | Software | TSK-0357; TSK-0361; TSK-0320 | ACC-0358: Server/browser state machine supports the complete accountless core plus optional account entry/return/expiry/logout and dashboard routing; state transitions preserve truthful evidence, recover safely from lost/expired state, and never force login for core value or persist browsing/activity history. | VER-0358: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement routing, setup, verification, Protection Map, troubleshooting, recovery/removal, and completion without mandatory login". | M | RSK-0045; priority CRITICAL; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 05 — Wave 1 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 19 | `TSK-0380` — Implement deterministic local build, lint, test, and validation commands | Software Engineering | TSK-0454 | ACC-0380: Clean environment setup succeeds; commands return nonzero on failure; versions are pinned or bounded; no manual undocumented step is required for the baseline build. | VER-0380: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement deterministic local build, lint, test, and validation commands". | S | RSK-0045; priority MEDIUM; critical-path NO | Development → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |
| 20 | `TSK-0451` — Implement only the post-VM server/network/configuration automation that materially improves reproducibility | Cloud/DevOps | TSK-0444; TSK-0454 | ACC-0451: Automation begins from owner-provided reachable VMs and applies only approved post-VM server/network/configuration state; it detects drift where useful, guards destructive changes, embeds no secrets, and does not create Azure subscriptions/VMs/resources merely for IaC completeness. | VER-0451: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, configuration, result, or evidence record for "Implement only the post-VM server/network/configuration automation that materially improves reproducibility". | M | RSK-0048; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |
| 42 | `TSK-0456` — Implement trusted-source verification, compatible version pinning/selection, checksums/signatures where available, and rollback inputs | Cloud | TSK-0455 | ACC-0456: Script refuses untrusted/incompatible artifacts, records exact versions/sources, supports approved upgrade workflow, and does not assume latest is safe. | VER-0456: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement trusted-source verification, compatible version pinning/selection, checksums/signatures where available, and rollback inputs". | S | RSK-0048; priority HIGH; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |
| 43 | `TSK-0457` — Implement secure secret/input acquisition, permissions, redaction, temporary-file cleanup, and non-exportable evidence | Cloud | TSK-0455 | ACC-0457: Production secrets/tokens/private keys are obtained only from approved external secret mechanisms; none is embedded, encrypted/committed to Git, echoed, left world-readable or included in evidence; temporary material is cleaned; missing/invalid secrets fail safely. | VER-0457: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement secure secret/input acquisition, permissions, redaction, temporary-file cleanup, and non-exportable evidence". | M | RSK-0048; priority CRITICAL; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 06 — Wave 2 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 7 | `TSK-0375` — Implement minimal intake validation and routing engine | Software Engineering | TSK-0358 | ACC-0375: Decision table and boundary/error tests cover every approved combination; prohibited data is rejected/not requested; unsupported combinations return clear safe state. | VER-0375: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement minimal intake validation and routing engine". | S | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 07 — Wave 2 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 4 | `TSK-0243` — Implement privacy-safe DNS protection verification | Network Engineering | TSK-0358 | ACC-0243: Verification result is deterministic for supported paths, does not expose query history, handles caches/failures/conflicts, records only approved event data, and maps exactly to Protection Map rules. | VER-0243: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement privacy-safe DNS protection verification". | S | RSK-0001; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 21 | `TSK-0422` — Implement versioned AdGuard and DNS service configuration pipeline | Network Engineering | TSK-0451 | ACC-0422: Generated/applied configuration matches approved settings; secrets are separated; changes are diffable; validation prevents query logging, ECS, or unapproved upstream/processor drift. | VER-0422: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement versioned AdGuard and DNS service configuration pipeline". | S | RSK-0004; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |
| 22 | `TSK-0449` — Implement environment DNS, DoH endpoint, and certificate automation | Cloud/DevOps | TSK-0451 | ACC-0449: CI/ephemeral test and any explicitly triggered staging endpoints resolve as applicable; TLS chain/hostname/protocol are correct; renewals are tested; expiry alert and emergency replacement procedure exist; registrar/API secrets are protected. | VER-0449: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement environment DNS, DoH endpoint, and certificate automation". | M | RSK-0048; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 08 — Wave 2 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 6 | `TSK-0360` — Implement safe generation/delivery of supported configuration profiles or endpoint instructions without exposing admin secrets | Software | TSK-0358; TSK-0317 | ACC-0360: Profiles/configs are correct, integrity-protected, revocable/reinstallable where applicable, privacy-minimal, rate-controlled, and tested on supported platforms. | VER-0360: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement safe generation/delivery of supported configuration profiles or endpoint instructions without exposing admin secrets". | M | RSK-0045; priority HIGH; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |
| 40 | `TSK-0453` — Configure formatting, linting, type checking, commit/change, and code-review rules | Software Engineering | TSK-0380 | ACC-0453: Checks run locally/CI; critical paths require review; generated/configuration changes are included; exceptions are documented and time-bounded. | VER-0453: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Configure formatting, linting, type checking, commit/change, and code-review rules". | S | RSK-0048; priority MEDIUM; critical-path NO | Development → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |
| 45 | `TSK-0491` — Establish dependency inventory, update policy, lock files, and SBOM generation | Security | TSK-0380 | ACC-0491: All direct dependencies/images are versioned; lockfiles or digests are committed; SBOM generates in CI; update/severity policy and owner are documented. | VER-0491: Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence. | Versioned artifact, decision, configuration, result, or evidence record for "Establish dependency inventory, update policy, lock files, and SBOM generation". | S | RSK-0007; priority MEDIUM; critical-path NO | Development → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 09 — Wave 2 — Localization, accessibility and hardening

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 5 | `TSK-0359` — Implement externalized content, locale routing/fallback, RTL layout support, metadata, and locale-specific instruction selection | Software | TSK-0311; TSK-0358 | ACC-0359: English, Turkish, and Arabic production locale paths/content render correctly; RTL works for Arabic; fallback/applicability and locale-specific instructions prevent silent mismatch; SEO/index behavior is explicit; language availability is not presented as official non-UK market activation. | VER-0359: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement externalized content, locale routing/fallback, RTL layout support, metadata, and locale-specific instruction selection". | M | RSK-0045; priority MEDIUM; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 10 — Wave 2 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 17 | `TSK-0417` — Implement removal, revocation, reset, and device-change procedures | Network Engineering | TSK-0358 | ACC-0417: Supported platforms can remove configuration; protection consequence is clear; revoked/replaced artifacts stop working as designed; stale records are deleted; support can follow a documented path. | VER-0417: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement removal, revocation, reset, and device-change procedures". | S | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A4 | PLANNED |
| 75 | `TSK-0629` — Implement privacy-safe automated checks that confirm what can be technically verified and clearly label everything else | Customer Experience | TSK-0358; TSK-0320 | ACC-0629: Checks identify working/failed/uncertain/removed states without browsing history; parent confirmation remains separate; actionable recovery is offered. | VER-0629: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement privacy-safe automated checks that confirm what can be technically verified and clearly label everything else". | M | RSK-0005; priority HIGH; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A4 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 11 — Wave 3 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 9 | `TSK-0376` — Implement Phone → Internet → Services step and skip state machine | Software Engineering | TSK-0375 | ACC-0376: All state transitions are defined/tested; illegal transitions are rejected; parent-confirmed and verified evidence are separate; resume/retry does not duplicate completed work. | VER-0376: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement Phone → Internet → Services step and skip state machine". | S | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 12 — Wave 3 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 23 | `TSK-0450` — Implement CI/ephemeral test environments and the isolated pilot environment | Cloud/DevOps | TSK-0451; TSK-0422; TSK-0449 | ACC-0450: CI/ephemeral preview/test environments use synthetic data, are isolated and disposable, and teardown/rebuild succeeds; the owner-provided pilot VM is verified against region/access/data policy; no persistent staging environment is provisioned unless its explicit evidence trigger opens. | VER-0450: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, configuration, result, or evidence record for "Implement CI/ephemeral test environments and the isolated pilot environment". | M | RSK-0048; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |
| 46 | `TSK-0489` — Implement continuous integration quality and security gates | Release Engineering | TSK-0453; TSK-0491; TSK-0422 | ACC-0489: All approved checks execute on pull/change requests and main; failures block promotion; evidence is retained; test bypass requires recorded owner authority. | VER-0489: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement continuous integration quality and security gates". | M | RSK-0007; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 13 — Wave 3 — Protection Map and safeguard guidance

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 8 | `TSK-0374` — Implement versioned device/service content delivery | Software Engineering | TSK-0375; TSK-0323 | ACC-0374: Correct content/version is selected; stale/unsupported states are visible; integrity/version metadata is preserved; missing content fails safely; update rollback is possible. | VER-0374: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement versioned device/service content delivery". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 14 — Wave 3 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 15 | `TSK-0416` — Implement detection/guidance for Private Relay, VPN, secure DNS, and network conflicts | Network Engineering | TSK-0243 | ACC-0416: Each known conflict has a test, detectable/undetectable state, safe guidance, coverage consequence, recovery, and Protection Map result; the product never claims universal enforcement. | VER-0416: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement detection/guidance for Private Relay, VPN, secure DNS, and network conflicts". | S | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 76 | `TSK-0630` — Implement the highest-priority troubleshooting, false-positive, compatibility, reinstall/reset, and removal decision trees | Customer Experience | TSK-0628; TSK-0629 | ACC-0630: Each path is concise, source-current, privacy-safe, testable, linked at point of need, and ends in verified resolution or exceptional escalation. | VER-0630: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, or evidence record for "Implement the highest-priority troubleshooting, false-positive, compatibility, reinstall/reset, and removal decision trees". | M | RSK-0005; priority HIGH; critical-path NO | L6 relative to its gate | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 15 — Wave 4 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 24 | `TSK-0418` — Deploy the approved AdGuard service from versioned configuration | Network Engineering | TSK-0422; TSK-0450 | ACC-0418: Deployment version/config are recorded; admin interface is restricted; service starts reliably; configuration drift check passes; no unapproved component is enabled. | VER-0418: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Deploy the approved AdGuard service from versioned configuration". | M | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 16 — Wave 4 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 44 | `TSK-0490` — Implement secrets, identity, and privileged-access controls | Security | TSK-0450 | ACC-0490: Secret scan proves no production secret/token/private key is committed, even encrypted; external secret injection is verified; normal identities/services are least privilege; any root-capable bootstrap/deploy path is narrowly scoped/audited; rotation/revocation and break-glass recovery are tested. | VER-0490: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement secrets, identity, and privileged-access controls". | M | RSK-0007; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 17 — Wave 4 — Operations, observability, resilience and incident response

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 38 | `TSK-0448` — Implement the lean approved operational metrics and necessary retrievable logs | SRE/Operations | TSK-0450 | ACC-0448: External/service health and basic CPU/memory/disk/availability metrics are available; any logs retained are only those necessary for diagnosis, privacy-safe and access/retention controlled; DNS queries/client browsing identifiers are absent/anonymised as approved; no centralized logging/APM platform is required without evidence. | VER-0448: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, configuration, result, or evidence record for "Implement the lean approved operational metrics and necessary retrievable logs". | M | RSK-0048; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 18 — Wave 4 — Privacy, transparency, support and product events

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 10 | `TSK-0369` — Implement minimal support, feedback, false-positive, and abandonment capture | Software Engineering | TSK-0376 | ACC-0369: Required fields are minimal; domain/device diagnostics are constrained/time-bounded; privacy notice and deletion route are present; root-cause categories support defined metrics. | VER-0369: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement minimal support, feedback, false-positive, and abandonment capture". | S | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 48 | `TSK-0499` — Implement approved product events and metric validation | Product Analytics | TSK-0497; TSK-0376 | ACC-0499: Analytics/measurement architecture supports aggregate product/service decisions and the minimum security/lifecycle signals required for optional accounts without browsing/activity history. Account/session/dashboard events are purpose-limited, access-controlled, retention-bounded and deletable; child-linked DNS/query data is never used as product analytics. | VER-0499: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement approved product events and metric validation". | M | RSK-0049; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 19 — Wave 4 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 11 | `TSK-0372` — Integrate DNS activation verification with journey state | Software Engineering | TSK-0243; TSK-0376; TSK-0358 | ACC-0372: Success/failure/timeout/cache/conflict/unsupported cases map correctly; retries are bounded; no query-history data is exposed/stored; verification cannot be spoofed by client-only confirmation. | VER-0372: Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence. | Versioned artifact, decision, configuration, result, or evidence record for "Integrate DNS activation verification with journey state". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 20 — Wave 5 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 39 | `TSK-0379` — Implement service, security, deployment, and cost dashboards | SRE/Operations | TSK-0448 | ACC-0379: Dashboards use approved aggregate signals, link to runbooks/releases, identify stale/missing telemetry, and contain no browsing-history/top-domain view. | VER-0379: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement service, security, deployment, and cost dashboards". | S | RSK-0045; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 21 — Wave 5 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 33 | `TSK-0421` — Configure and verify Quad9 dns10 DoH upstream with ECS disabled | Network Engineering | TSK-0418 | ACC-0421: Configured endpoint is exactly https://dns10.quad9.net/dns-query; ECS is disabled; DNSSEC behavior is verified; no fallback or alternate upstream bypasses approval. | VER-0421: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Configure and verify Quad9 dns10 DoH upstream with ECS disabled". | S | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 22 — Wave 5 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 47 | `TSK-0452` — Implement controlled direct-host CI/ephemeral and pilot deployment automation | Release Engineering | TSK-0489; TSK-0490 | ACC-0452: Pipeline deploys directly to the approved host without requiring Docker; records source/config/content/filter versions, environment, authority, tests, health checks and rollback target/result; failed health gates stop/roll back where safe; production secrets are externally injected and never committed. | VER-0452: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, implementation, decision, configuration, result, or evidence record for "Implement controlled direct-host CI/ephemeral and pilot deployment automation". | M | RSK-0048; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 23 — Wave 5 — Privacy, transparency, support and product events

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 25 | `TSK-0244` — Apply and verify privacy-minimal logging and statistics configuration | Privacy Engineering | TSK-0418 | ACC-0244: Direct inspection and test show prohibited logs/statistics/history are absent; diagnostic mode is off by default, time-bounded, access-controlled, and deletion-tested. | VER-0244: Use the approved checklist/test procedure against the exact artifact/environment; retain reproducible outputs and reviewer result. | Versioned artifact, decision, configuration, result, or evidence record for "Apply and verify privacy-minimal logging and statistics configuration". | S | RSK-0001; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 49 | `TSK-0242` — Implement retention expiry, deletion, and data-subject request workflows | Privacy Engineering | TSK-0499; TSK-0369 | ACC-0242: Expiry/deletion works for primary, cache, export, support, and backup handling as designed; DSR identity/authority checks are proportionate; audit evidence contains no deleted content. | VER-0242: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement retention expiry, deletion, and data-subject request workflows". | M | RSK-0001; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 24 — Wave 5 — Protection Map and safeguard guidance

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 12 | `TSK-0371` — Implement Protection Map evidence and state rules | Software Engineering | TSK-0372; TSK-0374 | ACC-0371: Every requirement example and edge case passes; verified cannot be inferred from parent input; Not covered remains visible; state evidence and copy version are traceable. | VER-0371: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement Protection Map evidence and state rules". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 25 — Wave 5 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 16 | `TSK-0381` — Implement DNS activation and verification flow | Frontend Engineering | TSK-0416; TSK-0372 | ACC-0381: All supported device/network paths, success/failure/timeout/conflict/removal states, retry limits, privacy copy, and Protection Map integration pass end-to-end tests. | VER-0381: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement DNS activation and verification flow". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 26 — Wave 6 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 13 | `TSK-0370` — Implement completion, optional save/export, and quiet exit behavior | Software Engineering | TSK-0371 | ACC-0370: Completion requires defined applicable steps, shows all gaps, provides approved save/export only if privacy-safe, explains removal/support, and contains no payment ask before the authorised experiment stage. | VER-0370: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement completion, optional save/export, and quiet exit behavior". | S | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 34 | `TSK-0419` — Configure and validate public DNS-over-HTTPS endpoint | Network Engineering | TSK-0449; TSK-0421 | ACC-0419: DoH resolves allowed domains, blocks approved test domains, rejects invalid paths as designed, presents valid TLS, and passes supported client/network tests. | VER-0419: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Configure and validate public DNS-over-HTTPS endpoint". | M | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 27 — Wave 6 — Build/release foundation

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 51 | `TSK-0519` — Test deployment rollback and environment recovery | Release Engineering | TSK-0452 | ACC-0519: An intentionally failed/superseded deployment is rolled back in the approved CI/ephemeral pre-production environment or explicitly triggered staging environment; DNS/web health returns to baseline; configuration/data consequences are verified and timed. | VER-0519: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Test deployment rollback and environment recovery". | M | RSK-0050; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 28 — Wave 6 — Operations, observability, resilience and incident response

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 50 | `TSK-0368` — Implement minimum safe operational configuration/admin capability | Software Engineering | TSK-0374; TSK-0242 | ACC-0368: Only a minimal private operator/admin surface exists where operations materially benefit; it is strongly authenticated, least privilege, audited, excludes browsing history and unnecessary user-level data, supports controlled change/rollback, and does not become a customer dashboard or second product. | VER-0368: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement minimum safe operational configuration/admin capability". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 69 | `TSK-0541` — Implement and test actionable alerts and notification routing | SRE/Operations | TSK-0379 | ACC-0541: Each actionable alert has threshold/rationale/severity/owner/dedup/runbook and no sensitive payload; urgent critical alerts reach Telegram and durable notices/reports reach email; test notifications are delivered and acknowledged. | VER-0541: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement and test actionable alerts and notification routing". | M | RSK-0006; priority MEDIUM; critical-path NO | Development Foundation → Development Foundation | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 29 — Wave 6 — Privacy, transparency, support and product events

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 26 | `TSK-0396` — Implement parent and child transparency at the required moments | Frontend Engineering | TSK-0322; TSK-0244 | ACC-0396: Content matches approved notice and actual deployed configuration; material limitations are prominent; child-readable text is accessible; contacts/rights/removal are complete. | VER-0396: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement parent and child transparency at the required moments". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 30 — Wave 7 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 52 | `TSK-0377` — Implement Firebase Google sign-in and privacy-minimal server session lifecycle | Software Engineering | TSK-0519 | ACC-0377: Google sign-in token is verified server-side; a Secure/HttpOnly/SameSite server session with CSRF protection is created, expired, resumed, revoked and logged out correctly; minimal identity fields only are retained; invalid/expired/revoked/provider-failure paths fail safely; auth tokens are not stored in browser localStorage. | VER-0377: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement Firebase Google sign-in and privacy-minimal server session lifecycle". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 31 — Wave 7 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 27 | `TSK-0397` — Implement intake, validation, and routing UI | Frontend Engineering | TSK-0375; TSK-0396 | ACC-0397: All prototype and requirements states are implemented; client/server validation agrees; screen-reader/errors/focus work; analytics events match catalogue; unsupported paths fail safely. | VER-0397: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement intake, validation, and routing UI". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 32 — Wave 7 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 36 | `TSK-0420` — Implement and version the sensible baseline filter policy | Network Engineering | TSK-0419 | ACC-0420: Policy source/version/rationale are recorded; expected test domains pass/fail; known false-positive tests are included; changes require staged verification and rollback. | VER-0420: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement and version the sensible baseline filter policy". | S | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A4 | PLANNED |
| 73 | `TSK-0488` — Implement resolver access, firewall, rate-limit, and abuse controls | Security | TSK-0419; TSK-0541 | ACC-0488: Only required ports/protocols are exposed; admin is restricted; approved rate/access controls work; abuse tests/alerts trigger; legitimate supported clients remain functional. | VER-0488: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement resolver access, firewall, rate-limit, and abuse controls". | M | RSK-0007; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 33 — Wave 7 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 35 | `TSK-0378` — Implement privacy-safe per-device ClientID configuration delivery mechanism | Network Engineering | TSK-0419 | ACC-0378: Each device receives a high-entropy opaque persistent ClientID and valid approved encrypted-DNS configuration; delivery is ownership-checked, minimal, revocable/replaceable, contains no admin credential or unnecessary child data, and supports safe retry without duplicate clients. | VER-0378: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement privacy-safe per-device ClientID configuration delivery mechanism". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 34 — Wave 8 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 53 | `TSK-0367` — Implement minimal parent/device datastore and ownership model | Software Engineering | TSK-0377; TSK-0232 | ACC-0367: Schema stores only approved parent/device metadata; every CRUD path enforces authenticated parent ownership; opaque IDs are used; cross-parent/IDOR tests fail closed; concurrency/deletion constraints are enforced. | VER-0367: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement minimal parent/device datastore and ownership model". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 58 | `TSK-0373` — Implement parent account profile, logout, revocation and deletion orchestration | Software Engineering | TSK-0377 | ACC-0373: Account exposes only approved minimal metadata; logout/session revocation works; deletion requires appropriate reauthentication/confirmation, initiates own-data/device cleanup, handles provider failure safely and produces privacy-safe completion evidence without retaining deleted content. | VER-0373: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement parent account profile, logout, revocation and deletion orchestration". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 61 | `TSK-0394` — Implement Google sign-in, sign-out and authenticated dashboard-entry UI | Frontend Engineering | TSK-0377; TSK-0396 | ACC-0394: Responsive/accessibility checks pass for sign-in, loading, provider failure, session expiry and sign-out; no password/SMS UI exists; privacy/data-use copy is accurate and successful authentication enters the correct parent dashboard. | VER-0394: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement Google sign-in, sign-out and authenticated dashboard-entry UI". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 35 — Wave 8 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 71 | `TSK-0414` — Implement DNS health probes, synthetic checks, and capacity signals | SRE/Operations | TSK-0420; TSK-0541 | ACC-0414: Checks exercise allowed/blocked resolution without real user domains, run from relevant paths, alert on defined failure/latency, and show capacity/headroom against the approved model. | VER-0414: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement DNS health probes, synthetic checks, and capacity signals". | M | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 36 — Wave 8 — Operations, observability, resilience and incident response

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 37 | `TSK-0447` — Implement and test DNS configuration backup and restore | SRE/Operations | TSK-0420 | ACC-0447: Backup scope excludes prohibited data; encryption/access/retention are configured; restore to a clean environment succeeds; service/config/verification tests pass; recovery time is recorded. | VER-0447: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement and test DNS configuration backup and restore". | S | RSK-0048; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 37 — Wave 8 — Protection Map and safeguard guidance

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 28 | `TSK-0382` — Implement native device safeguard guidance flow | Frontend Engineering | TSK-0374; TSK-0397 | ACC-0382: Supported paths use correct versioned content; skip/already-configured and errors work; no system verification is falsely claimed; screenshots/labels are accessible and maintainable. | VER-0382: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement native device safeguard guidance flow". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 38 — Wave 9 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 62 | `TSK-0387` — Implement dashboard shell, empty state and parent-owned device cards | Frontend Engineering | TSK-0394; TSK-0367 | ACC-0387: Dashboard renders only authenticated parent-owned devices; empty/loading/error states are polished; nickname/platform/protection summary uses approved minimal data; raw AdGuard identifiers/admin concepts are not exposed unnecessarily. | VER-0387: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement dashboard shell, empty state and parent-owned device cards". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 39 — Wave 9 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 54 | `TSK-0362` — Implement restricted server-side AdGuard API adapter and credential isolation | Software Engineering | TSK-0367; TSK-0418; TSK-0410 | ACC-0362: Adapter exposes only typed allowlisted client/setting operations, validates all inputs and AdGuard responses, uses bounded timeouts/retries, keeps admin secret server-side/restricted, cannot proxy arbitrary /control paths and emits no secret/client browsing data in errors/logs. | VER-0362: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement restricted server-side AdGuard API adapter and credential isolation". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 72 | `TSK-0415` — Implement AdGuard, filter, OS, and certificate update/rollback procedure | Network Engineering | TSK-0414; TSK-0447 | ACC-0415: Procedure identifies cadence/source, CI/ephemeral or otherwise approved pre-production tests, privacy/config regression checks, backup, authority, rollout, health observation, rollback, and evidence retention; one dry run succeeds. | VER-0415: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement AdGuard, filter, OS, and certificate update/rollback procedure". | M | RSK-0004; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |
| 74 | `TSK-0540` — Create DNS outage, false-positive, abuse, privacy, and compromise runbooks | SRE/Operations | TSK-0488; TSK-0414; TSK-0447 | ACC-0540: Runbooks have trigger, severity, first actions, data-minimising diagnostics, decision owner, rollback/fail-safe, communication, deletion, recovery verification, and postmortem requirements. | VER-0540: Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence. | Versioned artifact, decision, configuration, result, or evidence record for "Create DNS outage, false-positive, abuse, privacy, and compromise runbooks". | M | RSK-0006; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 40 — Wave 9 — Protection Map and safeguard guidance

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 29 | `TSK-0383` — Implement one relevant external-service safeguard flow | Frontend Engineering | TSK-0374; TSK-0382 | ACC-0383: Selection/routing matches requirements; content version is correct; parent confirmation remains distinct from verification; unsupported/irrelevant states do not create artificial tasks. | VER-0383: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement one relevant external-service safeguard flow". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 41 — Wave 10 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 55 | `TSK-0365` — Implement high-entropy ClientID generation and idempotent device provisioning | Software Engineering | TSK-0362; TSK-0378 | ACC-0365: One approved parent device maps to exactly one intended AdGuard persistent client; ClientID is high-entropy/opaque and never authorization; creation is idempotent/reconcilable; correct DoH endpoint is produced; explicit ignore_querylog/ignore_statistics privacy settings are applied and verified. | VER-0365: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement high-entropy ClientID generation and idempotent device provisioning". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 42 — Wave 10 — Accountless public journey

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 30 | `TSK-0337` — Implement Protection Map, gaps, completion, and optional save/output UI | Frontend Engineering | TSK-0371; TSK-0381; TSK-0383 | ACC-0337: Protection Map data contract works for anonymous journey state and, when the optional parent account is used, for the minimum authorised parent/device ownership record; verified vs parent-confirmed evidence remains separate; no browsing/query/activity history or unrestricted DNS administration is exposed. | VER-0337: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement Protection Map, gaps, completion, and optional save/output UI". | M | RSK-0002; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 43 — Wave 11 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 56 | `TSK-0363` — Implement approved curated per-device protection controls | Software Engineering | TSK-0365 | ACC-0363: Only G-05-approved parent-understandable controls are exposed and mapped deterministically to AdGuard client settings; ownership is checked on every change; privacy flags remain enforced; unsupported combinations fail safely; changes are auditable without activity history. | VER-0363: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement approved curated per-device protection controls". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 44 — Wave 11 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 64 | `TSK-0385` — Implement add-device, provisioning and DNS setup flow | Frontend Engineering | TSK-0387; TSK-0365; TSK-0378 | ACC-0385: Parent can name/select supported platform, provision one device, receive correct setup/configuration guidance, verify/retry safely and understand limitations; duplicate submissions do not create duplicate clients and no admin credential appears client-side. | VER-0385: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement add-device, provisioning and DNS setup flow". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 45 — Wave 11 — Privacy, transparency, support and product events

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 31 | `TSK-0391` — Publish versioned setup, troubleshooting, removal, and privacy help | Content | TSK-0323; TSK-0337 | ACC-0391: Every common support category has verified steps, applicability/version, expected result, escalation, last-reviewed date, and owner; no unsafe diagnostic instruction exists. | VER-0391: Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence. | Versioned artifact, decision, configuration, result, or evidence record for "Publish versioned setup, troubleshooting, removal, and privacy help". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 46 — Wave 12 — Privacy, transparency, support and product events

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 32 | `TSK-0393` — Implement contextual help, support contact, and structured case intake | Frontend Engineering | TSK-0369; TSK-0391 | ACC-0393: All critical errors expose a relevant self-service path and escalation; case fields match schema; consent/retention/contact text is accurate; success/confirmation works accessibly. | VER-0393: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement contextual help, support contact, and structured case intake". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 47 — Wave 12 — Protection Map and safeguard guidance

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 66 | `TSK-0390` — Implement truthful device protection status and per-device Protection Map | Frontend Engineering | TSK-0385; TSK-0371 | ACC-0390: UI distinguishes configured/verified/parent-confirmed/action-needed/not-covered/uncertain states exactly per frozen evidence rules, never infers continuous protection it cannot prove, and shows material DNS/app/VPN/Private Relay limits at the right moment. | VER-0390: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement truthful device protection status and per-device Protection Map". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 48 — Wave 12 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 57 | `TSK-0364` — Implement reinstall, revoke, remove, reset and replacement lifecycle | Software Engineering | TSK-0365; TSK-0363 | ACC-0364: Reinstall preserves intended ownership safely; revoke/remove/replacement disposition the old ClientID/client as designed; stale/duplicate mappings are reconciled; user sees truthful protection consequence and failed/partial operations are recoverable. | VER-0364: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement reinstall, revoke, remove, reset and replacement lifecycle". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 49 — Wave 13 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 67 | `TSK-0389` — Implement approved curated protection controls UI | Frontend Engineering | TSK-0390; TSK-0363 | ACC-0389: Only approved simple controls are shown with plain-language effect/limitations; changes are ownership-checked server-side, have loading/error/revert states and never expose raw policy editor, query history or comprehensive AdGuard administration. | VER-0389: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement approved curated protection controls UI". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 50 — Wave 13 — DNS/AdGuard service and verification

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 59 | `TSK-0241` — Implement account deletion cascade across app/device/AdGuard/auth state | Privacy Engineering | TSK-0373; TSK-0364; TSK-0242 | ACC-0241: Deletion/revocation sequence removes or expires app/account/device mappings and associated AdGuard clients according to the approved retention model, revokes authentication state as supported, handles partial failures with reconciliation, and retains only lawful minimal audit evidence without deleted content. | VER-0241: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement account deletion cascade across app/device/AdGuard/auth state". | M | RSK-0001; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 51 — Wave 13 — Operations, observability, resilience and incident response

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 70 | `TSK-0392` — Implement minimal service-status and incident communication surface | Frontend Engineering | TSK-0541; TSK-0393 | ACC-0392: If triggered, operators can publish/update/resolve factual incidents with affected component/time/impact/action and no sensitive detail; before trigger, no separate public status service is required. | VER-0392: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement minimal service-status and incident communication surface". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A4 | DEFERRED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 52 — Wave 13 — Configuration delivery, verification, recovery/removal

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 65 | `TSK-0388` — Implement reinstall, revoke, remove and replacement UI | Frontend Engineering | TSK-0385; TSK-0364 | ACC-0388: Parent can safely reinstall, revoke/remove or replace a device with clear confirmation/consequences, truthful post-action status, recoverable errors and support path; stale ClientID is never displayed as active protection after successful revocation. | VER-0388: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement reinstall, revoke, remove and replacement UI". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 53 — Wave 14 — Optional parent account/session/device management

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 63 | `TSK-0384` — Implement account settings, sign-out and account-deletion UI | Frontend Engineering | TSK-0387; TSK-0241 | ACC-0384: UI exposes minimal account identity, sign-out and deletion; deletion explains affected devices/protection/data, requires appropriate confirmation/reauthentication and shows only verified completion/recovery states. | VER-0384: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement account settings, sign-out and account-deletion UI". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 54 — Wave 14 — Operations, observability, resilience and incident response

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 60 | `TSK-0366` — Implement safe retry and reconciliation for auth/datastore/AdGuard partial failures | Software Engineering | TSK-0365; TSK-0363; TSK-0364; TSK-0241 | ACC-0366: Timeout/duplicate/partial-create/update/delete/provider-outage scenarios converge to a documented safe state; no orphan can grant access or silently claim protection; retries are bounded/idempotent; operator/user recovery evidence is testable. | VER-0366: Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria. | Versioned artifact, decision, configuration, result, or evidence record for "Implement safe retry and reconciliation for auth/datastore/AdGuard partial failures". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Slice 55 — Wave 15 — Localization, accessibility and hardening

| Order | Task | Owner | Dependencies | Acceptance | Verification / tests | Artifact | Size | Risk | Release target | Authority | Plan status |
|---:|---|---|---|---|---|---|:---:|---|---|---|---|
| 68 | `TSK-0386` — Polish and harden dashboard responsive, accessibility and failure states | Frontend Engineering | TSK-0387; TSK-0385; TSK-0390; TSK-0389; TSK-0388; TSK-0384 | ACC-0386: Supported mobile/desktop browsers pass responsive, keyboard, screen-reader, focus, contrast and text-resize checks; auth/AdGuard/datastore/offline/error states provide safe recovery; interface remains simple/direct and critical paths meet defined performance targets. | VER-0386: Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence. | Versioned artifact, decision, configuration, result, or evidence record for "Polish and harden dashboard responsive, accessibility and failure states". | M | RSK-0045; priority MEDIUM; critical-path NO | Development → Feature Complete | AUTO_ALLOWED / A3 | PLANNED |

### Slice checkpoint

- Execute only tasks whose current hard dependencies, gates, triggers, interfaces, executor/access, security/privacy constraints, and Action Authority are satisfied.
- Verify each task against its canonical acceptance/verification contract before any PASS state.
- Recompute eligibility after every durable state mutation; do not treat slice membership as execution authorization.

## Coverage checkpoints required before LG-07

- Accountless public/setup journey and configuration delivery/verification are represented.
- Optional authentication/session, parent/device ownership persistence, dashboard/device management, deletion/recovery are represented without making login mandatory.
- AdGuard/DNS typed integration, privacy-minimal state/logging, Protection Map truth, native safeguard and relevant external-service guidance are represented.
- Troubleshooting, removal/recovery, security/privacy negative tests, CI/release/recovery, observability/support/operations are represented.
- No L6 task is marked PASS by this planning artifact. `TSK-0516`, `TSK-0047`, `TSK-0587`, `TSK-0051`, and later gates retain their own acceptance boundaries.

## Execution handoff

After TSK-0048 acceptance, create/accept TSK-0516 master verification and acceptance plan, then TSK-0047 release/checkpoint/rollback plan, while independently completing any other eligible L5 prerequisites. L6 build begins only after LG-07 is actually PASS under current authority.
