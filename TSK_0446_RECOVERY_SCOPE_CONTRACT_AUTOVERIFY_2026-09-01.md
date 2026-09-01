# TSK-0446 recovery scope contract — automated verification marker — 2026-09-01

- Source commit: `6214ac817ed3279561495f73212bd7e2e9acfc6b`
- GitHub Actions run: `33504115232`
- Attempt: `1`
- Workflow: `Verify TSK-0446 recovery scope contract`
- Runner OS: `Linux`
- Result: **PASS**

Verified outcomes:

- current WBS binds TSK-0446 to L5, CRITICAL, A3/AUTO_ALLOWED, sole hard dependency TSK-0413, and current ACC-0446 wording;
- current runtime/evidence prove the accepted TSK-0413 predecessor and current LG-06 entry gate;
- the exact TSK-0413 bundle self-verifies and remains pinned to AdGuard Home v0.107.79/schema 34;
- the contract covers host/packages, AdGuard, configuration, network/firewall, DNS endpoint, TLS, filter, security, privacy, startup, verification and health;
- the owner-approved DEC-0016 semantics are preserved: query/file logging off, identifiable history excluded, client-IP anonymization on, ECS off, and only minimum anonymized aggregate statistics with 24-hour retention;
- the older BACKUP_SCOPE_POLICY.md statistics=false live preflight is explicitly treated as historical and cannot override the current desired state;
- the approximately 30-minute RTO has an exact measurement boundary and required downstream evidence;
- TSK-0446 makes no claim that an actual clean-server timed recovery drill has already occurred;
- master-plan structural validation and git diff checks passed.

This marker verifies the recovery **contract**, not target-environment restoration, production activation, or LG-07 PASS.
