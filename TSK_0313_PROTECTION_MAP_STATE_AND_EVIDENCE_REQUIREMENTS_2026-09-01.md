# TSK-0313 — Protection Map State and Evidence Requirements

**Task:** TSK-0313 — Specify Protection Map state and evidence requirements  
**Acceptance:** ACC-0313 / VER-0313 / EVD-0313  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 1.0.0-post-CR-0008  
**Date:** 2026-09-01  
**Status:** CURRENT L4 REQUIREMENT CANDIDATE; implementation, user validation, and downstream PASS are not inferred  
**Authority:** current owner-frozen modular Master Planning System; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008; TSK-0041 current DNS activation requirement; TSK-0144 current external-service safeguard requirement; TSK-0146 current Version-1 product baseline; TSK-0320 current Protection-State Model and Copy Rules.  

## 1. Acceptance boundary

The Protection Map is an evidence-backed status map for individual protection items. It is not a safety score and must never imply complete protection.

Every displayed protection item must resolve to exactly one of the current six states from TSK-0320:

1. `protected/verified`
2. `configured/parent-confirmed`
3. `action-needed`
4. `not-covered`
5. `uncertain/error`
6. `removed`

The selected state must be derived from current evidence for the exact item, device/layer/path/scope. Journey completion, configuration/profile presence, ClientID presence, parent confirmation, account ownership, dashboard/device registration, or a stored prior state are not technical verification.

Only fresh qualifying technical evidence from an approved verifier may produce `protected/verified`.

## 2. Protection-item record required by the experience contract

Each Protection Map item must expose or internally retain the minimum fields needed to make its displayed state reproducible and testable:

- `protection_item_id`
- `capability_or_layer`
- `declared_scope`
- `state_id`
- `reason_code`
- `evidence_refs`
- `evidence_evaluated_at`
- `freshness_or_expiry_boundary` where applicable
- `verifier_id` and `verifier_version` where technical verification exists
- `instruction_catalogue_id`
- `instruction_version`
- `source_ref`
- `source_checked_at`
- `source_review_trigger`
- `copy_version`
- `locale`
- `persistence_domain` (`anonymous-journey`, `parent-owned-device`, or `none`)

No protection-item record may contain browsing/query/activity history, raw DNS history, domains/URLs visited, child surveillance data, secrets, tokens, or unrestricted AdGuard administration material.

## 3. State requirements

### S1 — `protected/verified`

**Entry rule**

- Current positive technical evidence from an approved verifier exists for the exact declared scope.
- The evidence is still within its verifier-defined freshness boundary.
- No newer or equally authoritative material contradiction, removal event, unsupported determination, or unresolved path change exists.

**Evidence rule**

Only TSK-0320 E1 qualifying technical evidence may establish S1. E2 configuration/parent/account evidence cannot establish S1.

**Parent-facing copy**

| Locale | Primary | Supporting |
|---|---|---|
| en | Protection verified | UseSafeWeb verified this protection step for this setup. |
| tr | Koruma doğrulandı | UseSafeWeb bu kurulum için bu koruma adımını teknik olarak doğruladı. |
| ar | تم التحقق من الحماية | تحقّق UseSafeWeb تقنيًا من خطوة الحماية هذه لهذا الإعداد. |

When material, scope and verification time/limit must remain visible. Never use `Fully protected`, `Safe`, or equivalent universal assurances.

**Transitions**

- remain S1 on fresh successful re-verification;
- S1 → S3 when current reliable negative evidence identifies a concrete safe remedy;
- S1 → S5 when evidence becomes stale, conflicting, unavailable, or context/path changes make the prior proof insufficient;
- S1 → S4 on current authoritative not-covered determination;
- S1 → S6 on completed removal/revocation.

**Unsupported behavior**

S1 is impossible for an unsupported item or path.

**Persistence scope**

A persisted S1 value is only cached display metadata. It is not itself technical evidence and must be recomputed from current evidence before being presented as current after resume/sign-in/reinstall/device replacement/context change.

**Representative deterministic example**

Fresh approved DNS-path verifier returns positive for the currently active supported path with no contradiction → S1. Merely finding the profile installed → not S1.

---

### S2 — `configured/parent-confirmed`

**Entry rule**

Current configuration or explicit parent-confirmation evidence proves that the requested setup step was completed, but no fresh qualifying positive technical verification exists and no unresolved material contradiction is being hidden.

**Evidence rule**

TSK-0320 E2 only. Parent identity, ownership, dashboard presence, device registration, profile presence, installer success, and explicit parent confirmation may support S2 but may never promote to S1.

**Parent-facing copy**

| Locale | Primary | Supporting |
|---|---|---|
| en | Setup confirmed | Protection has not yet been technically verified. |
| tr | Kurulum onaylandı | Koruma henüz teknik olarak doğrulanmadı. |
| ar | تم تأكيد الإعداد | لم يتم التحقق تقنيًا من الحماية بعد. |

**Transitions**

- S2 → S1 only after fresh qualifying technical evidence;
- S2 → S3 on reliable evidence that corrective action is required;
- S2 → S5 on unresolved conflict, stale/indeterminate verification, or material path uncertainty;
- S2 → S4 on authoritative not-covered determination;
- S2 → S6 on completed removal/revocation.

**Unsupported behavior**

Do not use S2 as a cosmetic substitute for S4 or S5.

**Persistence scope**

Optional parent/device records may retain setup-confirmation context where separately authorized. Account ownership may authorize access to that record but never strengthens its evidence class.

**Representative deterministic example**

Parent confirms the external-service safeguard step from the current catalogue, but there is no independent verifier → S2, never S1.

---

### S3 — `action-needed`

**Entry rule**

The item is applicable/supported and current reliable evidence identifies a concrete safe action required to establish or restore the intended state.

**Evidence rule**

Requires an actionable condition traceable to current evidence/source. A generic assumption that the parent should “try again” is insufficient if the reason is unknown; unknown status belongs in S5.

**Parent-facing copy**

| Locale | Primary | Supporting template |
|---|---|---|
| en | Action needed | {specific_action}. Then verify again. |
| tr | İşlem gerekli | {specific_action}. Ardından yeniden doğrulayın. |
| ar | يلزم إجراء | {specific_action}. ثم أعد التحقق. |

**Transitions**

- S3 → S1 when remediation is followed by fresh qualifying technical evidence;
- S3 → S2 when remediation/setup is confirmed but technical verification is not available or has not yet succeeded;
- S3 → S5 when the remediation result is ambiguous/inconclusive;
- S3 → S4 if authoritative coverage becomes not-covered;
- S3 → S6 on completed removal/revocation.

**Unsupported behavior**

An unsupported path is S4, not S3.

**Persistence scope**

Persist only the minimum action reason/source/version needed to resume the approved journey. Do not infer the action from browsing history or raw DNS history.

**Representative deterministic example**

Supported DNS mechanism is configured incorrectly and a current approved diagnostic identifies one exact safe correction → S3.

---

### S4 — `not-covered`

**Entry rule**

Current authoritative coverage evidence says the exact capability/device/path/service is unsupported, outside approved scope, or has no approved applicable safeguard.

**Evidence rule**

Requires source-backed coverage determination with source/version and evaluation time. A failed supported setup is not S4 merely because it did not work.

**Parent-facing copy**

| Locale | Primary | Supporting |
|---|---|---|
| en | Not covered | UseSafeWeb does not cover this on your current setup. |
| tr | Kapsanmıyor | UseSafeWeb mevcut kurulumunuzda bunu kapsamıyor. |
| ar | غير مشمول | لا يغطي UseSafeWeb هذا في إعدادك الحالي. |

**Transitions**

- remain S4 while authoritative coverage is unchanged;
- S4 → S3 when coverage becomes supported and a concrete setup action is required;
- S4 → S2 when coverage becomes supported and setup is confirmed but not technically verified;
- S4 → S5 when applicability becomes possible but actual state is still indeterminate;
- S4 → S1 only when coverage is supported and fresh qualifying technical evidence exists;
- S4 → S6 only for a previously configured artifact that is actually removed; never invent removal for a never-configured unsupported item.

**Unsupported behavior**

S4 is the explicit unsupported state. It must remain visible and must not be converted to success, completion, or a generic warning.

**Persistence scope**

Coverage result may be cached only with its source/version/review trigger. When source currency expires or platform/service support changes, re-evaluate rather than displaying stale S4 as current.

**Representative deterministic example**

Parent selects an external service that is not in the current approved supported catalogue → S4 with a truthful reason/fallback; no fake completion task is created.

---

### S5 — `uncertain/error`

**Entry rule**

A trustworthy current classification cannot be made because relevant evidence is missing/stale, materially conflicting, verification is unavailable/timed out/errored, or the effective path/context is indeterminate.

**Evidence rule**

Use explicit uncertainty/error evidence and preserve the affected scope. Prior S1/S2 cannot remain visible as a current positive assurance when current evidence is materially uncertain.

**Parent-facing copy**

| Locale | Primary | Supporting |
|---|---|---|
| en | Protection status could not be verified | Retry verification or follow the troubleshooting steps before relying on this protection. |
| tr | Koruma durumu doğrulanamadı | Bu korumaya güvenmeden önce doğrulamayı yeniden deneyin veya sorun giderme adımlarını izleyin. |
| ar | تعذر التحقق من حالة الحماية | أعد محاولة التحقق أو اتبع خطوات استكشاف الأخطاء وإصلاحها قبل الاعتماد على هذه الحماية. |

**Transitions**

- S5 → S1 only on fresh qualifying technical evidence;
- S5 → S2 only after uncertainty/conflict is resolved and reliable current setup confirmation remains without qualifying technical evidence;
- S5 → S3 when reliable evidence resolves uncertainty into a concrete action;
- S5 → S4 when authoritative coverage proves not-covered;
- S5 → S6 on completed removal/revocation.

**Unsupported behavior**

Do not use S5 when current authoritative evidence already proves S4 or S6.

**Persistence scope**

S5 may retain minimum error/retry metadata but never raw browsing/DNS history. A subsequent resume must re-evaluate current evidence rather than silently restoring a prior positive state.

**Representative deterministic example**

Browser/app secure DNS or VPN state makes the effective resolver path indeterminate and current diagnostics cannot resolve it → S5.

---

### S6 — `removed`

**Entry rule**

Current evidence establishes completed/confirmed removal, revoke, unlink, uninstall, reset, or equivalent de-enrolment for the exact relevant item/scope, with no later explicit new setup superseding it.

**Evidence rule**

Requires an explicit removal/revocation event. Account deletion, saved-device-record deletion, dashboard unlink, and physical DNS configuration removal are distinct operations and must not be conflated.

**Parent-facing copy**

| Locale | Primary | Supporting |
|---|---|---|
| en | Removed | This setup is no longer enrolled through UseSafeWeb. |
| tr | Kaldırıldı | Bu kurulum artık UseSafeWeb üzerinden kayıtlı değil. |
| ar | تمت الإزالة | لم يعد هذا الإعداد مسجّلًا عبر UseSafeWeb. |

**Transitions**

- remain S6 until a later explicit new setup/enrolment/configuration event exists;
- S6 → S2 after a new setup is confirmed without qualifying technical evidence;
- S6 → S3 when a new setup attempt is incomplete or needs remediation;
- S6 → S5 when a new attempt exists but its status is indeterminate;
- S6 → S4 if the newly evaluated scope is not covered;
- S6 → S1 only after later explicit setup plus fresh qualifying technical evidence.

**Unsupported behavior**

Do not invent S6 for an unsupported path that was never configured.

**Persistence scope**

Removal history may be retained only where separately authorized to prevent a stale positive state from reappearing. A surviving account/device record cannot undo S6 or recreate S1.

**Representative deterministic example**

Parent completes removal of the UseSafeWeb DNS configuration and the removal operation is confirmed → S6 for that DNS configuration scope. Keeping the parent account does not change that state.

## 4. Deterministic state selection

For each item, evaluate current evidence for the same scope in this order:

1. latest applicable completed removal/revocation with no later explicit setup → S6;
2. current authoritative not-covered determination → S4;
3. material conflict/staleness/unavailable/indeterminate evidence → S5;
4. fresh qualifying positive technical evidence → S1;
5. current reliable actionable remediation condition → S3;
6. current setup/configuration/parent-confirmation evidence without qualifying technical evidence → S2;
7. applicable item with a known required setup action → S3; otherwise S5.

The evaluator may retain underlying facts separately, but the parent-facing state must be one truthful current state. No positive state may visually or textually override a current S4/S5/S6 condition.

## 5. Anonymous journey versus optional parent-owned device state

The product has two distinct state domains under the current Version-1 scope.

### Anonymous journey domain

- Exists only for the accountless setup journey and only within the separately approved anonymous-state lifecycle.
- Uses opaque journey/session references rather than parent identity.
- May retain only the minimum Protection Map state/evidence references necessary to complete or resume that anonymous journey.
- Must not be automatically joined, promoted, or copied into a parent account/device record merely because the parent later signs in.
- Sign-in must not extend evidence freshness or strengthen any Protection Map state.

### Optional parent-owned device domain

- Exists only after the parent explicitly uses the optional account/device-management capability and ownership is server-side authorized.
- May retain minimum approved device-management context and Protection Map metadata where separately authorized by the persistent data model.
- Ownership authorizes access; it is never technical protection evidence.
- A persisted state is not self-validating. Before presentation as current, evidence/freshness must be re-evaluated.
- Deleting/revoking account/device state is not proof that physical DNS/profile configuration was removed, and physical removal is not by itself proof that all account/device records were deleted.

**Hard separation invariant:** no browsing/query/activity history is stored in either domain to derive, preserve, or upgrade Protection Map state.

## 6. Source currency and instruction ownership

To satisfy REQ-0035, any state that presents platform/service-specific instructions, support/coverage conclusions, verifier behavior, or remediation must be backed by a versioned instruction-catalogue entry containing at minimum:

- stable instruction/catalogue ID;
- applicable platform/service/version rule;
- source reference;
- source checked/reviewed date;
- instruction version and copy version;
- owning role;
- expected result;
- known scope/limitations;
- unsupported/not-applicable behavior;
- verifier ID/version/freshness rule if technical verification exists;
- review triggers.

Minimum review triggers include material platform/service version change, provider documentation change, contrary technical test, verifier behavior change, changed support matrix, security/privacy concern, or the catalogue review deadline.

If an instruction or coverage source is stale or its applicability cannot be established, the UI must suppress unsupported certainty and resolve to S5 or S4 according to current evidence; it must not continue presenting stale success guidance.

Product owns state/eligibility policy. Content owns instruction/copy source currency. QA owns deterministic state/copy/transition verification. Privacy/safeguarding review is required before any new data/credential/account-linkage processing is introduced.

## 7. Accessibility, localization, and RTL requirements

- English, Turkish, and Arabic are required technical-language variants for the first public release under CON-0017.
- Arabic renders RTL; state semantics, evidence strength, actor, scope, and uncertainty must remain identical to English.
- Localization may never strengthen S2 into S1 or weaken S4/S5/S6.
- Primary state text must not rely on color/icon alone. Text labels remain perceivable and programmatically associated with the affected protection item.
- S1 and S2 must be visually distinguishable; a positive visual treatment must not make parent confirmation appear system-verified.
- Dynamic S3 action text and S4/S5 reasons must remain understandable when localized and must not expose internal identifiers/secrets.
- Technical language availability does not imply official localized market/legal/support activation; LG-16 remains separate.

## 8. Deterministic representative test set

These are internal specification tests, not human/user validation.

| Test | Evidence/input | Required state/result |
|---|---|---|
| PM-01 | Parent confirms configuration; no technical verifier result | S2; supporting copy says not technically verified |
| PM-02 | Profile/ClientID exists; no technical verifier result | not S1; S2/S3/S5 according to current evidence |
| PM-03 | Parent owns device in dashboard; no technical verifier result | ownership does not change evidence state |
| PM-04 | Fresh approved technical verifier positive for exact scope | S1 |
| PM-05 | Prior S1 evidence is now stale | S5 unless stronger current evidence selects S4/S6 |
| PM-06 | Supported setup fails and current diagnostic gives one safe remedy | S3 |
| PM-07 | Exact platform/path is currently unsupported | S4 |
| PM-08 | VPN/browser/app resolver makes path indeterminate | S5 |
| PM-09 | Explicit removal/revocation completes | S6 |
| PM-10 | S6 + parent account/device record remains | stays S6; account persistence does not restore protection |
| PM-11 | S6 + explicit new setup confirmation but no technical verification | S2 |
| PM-12 | S6 + explicit new setup + fresh qualifying technical verification | S1 |
| PM-13 | Unsupported external service selected | S4; no fake completion step |
| PM-14 | External-service step parent-confirmed, no approved verifier | S2 |
| PM-15 | Sign-in resumes a stored prior S1 value whose evidence is stale | recompute; not S1 |
| PM-16 | Anonymous journey state exists then parent signs in | no automatic identity join or evidence-strength upgrade |
| PM-17 | Current state has conflicting evidence | S5 unless current authoritative S4/S6 rule deterministically applies |
| PM-18 | EN/TR/AR render of S2 | all variants retain explicit no-technical-verification meaning |
| PM-19 | Arabic render | RTL and same semantic strength as English |
| PM-20 | Any state record | contains no browsing/query/activity history or secret |

## 9. Acceptance mapping

- **Entry/evidence rules:** Sections 2–4 define evidence schema, state entry, precedence, and evidence class boundaries.
- **Parent-facing copy:** Section 3 freezes EN/TR/AR primary/supporting copy or templates for all six states.
- **Transition rules:** Section 3 plus deterministic selection in Section 4 defines allowed transitions and fail-closed behavior.
- **Unsupported behavior:** Every state section defines unsupported behavior; S4 is the explicit not-covered state.
- **Persistence scope:** Every state section plus Section 5 separates cached state metadata from evidence and separates anonymous journey state from optional parent-owned device state.
- **Testable examples:** Section 8 supplies deterministic representative cases.
- **Parent-confirmed versus system-verified:** S2/E2 and S1/E1 are explicitly non-interchangeable; only fresh qualifying technical evidence can establish S1.
- **Account ownership:** authorizes access only and never substitutes for technical verification.
- **Privacy:** no browsing/query/activity history is stored or required.
- **REQ-0028:** every state interaction/confirmation is necessary to explain or change a Protection Map outcome; no unnecessary identity step is introduced.
- **REQ-0029:** state/action behavior preserves supported automatic configuration and technically correct platform-specific fallbacks without inventing support.
- **REQ-0035:** platform/service instructions and support determinations are versioned, source-backed, owner-assigned, and monitored for change.
- **CON-0010:** complete accountless core remains usable without login; optional account/device persistence is strictly separate and minimal.
- **CON-0017:** EN/TR/AR technical-language requirements and RTL semantics are explicit without implying market activation.
- **INT-0009 / INT-0010:** engineering and QA receive exact states, content, errors/recovery, i18n/accessibility semantics, and deterministic acceptance cases.

## 10. Evidence and non-inference

This artifact is specification evidence for ACC-0313. It relies on current durable project authority and current predecessor contracts; it does not claim real-user comprehension/usability evidence. Under RSK-0002, internal/automated representative tests are not user validation and must not be labelled as such.

No verifier implementation, datastore/schema implementation, browser/device test execution, legal/privacy-compliance conclusion, human behavioral validation, build, deployment, production activation, market activation, launch, or downstream gate/task PASS is inferred by this requirement freeze.
