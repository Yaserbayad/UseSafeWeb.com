# TSK-0352 — Current AdGuard Persistent ClientID API / Privacy / Lifecycle Contract Evidence

**Task:** TSK-0352 — Specify AdGuard API, persistent ClientID, privacy and lifecycle contract  
**Acceptance / Verification / Evidence:** ACC-0352 / VER-0352 / EVD-0352  
**Lifecycle / Priority / Capability / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Accepted artifact

- `TSK_0352_POST_CR0008_ADGUARD_PERSISTENT_CLIENTID_API_LIFECYCLE_CONTRACT_2026-09-02.md`
- version `1.0.0-post-CR0008`
- blob `e5cbbcac2f42810527717549482765b6b1ad72c1`
- publication commit `d5bf580f5d416539f9c176c2cec9aa65c69fa8aa`

## 2. Canonical contract / dependency proof

Independent VER-0352 hash-locked:

- WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- graph `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `761a608e37a959b237336d5f44aefefb4dc4fa3f`;
- accepted artifact `e5cbbcac2f42810527717549482765b6b1ad72c1`.

It proved the exact current WBS row:

- L4 / MEDIUM / A3 / `AUTO_ALLOWED`;
- dependencies exactly `TSK-0041; TSK-0142`;
- IDs exactly `ACC-0352 / VER-0352 / EVD-0352`;
- acceptance covers allowlisted server-side client add/search/update/delete, high-entropy ClientID generation, direct DoH endpoint, explicit `ignore_querylog` / `ignore_statistics`, idempotency, authorization, rollback/reconciliation, version compatibility, no arbitrary `/control` proxy and no browser admin credentials.

WBS verification method: `Peer/reviewer inspection against the stated acceptance criteria, source baseline, dependencies, and required evidence.`

WBS evidence requirement: `Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.`

Markers: `TSK0352_INPUT_HASHES=PASS`, `TSK0352_CURRENT_WBS=PASS`, `TSK0352_CURRENT_PREDECESSORS=PASS`.

## 3. Version-pinned upstream source proof

The verifier independently fetched official AdGuard sources:

- `https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/openapi/openapi.yaml`;
- `https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/client/src/__locales/en.json`;
- `https://raw.githubusercontent.com/wiki/AdguardTeam/AdGuardHome/Clients.md`.

It proved:

- AdGuard API version `0.107`, server base `/control`, global `basicAuth`;
- exact persistent-client operations `/clients/add`, `/clients/search`, `/clients/update`, `/clients/delete`;
- client schema supports identifiers plus `ignore_querylog` / `ignore_statistics`;
- exact-search request supports ClientID identifier;
- update/delete request semantics are present;
- v0.107.79 ClientID validation permits only numbers, lowercase letters and hyphens;
- official ClientID documentation supports DoH `/dns-query/<ClientID>` routing.

Markers: `TSK0352_UPSTREAM_FETCH=PASS`, `TSK0352_VERSION_PINNED_API=PASS`, `TSK0352_VERSION_PINNED_CLIENT_SCHEMA=PASS`, `TSK0352_VERSION_PINNED_CLIENTID_SYNTAX=PASS`, `TSK0352_OFFICIAL_DOH_CLIENTID_ROUTE=PASS`.

## 4. Accepted API / ClientID / privacy disposition

VER-0352 proved the artifact restricts the private adapter to named lifecycle operations and prohibits generic customer `/control` proxying.

The contract uses a server-generated 26-character lowercase RFC-4648 base32 ClientID, approximately 130 bits of random space, collision-checked before creation and independent of identity/content fields. High entropy is defense in depth; ClientID remains routing/configuration data rather than authorization.

Every active persistent client explicitly requires `ignore_querylog=true` and `ignore_statistics=true`, while the global privacy baseline remains independently required.

Current persistent DoH endpoint is exactly:

`https://dns.usesafeweb.com/dns-query/{client_id}`

The accountless route remains the same resolver without a persistent ClientID.

Markers: `TSK0352_API_ALLOWLIST=PASS`, `TSK0352_CLIENTID_GENERATION=PASS`, `TSK0352_PRIVACY_SETTINGS=PASS`, `TSK0352_DIRECT_DOH_ENDPOINT=PASS`.

## 5. Lifecycle / authorization disposition

Independent structural inspection proved distinct, bounded create/search/update/rotation/delete contracts with exact read-back before terminal success.

The accepted lifecycle requires server-side parent/device authorization before every consequential operation, rejects customer-supplied identifiers as authority, and includes cross-parent IDOR negative boundaries. ClientID possession is never ownership and AdGuard client/device ownership is never technical Protection Map evidence.

Markers:

- `TSK0352_CREATE_LIFECYCLE=PASS`;
- `TSK0352_SEARCH_LIFECYCLE=PASS`;
- `TSK0352_UPDATE_LIFECYCLE=PASS`;
- `TSK0352_ROTATE_LIFECYCLE=PASS`;
- `TSK0352_DELETE_LIFECYCLE=PASS`;
- `TSK0352_AUTHORIZATION_IDOR=PASS`.

## 6. Idempotency / reconciliation / rollback disposition

The contract assumes no upstream idempotency key. Consequential writes are single-attempt until actual state is re-read; timeouts/disconnects/5xx/ambiguous acknowledgement cause search/read reconciliation before retry. HTTP acknowledgement alone is not terminal proof, and local datastore plus AdGuard terminal truth must agree before customer-facing success.

Rollback is observed-state based. Create orphans, partial rotations and ambiguous deletes are reconciled before repair; recovery cannot resurrect deleted/revoked/cross-parent bindings.

Markers: `TSK0352_IDEMPOTENCY_RECONCILIATION=PASS`, `TSK0352_ROLLBACK_RECOVERY=PASS`.

## 7. Version-drift and downstream test surface

The accepted contract requires exact revalidation of `/control`, client CRUD/search schema, ClientID syntax/routing, privacy fields and CRUD/rotation/authorization/rollback behavior before relying on any AdGuard version change. v0.108+ behavior is not silently imported into the v0.107.79 contract.

The artifact contains exactly 30 deterministic downstream assertions.

Markers: `TSK0352_VERSION_DRIFT_GATE=PASS`, `TSK0352_ASSERTION_CATALOGUE=PASS`.

## 8. Independent VER-0352

Final independent read-only verifier:

- base script `.github/scripts/verify_tsk0352_current_contract.py` — blob `43a4013967c8066ba2c1f79d68a512c49cf9aef3`;
- final Markdown-robust wrapper `.github/scripts/verify_tsk0352_current_contract_v2.py` — blob `11640b9b0c99c0a19440eda7987f3dcd32474539`;
- workflow `.github/workflows/verify-tsk0352-current-contract.yml` — blob `3c3832a66ed03d5cbe5ac8f163b1ae0a97abdfcd`;
- workflow permission: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- run/job `33590945044 / 100124642037`;
- conclusion **SUCCESS**;
- responsible verifier: isolated GitHub Actions job executing hash-locked canonical checks plus version-pinned official-source retrieval.

Final markers also include:

- `TSK0352_STRUCTURE=PASS`;
- `TSK0352_NON_INFERENCE=PASS`;
- `TSK0352_CURRENT_ACC=PASS`;
- `TSK0352_CURRENT_VER=PASS`;
- `TSK0352_CURRENT_EVD_READY=PASS`;
- `TSK0352_CURRENT_CONTRACT=PASS`.

### Diagnostic-only first run

The first read-only run passed every canonical/source/API/ClientID/privacy/DoH check plus create/search lifecycle checks, then failed because a verifier predicate expected plain `server-known current name` while the artifact correctly rendered the field name as Markdown code. No project fact failed and no governed state changed. The v2 wrapper changes only that formatting-sensitive predicate.

A later attempt to download the already-successful final job log hit one transient GitHub protocol disconnect; the same log read succeeded on immediate retry. No workflow rerun or evidence change was needed.

## 9. Acceptance disposition

**ACC-0352 = PASS. VER-0352 = PASS. EVD-0352 = SATISFIED.**

**TSK-0352 current persistent ClientID/API/lifecycle contract: PASS, pending only guarded runtime reconciliation and exact GitHub read-back.**

## 10. Non-inference

This is L4 contract-definition acceptance only. It does not implement/deploy the adapter, call a live AdGuard server, create/update/delete a persistent client, activate account/auth/datastore services, change AdGuard configuration/version, authorize real-user processing, prove platform deployment behavior, publish, launch, pass a lifecycle gate or infer successor PASS.
