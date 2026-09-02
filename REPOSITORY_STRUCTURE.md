# UseSafeWeb canonical implementation repository structure

**Task boundary:** TSK-0454  
**Status:** implementation structure contract; planning and runtime authority remain elsewhere.

## Canonical implementation roots

| Path | Ownership / purpose | Generated/artifact policy |
| --- | --- | --- |
| `/website` | Software / Frontend / Backend Engineering. Home of the Version-1 TypeScript + Next.js full-stack application when TSK-0361 implements it. | Source and tests are versioned. Generated `.next/`, coverage, dependency directories and local build output are ignored. |
| `/infrastructure/adguard-server` | Cloud / Platform + Network / DNS Engineering. Direct-host Ubuntu 24.04 LTS AdGuard deployment/recovery source, non-secret desired-state inputs and verification helpers. | Scripts and non-secret config are versioned. Runtime configuration, private keys, credentials, backups and secrets remain outside Git. |
| `/tests` | Cross-repository deterministic tests that verify repository-level contracts rather than feature-owned tests. | Test source is versioned; generated reports/coverage are ignored. |
| `/docs` | Non-authoritative implementation/developer documentation that does not belong to a feature directory. | Durable implementation docs may be versioned; generated exports stay outside source unless a canonical task explicitly requires them. |

Feature-local configuration and tests live with their owner (for example `/website/config` and `/website/tests`) rather than creating parallel top-level state stores.

## Authority boundary — no duplicate authority

This source structure does **not** create a second project authority:

- `Plans/Master/` remains the canonical planning system; its manifest routes ownership, the WBS owns tasks/acceptance, the relationship index owns traversal, and the gate/register files own their defined entities.
- `CURRENT_STATE.md` remains the only volatile runtime-state authority.
- Implementation READMEs explain source ownership and locations only. They do not redefine product scope, task state, dependencies, gates, decisions, requirements, risks or interfaces.
- Durable task evidence may point to implementation commits, hashes and test runs, but generated evidence indexes must never become a mutable task database.

## Configuration and secret boundary

Only non-secret, reviewable configuration belongs in Git. Environment-specific runtime configuration and every secret/password/token/private key are supplied through approved external mechanisms and remain outside Git. Files under `/website/config` document the application-side boundary; `/infrastructure/adguard-server` follows its current recovery/config contracts.

The root `.gitignore` excludes common generated output and secret-like file classes. Ignoring a file is a defense-in-depth measure, not permission to place secret material in the working tree.

## Generated files and artifact locations

- Website dependency/build output: `/website/node_modules`, `/website/.next`, `/website/dist`, `/website/coverage` — generated, not committed.
- Cross-repository test output: local/CI ephemeral output only unless a WBS acceptance criterion explicitly requires durable evidence.
- Infrastructure runtime journals, restored config, backups and TLS material: target-host protected locations defined by the current infrastructure contracts, never this repository.
- Versioned implementation evidence: the existing project evidence convention and `CURRENT_STATE.md` references remain controlling; TSK-0454 creates no new evidence/state store.

## Clean-checkout verification

Run:

```bash
python3 tests/repository-structure/verify_structure.py
python3 Plans/Master/Tools/validate_master_plan.py
```

These checks prove the canonical roots, ownership/authority boundaries, generated-file locations and secret exclusions. They do not claim that the future Next.js application or TSK-0455 deployment/recovery system has already been implemented.
