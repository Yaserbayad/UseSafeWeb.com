# TSK-0204 — Persistent Query and File Logging Privacy Evidence

**Task:** TSK-0204  
**Acceptance:** ACC-0204  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Date:** 2026-08-27

## Acceptance intent

The frozen project requirement is stricter than merely observing an empty log: persistent identifiable query logging **and file query logging** must be off, historical query-log data must not remain, and fresh synthetic activity must not be retained. TSK-0204 is `A3 / AUTO_ALLOWED` and owns this control.

Official AdGuard Home configuration documentation distinguishes two query-log controls:

- `querylog.enabled` — query-log status;
- `querylog.file_enabled` — whether query logs are written to a file.

The current query-log implementation reads both values and returns before creating a record when global logging is disabled. Therefore `enabled=false` prevents current query capture, but the project baseline still requires the separate file-writing capability itself to be disabled rather than left latent.

Primary sources checked during correction:

- `https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration`
- `https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/openapi.yaml`
- `https://github.com/AdguardTeam/AdGuardHome/blob/master/internal/querylog/qlog.go`

## Original mutation and evidence

Original workflow: `.github/workflows/adguard-querylog-disable.yml`  
Original run: `33122182026`  
Original job: `98691510253`  
Original implementation blob: `770dcc466d0d0c569aa052105f8ff5c189c8e116`  
Original result: **PASS at the then-tested evidence scope**

It proved:

- authenticated loopback query-log configuration was read;
- `enabled` was set to `false` while API-exposed unrelated fields were preserved;
- prior query-log history was cleared;
- a synthetic `.invalid` query was not retained;
- query-log API item count remained `0`;
- no non-empty `querylog.json*` file remained.

Original independent audit run `33122229571` / job `98691673148` also proved fresh synthetic traffic was not retained, no persistent non-empty query-log file existed, and AdGuard remained active.

### Evidence gap later discovered

The original mutation and independent audit did **not** inspect the separate persisted `querylog.file_enabled` scalar. They therefore proved that logging was not occurring but did not prove every part of the frozen configuration requirement.

## Contradictory current evidence and reopening

While executing the downstream TSK-0202 safe configuration export, corrected read-only run `33126066177` / job `98704396731` directly inspected `AdGuardHome.yaml` and found:

- `querylog.enabled=false`;
- `querylog.file_enabled=true`;
- persistent client count `0`;
- no secrets or query history emitted by the safe-field exporter.

Because global logging was disabled and the current AdGuard implementation returns before adding query-log entries when `enabled=false`, this was **not evidence of an active privacy leak**. However, it contradicted the explicit project requirement that file query logging itself be off. The prior TSK-0204 PASS was therefore reopened rather than silently relied upon, and downstream TSK-0202 was fenced on its hard predecessor.

## Corrective implementation

Canonical implementation was hardened at:

`infrastructure/adguard-server/disable-query-logging.sh`

Final corrected script blob after read-back:

`3018fedb5292c5c302a74ff8b42cada18aec26b5`

The corrected implementation:

1. keeps the supported query-log API globally disabled and clears historical log state;
2. detects persisted `querylog.file_enabled` directly;
3. because the current `/querylog/config` API does not expose `file_enabled`, stops AdGuard before any necessary YAML edit;
4. creates a root-only target-local rollback copy;
5. edits only the `querylog.file_enabled` scalar;
6. restarts AdGuard and waits for authenticated control-API readiness when a restart occurs;
7. verifies persisted query/file logging state plus dns10/ECS, anonymisation, statistics and filter-policy invariants;
8. sends only synthetic `.invalid` DNS activity and verifies it is not retained;
9. verifies no non-empty `querylog.json*` file remains; and
10. removes the temporary rollback copy only after successful verification.

The rollback guard was also corrected to test the root-only backup through `sudo`, so a future failed post-edit verification can actually restore that protected backup.

## First corrective run — failure after desired persisted change

Workflow trigger commit: `1fe373403d8a3b590ea86903fddb5ede741d2cc4`  
Run: `33126239702`  
Job: `98704969927`  
Result: **FAILURE — not accepted as completion**

The run proved before failure:

- global query logging disabled and prior log cleared;
- `querylog.file_enabled` changed to `false`;
- persisted `querylog.enabled=false`;
- persisted `querylog.file_enabled=false`;
- privacy/upstream/filter invariants preserved.

The immediate authenticated query-log API read then returned HTTP `404` during post-restart readiness, so the workflow correctly failed instead of claiming PASS. Subsequent inspection also showed the original rollback condition was not robust for a root-only backup path; that implementation defect was corrected before reuse.

## Independent post-failure target audit

Audit workflow commit: `d31f7a8a13b26746f7f364417f9fe0633b5b7907`  
Audit workflow blob after read-back: `e2e3024f21e9e0fbe5e35eff7b8e3c58e7f944b1`  
Run: `33126279381`  
Job: `98705094275`  
Result: **PASS**

A separate read-only audit directly proved the stable target after the failed workflow:

- `querylog.enabled=false` in persisted YAML;
- `querylog.file_enabled=false` in persisted YAML;
- HTTP admin address remained `127.0.0.1:3000`;
- schema version remained `34`;
- dns10/ECS, anonymisation, statistics and filtering invariants were preserved;
- authenticated `/control/status` returned HTTP `200`;
- authenticated `/control/querylog/config` returned HTTP `200` with global logging disabled;
- authenticated query-log read returned HTTP `200`;
- a fresh synthetic `.invalid` query was not retained;
- query-log item count remained `0`;
- non-empty persistent `querylog.json*` file count remained `0`.

Marker: `TSK_0204_ROLLBACK_AUDIT=PASS`.

This established that the desired file-log-off state itself was stable and that the earlier 404 was transient post-restart readiness, not a persistent control-plane failure.

## Final corrected idempotent control run

Final workflow trigger commit: `6ef36214537b55211b9d66c8e3bd1bdf1965b2fb`  
Final workflow blob after read-back: `0e4d06823a8de5340ff2151d5b3661fd19148871`  
Final script blob: `3018fedb5292c5c302a74ff8b42cada18aec26b5`  
Run: `33126344825`  
Job: `98705307945`  
Result: **PASS**

The final run detected the already-correct state and therefore made no second direct YAML edit. It proved:

- global query logging disabled and historical query-log state cleared;
- `querylog.file_enabled` already `false`;
- persisted `querylog.enabled=false`;
- persisted `querylog.file_enabled=false`;
- dns10/ECS, client-IP anonymisation, disabled statistics and conservative filter-policy invariants preserved;
- API query-log configuration still reports `enabled=false` and anonymisation enabled;
- fresh synthetic query retained: `false`;
- query-log item count: `0`;
- non-empty persistent `querylog.json*` file count: `0`;
- `TSK_0204_MUTATION=PASS`;
- `TSK_0204_WORKFLOW=PASS`.

## Security and evidence hygiene

No administrator password, password hash, token, private key, participant IP, real browsing/domain history, or raw user DNS data is contained in this evidence. Only synthetic `.invalid` names were used for verification. The temporary configuration rollback copy remained root-only on the target and is not persisted in GitHub.

## Stable corrected task outcome

**TSK-0204: PASS.**

ACC-0204 is now fully and directly satisfied at the stronger current evidence level: global query logging is disabled, file query logging is explicitly disabled, prior query-log state is cleared, fresh synthetic activity is not retained, no non-empty persistent query-log file remains, AdGuard/control APIs are healthy, and previously verified resolver/privacy/filter invariants remain intact.
