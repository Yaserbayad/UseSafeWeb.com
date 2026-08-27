# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T21:51Z  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`

`CURRENT_STATE.md` owns volatile runtime state only. The owner-frozen planning authority remains rooted at `Plans/Master/MASTER_PLAN.md` and routed by `Plans/Master/MANIFEST.yaml`; the WBS owns task definitions/dependencies, the relationship index owns traversal, and Layer 5 owns execution/evidence rules.

## Canonical planning activation

**ACTIVE / OWNER-FROZEN / PUBLISHED / READ-BACK VERIFIED.**

- Owner freeze: `TSK-0017` PASS.
- Frozen planning publication commit: `fce408f34470c0a0883ab978685b5265fdec4b97`.
- Frozen `Plans/` subtree Git tree: `e6c78a67a191e04ea85fbb68caf18b854067c3de`.
- Deterministic freeze validation: **641 tasks / 849 dependency edges / 0 broken links / 51 of 51 checksums**.
- `TSK-0009`, `TSK-0010`, `TSK-0011`: PASS.

## Frozen product / technical identity

- Brand/domain: **UseSafeWeb / UseSafeWeb.com**.
- Product: **UseSafeWeb — First Phone Safety Setup**.
- Initial validation market: England / UK.
- Backend: **AdGuard Home** unless a verified critical blocker requires reopening.
- Accountless-first baseline under `DEC-0042`.
- Hosting: Microsoft Azure.
- Experiment-1 resolver region: Azure West Europe (`westeurope`).
- AdGuard/DNS VM: `srv.UseSafeWeb.com` / Azure VM `adguardvm`, Ubuntu 24.04 LTS.
- Upstream: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard is the filtering layer.
- Client resolver identity: `dns.usesafeweb.com`.
- Canonical DoH endpoint: `https://dns.usesafeweb.com/dns-query`.
- Native Android pilot transport: DoT to `dns.usesafeweb.com` on TCP 853.

## Current gate

### LG-03 — Validation Readiness

**IN PROGRESS / TECHNICAL TARGET ACTIVE.**

Real participant activation remains governed by its applicable gate requirements. Current work is technical preparation and target verification only.

## Persistent autonomous server-execution channel

GitHub is now the approved available execution path for eligible host-side AUTO_ALLOWED work on `adguardvm`.

- repository-scoped self-hosted runner: `adguardvm`, runner `2.336.0`, user `azureusr`;
- read-only runner preflight workflow run `33119306556`: PASS;
- non-interactive `sudo -n`: PASS;
- runner service bootstrap workflow run `33119643639`: PASS;
- fresh persistent-service verification run `33119676243`: PASS;
- `actions.runner.*` systemd service: enabled and active, verified by a fresh job;
- host mutation workflows are restricted to trusted `main` pushes, use `contents: read`, use `persist-credentials: false` where checkout is needed, and share serialized concurrency group `usesafeweb-adguard-server`.

This replaces the earlier manual per-command SSH handoff for ordinary eligible host operations. No persistent RUNNING/lease/claim state is introduced.

## Current technical task state

### PASS

- `TSK-0435` — owner-provided Azure VM handoff. Evidence: `TSK_0435_HANDOFF_EVIDENCE_2026-08-27.md`, blob `57de1a4187288870da7655973ac09bf907674d89`.
- `TSK-0438` — UseSafeWeb.com domain control/registration owner condition.
- `TSK-0440` — encrypted-DNS hostname/path selection. Evidence: `infrastructure/adguard-server/DNS_ENDPOINT_DECISION.md`, blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.
- `TSK-0439` — supported pilot device DNS methods. Evidence: `infrastructure/adguard-server/PILOT_DEVICE_DNS_CONFIGURATION_METHODS.md`, blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0437` — host security baseline. Evidence: `TSK_0437_HOST_HARDENING_EVIDENCE_2026-08-27.md`, blob `bb9221657a65c254975f61762af73b16a3e50241`.

### TSK-0437 accepted host baseline

Mutation workflow run `33119801746`, job `98683551633`, and independent fresh audit run `33119961094`, job `98684096030`, both PASS.

Directly proven stable state:

- Ubuntu 24.04;
- key-based administrative SSH proven before authentication changes;
- root/password/keyboard-interactive SSH disabled; public-key authentication enabled;
- `MaxAuthTries 3`, `LoginGraceTime 30`, empty passwords and X11 forwarding disabled;
- UFW active with default-deny inbound/default-allow outbound and SSH retained;
- unattended security-update mechanism installed/enabled;
- no currently installable package upgrades;
- no unexpected externally listening service; pre-AdGuard external TCP exposure is SSH only;
- no reboot required;
- mutation result `OVERALL=PASS failures=0 warnings=0`;
- fresh independent audit result `OVERALL=PASS failures=0 warnings=0` / `FRESH_AUDIT=PASS`.

ACC-0437 is fully satisfied.

### WAITING / dependency constrained

- `TSK-0441` — create public `dns.usesafeweb.com` DNS record: WAITING on an actual DNS-provider execution path. The desired record is not claimed created.
- `TSK-0483` — resolver abuse/amplification protections: WAITING on an actual resolver service/configuration surface and the WBS sequencing correction below.

## Material WBS sequencing inconsistency

The frozen WBS currently makes `TSK-0203 — Install supported AdGuard release` depend on `TSK-0483 — implement resolver abuse/amplification protections`.

That ordering is technically impossible under the current acceptance contracts: ACC-0483 requires resolver rate-limiting/denial/amplification controls to be implemented and tested on an actual resolver, while the accepted fresh VM has no resolver before TSK-0203 installs AdGuard. No historical or planning evidence can substitute for the missing live resolver.

**Required resolution:** perform the smallest governed WBS/dependency correction that allows installation of the supported AdGuard release before live resolver-abuse implementation/testing, while keeping TSK-0483 mandatory before public resolver activation. Do not mark either task PASS by inference.

## Preserved preparation evidence

- `TSK-0166`, `TSK-0168` — Experiment-1 protocol artifacts.
- `TSK-0214` — `RETENTION_DELETION_EXECUTION_CHECKLIST.md`.
- `TSK-0225` — `PROTECTION_CLAIMS_CHECKLIST.md`.
- `TSK-0227` — `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md`.
- `TSK-0228` — `CHILD_SAFETY_ESCALATION_PROCEDURE.md`.
- `TSK-0165` — `EXPERIMENT_01_FACILITATOR_GUIDE.md`.
- `TSK-0169` — `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`.
- recurring governance checkpoint: `LG_03_CHECKPOINT_2026-08-27.md`.

## Runtime safeguards

- Runtime states are only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires every applicable current acceptance criterion with durable/reconstructable proof.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS history in GitHub evidence.
- No public launch until its later gates pass.
- Azure control-plane provisioning/configuration remains owner-managed under the current boundary; GitHub runner autonomy applies to the handed-off VM host and repository-authorized tasks, not Azure control-plane actions.

## Exact next authoritative step

Reconcile the `TSK-0203` / `TSK-0483` dependency inversion through the smallest authoritative WBS/relationship correction, validate/read back the planning tree as required, then recompute eligibility. If the corrected chain authorizes `TSK-0203`, use the persistent GitHub runner to install and independently verify the supported AdGuard Home release before configuring resolver-abuse controls or opening public resolver ports.
