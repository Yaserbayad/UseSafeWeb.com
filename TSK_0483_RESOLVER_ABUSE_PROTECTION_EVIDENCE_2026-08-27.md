# TSK-0483 — Resolver Abuse and Amplification Protection Evidence

**Task:** TSK-0483 — Implement resolver abuse and amplification protections  
**Acceptance:** ACC-0483  
**Verification:** VER-0483  
**Evidence:** EVD-0483  
**Target:** `srv.UseSafeWeb.com` / `adguardvm`  
**Execution date (UTC):** 2026-08-27

## Authority and predecessor reconciliation

The canonical WBS row defines TSK-0483 as `A3`, `AUTO_ALLOWED`, high priority, critical-path work with hard predecessors `TSK-0203`, `TSK-0436`, and `TSK-0011`.

Before target testing:

- `TSK-0203` was already directly evidenced PASS on the accepted AdGuard host.
- `TSK-0436` is explicitly `NOT_APPLICABLE + PASS`: Azure NSG/control-plane configuration remains owner-managed, while actual handed-off exposure/security still requires project verification.
- `TSK-0011`'s publication/read-back condition is satisfied by the owner-frozen modular planning system plus the verified CR-0001 publication/read-back state. CR-0001 specifically repaired the impossible predecessor edge so installed AdGuard precedes TSK-0483 and retained TSK-0483 as mandatory before public resolver activation.

## Acceptance contract

ACC-0483 requires:

1. unauthorised query patterns are rate-limited or denied;
2. amplification exposure is tested; and
3. limits do not block the intended pilot cohort.

The task is reversible/idempotent by default. Existing state must be detected before change; unnecessary mutation is not permitted.

## Current product-source baseline

AdGuard Home's current official configuration reference documents these anti-amplification controls:

- `ratelimit` limits handled DNS queries per second and silently drops excess traffic;
- `ratelimit_subnet_len_ipv4` / `ratelimit_subnet_len_ipv6` define rate-limit aggregation subnet lengths;
- `ratelimit_whitelist` exempts explicitly listed addresses;
- `refuse_any` refuses DNS `ANY` requests to mitigate reflection/amplification.

Source reviewed during execution: AdGuardTeam/AdGuardHome official Configuration wiki, current as of 2026-08-27: `https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration`.

## Preflight verifier corrections — not accepted as completion

Two read-only verifier runs were used to inspect the target before acceptance:

- Run `33124007401` exposed the live configuration but failed because the UFW-reporting helper contained a syntax error.
- Run `33124063423` completed all substantive checks but failed cleanup of a root-owned temporary file.

Neither run was used to claim PASS. Neither changed AdGuard, UFW, DNS exposure, or any resolver setting.

The second run nevertheless established the live baseline before the final acceptance run:

- `ratelimit=20`;
- IPv4 rate-limit subnet `/24`;
- IPv6 rate-limit subnet `/56`;
- zero rate-limit whitelist entries;
- `refuse_any=true`;
- no wildcard IPv4 or IPv6 DNS bind;
- query logging disabled;
- client-IP anonymisation enabled;
- statistics disabled;
- UFW active with default incoming deny and no DNS/DoT allow-rule mentions;
- an 80-query burst received 19 responses and dropped 61.

## Final acceptance run

Workflow: `.github/workflows/adguard-abuse-preflight.yml`  
Workflow trigger commit: `9160a348c607c07046b285af64342d5444df1f06`  
Workflow blob after read-back: `029381d7862053cd12deee6618c4431befbfb7cb`  
Run: `33124114154`  
Job: `98697977476`  
Result: **PASS**

### Configuration and exposure checks

The target directly proved:

- DNS port `53`;
- `ratelimit=20`;
- `ratelimit_subnet_len_ipv4=24`;
- `ratelimit_subnet_len_ipv6=56`;
- `ratelimit_whitelist_count=0`;
- `refuse_any=true`;
- one configured bind host, with no public wildcard bind and no non-loopback IPv4 bind;
- `querylog_enabled=false`;
- `anonymize_client_ip=true`;
- `statistics_enabled=false`;
- UFW active;
- UFW default incoming policy deny;
- no DNS port 53 or DoT port 853 allow-rule mention in current UFW state.

This confirms the resolver remains pre-public and cannot presently be reached as a public recursive endpoint from the host boundary.

### Intended-pilot traffic check

A bounded low-rate synthetic DNS sequence sent 8 requests and received 8 responses.

Result: **8/8 pass**. The configured rate limit did not block representative low-rate pilot traffic.

### Amplification check

A synthetic DNS `ANY` request received response code `4` (`NOTIMP`) with response/query byte ratio `1.00`.

Result: the server refused the `ANY` request and did not amplify it.

### Rate-limit check

A bounded burst sent 80 synthetic UDP DNS requests in approximately 0.6 ms.

- Sent: `80`
- Responses received: `20`
- Silently dropped: `60`

Result: excess traffic was rate-limited while normal low-rate traffic remained functional.

## Mutation and rollback disposition

**No resolver mutation was required.** The live AdGuard configuration already contained bounded anti-amplification settings that satisfied ACC-0483, so changing rate values, subnet aggregation, access lists, or `refuse_any` without a project-specific need would have added risk without improving the acceptance outcome.

Because no configuration was changed, rollback was not triggered. The task's idempotency requirement was satisfied by detecting and verifying the existing stable state before mutation.

## Scope boundary for later public activation

This PASS establishes the pre-public server-side abuse/amplification controls required by TSK-0483. It does **not** authorize opening resolver ports, changing Azure NSG rules, widening AdGuard bind addresses, or launching a public resolver. Any later exposure change must preserve these controls and re-run external exposure/abuse verification under the applicable downstream task/gate before public activation.

## Evidence hygiene

Only synthetic `.invalid` DNS names were used. No participant IP address, browsing history, credential, token, private key, or raw user DNS history is included in this evidence.

## Stable task outcome

**TSK-0483: PASS.**

ACC-0483 is satisfied on the current target: excess query bursts are rate-limited, `ANY` reflection/amplification is refused and measured, representative low-rate traffic remains functional, and the resolver remains non-public behind the existing network boundary. Privacy controls verified in TSK-0204/0205/0206 remained unchanged.
