# TSK-0406 — Conservative Filtering Policy Evidence

**Task:** TSK-0406 — Configure sensible baseline filtering policy  
**Acceptance:** ACC-0406  
**Verification:** VER-0406  
**Evidence:** EVD-0406  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Execution date (UTC):** 2026-08-27

## Authority and eligibility

The canonical WBS defines TSK-0406 as `A3`, `AUTO_ALLOWED`, HIGH priority, critical-path work. Its hard predecessors are `TSK-0407` and `TSK-0011`; both were satisfied before execution. TSK-0407 is directly evidenced PASS, and TSK-0011's publication/read-back condition is satisfied by the owner-frozen modular planning tree plus the verified CR-0001 publication/read-back state.

ACC-0406 requires all of the following:

1. a documented policy rationale;
2. a low-risk allowlist/exception path;
3. no unsupported “complete safety” promise; and
4. a versioned configuration.

The current package/requirements also require a conservative versioned baseline, allowed/blocked regression, exception and rollback evidence, the frozen AdGuard layer, exact Quad9 dns10/ECS-off behavior, and privacy-minimal operation.

## Existing project controls reused

This task did not create a parallel support or claims system. It reuses:

- `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md` for privacy-safe false-positive intake and the narrow/reversible exception workflow; and
- `PROTECTION_CLAIMS_CHECKLIST.md` for truthful DNS-scope claims and the explicit prohibition on complete-safety claims.

The support process requires synthetic reproduction where possible, the narrowest safe correction, no blanket disabling of filtering, retesting after an exception, truthful protection-state reporting, and no routine collection of browsing history or raw query logs.

## Read-only live baseline inspection

Workflow: `.github/workflows/adguard-filter-policy-preflight.yml`  
Initial workflow commit: `525cab5320ec38dd17d712389bc8e1d566338cbc`  
Initial workflow blob after read-back: `29b3834ea7005b6bb9e9f91ae72294f33a0fc832`  
Run: `33125558800`  
Job: `98702744879`  
Result: **PASS**

Direct target evidence before any acceptance mutation:

- filtering enabled;
- two configured filter entries, but exactly one enabled;
- enabled list: `AdGuard DNS filter`, `https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt`;
- enabled list reported `178285` rules at inspection time;
- configured but disabled list: `AdAway Default Blocklist`, `https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt`;
- zero whitelist filters;
- zero user rules;
- 24-hour filter refresh interval;
- persisted protection/filtering enabled with `blocking_mode=default`;
- normal `example.com` resolution returned rcode `0` with 2 answers;
- exact Quad9 dns10 upstream, ECS disabled, query logging disabled, client-IP anonymisation enabled, and statistics disabled remained unchanged.

This established that the deployed state was already a conservative one-list baseline. Enabling extra lists without project-specific evidence would have expanded filtering and false-positive risk without being required by ACC-0406, so no active-list mutation was made.

## Versioned policy artifact

Artifact: `infrastructure/adguard-server/filter-policy-v1.yaml`  
Creation commit: `db349b3afd95bb85248f65812a7187d5362caa40`  
Blob after read-back: `333a4ef8cd34719d66056aa608ab19473f839634`

Version: **1.0.0**.

The policy records:

- rationale for using one maintained general-purpose DNS filter as the initial conservative baseline;
- the active AdGuard DNS filter and inactive AdAway list;
- no baseline whitelist filters and no baseline user rules;
- frozen dns10/ECS-off and privacy invariants;
- the existing privacy-safe false-positive intake as the exception path;
- a narrow explicit AdGuard allow rule as the technical exception mechanism, never blanket filtering disablement;
- exact prior-rule restoration as rollback;
- the Protection Claims Checklist as the claims boundary;
- explicit statement that DNS filtering is only a domain-resolution safety layer and is not complete online safety;
- allowed, blocked, exception, rollback and privacy verification requirements; and
- governed change control for later list/allowlist/filtering/upstream/privacy changes.

## First acceptance run — failed and not accepted

Workflow: `.github/workflows/adguard-filter-policy-acceptance.yml`  
Initial trigger commit: `fc3ba3aa1d29e2dbd480377f92c3118ad3f7d958`  
Initial workflow blob: `cb0354c5179ec4dd7eddd794fc2f0bf5a80387e5`  
Run: `33125650171`  
Job: `98703037668`  
Result: **FAILURE — not accepted as task completion**

The baseline checks passed. The run then submitted a temporary exact block rule for a randomized `.invalid` name, but the immediate post-write `check_host` observation still reported `NotFilteredNotFound` rather than the expected `FilteredBlackList`. The test failed at that assertion.

The temporary mutation had been wrapped by a restore trap before it was made. Because the acceptance observation failed, no PASS was claimed and continuation was stopped pending direct recovery verification.

## Mandatory post-failure recovery audit

The read-only verifier was strengthened to require zero API and persisted user rules after the failed run.

Recovery verifier commit: `92d5226140417551f34c948d7271eeb77b519a16`  
Recovery verifier blob after read-back: `37b9ea4f462fd3fe0085a6001a4027755f48dfbb`  
Run: `33125686361`  
Job: `98703159125`  
Result: **PASS**

The target proved:

- API user-rule count returned to `0`;
- persisted user-rule count returned to `0`;
- the single enabled AdGuard DNS filter and disabled AdAway entry were unchanged;
- filtering/protection and `blocking_mode=default` were unchanged;
- dns10/ECS-off, query-log-off, anonymisation-on and statistics-off invariants were preserved; and
- `example.com` still resolved with rcode `0` and 2 answers.

Marker: `TSK_0406_RECOVERY_AUDIT=PASS`.

Therefore the failed acceptance attempt left no durable filter-rule change.

## Corrected acceptance verification

The acceptance verifier was changed based on the observed target behavior, not blindly retried. It now polls the rule-engine observation until the expected state is directly observed, bounded to at most 100 checks with 0.1-second spacing per transition. The restore trap remains armed until rollback is itself observed and the original state is compared exactly.

Corrected verifier commit: `ac8a13ea66d4a6fb695067f04cd3cab8b37fb970`  
Corrected verifier blob after read-back: `5ffaf1e1e77273cb77a21afd03c4800a230b45a9`  
Run: `33125736588`  
Job: `98703328392`  
Result: **PASS**

### Baseline

Before mutation:

- filtering enabled;
- exactly one active list: AdGuard DNS filter;
- zero whitelist filters;
- zero user rules;
- randomized synthetic `.invalid` test name: `NotFilteredNotFound`.

### Block regression

The complete temporary user-rule set was replaced with one exact synthetic block rule. The target subsequently reported:

- result: `FilteredBlackList`;
- convergence observed on poll attempt `2`.

Result: **blocked regression PASS**.

### Narrow exception regression

The complete temporary rule set was then replaced with the same block rule plus a matching explicit allow exception. The target subsequently reported:

- result: `NotFilteredWhiteList`;
- convergence observed on poll attempt `2`.

Result: **narrow exception PASS**.

### Exact rollback regression

The exact pre-test user-rule set (`[]`) was restored. The target subsequently reported:

- result: `NotFilteredNotFound`;
- convergence observed on poll attempt `3`;
- API user-rule set exactly restored to `[]`;
- filter-list enabled/disabled state unchanged;
- whitelist-filter state unchanged.

The persisted YAML then independently proved:

- policy still matches v1 baseline;
- zero persisted user rules;
- one active AdGuard DNS filter;
- dns10 upstream unchanged;
- ECS disabled;
- query logging disabled;
- client-IP anonymisation enabled;
- statistics disabled.

A direct post-rollback DNS request for `example.com` returned a valid answer (`answer_count=2`).

Final marker: `TSK_0406_ACCEPTANCE=PASS`.

## Mutation and rollback disposition

No permanent resolver filter-list or user-rule mutation was required for the accepted baseline. The only live changes made by the acceptance test were temporary synthetic user rules on the loopback-only pre-public resolver. They were restored exactly and independently verified at both API and persisted-config levels.

The durable project change is the versioned policy artifact defining the already-deployed conservative baseline and its governed exception/rollback/claims boundaries.

## Evidence hygiene

The filter tests used a randomized `.invalid` name plus `example.com`. No participant IP address, browsing/domain history, credential, token, private key, or raw user DNS history is contained in this evidence. Persistent query logging and identifiable statistics remained disabled throughout the accepted run.

## Stable task outcome

**TSK-0406: PASS.**

ACC-0406 is fully satisfied: the conservative baseline rationale is documented, the false-positive/allow-exception path is narrow and reversible, complete-safety claims are explicitly prohibited, configuration is versioned as policy v1.0.0, blocked/allowed/exception/rollback behavior is directly tested, the original live state is restored exactly, and all previously verified privacy/upstream invariants remain intact.
