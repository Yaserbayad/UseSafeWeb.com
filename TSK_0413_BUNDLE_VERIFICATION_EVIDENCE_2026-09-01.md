# TSK-0413 — AdGuard recovery bundle verification evidence — 2026-09-01

## Stable result

`TSK-0413 — Create the secret-safe versioned AdGuard configuration, filter, allowlist, endpoint, and verification bundle consumed by recovery automation` has a verified candidate satisfying current `ACC-0413 / VER-0413 / EVD-0413`. This evidence record does not itself mutate runtime PASS state.

## Artifact identity

- Bundle path: `infrastructure/adguard-server/tsk-0413-bundle-v1/`
- Bundle version: `1.0.0`
- Candidate verification head: `8d329051ba900a92ae9d5897022bd2d090ad1c2d`
- `bundle.json` Git blob: `f0735e6a508f16de7a9c4510cc2893b972c1786c`
- `bundle.json` SHA-256: `e51130d22ba22a940fe5be10e423537474bb7ccc6a2a6b3b25596bbe96081bb0`
- Bundle checksum manifest Git blob: `5187374f2a4763491f1ac8bf82afde698a89cfc0`
- Prior approved secret-safe source config: `infrastructure/adguard-server/approved-adguard-config-v1.json`, Git blob `e9975c4e75c2a68131f049da942468d8d1952d8d`.
- Owner baseline: `TSK_0413_OWNER_PRIVACY_BASELINE_RECONCILIATION_2026-09-01.md` under current `DEC-0016`.
- Current DNS identity dependency: current `TSK-0408` PASS / `TSK_0408_POST_CR0007_REVALIDATION_EVIDENCE_2026-09-01.md`.

## Independent verification

GitHub Actions workflow: `.github/workflows/verify-tsk0413-bundle-20260901.yml`

- Run/job: `33500597612 / 99832778403`
- Head: `8d329051ba900a92ae9d5897022bd2d090ad1c2d`
- Result: **SUCCESS**
- Hosted verification environment: Ubuntu 24.04 runner.
- Bundle self-check: `TSK_0413_BUNDLE_VERIFY=PASS`.
- Repository verifier: `TSK_0413_REPOSITORY_VERIFICATION=PASS`.
- Master-plan validator: **PASS**, 641 tasks, 858 dependency edges, 0 broken links, 0 generated missing task IDs.
- Verified prior config blob: `e9975c4e75c2a68131f049da942468d8d1952d8d`.
- Verified official latest non-prerelease AdGuard Home release: `v0.107.79`.
- Verified annotated tag object: `314ec91cd14765fa8f878de4bb19fa546b5c40c4`.
- Verified official `v0.107.79` tag commit: `05ba17b282da1c4393d6a4ba4db0cf519194a362`.

The immediately preceding verification run `33500395219 / 99832136257` failed closed because the candidate carried an incorrect official tag commit pin. No PASS/runtime mutation occurred. Official GitHub tag evidence was reread; the pin, bundle checksums, and independent verifier were corrected, after which the complete verification passed at the head above.

## ACC-0413 mapping

| Current acceptance area | Verified evidence | Result |
|---|---|---|
| Approved upstream | exactly `https://dns10.quad9.net/dns-query`; preserved from approved source | PASS |
| ECS | disabled; no ECS endpoint introduced | PASS |
| Query logging/history | default persistent query logging and file logging off; exceptional diagnostics capped at 24h/delete; no browsing/query/activity-history store | PASS |
| Statistics | minimum anonymized aggregate statistics only; enabled with `1d` retention; identifiable per-client statistics/history excluded | PASS |
| Anonymization | client-IP anonymization enabled | PASS |
| Filter baseline | exactly one initial active official `AdGuard DNS filter` (`filter_1.txt`); dormant historical AdAway list deliberately excluded | PASS |
| Allowlist/exceptions | versioned allowlist is empty initially; later exceptions are central, documented, reversible and evidence-bound | PASS |
| Admin settings | admin bind `127.0.0.1:3000`, public exposure false, authentication required, credentials external/not versioned, browser receives no admin credentials | PASS |
| DNS/service endpoint identity | `UseSafeWeb DNS`; `dns.usesafeweb.com`; DoH `https://dns.usesafeweb.com/dns-query`; Android Private DNS uses DoT hostname semantics | PASS |
| Secrets/history exclusion | bundle contains no passwords/hashes, private keys, certificates, API/bearer secrets, client identifiers, raw query history or browsing/activity history | PASS |
| Checksums | all eight payload files are covered by `SHA256SUMS`; `verify_bundle.py` validates exact coverage/content | PASS |
| Version compatibility | bundle pinned to AdGuard Home `v0.107.79`, schema `34`, official tag commit `05ba17...`; exact-version-only compatibility policy fails closed on change | PASS |
| Recovery-consumer boundary | README defines checksum/version guard, field merge, external secret injection, loopback-only admin/plain DNS, filter/allowlist restoration and downstream live verification | PASS |

## Scope / non-inference

- This evidence proves the **versioned recovery-consumable bundle**, not deployment of the owner-approved new statistics/filter desired state to the live AdGuard server.
- It does not claim a live rebuild, restore, rollback duration, production activation, LG-07 PASS, TSK-0412 PASS, or TSK-0446 PASS.
- Secret material is intentionally absent; recovery automation must inject it from the governed external secret mechanism.
- Any AdGuard version/schema/API/default change must be reverified before this bundle is consumed.

## Disposition

All current `ACC-0413` clauses are evidenced. `TSK-0413` is eligible for a separate, stale-write-guarded runtime PASS reconciliation under `A4 / AUTO_ALLOWED`, followed by fresh L5 frontier derivation.
