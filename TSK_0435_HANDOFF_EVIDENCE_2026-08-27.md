# TSK-0435 — Azure VM Handoff Verification Evidence

**Task:** TSK-0435  
**Acceptance:** ACC-0435  
**Target:** `srv.UseSafeWeb.com` / Azure VM `adguardvm`  
**Target test timestamp:** `2026-08-27T20:34:37Z`  
**Evidence source:** owner-provided target-console output from executing the published verifier on the handed-off VM  
**Verifier artifact:** `infrastructure/adguard-server/verify-handoff.sh`

## Acceptance criterion

ACC-0435 requires direct Azure metadata proving the owner-provided VM is in `westeurope`, uses the supported Ubuntu baseline, has the intended pilot role/network exposure, is reachable through the approved deployment path, and records evidence without secrets.

## Verified target results

The supplied target execution proves:

- Ubuntu OS ID: **PASS** (`ubuntu`).
- Ubuntu version: **PASS** (`24.04`).
- Azure Instance Metadata Service reachable: **PASS**.
- Azure metadata JSON parsed: **PASS**.
- Azure region: **PASS** (`westeurope`).
- Azure OS type: **PASS** (`Linux`).
- Azure VM name: `adguardvm`.
- Azure VM size: `Standard_B2ls_v2`.
- Expected hostname resolution: **PASS** — `srv.UseSafeWeb.com` resolved from the VM to `52.157.109.120`.
- Public-IP correlation through IMDS: **not applicable / warning only** because this VM's IMDS response exposed no public IPv4 value.
- Listener inventory at handoff:
  - TCP `0.0.0.0:22`
  - TCP `[::]:22`
  - local-only resolver/system listeners on loopback
  - DHCP/chrony/system UDP listeners
  - no AdGuard service listeners yet, consistent with a fresh pre-installation handoff.

No credential, token, private key, subscription ID, resource ID, raw DNS history, or other secret is contained in this evidence.

## Single failed verifier assertion

The verifier reported:

`FAIL  SSH_CONNECTION is absent; approved remote deployment-path reachability is not proven`

The command was invoked as:

`sudo bash verify-handoff.sh`

Running the verifier under `sudo` removed the user session's `SSH_CONNECTION` environment variable before the script evaluated it. Therefore this failure does **not** contradict any of the Azure/Ubuntu/DNS/network-exposure evidence above; it leaves only the approved remote deployment-path reachability assertion unproven by this test run.

The verifier's final status was therefore correctly fail-closed:

`OVERALL=FAIL failures=1 warnings=1`

## Stable task outcome

**TSK-0435 remains WAITING**, with all ACC-0435 elements evidenced except explicit approved deployment-path reachability.

### Deterministic resolution check

From the same remote shell session, rerun the read-only verifier **without `sudo`**:

```bash
bash verify-handoff.sh srv.UseSafeWeb.com
```

If the rerun reports:

- `PASS  verification is executing through an SSH session`, and
- `OVERALL=PASS`

then the remaining ACC-0435 element is satisfied and TSK-0435 can be promoted to PASS after durable result/read-back reconciliation.
