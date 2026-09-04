# TSK-0450 CI/ephemeral and owner-provided environment evidence

**Date:** 2026-09-04
**Task:** TSK-0450 - Implement CI/ephemeral test environments and the isolated pilot environment
**Acceptance / verification / evidence:** ACC-0450 / VER-0450 / EVD-0450
**Source commit:** `ee48ffed89184024c9cff5a85d4d8a32307135db`
**Verifier blob / SHA-256:** `6ae22f608a3cd8cd689e8e4ada787b153205446a` / `0e1f97ba360cf39baa284c406655f28c8523e212e72fa9f69f6d0f51e41865ad`
**Workflow blob:** `4ab02533fa29aeb0c1c79a83d44a2dbc08bdf5a5`
**WBS / relationship-index blobs:** `20a0674d8f67c673d2c851806ac768f1fe5760a7` / `862c9167dc37ceb12415208065327fd1903edbcc`
**GitHub Actions run / attempt:** `33853498129 / 1`

## Result
**PASS.** ACC-0450 was satisfied without a new Azure resource, persistent staging/pilot environment, service deployment, or participant-facing mutation.

- Hard predecessors TSK-0451, TSK-0422 and TSK-0449 plus LG-07 were current PASS; WBS authority is A3 / AUTO_ALLOWED.
- GitHub-hosted Ubuntu 24.04 CI used deterministic synthetic data only, loopback binding, negative policy fixtures, complete teardown, and deterministic rebuild into a distinct disposable directory; an independent fresh CI job repeated this proof.
- The already owner-provided adguardvm target was verified read-only for approved West Europe region, TSK-0451 access/security policy, and TSK-0422 runtime data/privacy policy. AdGuard configuration remained unchanged.
- Under DEC-0054, this verifies the owner-provided pilot-VM acceptance clause without introducing a mandatory separate pilot/staging lifecycle. The staging trigger was not open and no persistent staging environment was provisioned.
- CR-0012 / DEC-0059 remains unchanged; TSK-0455 clean fresh-host verification is not inferred from this task.
- Rollback/recovery: CI process and directory were removed and verified absent. The target phase was read-only, so target rollback was not applicable.
- Privacy: no participant data, secret, raw query data or client identifier is retained in evidence.

## Evidence integrity
- Ephemeral transcript SHA-256: `a5b8c54c9dd9f0ffc73fccbd0f69a9fb736a3824fb1a5dcd18861ae4de617fe2`
- Target transcript SHA-256: `73974c361ffa3e461007654591b1d8532aa7a1bbadb4ddbefef72f40f203ed5d`
- Independent transcript SHA-256: `8c10a8c3d3455431304c47ad9b5a4aa90ae250d9d9dde849e62a15b9e8a14796`

## Non-inference
This PASS proves only TSK-0450. REQ-0049, REQ-0050, CON-0004, CON-0005, INT-0014, RSK-0048, DEC-0054, DEC-0059 and CR-0012 remain controlling. It does not create/configure Azure control-plane resources; deploy a new environment; process participants; enable telemetry; distribute profiles/certificates; revoke/remove service; make payment; authorize public/market activation; pass a launch gate; or alter TSK-0455, TSK-0456, TSK-0457 or TSK-0492.
