# TSK-0204 — Persistent Query Logging Privacy Evidence

**Task:** TSK-0204  
**Acceptance:** ACC-0204  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27

## Versioned interface basis

AdGuard Home v0.107.79 exposes query-log configuration through its authenticated control API. The versioned client model `GetQueryLogConfigResponse` defines the persistent query-log state including `enabled`, `interval`, `anonymize_client_ip`, and ignored-host settings. The versioned server query-log implementation uses `querylog.json` as its persistent query-log file name.

## Mutation evidence

Workflow: `.github/workflows/adguard-querylog-disable.yml`  
Run: `33122182026`  
Job: `98691510253`  
Result: **PASS**

Canonical implementation: `infrastructure/adguard-server/disable-query-logging.sh`, Git blob `770dcc466d0d0c569aa052105f8ff5c189c8e116`.

Observed target result:

- existing query-log configuration was read through the authenticated loopback control API;
- unrelated query-log fields were preserved while `enabled` was set to `false`;
- prior query-log history was explicitly cleared;
- post-change API state: `querylog_enabled=false`;
- synthetic DNS request `usesafeweb-log-test.invalid` was sent directly to the loopback AdGuard resolver;
- synthetic request was not retained in query-log API output;
- query-log item count after clear/test: `0`;
- no non-empty `querylog.json*` file remained beneath `/opt/AdGuardHome`;
- final markers: `TSK_0204_MUTATION=PASS`, `TSK_0204_WORKFLOW=PASS`.

The observed `anonymize_client_ip=false` value was deliberately not changed by this task because TSK-0206 owns that separate privacy control.

## Independent fresh stable-state audit

Workflow: `.github/workflows/adguard-querylog-audit.yml`  
Workflow commit: `fb6666527666434e5d1f8a2f682c809522a6993e`  
Run: `33122229571`  
Job: `98691673148`  
Result: **PASS**

Fresh audit proved:

- query-log configuration remains `enabled=false`;
- a new synthetic DNS request `usesafeweb-fresh-audit.invalid` was not retained;
- query-log API item count remained `0`;
- persistent non-empty `querylog.json*` files remained `0`;
- AdGuard service remained active;
- persistent GitHub runner service remained active;
- final marker: `FRESH_QUERYLOG_AUDIT=PASS`.

## Security/evidence hygiene

No administrator password, token, private key, real user query/domain history, or other secret/personal DNS data is present in this evidence. Only synthetic `.invalid` names were used for verification.

## Stable task outcome

**TSK-0204: PASS.**

ACC-0204 is fully satisfied: persistent query logging is disabled, prior history is cleared, synthetic DNS activity is not retained through the query-log API, and no non-empty persistent query-log file remains after an independent fresh verification.
