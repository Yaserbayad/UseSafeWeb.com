# UseSafeWeb TSK-0413 AdGuard recovery bundle v1.0.0

This directory is the secret-safe versioned AdGuard desired-state bundle consumed by later recovery automation. It is not a raw server backup and must never contain credentials, password hashes, private keys, certificate material, client identifiers, raw DNS query history, or browsing/activity history.

## Frozen desired state

- AdGuard Home `v0.107.79`, configuration schema `34`.
- Upstream exactly `https://dns10.quad9.net/dns-query`; ECS disabled.
- Persistent query/file logging disabled by default. Exceptional query diagnostics require separate authority, are capped at 24 hours, and must be deleted after use.
- Minimum anonymized aggregate statistics enabled with 24-hour retention; identifiable per-client statistics/history excluded.
- Client-IP anonymization enabled.
- Exactly one initial active filter: official `AdGuard DNS filter` (`filter_1.txt`).
- Allowlist starts empty. Later exceptions must be verified false positives or essential-functionality exceptions, centrally controlled, documented, reversible, and separately versioned.
- AdGuard administration binds to `127.0.0.1:3000`, is not publicly exposed, requires authentication, and receives credentials only from an external secret source.
- Public service identity remains `UseSafeWeb DNS` at `dns.usesafeweb.com`; DoH is `https://dns.usesafeweb.com/dns-query` and Android Private DNS uses the DoT hostname `dns.usesafeweb.com`.

## Recovery consumer contract

1. Verify `SHA256SUMS` before consuming any file.
2. Require exact bundle version `1.0.0`, AdGuard Home `v0.107.79`, and schema `34`; fail closed on mismatch.
3. Merge only the approved fields from `AdGuardHome.public-fragment.yaml` into the recovered configuration. Do not replace secret-bearing fields from Git.
4. Inject administrator authentication material and TLS/proxy secrets from the governed external secret/recovery mechanism; never synthesize or commit them.
5. Keep the AdGuard admin/plain-DNS listeners loopback-only. Preserve the existing protected same-host path-restricted encrypted-DNS proxy design.
6. Install only the official active filter represented in the bundle and the exact versioned allowlist. Do not restore dormant or historical third-party lists.
7. Run `verify_bundle.py` before deployment and again against the exact checked-out recovery bundle.
8. Live deployment, target observation, rollback/rebuild timing, and production activation require their own downstream governed acceptance; this bundle alone does not prove them.
