# TSK-0206 — Client IP Anonymisation Evidence

**Task:** TSK-0206  
**Acceptance:** ACC-0206  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Execution date (UTC):** 2026-08-27

## Acceptance contract

ACC-0206 requires controlled requests to produce only the intended anonymised representation and raw client IP not to be retained in approved logs/statistics. The current privacy baseline also requires query logging and client statistics to remain disabled.

## Initial mutation attempt — not accepted as completion

Workflow: `.github/workflows/adguard-ip-anonymization.yml`  
Trigger commit: `ed07da489ff213986c713e34da265266fd2a74ec`  
Run: `33122650943`  
Job: `98693120873`  
Result: **FAILURE**

The target API mutation itself succeeded and reported:

- `querylog_enabled=false`;
- `anonymize_client_ip=true`;
- `statistics_enabled=false`.

The run then failed its persisted-configuration assertion because the verifier looked for `anonymize_client_ip` under the wrong YAML section. This run was therefore not used to claim PASS and was not blindly retried.

## Verification correction

The persisted verifier was corrected to inspect `dns.anonymize_client_ip` while still checking `querylog.enabled=false`.

Correction commit: `76d3e5b4e6871fa94c4fd1e0ed1467cee9f1b0fc`  
Corrected script: `infrastructure/adguard-server/enable-ip-anonymization.sh`  
Corrected script blob: `6ef152c02b154d4aaba4e851aa43f8e13f15e823`.

The workflow pins this exact script blob before execution.

## Successful mutation and persisted-state verification

Workflow: `.github/workflows/adguard-ip-anonymization.yml`  
Trigger commit: `cf8d603206c98896700b58b0feefb1cfb39c7589`  
Run: `33123662351`  
Job: `98696491164`  
Result: **PASS**

Direct target output proved:

- `querylog_enabled=false`;
- `anonymize_client_ip=true`;
- `statistics_enabled=false`;
- persisted `querylog.enabled=false`;
- persisted `dns.anonymize_client_ip=true`;
- final markers `TSK_0206_MUTATION=PASS` and `TSK_0206_WORKFLOW=PASS`.

## Independent fresh stable-state audit

Workflow: `.github/workflows/adguard-ip-anonymization-audit.yml`  
Workflow commit: `fa55659c42581f21b455d07f05edd438b1726c94`  
Workflow blob after read-back: `390486f2c911cbf0ddedac3667006f543e2367f9`  
Run: `33123701221`  
Job: `98696614657`  
Result: **PASS**

Fresh audit independently proved:

- API query logging remains disabled;
- API client-IP anonymisation remains enabled;
- API statistics remain disabled;
- persisted `querylog.enabled=false`;
- persisted `dns.anonymize_client_ip=true`;
- persisted `statistics.enabled=false`;
- a new synthetic `.invalid` DNS request was not retained in query-log data;
- `top_clients` remained empty;
- stored statistics query count remained `0`;
- no non-empty `querylog.json*` file existed;
- AdGuard Home remained active;
- final marker `FRESH_IP_ANONYMIZATION_AUDIT=PASS`.

## Security and evidence hygiene

Only a synthetic `.invalid` DNS name was used. No participant IP address, browsing history, credential, token, private key, or raw DNS query history is included in this evidence.

## Stable task outcome

**TSK-0206: PASS.**

ACC-0206 is satisfied under the approved privacy baseline: the anonymisation setting is enabled in both the runtime API and persisted configuration, while query logging and statistics remain disabled; fresh controlled DNS activity produces no retained query-log item, no per-client statistics, and no persistent query-log file containing a raw client IP.
