# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27T21:59Z  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`

`CURRENT_STATE.md` owns volatile runtime state only. Planning authority is the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and routed by `Plans/Master/MANIFEST.yaml`; the WBS owns task definitions/dependencies, the relationship index owns traversal, and Layer 5 owns execution/evidence rules.

## Canonical planning authority

**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0001 PUBLISHED AND READ-BACK VERIFIED.**

- Owner freeze: `TSK-0017` PASS.
- Original frozen publication commit: `fce408f34470c0a0883ab978685b5265fdec4b97`.
- Original frozen `Plans/` tree: `e6c78a67a191e04ea85fbb68caf18b854067c3de`.
- `TSK-0009`, `TSK-0010`, `TSK-0011`: PASS.
- Post-freeze change: `CR-0001` — repair technically impossible AdGuard install/abuse-control dependency ordering.
- CR-0001 publication commit: `904ca6cb0beca7a868d5ca64729d94f5b4d7217d`.
- Validated/published post-CR `Plans/` tree: `c42616e92f0624aaf5caf788b2383a1402393dfd`.
- Final `main` after removing the temporary write-capable workflow: `6617c0c268ad27b928930fc646236662637a8ee6`; read-back confirms `Plans/` remains exactly `c42616e92f0624aaf5caf788b2383a1402393dfd`.
- CR-0001 deterministic validation: **PASS — 25 assembly modules, 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 relationship targets, 0 broken links, 0 generated missing task IDs; 51 checksum entries valid.**
- Independent compare confirms the CR publication changed exactly seven allowlisted planning files and no unrelated path.
- The temporary `contents: write` CR workflow was deleted immediately after successful read-back.

### CR-0001 semantic result

- `TSK-0203 — Install supported AdGuard release` now depends on `TSK-0011` rather than impossible pre-install `TSK-0483` execution.
- `TSK-0483 — Implement resolver abuse and amplification protections` now depends on `TSK-0203`, `TSK-0436`, and `TSK-0011`.
- No task ID, title, scope, status, acceptance criterion, gate, requirement, constraint, interface, risk, capability, action authority, or owner decision changed.
- `TSK-0483` remains mandatory before public resolver activation.

## Frozen product / technical identity

- Brand/domain: **UseSafeWeb / UseSafeWeb.com**.
- Product: **UseSafeWeb — First Phone Safety Setup**.
- Initial validation market: England / UK.
- Backend: **AdGuard Home** unless a verified critical blocker requires reopening.
- Accountless-first baseline under `DEC-0042`.
- Hosting: Microsoft Azure.
- Experiment-1 resolver region: Azure West Europe (`westeurope`).
- AdGuard/DNS VM: `srv.UseSafeWeb.com` / `adguardvm`, Ubuntu 24.04 LTS.
- Upstream: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard is the filtering layer.
- Client resolver identity: `dns.usesafeweb.com`.
- Canonical DoH endpoint: `https://dns.usesafeweb.com/dns-query`.
- Native Android pilot transport: DoT to `dns.usesafeweb.com` on TCP 853.

## Current gate

### LG-03 — Validation Readiness

**IN PROGRESS / TECHNICAL TARGET ACTIVE.**

Current work is technical preparation and target verification. Real participant activation remains governed by its applicable gate requirements.

## Persistent autonomous server execution

GitHub is the active execution bridge for eligible host-side AUTO_ALLOWED work on `adguardvm`.

- repository-scoped self-hosted runner `adguardvm`, runner `2.336.0`, account `azureusr`;
- read-only runner preflight run `33119306556`: PASS;
- non-interactive sudo: PASS;
- persistent systemd runner service bootstrap run `33119643639`: PASS;
- fresh persistent-service verification run `33119676243`: PASS;
- host workflows use trusted `main` push triggers, read-only repository permissions except bounded one-shot authority mutations, `persist-credentials: false` for ordinary host jobs, and serialized concurrency group `usesafeweb-adguard-server`.

This channel replaces manual per-command SSH execution for ordinary eligible server work.

## Current technical task state

### PASS

- `TSK-0435` — Azure VM handoff. Evidence: `TSK_0435_HANDOFF_EVIDENCE_2026-08-27.md`, blob `57de1a4187288870da7655973ac09bf907674d89`.
- `TSK-0437` — host security baseline. Evidence: `TSK_0437_HOST_HARDENING_EVIDENCE_2026-08-27.md`, blob `bb9221657a65c254975f61762af73b16a3e50241`.
- `TSK-0438` — UseSafeWeb.com domain/control owner condition.
- `TSK-0439` — supported pilot device DNS methods. Evidence: `infrastructure/adguard-server/PILOT_DEVICE_DNS_CONFIGURATION_METHODS.md`, blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0440` — encrypted-DNS hostname/path selection. Evidence: `infrastructure/adguard-server/DNS_ENDPOINT_DECISION.md`, blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.

### TSK-0437 accepted stable host state

Mutation run `33119801746` / job `98683551633` and fresh independent audit run `33119961094` / job `98684096030` both PASS:

- Ubuntu 24.04 current installable patches applied;
- public-key admin SSH; root/password/keyboard-interactive SSH disabled;
- UFW default-deny inbound/default-allow outbound; SSH retained;
- unattended security updates enabled;
- no currently installable package upgrades;
- no unexpected external listeners; pre-AdGuard external TCP exposure is SSH only;
- mutation and fresh audit both `OVERALL=PASS failures=0 warnings=0`.

### Newly eligible

- `TSK-0203` — install supported AdGuard release: **TODO / eligible** after CR-0001 and TSK-0437 PASS. It must use an approved official source, record the exact version, install a service that starts automatically, keep administration restricted, and produce target evidence before PASS.

### WAITING / later dependency work

- `TSK-0441` — create public `dns.usesafeweb.com` record: WAITING on an actual DNS-provider execution path; no record is claimed created.
- `TSK-0483` — resolver abuse/amplification controls: correctly waits for `TSK-0203` installation; remains mandatory before public resolver activation.

## Preserved preparation evidence

- `TSK-0166`, `TSK-0168` — Experiment-1 protocol artifacts.
- `TSK-0214` — retention/deletion checklist.
- `TSK-0225` — protection-claims checklist.
- `TSK-0227` — exceptional diagnostic procedure.
- `TSK-0228` — child-safety escalation boundary.
- `TSK-0165` — facilitator/intervention guide.
- `TSK-0169` — support/false-positive intake.
- recurring governance checkpoint: `LG_03_CHECKPOINT_2026-08-27.md`.

## Runtime safeguards

- Runtime states are only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires every applicable current acceptance criterion with durable/reconstructable proof.
- No secrets, credentials, private keys, unnecessary personal data, or raw DNS history in GitHub evidence.
- No public launch until its later gates pass.
- Azure control-plane provisioning/configuration remains owner-managed; GitHub runner autonomy applies to the handed-off VM host and repository-authorized tasks, not Azure control-plane actions.

## Exact next authoritative step

Execute `TSK-0203`: verify the current supported AdGuard Home release from the official AdGuard/GitHub source, install it through the persistent self-hosted runner without opening public resolver ports, restrict the initial administration surface, verify systemd autostart/version/source/integrity/admin exposure in a fresh job, persist evidence, then recompute eligibility before configuring resolver privacy/upstream/abuse controls.
