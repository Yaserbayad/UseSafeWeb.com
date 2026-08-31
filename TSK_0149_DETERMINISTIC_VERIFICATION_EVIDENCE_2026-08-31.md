# TSK-0149 — Deterministic Verification Evidence

**Task:** TSK-0149 — Freeze the distinct public website and product/setup outcomes  
**Acceptance:** ACC-0149  
**Verification:** VER-0149  
**Evidence:** EVD-0149 supplemental deterministic proof  
**Date:** 2026-08-31  
**Result:** PASS

## Exact verified baseline

- Requirements artifact: `TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_2026-08-31.md`
- Artifact version: `1.0.0-post-cr0007`
- Artifact blob: `3eb1b90dc9fc3a79be94c7343cd16a9d3093748f`
- Artifact publication commit: `06efdf5e9b1d5ee4366714875b042bd19f31f333`
- Analytical evidence: `TSK_0149_POST_CR0007_PUBLIC_SITE_PRODUCT_SETUP_OUTCOMES_ACCEPTANCE_EVIDENCE_2026-08-31.md`
- Analytical-evidence blob: `e55306c70fee60079aedfb42fd6cffbc863936f5`
- Analytical-evidence publication commit: `29ae07dca4d8ba247abb2fad44e1c5b3347ce182`
- WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`
- Runtime baseline blob: `e3d8a09ccf42f61f65b48ecd2e43773a7300bfbf`

## Successful independent execution

- GitHub Actions run: `33402148107`
- Job: `99520837413`
- Runner: self-hosted `adguardvm`
- Workflow head commit: `9c37928b8427b3eaeb2c2b70656c51ccae167a4a`
- Conclusion: **SUCCESS**
- Repository `git diff --check`: PASS
- Clean repository status: PASS

Verifier output:

- `TSK0149_WBS_CONTRACT=PASS`
- `TSK0149_DEPENDENCY_RUNTIME=PASS`
- `TSK0149_ACC_SEMANTICS=PASS`
- `TSK0149_ASSERTIONS_10=PASS`
- `TSK0149_ANALYTICAL_EVIDENCE=PASS`
- `TSK0149_NO_DOWNSTREAM_PASS_INFERENCE=PASS`
- `TSK0149_INDEPENDENT_VERIFICATION=PASS`

## Proven disposition

The exact current artifact separates the public **discover / understand / trust / decide / start** outcome from the operational **start / configure / verify / understand / recover/manage** outcome while preserving one coherent brand/design system. It incorporates optional account sign-in/return/dashboard continuity without making login a prerequisite for core safety value.

The prior WBS `PASS` snapshot was not treated as runtime proof because no prior task artifact/evidence/runtime record existed. This fresh evidence supplies the missing durable acceptance chain.

No IA, implementation/build, provider/vendor/security architecture, real-user evidence, LG-06 or later-gate PASS is inferred.

**ACC-0149 is proven PASS.** A separate runtime reconciliation is still required before TSK-0149 may satisfy successor dependencies.
