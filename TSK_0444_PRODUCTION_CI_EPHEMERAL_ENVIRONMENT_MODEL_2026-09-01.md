# TSK-0444 — Production + CI/Ephemeral Environment Model and Conditional Staging Rule

**Version:** 1.0.0
**Date:** 2026-09-01
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness
**Task:** TSK-0444 — Record the production + CI/ephemeral environment model and conditional staging rule
**Acceptance:** ACC-0444 / VER-0444 / EVD-0444
**Authority:** current WBS; DEC-0016; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008
**Dependencies:** TSK-0355 current PASS; TSK-0411 current PASS; LG-06 current PASS
**Application architecture source:** `TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md`, blob `e9efc3b498040cc7e3cdd42a912359e41250d068`
**DNS topology source:** `TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md`, blob `8bd206e3832bafc5b8033dddd3e7913a5e01f7b6`
**DNS privacy/config source:** `infrastructure/adguard-server/tsk-0413-bundle-v1/`, version `1.0.0`; README blob `5a162a87dd2761ff5a0da587fa660549309a1404`; public-fragment blob `867ef7162c739106fa42af151cda145f6d16888e`; endpoints blob `fe1d1b2d5cff13f85eda96a28f90a40921ef4506`

## 1. Decision

Use **one live production environment**, backed by the two owner-provided Ubuntu 24.04 LTS VMs already frozen by REQ-0049/CON-0004:

1. one dedicated AdGuard/DNS VM; and
2. one separate web/application VM.

Use CI, local and disposable/ephemeral environments only for verification and build/test evidence. **Do not maintain a persistent staging environment by default.** A staging-like environment may be introduced only when a specific verified risk cannot be tested adequately with local/CI/ephemeral methods or a bounded production-safe mechanism, and only for the shortest justified period.

Under DEC-0054/CR-0007 there is no separate mandatory pilot or staging lifecycle. The WBS/ACC-0444 historical word **pilot** is therefore reconciled as the **initial bounded/ramped live-production validation mode after LG-09 PASS**, not as a second customer environment, second DNS identity, or extra gate.

No environment created or described by this task changes the owner-controlled Azure boundary, creates public production resources, or claims deployment has occurred.

## 2. Environment taxonomy

| ID | Environment / mode | Persistent? | Real users/data? | Purpose |
|---|---|---:|---:|---|
| PROD-DNS | Production DNS VM | Yes | Yes, only after applicable release/readiness authority | Live encrypted UseSafeWeb DNS service. |
| PROD-WEB | Production web/application VM | Yes | Yes, only after applicable release/readiness authority | Public site, accountless setup, optional account/session/dashboard, server-side integration. |
| PROD-RAMP | Bounded live-production validation/ramp | **Not a separate environment** | Yes, after LG-09 and applicable prerequisites | Limit exposure/cohort/traffic while observing live production behavior safely. |
| CI-SOURCE | GitHub-hosted source/build/test jobs | Ephemeral per job | **No** real child/participant/DNS browsing data | Static checks, unit/integration tests, plan/config verification, builds, artifact/checksum generation. |
| CI-TARGET | Governed self-hosted/target verification | Job-scoped | No new user dataset; target may be a real managed host only when task authority permits | Read-only/controlled target observation and exact-environment acceptance where source-only evidence is insufficient. |
| EPH-APP | Disposable application preview/test instance | Ephemeral | Synthetic/minimal test fixtures only | Browser/E2E/accessibility/failure/rollback verification before production. |
| EPH-DNS | Disposable isolated DNS test instance when required | Ephemeral | Synthetic DNS test cases only | Configuration parsing, upgrade/recovery/filter/TLS/abuse tests that must not touch live users. |
| STAGE-COND | Conditional staging-like environment | **Absent by default** | No live participant/customer data unless separately authorized by the controlling task/gate | Only a risk-specific temporary test boundary when ordinary CI/ephemeral evidence cannot safely prove acceptance. |

## 3. Production environment contract

### 3.1 PROD-DNS

**Purpose**

- provide the single public UseSafeWeb DNS production service;
- run the accepted AdGuard filtering/privacy configuration;
- support the bounded live-production validation/ramp after LG-09 without creating a second resolver environment.

**Data**

- ordinary DNS traffic is processed only as required to provide the service;
- persistent query logging and file query logging remain OFF;
- identifiable per-client statistics/history remain excluded;
- only anonymized aggregate operational statistics with 24-hour retention are allowed under DEC-0016/TSK-0413;
- client-IP anonymization remains ON wherever stored records can contain it;
- browsing/query/activity history is not a product, analytics, support, CI or recovery dataset.

**Access**

- public encrypted DNS only through the approved DoH/DoT boundary from TSK-0411;
- public UDP/TCP 53 remains closed;
- AdGuard plain DNS remains loopback-only;
- AdGuard administration remains authenticated, server-side and loopback-bound at `127.0.0.1:3000`;
- no browser/customer route receives an AdGuard admin credential or arbitrary `/control/*` access.

**Region**

- the initial child-linked DNS service is Azure **West Europe / Netherlands**;
- no US DNS node belongs to the initial path;
- actual Azure metadata must be verified from the handed-off VM before production acceptance.

**Endpoint**

- service identity: `UseSafeWeb DNS`;
- resolver hostname: `dns.usesafeweb.com`;
- DoH: `https://dns.usesafeweb.com/dns-query`;
- Android Private DNS / DoT hostname: `dns.usesafeweb.com`.

**Deployment**

- project automation starts only after the owner hands off the fresh Ubuntu 24.04 LTS VM;
- direct-host deployment/recovery is the default;
- the versioned TSK-0413 secret-safe bundle is the DNS desired-state input;
- secrets/private keys/admin credentials are externally injected and never committed;
- a release is not production-ready merely because configuration files exist.

**Cleanup / retention**

- the production VM is persistent;
- diagnostic exceptions are separate controlled actions, maximum 24 hours where explicitly authorized, followed by deletion proof;
- obsolete build/temp artifacts and prohibited history are not retained as recovery data.

**Cost**

- Azure remains the owner-managed hosting baseline;
- this task invents no numeric VM price or budget;
- actual production cost belongs to the current cost/resource tasks and must be recorded from current billing/pricing evidence;
- expensive HA/multi-node DNS is not introduced without evidence.

**Rollback / recovery**

- configuration rollback uses a previously verified versioned bundle/configuration;
- server failure uses the accepted direct-host recovery contract and approximately 30-minute recovery objective;
- unsafe/partial service remains disabled or explicitly uncertain until all DNS/privacy/TLS/health checks pass;
- rollback never restores browsing/query history because such history is outside the approved dataset.

### 3.2 PROD-WEB

**Purpose**

- one `/website` TypeScript + Next.js full-stack application serving public content, accountless setup, optional account/session/dashboard/device management, recovery and server-side integration.

**Data**

- accountless J0/J1 is minimum and short-lived as already frozen;
- optional persistent account/device state is limited to approved ownership/settings/lifecycle purposes;
- no browsing/query/activity history enters the application/account datastore, dashboard, CMS, analytics or support path.

**Access**

- public HTTPS for customer-facing routes;
- protected account/device operations require the approved server-session and server-side authorization boundary;
- AdGuard control, datastore credentials, Firebase Admin credentials, private keys and recovery secrets remain server-only.

**Region**

- the web/application VM is owner-provided and separate from the DNS VM;
- this task does **not** invent its Azure region; actual handed-off region and data-path compatibility must be verified before production use.

**Endpoint**

- the public product/domain remains UseSafeWeb.com under the frozen product identity;
- exact deployment-origin/runtime binding must be read from the eventual production deployment rather than invented by this architecture record;
- DNS service endpoints remain those owned by PROD-DNS and are not duplicated by the app environment.

**Deployment**

- direct-host self-hosting behind an HTTPS reverse proxy with a Node.js runtime;
- exact dependency versions, release artifact, lockfile, checksums and environment contract are pinned/tested when `/website` exists;
- immutable/versioned release artifacts are promoted only after their applicable gates/tests pass.

**Cleanup / retention**

- production application state follows the approved account/device retention/deletion contract;
- transient build/cache/test data is not turned into product history;
- deleted account/device data must not be silently resurrected by restore.

**Cost**

- actual Azure/application/provider costs are sourced by their owning cost/vendor tasks;
- no unpriced service is silently added by this environment model.

**Rollback / recovery**

- rollback restores the previous verified application artifact plus compatible configuration;
- account/provider/datastore/AdGuard failures degrade only their affected feature where safe; the accountless core remains available whenever its own dependencies are healthy;
- a rollback must not widen data collection or disable TSK-0413 privacy controls.

## 4. PROD-RAMP — bounded live-production validation is a mode, not an environment

After LG-09 PASS and all actually applicable legal/privacy/consent prerequisites, DEC-0054 permits the first real users directly on production using bounded/capped/ramped exposure.

`PROD-RAMP` therefore means controls such as:

- limited cohort/user count;
- limited traffic or feature exposure;
- stop/rollback thresholds;
- intensified privacy-safe health/reliability monitoring;
- fast disable/recovery capability.

It does **not** mean:

- a separate pilot VM;
- a staging DNS hostname;
- a second customer database;
- a second resolver identity;
- a pre-production participant study;
- an additional mandatory gate between LG-09 and live use.

All users in this mode are production users and all observations must be labelled as live-production evidence. No real-user evidence is inferred before that authority is reached.

## 5. CI-SOURCE environment

**Purpose**

- deterministic source/config/plan validation;
- unit/integration tests that do not need production targets;
- application builds, lint/type checks, secret scans, dependency/config checks, generated checksums and reproducible evidence.

**Data**

- repository sources and synthetic fixtures only;
- no real child browsing data, DNS query history, participant data, production account export or raw production logs;
- test fixtures must be fabricated/synthetic and privacy-safe.

**Access**

- default read-only repository access where mutation is unnecessary;
- narrowly scoped GitHub token only for governed writes when a workflow's task explicitly requires them;
- no production AdGuard admin credential, private key or broad Azure control-plane credential in ordinary source CI.

**Region**

- GitHub-hosted runner location is not treated as a controlled UseSafeWeb processing region or production evidence;
- location-sensitive/child-linked production processing must not be moved into hosted CI.

**Endpoint**

- no stable customer endpoint;
- public vendor/docs endpoints may be read only as the task permits;
- synthetic services are test-only and never published as `dns.usesafeweb.com` production.

**Deployment**

- ephemeral runner per job;
- checkout exact commit; pin exact action/dependency versions according to the applicable CI policy;
- no direct production promotion merely because CI is green.

**Cleanup**

- runner filesystem is disposable;
- any evidence artifact retained must contain only the minimum reproducible non-secret result;
- temporary secrets/files are removed with the job environment.

**Cost**

- use included/current GitHub runner capacity where available;
- no numeric cost is invented here;
- if new usage causes material/unbudgeted spend, the relevant owner-spend authority applies before commitment.

**Rollback**

- source-only CI has no customer runtime to roll back;
- failed jobs leave canonical production unchanged and must not mutate runtime PASS state.

## 6. CI-TARGET environment / execution mode

**Purpose**

- exact-target inspection where a source-only test cannot prove an acceptance criterion;
- bounded read-only or explicitly authorized reversible target checks on the correct host/environment.

**Data**

- minimum configuration/health evidence only;
- no raw DNS query history or customer browsing export;
- secrets are neither printed nor committed.

**Access**

- self-hosted runner/target access is used only when current task authority permits the exact action;
- target identity, environment and commit/config version are verified before an acceptance claim;
- a source-only hosted runner cannot substitute for target observation where acceptance requires the deployed environment.

**Region / endpoint**

- inherits the actual target host region and endpoint; both must be observed rather than assumed;
- target CI is not a second staging/customer environment merely because a runner is installed there.

**Deployment / cleanup / cost / rollback**

- default is inspection/test, not mutation;
- if a governed task authorizes a reversible target mutation, it uses stale-write/idempotency/rollback controls and rereads durable outcome;
- transient test material is removed after verification;
- no standing duplicate infrastructure is created solely to run CI.

## 7. EPH-APP — disposable application preview/test

**Purpose**

- browser/E2E, accessibility, state-transition, failure-path and release-artifact verification before production.

**Data**

- synthetic accounts/devices/journey state only;
- no real participant/child browsing data or production account copy;
- no DNS history dataset.

**Access**

- private/local/CI-only by default;
- if a temporary public preview is technically necessary, access is bounded, not indexed/advertised, carries no production secrets/data, and is destroyed after the test.

**Region / endpoint**

- region is test-infrastructure dependent and cannot satisfy production-region evidence;
- endpoint is ephemeral/non-customer and must never be published as the production origin or DNS service.

**Deployment**

- build exact candidate release from an exact commit/lockfile;
- inject test-only scoped secrets/config;
- exercise the same logical runtime contract without claiming production observation.

**Cleanup / cost / rollback**

- teardown immediately after the test/evidence window unless a specific active verification requires retention;
- no standing cost by default;
- rollback is destroy/recreate from the previous exact test artifact.

## 8. EPH-DNS — isolated disposable DNS test

**Purpose**

- AdGuard configuration parsing/version compatibility;
- filter/allowlist regression;
- DNS/TLS/abuse controls;
- recovery/upgrade/failure injection that would be unsafe or ambiguous on the live service.

**Data**

- synthetic controlled domains/test queries only;
- persistent query logging remains off unless a separately authorized diagnostic test explicitly requires otherwise, in which case the 24-hour maximum and deletion proof still apply;
- never import customer browsing/query history.

**Access / region / endpoint**

- isolated test boundary; no customer instructions point to it;
- no stable public `dns.usesafeweb.com` identity is created for it;
- location is test evidence only and does not substitute for West-Europe production-region proof.

**Deployment**

- use the exact TSK-0413 desired-state baseline plus test-only non-secret overrides that are explicitly enumerated;
- production secrets/private keys are not copied merely for convenience;
- differences from TSK-0413 are test fixtures, not new production policy.

**Cleanup / cost / rollback**

- destroy after the bounded test;
- zero standing infrastructure by default;
- material cost requires current approval authority;
- rollback is teardown/recreate, while any production rollout remains separately governed.

## 9. Conditional staging rule

Persistent staging is **ABSENT** on the current architecture.

A staging-like environment may be created only when all of the following are true:

1. a current task/acceptance criterion identifies a specific risk or integration behavior that cannot be adequately proven with local/CI/EPH-APP/EPH-DNS or a safer production-read-only check;
2. the staging environment materially reduces that risk rather than merely providing comfort or mirroring production by habit;
3. its exact purpose, expected evidence and deterministic exit/teardown condition are recorded before creation;
4. required data is synthetic/minimized by default; real user/participant data is prohibited unless separately authorized by the controlling gate/task and all applicable prerequisites;
5. secrets are externally injected, least privilege and separately scoped from production wherever technically possible;
6. it receives a clearly non-production endpoint/identity and cannot be mistaken for `dns.usesafeweb.com` production or the public UseSafeWeb customer service;
7. TSK-0413 privacy controls are preserved unless the test itself explicitly exercises a separately authorized diagnostic exception;
8. no public AdGuard administration or browsing-history path is introduced;
9. owner-provided Azure control-plane boundaries are respected; project automation does not create Azure resources unless explicit authority changes that boundary;
10. incremental cost is recorded before creation; material/unbudgeted spend follows its human authority;
11. rollback is defined before test execution; and
12. teardown occurs when the evidence is captured or the risk-specific exit condition is met.

A staging-like environment **does not create a permanent lifecycle stage or gate**. Repeated need for staging is evidence that the CI/ephemeral/recovery architecture should be improved or that a new explicit owner architecture decision may be required.

## 10. Owner-provided Azure VM boundary

REQ-0049 and CON-0004 remain exact:

- Azure is the hosting baseline;
- the owner manually provides two reachable fresh Ubuntu 24.04 LTS VMs;
- one VM is AdGuard/DNS and one is web/application;
- Azure control-plane provisioning/configuration is owner-managed;
- project automation begins after VM handoff;
- project verification must still inspect actual handed-off region, exposure, backup and security state before use;
- no task may silently create/configure Azure control-plane resources merely because it has host-level automation access.

TSK-0444 therefore defines the **runtime/environment contract after handoff**, not Azure subscription/VNet/NSG/VM creation.

## 11. INT-0014 — cloud runtime to application contract

The environment producer exposes a bounded deployment contract to the application/release work.

| Logical binding | Exposure | Current value/rule |
|---|---|---|
| Application release identity | Server/ops | Exact immutable release/commit/build identity; bound when `/website` is implemented. |
| Public application origin | Public | Must be the approved UseSafeWeb production origin read from deployment authority; not invented by TSK-0444. |
| DNS service name | Public | `UseSafeWeb DNS`. |
| DNS resolver hostname | Public | `dns.usesafeweb.com`. |
| DNS DoH URL | Public | `https://dns.usesafeweb.com/dns-query`. |
| AdGuard control origin/transport | Server only | Approved private transport to loopback-only administration; exact mechanism remains downstream and must not become a public proxy. |
| AdGuard admin credential | Secret/server only | External secret source; never Git/client bundle/evidence. |
| TLS/private-key material | Secret/server only | External certificate/secret path; never Git/client bundle/evidence. |
| Optional Firebase client configuration | Intentionally public subset only | Bound only after TSK-0356/current vendor architecture; public values do not include Admin credentials. |
| Firebase Admin credential/session signing material | Secret/server only | External secret source; downstream exact binding. |
| Ownership datastore connection/credential | Secret/server only | Downstream exact datastore selection; no browser exposure. |
| Environment class | Runtime/evidence | `production`, `ci`, or `ephemeral`; staging-like mode exists only under Section 9 justification. |

Exact environment-variable names and secret-provider implementation may be selected by their owning implementation tasks. Whatever names/products are used must preserve these exposure classes, current endpoint values and no-history/no-public-admin constraints.

### INT-0014 release invariant

A release may be promoted only when it deploys without an unapproved service/data flow and rollback is available. Environment differences must not silently change:

- accountless-core availability;
- persistent-data scope;
- AdGuard upstream/ECS/log/statistics/anonymization settings;
- public DNS/admin exposure;
- authentication requirement for core value;
- region rules for child-linked DNS;
- browsing/query/activity-history prohibition.

A producer change to this environment contract requires consumer-impact review and affected acceptance/regression evidence before release.

## 12. Cost model and anti-overbuild rule

This architecture intentionally has only two standing production VMs because REQ-0050 requires a lean initial topology and accepts approximately 30 minutes recovery/downtime rather than expensive HA absent evidence.

- CI/ephemeral environments have **zero standing infrastructure by default** and are created only for the evidence window.
- Persistent staging has zero standing cost because it is absent.
- No numeric Azure/GitHub/provider amount is asserted by TSK-0444; current sourced cost belongs to the cost/resource tasks.
- A new standing service, region, HA node, staging VM or paid testing product requires evidence that it materially improves an acceptance/risk boundary and must follow current spend/contract authority.

## 13. RSK-0048 disposition

`RSK-0048` remains **OPEN — critical control**. This environment model does not claim clean-server recovery has been executed merely because the recovery scope/design exists.

Controls contributed by TSK-0444:

- production is small and reconstructable: two owner-provided host roles, one DNS and one web/app;
- immutable/versioned inputs are kept separate from externally injected secrets;
- ephemeral destructive/failure-injection work is isolated from production where appropriate;
- no persistent staging drift or third environment must be recovered;
- rollback/recovery is required for production changes;
- TSK-0413 privacy configuration remains part of DNS recovery rather than an optional post-recovery step;
- unsafe partial service stays disabled/uncertain until health/privacy/security verification passes;
- the accepted approximately 30-minute DNS recovery objective remains visible rather than hidden by HA assumptions.

A later timed clean-server acceptance failure, secret leak, unsafe partial service or RTO miss reopens the relevant recovery/environment work.

## 14. ACC-0444 verification trace

| ACC-0444 element | Evidence in this model | Result |
|---|---|---|
| Pilot/production model | Legacy pilot wording reconciled to bounded `PROD-RAMP` inside the one production environment under DEC-0054 | SATISFIED UNDER CURRENT AUTHORITY |
| Production purpose/data/access | Sections 3-4 | SATISFIED |
| Production region | DNS fixed West Europe/Netherlands; web region deliberately read from handed-off reality | SATISFIED |
| Production endpoint | Exact DNS identity/DoH/DoT; application origin non-invented until deployment | SATISFIED |
| Production deployment | Direct-host, exact release/config, owner-handoff boundary | SATISFIED AT ARCHITECTURE BOUNDARY |
| Production cleanup/retention | Minimum data, no DNS history, diagnostic deletion, lifecycle retention | SATISFIED |
| Production cost | Lean two-VM topology; no invented number; source current cost downstream | SATISFIED AT ARCHITECTURE BOUNDARY |
| Production rollback | Previous verified app/config plus recovery contract; unsafe partial service fails closed | SATISFIED AT ARCHITECTURE BOUNDARY |
| CI environment | CI-SOURCE + CI-TARGET purpose/data/access/region/endpoint/deployment/cleanup/cost/rollback | SATISFIED |
| Ephemeral preview/test | EPH-APP + EPH-DNS complete environment contracts | SATISFIED |
| Persistent staging absent | Section 9; explicitly ABSENT by default | SATISFIED |
| Evidence-based staging trigger | 12-point conditional rule + teardown/exit condition | SATISFIED |
| Owner-provided VM boundary | Section 10 | SATISFIED |
| REQ-0049 / CON-0004 | Azure owner handoff, two VMs, no project control-plane provisioning | SATISFIED |
| REQ-0050 / CON-0005 | Lean one-node DNS, West Europe child-linked DNS, no US initial node, ~30m recovery model | SATISFIED |
| INT-0014 | Environment/runtime bindings, secret/exposure classes, promotion/rollback invariant | SATISFIED AT ARCHITECTURE BOUNDARY |
| TSK-0413 privacy baseline | Preserved in production, CI/ephemeral and conditional-staging rules | SATISFIED |

## 15. Deviations, unresolved implementation facts and non-inference

The following are intentionally not invented by TSK-0444:

- actual Azure VM IDs, addresses, NSGs/VNet topology, current web VM region or production billing amount;
- an already deployed `/website` release;
- the exact application public origin until its production deployment contract exists;
- exact environment-variable names, datastore product, Firebase Admin credential mechanism or secret-provider product;
- any persistent staging VM/endpoint;
- a separate pilot environment;
- production activation or real-user evidence;
- successful clean-server recovery timing merely from architecture documentation.

Those facts require their owning target/implementation evidence.

**No Azure control-plane provisioning, website/DNS deployment, LG-07/LG-08/LG-09, live-production activation, market launch, payment or real-user validation PASS is inferred by this environment model.**

## 16. Review record

- Review date: 2026-09-01.
- Responsible reviewer: ChatGPT Project Governor under A3 / AUTO_ALLOWED, subject to independent deterministic GitHub acceptance before runtime PASS.
- Exact source environment: canonical GitHub `main`, current WBS/registers, current TSK-0355/TSK-0411 accepted artifacts, current TSK-0413 bundle and current DEC-0054 production-only authority.
- Deviation/disposition: ACC-0444's inherited word `pilot` is retained for traceability but is superseded as an environment/lifecycle concept. It is satisfied by the bounded live-production `PROD-RAMP` mode after LG-09, with no separate persistent pilot/staging environment.
