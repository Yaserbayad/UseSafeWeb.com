# UseSafeWeb AdGuard Privacy-Minimal Backup Scope

**Task:** TSK-0429  
**Acceptance:** ACC-0429  
**Policy version:** 1.0.0  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Pilot region:** Azure West Europe (`westeurope`), Netherlands  
**Status:** approved scope definition for the current pre-Experiment AdGuard node

## 1. Purpose and boundary

This policy defines the smallest configuration backup needed to recover the current single-node AdGuard service without turning backups into a DNS-history, participant-data, or secret archive.

It supports the frozen operating model:

- Microsoft Azure remains the hosting baseline;
- Experiment-1 child-linked DNS uses West Europe, Netherlands;
- the initial DNS service is one lean AdGuard node, separate from the web/app VM;
- approximately 30 minutes recovery/downtime is accepted for a server failure/rebuild;
- Azure control-plane creation/configuration remains owner-managed;
- Git remains the source of versioned scripts and non-secret configuration expectations, not secret-bearing backup data.

This policy does **not** create an Azure Backup resource, storage account, vault, public endpoint, or other Azure control-plane object.

## 2. Current verified live facts

Read-only preflight run `33127459481` / job `98708878287` on `adguardvm` established:

- `/opt/AdGuardHome/AdGuardHome.yaml` exists as `600 root:root`;
- `/var/lib/usesafeweb/adguard/admin.env` exists separately as `600 root:root`;
- the old initialization rollback copy `/var/lib/usesafeweb/adguard/AdGuardHome.pre-loopback.yaml` exists as `600 root:root`;
- schema version is `34`;
- query logging is disabled;
- file query logging is disabled;
- statistics are disabled;
- client-IP anonymisation is enabled;
- persistent client count is `0`;
- user-rule count is `0`;
- one administrator account exists in the AdGuard configuration;
- AdGuard TLS is currently disabled;
- no TLS private key is configured;
- no TLS certificate chain is configured;
- non-empty `querylog.json*` file count is `0`;
- the versioned non-secret approved-settings artifact and filter policy match their accepted Git blobs.

The current secret-safe approved settings are independently captured in `approved-adguard-config-v1.json`; TSK-0202 proved that artifact exactly matches the live safe-field projection.

## 3. Backup data classification

### 3.1 Included inside the encrypted configuration payload

For the current node, the encrypted payload contains exactly:

1. `/opt/AdGuardHome/AdGuardHome.yaml` — the current raw AdGuard configuration, copied only after the backup preflight verifies the privacy invariants in this policy; and
2. a generated non-secret manifest containing backup format version, creation UTC, source hostname, AdGuard version, source configuration checksum, archive checksum, and the canonical Git commit/config-policy identifiers required to verify restoration.

Rationale: the raw AdGuard configuration is the only live server-managed configuration state that is not completely reproduced by Git. It may contain security-sensitive configuration such as the administrator password hash, so it is allowed only inside the encrypted payload and must never be written to Git or workflow logs.

### 3.2 Referenced from Git, not duplicated into the protected payload

The following remain canonical/versioned in Git and are recovered from the repository rather than backed up as mutable server data:

- `/infrastructure/adguard-server` deployment/recovery scripts;
- `infrastructure/adguard-server/approved-adguard-config-v1.json`;
- `infrastructure/adguard-server/filter-policy-v1.yaml`;
- deployment/privacy/filter/security evidence records.

This avoids unnecessary duplicate mutable copies.

### 3.3 Explicitly excluded

The backup must not contain:

- `/var/lib/usesafeweb/adguard/admin.env` or any plaintext administrator password/credential;
- `/var/lib/usesafeweb/adguard/AdGuardHome.pre-loopback.yaml` or other stale initialization/rollback copies;
- `querylog.json*`, query-log databases, raw DNS query/domain history, or exports of such history;
- identifiable per-client statistics, persistent client records, top-domain/client-history data, or client-IP datasets;
- participant/contact/research records or Experiment-1 pseudonymous metrics;
- diagnostic DNS logs except under a separately authorised time-boxed diagnostic procedure; those diagnostic datasets are never automatically folded into this configuration backup;
- downloaded/generated filter cache files that can be recreated from the versioned filter URLs/policy;
- generic OS caches, package caches, temporary files, GitHub runner work directories, or application logs;
- the AdGuard binary/packages that can be reinstalled by the versioned recovery process;
- TLS private keys or certificate material under the **current** scope because none is currently configured.

If TLS private material is introduced later, it is **not automatically added**. That change triggers a fresh backup-scope/security review before any private key can be included in a backup.

## 4. Pre-backup fail-closed checks

TSK-0430 must refuse to create an accepted backup unless current target inspection proves all of the following immediately before capture:

- query logging `false`;
- file query logging `false`;
- statistics `false`;
- client-IP anonymisation `true`;
- no persistent clients;
- no non-empty query-log files;
- no unexpected user rules or whitelist state outside the accepted versioned configuration;
- source is the expected `adguardvm` / AdGuard version and the current raw config exists root-owned/root-readable only;
- the versioned approved-settings artifact remains consistent with the safe-field projection of the live configuration.

Any failed check blocks backup creation/acceptance and requires reconciliation before retry.

## 5. Encryption requirement

Any payload containing the raw `AdGuardHome.yaml` must be encrypted **before durable retention or movement off the root-restricted staging area**.

Required properties:

- confidentiality plus integrity/authentication, so tampering is detectable;
- decryption is possible only through an owner-authorised recovery path;
- encryption key/passphrase/private material is separate from the encrypted archive;
- encryption material must not be committed to Git, embedded in the archive, printed to workflow logs, or stored in a GitHub Actions artifact;
- plaintext temporary copies use a root-only directory and restrictive umask and are deleted after successful encryption/checksum verification or on failure.

The exact encryption tool/key mechanism is intentionally left to TSK-0430 because no owner decryption key or approved external secret-store object is currently part of canonical state. TSK-0430 may choose only a mechanism that satisfies these properties and can prove owner-authorised decryption; it must not silently invent or publish key material.

## 6. Access control

Backup contents are restricted to:

- root on the handed-off DNS VM during creation/restore; and
- the Project Owner or an explicitly owner-authorised recovery mechanism/person for decryption/recovery.

The encrypted backup must not be placed in the Git repository, public storage, workflow logs, or unencrypted GitHub Actions artifacts.

No support, analytics, research, marketing, or product process receives backup access.

## 7. Location

### Current creation/staging location

TSK-0430 may create the root-only encrypted configuration backup on `adguardvm`, which is the verified Azure `westeurope` / Netherlands DNS VM. The staging directory is to be a dedicated root-only path outside the live AdGuard application directory (for example `/var/backups/usesafeweb/adguard/`), with the exact path recorded by TSK-0430.

A same-VM copy is a staging/recovery artifact, not proof of node-loss resilience.

### Durable/off-host location

Until an owner-approved change says otherwise, any durable off-host copy used for the Experiment-1 DNS recovery path must remain within the approved Azure/EU operating boundary and must not introduce a US-node or unreviewed processor/data flow. Azure control-plane provisioning/configuration is owner-managed, so this task does not create or assume a specific vault/storage resource.

If an owner-managed Azure backup/storage target is later supplied, its actual region, access and retention behavior must be verified before it becomes an accepted durable location.

## 8. Retention

No project-approved calendar duration exists for configuration backups, and this policy does not invent one. Retention is therefore minimal and event-based:

1. retain the **latest verified encrypted configuration backup** needed for recovery;
2. one immediately previous verified encrypted backup may be retained as the rollback generation while a newer backup is being validated;
3. after the newer backup passes its required checksum + owner-authorised decryption verification, no more than those two verified generations may remain;
4. when another verified generation is added, delete the oldest so the retained set remains at most two generations;
5. plaintext staging copies are deleted immediately after successful encryption/checksum verification and also on failed backup attempts;
6. an invalid, partial, unverified, or policy-violating backup is deleted as soon as its failure is established and is never counted as a retained recovery generation.

This retention rule is separate from Experiment-1 participant-data retention because participant/contact/DNS-history data is excluded from this backup entirely.

## 9. Deletion and verification

For project-controlled files:

- delete superseded/failed plaintext and encrypted files using the host filesystem controls available at execution;
- verify deletion by read-back/file absence and record the deleted backup identifier/checksum without copying its contents into evidence;
- do not claim forensic or cryptographic erasure from a cloud block device unless the storage platform actually proves it.

For any future owner-managed Azure durable copy:

- provider-side retention/deletion is owner-controlled;
- the project records the configured lifecycle/deletion behavior when that target is actually supplied;
- backup success does not prove provider-side deletion.

If prohibited participant data, DNS history, credentials outside the permitted encrypted configuration, or unexpected private-key material is discovered during backup creation, stop, delete the partial backup/staging copy, preserve only non-sensitive incident evidence, and reopen the relevant privacy/security control before retry.

## 10. Recovery behavior

A clean rebuild should prefer deterministic reconstruction rather than restoring unnecessary state:

1. reinstall/harden using the versioned Git recovery scripts;
2. inject or generate administrator credentials through the protected server mechanism rather than restoring `admin.env` from backup;
3. decrypt and restore the accepted raw `AdGuardHome.yaml` only through the authorised recovery path;
4. independently compare restored safe settings to the versioned approved-settings artifact;
5. re-download generated filter data from the versioned filter policy;
6. re-prove privacy, upstream, filter, abuse, service-health and access invariants before exposure.

`initialize-admin.sh` already proves that if `admin.env` is absent it can create a fresh strong credential in a `0600 root:root` server-only file. Excluding that plaintext credential from the backup therefore reduces recovery secret exposure without preventing deterministic rebuild.

## 11. Alignment with current DPIA/data-flow and retention authority

This scope is aligned to the current validation-readiness/DPIA baseline:

- identifiable DNS/domain history is not retained;
- exceptional diagnostic DNS data remains time-boxed and deleted after resolution under its separate procedure;
- Git receives only non-sensitive evidence/aggregate or anonymised findings;
- Experiment-1 child-linked DNS uses Azure West Europe/Netherlands and Quad9 dns10, with no US node in the pilot path;
- the current pilot data-flow has no additional backup processor selected;
- participant/contact/research data has its own 30-day/90-day maximum rules and is excluded from this configuration backup, so backup retention cannot silently extend those periods.

Adding a new backup service/provider/location, including participant data, including a TLS private key, changing the VM geography, or retaining more data/generations is a material scope change that requires privacy/security impact review before use.

## 12. Acceptance mapping

ACC-0429 requires the following to be documented and aligned with the DPIA:

| Acceptance dimension | Policy result |
|---|---|
| Included data | Current raw `AdGuardHome.yaml` + non-secret verification manifest only |
| Excluded data | Plaintext admin credential, stale rollback copies, query/history/stat/client data, participant data, diagnostics, generated caches, current-absent TLS material |
| Encryption | Confidentiality + integrity/authentication before durable retention/off-host movement; owner-authorised decryption; key separate and never in Git/log/archive |
| Retention | Event-based; latest verified + at most one previous verified generation; no invented calendar duration; plaintext staging removed immediately |
| Access | Root during execution plus owner/explicit owner-authorised recovery path only |
| Location | Root-only staging on verified West Europe DNS VM; future durable copy remains in approved Azure/EU boundary and requires actual owner-managed target verification |
| Deletion | Delete failed/superseded copies, verify absence; no unsupported forensic-erasure claim; provider-side deletion verified only when a real provider target exists |
| DPIA alignment | No identifiable DNS history/participant data; no US pilot node/unreviewed processor; separate Experiment-1 retention periods cannot be extended by backup |

## 13. Source/evidence basis

- Canonical WBS TSK-0429 / ACC-0429, re-read in queue run `33127287940` / job `98708339992`.
- `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`.
- `RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`.
- `PILOT_PRIVACY_NOTICE.md`, blob `331f263388dfacfa73b6e9e556277d4230864ce8`.
- `infrastructure/adguard-server/initialize-admin.sh`, blob `0fa0b3481d9b7173649c72606b40642c278e9c32`.
- `infrastructure/adguard-server/approved-adguard-config-v1.json`, blob `ea85830b5ef9de7f2772e5467570d52013228b0b`.
- `infrastructure/adguard-server/filter-policy-v1.yaml`, blob `333a4ef8cd34719d66056aa608ab19473f839634`.
- Read-only live backup-scope preflight `.github/workflows/adguard-backup-scope-preflight.yml`, blob `ae667b40bfb44ffa13eae0c3d7ec9ad243f5f2ad`, run `33127459481` / job `98708878287`.
- REQ-0049 / REQ-0050, CON-0004 / CON-0005, INT-0014, RSK-0048 from the current canonical registers.

## Stable policy result

This policy defines the current privacy-minimal backup scope without creating a backup or Azure resource. TSK-0430 may implement only inside this scope. Any implementation that cannot prove encryption, owner-authorised decryption, exact allowed contents, prohibited-data exclusion, checksum/date, retention rotation and deletion behavior must remain open rather than relying on this policy artifact alone.
