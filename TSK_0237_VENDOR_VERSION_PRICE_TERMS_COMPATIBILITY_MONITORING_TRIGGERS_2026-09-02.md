# TSK-0237 — Firebase/Auth and AdGuard Version, Price, Terms and Compatibility Monitoring Triggers

**Version:** 1.0.0  
**Date:** 2026-09-02  
**Owner:** SRE/Operations  
**Authority:** L5 operating design derived from current WBS and current official vendor sources. Legal interpretation remains owner-external under CR-0009/DEC-0056.

## Current official-source baseline

| Area | Current observable baseline used for monitoring | Official source |
|---|---|---|
| Firebase Authentication product | Supports federated providers including Google; integrates with custom backends using standard identity protocols. | https://firebase.google.com/docs/auth |
| Firebase pricing | Spark and Blaze plans exist. Most Authentication options are no-cost; phone auth is paid-tier. Firebase pricing currently shows Identity Platform MAU no-cost up to 50K, then Google Cloud pricing. | https://firebase.google.com/pricing ; https://firebase.google.com/docs/projects/billing/firebase-pricing-plans |
| Firebase auth limits | Firebase documents operation/usage limits and explicitly states limits can change without notice and abuse protections can be enabled. | https://firebase.google.com/docs/auth/limits |
| Firebase server sessions | Firebase supports server-side session cookies; documented custom expiration range is 5 minutes to 2 weeks, with revocation support and CSRF protection required around session-login exchange. | https://firebase.google.com/docs/auth/admin/manage-cookies |
| Firebase terms | Firebase service terms page currently reports “Terms last modified: May 1, 2026”; Firebase Authentication is listed under Google Cloud Platform Terms. | https://firebase.google.com/terms |
| Google Cloud subprocessors | Current Google Cloud subprocessor register includes Firebase-related processing/support entries and is the observable register to diff. | https://cloud.google.com/terms/subprocessors |
| Google Identity Services | Sign In With Google release notes track material GIS/FedCM/browser/Workspace-policy changes; current setup requires OAuth client ID and related branding/settings. | https://developers.google.com/identity/gsi/web/reference/release-notes ; https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid |
| Google OAuth | Google OAuth 2.0 documentation defines current authorization flows and token behavior; authentication-only use should remain bounded to the approved sign-in design rather than silently expanding authorization scopes. | https://developers.google.com/identity/protocols/oauth2 ; https://developers.google.com/identity/oauth2/web/guides/overview |
| AdGuard Home API | Official OpenAPI is the integration contract; current spec advertises API version `0.107`, `/control` server path, Basic auth for protected admin API, typed client endpoints, and deprecations such as `GET /clients/find`. | https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/openapi.yaml ; https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/README.md |
| AdGuard API compatibility | Official OpenAPI changelog records incompatible/deprecated/field/default changes; current changelog contains entries through v0.107.79. | https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/CHANGELOG.md |
| AdGuard releases/channels | Official releases and repository are the version source; project documents release/beta/edge channels. Beta/edge are not implicit production-upgrade authority. | https://github.com/AdguardTeam/AdGuardHome/releases ; https://github.com/AdguardTeam/AdGuardHome |
| AdGuard security | Official GitHub Security page/advisories are the security-event source. | https://github.com/AdguardTeam/AdGuardHome/security |

## Monitoring cadence

- **Before every release candidate / production activation:** mandatory refresh of every source in this artifact and comparison against the last accepted baseline.
- **Weekly:** Firebase pricing/limits/auth/session docs, GIS/OAuth release notes, AdGuard releases/OpenAPI/API changelog and supported-platform information.
- **Weekly:** Firebase terms and Google Cloud subprocessor register are fingerprinted for observable change only; any change is routed to the Project Owner/external legal process without AI legal interpretation.
- **Daily or event-driven subscription where platform support exists:** AdGuard security advisories and critical vendor security/deprecation notices.
- **Monthly:** consolidated compatibility/cost review even if no individual threshold fired, including pinned-version drift and quota headroom.
- **Immediately after a vendor incident or unexpected integration failure:** refresh the relevant official sources before retrying or modifying the integration.

## Trigger matrix

| Trigger | Signal / threshold | Responsible owner | Verification | Safe response | Migration / retest path | Gate/state reopening rule |
|---|---|---|---|---|---|---|
| F-AUTH-01 Auth quota/limit | Any documented limit relevant to enabled auth flow changes, or observed peak reaches **>=70%** of an applicable hard/documented quota | SRE/Operations | Diff official auth-limits page; reproduce usage measurement with privacy-safe aggregate | Freeze scale-up that would exceed safe headroom; keep accountless core available; do not bypass abuse controls | Update capacity assumptions; run VAT-004/005/006 and affected load/failure tests | Reopen cost/capacity evidence and any gate whose accepted headroom assumption is invalidated; pre-L6 reopen TSK-0049/LG-07 component if architecture viability changes |
| F-PRICE-01 Price/free-tier | Authentication, Identity Platform, required Firebase/Google Cloud dependency changes price, free tier, billing requirement, or quota economics materially versus approved envelope | SRE/Operations + Finance/Admin | Diff official Firebase pricing/billing pages; calculate projected approved-envelope impact without invented amounts | No automatic plan upgrade/spend; keep optional account feature fenced if cost authority is missing; accountless core remains available | Re-estimate cost; rerun TSK-0586/TSK-0587 resource review as applicable | Reopen the current cost/resource gate if approved envelope could be exceeded; material spend remains owner-controlled |
| F-SESSION-01 Session semantics | Session-cookie max/min lifetime, verification/revocation claims, token issuer/audience/signature requirements, or CSRF guidance changes | Security + SRE/Operations | Diff Firebase session-cookie documentation and affected Admin SDK reference | Freeze auth/session release; do not weaken cookie/CSRF/revocation controls | Update session implementation; run VAT-004/006/007 and security regression | Reopen TSK-0049 if architecture contract changes; after build reopen affected L6 auth task and LG-08/LG-09 evidence |
| F-AUTH-02 Firebase auth API/provider | Google provider, Admin SDK, token verification, supported platform, deprecation or required configuration changes | Engineering + SRE/Operations | Official Firebase auth docs/release notes/reference diff; minimal synthetic auth canary | Pin current known-good version/config; disable only optional auth path if necessary, never accountless core | Upgrade in bounded branch; auth happy/negative/provider-failure/session tests | Reopen affected architecture/build acceptance when compatibility assumption no longer holds |
| G-OAUTH-01 GIS/OAuth browser/flow | GIS release note, FedCM behavior, OAuth client setup, consent/branding, popup/redirect/browser requirement, token-flow or scope guidance changes materially | Web Engineering + Security | Diff Google Identity Services/OAuth official docs; run supported-browser synthetic sign-in | Freeze optional sign-in rollout if incompatible; keep accountless flow usable | Update GIS/auth integration and CSP/COOP/config if required; VAT-003/004/005/006 + browser matrix | Reopen affected auth UX/security evidence; architecture gate only if approved identity/session boundary changes |
| G-OAUTH-02 Scope expansion | Implementation would require any scope beyond the approved authentication-only minimum (`openid`, `email`, `profile` where applicable) or new Google API authorization | Product + Security | Inspect configured OAuth scopes and official Google auth-vs-authorization guidance | Fail closed; do not silently request new data/access | Treat as scope/privacy change requiring current authority before implementation; update threat/privacy tests | Reopen product/privacy/security decisions before implementation; no automatic scope expansion |
| F-TERMS-01 Terms page | Firebase Terms “last modified” value/content fingerprint changes or governing service mapping changes | Project Owner / external legal process; SRE detects only | Archive URL/date/hash metadata, identify changed document; **no AI legal conclusion** | Flag `OWNER_EXTERNAL_SATISFIED` process item; freeze only if a known actual prohibition/technical requirement is identified by higher authority | Technical actions only after owner/external disposition identifies concrete implementation impact | Reopen affected technical gate only when a concrete product/security/privacy/technical requirement changes; never mark legal PASS |
| F-SUBPROC-01 Subprocessor register | Current Google Cloud subprocessor page adds/removes/changes a Firebase-relevant processor, service, activity or location | Project Owner / external legal process; SRE detects only | Structured diff of current register metadata; **no AI legal interpretation** | Route externally; do not infer transfer/compliance status | Apply only explicit resulting technical/privacy-engineering requirements | Same as F-TERMS-01; legal determination remains external |
| A-REL-01 AdGuard stable release | New stable release exceeds the currently pinned production candidate | DNS/AdGuard Engineering + SRE | Compare official release/tag/checksum and changelog to pin | Do not auto-upgrade production; retain known-good pin | Review release + API/config/security deltas; clean-server/rollback + DNS/API regression before adoption | Reopen affected L6 AdGuard/recovery acceptance; reopen TSK-0049/LG-07 only if pre-build architecture compatibility changes |
| A-REL-02 Beta/edge signal | Beta/edge introduces a future breaking API/config/security change relevant to project | DNS/AdGuard Engineering | Review release notes/OpenAPI changelog only; no production adoption from this trigger alone | Create early compatibility work item; keep stable pin | Prepare adapter/config migration and test against isolated/ephemeral target if useful | No PASS invalidation until the change affects selected/pinned supported path, unless current path is announced deprecated/unsafe |
| A-API-01 OpenAPI breaking/deprecation | Used endpoint/field/default/auth scheme changes, is deprecated/removed, or request/response schema becomes incompatible | DNS/AdGuard Engineering | Diff official `openapi.yaml` and `openapi/CHANGELOG.md` against pinned accepted contract | Fail closed on unknown response/field semantics; never expose generic `/control` proxy | Update only typed allowlisted adapter operations; contract/negative/recovery tests including VAT-012/010/011/030 | Reopen typed-adapter acceptance and dependent gate evidence until compatibility is proven |
| A-DEF-01 Privacy/security default | Default for query log/statistics/client logging, TLS/DNS privacy, authentication, filtering, or ClientID-related behavior changes | Security + DNS/AdGuard Engineering | Diff OpenAPI/changelog/config defaults; clean install inspection | Preserve explicit privacy-safe configuration; never rely solely on vendor default | Update explicit configuration + clean-server/idempotency/privacy tests | Reopen affected privacy/security/recovery task and downstream gate evidence |
| A-SEC-01 Security advisory | Critical/High advisory affects deployed/pinned version or project-used API/config surface; lower severity with applicable exploit path also triggers | Security + SRE/Operations | Match advisory affected versions/config to pin and project usage | Fence deployment; patch/mitigate or disable affected optional surface; rotate credentials if exposure plausible | Upgrade to fixed version or apply documented mitigation; security, API, DNS, clean-server and rollback tests | Reopen affected security/build/release evidence immediately; current gate cannot PASS with unresolved applicable Critical/High risk |
| A-LIC-01 AdGuard license | Repository license identifier/text or published licensing terms materially change | Project Owner / external legal process; SRE detects only | Compare repository license metadata/text and source revision; no AI legal conclusion | Route externally; do not infer permission/prohibition | Apply technical packaging/dependency changes only if owner/external disposition requires them | Reopen technical/release gate only for concrete implementation/distribution impact; no legal PASS inference |
| A-PLAT-01 Platform compatibility | Official support matrix/release assets stop supporting the selected Ubuntu/Linux architecture or required runtime dependency | SRE/Operations | Verify current official release assets/platform docs on target architecture | Freeze upgrade/build path that lacks supported artifact | Select supported pinned version/architecture or owner-approved platform change; clean-server recovery retest | Reopen server/recovery architecture and relevant LG-07/L6 evidence if current target is no longer viable |

## Baseline fingerprint record

For each scheduled review retain privacy-safe metadata only:

`source_id | canonical_url | checked_at_utc | observed_version_or_modified_date | content/hash-or-ETag-if-available | disposition | affected_task_ids`

Do not store credentials, tokens, raw DNS queries, browsing history, or unnecessary personal data in the monitoring record.

## Verification and response workflow

1. Fetch the canonical official source; reject mirrors/blogs as decision authority.
2. Compare to the last accepted fingerprint/version/pin and classify: `NO_MATERIAL_CHANGE`, `TECHNICAL_RETEST`, `COST_REVIEW`, `OWNER_EXTERNAL_REVIEW`, or `SECURITY_BLOCKER`.
3. Identify exact accepted assumption/task/gate potentially invalidated; historical PASS is not reused when the vendor change contradicts it.
4. Apply the matrix safe response before migration. Ambiguous non-idempotent vendor changes are never blindly retried.
5. Implement the smallest compatibility/migration correction under current Action Authority.
6. Re-run the mapped TSK-0516 VAT tests plus vendor-specific contract/security/recovery tests.
7. Persist source/date/version/hash, test evidence and disposition; reopen current runtime state only when the new evidence materially invalidates accepted criteria.

## Legal/commercial boundary

TSK-0237 monitors observable **price/quota/terms/subprocessor/license changes** so project governance notices them. Under CR-0009/DEC-0056, AI does not determine whether changed terms, subprocessors, licenses or transfers are legally acceptable and does not create legal approval. Technical/security/privacy-engineering consequences identified by actual authority remain mandatory.

## Acceptance decision

This operating design defines owners, cadence, official signals, quantitative/material thresholds, verification, fail-safe response, migration/retest paths and gate-reopening semantics for every TSK-0237 class. It creates no vendor upgrade, spend, legal conclusion, production action or LG-07 PASS by itself.
