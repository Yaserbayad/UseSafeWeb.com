# TSK-0413 compatibility contract

- Bundle version: `1.0.0`.
- Pinned AdGuard Home: `v0.107.79`.
- Pinned configuration schema: `34`.
- Official `v0.107.79` tag commit: `05ba17b282da1c4393d6a4ba4db0cf519194a362`.
- Supported use: reconstruct the approved secret-safe desired state on the frozen AdGuard backend/recovery path.
- This bundle does not authorize an AdGuard upgrade. A version/schema/API/default change requires current compatibility and rollback verification before use.
- Secret/authentication material and TLS private-key material are deliberately absent and must come from the governed external secret/recovery mechanism.
- Public encrypted DNS terminates at the existing protected same-host proxy path; the AdGuard administrative interface and plain DNS listener remain loopback-only.
