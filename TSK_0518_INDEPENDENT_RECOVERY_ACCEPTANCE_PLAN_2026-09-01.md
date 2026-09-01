# TSK-0518 — Independent recovery acceptance plan

**Task:** TSK-0518  
**Acceptance:** ACC-0518  
**Verification:** VER-0518  
**Evidence:** EVD-0518  
**Plan version:** 1.0.0  
**Date:** 2026-09-01  
**Owner:** QA / Release Acceptance  
**Authority:** A3 / AUTO_ALLOWED  
**Status:** candidate frozen acceptance plan pending independent repository verification

## 1. Purpose and decision boundary

This plan defines the independent acceptance system for the UseSafeWeb AdGuard/DNS deployment and recovery path. It consumes the current TSK-0446 recovery contract and prevents the Cloud/Platform producer, its local environment, or artifact existence from self-certifying recovery PASS.

TSK-0518 does **not** execute a clean-server recovery, provision Azure, expose a public resolver, activate users, or claim the approximately-30-minute RTO has been achieved. It defines what later independent target-environment evidence must prove.

Current governing inputs:

- current `LG-06` PASS, which unlocks L5;
- current `TSK-0446` PASS and `infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md` version `1.0.0`;
- current `TSK-0413` privacy-first DNS desired-state bundle version `1.0.0`;
- `REQ-0065`, `REQ-0066`, `RSK-0050`, `CON-0023`, `CON-0029`;
- `INT-0017` Verified release to operations and the recovery-specific producer-to-QA interface `INT-0025`;
- owner-approved `DEC-0016` privacy semantics.

Higher/current authority always wins. A later source change invalidates only the affected evidence and requires targeted re-verification; it never creates PASS by inference.

## 2. Independence model — producer-only self-certification is prohibited

### Roles

- **Producer:** Cloud / Platform Engineering (`PKG-09`) creates the deployment/recovery system and may provide producer test outputs.
- **Acceptance owner:** QA / Release Acceptance (`PKG-12`) owns the acceptance result.
- **Independent executor/verifier:** a QA-owned workflow/runner or separate authorized verifier executes/observes the exact candidate and target. It may use producer artifacts as immutable inputs, but must not rely on the producer's PASS assertion.
- **Operations consumer:** SRE / Operations (`PKG-13`) receives only an independently accepted version through `INT-0017`.

### Mandatory independence rules

1. Producer-generated logs, unit tests, screenshots, local runs, or declarations are **supporting evidence only**; none can independently close a target criterion.
2. Final target acceptance requires independent execution or observation against the exact candidate commit/config on the exact approved target class.
3. The independent run must capture its own environment identity, commands/tests, results, timestamps, and evidence hashes or immutable job references.
4. The acceptance owner must be able to reproduce the result from durable evidence without hidden chain-of-thought or private model reasoning.
5. If producer and verifier are the same human/AI session, a separate deterministic QA-owned workflow/runner must reproduce the material observations; a second prose assertion is not independence.
6. The producer must not mutate the candidate during the acceptance run. Any candidate/config/version change invalidates the affected run and requires a new immutable candidate identity.
7. A local/container/mock-only result cannot satisfy a criterion that requires the owner-provided clean Ubuntu target, network exposure, TLS, DNS, backup/restore, restart, timing, or external health.
8. Missing, ambiguous, redacted-beyond-reproducibility, wrong-version, or wrong-target evidence is a blocking evidence failure, not a reason to infer success.

## 3. Exact candidate and target identity required for every acceptance run

Every run must record, without secrets:

- repository and branch;
- exact source/release commit SHA;
- recovery-system version and hashes of material scripts/templates;
- TSK-0413 bundle version and checksum identity;
- TSK-0446 recovery-contract version/hash;
- Ubuntu version/image facts for the target;
- target role (`AdGuard/DNS`), region/exposure evidence supplied or observed after owner handoff;
- installed AdGuard Home version and schema;
- DNS/TLS endpoint identity;
- independent workflow/run/job/verifier identity;
- UTC start/stop plus elapsed duration for timed runs;
- test-suite version/hash;
- deviations and final disposition.

No PASS may be carried forward across a changed candidate, changed privacy/filter/upstream/TLS desired state, material OS/AdGuard change, or target-class mismatch without explicit impact review and required re-execution.

## 4. Evidence classes

| Class | Meaning | Can satisfy a target acceptance row? |
|---|---|---|
| `DT` Direct target evidence | Independently observed on the exact owner-provided clean/approved target or external network against the exact candidate | **Yes** |
| `IR` Independent repository/CI evidence | Independent deterministic verification of exact source/config/artifacts | Yes for source/config requirements; **not** a substitute for target behavior |
| `PE` Producer evidence | Producer unit/integration/local outputs | Supporting only |
| `DO` Durable observation | Immutable cloud/job/check/commit/blob/read-back or independently captured target output | Yes when it directly proves the criterion |
| `IN` Inference | Human/AI reasoning without direct durable proof | **Never** |

A criterion whose required evidence class includes `DT` cannot PASS from `IR` or `PE` alone.

## 5. Severity and blocking rules

### Evidence blocker `EB`

Any missing applicable criterion evidence, wrong candidate/target, producer-only evidence, unverified redaction, broken evidence link/hash, or hidden-reasoning dependency is **BLOCKING regardless of defect severity**. This directly controls `RSK-0050`.

### `S1 — Critical` — always blocking

Examples: secret/private-key exposure; public/unauthenticated admin surface; persistent raw query/file logging; identifiable browsing/client history; ECS enabled contrary to baseline; wrong resolver/upstream/endpoint identity; invalid TLS trust/hostname; unsafe partially exposed service; corrupted/untrusted recovery input; recovery cannot produce a trustworthy operating state.

Disposition: fail acceptance, keep/return service disabled or uncertain as applicable, correct root cause, and fully retest affected controls plus regression dependencies.

### `S2 — High` — always blocking for recovery acceptance

Examples: required clean deployment/restore fails; approved filter or allowlist state is wrong; restart/startup fails; repeat execution is harmful; safe drift is not repaired or unsafe drift is not detected; required failure-injection/rollback path is nondeterministic; external encrypted-DNS health fails; backup/restore cannot reproduce safe state; measured RTO exceeds the current accepted approximately-30-minute target without an authorised current disposition.

Disposition: no recovery PASS; correct and rerun affected target tests. No numeric tolerance around “approximately 30 minutes” is invented by QA; a result above 30:00 is a blocking deviation until current governing authority explicitly accepts a different threshold/disposition.

### `S3 — Medium` — conditionally nonblocking only if it does not weaken an applicable criterion

Examples: noncritical diagnostic ergonomics or evidence presentation issue where direct proof remains complete and reproducible.

Disposition: may remain open only with impact, workaround, owner, due/review point and explicit disposition allowed by the current gate/task. It cannot waive an ACC, privacy/security control, recovery correctness, or required evidence.

### `S4 — Low`

Cosmetic/formatting issue with no effect on correctness, reproducibility, security/privacy, operation or evidence interpretation. Track if useful; nonblocking.

### Global PASS rule

Recovery acceptance is PASS only when every applicable mapped row is directly proven with the required evidence class, there is no `EB`, `S1`, or `S2` finding, no unresolved critical/high control failure, and every permitted lower finding is explicitly dispositioned. Artifact existence, “works locally,” or producer confidence is never sufficient.

## 6. Recovery requirement-to-evidence matrix

The matrix below is the minimum current recovery acceptance surface. Rows are independently dispositioned; one passing row cannot compensate for another missing row.

| ID | Recovery requirement | Minimum independent evidence | Evidence class | Default failure severity/block |
|---|---|---|---|---|
| `RA-01` | Owner-handoff target is a supported fresh Ubuntu 24.04 LTS AdGuard/DNS VM; Azure control-plane provisioning remains owner-managed | Target OS/role identity, handoff prerequisites, region/exposure observation, no preinstalled hidden recovery state | `DT+DO` | `EB/S2` |
| `RA-02` | Exact source, TSK-0413 bundle and TSK-0446 contract are immutable and trusted | Commit, hashes, bundle `SHA256SUMS`, bundle self-verifier, contract/test-plan version | `IR+DO` | `EB/S1` |
| `RA-03` | Prerequisites/packages install deterministically and unsupported states fail closed | Fresh-host transcript, package/source identities, negative unsupported-version check where safe | `DT+DO` | `S2` |
| `RA-04` | AdGuard Home is exactly compatible with current baseline: `v0.107.79`, schema `34`, official tag commit expectation | Installed version/schema output plus source/config compatibility verifier | `DT+IR` | `S1/S2` |
| `RA-05` | Protected configuration/secrets are acquired externally and final safe-field projection matches TSK-0413 | Secret-redacted input-path evidence, permissions, safe projection diff, checksum/self-verifier; no secret in Git/logs | `DT+IR+DO` | `S1` |
| `RA-06` | Plain DNS/admin listeners remain private; public exposure is limited to approved encrypted-DNS surface | Listener/socket/firewall/NSG observation after handoff, external port tests, admin access negative test | `DT+DO` | `S1` |
| `RA-07` | DNS desired state uses only `https://dns10.quad9.net/dns-query`; ECS off; client-IP anonymization on | Safe config/API projection and functional upstream verification without query-history capture | `DT+IR` | `S1` |
| `RA-08` | Privacy baseline matches DEC-0016/TSK-0413: persistent query/file logging off; identifiable per-client statistics/history excluded; only minimum anonymized aggregate operational statistics at `1d`; browsing/query/activity history prohibited | Safe config projection, storage/path inspection, negative prohibited-field/history checks, retention setting | `DT+IR+DO` | `S1` |
| `RA-09` | Public service identity is `dns.usesafeweb.com`, DoH is `https://dns.usesafeweb.com/dns-query`, and applicable DoT/Private DNS semantics work | External-network encrypted-DNS probes plus endpoint/hostname outputs | `DT+DO` | `S1/S2` |
| `RA-10` | TLS uses approved same-host path-restricted proxy topology; chain/hostname/validity are correct; private key remains protected; AdGuard internal TLS stays disabled | External TLS handshake/chain/hostname evidence, service topology/listener inspection, permissions/secret scan | `DT+IR+DO` | `S1` |
| `RA-11` | Initial filtering is exactly one official AdGuard DNS filter; versioned initial allowlist/user rules are empty | Safe config projection, filter source/hash/reference, allowed-domain and blocked-domain regression outcomes | `DT+IR` | `S1/S2` |
| `RA-12` | Allowed resolution, blocking behavior and external encrypted-DNS health are functionally correct without capturing real child browsing data | Synthetic/privacy-safe regression set, external resolution/block results, health result | `DT+DO` | `S2` |
| `RA-13` | Startup/restart recovers accepted state without a public unsafe partial window | Controlled restart test, service ordering/status, post-restart full critical invariant subset | `DT+DO` | `S1/S2` |
| `RA-14` | First run, repeat run, partial prior state, approved config change and drift behavior are idempotent/safe | Independent execution set proving no harmful duplicate mutation, safe repair, unsafe-drift detection and deterministic state | `DT+DO` | `S2` |
| `RA-15` | Representative network/package/certificate/config/service/permission/disk/interruption failures fail safely and have bounded retry/rollback/resume | Failure-injection matrix, exit/error states, target before/after observations, no secret/unsafe exposure | `DT+DO` | `S1/S2` |
| `RA-16` | Backup/restore inputs exclude prohibited data and a clean restore reproduces current safe desired state | Protected backup scope metadata, clean restore result, safe projection, prohibited-data absence, encryption/access/retention evidence | `DT+DO` | `S1/S2` |
| `RA-17` | Rollback/emergency recovery returns to a known-good safe state or explicitly remains disabled/uncertain | Intentional failed/superseded scenario, rollback target/version, post-rollback critical checks, ambiguous-effect no-blind-replay proof | `DT+DO` | `S1/S2` |
| `RA-18` | Complete service restoration is independently timed against the current approximately-30-minute RTO contract | Independent UTC start/stop, elapsed seconds, transcript, exact candidate/target, all stop-condition checks, deviation record | `DT+DO` | `EB/S2` |
| `RA-19` | Evidence itself is privacy/security safe and reproducible | Secret scan, prohibited-history scan, evidence index/hash/read-back, exact environment/release links | `IR+DO` | `EB/S1` |
| `RA-20` | Operations handoff identifies exact accepted version, recovery/rollback requirements and known residual findings | QA acceptance report, exact manifest, known-risk/deviation register and `INT-0017` handoff checklist | `IR+DO` | `EB/S2` |

## 7. Required independent execution suites

### Suite A — provenance and immutable candidate

- Freeze exact candidate commit and material hashes before target testing.
- Verify TSK-0413 checksum set and current recovery contract.
- Reject any candidate drift during the run.
- Record test-plan version and QA verifier identity.

### Suite B — clean-server deployment/recovery

- Start only after owner-provided fresh Ubuntu 24.04 LTS handoff prerequisites are established.
- Execute the approved direct-host recovery path without assuming pre-existing AdGuard/config/filter/TLS/firewall state.
- Capture deterministic exit codes and privacy-safe transcript.
- Confirm unsupported/incompatible state fails closed.

### Suite C — current desired-state/configuration invariants

Independently verify the final state against TSK-0413, including:

- Quad9 `dns10` DoH only;
- ECS off;
- client-IP anonymization on;
- query logging off and file logging off;
- **minimum anonymized aggregate operational statistics enabled with `1d` retention**, while identifiable per-client statistics/history remain excluded;
- official AdGuard DNS filter only initially;
- empty versioned allowlist/user rules;
- private authenticated admin binding;
- no browsing/query/activity history.

Any older source saying simply “statistics off” is not allowed to override current DEC-0016/TSK-0413. If a later task/acceptance row still encodes that stale meaning, it must be reconciled before that later task can PASS.

### Suite D — DNS/TLS/network/external health

Use independent external-network tests to prove endpoint identity, TLS trust/hostname, DoH and applicable DoT/Private DNS behavior, allowed and blocked synthetic domains, and no unintended public admin/plain-DNS exposure.

### Suite E — privacy/security/secret negative tests

Verify no secret/private key/password hash/token/raw DNS history/browsing history/identifiable client-history artifact appears in Git, test evidence or unintended storage paths. Verify permissions and public exposure. Any detected leak is S1 and requires containment plus fresh evidence after correction.

### Suite F — idempotency and drift

Exercise first run, repeat run, partial prior state, approved current config change, safe drift and unsafe divergence. Independent evidence must distinguish unchanged/no-op, repaired state, blocked unsafe state and rollback behavior.

### Suite G — failure injection and rollback

Inject representative failure classes only in the approved non-user acceptance environment: network, package/source, certificate/TLS, configuration, service, permission, disk/resource and interruption. Verify deterministic failure, bounded retry, safe rollback/resume and absence of partial unsafe public service.

### Suite H — backup/restore

Use only protected, approved backup/recovery inputs. Prohibited query/history data is not part of the backup. Restore into a clean supported environment, then reconcile final safe fields to the current TSK-0413 desired state and rerun critical DNS/TLS/privacy/filter/health checks.

### Suite I — timing

Start the RTO clock immediately before the first recovery/deployment command after owner-handoff prerequisites. Do not pause it for a missing input discovered after start. Stop only after every applicable stop-condition check and external encrypted-DNS health passes. Record UTC start/stop and elapsed seconds. Do not infer or predeclare ~30-minute attainment.

### Suite J — evidence and handoff

Create a machine/human-readable evidence index mapping `RA-01` through `RA-20` to exact immutable artifacts, direct observations, run/job IDs, target identity, severity and disposition. Operations receives only the accepted exact version plus known residuals/recovery/rollback requirements.

## 8. Evidence record schema

Every `RA-*` result must record at least:

- requirement ID;
- result: `PASS | FAIL | BLOCKED | NOT_APPLICABLE`;
- exact candidate/release commit;
- exact config/bundle/test-plan version;
- target/environment identity;
- evidence class (`DT/IR/PE/DO`);
- immutable evidence reference/hash/run-job ID;
- independent executor/verifier;
- UTC timestamp/time window;
- severity if failed;
- deviation/root cause;
- corrective action/retest reference;
- final disposition.

`NOT_APPLICABLE` requires explicit current-authority justification and evidence of exclusion; it is never a shortcut for a missing test.

## 9. PASS algorithm

A QA acceptance result may be recorded as PASS only when all of the following are true:

1. exact current candidate, config/bundle and target identity are frozen and evidenced;
2. all currently applicable `RA-01` through `RA-20` rows have durable direct/reproducible evidence;
3. every row requiring `DT` has independent target evidence, not producer/local-only output;
4. there is no `EB`, `S1`, or `S2` finding;
5. every permitted lower finding is explicitly dispositioned without waiving a current ACC/control;
6. privacy/security evidence matches current DEC-0016/TSK-0413, including the approved `1d` anonymized aggregate operational statistics semantics;
7. recovery timing is measured from the TSK-0446 start/stop boundary and does not receive invented tolerance;
8. evidence contains no prohibited secrets or DNS/browsing/client-history data;
9. contrary current evidence has been searched/reconciled;
10. the acceptance owner records the exact release/config/environment and independent verifier;
11. GitHub evidence/state writes are read back and exact hashes/commit identities are verified;
12. no downstream gate/task PASS, production activation, or user readiness is inferred beyond the evidence actually proven.

If any rule fails, disposition is `TODO`, `WAITING`, or `BLOCKED` according to the actual condition; never PASS.

## 10. Planned evidence producers — not automatic PASS

The following current tasks are expected to contribute evidence when their own gates/dependencies become eligible; listing them does not mark them complete or create new dependencies:

- `TSK-0456` trusted-source/version/checksum/rollback inputs;
- `TSK-0457` secure secret/input handling;
- `TSK-0462` first/repeat/partial/drift behavior;
- `TSK-0459` representative failure injection;
- `TSK-0460` independent timed clean-server restoration;
- `TSK-0447` DNS configuration backup/restore;
- `TSK-0519` deployment rollback/environment recovery where applicable;
- `TSK-0461` final authoritative recovery-path acceptance;
- later `TSK-0482` recurring re-acceptance after material changes.

Producer task PASS is not sufficient by itself; TSK-0518 acceptance rules still require the correct independent evidence class for the criterion.

## 11. Reopen / invalidation triggers

Re-run affected independent acceptance after any material change to:

- Ubuntu target class;
- AdGuard version/schema or installation source;
- TSK-0413 DNS/privacy/filter/upstream baseline;
- recovery scripts/modules/config merge behavior;
- network/firewall/listener topology;
- TLS termination/certificate mechanism;
- backup/restore format or protected-input mechanism;
- secret handling;
- failure/rollback behavior;
- RTO threshold/measurement boundary;
- test suite or evidence semantics where prior proof no longer reproduces.

A current incident, security/privacy finding, or target observation that contradicts earlier evidence reopens the affected acceptance regardless of historical PASS.

## 12. TSK-0518 acceptance mapping

`ACC-0518`: “Plan prevents producer-only self-certification and maps every recovery requirement to evidence and severity/blocking rules.”

This plan satisfies that contract by:

- separating producer, acceptance owner, independent executor/verifier and operations consumer;
- defining direct-target versus source/supporting evidence classes;
- making producer-only/local/artifact-only proof insufficient;
- mapping the complete current recovery surface in `RA-01` through `RA-20`;
- assigning minimum evidence and default blocking severity to every row;
- defining global `EB/S1/S2` blocking rules and lower-severity disposition;
- binding the matrix to the current TSK-0446 and TSK-0413 owner-approved privacy-first baseline;
- defining exact candidate/target/evidence schema, PASS algorithm and reopen triggers;
- explicitly refusing to infer any clean-server/RTO result that has not yet been executed independently.

## 13. Non-inference

This document is an acceptance **plan**. It does not prove a working deployment/recovery script, idempotency, a clean restore, failure recovery, live DNS/TLS health, backup recovery, production safety, or the ~30-minute RTO. Those outcomes require later direct target evidence under the exact gates and authorities of their tasks.
