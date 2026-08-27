# TSK-0437 — Host Security Baseline Evidence

**Task:** TSK-0437  
**Acceptance:** ACC-0437  
**Target:** `srv.UseSafeWeb.com` / Azure VM `adguardvm`  
**Execution path:** repository-scoped GitHub self-hosted runner on `adguardvm`  
**Date:** 2026-08-27

## Acceptance criterion

ACC-0437 requires the accepted Ubuntu host to expose only required services/ports, restrict administrative access, apply current host patches, and capture durable host-baseline evidence.

## Persistent execution channel prerequisite

Before applying the baseline, the previously foreground GitHub runner was migrated to GitHub's Linux systemd service model and verified by a fresh job:

- runner: `adguardvm`, version `2.336.0`;
- account: `azureusr`;
- platform: Linux X64 / Ubuntu 24.04;
- non-interactive sudo: PASS;
- runner service install/bootstrap run: `33119643639`, job `98683013736`, conclusion PASS;
- independent persistent-service verification run: `33119676243`, conclusion PASS;
- service was required to be enabled, active, and have a nonzero systemd MainPID before host mutation.

The host-mutation workflows use `permissions: contents: read`, trusted `main` push triggers only, `persist-credentials: false` during checkout, and the serialized `usesafeweb-adguard-server` concurrency group.

## Mutation evidence

Workflow: `.github/workflows/adguard-host-hardening.yml`  
Workflow commit: `ab5d6faedd0df4e22f8f0e2087b463da6164c90e`  
Workflow run: `33119801746`  
Job: `98683551633`  
Result: **PASS**

The job first proved a recent `Accepted publickey` SSH login for `azureusr`, then executed the reviewed `infrastructure/adguard-server/harden-host.sh` through bounded non-interactive sudo.

Observed mutation result:

- Ubuntu 24.04 baseline: PASS.
- Recent public-key SSH authentication proof for `azureusr`: PASS.
- 48 currently offered Ubuntu packages upgraded; Ubuntu phased updates not currently installable were not forced.
- `ufw` and `unattended-upgrades` present/current.
- unattended security-update timers enabled.
- effective OpenSSH baseline validated and reloaded:
  - direct root login disabled;
  - password authentication disabled;
  - keyboard-interactive authentication disabled;
  - public-key authentication enabled;
  - empty passwords disabled;
  - X11 forwarding disabled;
  - MaxAuthTries = 3;
  - LoginGraceTime = 30 seconds.
- UFW enabled with default-deny incoming / allow outgoing and SSH retained.
- GitHub runner service restart was explicitly deferred by `needrestart`, preserving the executing control channel.
- no currently installable package upgrades remained after application.
- external-listener audit found only SSH on TCP 22; loopback DNS/SSH forwarding, DHCP, and chrony listeners remained local/system-only.
- no reboot was required.
- mutation-script final result: **`OVERALL=PASS failures=0 warnings=0`**.

## Independent stable-state audit

Workflow: `.github/workflows/adguard-host-hardening-audit.yml`  
Workflow commit: `92f921457fb4db1038b8d87b0e33ed58c77e77b6`  
Workflow run: `33119961094`  
Job: `98684096030`  
Result: **PASS**

The fresh job independently re-established that the persistent runner service was active/enabled and then ran the hardening artifact in audit-only mode.

Fresh audit result:

- effective SSH administrative-access baseline: PASS;
- UFW active with deny-incoming / allow-outgoing defaults: PASS;
- unattended security updates installed and scheduled: PASS;
- no currently installable package upgrades: PASS;
- no unexpected externally listening service: PASS;
- external TCP listeners: SSH only on `0.0.0.0:22` and `[::]:22`;
- final result: **`OVERALL=PASS failures=0 warnings=0`**;
- workflow marker: **`FRESH_AUDIT=PASS`**.

## Security/evidence hygiene

No password, token, private key, GitHub registration token, raw DNS history, or other secret is recorded in this evidence. The Actions token was scoped read-only to repository contents for these host jobs.

## Stable task outcome

**TSK-0437: PASS.**

All ACC-0437 elements are directly proven by target mutation evidence plus a separate fresh stable-state audit. Later service installation may intentionally open additional resolver/TLS ports; those changes require their own WBS authorization, firewall update, and post-change evidence and do not invalidate this pre-AdGuard baseline by themselves.
