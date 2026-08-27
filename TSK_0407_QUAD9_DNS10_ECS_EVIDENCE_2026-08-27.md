# TSK-0407 — Quad9 dns10 / ECS-Off Evidence

**Task:** TSK-0407 — Configure Quad9 dns10 and disable ECS  
**Acceptance:** ACC-0407  
**Verification:** VER-0407  
**Evidence:** EVD-0407  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Execution date (UTC):** 2026-08-27

## Authority and eligibility

The canonical WBS row defines TSK-0407 as `A3`, `AUTO_ALLOWED`, HIGH priority, critical-path work with hard predecessors `TSK-0203`, `TSK-0405`, and `TSK-0011`.

Before target verification:

- `TSK-0203` was already directly evidenced PASS on the accepted AdGuard host;
- `TSK-0405` is a canonical completed-record PASS selecting Quad9 `dns10` DoH;
- `TSK-0011`'s publication/read-back condition is satisfied by the owner-frozen planning tree and verified CR-0001 publication/read-back state.

ACC-0407 requires the configured upstream to exactly match `https://dns10.quad9.net/dns-query`, ECS to be disabled, and test evidence to confirm that no ECS endpoint is used.

## Current authoritative external-source check

Official Quad9 documentation checked during execution identifies:

- `https://dns10.quad9.net/dns-query` as the 9.9.9.10 service;
- `dns11.quad9.net` and `dns12.quad9.net` as ECS-enabled variants;
- Quad9's current documentation continues to distinguish dns10 from ECS-enabled endpoints.

Quad9 also announced in April 2026 that, effective 15 June 2026, DNSSEC validation is enabled on the formerly non-validating 9.9.9.10/dns10 service. The announcement explicitly states that ECS behavior remains unchanged. The project contract requires dns10 plus ECS-off; it does not require DNSSEC validation to be disabled, so this current service change does not invalidate ACC-0407 or the frozen upstream choice.

Official AdGuard Home configuration documentation checked during execution confirms that `dns.upstream_dns` defines upstream resolvers and, since v0.107.26, `dns.edns_client_subnet.enabled` controls whether AdGuard Home adds ECS to upstream requests.

## Read-only target preflight

Workflow: `.github/workflows/adguard-upstream-preflight.yml`  
Workflow commit: `78c400409f5f02de13bd266266b32229409cd343`  
Workflow blob after read-back: `6eaf3a4d890c59143e3cb77c83597dd1337de25f`  
Run: `33124332533`  
Job: `98698691502`  
Result: **PASS**

The target directly reported:

- schema version `34`;
- exactly one configured upstream;
- configured upstream exactly `https://dns10.quad9.net/dns-query`;
- no `dns11` or `dns12` entry;
- `upstream_dns_file` empty;
- zero fallback resolvers;
- ECS `enabled=false`, `use_custom=false`, and no custom IP;
- query logging disabled;
- client-IP anonymisation enabled;
- statistics disabled;
- a synthetic local DNS request received a resolver response.

No resolver setting was changed.

## Independent runtime/persisted-state audit

Workflow: `.github/workflows/adguard-upstream-audit.yml`.

### First audit attempt — not accepted as completion

Trigger commit: `2f4181ce6faabbf638c3140140c6d90c5429a9eb`  
Run: `33124383023`  
Job: `98698868690`  
Result: **FAILURE**

The runtime API checks themselves passed:

- exact dns10-only upstream;
- no upstream file override;
- no fallback resolver;
- ECS disabled;
- no ECS endpoint present.

AdGuard's own `/control/test_upstream_dns` returned the tested endpoint as `https://dns10.quad9.net:443/dns-query` with status `OK`. The verifier incorrectly compared that normalized explicit-port form as a literal string against the configured no-port form, so the audit failed. This was a verifier-normalisation defect, not a target configuration defect. No resolver mutation occurred and the failed run was not used to claim PASS.

### Corrected independent audit

Verifier correction commit: `2b05b425dcf0ec499f570248ba4077a0001ee82d`  
Corrected workflow blob after read-back: `5df7da3bd8f9fb8a99cf4cb146bd9263ac95286d`  
Run: `33124417228`  
Job: `98698974470`  
Result: **PASS**

The corrected verifier normalised HTTPS default port 443 while still requiring:

- scheme `https`;
- hostname exactly `dns10.quad9.net`;
- path exactly `/dns-query`;
- no dns11/dns12 endpoint;
- upstream test status `OK`.

It then independently proved both runtime API and persisted `AdGuardHome.yaml` state:

- exact configured upstream `https://dns10.quad9.net/dns-query` and no other upstream;
- empty upstream file;
- zero fallbacks;
- ECS disabled;
- no ECS endpoint present;
- AdGuard built-in dns10 upstream test `OK`;
- query logging remains disabled;
- client-IP anonymisation remains enabled;
- statistics remain disabled;
- a fresh randomized synthetic `*.example.com` DNS request received a valid resolver response (`rcode=0`).

Final marker: `TSK_0407_ACCEPTANCE=PASS`.

## Mutation and rollback disposition

**No resolver mutation was required.** The live runtime and persisted configuration already exactly satisfied the frozen dns10/ECS-off contract. Changing an already-correct upstream would have added avoidable operational risk without improving acceptance evidence.

Because no configuration was changed, rollback was not triggered. Idempotency was satisfied by detecting existing state before change and verifying both runtime and persisted configuration.

## Evidence hygiene

Only synthetic/reserved test names were used. No participant IP address, browsing history, credential, token, private key, or raw user DNS history is included in this evidence.

## Stable task outcome

**TSK-0407: PASS.**

ACC-0407 is satisfied: AdGuard's runtime API and persisted configuration contain exactly `https://dns10.quad9.net/dns-query`, ECS is disabled, no dns11/dns12 or fallback/upstream-file bypass exists, AdGuard's own upstream test returns `OK`, and fresh resolution succeeds while previously verified privacy controls remain intact.
