# TSK-0308 — Current Dual-Mode Shared Responsive Design-System Revalidation Acceptance Evidence

**Task:** TSK-0308 — Create the shared responsive design system for public and product surfaces  
**Acceptance / Verification / Evidence:** ACC-0308 / VER-0308 / EVD-0308  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Current accepted revalidation artifact

- `TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `90dce398ae86238abf5cf141acac47d78bf085b8`
- publication commit `0f840f3616af0030d65181965a4bf683a981586f`

The artifact preserves the historically approved TSK-0308 design system for still-valid responsive/state/accessibility/localization behavior and adds only the bounded dual-mode account/session/dashboard/device-lifecycle composition required by current CR-0006/CR-0008 authority. No SafeWeb identity, shared token, primitive or brand redesign was performed.

## 2. Current canonical inputs

Independent VER-0308 hash-locked:

- WBS `Plans/Master/WBS/master-wbs.csv` — `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship graph `Plans/Master/RELATIONSHIP_INDEX.yaml` — `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation `CURRENT_STATE.md` — `933bc16d90f66a7c8099666bd009cf50f78c5508`;
- current TSK-0309 dual-mode baseline `prototype/TSK-0309/BASELINE.md` — `6302bb2509d04c8269e4df112140d7c416e42eff`;
- current TSK-0300 evidence `TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md` — `efaf7c80c1723208569b13ba4e725b2e7cad8d1a`;
- shared `brand/system/TSK-0300/tokens.css` — `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- shared `brand/system/TSK-0300/components.css` — `831e92a74b6dda04252d93242cb33bd491a02381`;
- owner-approved SafeWeb primary wordmark — `f93958e3e4a16f9056693072c1b9b8b31fcda852`.

VER-0308 parsed the canonical WBS and proved L4 / HIGH / A3 / `AUTO_ALLOWED`, direct dependencies exactly `TSK-0309; TSK-0300`, and exact `ACC-0308 / VER-0308 / EVD-0308` binding. Marker: `TSK0308_CURRENT_WBS=PASS`.

Both direct predecessor task states were parsed with non-uniform-heading-tolerant logic and proved durable PASS. Marker: `TSK0308_CURRENT_PREDECESSORS=PASS`.

## 3. Historical approved provenance retained

Current acceptance preserves the following immutable historical package for compatible facts:

- `prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md` — `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4`;
- `prototype/TSK-0308/candidate.css` — `de5571379ff240f36b5aecd50f555a07176dbd32`;
- historical reference surface — `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862`;
- deterministic map — `cd83279cdf5381cd7dae3feb177439158c1f9197`;
- requirement/interface trace — `5e34ce9c192c6af65ba493cb356adb964c3d30b6`;
- historical acceptance evidence `TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md` — `343961f30bc46a20762ad2b0108a4afe9593e5a3`;
- historical technical verification run/job `33273620531 / 99156419342`.

That evidence proved 13/13 component contracts, 6/6 required state classes, 6/6 Protection Map states, 8/8 requirement/interface trace, 320/768/1024/1440 responsive rendering, visible focus, reduced-motion behavior, RTL/LTR isolation, target-size floor and clean browser console.

Independent current marker: `TSK0308_HISTORICAL_PROVENANCE=PASS`.

## 4. Current contradiction and bounded correction

The historical approved candidate explicitly prohibited Login / Account / Dashboard / Profile components, account/dashboard navigation and persistent account navigation. Those clauses conflict with current TSK-0309, which now requires optional account/session/dashboard/device-management and destructive account/device lifecycle while preserving the complete login-free core.

Independent VER-0308 proved both the historical contradiction and current predecessor semantics before accepting the correction:

- `TSK0308_DUAL_MODE_PREDECESSOR=PASS`;
- `TSK0308_SCOPE_RECONCILIATION=PASS`.

The correction preserves the historical files unchanged and adds only:

- `prototype/TSK-0308/DUAL_MODE_ADDENDUM.md` — `195ace26e6e8586e8e19da85a21d430a4a89a55a`;
- `prototype/TSK-0308/dual-mode-addendum.css` — `67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8`;
- `prototype/TSK-0308/dual-mode-reference.html` — `293945d9e2df823079e8dd73134168773a65a652`.

The addendum retains DS-01 through DS-13 and adds four bounded current patterns:

- DS-14 `OptionalAccountEntry`;
- DS-15 `SessionStatus`;
- DS-16 `DeviceManagementList`;
- DS-17 `AccountLifecycleActions`.

Marker: `TSK0308_DUAL_MODE_COMPONENTS=4/4_PASS`.

## 5. Shared-system / identity preservation

The additive CSS contains no local raw brand colors or font-family declaration and consumes existing `var(--sw-*)` tokens. The reference imports current TSK-0300 token/component sources, historical candidate CSS, the additive CSS and the approved SafeWeb wordmark.

Markers:

- `TSK0308_NO_TOKEN_OR_BRAND_FORK=PASS`;
- `TSK0308_REFERENCE_STRUCTURE=PASS`;
- `TSK0308_CURRENT_REVALIDATION_ARTIFACT=PASS`.

No identity reselection, logo edit, shared token change, primitive fork or public deployment occurred.

## 6. Current semantic acceptance

The accepted current design-system contract proves:

1. the complete accountless core remains primary and usable without login;
2. optional sign-in/manage-devices entry is secondary and non-coercive;
3. sign-in/session/device ownership never substitutes for technical Protection Map verification;
4. auth-provider/session failure preserves `Continue without signing in` where the core path is available;
5. device ownership, configuration and protection verification remain distinct facts;
6. Sign out, Unlink device, Delete device record, Delete account, Reset anonymous web state and Remove SafeWeb DNS are separate lifecycle operations;
7. account deletion does not claim DNS removal and DNS removal does not claim account/device-state deletion;
8. browsing/query/child-activity/raw-admin/query-log/overall-safety-score surfaces remain prohibited;
9. EN/TR/AR+RTL expansion, keyboard/focus, reflow and responsive behavior remain current requirements.

Static current markers:

- `TSK0308_CURRENT_ACC_STRUCTURAL=PASS`;
- `TSK0308_STATIC_VERIFICATION=PASS`.

## 7. Independent current VER-0308

Final robust verifier:

- script `.github/scripts/verify_tsk0308_current_revalidation.py` — blob `c614eb171c13a7c845257a10cb0597eb7d851b37`;
- workflow `.github/workflows/verify-tsk0308-current-revalidation.yml` — final accepted workflow blob `b26d5f8f502b1f6e3e671b179c23734fe6d07ccc`;
- permissions: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- Playwright `1.62.0`;
- Chromium / Chrome for Testing `151.0.7922.34`, Playwright revision `1234`;
- final run `33585488537`;
- final job `100108650200`;
- conclusion: **SUCCESS**.

Final rendered markers:

- `TSK0308_VIEWPORT_320=PASS`;
- `TSK0308_VIEWPORT_768=PASS`;
- `TSK0308_VIEWPORT_1024=PASS`;
- `TSK0308_VIEWPORT_1440=PASS`;
- `TSK0308_BROWSER_NO_OVERFLOW=PASS`;
- `TSK0308_BROWSER_ACCOUNTLESS_PRIMARY=PASS`;
- `TSK0308_BROWSER_OPTIONAL_ACCOUNT_SECONDARY=PASS`;
- `TSK0308_BROWSER_PROVIDER_FALLBACK=PASS`;
- `TSK0308_BROWSER_IDENTITY_PROTECTION_SEPARATION=PASS`;
- `TSK0308_BROWSER_LIFECYCLE_SEPARATION=PASS`;
- `TSK0308_BROWSER_RTL=PASS`;
- `TSK0308_BROWSER_FOCUS=PASS`;
- `TSK0308_BROWSER_CONSOLE=PASS`;
- `TSK0308_RENDERED_CURRENT_ACCEPTANCE=PASS`;
- `TSK0308_SOURCE_UNCHANGED=PASS`.

The final browser run re-proved the current additive surface at all four target widths, with no horizontal overflow, clean console/page behavior and no tracked source mutation during verification.

## 8. Diagnostic corrections retained without weakening acceptance

Three earlier diagnostic runs are retained as verifier-development evidence only; none changed the accepted artifact or runtime state:

1. the first structural run rejected the words `raw AdGuard administration` even though they appeared inside an explicit prohibition disclosure; the predicate was replaced by semantic prohibition checks;
2. the next rendered run appeared to report `VIEWPORT_320_overflow=FAIL`, but the verifier loop had mistakenly treated the desired boolean `overflow=false` as failure; diagnostic geometry proved there was no 320 px overflow;
3. the next run matched the header navigation `Sign in / Manage devices` instead of the secondary CTA inside `#setup`; the selector was scoped to the actual primary/secondary CTA group.

The final successful run used the same product/addendum/reference artifacts and corrected only verifier logic.

## 9. Acceptance disposition

- Current WBS/dependencies — **PASS**.
- Historical compatible DS-01–DS-13/state/responsive/accessibility/localization provenance — **PASS**.
- Current dual-mode scope correction — **PASS**.
- DS-14–DS-17 current component patterns — **PASS**.
- TSK-0300 token/primitive authority preservation — **PASS**.
- SafeWeb identity preservation — **PASS**.
- Structural current acceptance — **PASS**.
- Rendered 320/768/1024/1440 acceptance — **PASS**.
- Focus/RTL/no-overflow/console/source-integrity checks — **PASS**.

**ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED.**

**TSK-0308 current dual-mode revalidation: PASS, pending only durable runtime reconciliation/read-back.**

## 10. Non-inference

This proves the L4 shared responsive design-system contract only. It does not implement authentication/session/datastore/device ownership, process real users, activate telemetry/payment/market, prove legal/privacy completion, publish the product, pass LG-06, launch, or infer any successor PASS.
