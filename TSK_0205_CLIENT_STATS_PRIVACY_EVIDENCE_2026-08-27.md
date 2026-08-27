# TSK-0205 — Identifiable Client Statistics Privacy Evidence

**Task:** TSK-0205  
**Acceptance:** ACC-0205  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27

## Versioned interface basis

AdGuard Home v0.107.79's statistics service exposes `GET/PUT /control/stats/config`, an explicit `enabled` flag, `GET /control/stats` including `top_clients`, and `POST /control/stats_reset`. The server implementation persists the configured enabled state and does not accumulate statistics while disabled.

## Mutation evidence

Workflow: `.github/workflows/adguard-stats-disable.yml`  
Run: `33122472506`  
Job: `98692503341`  
Result: **PASS**

Canonical implementation: `infrastructure/adguard-server/disable-client-statistics.sh`, Git blob `a3955852b8e7b8270de777ffa8a31c8ffbd5371d`.

Observed target result:

- statistics configuration updated to `enabled=false` while unrelated configuration was preserved;
- existing statistics reset;
- post-change config: `stats_enabled=false`;
- synthetic DNS request after disablement produced `top_clients_count=0`;
- total stored statistics query count remained `0`;
- persisted `/opt/AdGuardHome/AdGuardHome.yaml` recorded `statistics.enabled=false`;
- final markers: `TSK_0205_MUTATION=PASS`, `TSK_0205_WORKFLOW=PASS`.

## Independent fresh stable-state audit

Workflow: `.github/workflows/adguard-stats-audit.yml`  
Workflow commit: `53fdf8ad8f785ea354e501780cde24e3073c3ec3`  
Run: `33122513746`  
Job: `98692650302`  
Result: **PASS**

Fresh audit proved:

- statistics remain disabled;
- a new synthetic query did not create any `top_clients` record;
- total stored statistics query count remained zero;
- persisted YAML still records `statistics.enabled=false`;
- AdGuard service remained active;
- final marker `FRESH_STATS_AUDIT=PASS`.

## Security/evidence hygiene

Only synthetic `.invalid` names were used. No participant address, browsing history, credential, token, or private key is present in the evidence.

## Stable task outcome

**TSK-0205: PASS.**

ACC-0205 is fully satisfied: identifiable per-client statistics are disabled rather than merely hidden, prior statistics are reset, the UI/API configuration reflects the disabled state, the persisted configuration reflects the disabled state, and fresh DNS activity does not repopulate `top_clients`.
