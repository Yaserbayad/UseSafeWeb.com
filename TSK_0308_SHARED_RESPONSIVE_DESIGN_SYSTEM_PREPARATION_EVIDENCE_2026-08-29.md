# TSK-0308 — Shared Responsive Design System Preparation Evidence

**Date:** 2026-08-29  
**Task:** `TSK-0308 — Create the shared responsive design system for public and product surfaces`  
**Acceptance:** `ACC-0308`  
**Verification:** preparation verification only; final `VER-0308` remains subject to explicit HUMAN_ONLY owner disposition  
**Action authority:** `HUMAN_ONLY`  
**Disposition:** **CANDIDATE PREPARED / VERIFIED FOR OWNER DECISION / NOT PASS**

## 1. Human-authority boundary

The Project Owner explicitly instructed ChatGPT to **proceed with TSK-0308 preparation**. That instruction authorizes preparation and verification of a decision package; it does **not** constitute approval of the candidate and does not permit self-certification of TSK-0308 PASS.

Current WBS authority confirms:

- lifecycle: L4;
- priority: HIGH;
- dependencies: `TSK-0309; TSK-0300`;
- `ACC-0308 / VER-0308 / EVD-0308`;
- AI capability A1;
- Action Authority **HUMAN_ONLY**.

Both hard dependencies are current durable PASS under canonical runtime evidence.

## 2. Prepared candidate

The prepared candidate is deliberately a thin responsive composition layer over the existing TSK-0300 shared brand/token system rather than a second design system.

| Artifact | Role | Blob |
| --- | --- | --- |
| `prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md` | normative owner-decision/design-system candidate | `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4` |
| `prototype/TSK-0308/candidate.css` | composition-only CSS consuming existing `--sw-*` tokens | `de5571379ff240f36b5aecd50f555a07176dbd32` |
| `prototype/TSK-0308/reference.html` | internal representative public/setup/state/recovery browser surface | `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862` |
| `prototype/TSK-0308/DESIGN_SYSTEM_MAP.json` | non-authoritative deterministic verification projection | `cd83279cdf5381cd7dae3feb177439158c1f9197` |
| `prototype/TSK-0308/REQUIREMENT_INTERFACE_TRACE.md` | explicit requirement/interface trace companion | `5e34ce9c192c6af65ba493cb356adb964c3d30b6` |

The candidate defines 13 reusable composition contracts (`DS-01` through `DS-13`) and explicitly covers the six ACC-required classes: content, error, loading, verification, uncertain, and recovery.

## 3. Current source bindings

Verification pinned these current source blobs:

- `brand/system/TSK-0300/README.md` — `4baa67f565c14c3034fca47bb5fad0b9ff71b091`
- `brand/system/TSK-0300/tokens.css` — `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`
- `brand/system/TSK-0300/components.css` — `831e92a74b6dda04252d93242cb33bd491a02381`
- `prototype/TSK-0309/BASELINE.md` — `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`
- `prototype/TSK-0324/UI_COMPONENT_RULES.md` — `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`
- `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md` — `4efb624005061e242e427994953d0fc00fcd745f`
- `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` — `d12c1e707f0390915002b27bf3a5073d0135d466`
- `brand/identity/TSK-0301/README.md` — `b8ffd2ed234465a238558a7b94e56274de49696a`
- `Plans/Master/WBS/master-wbs.csv` — `f23b4f017d1baf73258fa30ecd71549bbfe1b815`

Current sequencing is `DEC-0052 / CR-0005`.

## 4. Structural preparation verification

Final successful preparation workflow:

- GitHub Actions run: `33273620531`
- job: `99156419342`
- runner: `adguardvm`
- Node: `v22.23.2`
- npm: `10.9.8`
- Playwright: `1.62.0`
- retained Playwright Chromium capability: PASS

Structural markers:

- `TSK0308_WBS_HUMAN_ONLY=PASS`
- `TSK0308_DEPENDENCIES_CURRENT_PASS=PASS`
- `TSK0308_SOURCE_AND_CANDIDATE_BLOBS=PASS`
- `TSK0308_CANDIDATE_STATUS_NOT_PASS=PASS`
- `TSK0308_REQUIREMENT_INTERFACE_TRACE=8/8_PASS`
- `TSK0308_COMPONENTS=13/13_PASS`
- `TSK0308_REQUIRED_STATE_CLASSES=6/6_PASS`
- `TSK0308_PROTECTION_STATES=6/6_PASS`
- `TSK0308_RESPONSIVE_LOCALE_SPEC=PASS`
- `TSK0308_NO_TOKEN_BRAND_FONT_FORK=PASS`
- `TSK0308_ACCOUNT_SUPPORT_TRUTH_FENCES=PASS`

The explicit 8/8 trace covers:
`REQ-0028`, `REQ-0029`, `REQ-0030`, `CON-0010`, `CON-0017`, `CON-0022`, `INT-0009`, `INT-0010`.

## 5. Rendered Chromium preparation verification

The internal reference surface was rendered with Chromium against four target layout widths:

- `VIEWPORT_320=PASS`
- `VIEWPORT_768=PASS`
- `VIEWPORT_1024=PASS`
- `VIEWPORT_1440=PASS`
- `FOCUS_VISIBLE=PASS`
- `REDUCED_MOTION=PASS`
- `BROWSER_CONSOLE=PASS`
- `TSK0308_RENDERED_CANDIDATE=PASS`
- `REPOSITORY_CLEAN=PASS`

At every viewport the verifier required:

- TSK-0300 shared tokens loaded;
- no page-level horizontal overflow;
- representative public/setup/help/limitations/RTL surfaces present;
- all six current protection labels present: `Verified`, `You confirmed this is set up`, `Action needed`, `Not covered`, `Status uncertain`, `Removed`;
- loading region exposes `aria-busy=true` and textual status;
- Arabic/RTL structural container computes RTL while technical values remain LTR-isolated;
- all reference `.sw-button` controls meet at least the WCAG 2.2 AA 24 CSS-pixel target-size floor used by current project rules;
- visible focus remains present;
- optional busy animation is disabled under reduced motion;
- no browser console/page errors.

The first transient HTTP probe occurred before the local loopback test server finished binding; the workflow retried as designed, the subsequent readiness probe succeeded, and all rendered assertions passed. No production service was modified.

## 6. Debugging/recovery history

Preparation failures were stopped and classified before progression:

1. Run `33273426515` / job `99155895732`: verifier assumed a literal historical runtime heading for TSK-0309. Classified as verifier-format fragility; no candidate defect and no browser execution occurred.
2. Run `33273496823` / job `99156079696`: robust dependency parsing passed far enough to expose a real traceability gap—the normative package did not explicitly bind every current requirement/interface ID. Corrective artifact `REQUIREMENT_INTERFACE_TRACE.md` was added.
3. Run `33273561984` / job `99156254247`: complete structural verification passed; browser step exited `127` before assertions because the workflow omitted Node provisioning. Corrected by adding `actions/setup-node@v6` with Node 22, matching the proven browser-testing execution pattern.
4. Run `33273620531` / job `99156419342`: complete structural + Chromium verification PASS.

A separate preparation QA correction removed a local monospace `font-family` from `candidate.css`, preserving TSK-0300 as the sole approved shared typography authority.

## 7. Design-system boundary proven by preparation

The candidate:

- uses TSK-0300 as sole token/primitive authority;
- contains no raw brand hex values, local `--sw-*` token declarations, local font stack or external asset URL in candidate CSS;
- preserves current S1–S6 evidence semantics;
- keeps S1 system verification distinct from S2 parent confirmation;
- includes no mandatory Login/Account/Dashboard/Profile/payment/child-profile/history surface;
- keeps ordinary support/recovery self-service;
- supports EN/TR/AR+RTL structurally without claiming non-UK launch/legal/support readiness;
- preserves public-versus-setup purpose separation;
- provides implementation-ready and QA-testable responsive/accessibility/state/recovery rules.

## 8. Stable disposition

**TSK-0308 is not PASS.** The candidate is prepared and technically verified for decision, but the WBS requires a genuine Project Owner HUMAN_ONLY disposition.

Exact decision choices:

- `APPROVE TSK-0308 CANDIDATE`
- `REVISE TSK-0308: <specific change>`

Only explicit approval of this exact candidate version may authorize final acceptance verification, EVD-0308 publication and runtime PASS reconciliation.

No real-user/native-speaker validation, legal completion, production build, publication, participant processing, payment, market activation or launch authority is inferred. `RSK-0002` remains OPEN; human/user validation remains deferred under CR-0005 until the integrated-product stage.
