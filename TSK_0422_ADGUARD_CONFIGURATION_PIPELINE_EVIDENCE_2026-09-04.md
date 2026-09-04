# TSK-0422 AdGuard configuration pipeline evidence

**Date:** 2026-09-04
**Task:** TSK-0422 — Implement versioned AdGuard and DNS service configuration pipeline
**Acceptance:** ACC-0422
**Verification:** VER-0422
**Evidence:** EVD-0422
**Source commit:** `2ba9bb46a5ecba83c71418231dae2fa248d958b2`
**Pipeline blob:** `a947aea558804da9a06650a6ae2324a9ca81a1d8`
**Pipeline SHA-256:** `1867421b38c3e8af59745524706396bb05735b64017be254d08615e980e66d61`
**Approved configuration blob:** `e9975c4e75c2a68131f049da942468d8d1952d8d`
**Approved configuration SHA-256:** `394fb78a4c61677ff4b1612452bbabd14423d1bf86e44eeda5f3e358731d5988`
**GitHub Actions run / attempt:** `33848412976 / 1`
**Target:** repository-scoped self-hosted runner on `adguardvm`, Ubuntu 24.04 LTS.

## Result

**PASS.** The target applied the version-controlled, secret-safe approved AdGuard projection idempotently and a separate target job independently re-ran VER-0422.

- Sanitized controlled-field change count at apply: `0`.
- Sanitized changed paths: `none`.
- Persisted controlled settings match `approved-adguard-config-v1.json` after apply.
- Runtime API checks prove protection enabled, the only approved upstream is `https://dns10.quad9.net/dns-query`, query logging disabled, statistics disabled, and the active filter is the approved AdGuard DNS filter.
- A synthetic loopback DNS request passed without retaining or publishing query content.
- Negative fixtures for query logging, ECS, a non-approved upstream, and an unapproved active filter/processor were all rejected.
- Runtime-only filter identifiers are preserved rather than rewritten by the versioned artifact.
- Secrets remain outside Git; the credential file remains root-owned mode 0600 and no credential/query/client-identifier content is copied into evidence.
- Changes are diffable through a deterministic privacy-safe projection; candidate generation preserves all non-controlled configuration semantics.
- Apply uses a staged candidate and root-only rollback copy; any post-replacement failure restores the prior configuration and restarts AdGuard Home.

## Sanitized evidence integrity

- Apply transcript SHA-256: `a046edd8e703a949a4da6db276eecbea72c00e5a8ef66d9ba8abe2ac944f9dae`
- Independent verification transcript SHA-256: `ab9779aa466b0ddc377cf29b3646fc84d6695e2927a4eba4651386db12b39d19`
- Raw credentials, query records and client identifiers are not persisted in project evidence.

## Authority and non-inference

The pipeline consumes the existing canonical `approved-adguard-config-v1.json`; it does not create a second configuration authority. REQ-0042/REQ-0043 and CON-0002/CON-0003 remain controlling. This PASS proves only TSK-0422. It does not pass or alter TSK-0455, TSK-0456, TSK-0457 or TSK-0492; deploy a new environment; distribute profiles/certificates; revoke service; process participants; enable telemetry; authorize public/market activation; or satisfy launch gates.
