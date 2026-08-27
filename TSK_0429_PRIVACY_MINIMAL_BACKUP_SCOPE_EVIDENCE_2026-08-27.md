# TSK-0429 — Privacy-Minimal Backup Scope Evidence

**Task:** TSK-0429  
**Acceptance:** ACC-0429  
**Evidence:** EVD-0429  
**Verification:** VER-0429  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27

## Authoritative task contract

Queue recomputation run `33127287940` / job `98708339992` directly re-read the canonical WBS row for TSK-0429:

- capability `A3`;
- authority `AUTO_ALLOWED`;
- priority `HIGH`;
- critical path `YES`;
- hard predecessors `TSK-0437` + `TSK-0011`, both satisfied by current direct runtime/publication evidence;
- ACC-0429: included/excluded data, encryption, retention, access, location, and deletion must be documented and aligned with the DPIA.

Linked current authority re-read before policy creation:

- REQ-0049 — Azure remains hosting baseline; Experiment-1 child-linked DNS uses West Europe, Netherlands; Azure control-plane owner-managed;
- REQ-0050 — one lean AdGuard node, separate web/app VM, approximately 30 minutes recovery/downtime accepted;
- CON-0004 / CON-0005 — Azure owner-managed boundary and no US node in the Experiment-1 path;
- INT-0014 — deployment/runtime contract must introduce no unapproved service/data flow and retain rollback;
- RSK-0048 — recovery must not leak secrets or leave unsafe partial service;
- current validation-readiness/DPIA, retention/deletion and privacy-notice artifacts.

## Current source artifacts

The policy was grounded in the following exact canonical Git blobs:

- `VALIDATION_READINESS_GATE.md` — `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`;
- `RETENTION_DELETION_EXECUTION_CHECKLIST.md` — `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`;
- `PILOT_PRIVACY_NOTICE.md` — `331f263388dfacfa73b6e9e556277d4230864ce8`;
- `infrastructure/adguard-server/initialize-admin.sh` — `0fa0b3481d9b7173649c72606b40642c278e9c32`;
- `infrastructure/adguard-server/approved-adguard-config-v1.json` — `ea85830b5ef9de7f2772e5467570d52013228b0b`;
- `infrastructure/adguard-server/filter-policy-v1.yaml` — `333a4ef8cd34719d66056aa608ab19473f839634`.

The DPIA/readiness authority says identifiable DNS/domain history is not retained, diagnostics are time-boxed/deleted, Experiment-1 DNS stays in Azure West Europe/Netherlands before Quad9, no US UseSafeWeb node participates, and participant/contact data has separate 30-day/90-day maximum rules that must not be extended by infrastructure backup copies.

## Read-only live scope preflight

Workflow:

`.github/workflows/adguard-backup-scope-preflight.yml`

Workflow blob after read-back:

`ae667b40bfb44ffa13eae0c3d7ec9ad243f5f2ad`

Trigger commit / run / job:

- commit `759f0c83df32b4d166330e619f87e2c0ca6b9292`;
- run `33127459481`;
- job `98708878287`;
- result **PASS**.

Direct current target facts established without exposing secret contents:

- `/opt/AdGuardHome/AdGuardHome.yaml` exists as `600 root:root`;
- `/var/lib/usesafeweb/adguard/admin.env` exists separately as `600 root:root`;
- old initialization rollback `/var/lib/usesafeweb/adguard/AdGuardHome.pre-loopback.yaml` exists as `600 root:root`;
- schema version `34`;
- query logging `false`;
- file query logging `false`;
- statistics `false`;
- client-IP anonymisation `true`;
- persistent clients `0`;
- user rules `0`;
- administrator users `1`;
- AdGuard TLS `false`;
- TLS private key configured `false`;
- TLS certificate chain configured `false`;
- non-empty `querylog.json*` files `0`;
- the accepted non-secret config manifest and filter-policy Git blobs match.

This proved the current node contains no DNS-history/client dataset that needs to be preserved and no current TLS private material that must be included.

## Backup-scope policy

Created and read back:

`infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md`

Policy version:

`1.0.0`

Git blob:

`e62b48a3e746b1be90881bbffab3b7680384cc16`

Publication commit:

`1cceaa3f019dde55f3bbecb93e6ad2489177e48a`

The policy defines all ACC-0429 dimensions:

### Included data

Only:

1. current `/opt/AdGuardHome/AdGuardHome.yaml`, after fail-closed privacy preflight; and
2. a generated non-secret verification manifest with version/time/source/checksum/Git-policy identities.

Versioned scripts, the non-secret approved-settings artifact, filter policy and evidence remain referenced from Git rather than duplicated as mutable backup state.

### Explicit exclusions

- plaintext `/var/lib/usesafeweb/adguard/admin.env`;
- stale initialization/rollback copies;
- query logs or DNS/domain history;
- identifiable per-client statistics/persistent clients/top-domain/client-IP datasets;
- participant/contact/research data and Experiment-1 pseudonymous metrics;
- automatic inclusion of diagnostic datasets;
- generated filter cache, OS/package caches, temporary files, runner work directories and application logs;
- reinstallable AdGuard binary/packages;
- TLS private key/certificate material under the current scope because none is configured.

`initialize-admin.sh` provides an existing protected path to generate a fresh strong root-only administrator credential if the server credential file is absent, so backing up the plaintext admin password is not required for deterministic recovery.

### Encryption

Any payload containing raw `AdGuardHome.yaml` must receive confidentiality plus integrity/authentication before durable retention/off-host movement. Decryption material stays separate from the archive and must never be placed in Git, the encrypted archive, workflow logs or a GitHub Actions artifact. Plaintext staging must be root-only and deleted after successful encryption/checksum verification or on failure.

The exact encryption/key mechanism is deliberately reserved for TSK-0430 because no existing owner decryption key or approved external secret-store object is currently canonical; TSK-0429 does not invent/publish secret material.

### Retention

No approved calendar duration exists, so none was invented. The policy uses minimal event-based retention:

- latest verified encrypted configuration backup;
- at most one immediately previous verified generation;
- maximum two verified generations;
- delete oldest when a new verified generation is added;
- delete plaintext staging immediately after encryption verification;
- delete failed/invalid/partial copies immediately.

Participant/contact/DNS-history records are excluded, so infrastructure backups cannot silently extend the separate Experiment-1 30-day/90-day limits.

### Access

Root on the handed-off DNS VM during creation/restore plus the Project Owner or an explicitly owner-authorised recovery mechanism/person for decryption. No support, analytics, research, marketing or product process receives access. No backup may be stored in Git, public storage, workflow logs or unencrypted Actions artifacts.

### Location

Root-only staging on the verified Azure West Europe/Netherlands `adguardvm` outside the live AdGuard application directory. A same-VM copy is explicitly not treated as proof of node-loss resilience. Future durable off-host storage must remain within the approved Azure/EU boundary unless changed by owner authority, and any actual owner-managed Azure target must have region/access/retention verified before acceptance.

### Deletion

Failed/superseded project-controlled files are deleted and absence is verified; no unsupported forensic-erasure claim is made. Future provider-side retention/deletion remains owner-controlled and must be verified when an actual owner-managed storage target exists. Discovery of prohibited data/private material stops the backup and reopens affected controls.

## Independent policy/source/live audit

Workflow:

`.github/workflows/adguard-backup-scope-audit.yml`

Final corrected workflow blob after read-back:

`a41522be6361802d8964ccec8e53b92b3e9e62a1`

The first audit run `33127565783` / job `98709225350` was **not accepted** because a literal static verifier expected the phrase `provider-side deletion is owner-controlled`, while the policy correctly used `provider-side retention/deletion is owner-controlled`. It failed before live verification and performed no target mutation. The assertion was corrected without changing the policy.

Corrected run:

- trigger commit `cf19b6cecd2e4d1174365ae91492e1074782acbd`;
- run `33127643804`;
- job `98709483562`;
- result **PASS**.

Independent proof:

- expected policy blob matched exactly;
- all six referenced source/config/filter blobs matched exactly;
- every ACC-0429 policy dimension was present;
- no administrator password assignment or private-key block was present in the policy;
- DPIA region/no-US/DNS-history controls matched source;
- 30-day/90-day participant retention controls matched source;
- Git aggregate/anonymised-only rule matched source;
- protected admin-secret regeneration path matched source;
- live raw config, admin secret and old rollback remain `600 root:root`;
- live query/file logging remain disabled;
- statistics remain disabled;
- anonymisation remains enabled;
- persistent clients and user rules remain empty;
- TLS remains disabled with no TLS private key/certificate material;
- non-empty query-log file count remains zero.

Final markers:

- `policy_acceptance_dimensions_present=PASS`;
- `policy_secret_material_absent=PASS`;
- `dpia_retention_location_source_alignment=PASS`;
- `admin_secret_regeneration_source_alignment=PASS`;
- `live_backup_scope_privacy_invariants=PASS`;
- `live_tls_private_material_absent=true`;
- `live_nonempty_querylog_files=0`;
- `TSK_0429_INDEPENDENT_AUDIT=PASS`.

## Security/privacy boundary

This task defined policy only. It did not create an encrypted backup, encryption key, Azure backup/storage resource, off-host copy, participant record, query history, or public exposure.

The owner-deferred UK representative/ICO work remains unresolved and is unaffected by this technical PASS.

## Stable task outcome

**TSK-0429: PASS.**

ACC-0429 is fully satisfied: included and excluded backup data, encryption, retention, access, location and deletion behavior are explicitly documented; the policy is aligned to the current DPIA/data-flow/retention authority; its source blobs and current live assumptions were independently verified; and no secret material or prohibited data was introduced by the task.
