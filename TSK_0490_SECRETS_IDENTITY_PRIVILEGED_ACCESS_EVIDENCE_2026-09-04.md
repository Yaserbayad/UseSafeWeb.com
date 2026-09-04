# TSK-0490 secrets, identity and privileged-access evidence

**Date:** 2026-09-04
**Task:** TSK-0490 - Implement secrets, identity, and privileged-access controls
**Acceptance / verification / evidence:** ACC-0490 / VER-0490 / EVD-0490
**Authoritative v2 source commit:** `4cbc7e3e1fa6e6c4ea248f289de906ff0b2bf580`
**Verifier blob / SHA-256:** `2d6222126223d22f40b073e4d281251303af0195` / `f58a93ead9acb4405b703804a0bb16c3b88f811955d113af1c6e11eb459d8136`
**V2 workflow blob:** `0ac50bd25fd25970cf99ac4f80b021b7ac4047b4`
**WBS / relationship-index blobs:** `20a0674d8f67c673d2c851806ac768f1fe5760a7` / `862c9167dc37ceb12415208065327fd1903edbcc`
**V2 run / attempt:** `33854838835 / 1`

## Result
**PASS.** Hardened v2 verification independently satisfies ACC-0490 / VER-0490 / EVD-0490 and supersedes the earlier run-3 evidence quality gap.

- Full Git history contains no detected complete plausible PEM private-key material, high-confidence provider-token signature, or forbidden encrypted/private-key container. The earlier lone-header hit was verified as a negative test assertion in historical TSK-0355 verifier source, not key material.
- Job-scoped external secret injection was verified without printing or persisting the value.
- Isolated synthetic tests proved rotation, revocation, bounded break-glass recovery/resealing, restrictive transient permissions, cleanup and rollback; no production credential was used or changed.
- Existing `adguardvm` was verified read-only: normal executor and runner are non-root `azureusr`; bounded root-capable checks are auditable; SSH root login/password authentication are disabled; inspected SSH/sudo configuration was unchanged.
- Source, target and independent transcripts passed an independent complete-PEM/provider-credential sanitizer.
- No deployment, telemetry activation, participant-facing mutation, production credential rotation/revocation, service revocation/removal, payment, activation or launch occurred.

## Evidence integrity
- Source transcript SHA-256: `00132a128d0486e114d1dbfe6a2a8e7698992fb93acf0df1b91723e4c4540151`
- Target transcript SHA-256: `ed3e363f7e39fa1c2f7654b0454238aecb9b52bd68945c7651bb41273d739e92`
- Independent transcript SHA-256: `ab1e4cb05ea81923c0f2a25fbbf25be8f50811f7b900cb6a3941569ffea73b20`

## Non-inference
TSK-0453 remains WAITING. TSK-0455 remains DEFERRED / WAITING under DEC-0059 / CR-0012 with ACC-0455 / VER-0455 / EVD-0455 unchanged. TSK-0456, TSK-0457 and TSK-0492 remain dependency-blocked. No successor/gate/deployment/activation/launch/service-revocation/telemetry/payment/participant PASS is inferred.
