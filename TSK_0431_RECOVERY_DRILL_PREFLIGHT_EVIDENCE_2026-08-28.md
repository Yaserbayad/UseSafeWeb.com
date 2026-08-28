# TSK-0431 — Clean Restore/Rebuild Drill Preflight Evidence

**Task:** TSK-0431  
**Acceptance:** ACC-0431  
**Verification:** VER-0431  
**Evidence:** EVD-0431  
**Date:** 2026-08-28  
**Stable outcome:** WAITING

## Authoritative task contract

The canonical WBS defines TSK-0431, `Test pilot restore or rebuild procedure`, as L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0430; TSK-0011`, both currently satisfied.

ACC-0431 requires: **the test target becomes functional, passes encrypted DNS and privacy checks, and recovery time/issues are recorded.**

VER-0431 requires execution in the target environment with functional, negative, configuration, security/privacy and rollback checks.

REQ-0052 further requires a **timed clean-server restore/rebuild drill** covering end-to-end restoration: host baseline, packages, AdGuard, server-managed configuration recovery, firewall/network, endpoint, TLS, filters, privacy, startup, Azure-native backup/restore, verification and health.

CON-0019 fixes the recovery baseline to a **fresh Ubuntu 24.04 LTS owner-provided reachable Azure VM** and states Azure VM/control-plane creation/configuration is outside project automation.

CON-0004 likewise prohibits project automation from creating or configuring Azure control-plane resources unless the owner explicitly reopens that boundary.

RSK-0048 requires independent timed clean-server acceptance and treats unsafe partial service, secret leakage, failed recovery criteria or exceeding the approximately 30-minute recovery target as a critical-control failure.

## Current prerequisite evidence

TSK-0430 is PASS. The exact encrypted source backup is independently verified and owner-decryptable:

- created UTC: `2026-08-27T23:56:12Z`;
- ciphertext SHA-256: `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`;
- owner recipient fingerprint: `SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`;
- owner-side decrypted configuration SHA-256: `d8b6eae3b85edbaa1c49e318354389dc616099ecb3d2d90eff3c3dd8c663e1f2`;
- durable TSK-0430 evidence blob: `de1820cb2a9fc5b175c5e5eb1e18b45e6a430a82`.

The production DNS VM is the current single lean AdGuard node. It is not a clean test target. Destructively rebuilding it merely to satisfy TSK-0431 would introduce avoidable outage/security/privacy risk and would not provide independent clean-target evidence.

The current frozen endpoint contract is `dns.usesafeweb.com` with DoH path `/dns-query` and Android pilot DoT on port 853, but the public DNS record task TSK-0441 and TLS certificate task TSK-0442 have not yet passed. Therefore the required encrypted-DNS/TLS component of the clean recovery acceptance cannot currently be demonstrated end-to-end on a clean target.

No Azure control-plane action was performed, no new VM was created, and no production service/configuration was mutated during this preflight.

## Deterministic WAITING condition

TSK-0431 remains **WAITING**, not PASS, until the following test inputs exist:

1. an owner-provided, reachable, fresh Ubuntu 24.04 LTS Azure test target in the approved West Europe boundary, isolated from the live DNS node and containing no participant data;
2. approved project automation access to that handed-off host with the required non-interactive privileged path, without exposing owner secrets;
3. the endpoint/TLS inputs needed to verify encrypted DNS on the restored target (normally the verified public DNS/TLS chain from TSK-0441/TSK-0442, or another owner-approved equivalent that proves the same acceptance semantics);
4. an owner-managed Azure-native backup/restore interface or evidence path sufficient to exercise and record the Azure-native recovery component required by REQ-0052.

When these conditions are present, the project may execute the timed clean-server drill, verify every ACC-0431 element, record elapsed recovery time/issues and rollback behavior, and only then consider PASS.

## Stable classification

**TSK-0431: WAITING — exact external test-target / Azure-control-plane / endpoint-TLS prerequisites are not yet available.**

This is a platform/owner-managed infrastructure boundary, not a failed implementation. No acceptance criterion has been waived or weakened.
