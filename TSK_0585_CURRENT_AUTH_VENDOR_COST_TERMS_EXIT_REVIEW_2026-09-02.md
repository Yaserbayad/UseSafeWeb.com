# TSK-0585 — Current Authentication / AdGuard Vendor Cost, Licence, Terms and Exit Review

**Task:** TSK-0585 — Verify authentication free tier, AdGuard licence/API cost, vendor terms and exit triggers  
**Acceptance / Verification / Evidence:** ACC-0585 / VER-0585 / EVD-0585  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / AUTO_ALLOWED  
**Version:** 1.0.0  
**Evidence date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0585, durable EVD-0585 publication, guarded runtime reconciliation and exact GitHub read-back.

## 1. Decision boundary

This is a dated factual vendor/cost/licence review for the frozen Version-1 direction. It does **not** activate Firebase Authentication with Identity Platform, create a billing account, add SMS/phone authentication, purchase a service, change the self-hosted AdGuard Home backend, make a legal/compliance conclusion, accept vendor terms on behalf of the owner, or authorize launch.

Current direct predecessors are:

- TSK-0045 — current maintainability/deployment/cost-control NFR;
- TSK-0353 — current authentication/authorization/session/account-lifecycle NFR;
- TSK-0044 — current AdGuard API/credential/failure NFR.

The current planned initial authentication route remains **Google sign-in through Firebase Authentication without SMS/phone authentication**. Identity Platform is an optional upgrade, not a requirement for the initial route.

## 2. Dated official-source register

All vendor facts below were rechecked on **2026-09-02 UTC** against official sources.

| Source | Official URL | Current fact used by this review |
|---|---|---|
| Firebase pricing | `https://firebase.google.com/pricing` | Spark is a no-cost plan requiring no payment method; “Other Authentication services” are available on Spark/Blaze; Phone Auth is billed per SMS; with Identity Platform the pricing table shows no-cost usage before paid Google Cloud pricing. |
| Firebase Authentication docs | `https://firebase.google.com/docs/auth` | Identity Platform is an optional upgrade. Upgraded Spark limits most Email/Social/Anonymous/Custom providers to 3,000 DAU and SAML/OIDC to 2 DAU; upgraded Blaze has 50,000 MAU no-cost for Tier-1 providers and 50 MAU no-cost for SAML/OIDC before paid usage. |
| Google Cloud Identity Platform pricing | `https://cloud.google.com/identity-platform/pricing` | Tier-1 Email/Phone/Anonymous/Social: 0–50,000 MAU $0, then $0.0055 / $0.0046 / $0.0032 / $0.0025 per MAU by tier. Tier-2 SAML/OIDC: 0–50 MAU $0, then $0.015/MAU. Phone/MFA messaging is separately charged per message. |
| Firebase Authentication limits | `https://firebase.google.com/docs/auth/limits` | Upgraded Identity Platform on Spark has 3,000 Tier-1 DAU and 2 Tier-2 DAU instrumentless limits; quotas/abuse controls can change and are not treated as permanent entitlements. |
| Firebase Privacy & Security | `https://firebase.google.com/support/privacy` | **Firebase Authentication is run only from US data centers and processes data exclusively in the United States.** |
| Firebase Terms | `https://firebase.google.com/terms/` | Terms page states last modified **May 1, 2026**. Firebase Authentication is listed under Google Cloud Platform Terms of Service; the terms reference applicable data-location/service-specific terms. |
| Firebase Data Processing and Security Terms | `https://firebase.google.com/terms/data-processing-terms` | Current data-processing terms contain restricted-transfer/SCC mechanisms and refer to Google data-center information. This review records the terms but makes no adequacy/lawful-transfer conclusion. |
| AdGuard Home official repository | `https://github.com/AdguardTeam/AdGuardHome` | Official repository describes AdGuard Home as **free and open source**, displays **GPL-3.0 license**, supports self-hosted installation, and directly documents use of its REST API for integration. |
| AdGuard Home licence file | `https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/LICENSE.txt` | Repository licence text is GNU General Public License Version 3. GPL obligations matter if software is copied/modified/conveyed; this task does not render a legal interpretation for the project’s exact distribution model. |
| AdGuard Home OpenAPI | `https://github.com/AdguardTeam/AdGuardHome/tree/master/openapi` and `https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/README.md` | The official repository includes an OpenAPI specification for the AdGuard Home REST API; its OpenAPI README documents authenticated API access. |

## 3. Initial Version-1 authentication cost assumption

### 3.1 Planned initial route

The initial project assumption is:

- Firebase Authentication;
- Google/social sign-in only for the optional parent account;
- no phone/SMS sign-in or SMS MFA;
- no SAML/OIDC enterprise federation;
- no Identity Platform upgrade unless a later requirement/threshold/security/vendor review justifies it;
- complete accountless core remains available without authentication.

Under the current Firebase pricing page, Spark is a no-cost plan with no payment method required and “Other Authentication services” are available. Therefore **initial authentication-service fee assumption = $0** for the current small-scale Google/social-sign-in path, subject to Firebase product quotas/abuse limits and future terms/pricing changes.

This is a vendor-price assumption, not a statement that the overall application costs $0. Hosting, compute, storage, backups, network, secrets, logging, domain/TLS and any separately used Google Cloud/Firebase products remain separate infrastructure/service cost categories under TSK-0045.

## 4. Optional Identity Platform thresholds

Identity Platform is optional and changes both features and billing/usage limits.

| Mode / provider class | Current no-cost boundary | Current paid boundary | Current project disposition |
|---|---:|---:|---|
| Base Firebase Authentication, Google/social route on Spark | Firebase pricing lists Other Authentication services on Spark; ordinary Firebase quotas/abuse controls still apply | Not currently required for the planned initial route | **Initial route**; no upgrade performed by this task |
| Firebase Auth **with Identity Platform**, Spark, Tier-1 Email/Social/Anonymous/Custom | 3,000 DAU | Spark is instrumentless/no-cost and does not provide a paid-overage path; exceeding/feature needs trigger plan/provider review | **Optional**, not activated |
| Firebase Auth **with Identity Platform**, Blaze, Tier-1 | 50,000 MAU | 50k–100k $0.0055/MAU; 100k–1m $0.0046; 1m–10m $0.0032; >10m $0.0025 | **Optional**, not activated |
| Identity Platform SAML/OIDC, Spark | 2 DAU | No paid Spark overage path; trigger upgrade/review | Not Version-1 requirement |
| Identity Platform SAML/OIDC, Blaze | 50 MAU | >50 MAU $0.015/MAU | Not Version-1 requirement |
| Phone authentication / SMS MFA | Separate message/SMS billing | Region/message pricing applies | **Excluded from current V1 path**; adding SMS reopens cost/security/vendor review |

The Firebase pricing overview’s 50K MAU no-cost language and the Firebase Authentication documentation’s upgraded-Spark 3,000-DAU limit describe different plan/measurement boundaries; this review does not collapse them. **Spark upgraded usage is governed by the 3,000 DAU / 2 DAU instrumentless limits; Blaze uses the MAU pricing tiers.**

## 5. SMS / phone-auth exclusion

Current TSK-0353 does not introduce local-password, SMS authentication or SMS MFA functionality. Firebase/Identity Platform official pricing treats phone/MFA messaging separately and charges by message/SMS.

Therefore:

- current V1 initial authentication estimate includes **zero SMS/phone messages**;
- no phone-number verification cost is included in the initial auth assumption;
- adding phone sign-in, phone verification or SMS MFA is a **mandatory TSK-0585 reopen trigger** before activation because it changes both cost and security/privacy processing.

## 6. Firebase Authentication processing location — resolved current fact

Earlier planning wording treated authentication processing location as a question that must not be guessed. The current official Firebase Privacy & Security page resolves this factual point:

> Firebase Authentication is run only from US data centers and processes data exclusively in the United States.

Accordingly:

- **processing location for Firebase Authentication is currently confirmed as United States-only**, not “unconfirmed”;
- this task makes no conclusion that US-only processing is legally acceptable for every target user/jurisdiction;
- restricted-transfer mechanism, controller/processor roles, exact data fields, retention, subprocessors, disclosures, notices/consent if applicable and target-market legal acceptability remain separate legal/privacy/security gate questions;
- no location or transfer fact not stated by an authoritative source is inferred;
- any future change to this US-only Authentication statement is a mandatory vendor/privacy/legal re-review trigger.

## 7. Firebase terms / vendor boundary

Current dated findings:

- Firebase Terms page: last modified **May 1, 2026**;
- Firebase Authentication is listed among services subject to the Google Cloud Platform Terms of Service;
- Firebase publishes separate Data Processing and Security Terms;
- the data-processing terms include restricted-transfer/SCC mechanisms, but this document does not decide whether those mechanisms satisfy the project’s final England/UK/EU or other target-market legal requirements.

No offline contract, enterprise support agreement, paid Identity Platform plan, billing account or vendor-specific owner acceptance is inferred.

### Mandatory Firebase re-review / migration triggers

Reopen TSK-0585 or the applicable downstream vendor/legal/architecture task before reliance if any of the following occurs:

1. Firebase Authentication/Identity Platform pricing or no-cost thresholds materially change;
2. current usage approaches the accepted Spark/Blaze threshold or quota;
3. Identity Platform upgrade becomes required for MFA, SAML/OIDC, blocking functions, SLA/support or another accepted requirement;
4. SMS/phone authentication/MFA is proposed;
5. Firebase Authentication processing location changes from current US-only status;
6. Firebase/Google terms, Data Processing and Security Terms, material subprocessors/transfer commitments or applicable service-specific terms materially change;
7. a legal/privacy gate finds the current US-only processing/transfer arrangement unacceptable or unresolved for the target market;
8. provider API/deprecation/lock-in/export/delete limitations prevent TSK-0230/0353 lifecycle requirements;
9. provider outage/reliability or accountless-fallback evidence violates the accepted NFR/SLO boundary;
10. the provider requires a new contract, billing/payment arrangement or material/unbudgeted spend outside current owner-approved authority.

## 8. AdGuard Home licence and API cost finding

Current official AdGuard Home repository evidence establishes:

- AdGuard Home is described by its official repository as **free and open source**;
- repository licence is **GPL-3.0** and the root licence text is GNU GPL Version 3;
- the official project directly documents a **REST API** for integration;
- the repository includes the official **OpenAPI specification** and API authentication documentation;
- self-hosted installation/Docker packages are provided by the project.

### 8.1 Software/API subscription finding

The reviewed official AdGuard Home project materials expose the REST/OpenAPI interface as part of the self-hosted GPL-licensed software and **do not evidence a separate AdGuard Home API subscription or per-call API fee**.

Therefore the current project planning assumption is:

- **AdGuard Home software licence fee: $0 evidenced for the self-hosted GPL-licensed software**;
- **separate AdGuard Home API subscription fee: none evidenced in the reviewed official project materials**;
- AdGuard Home infrastructure/VM/storage/network/backup/operations costs remain **separate** and are governed under TSK-0045/current infrastructure planning;
- this does not mean GPL has no obligations, nor that every future AdGuard commercial service is free.

### 8.2 GPL boundary / no legal conclusion

The licence is a real contractual/legal constraint. Distribution, modification, conveying, source-code availability and combined-work questions may create obligations depending on the actual deployment/distribution model. This task records GPL-3.0 source status only and does not give a final legal interpretation. If the product later distributes, modifies, bundles or conveys AdGuard Home or creates a materially different integration model, route the exact use case through the applicable legal/licensing review before public distribution.

## 9. AdGuard exit / re-review triggers

Reopen the vendor/licence/API review before reliance if:

1. AdGuard Home licence changes or an additional licence/commercial term becomes applicable;
2. the official REST/OpenAPI interface becomes separately licensed/subscription-gated or the project begins relying on a paid AdGuard service rather than the self-hosted Home API;
3. the frozen AdGuard version has a verified security/compatibility blocker requiring upgrade/replacement;
4. required API endpoints/client lifecycle semantics disappear or materially change;
5. a legal/licensing review finds the planned distribution/modification/integration incompatible with project constraints;
6. project infrastructure/operations cost exceeds the accepted budget thresholds even though the software/API remains no-fee;
7. upstream maintenance/security support becomes inadequate for the accepted production risk;
8. the project proposes an unrestricted customer DNS-administration model or other scope change beyond the approved server-side allowlist.

## 10. Infrastructure cost is separate

TSK-0585 does not merge software/vendor licence cost with infrastructure operating cost.

Examples of separate cost categories include:

- Azure/other VM compute for the self-hosted DNS/backend;
- storage/backups/snapshots;
- network/egress/public IP/DNS/domain/TLS dependencies where billable;
- web/account app hosting/compute;
- database/storage for minimum optional-account persistence;
- secret management/logging/monitoring services;
- CI/build/runtime infrastructure;
- any non-auth Firebase/Google Cloud service intentionally introduced later.

These remain subject to current TSK-0045 cost tagging/budget/reporting rules and later architecture/deployment decisions. **A $0 authentication-service or AdGuard API licence assumption must never be presented as a $0 end-to-end service cost.**

## 11. Current factual disposition matrix

| Question | Current evidence-backed answer | Confidence / boundary |
|---|---|---|
| Can initial Google/social Firebase Authentication use a no-cost Spark path? | **Yes**, current pricing lists Other Authentication services on Spark and Spark requires no payment method. | Current vendor fact; quotas/terms may change. |
| Is Identity Platform required for the initial route? | **No evidence of requirement**; Firebase states it is an optional upgrade. | Product/security needs may later trigger upgrade. |
| Upgraded Spark Identity Platform Tier-1 threshold? | **3,000 DAU**; SAML/OIDC **2 DAU**. | Current Firebase Authentication docs/limits. |
| Upgraded Blaze Tier-1 no-cost threshold? | **50,000 MAU**, then tiered per-MAU pricing. | Current Firebase / Google Cloud pricing. |
| SAML/OIDC Blaze threshold? | **50 MAU free**, then `$0.015/MAU`. | Current Identity Platform pricing. |
| SMS/phone cost in current V1? | **Excluded** because current V1 has no SMS path; official vendor pricing bills phone/MFA messages separately. | Reopen before adding SMS. |
| Firebase Authentication processing location? | **US-only**, explicitly stated by Firebase. | Current factual location; legal acceptability not concluded. |
| Firebase terms date? | **May 1, 2026** on the current Firebase Terms page. | Re-review on material terms change. |
| AdGuard Home licence? | **GPL-3.0 / GNU GPL Version 3** in official repository. | Legal obligations depend on exact use/distribution; no legal conclusion here. |
| AdGuard Home software cost? | Official repository describes it as **free and open source**. | Self-hosted software finding; infrastructure separate. |
| AdGuard Home REST/OpenAPI available? | **Yes**, documented by official repository/OpenAPI materials. | Exact version/API compatibility remains TSK-0044/0352. |
| Separate AdGuard Home API subscription? | **None evidenced** in reviewed official self-hosted project materials. | Absence-of-evidence finding, not a perpetual commercial guarantee. |
| Overall service cost zero? | **No such conclusion.** Infrastructure and any other cloud/vendor products are separate. | TSK-0045 and later deployment architecture own these costs. |

## 12. Legal/privacy/unconfirmed questions deliberately not guessed

This review does not determine:

- final lawful basis or transfer mechanism for target users;
- whether current US-only Firebase Authentication processing is legally acceptable for every target jurisdiction;
- final DPA/controller/processor/subprocessor obligations for the actual deployed architecture;
- whether the project’s eventual AdGuard Home use constitutes distribution/conveyance or creates additional GPL obligations;
- final vendor-contract acceptance or owner-signature authority;
- exact future infrastructure spend before the architecture/deployment quantities are known.

These facts remain routed to their authoritative legal/privacy/licensing/architecture/budget gates. They are recorded as unresolved rather than guessed.

## 13. Change control and evidence freshness

Because pricing, quotas, terms and vendor processing facts can change, this evidence must be refreshed before any consequential provider upgrade, paid-plan activation, contract acceptance, production legal/privacy gate, market activation or other action whose correctness depends on these vendor facts.

At minimum, re-check the official source immediately before:

- activating Identity Platform or a billing plan;
- adding SMS/phone/MFA/SAML/OIDC;
- accepting/signing a new vendor agreement;
- making a legal transfer/privacy conclusion;
- distributing/conveying modified or bundled AdGuard Home software;
- materially changing the frozen AdGuard version/API model;
- committing material/unbudgeted spend.

## 14. Acceptance disposition

Current dated official-source evidence establishes:

1. initial Google/social Firebase Authentication has a current no-cost Spark path and no payment method is required for Spark;
2. Identity Platform is optional and its Spark/Blaze/Tier-1/Tier-2 thresholds are explicit;
3. current V1 has no SMS path, so separately billed phone/SMS costs are excluded from the initial auth assumption and are a reopen trigger;
4. Firebase Authentication processing location is currently confirmed as US-only; legal/transfer acceptability remains unresolved and is not guessed;
5. current Firebase Terms are dated May 1, 2026 and applicable data-processing/service terms remain a review trigger;
6. self-hosted AdGuard Home is officially free/open-source, GPL-3.0 licensed and includes a documented REST/OpenAPI interface;
7. no separate AdGuard Home API subscription/per-call fee is evidenced by the reviewed official self-hosted project materials;
8. infrastructure costs remain separate and cannot be collapsed into the software/auth-service cost assumption;
9. legal review/migration/repricing/provider/API/licence/processing-location/threshold triggers are explicit.

No vendor activation, paid-plan purchase, contract acceptance, legal approval, infrastructure purchase, software deployment, participant processing, market activation, lifecycle gate or successor PASS is inferred.

**ACC-0585 current result candidate: PASS pending independent VER-0585, durable EVD-0585, guarded runtime reconciliation and exact GitHub read-back.**
