# TSK-0430 — Encrypted Configuration Backup Evidence

**Task:** TSK-0430  
**Acceptance:** ACC-0430  
**Evidence:** EVD-0430  
**Verification:** VER-0430  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27

## Current task outcome

**TSK-0430 is WAITING, not PASS.**

The encrypted configuration backup has been created and independently audited on the target, with recorded checksum/date and no prohibited query-history retention. The remaining ACC-0430 element is direct proof that the **authorised owner can decrypt this exact retained archive using the corresponding owner-held SSH private-key file**. That private key is correctly absent from the server/GitHub execution environment, so the owner-decryption step cannot be fabricated or performed autonomously without crossing the secret/access boundary.

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

## Remaining owner-decryption acceptance proof

The server-side evidence proves that the archive was encrypted to the exact sole public key used for the owner-controlled SSH path. It does **not** prove that the owner-held private key is an ordinary SSH private-key file usable by `age -i`, rather than an ssh-agent/hardware-token-only identity, nor does it execute decryption of this exact ciphertext.

Because ACC-0430 explicitly requires that the backup **can be decrypted by the authorised owner**, the strongest practical acceptance evidence is one owner-side decryption/checksum run with the real owner private key while that key stays off the server.

A no-secret owner-side verifier has been prepared and read back:

`infrastructure/adguard-server/verify-owner-encrypted-backup.sh`

Git blob:

`d0d9c30bbb8f2b495f4cd852facf233ffab90843`

The script:

- takes the SSH target and local private-key path as arguments;
- streams only the known ciphertext and non-secret sidecar from the server;
- verifies ciphertext size/hash/date/recipient fingerprint locally;
- decrypts locally using `age -d -i <owner-private-key>`;
- verifies the decrypted package contains only `configuration.tar` and `manifest.json`;
- verifies the manifest identity/scope;
- verifies the inner archive and raw configuration checksums without printing configuration contents;
- deletes all local plaintext through its cleanup trap;
- emits only safe hashes/fingerprint and `TSK_0430_OWNER_DECRYPTION=PASS` on success.

The owner's private key and any key passphrase remain solely on the owner workstation and must not be pasted into ChatGPT, GitHub, the VM, or workflow logs.

## Current acceptance evaluation

| ACC-0430 element | State | Evidence |
| --- | --- | --- |
| Backup completes | PASS | creation run `33128004795` / job `98710652627` |
| Contains no prohibited query history | PASS | fail-closed preflight + independent audit; querylog/filelog off, no persistent clients/query files, strict backup scope |
| Recorded checksum/date | PASS | UTC `2026-08-27T23:56:12Z`, ciphertext SHA-256 `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`, independently reverified |
| Can be decrypted by authorised owner | **WAITING direct owner proof** | encrypted to exact owner-controlled 3072-bit RSA public key and format is supported by `age`, but the corresponding owner private-key file is intentionally not available to server automation and actual owner decryption has not yet been executed |

## Stable current outcome

**TSK-0430: WAITING.**

The encrypted backup itself is complete and independently stable. The deterministic resumption condition is a successful owner-side execution of `verify-owner-encrypted-backup.sh` against this exact archive, returning `TSK_0430_OWNER_DECRYPTION=PASS` and the expected ciphertext SHA-256 without exposing private-key material. Only then may ACC-0430 and TSK-0430 be marked PASS and the downstream restore task be considered for execution.
