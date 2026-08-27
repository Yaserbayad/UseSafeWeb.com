# TSK-0201 — Secure AdGuard Administration and Change Access Evidence

**Task:** TSK-0201  
**Acceptance:** ACC-0201  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27

## Versioned interface basis

AdGuard Home v0.107.79's official OpenAPI defines `/control/install/configure` for the initial configuration and the generated `InitialConfiguration` model with `web`, `dns`, `username`, `password`, and optional `language`. The versioned server source also shows the first-run handler's bind-validation behavior, which required a safe two-phase web-bind transition when moving the already-listening setup endpoint from wildcard TCP 3000 to loopback TCP 3000.

## Mutation evidence

Workflow: `.github/workflows/adguard-admin-init.yml`  
Successful run: `33121944276`  
Job: `98690689645`  
Result: **PASS**

Canonical script: `infrastructure/adguard-server/initialize-admin.sh`, Git blob `0fa0b3481d9b7173649c72606b40642c278e9c32`.

Observed mutation result:

- existing root-restricted generated admin credential reused; secret value never printed;
- initial authenticated AdGuard configuration applied successfully;
- authenticated local `/control/status`: PASS;
- generated `http.address` hardened from `0.0.0.0:3000` to `127.0.0.1:3000` through a rollbackable config-file transition and service restart;
- authenticated API worked after the restart;
- unauthenticated `/control/status` returned HTTP 401;
- admin listener: `127.0.0.1:3000` only;
- AdGuard DNS listeners: TCP/UDP `127.0.0.1:53` only;
- UFW remained default-deny incoming/default-allow outgoing with only SSH/TCP 22 allowed inbound;
- admin credential file mode/owner: `600 root:root`;
- final markers: `TSK_0201_MUTATION=PASS` and `TSK_0201_WORKFLOW=PASS`.

The first initialization attempt failed safely with HTTP 400 before setup application because AdGuard's first-run handler cannot validate a new loopback bind on port 3000 while its own wildcard setup listener still owns that port. A read-only `/install/check_config` diagnostic then isolated the behavior, and the successful attempt used the versioned handler semantics rather than bypassing validation.

## Independent stable-state audit

Workflow: `.github/workflows/adguard-admin-audit.yml`  
Workflow commit: `d3e8cbf1206e6c0878a297b4864e9717d73bcb71`  
Run: `33121987585`  
Job: `98690840349`  
Result: **PASS**

Fresh audit proved:

- root credential file remains `600 root:root`;
- authorised admin username is `usesafeweb-admin`; password remained unlogged;
- authenticated local control status HTTP 200;
- unauthenticated control status HTTP 401;
- admin listener exactly `127.0.0.1:3000`;
- AdGuard DNS listeners exactly TCP/UDP `127.0.0.1:53`;
- UFW only allows inbound SSH;
- AdGuard service active/enabled;
- persistent GitHub runner service active;
- final marker `FRESH_ADMIN_AUDIT=PASS`.

## Attribution / authorised change path

The authorised administration/change path is the repository-scoped GitHub self-hosted runner executing trusted `main` workflows on `adguardvm`, using the single local admin identity `usesafeweb-admin` through a root-only on-host credential file. Every governed change is attributable through the GitHub commit/workflow/run/job evidence chain. No public admin endpoint is enabled.

## Stable task outcome

**TSK-0201: PASS.**

ACC-0201 is fully satisfied: the admin UI/API is non-public and loopback-only, authentication works and rejects unauthenticated requests, authorised access is recorded, and changes are attributable to the governed GitHub execution chain.
