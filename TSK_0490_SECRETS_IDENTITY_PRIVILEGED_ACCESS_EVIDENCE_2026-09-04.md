# TSK-0490 secrets, identity and privileged-access evidence

**Date:** 2026-09-04
**Task:** TSK-0490 - Implement secrets, identity, and privileged-access controls
**Acceptance / verification / evidence:** ACC-0490 / VER-0490 / EVD-0490
**Source commit:** `af8e4d3d1ebf1b958bf40e3c41b01f0ecd4a659c`
**Verifier blob / SHA-256:** `2d6222126223d22f40b073e4d281251303af0195` / `f58a93ead9acb4405b703804a0bb16c3b88f811955d113af1c6e11eb459d8136`
**Workflow blob:** `f777b880891e80e31c8b3ce283368ac46ff11eab`
**WBS / relationship-index blobs:** `20a0674d8f67c673d2c851806ac768f1fe5760a7` / `862c9167dc37ceb12415208065327fd1903edbcc`
**GitHub Actions run / attempt:** `33854568788 / 1`

## Result
**PASS.** ACC-0490 was satisfied without rotating/revoking a production credential, deploying a service, enabling telemetry, processing a participant, or crossing another material-action fence.

- TSK-0450 is current durable PASS; TSK-0490 is A3 / AUTO_ALLOWED under the current WBS.
- A full Git-history scan across unique blobs found no private-key or high-confidence provider-token signature and no forbidden encrypted/private-key container format. Matched content is never emitted.
- External injection was verified with the job-scoped GitHub token under contents-read permission; the value was never printed or persisted.
- Isolated synthetic controls proved credential rotation (old rejected/new accepted), revocation (revoked rejected), bounded break-glass recovery and resealing, restrictive temporary permissions, cleanup and rollback. No production credential was used or changed.
- The existing owner-provided `adguardvm` was checked read-only: the normal executor and repository runner service operate as non-root `azureusr`; the root-capable sudo bridge was exercised only for read-only task-scoped checks and is auditable through this exact Actions run; SSH root login and password authentication remain disabled; inspected SSH/sudo configuration hashes were unchanged.
- Security/privacy evidence contains no secret values, private keys, authentication logs, DNS query history, client identifiers or participant data.
- Current owner fences remain intact: no deployment, telemetry activation, participant-facing mutation, service revocation/removal, payment, public/market activation or launch occurred.

## Evidence integrity
- Source/synthetic transcript SHA-256: `bdbb5d2ea35397a95282557722d235bdc381e5538635c71f0b7ebcf83132e348`
- Target read-only transcript SHA-256: `1a658d84880cf0c7242c2eb40f0ed49f98a9117e797378e2283b52fc60316b3e`
- Independent transcript SHA-256: `eac74ec3b7476058a08398a917b1d73c3e8a2a2cd068c86c2042e9c637887174`

## Non-inference
This PASS proves only TSK-0490. It does not satisfy TSK-0452 or TSK-0489, does not alter TSK-0453 WAITING, and does not create any deployment/activation authority. TSK-0455 remains DEFERRED / WAITING under DEC-0059 / CR-0012 with ACC-0455 / VER-0455 / EVD-0455 unchanged; TSK-0456, TSK-0457 and TSK-0492 remain dependency-blocked.
