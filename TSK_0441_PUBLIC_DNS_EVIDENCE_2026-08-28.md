# TSK-0441 — Public DNS Record Evidence

**Task:** TSK-0441  
**Acceptance:** ACC-0441  
**Evidence date:** 2026-08-28  
**Result:** PASS

## Authority and prior boundary

The canonical runtime/WBS preflight defines TSK-0441 as L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0440; TSK-0435; TSK-0011`, all already satisfied. ACC-0441 requires `dns.usesafeweb.com` to resolve to the correct pilot target from multiple resolvers with no stale or conflicting record.

The prior deterministic WAITING condition required the owner/provider to create a DNS-only A record `dns.usesafeweb.com` -> `52.157.109.120`, with no baseline AAAA or CNAME, followed by independent multi-resolver read-back. Preflight evidence remains `TSK_0441_PUBLIC_DNS_PREFLIGHT_EVIDENCE_2026-08-28.md`, blob `a4c5365507fa9ffb9803872ace7fe78a4c9aec01`.

## Current independent verification

After the owner reported the provider-side record created, GitHub Actions run `33156757093` executed two read-only probes on exact `main` commit `044657d39d0622fdcb88e1d0f739f0449816cf69`, with `contents: read` and no persisted checkout credentials.

The probes ran independently on:

- job `98801252982` — runner `adguardvm`;
- job `98801253193` — runner `adguartestdvm`.

Both jobs completed successfully and returned the same DNS state:

- system resolver A: `52.157.109.120`;
- Cloudflare `1.1.1.1` A: `52.157.109.120`; AAAA: none; CNAME: none;
- Google `8.8.8.8` A: `52.157.109.120`; AAAA: none; CNAME: none;
- Quad9 `9.9.9.9` A: `52.157.109.120`; AAAA: none; CNAME: none;
- verifier marker: `TSK_0441_MULTI_RESOLVER_DNS=PASS`.

Because the public answer is the exact origin target rather than a Cloudflare proxy address, the observed public state is consistent with the required direct/DNS-only endpoint contract.

## Acceptance result

ACC-0441 is fully satisfied: the pilot resolver hostname resolves consistently to `52.157.109.120` from the system resolver and three independent public recursive resolvers, with no conflicting AAAA or CNAME state observed.

## Boundary

This PASS proves public DNS only. It does not prove TLS/DoH/DoT readiness, does not open public resolver ports, does not authorize participant activation, and does not change the separate TSK-0431 recovery-drill boundary.