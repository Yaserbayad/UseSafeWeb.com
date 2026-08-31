# TSK-0312 — Deterministic Verification Evidence

**Task:** TSK-0312 — Specify parent authentication, account/session, and minimal intake requirements  
**Acceptance:** ACC-0312  
**Verification:** VER-0312  
**Evidence:** EVD-0312 supplemental deterministic proof  
**Date:** 2026-08-31  
**Result:** PASS

## Exact verified baseline

- Requirements artifact: `TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_REQUIREMENTS_2026-08-31.md`
- Artifact version: `1.0.0`
- Artifact blob: `8dd71bccbd24ac5f62d5c536e644e7d9209b5832`
- Artifact publication commit: `f2f383c0c7b01b72b1eb708e0522bf13bb415369`
- Analytical evidence: `TSK_0312_PARENT_AUTH_ACCOUNT_SESSION_MINIMAL_INTAKE_ACCEPTANCE_EVIDENCE_2026-08-31.md`
- Analytical-evidence blob: `8a4eec66fb63b57d01a6413ca9459c0713f29ff5`
- Analytical-evidence publication commit: `4cd272051fcb42643054361169ba828426ff3c8b`
- WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`
- Runtime baseline blob: `7d337793c68b72f5001b305905acc606c1f839c7`
- Requirements register blob: `a2212059f69c4602eb0c05961d5d1639e3543f83`
- Constraints register blob: `9464720bff94fd569e3b939568996a26eed83ca1`
- Interfaces register blob: `b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c`
- Current TSK-0140 product brief blob: `8ed698b3e34540aefac617e5f6754e20d9dfbdc3`
- Current TSK-0229 no-linkage amendment blob: `2955c2762e726f95ec67c33b9abbc5e4b25cb84a`

## Successful independent execution

- GitHub Actions run: `33397888358`
- Job: `99506708568`
- Runner: self-hosted `adguardvm`
- Workflow head commit: `a40475b73c02df477e45257f66b5d1f7dd47b884`
- Conclusion: **SUCCESS**
- `git diff --check`: PASS
- clean `git status --porcelain`: PASS

The verifier emitted:

- `TSK0312_WBS_CONTRACT=PASS`
- `TSK0312_DEPENDENCY_RUNTIME=PASS`
- `TSK0312_PRODUCT_SCOPE=PASS`
- `TSK0312_IDENTITY_INTAKE_MINIMIZATION=PASS`
- `TSK0312_ACCOUNT_SESSION_LIFECYCLE=PASS`
- `TSK0312_CSRF_SESSION_REQUIREMENTS=PASS`
- `TSK0312_NO_LINKAGE=PASS`
- `TSK0312_NO_PASSWORD_SMS=PASS`
- `TSK0312_TEST_CASES_16=PASS`
- `TSK0312_NO_DOWNSTREAM_PASS_INFERENCE=PASS`
- `TSK0312_INDEPENDENT_VERIFICATION=PASS`

## What was independently proven

1. The exact current WBS row is L4, depends only on current-PASS TSK-0140, and is A3 / AUTO_ALLOWED.
2. The exact artifact covers every explicit ACC-0312 clause.
3. The account branch remains optional and the accountless core remains intact.
4. Identity/intake is defined by a documented-necessity/minimum allowlist rather than provider payload convenience.
5. Logout, revocation, deletion, expiry, errors and recovery/resume states are explicitly defined and separated from DNS-removal claims.
6. CSRF/session security outcomes are mandatory without prematurely selecting L5/L6 mechanisms.
7. Current TSK-0229 no-linkage/expiry/deletion separation remains intact.
8. Password and SMS authentication are not introduced.
9. Sixteen deterministic/synthetic test cases are present without fabricating pre-L8 human evidence.
10. No provider/security architecture, implementation, legal/privacy compliance, LG-06 or later gate PASS is inferred.

## Disposition

Combined with the independently authored analytical acceptance review, the successful deterministic verifier proves **ACC-0312 PASS** for TSK-0312 under the current authority and exact artifact baseline.

TSK-0312 may be marked runtime PASS only by a separate canonical runtime reconciliation that reads this evidence, preserves unrelated state, writes `CURRENT_STATE.md`, commits it, and reads the result back. Successor eligibility must then be recomputed independently.
