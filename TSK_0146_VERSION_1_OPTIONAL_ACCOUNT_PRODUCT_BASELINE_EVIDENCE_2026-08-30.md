# TSK-0146 — Version-1 Optional-Account Product Baseline Acceptance Evidence

**Date:** 2026-08-30  
**Task:** TSK-0146 — Freeze Version-1 optional-account product baseline and accountless core path  
**Acceptance:** ACC-0146  
**Verification:** VER-0146  
**Evidence:** EVD-0146  
**Action authority:** A3 / AUTO_ALLOWED  
**Disposition:** PASS evidence for TSK-0146, subject to canonical runtime reconciliation/read-back

## 1. Artifact under verification

- Artifact: `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md`
- Version: `1.0.0`
- Artifact commit: `1a913b44a09c383ac6c9939959648629351d9f6c`
- Artifact blob: `9d3870d90add696fc352829fb4763c834b8d09af`
- Read-back: exact GitHub `main` path fetched after publication; blob matched expected artifact.

The artifact is additive. It does not rewrite historical accountless-only evidence; it supersedes only the account-scope clauses invalidated by DEC-0053/CR-0006.

## 2. Canonical source bindings

Verification was pinned to the following authoritative source blobs:

- WBS `Plans/Master/WBS/master-wbs.csv`: `3bb1598a6233a2bbefa52c746a7621867c6c6e89`
- Requirements `Plans/Master/Registers/REQUIREMENTS.md`: `a2212059f69c4602eb0c05961d5d1639e3543f83`
- Constraints `Plans/Master/Registers/CONSTRAINTS.md`: `9464720bff94fd569e3b939568996a26eed83ca1`
- Interfaces `Plans/Master/Registers/INTERFACES.md`: `b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c`
- Risks `Plans/Master/Registers/RISKS.md`: `0ebb7ab97ec4d418e61eaae0fce6a35e3a9e36ec`
- Decisions `Plans/Master/Registers/DECISIONS_TRIGGERS.md`: `9cb2908f4c6f19cb38fce4a8aff71abca3b7b095`

Current WBS contract verified TSK-0146 as L4, PLANNED/TODO before execution, zero hard dependencies, A3, AUTO_ALLOWED, ACC-0146, VER-0146 and EVD-0146.

## 3. Deterministic verification evidence

Workflow: `Verify TSK-0146 Version-1 baseline`  
Workflow file at execution: `.github/workflows/verify-tsk0146-v1-baseline-20260830.yml`  
Verification workflow commit/head: `f18219f475e523213eacc39ce13366f173dc7da5`  
GitHub Actions run: `33307541477`  
Job: `99246630910` (`verify`)  
Runner: self-hosted `adguardvm`  
Result: **SUCCESS**

Observed verification outputs:

- `TSK0146_WBS_CONTRACT=PASS`
- `TSK0146_SOURCE_BINDINGS=PASS`
- `TSK0146_ACC_REQUIRED_CLAUSES=PASS`
- `TSK0146_SCOPE_NON_GOALS=PASS`
- `TSK0146_NO_DOWNSTREAM_PASS_INFERENCE=PASS`
- `TSK0146_VERIFICATION=PASS`

The workflow verified exact source and artifact hashes before evaluating content, preventing a stale-source or wrong-artifact pass.

## 4. ACC-0146 review

| Criterion | Evidence in version 1.0.0 | Result |
| --- | --- | --- |
| Version 1 includes an optional parent account | Dual-mode baseline makes optional parent account a required V1 path. | PASS |
| Lightweight dashboard/device management included | Dashboard is bounded to minimum parent/device ownership, settings/state and lifecycle value. | PASS |
| Complete core setup/protection journey remains usable without login | Accountless core is a first-class required path and auth/provider failure may not make it login-dependent. | PASS |
| Minimum identity/device persistence defined | Only minimum parent/account/device ownership/settings/lifecycle classes are authorised; exact schema is explicitly deferred to downstream authoritative design. | PASS |
| Authentication/session boundary defined | Sign-in, secure session/return, expiry, logout, revocation and provider-failure behavior are required. | PASS |
| Deletion/recovery boundary defined | Account/device deletion, revocation, recovery and truthful partial-failure behavior are required. | PASS |
| Privacy/security boundary defined | Non-surveillance, parent/device isolation and mandatory downstream auth/authz/CSRF/IDOR/account-takeover/ClientID controls are explicit. | PASS |
| Failure boundary defined | Auth/datastore/session/ownership/DNS verification/partial-deletion failures have truthful behavior; accountless core is preserved where technically possible. | PASS |
| Browsing/activity history prohibited | DNS query, visited-domain, browsing/activity and top-domain product history are explicitly prohibited. | PASS |
| Child accounts prohibited | Child accounts/apps and persistent child behavioral profiles remain outside V1. | PASS |
| Broad DNS administration prohibited | Unrestricted/raw AdGuard/DNS administration is explicitly excluded. | PASS |
| Mandatory-login expansion remains owner-only | A later explicit Project Owner decision is required. | PASS |

**ACC-0146 result: PASS.**

## 5. Independent reviewer inspection

The acceptance review was performed as a separate verification operation after publication/read-back of the baseline artifact. It compared the artifact with the exact current WBS task contract and authoritative decision/requirement/constraint/risk/interface sources rather than treating artifact existence as completion.

No applicable ACC-0146 contradiction or omitted element was found.

## 6. Residuals preserved — not blockers to TSK-0146

The following are intentionally **not** treated as completed by this PASS:

- `RSK-0002` remains OPEN: human behavioral/usability/comprehension evidence is deferred to L8 after LG-09 under DEC-0052/CR-0005.
- Account/dashboard privacy drift and query/history exposure risk remain for downstream data-contract/runtime verification.
- Google/Firebase is only the planned initial authentication route; L5 vendor/privacy/security/architecture acceptance remains required.
- Exact persistence schema, retention, storage, backup, access, deletion and ownership mechanics remain downstream work.
- L4 account UX/prototype, L5 architecture/security/privacy/vendor, L6 implementation and L7 auth/authz/IDOR/ClientID/deletion/recovery work remain required by their own tasks and gates.
- LG-06 remains non-PASS until its revised complete evidence package satisfies its current gate contract and Project Owner authority.
- No real-user validation, participant processing, public launch or payment activation is authorised or inferred.

## 7. Final evidence disposition

All applicable current ACC-0146 elements are supported by a versioned, read-back artifact and deterministic source-bound verification. No unresolved critical/high conflict specific to this L4 scope-freeze task was found.

**TSK-0146 is evidence-ready for runtime state `PASS`.** The PASS becomes canonical only after `CURRENT_STATE.md` is updated, committed, reread and verified against this evidence.
