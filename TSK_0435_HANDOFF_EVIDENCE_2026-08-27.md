# TSK-0435 — Azure VM Handoff Verification Evidence

**Task:** TSK-0435  
**Acceptance:** ACC-0435  
**Target:** `srv.UseSafeWeb.com` / Azure VM `adguardvm`  
**Evidence source:** Project Owner supplied target-console output from the published verifier executed on the handed-off VM.  
**Verifier:** `infrastructure/adguard-server/verify-handoff.sh`, GitHub blob `0264b6ad15554fd289f4bdbf0ee49b9e959e7843`

## Acceptance criterion

ACC-0435 requires direct Azure metadata proving the owner-provided VM is in `westeurope`, uses the supported Ubuntu baseline, has the intended pilot role/network exposure, is reachable through the approved deployment path, and records identifiers/evidence without secrets.

## Target verification

### Run 1 — 2026-08-27T20:34:37Z

Executed as `sudo bash verify-handoff.sh`. All substantive host checks passed, but the elevated shell did not preserve `SSH_CONNECTION`; verifier correctly ended `OVERALL=FAIL failures=1 warnings=1` rather than falsely proving remote-path reachability.

Preserved valid evidence from this run:

- Ubuntu ID `ubuntu`: PASS.
- Ubuntu version `24.04`: PASS.
- Azure IMDS reachable and JSON parsed: PASS.
- Azure region `westeurope`: PASS.
- Azure OS type `Linux`: PASS.
- Azure VM name `adguardvm`; size `Standard_B2ls_v2`.
- `srv.UseSafeWeb.com` resolved on-target to `52.157.109.120`: PASS.
- IMDS exposed no public IPv4, so DNS-to-IMDS-public-IP correlation was not applicable and remained a warning only.
- Listener inventory showed public SSH only (`0.0.0.0:22`, `[::]:22`) plus loopback/system DHCP/chrony listeners; no AdGuard listener existed yet, consistent with fresh pre-installation handoff.

### Run 2 — 2026-08-27T20:41:57Z

Executed from the remote user shell as:

`bash verify-handoff.sh srv.UseSafeWeb.com`

Result:

- Ubuntu ID: PASS.
- Ubuntu version `24.04`: PASS.
- `PASS  verification is executing through an SSH session`.
- Azure IMDS reachable: PASS.
- Azure metadata JSON parsed: PASS.
- Azure location `westeurope`: PASS.
- Azure OS type Linux: PASS.
- VM identity `adguardvm`, size `Standard_B2ls_v2`: recorded.
- `srv.UseSafeWeb.com` resolved to `52.157.109.120`: PASS.
- IMDS public-IP field absent: warning/not-applicable only.
- Listener inventory remained the expected fresh-host state with externally listening SSH only.
- Final verifier status: **`OVERALL=PASS failures=0 warnings=1`**.

## Security/evidence hygiene

The captured evidence contains no credential, password, token, private key, subscription ID, resource ID, raw DNS history, or other secret. The warning is explicitly non-blocking because Azure IMDS did not expose a public IPv4 field; hostname resolution and the other required target properties were independently observed.

## Acceptance evaluation

- Direct Azure metadata / exact environment: satisfied.
- Azure West Europe region: satisfied.
- Supported Ubuntu 24.04 baseline: satisfied.
- Intended fresh AdGuard/DNS pilot role and current network exposure: satisfied.
- Approved remote deployment-path reachability through SSH: satisfied by Run 2.
- Evidence captured without secrets: satisfied.

## Stable task outcome

**TSK-0435: PASS.**

All elements of ACC-0435 are satisfied by the two target runs, with the second run closing the only unresolved deployment-path assertion. The Run-1 sudo/environment failure is retained for auditability but is superseded for acceptance by the clean non-privileged Run-2 PASS.
