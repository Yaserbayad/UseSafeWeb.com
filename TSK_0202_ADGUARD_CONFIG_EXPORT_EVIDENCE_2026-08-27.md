# TSK-0202 — Approved AdGuard Configuration Export Evidence

**Task:** TSK-0202  
**Acceptance:** ACC-0202  
**Evidence:** EVD-0202  
**Verification:** VER-0202  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**AdGuard Home:** v0.107.79  
**Date:** 2026-08-27

## Authoritative task contract

The canonical WBS row was reread from `Plans/Master/WBS/master-wbs.csv` through workflow run `33127005407` / job `98707426869`.

Current task metadata:

- AI capability: `A3`;
- Action authority: `AUTO_ALLOWED`;
- priority: `HIGH`;
- critical path: `YES`;
- hard predecessors: `TSK-0204`, `TSK-0205`, `TSK-0206`, `TSK-0406`, `TSK-0201`, `TSK-0011`;
- acceptance: **the artifact reproduces the approved settings, excludes secrets and query history, and is linked to the deployment evidence**.

All hard predecessors are satisfied by current direct PASS/publication-readback evidence before this task is accepted.

Linked controls were rechecked before publication:

- `CON-0007`: persistent identifiable query logging and file query logging are off;
- `CON-0008`: identifiable per-client statistics are off/excluded unless specifically justified;
- `INT-0007`: actual behavior/configuration must match the documented data-flow reality;
- `REQ-0019`: processing/data/safeguard documentation must reflect actual reality;
- `REQ-0022` remains intentionally unresolved under the owner's legal-work deferral and is **not** satisfied, waived, or inferred non-applicable by this technical task.

No real England participant activation is authorized by this PASS.

## Fresh corrected live export

Canonical exporter after read-back:

`.github/workflows/adguard-approved-config-export.yml`

Workflow blob:

`a02dca9e536d7c036b44a5dadea19cd9cdb26a98`

Trigger commit:

`b977e55345c72ea7f9c4f42de194ab73589537e0`

Run / job:

- run `33127050108`;
- job `98707574318`;
- result: **PASS**.

The exporter first required the current approved pre-public invariants to be true before emitting any settings. Direct checks included:

- admin HTTP address is loopback `127.0.0.1:3000`;
- DNS bind is loopback-only;
- upstream is exactly `https://dns10.quad9.net/dns-query`;
- no fallback upstream and ECS disabled;
- client-IP anonymisation enabled;
- resolver rate limit `20`, IPv4 `/24`, IPv6 `/56`, empty rate-limit whitelist, `refuse_any=true`;
- filtering/protection enabled with `blocking_mode=default`;
- only the AdGuard DNS filter is active;
- query logging disabled;
- file query logging disabled;
- statistics disabled;
- no whitelist filters;
- no user rules;
- no persistent clients.

The exporter then emitted only an explicit safe-field allowlist. It did not export the raw `AdGuardHome.yaml`.

Observed fresh settings SHA-256:

`327c374d46fc40c03a847a57d7078df6035edc71710eb8725ce57c69ac8a93a8`

Markers:

- `approved_invariants=PASS`;
- `sensitive_field_guard=PASS`;
- `TSK_0202_SAFE_EXPORT=PASS`.

## Versioned artifact

Artifact:

`infrastructure/adguard-server/approved-adguard-config-v1.json`

Artifact version:

`1.0.0`

Git blob after direct GitHub read-back:

`ea85830b5ef9de7f2772e5467570d52013228b0b`

Publication commit:

`3d58f8f70d29134c847559078108ad4f9df9bb4a`

The artifact contains:

- target/version metadata;
- the secret-safe approved settings object;
- the deterministic settings SHA-256;
- source exporter run/job/commit identity;
- links to the existing installation, administration, privacy, filtering, upstream, abuse-protection, and host-hardening evidence.

It explicitly records that it is **not** a complete raw AdGuard configuration backup. Authentication material, certificate private material, query history, client-identifying records, and volatile runtime data remain excluded from Git and must be handled only through separately approved protected mechanisms.

## Independent exact-match audit

Independent audit workflow:

`.github/workflows/adguard-approved-config-audit.yml`

Workflow blob after direct read-back:

`c70846f2b5f6b702e0af5d5463d50a5a8dad841a`

Trigger commit:

`0011b4498ac06a08202b9df3dd43b9443b60cdd5`

Run / job:

- run `33127141644`;
- job `98707868115`;
- result: **PASS**.

The audit independently proved:

1. the checked-out artifact Git blob is exactly `ea85830b5ef9de7f2772e5467570d52013228b0b`;
2. artifact schema/task/version metadata are correct for TSK-0202;
3. the canonicalized artifact settings hash is exactly `327c374d46fc40c03a847a57d7078df6035edc71710eb8725ce57c69ac8a93a8`;
4. forbidden sensitive configuration keys are absent from the settings object;
5. no private-key marker, administrator-password assignment, or query-log file content is present in the artifact;
6. query logging and file logging are both disabled in the artifact;
7. statistics are disabled, anonymisation is enabled, ECS is disabled, and user/whitelist rules are empty;
8. all **9** declared linked evidence paths exist at the exact declared Git blobs;
9. an independently regenerated safe settings object from current `/opt/AdGuardHome/AdGuardHome.yaml` equals the versioned artifact exactly;
10. the independently regenerated live settings hash is also `327c374d46fc40c03a847a57d7078df6035edc71710eb8725ce57c69ac8a93a8`;
11. persistent client count remains `0`;
12. non-empty `querylog.json*` file count remains `0`.

Final markers:

- `artifact_sensitive_field_guard=PASS`;
- `artifact_evidence_links_verified=9`;
- `live_to_artifact_exact_match=true`;
- `persistent_querylog_files=0`;
- `TSK_0202_INDEPENDENT_AUDIT=PASS`.

## Linked deployment evidence verified by the audit

The artifact links and the audit verifies exact Git blobs for:

- TSK-0203 — supported AdGuard installation;
- TSK-0201 — restricted authenticated administration;
- TSK-0204 — query/file logging disabled;
- TSK-0205 — identifiable client statistics disabled;
- TSK-0206 — client-IP anonymisation;
- TSK-0406 — conservative filtering policy;
- TSK-0407 — exact Quad9 dns10/ECS-off upstream;
- TSK-0483 — resolver abuse/amplification controls;
- TSK-0437 — host hardening baseline.

## Security and privacy evidence hygiene

No administrator credential, password hash, token, private key, certificate private material, participant IP, persistent client record, browsing/domain history, raw DNS query history, or other unnecessary personal data is stored in the versioned artifact or this evidence.

The artifact is therefore a reproducible **non-secret approved-settings manifest**, not a secret-bearing recovery backup.

## Stable task outcome

**TSK-0202: PASS.**

ACC-0202 is fully satisfied: the versioned artifact reproduces the current approved safe settings exactly, excludes secrets and query history/client-identifying records, and links to deployment evidence whose exact Git blobs were independently verified. The artifact-to-live equality and settings checksum are directly reproducible from the current target.
