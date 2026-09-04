# TSK-0451 post-VM server security baseline evidence

**Date:** 2026-09-04
**Task:** TSK-0451
**Acceptance:** ACC-0451
**Verification:** VER-0451
**Evidence:** EVD-0451
**Source commit:** `b1cab12c5dff3d5cbe8eec1ca790cbda1c60a61f`
**Source script blob:** `1a409508b5d71e379787b95f212f41c8a5573cdb`
**Source script SHA-256:** `9ec0a319464ff87b5c9e94353f409db604284e384c355fa77bfcfaa15a0c375e`
**GitHub Actions run / attempt:** `33846507277 / 1`
**Target:** repository-scoped self-hosted runner on `adguardvm`, Ubuntu 24.04 LTS, running as `azureusr` with previously approved non-interactive sudo bridge.

## Result

**PASS.** The target independently proved the complete current TSK-0451 baseline:

- `sshd -t` passed; effective `sshd -T` reports `PermitRootLogin no` and `PasswordAuthentication no`.
- `ufw status verbose` reports active firewall, default deny incoming / allow outgoing, with SSH on 22/tcp allowed.
- Fail2ban configuration validation passed; `fail2ban.service` is enabled and active; `fail2ban-client status sshd` confirms the `sshd` jail is active.
- `unattended-upgrades.service`, `apt-daily.timer`, and `apt-daily-upgrade.timer` are enabled.
- `/etc/apt/apt.conf.d/20auto-upgrades` contains daily `Update-Package-Lists` and `Unattended-Upgrade` settings.
- Evidence is sanitized: no authentication log lines, banned-IP list, credential, private key, token, or secret value is retained here.

## Bounded change and rollback safety

The task-specific apply script first re-verified the already-accepted SSH/UFW state and did **not** rewrite SSH or UFW. It then installed/configured only Fail2ban and the unattended-upgrades enablement required by ACC-0451. A new Fail2ban jail file is syntax-tested before service enablement; if enablement fails, the prior jail file is restored (or the new file removed) before failure is reported.

## Sanitized run evidence

- Apply transcript SHA-256: `63125bf2d0604bb1367e98f536970ad76a048c180468397f0427a7cd330b5850`
- Independent verification transcript SHA-256: `7eb89d18ce4de68ad7f1b4699ee11b558294ad7a4340d33c072233cd3a6aa131`
- Both workflow artifacts were retained for seven days; only privacy-safe PASS/status markers are reproduced in durable project evidence.

## Source basis

- Ubuntu 24.04 OpenSSH: https://manpages.ubuntu.com/manpages/noble/man5/sshd_config.5.html
- Ubuntu 24.04 Fail2ban jail configuration: https://manpages.ubuntu.com/manpages/noble/man5/jail.conf.5.html
- Ubuntu 24.04 Fail2ban client: https://manpages.ubuntu.com/manpages/noble/man1/fail2ban-client.1.html
- Ubuntu Server automatic updates: https://ubuntu.com/server/docs/how-to/software/automatic-updates/

## Non-inference

This PASS proves only TSK-0451. It does not pass TSK-0455 or any dependent task, deploy application/DNS/TLS changes, distribute profiles/certificates, revoke services, process participants, enable telemetry, authorize public/market activation, or satisfy launch gates.
