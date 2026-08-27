# TSK-0203 — AdGuard Home Installation Evidence

**Task:** TSK-0203  
**Acceptance:** ACC-0203  
**Target:** `srv.UseSafeWeb.com` / Azure VM `adguardvm`  
**Execution path:** repository-scoped GitHub self-hosted runner  
**Date:** 2026-08-27

## Approved source and release identity

The installed release is the current official non-prerelease AdGuard Home release verified from the official `AdguardTeam/AdGuardHome` GitHub repository:

- version: **v0.107.79**;
- release date: 2026-08-18;
- asset: `AdGuardHome_linux_amd64.tar.gz`;
- GitHub release-asset SHA-256: `c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f`;
- official release `checksums.txt` independently returned the same digest for `./AdGuardHome_linux_amd64.tar.gz`.

Canonical installer artifact:

- `infrastructure/adguard-server/install-adguard.sh`;
- final installer Git blob used for the successful run: `5891f79b531ac2f0366374a8f4bec8fa560a2496`;
- successful-run installer SHA-256: `f1088b5dcf1b5b9a10b475ebe7a9a6d617233dcab8432cee9592daa08f32d40b`.

The installer verifies the pinned asset digest, verifies the official checksum file, rejects unsafe archive paths, refuses an unrecognized pre-existing installation, uses AdGuard Home's supported built-in service installer, and does not open public resolver/admin firewall ports.

## Mutation evidence

Workflow: `.github/workflows/adguard-install.yml`  
Successful workflow run: `33121330758`  
Job: `98688639507`  
Result: **PASS**

Observed target result:

- canonical installer artifact identity check: PASS;
- release asset matches the pinned GitHub digest: PASS;
- official `checksums.txt` agrees with the pinned digest: PASS;
- extracted binary identified itself as `AdGuard Home, version v0.107.79`: PASS;
- AdGuard Home built-in service installation completed successfully;
- AdGuard Home reported that it was installed and would automatically start on boot;
- `AdGuardHome.service` enabled: PASS;
- `AdGuardHome.service` active: PASS;
- installed binary version: `AdGuard Home, version v0.107.79`;
- UFW remained active and no public AdGuard/admin rule was opened;
- initial AdGuard setup/admin listener observed on TCP 3000; firewall exposure remained limited to SSH at this phase;
- no resolver/TLS listener was opened on 53/80/443/853 by this task;
- workflow marker: `TSK_0203_MUTATION=PASS` / `TSK_0203_WORKFLOW=PASS`.

Several earlier workflow attempts failed closed before installation while validating canonical bytes, the vendor checksum filename format, archive member normalization, and a shell-variable collision. None of those attempts copied the binary into `/opt` or installed the service. Each retry was based on new target evidence and a specific corrected cause.

## Independent fresh stable-state audit

Workflow: `.github/workflows/adguard-install-audit.yml`  
Workflow commit: `db827a051f62c1a4e5405b14ff67ffa94310a05e`  
Workflow run: `33121382223`  
Job: `98688809908`  
Result: **PASS**

Fresh audit observed:

- installed version: `AdGuard Home, version v0.107.79`;
- installed binary SHA-256: `7e247573e63ce771a5925d16ca4ca9344e6e888673244289dc302f0fdfdfbf4e`;
- systemd service enabled and active: PASS;
- systemd `ExecStart` uses `/opt/AdGuardHome/AdGuardHome -s run`: PASS;
- UFW active with default deny incoming / allow outgoing: PASS;
- only inbound UFW ALLOW rule is SSH/TCP 22: PASS;
- AdGuard listener exists on TCP 3000: PASS;
- no AdGuard listener exists yet on 53, 80, 443, or 853: PASS;
- local setup UI is reachable at `http://127.0.0.1:3000/` and returned HTTP 302: PASS;
- persistent GitHub runner service remained enabled/active: PASS;
- final marker: `FRESH_INSTALL_AUDIT=PASS`.

## Administrative exposure interpretation

At this installation stage AdGuard Home's setup listener binds to `*:3000`, but UFW denies inbound access to that port and the only allowed inbound host rule remains SSH. Therefore the setup/admin surface is not publicly reachable through the host firewall. Later configuration work must further establish the intended restricted administration model before any public resolver/TLS service is opened.

## Security/evidence hygiene

No password, credential, registration token, private key, API token, raw DNS query history, or other secret is stored in this evidence.

## Stable task outcome

**TSK-0203: PASS.**

ACC-0203 is satisfied by official-source/version/integrity evidence, successful installation and autostart evidence, restricted current exposure, and a separate fresh stable-state audit.
