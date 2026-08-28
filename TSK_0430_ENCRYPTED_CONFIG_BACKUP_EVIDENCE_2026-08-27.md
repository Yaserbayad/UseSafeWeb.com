# TSK-0430 — Encrypted Configuration Backup Evidence

**Task:** TSK-0430  
**Acceptance:** ACC-0430  
**Evidence:** EVD-0430  
**Verification:** VER-0430  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27 / owner decryption proof 2026-08-28

## Current task outcome

**TSK-0430 is PASS.**

The encrypted configuration backup was created and independently audited on the target, with recorded checksum/date and no prohibited query-history retention. On 2026-08-28, the Project Owner directly executed the repository-pinned owner-side verifier from an owner-controlled workstation and successfully decrypted this exact retained archive using the corresponding owner-held SSH private key. No private-key material or passphrase was supplied to GitHub, the server, or ChatGPT as part of this proof.

All elements of ACC-0430 are now directly proven.

## Authoritative task contract

The canonical WBS defines TSK-0430 as:

- A3;
- `AUTO_ALLOWED` for project-controlled execution;
- HIGH priority;
- critical path;
- predecessors `TSK-0202`, `TSK-0429`, `TSK-0011`, all satisfied;
- ACC-0430: **backup completes, can be decrypted by the authorised owner, contains no prohibited query history, and has a recorded checksum/date**.

The backup scope is controlled by `infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md`, blob `e62b48a3e746b1be90881bbffab3b7680384cc16`.

## Owner-recipient preflight

No private key or backup decryption secret was created on the server.

The final recipient preflight proved:

- `/home/azureusr/.ssh/authorized_keys` contains exactly one key;
- type: `ssh-rsa`;
- size: 3072 bits;
- effective SSH configuration has public-key authentication enabled;
- password, keyboard-interactive, GSSAPI and host-based authentication are disabled;
- Ubuntu 24.04 offers `age` package `1.1.1-1ubuntu0.24.04.3`;
- prior TSK-0435 evidence independently proves the Project Owner successfully executed the handoff verifier through an SSH session to `azureusr` on this VM.

The final preflight workflow commit was `c44995a0c6c3ad894ce96a4cf33fda68a567e68b`, with workflow blob `96c2bc873ffdd7cf5a05de613e7c4adcdfd7d5f5`; run `33127873331` / job `98710219734`: **PASS**.

An earlier diagnostic attempt `33127836379` / job `98710104141` was not accepted because it tried to corroborate the historical owner handoff through a narrow SSH journal window where the old acceptance event was no longer present. It performed no target mutation. The verifier was corrected to use current effective SSH authentication configuration plus the existing durable TSK-0435 owner-handoff evidence.

Current official `age` documentation states that SSH RSA public keys are supported recipients when they are at least 2048 bits, recipient files passed with `-R` may use `authorized_keys` format, and decryption uses the corresponding SSH private-key file through `-i`. It also explicitly notes that ssh-agent/hardware-token identities are not supported by this SSH-key mode. Ubuntu's current Noble package source lists `age` version `1.1.1-1ubuntu0.24.04.3` for amd64.

## Backup implementation

Canonical implementation:

`infrastructure/adguard-server/create-encrypted-config-backup.sh`

Git blob after read-back:

`6b2642515b9c345f2ec3b47cbf5d7f0ec5c87e51`

Execution workflow:

`.github/workflows/adguard-encrypted-config-backup.yml`

Workflow blob after read-back:

`5bd12413a6dec63ddea54915f953be5bb5553dac`

The implementation:

1. fails closed unless the current live safe settings exactly match `approved-adguard-config-v1.json`;
2. requires query/file logging off, statistics off, anonymisation on, no persistent clients, no user/whitelist rules, no TLS private material and no non-empty query-log files;
3. uses the sole 3072-bit owner SSH public key as the `age` recipient without copying or generating any corresponding private key;
4. stages plaintext only under a root-only `0700` directory with `umask 077`;
5. copies only the current raw `AdGuardHome.yaml` plus a non-secret manifest into the backup package;
6. excludes plaintext `admin.env`, query/DNS history, persistent client/statistics data, participant/research data, diagnostic logs, generated caches, stale rollback copies and current-absent TLS private material;
7. encrypts the package before retention using `age -R /home/azureusr/.ssh/authorized_keys`;
8. records archive creation UTC, ciphertext SHA-256, size, recipient public fingerprint and source Git commit in a root-only sidecar;
9. keeps at most two verified encrypted generations;
10. removes plaintext staging before reporting success.

## Backup creation execution

Workflow trigger commit:

`87a00336ca05387db706d268d8a8e3c7fd608e7c`

Run / job:

- run `33128004795`;
- job `98710652627`;
- conclusion: **PASS**.

The workflow installed the pinned Ubuntu package `age=1.1.1-1ubuntu0.24.04.3` and verified `age --version` = `1.1.1`.

Direct safe output:

- privacy and approved-settings preflight: PASS;
- encrypted archive and metadata verification: PASS;
- created UTC: `2026-08-27T23:56:12Z`;
- archive: `usesafeweb-adguard-config-20260827T235612Z.tar.age`;
- ciphertext SHA-256: `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`;
- ciphertext size: `21121` bytes;
- owner recipient public fingerprint: `SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`;
- retained encrypted generations: `1`;
- plaintext staging directories remaining: `0`;
- `TSK_0430_BACKUP_CREATE=PASS`;
- `TSK_0430_WORKFLOW=PASS`.

The retained copy is root-only on the same West Europe DNS VM and is deliberately classified as a same-VM encrypted staging/recovery artifact, **not** as proof of node-loss resilience or an owner-managed Azure off-host backup target.

## Independent retained-backup audit

Independent workflow:

`.github/workflows/adguard-encrypted-config-backup-audit.yml`

The first audit run `33128102728` / job `98710969640` was **not accepted** because the privileged Python process did not inherit workflow environment variables and failed with `KeyError` before substantive metadata/live-state assertions. It performed no backup mutation.

The verifier was corrected to pass expected values explicitly. Final workflow blob after read-back:

`2e9e5a168ca93d39528176fa092b5fa19263c139`

Corrected run / job:

- trigger commit `810997736c7d5d95b7b4a7cddac6868e201cd684`;
- run `33128142374`;
- job `98711096972`;
- conclusion: **PASS**.

Independent proof:

- backup directory = `0700 root:root`;
- encrypted archive and sidecar = `0600 root:root`;
- ciphertext size exactly `21121` bytes;
- ciphertext SHA-256 exactly `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`;
- ciphertext has the `age-encryption.org/v1` header;
- sidecar exactly matches expected date/name/hash/size/source commit/recipient fingerprint/location classification;
- current sole authorised SSH key is still the same 3072-bit recipient fingerprint;
- no dedicated symmetric backup key/recipient marker exists;
- root and `azureusr` GPG secret-key counts are zero;
- retained encrypted generation count is exactly `1`;
- plaintext/temp staging count is `0`;
- current live privacy and approved-settings projection remains unchanged;
- non-empty live `querylog.json*` file count remains `0`;
- final marker: `TSK_0430_INDEPENDENT_AUDIT=PASS`.

## Owner-side direct decryption proof — 2026-08-28

The Project Owner executed the repository-pinned `infrastructure/adguard-server/verify-owner-encrypted-backup.sh` from an owner-controlled workstation against the retained archive on `srv.UseSafeWeb.com`. The private key remained owner-held and was not copied into the VM, GitHub, or project evidence.

Safe reported verification outputs:

- `PASS ciphertext checksum verified locally`;
- `owner_local_sidecar_verification=PASS`;
- `PASS owner private key decrypted encrypted backup locally`;
- `decrypted_package_member_scope=PASS`;
- `decrypted_manifest_identity_and_scope=PASS`;
- `PASS decrypted configuration checksum verified without printing configuration contents`;
- `encrypted_archive_sha256=bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`;
- `owner_recipient_fingerprint=SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`;
- `decrypted_configuration_sha256=d8b6eae3b85edbaa1c49e318354389dc616099ecb3d2d90eff3c3dd8c663e1f2`;
- `TSK_0430_OWNER_DECRYPTION=PASS`.

The ciphertext SHA-256 and owner recipient fingerprint exactly match the independently audited retained backup. The decrypted package-member scope and manifest identity checks passed, and the raw configuration checksum was verified without printing configuration contents. This is direct owner evidence for decryptability of the exact retained archive and closes the remaining ACC-0430 element.

## Current acceptance evaluation

| ACC-0430 element | State | Evidence |
| --- | --- | --- |
| Backup completes | PASS | creation run `33128004795` / job `98710652627` |
| Contains no prohibited query history | PASS | fail-closed preflight + independent audit + owner-side decrypted package/member scope verification |
| Recorded checksum/date | PASS | UTC `2026-08-27T23:56:12Z`, ciphertext SHA-256 `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`, independently and owner-side reverified |
| Can be decrypted by authorised owner | PASS | owner-side direct decryption of the exact retained ciphertext, ending `TSK_0430_OWNER_DECRYPTION=PASS`, with matching recipient fingerprint and verified decrypted configuration checksum |

## Stable current outcome

**TSK-0430: PASS.**

ACC-0430 is fully satisfied with durable server-side creation/audit evidence plus direct owner-side decryption evidence. No private-key material or passphrase is stored in project evidence. Downstream work may now be evaluated from current WBS/graph authority.
