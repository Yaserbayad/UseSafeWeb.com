# TSK-0299 — Provisional Verbal System Acceptance Evidence

**Task:** TSK-0299  
**Date:** 2026-08-29  
**Artifact:** `TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md`  
**Artifact blob verified by GitHub read-back:** `a4ff2314ff02c407249e8b5d4d6b9600b89403b3`  
**Artifact publication commit:** `5f9cd0f2521fb81ba5b3692e110c9c1b197b5804`  
**Acceptance:** `ACC-0299` — verbal system follows plain-language, child-aware, non-alarmist, non-technical design rules for parent-facing use, conforms to current approved claims/non-surveillance constraints, is reusable across surfaces/locales, and does not imply representative-parent comprehension or legal completion.

## 1. Evidence basis

The acceptance review is grounded in current durable sources rather than general brand-writing preference:

- `TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md`, blob `73d8587ef9bb37d92b44f102d5a33545b416c44b` — brand role, promise, personality, trust strategy, allowed/conditional/prohibited claim classes and explicit RSK-0002 boundary.
- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md`, blob `1146f7622f434590dde1253d11f14fb6a87e19de` — canonical six-state vocabulary, evidence thresholds, copy grammar, no overall safety score and no confirmation-as-verification.
- `TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md`, blob `ef746d64c7878eb7d0f1b8fdf2356721728041c4` — en-GB baseline, provisional tr-TR/ar, semantic translation keys, evidence-strength parity, RTL and fallback rules.
- `TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md`, blob `d717c9b3f66197abe1f3e73361633f222b817e7c` — source-owned Android/iPhone setup/verification/removal terminology and platform asymmetry.
- `TSK_0559_FIRST_PHONE_CONTENT_QUALITY_SOURCE_UPDATE_PRUNING_STANDARD_2026-08-28.md`, blob `b2039d48e2356c0ea37fafe4fadc59d065cca6c8` — source hierarchy, claim classes, no fabricated user findings, localization-strength parity and anti-overclaim content rules.
- `CURRENT_STATE.md` immediately before TSK-0299 execution, blob `8389f7cad50db406948acc6b0ccf6ad775811ad0` — TSK-0298 durable PASS, TSK-0299 selected HIGH/AUTO_ALLOWED, TSK-0187 non-PASS, CR-0004 fences active.

## 2. ACC-0299 clause review

### A. Plain-language parent-facing design — PASS

The artifact establishes a parent-outcome-first message hierarchy, defers technical detail to the final message layer, uses short concrete action language, and defines parent-facing CTA patterns such as `Start setup`, `Check compatibility`, `Set up UseSafeWeb DNS`, `Check protection`, `See why this is uncertain`, `Remove UseSafeWeb DNS` and `Get recovery help`.

Technical terms are retained only where they correspond to an exact supported action or evidence distinction. The product is not positioned as a DNS/security stack.

### B. Child-aware language — PASS

Section 17 explicitly prohibits describing the child as a threat, data source, suspect or surveillance target; prohibits shame; prohibits claims of reading messages/images/location/contacts/social content; and frames the product around sensible safeguards, clear limits and safer independence.

The canonical role terminology uses `parent/caregiver` and avoids ordinary-user `administrator/operator/monitor` language.

### C. Non-alarmist design — PASS

The voice model requires calm risk framing and explicitly rejects urgency theatre, fear, guilt and parental shame. The prohibited-claim library carries forward the TSK-0298 ban on `Your child is in danger unless…`, `Responsible parents must…`, complete-safety language and fear-based conversion pressure.

### D. Non-technical design rules — PASS

The message hierarchy is ordered parent outcome → three bounded layers → evidence truth → privacy/limits/control → technical detail. Technical implementation appears only when needed for a supported setup, verification or recovery action.

The terminology table specifically keeps `First Phone Safety Setup` as the primary category and reserves Android `Private DNS` and iPhone `DNS profile` for their exact platform contexts rather than universalizing one mechanism.

### E. Approved claims and non-surveillance constraints — PASS

The artifact contains separate approved, conditional and prohibited claim libraries. It preserves:

- accountless-first language without absolute `zero data` claims;
- non-surveillance language without implying message/browsing/location inspection;
- bounded DNS-filtering scope;
- current-evidence-only `Verified` language;
- parent-confirmed language that cannot become technical verification;
- explicit Not covered / Status uncertain / Removed semantics;
- removal/recovery consequence language;
- bans on total-safety, bypass-proof, legal-certification, behavioral-validation, market-superiority, universal-support and fabricated-support claims.

The positive claim library does not claim representative-parent validation, legal completion, universal support or market readiness.

### F. Protection-state conformance — PASS

The artifact preserves all six TSK-0320 user-visible states and their default copy:

1. `Verified`;
2. `You confirmed this is set up`;
3. `Action needed`;
4. `Not covered`;
5. `Status uncertain`;
6. `Removed`.

It explicitly prohibits an overall safety score/all-green equivalence and uses the accepted completion language that separates verified, confirmed, action-needed and not-covered states.

### G. Reusable across surfaces — PASS

One shared message hierarchy, terminology system, CTA grammar and trust-language pattern is mapped to Home, How it works, Compatibility, Privacy, Setup, Verification, Protection Map, Troubleshooting, Removal/recovery and Help. The artifact does not create separate incompatible verbal systems for marketing versus operational surfaces.

Source-backed setup text remains owned by TSK-0307; the verbal-system examples do not create a second mutable technical-instruction authority.

### H. Reusable across locales — PASS

The artifact explicitly binds its semantics to TSK-0311:

- en-GB canonical authored baseline;
- tr-TR/ar provisional only;
- semantic translation keys rather than English-word keys;
- evidence strength may not increase in translation;
- technical literals remain untranslated/directionally isolated;
- Arabic RTL is preserved;
- authoritative critical copy cannot use runtime machine translation as fallback;
- localized language does not activate markets.

No native-speaker or publication-ready translation claim is made.

### I. Representative-parent comprehension remains unproven — PASS

The opening boundary explicitly states that no representative-parent evidence proves optimal comprehension, preference, trust, friction or support burden. `RSK-0002` remains OPEN, `TSK-0187` remains mandatory, and `TSK-0309` remains the later real-evidence correction/freeze point.

Examples are labelled reusable communication examples, not evidence that parents understand them.

### J. Legal completion remains unproven — PASS

The artifact expressly states that it does not author legal notices, statutory conclusions, consent language, age-policy conclusions, regulator claims or market-specific legal representations. It prohibits `GDPR compliant`, certification and equivalent claims without explicit authority and keeps unresolved legal work unresolved.

No publication, market, payment, participant, build or launch authority is inferred.

## 3. Overclaim / contradiction audit

Review of the complete GitHub-read-back artifact found:

- no positive claim of complete/100% safety;
- no positive surveillance/child-monitoring claim;
- no positive behavioral-validation statement;
- no positive legal-certification/compliance statement;
- no positive universal device/network support statement;
- no positive 24/7/routine staffed-support statement;
- no `Verified` use that deliberately redefines parent confirmation as system evidence;
- prohibited examples are explicitly presented as prohibited, not endorsed claims;
- the provisional tagline `Clear guardrails for safer first-phone independence` is explicitly bounded so `safer` is not treated as a guarantee.

No material contradiction with TSK-0298, TSK-0320, TSK-0311, TSK-0307 or TSK-0559 was found.

## 4. Acceptance decision

**ACC-0299: PASS.**

Every current acceptance clause is satisfied by the exact GitHub-read-back artifact under DEC-0051/CR-0004 provisional internal L4 semantics.

**Stable task disposition:** `TSK-0299 = PASS`, subject to reopening if later representative-parent evidence, legal authority or other higher-quality current evidence materially contradicts the provisional verbal assumptions.

This PASS does not authorize publication, implementation/build, participant processing, legal completion, payment, market activation or launch.
