# TSK-0413 owner privacy-first AdGuard baseline reconciliation — 2026-09-01

**Owner approval:** `APPROVE TSK-0413 RECOMMENDED PRIVACY-FIRST ADGUARD BASELINE`

## Approved baseline

- Persistent raw DNS query history: **off**.
- File query logging: **off**.
- Exceptional operational query diagnostics: allowed only when specifically needed later, with a **24-hour maximum** and deletion; this is not the default production state.
- Operational statistics: **minimum anonymized aggregate statistics only**, enabled with **24-hour retention**; identifiable per-client statistics/history remain excluded.
- Client IP anonymization: **on** wherever query/statistical records can contain client IP.
- ECS: **off**.
- Filter baseline: only the official **AdGuard DNS filter** is active initially; no stacked third-party lists without later evidence.
- Allowlist/exceptions: minimal, centrally controlled, documented, reversible, and limited to verified false positives or essential functionality.
- AdGuard administration: private management only, never directly public; authentication is mandatory; credentials remain outside Git.
- Browsing/query/activity history remains prohibited.

## Authority reconciliation

`DEC-0016` is the owning privacy decision and is refined to persist the approved 24-hour anonymized aggregate-statistics baseline without weakening its historical prohibition on identifiable history. `REQ-0044` remains unchanged because default query/file logging stays off. `REQ-0045` remains unchanged because identifiable per-client statistics remain excluded and IP anonymization stays on.

`TSK-0410` contained the older shorthand `no-querylog/no-statistics`. Its acceptance wording is narrowly reconciled to `no-querylog/no-identifiable-statistics` plus the owner-approved anonymized aggregate 24-hour statistics. No dependency, lifecycle, priority, action authority, task status, gate state, requirement, interface, or risk is changed.

## Impact

- `TSK-0413`: approved input is now durable and may be used to construct the versioned secret-safe recovery-consumable AdGuard bundle.
- `TSK-0410`: future acceptance no longer contradicts the approved privacy baseline. No PASS is implied.
- Current live AdGuard settings are not changed by this planning reconciliation; deployment remains separate governed work.
- No LG-07 or downstream PASS is implied.
