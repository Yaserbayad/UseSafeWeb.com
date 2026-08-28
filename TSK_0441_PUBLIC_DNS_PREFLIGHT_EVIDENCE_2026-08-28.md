# TSK-0441 — Public DNS Record Preflight Evidence

**Task:** TSK-0441  
**Acceptance:** ACC-0441  
**Verification:** VER-0441  
**Evidence:** EVD-0441  
**Date:** 2026-08-28  
**Stable outcome:** WAITING

## Authoritative task contract

The canonical WBS defines TSK-0441, `Create public DNS records for the pilot endpoint`, as L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0440; TSK-0435; TSK-0011`, all satisfied.

ACC-0441 requires: **the record resolves to the correct pilot target from multiple resolvers and no stale/conflicting record remains.**

The approved endpoint decision fixes:

- client hostname: `dns.usesafeweb.com`;
- DoH URL: `https://dns.usesafeweb.com/dns-query`;
- public resolver record is DNS-only/direct to the Azure resolver, not CDN/proxy-fronted;
- no AAAA record until a public IPv6 target is directly verified;
- `srv.usesafeweb.com` remains the separate server/administration hostname.

## Direct public DNS evidence

Read-only resolver preflight was executed from the handed-off `adguardvm` through repository workflow `.github/workflows/governance-task-row-inspect.yml`.

Corrected DNS-state run:

- commit `a81284647344da5ca9e14592c4f469d720173333`;
- run `33130366213`;
- job `98718208157`;
- conclusion: **PASS** for read-only inspection.

Across the system resolver, Cloudflare `1.1.1.1`, Google `8.8.8.8`, and Quad9 `9.9.9.9`:

- `dns.usesafeweb.com` A: **NONE**;
- `dns.usesafeweb.com` AAAA: **NONE**;
- `dns.usesafeweb.com` CNAME: **NONE**;
- `srv.usesafeweb.com` A: **`52.157.109.120`** on all four resolvers.

A prior read-only run `33130335519` / job `98718108188` failed before DNS comparison because Azure IMDS did not expose a public-IP value through the queried network metadata shape. It made no target or DNS mutation. The corrected verifier removed that unnecessary assumption and used the already-controlled public server hostname for the independently resolved target.

## DNS authority evidence

Authoritative-provider preflight:

- commit `1e63f48b230c07a79c9f592ccac1179ea9228eb3`;
- run `33130403163`;
- job `98718326300`;
- conclusion: **PASS**.

Direct results:

- zone NS: `devin.ns.cloudflare.com.` and `haley.ns.cloudflare.com.`;
- SOA primary: `devin.ns.cloudflare.com.`;
- provider: **Cloudflare authoritative DNS**;
- the same four-resolver check again returned no A/AAAA/CNAME for `dns.usesafeweb.com` and `52.157.109.120` for `srv.usesafeweb.com`.

Therefore there is no out-of-band record to reconcile as PASS.

## Available execution authority

No Cloudflare account-control connector is installed in the current execution environment. Plugin discovery for `Cloudflare DNS` and `Cloudflare` returned no installable account-control plugin. The installed Cloudflare connector is documentation-only and cannot modify an owner Cloudflare zone. A repository search found no existing Cloudflare DNS automation/token path in the project.

No API token, account credential or Cloudflare secret was requested, pasted, committed, or inferred. Project automation must not invent or solicit a credential through Git/chat simply to bypass this boundary.

## Exact owner/provider action required

In the authoritative Cloudflare zone for `usesafeweb.com`, create the following record under the current approved endpoint contract:

- Type: **A**
- Name: **`dns`** (resulting FQDN `dns.usesafeweb.com`)
- IPv4 address: **`52.157.109.120`**
- Proxy status: **DNS only / not proxied**
- AAAA: **do not create** unless a public IPv6 target is separately verified and approved
- CNAME: **do not create** for this baseline

Do not expose or modify the separate `srv.usesafeweb.com` management identity as part of this action.

After the record is created, the project will re-run multi-resolver verification. TSK-0441 may reach PASS only if all required resolvers return the intended direct target with no stale/conflicting A/AAAA/CNAME state.

## Stable classification

**TSK-0441: WAITING — the required DNS record is currently absent and the consequential Cloudflare zone mutation requires owner/provider account access that is not available to the current connected execution environment.**

Deterministic resumption condition: the record is created by the owner/provider, or an explicitly authorized Cloudflare zone-control interface becomes available; then multi-resolver read-back proves `dns.usesafeweb.com` resolves directly to `52.157.109.120` with no conflicting AAAA/CNAME record.
