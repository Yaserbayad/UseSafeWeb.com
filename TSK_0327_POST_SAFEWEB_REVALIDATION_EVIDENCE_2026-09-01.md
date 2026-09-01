# TSK-0327 — Post-SafeWeb Current Findings Revalidation Evidence

**Task:** `TSK-0327 — Resolve critical usability, trust, and accessibility findings`  
**Acceptance / Verification / Evidence:** `ACC-0327 / VER-0327 / EVD-0327`  
**Date:** 2026-09-01  
**Authority:** `DEC-0053 / CR-0006`, `DEC-0054 / CR-0007`  
**Action authority:** A3 / `AUTO_ALLOWED`  
**Disposition:** PASS, subject to guarded runtime refresh/read-back

## Reason for this revalidation

The first 2026-09-01 post-CR-0007 TSK-0327 findings review correctly re-evaluated the expanded dual-mode surface and closed the DNS-removal reachability defect. A later authority comparison then found a second real defect in the accepted TSK-0333 prototype: it rendered capitalized `UseSafeWeb` as the visible product name although owner-approved TSK-0301/TSK-0297 requires visible brand exactly `SafeWeb`.

TSK-0333 was corrected and fully regression-tested. TSK-0327 therefore had to be revalidated because its first current evidence pinned the superseded pre-brand TSK-0333 source blobs.

## Current findings artifact

`prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md`, version `2.1.0-post-cr0007`, blob `00abb274c7397e6fa8ffff3d6e1d407cc5cb9cc3`.

It explicitly records and closes both real product defects found in the current integrated review:

1. configured SafeWeb DNS removal was not reachable from the Protection Map — fixed and browser-retested;
2. visible product name rendered as `UseSafeWeb` contrary to owner-approved identity — fixed by a bounded pure `UseSafeWeb → SafeWeb` visible-name substitution and full browser regression.

The two earlier test failures caused by an ambiguous locator and overly literal privacy-copy assertion remain verifier-only diagnostics.

## Current corrected predecessor evidence

Current TSK-0333 runtime was refreshed after identity correction and is accepted under heading `TSK-0333 current accepted stable state — 2026-09-01 — POST-CR-0007`, runtime commit `9fd087c7510999e4fafcca29c4a2de862386f768`, runtime blob `ddbc60b780905094cf3714bf63d595b02ef8e7f2`.

Current corrected source blobs:
- `prototype/TSK-0333/index.html` `934dc19d00cc9dd32e1ebc20c604373d153d4013`
- `prototype/TSK-0333/model.mjs` `fc25e4b1facc303840311e8ce186612eb8799212`
- `prototype/TSK-0333/app.mjs` `98659ba74a86d539b89664708bbcb830292486f8`
- `prototype/TSK-0333/prototype.css` `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8` unchanged.

SafeWeb correction evidence: `TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `f3ea3bf41c38050356a6e9e94aa251b07b35c5f3`.

Owner-approved identity authority: `brand/identity/TSK-0301/README.md`, blob `b8ffd2ed234465a238558a7b94e56274de49696a`.

## Deterministic verification

Verifier: `.github/scripts/verify_tsk0327_after_safeweb_20260901.py`, blob `95f87920e76c72e4988173aa976cbb1e6283c8fb`.  
Workflow: `.github/workflows/verify-tsk0327-after-safeweb-20260901.yml`, blob `fbbc30d98892dfad5e5315f7527c9626325e3c7a`.  
Run/job: `33479274751 / 99765034038`.  
Runner: self-hosted `adguardvm`.  
Conclusion: **SUCCESS**.

Observed markers:
- `TSK0327_SAFEWEB_CURRENT_BLOBS=PASS`
- `TSK0327_SAFEWEB_WBS_CONTRACT=PASS`
- `TSK0327_SAFEWEB_PREDECESSOR_CONTEXT=PASS`
- `TSK0327_SAFEWEB_FINDINGS_DISPOSITION=PASS`
- `TSK0327_SAFEWEB_RETEST_EVIDENCE=PASS`
- `TSK0327_AFTER_SAFEWEB_REVALIDATION=PASS`

## Acceptance disposition

Current TSK-0327 is again evidence-complete against the corrected dual-mode product. No unresolved critical/high functional, trust/evidence-state, accessibility/responsive, recovery/lifecycle, privacy-boundary or identity-conformance finding remains in the applicable internal/automated L4 review. `TSK-0321` remains a separate HUMAN_ONLY accessibility-review authority boundary and is not self-certified here. No human comprehension/usability evidence is inferred before L8. `RSK-0002` remains OPEN/non-blocking before L8.

**ACC-0327 = PASS. VER-0327 = PASS. EVD-0327 = SATISFIED.**
