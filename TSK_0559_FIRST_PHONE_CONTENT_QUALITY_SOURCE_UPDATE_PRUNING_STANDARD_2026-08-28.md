# TSK-0559 — First-Phone Content Quality, Source, Update, Localization and Pruning Standard

**Task:** TSK-0559 — Define the research, originality, usefulness, source, claims, update, localization, and pruning standard for first-phone content  
**Acceptance:** ACC-0559  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 CONTENT-GOVERNANCE CONTRACT / PUBLICATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0558 GTM baseline + CON-0014/CON-0015 + first-phone product/job authority + TSK-0143/0144 source-version rules + TSK-0320 truth-state rules + CON-0017 multilingual/market distinction + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Governing principle

UseSafeWeb content exists to solve a concrete first-phone parent job and connect that parent to a correct product/setup/help outcome. **Traffic volume is not an independent reason to create a page.**

The active rule is:

> Publish the smallest set of source-backed, original, genuinely useful first-phone content that answers a real parent decision or problem better than a generic restatement, then update, consolidate or remove it when it stops serving that job.

This content standard does not authorize public publication, GTM launch, paid acquisition or a mass editorial program. `RSK-0002` remains OPEN for unvalidated parent behavior/comprehension/value assumptions.

## 2. Hard prohibition — mass low-quality AI SEO

The following are prohibited:

- bulk-generating pages primarily to cover keyword/query variants;
- creating many near-duplicate pages for minor wording, device or locale permutations when one authoritative page can serve the job;
- generative-AI pages that add no material UseSafeWeb-specific value;
- scraped, stitched, synonymized or lightly paraphrased vendor/help content;
- automated translation used as the only added value;
- pages whose main purpose is ranking rather than solving a parent task;
- keyword-heavy pages that do not connect to an actual UseSafeWeb product/help decision;
- fabricated firsthand experience, test results, parent quotes, demand, search volume or behavioral findings;
- publishing unsupported “best”, “safest”, “complete protection”, “works everywhere”, “5-minute setup” or similar claims;
- retaining obsolete pages solely because they still receive impressions/traffic.

AI may research, structure, draft, compare and maintain content, but every published item is held to the same source, originality, evidence and review requirements regardless of whether AI assisted.

Google's current Search spam policy describes scaled content abuse as generating many pages primarily to manipulate rankings rather than help users, including generative-AI pages without added value, automated transformations/translations with little value, and stitched content without added value. This standard intentionally stays inside that boundary rather than treating AI production capacity as a content strategy.

Primary source checked 2026-08-28:
- Google Search Central — Spam policies: https://developers.google.com/search/docs/essentials/spam-policies

## 3. Required content record before creation

Every proposed content item must have a durable content record containing all of the following before drafting beyond a short outline:

| Field | Requirement |
| --- | --- |
| `Content_ID` | Stable internal identifier. |
| `Parent_Job` | One concrete first-phone parent job/question/problem. |
| `Why_This_Exists` | Why an existing product/help page cannot already satisfy the job. |
| `Unique_Value` | What UseSafeWeb adds beyond generic/vendor restatement: synthesis, tested project evidence, decision tree, limitation map, platform comparison, recovery path or direct setup bridge. |
| `Product_Help_Destination` | The exact setup/help/product action the content leads to when appropriate. |
| `Primary_Sources` | Current authoritative sources, normally platform/provider/government/regulator/project direct evidence. |
| `Applicability` | Platform/version/service/region/lifecycle conditions. |
| `Claims` | Material claims and their evidence class. |
| `Owner` | Accountable content owner/reviewer. |
| `Last_Verified` | Date the factual/source baseline was checked. |
| `Review_Triggers` | Events that force re-review. |
| `Locale_Status` | English/Turkish/Arabic status and whether content is translated, localized, or not applicable. |
| `Metric` | One privacy-safe usefulness metric aligned to the item's job. |
| `Disposition` | Draft / publish-eligible / update / consolidate / redirect / remove / archived-evidence. |

If a required field cannot be established, the item is not publish-eligible.

## 4. What counts as a real high-intent first-phone job

A job is in scope when a parent is trying to make or understand a concrete decision/action around the frozen UseSafeWeb first-phone lifecycle, such as:

- set up a child's first iPhone/Android with current native safeguards;
- understand which native control path applies;
- configure or verify UseSafeWeb DNS on a currently supported phone;
- understand why a supported path is uncertain/not covered;
- resolve a VPN/Private Relay/browser/network conflict;
- remove/reset UseSafeWeb and restore normal DNS;
- understand what `Verified`, parent-confirmed, action-needed, not-covered, uncertain or removed means;
- determine whether one currently supported external-service safeguard applies;
- solve a documented setup/compatibility/false-positive/help problem;
- understand a material protection limitation before relying on the service.

A topic is **not** high intent merely because a keyword tool, model or competitor suggests it. Search-volume estimates and trend claims are not introduced unless later supported by direct approved evidence.

Content outside the frozen first-phone product/job should be rejected or deferred rather than used to broaden the product by editorial drift.

## 5. Originality and usefulness test

Every item must add at least one material benefit that is difficult to obtain from a generic summary alone:

1. **UseSafeWeb-specific decision support** — clearly tells the parent which supported branch/state/action applies.
2. **Verified project evidence** — uses exact accepted UseSafeWeb technical behavior/limits where relevant.
3. **Cross-source synthesis** — reconciles multiple authoritative platform/service rules into one bounded parent decision without overclaiming.
4. **Recovery/troubleshooting value** — provides a safe, tested or explicitly provisional route from failure/uncertainty to recovery.
5. **Truth/coverage clarity** — explains what is and is not verified/covered in a way tied to the active product-state model.
6. **Version/applicability clarity** — prevents a parent from following a technically plausible but wrong device/version/service instruction.

Fail if the page is merely:

- a rewritten vendor help page;
- a generic “tips” article with no UseSafeWeb-specific decision or evidence;
- a list assembled from other lists;
- a keyword variant of an existing page;
- a translation with no localized/applicability work where such work is needed;
- filler designed to create site breadth.

Google's current generative-AI Search guidance likewise emphasizes useful, trustworthy, people-oriented, non-template content and warns against creating separate content for every possible query variation primarily to influence Search. UseSafeWeb adopts that direction as an external search-quality constraint, not as evidence that any particular content will rank.

Primary current Google guidance:
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

## 6. Source hierarchy

Use the strongest available source for each material claim:

1. **Current direct UseSafeWeb target evidence** for UseSafeWeb behavior, supported states, endpoints, tests and recovery.
2. **First-party platform/service documentation** for Apple/Google/provider behavior and settings.
3. **Government/regulator/legislation/standards source** for current legal/policy/regulatory facts.
4. **Authoritative technical standards/security source** where platform/vendor source is insufficient.
5. **High-quality secondary source** only when a primary source is unavailable or additional independent interpretation is materially necessary; label the limitation.

Rules:

- never cite a search-result snippet as the evidence when the underlying source is available;
- record exact source URL/title and last-checked date;
- use current applicability/version, not merely a source with a recent page timestamp;
- if primary sources conflict, do not silently choose the convenient one; mark uncertainty and resolve before publication or narrow the claim;
- if a current fact cannot be confirmed, say it cannot be confirmed and do not publish it as fact.

## 7. Claim classes

Every material claim must fit one of these classes:

| Class | Meaning | Publication rule |
| --- | --- | --- |
| `PROJECT_VERIFIED` | Direct accepted UseSafeWeb execution evidence. | May state the bounded tested result, with scope/date/version where material. |
| `SOURCE_CONFIRMED` | Current authoritative external source directly supports it. | Cite/source it and preserve exact applicability. |
| `EVIDENCE_SUPPORTED_CONCLUSION` | Multiple sources/evidence support a bounded interpretation. | State as a conclusion, not direct observed fact; retain basis. |
| `PROVISIONAL_DESIGN` | Current L4 design/owner hypothesis without real-user proof. | Must be labelled provisional internally; public wording cannot imply user validation. |
| `UNCONFIRMED` | Material fact cannot presently be verified. | Do not state as fact; narrow/remove or explicitly say it cannot be confirmed. |

Prohibited claim patterns include complete-safety promises, behaviorally validated claims without L3 evidence, platform-universal claims beyond TSK-0409, official non-UK market/support implications from language availability, and unverified legal conclusions.

## 8. AI use standard

Generative AI is allowed to accelerate content work only under these controls:

- retrieve/inspect current authoritative sources before making material factual claims;
- separate source fact from project evidence, inference and provisional design;
- never invent quotations, statistics, dates, test results, parent experience or search demand;
- never create fake “expert” or firsthand author experience;
- preserve source applicability/version/region;
- perform an adversarial pass for obsolete platform steps, overclaims, unsupported universality and duplicated pages;
- require a named content owner/reviewer even when AI produced the draft;
- stop bulk generation when additional pages cease adding distinct user value.

AI throughput is not a KPI. A smaller, maintained corpus outranks a larger low-confidence one.

## 9. Content-to-product/help connection

Every content item must terminate in one of three legitimate outcomes:

1. **Product action:** enter the exact relevant UseSafeWeb setup/check/recovery route.
2. **Help resolution:** solve or route a concrete issue without forcing product activation.
3. **Decision/understanding only:** answer a material question honestly when no product action should follow.

A page fails this standard if it exists only to attract traffic and has no legitimate next outcome for the parent.

Links/CTAs must not make unsupported conversion claims, hide Not covered/uncertain states, or create an account/payment gate before core value.

## 10. Update and source-freshness rules

Content is re-reviewed on the **earliest** applicable trigger:

- Apple/Google/service provider changes a menu, setting, supported version, account prerequisite, age policy or feature semantics;
- UseSafeWeb changes supported platform/network state, endpoint/profile contract, filtering behavior, state semantics or recovery method;
- current target evidence contradicts published instructions;
- UK or another officially activated market changes a law/regulation/policy materially affecting the content;
- source URL is removed/redirected or its current text no longer supports the claim;
- a security/privacy/safeguarding issue changes the recommended action;
- a recurring support/failure issue shows the page does not solve its stated job;
- localization/market activation changes applicability;
- material product scope changes under owner authority.

Do not use a universal arbitrary review interval as a substitute for event-driven review. A bounded periodic freshness audit may supplement these triggers but cannot keep a contradicted page “current.”

When a trigger fires, affected content becomes `REVIEW_REQUIRED` and must not continue presenting stale instructions as current fact.

## 11. Localization and multilingual standard

CON-0017 requires first public release capability in English, Turkish and Arabic with RTL, while official non-UK market/support activation remains separately gated.

Rules:

1. Translation must preserve the exact evidence strength, limitation and state semantics of the source content.
2. Translation may not strengthen `parent confirmed` into `verified`, uncertainty into certainty, or technical language availability into official market support.
3. Platform/service instructions may need **localization**, not literal translation, when vendor terminology/menu labels/availability differ by locale/region/version.
4. A locale page whose navigation/chrome is translated but whose substantive body remains another language is not treated as a complete localized variant.
5. Machine translation alone does not satisfy originality, verification or locale-applicability review.
6. Arabic RTL rendering/content QA is required before any Arabic page becomes publish-eligible.
7. Unsupported locale/market claims remain omitted or explicitly limited.
8. Duplicate same-language regional pages should not be created unless a genuine regional difference exists.

Google currently notes that different language versions are only considered distinct language content when the primary body is translated; same-language regional variants may require canonicalization plus `hreflang`. Actual technical implementation belongs to the website/SEO implementation tasks, but the content model must not generate duplicate/empty locale shells.

Current source checked 2026-08-28:
- Google Search Central — Canonicalization: https://developers.google.com/search/docs/crawling-indexing/canonicalization

## 12. Metrics — usefulness, not vanity volume

Every item has one primary privacy-safe metric tied to its job. Allowed examples, when the relevant analytics/search tooling is later approved and configured:

- Search Console impressions/clicks/CTR for discoverability diagnostics;
- click-through to the exact relevant setup/help route;
- successful completion of a privacy-safe synthetic/help resolution event where that measurement is independently approved;
- reduction in repeated support issue occurrence where aggregate evidence exists;
- stale-content defects detected/corrected;
- content-assisted setup/recovery outcome only when the product later has an approved privacy-minimal measurement method.

Prohibited metric design:

- child browsing/DNS history;
- persistent child/family behavioral profiles;
- cross-site ad tracking;
- publishing more pages as a success metric;
- pageviews alone as evidence that the content solved the parent's job;
- invented conversion/search-volume baselines.

No metric in this L4 standard authorizes a new analytics processor or data flow.

## 13. Pruning, consolidation and redirect rules

A content item must be reviewed for consolidation/removal when:

- its source/applicability is obsolete and no safe update exists;
- the product no longer supports the underlying job/path;
- another page now answers the same intent more completely;
- it is a thin query/keyword/locale variant without distinct value;
- it cannot meet the current source/evidence standard;
- it attracts traffic unrelated to the current product/target parent;
- current policy makes the recommended action unavailable/inappropriate;
- it creates a misleading outdated support claim.

Disposition order:

1. **Update** when the same job remains valid and a reliable current answer exists.
2. **Consolidate** when two or more pages solve the same job without meaningful distinction.
3. **Redirect** when a clear successor page answers the same parent need.
4. **Remove/noindex as appropriate** when no current useful successor exists or indexing would retain low-value/stale material.
5. **Archive evidence internally** when historical traceability is needed; historical evidence is not a public-current instruction.

Traffic preservation never outranks factual correctness, parent safety or current product scope.

## 14. GTM resource boundary inherited from TSK-0558

Content creation must fit the current owner-frozen GTM constraints:

- initial discretionary GTM budget is approximately **USD 20–50/month maximum**;
- funds may accumulate for bounded experiments;
- earned distribution is the primary engine;
- paid acquisition is not the initial engine;
- TSK-0558's one-primary/one-challenger discipline prevents simultaneous platform-program sprawl.

Consequences for content:

- do not create a large editorial operation the project cannot maintain;
- do not start simultaneous high-volume programs for every platform/locale/channel;
- prioritize the small set of content that directly supports the primary current acquisition/help path;
- use a challenger content hypothesis only when bounded and measurable;
- maintenance burden is part of the decision to create an item.

Canonical constraints:
- `CON-0014` and `CON-0015` in `Plans/Master/Registers/CONSTRAINTS.md`.

## 15. Content quality gate

An item is `PUBLISH_ELIGIBLE` only if **all** are true:

1. one real first-phone parent job is explicit;
2. unique value beyond generic restatement is explicit;
3. product/help/decision destination is explicit;
4. all material claims have an evidence class and current support;
5. required primary sources and last-verified date are recorded;
6. platform/service/market applicability is explicit;
7. no current contradiction remains unresolved;
8. owner/reviewer is named;
9. update/review triggers exist;
10. privacy-safe usefulness metric exists;
11. locale state is explicit and translation does not strengthen claims;
12. the item is not duplicative/thin/scaled-content abuse;
13. no real-user-validation claim exceeds current `RSK-0002` evidence;
14. publication itself is authorized by the applicable later task/gate.

Failure of any gate keeps the item draft/internal, or triggers update/consolidation/removal for an existing item.

## 16. Testable acceptance assertions

A later content/SEO/QA audit must prove:

1. no bulk page-generation target exists;
2. every content item has one specific first-phone parent job;
3. every item has a legitimate product/help/decision destination;
4. every material factual claim has a current source or accepted direct project evidence;
5. unconfirmed material facts are not stated as fact;
6. AI-assisted content follows the same evidence/review gate as human-written content;
7. no AI-generated page claims fabricated firsthand/user experience;
8. query/keyword variants without distinct value are consolidated/rejected;
9. scraped/stitched/paraphrased vendor content without UseSafeWeb-specific value is rejected;
10. automated translation alone cannot make a page publish-eligible;
11. English/Turkish/Arabic variants preserve evidence strength and official-market distinctions;
12. Arabic publish-eligible content has RTL/content QA;
13. platform/provider/policy changes trigger review before stale guidance continues;
14. unsupported obsolete pages are updated, consolidated, redirected or removed rather than kept for traffic;
15. content metrics do not require child browsing/DNS history or persistent family profiling;
16. no paid-acquisition dependency or mass content program violates the USD 20–50/month/earned-first baseline;
17. publication volume is never itself a success metric;
18. no page promises complete safety, universal compatibility or behaviorally proven ease without evidence.

## 17. ACC-0559 result

ACC-0559 requires that mass low-quality AI SEO be prohibited and that every item solve a real high-intent job and connect to product/help with source, review, owner and metric.

This standard directly provides those controls plus originality, claim evidence classes, source hierarchy, AI-use restrictions, update/freshness triggers, localization rules, privacy-safe metrics, pruning/consolidation rules and the inherited bounded GTM resource constraints.

**TSK-0559 result: PASS candidate subject to independent verification and runtime read-back.**
