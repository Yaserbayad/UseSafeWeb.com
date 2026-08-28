# TSK-0318 — IA Design Preparation Evidence

**Task:** `TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems`  
**Acceptance:** `ACC-0318`  
**Action authority:** **A1 / HUMAN_ONLY**  
**Date:** 2026-08-28  
**Disposition tested:** preparation completeness only; **NOT task PASS**.

## Exact evidence set

- Candidate `TSK_0318_PUBLIC_PRODUCT_SETUP_IA_DESIGN_CANDIDATE_2026-08-28.md`, publication commit `e963f39684206bc08f5977957b0c9f379c82e716`, read-back blob `e5f7cd082397966893864213d43c634e62c0e701`.
- Current runtime selected TSK-0318 TODO for preparation only after TSK-0307 PASS.
- Sole hard dependency TSK-0315 is current runtime PASS.
- Accepted inputs consumed without redefining them: TSK-0315 accountless service blueprint, TSK-0316 friction contract, TSK-0317 platform setup design, TSK-0307 instruction catalogue, TSK-0320 protection-state contract, TSK-0314 accessibility NFR, TSK-0229 accountless data contract, TSK-0140 approved product brief.

## WBS / authority verification

The WBS assigns TSK-0318 A1 / `HUMAN_ONLY`. ACC-0318 requires every page/screen to have one purpose, entry/exit, content owner, SEO/index intent, privacy/accessibility requirement, with no duplicated or missing critical step.

The dependency is satisfied, but HUMAN_ONLY remains an independent completion boundary. AI may prepare and verify the candidate; it cannot approve the IA.

## ACC-0318 preparation checks

| Check | Result | Evidence |
| --- | --- | --- |
| Public website and setup/product are distinct connected systems | **PASS** | Candidate defines separate public information navigation and task/state-driven setup IA with explicit Start transition. |
| One purpose per public page | **PASS** | Home, How it works, Compatibility, Privacy, Help, controlled legal-notice slot and Start transition each have one stated purpose. |
| One purpose per setup screen/state | **PASS** | Router, native safeguard, Android/iPhone DNS, verification, external safeguard, Protection Map, action-needed, uncertain, not-covered, help, reset, removal, recovery and completion each have one purpose. |
| Entry defined for every page/screen | **PASS** | Both IA matrices contain explicit Entry columns. |
| Exit/next action defined for every page/screen | **PASS** | Both matrices contain explicit Exit / primary-next-action columns. |
| Content owner defined | **PASS** | Product, UX, Content, Network Engineering, Privacy, Support and legal-owning boundary are explicit per surface. |
| SEO/index intent defined | **PASS** | Stable public informational surfaces are index candidates only after release authority; operational/session/state surfaces are noindex by design. |
| Privacy requirement defined | **PASS** | Every row states accountless/no-history/transient/no-identity or owning privacy requirement; session/device state is barred from indexable URLs. |
| Accessibility requirement defined | **PASS** | Every row maps to WCAG 2.2 AA-target behavior including labels, focus, text states, reflow, accessible decision trees and non-color-only status. |
| No missing critical service-blueprint step | **PASS** | Completeness table maps every material TSK-0315 stage from discovery through removal/recovery/exit to an IA owner surface. |
| No duplicated mutable technical/support authority | **PASS** | Compatibility owns support explanation, TSK-0307 owns instruction semantics, TSK-0320 owns state truth; Help/setup link rather than create second authorities. |
| Accountless-first preserved | **PASS** | Login/account/dashboard/pricing/payment are absent from the active core IA; no persistence reason is introduced. |
| Friction contract preserved | **PASS** | Public explanatory content is not forced as extra setup screens; setup remains task/state driven. |
| Legal hold preserved | **PASS** | Legal page is only a controlled IA slot; unresolved REQ-0022/contact/legal completion is not asserted. |
| Build/publication boundary preserved | **PASS** | Index/noindex statements are design intent only; no implementation, publication or launch is claimed or authorized. |

## Adversarial checks

1. **Could the public website and setup accidentally become one mixed sitemap?** No. Navigation models, index intent and purposes are separated; links are explicit controlled connections.
2. **Could Help become a duplicate support matrix?** No. Stable Help routes users while Compatibility/TSK-0409 retain support truth and TSK-0307 retains instruction-source metadata.
3. **Could a search result expose transient device/journey state?** No. Operational routes are noindex by design and user/device state is prohibited from indexable URLs.
4. **Could legal-page presence be misread as legal readiness?** No. The candidate explicitly retains unresolved REQ-0022/legal/contact boundaries.
5. **Could account/dashboard scope sneak back through navigation?** No. Those routes are explicitly absent and EXC-0001 remains authoritative.
6. **Could a public page create a Verified state?** No. Verification remains an operational setup function governed by TSK-0320/current technical evidence.
7. **Could the candidate imply implemented SEO/accessibility controls?** No. It labels them design requirements/intents rather than execution evidence.
8. **Does this establish representative-parent usability?** No. RSK-0002 remains OPEN.
9. **Does technical preparation satisfy HUMAN_ONLY authority?** No. Human disposition remains required.

## Correct stable outcome

**Preparation:** COMPLETE and independently verified.  
**ACC-0318 technical/content coverage:** COMPLETE.  
**TSK-0318 runtime disposition:** **WAITING** for HUMAN_ONLY review/decision on exact candidate blob `e5f7cd082397966893864213d43c634e62c0e701`.

Minimum resume condition: authorized human explicitly `APPROVE`, `REQUEST CHANGES`, or `REJECT` the exact candidate. Approval alone would still be followed by an independent final ACC-0318 re-check before runtime PASS. No approval authorizes implementation/publication/launch.