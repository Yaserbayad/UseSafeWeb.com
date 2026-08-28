# TSK-0042 — User Support, Exception, Recovery and Removal Requirements

**Task:** TSK-0042 — Specify user support, exception, recovery, and removal requirements  
**Acceptance:** ACC-0042  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 SUPPORT/RECOVERY REQUIREMENTS / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** DEC-0042 accountless-first + EXC-0001/EXC-0008 + TSK-0041 DNS activation requirements + TSK-0146 accountless baseline + TSK-0229 accountless journey data contract + TSK-0409 support matrix + TSK-0320 protection-state semantics + existing false-positive/diagnostic/safeguarding procedures + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

This contract defines the minimum support/recovery behavior that is justified by current owner decisions, technical evidence and existing operational procedures. It does **not** prove that representative parents can self-serve successfully, that the support burden is acceptable, or that the proposed wording/sequence is understood. Those behavioral questions remain unresolved under `RSK-0002` and the deferred L3 branch.

This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real participants, legal completion, payment, publication or launch.

## 1. Support objective and boundary

The active UseSafeWeb support model must help a parent recover safely from an accountless first-phone setup problem without creating surveillance, persistent identity, unnecessary diagnostics or false protection claims.

Support must cover, at minimum:

1. accountless setup/journey-state recovery;
2. supported device-configuration lifecycle and removal;
3. UseSafeWeb/AdGuard encrypted-DNS setup and verification incidents;
4. baseline-filtering false positives and narrow exceptions;
5. unsupported/conflicting device, network, VPN, Private Relay, browser/app DNS and managed-device states;
6. privacy/security and safeguarding escalation boundaries;
7. deletion and recovery of transient product state; and
8. privacy-minimal support-burden measurement.

UseSafeWeb support is **not** a remote administration service, emergency service, safeguarding investigation service, surveillance service or general technical-support desk for unrelated device/app problems.

## 2. Accountless-first support contract

`DEC-0042` and `EXC-0001` control the baseline.

### Required behavior

- No support path may require a UseSafeWeb login, password reset, account recovery, email address, phone number or persistent customer identity.
- A parent must be able to reset/restart the supported journey and remove/recover the DNS configuration without authenticating to UseSafeWeb.
- Support must not create a persistent parent/device record merely to remember a support case.
- Any temporary journey state must follow the TSK-0229 J0/J1 contract.
- If a future problem can only be solved with persistent account/device identity, that is evidence for the `EXC-0001` trigger; it does not silently activate an account architecture.
- Customer-facing AdGuard administration credentials/control-plane access remain excluded.

### Staffed-support boundary

`EXC-0008` keeps routine staffed customer support deferred. Therefore:

- ordinary issues must have a self-service path wherever the current product claims support;
- escalation is exceptional and issue-class-driven, not the default completion mechanism;
- this contract defines product/system **response behavior**, not an unapproved human-response-time SLA;
- later evidence that ordinary issues cannot be safely productized/self-served must be recorded as support-burden evidence and routed through the EXC-0008 trigger/owner authority.

## 3. Controlled issue taxonomy

The product/help system must classify the current problem before giving a remedy. Reuse the existing support taxonomy rather than inventing parallel categories.

| Class | Typical condition | Minimum response |
| --- | --- | --- |
| `SETUP` | Parent cannot complete a supported platform step | Show current supported instruction, state and next reversible action. |
| `JOURNEY_STATE` | Browser/session reset, expired transient state, invalid resume token or partial accountless journey | Restore from allowed J0/J1 state where valid; otherwise restart safely without identity recovery. |
| `DNS_REACHABILITY` | Resolver/profile/DoT/DoH path cannot be reached or verified | Distinguish endpoint/service/network/configuration cause where evidence permits; never retain S1 without current verification. |
| `FILTERING_FALSE_POSITIVE` | Legitimate required service appears blocked by UseSafeWeb filtering | Reproduce with low-data/synthetic evidence and use the narrowest safe reversible exception if justified. |
| `COMPATIBILITY_CONFLICT` | VPN, Private Relay, browser/app custom DNS, captive portal, managed device/network or transport interaction | Use S5/S4 as appropriate; do not invent coexistence or bypass a required control. |
| `REMOVAL_RECOVERY` | Parent wants to remove UseSafeWeb or normal DNS behavior must be restored | Execute the platform-specific removal path, verify ordinary recovery, withdraw protection claim. |
| `STALE_GUIDANCE` | Current OS/provider/service behavior no longer matches the owned instruction | Stop presenting the affected instruction as current; route to not-covered/uncertain until reviewed. |
| `SERVICE_OUTAGE` | UseSafeWeb DNS/service itself is unhealthy | Distinguish service fault from local setup; show uncertainty/action needed and recovery/removal option. |
| `PRIVACY_SECURITY` | Suspected prohibited persistence, secret exposure, unsafe diagnostics or material security/privacy defect | Stop affected path and escalate under the applicable incident/privacy/security process. |
| `SAFEGUARDING` | Abuse, neglect, grooming, exploitation or immediate-danger disclosure/concern | Exit product troubleshooting on the disclosure; follow the dedicated child-safety escalation procedure. |
| `GUIDANCE` | Parent asks what UseSafeWeb covers/does not cover | Use the current Protection Map/claims contract; do not promise complete safety. |

If the symptom does not fit a supported class, record the smallest safe `OTHER/unsupported` classification rather than improvising an unsupported configuration.

## 4. Severity and support routing

Reuse the current support severity semantics:

- **S1 urgent:** safety/privacy/security or safeguarding boundary. Stop the affected product/diagnostic path immediately and use the applicable escalation route.
- **S2 blocking:** supported setup/protection cannot safely continue. Do not advance the journey as successful; provide one bounded repair/recheck or removal/recovery path.
- **S3 degraded:** the user can continue only with an explicit limitation/workaround whose protection consequence is stated truthfully.
- **S4 informational:** no material protection impact; answer through current source-backed help.

Severity is separate from the TSK-0320 Protection Map state. Support may assign an incident severity while the product state is S3 `Action needed`, S4 `Not covered`, S5 `Status uncertain`, or S6 `Removed`.

## 5. Accountless journey-state recovery

TSK-0229 remains authoritative for J0/J1 state, expiry, deletion and no-linkage.

### J0 — browser/session state

- If valid J0 remains available, use only the minimum current routing/protection state needed to resume the immediate session.
- A reset/start-over action clears J0 immediately.
- Lost/destroyed J0 has no server-side identity-recovery path; the safe remedy is to restart the necessary step(s).
- Re-entry must not assume a prior S1 `Verified` state without current evidence.

### J1 — optional anonymous short-lived state

Where a later implementation legitimately uses J1:

- resume only with a valid opaque journey token and unexpired record;
- hard expiry remains no later than 24 hours from creation and is non-sliding;
- expired/deleted/invalid tokens must not be reconstructed from IP, cookies, fingerprinting, account identity or support notes;
- if J1 cannot be recovered, restart safely rather than asking the parent to create an account;
- completion/reset/exit and other TSK-0229 early-deletion triggers remain binding;
- support must never lengthen J1 retention merely to make troubleshooting convenient.

## 6. Device-configuration lifecycle requirements

Support must treat configuration as a lifecycle, not a one-time install success.

### Minimum lifecycle states

1. **Not configured / action needed** — supported route exists but has not been completed.
2. **Configured but unverified** — expected platform setting/profile exists or is parent-confirmed, but current UseSafeWeb verification has not succeeded.
3. **Verified** — current approved verifier succeeds for the exact supported tuple and no known conflict invalidates the claim.
4. **Conflict/uncertain** — effective resolver or coverage cannot be established.
5. **Unsupported/not covered** — the current device/network combination is outside the accepted matrix.
6. **Removal requested/in progress** — parent chooses exit or recovery requires reverting UseSafeWeb configuration.
7. **Removed** — platform-specific UseSafeWeb configuration is removed/reset and the UseSafeWeb protection claim is withdrawn.
8. **Recovery verified** — ordinary DNS/internet behavior is confirmed after removal using neutral/synthetic checks; this does not imply UseSafeWeb protection is active.

The user must be able to move from any supported configuration state toward safe removal/recovery without an account.

## 7. DNS/AdGuard integration incident requirements

Consume TSK-0041 and TSK-0409; do not create alternate resolver semantics.

### Android

- Supported native path is Android 9+ phone with usable Private DNS provider hostname control, configured with hostname `dns.usesafeweb.com` using native DoT.
- Do not substitute a VPN/app workflow merely because the native route fails.

### iPhone

- Supported path is iPhone/iOS 14+ using the approved DNS Settings profile with DoH URL `https://dns.usesafeweb.com/dns-query`.
- Profile presence alone is not verification.

### Minimum DNS incident classes

Support must distinguish at least:

- invalid platform input/profile;
- endpoint unreachable;
- TLS/certificate/authentication failure;
- transport reachable but filtering verification failed;
- service outage;
- effective resolver path uncertain;
- VPN/Private Relay/browser/app conflict;
- unsupported/managed device/network;
- stale profile/instruction;
- removal/recovery failure.

Each incident class must map to one truthful protection state and one bounded next action or explicit unsupported result. It must not collapse to a generic “try again” loop.

## 8. False-positive and exception requirements

The accepted filtering baseline uses a narrow reversible exception model. Support must preserve it.

### Required sequence

1. Receive a specific symptom without asking for browsing history.
2. Confirm it is within current support scope.
3. Reproduce with synthetic/non-participant evidence where possible.
4. Establish whether UseSafeWeb filtering is actually causal rather than the site/app/upstream/device/network/other policy.
5. If correction is justified, apply only the narrowest safe exception through the owning configuration/change process.
6. Re-test the legitimate path.
7. Re-test a relevant blocked/filtering regression so protection is not silently disabled.
8. Make the change reversible and record only privacy-safe evidence.
9. Update the Protection Map truthfully.

### Hard limits

- Never disable the whole filtering baseline to solve one false positive.
- Never create a parent-facing persistent personalized allowlist/dashboard in the active accountless baseline.
- Never infer a per-device exception capability from the existence of a global technical exception mechanism.
- If the exception would materially weaken protection or its effect cannot be established, use `Action needed`, `Status uncertain` or `Not covered` instead of preserving S1.

## 9. Unsupported/conflict-state behavior

For VPN, Private Relay, browser/app custom DNS, captive portals, transport blocking, managed devices/networks, IPv6-only/NAT64-only contexts and other TSK-0409 unsupported/not-yet-supported combinations:

1. do not claim coexistence unless exact current evidence exists;
2. do not instruct the parent to defeat employer/school/security/privacy controls merely to make UseSafeWeb appear successful;
3. do not label profile/setting presence as verified when the effective resolver is uncertain;
4. provide the smallest safe explanation and either a supported re-check or an explicit `Not covered`/`Status uncertain` result;
5. where UseSafeWeb configuration is causing loss of normal connectivity and no safe supported fix exists, route to removal/recovery;
6. record the unsupported/conflict category for aggregate product-improvement analysis without browsing/domain history or persistent identity.

## 10. Data-minimising diagnostics

Routine support follows the existing evidence hierarchy:

1. configuration/state inspection without request history;
2. purpose-built synthetic test traffic;
3. non-identifying service health/configuration evidence;
4. minimal redacted screenshots/config excerpts only where genuinely necessary;
5. exceptional request-level/identifiable diagnostics only through the separately governed exceptional diagnostic procedure.

### Exceptional diagnostic boundary

The exceptional procedure remains authoritative and requires, before collection:

- a concrete incident/ticket ID;
- lower-data checks already attempted;
- necessity rationale;
- exact field allowlist and smallest affected scope;
- fixed UTC start/end;
- restricted approved storage/access;
- Project Owner or delegated incident/privacy approval;
- user-notice decision where applicable;
- deletion owner and deletion-verification method.

Exceptional collection must stop at resolution or approved end time, restore the privacy-minimal baseline, delete the temporary dataset/copies, and record deletion verification. Raw diagnostic/query data must never be committed to GitHub or reused for analytics/profiling/marketing.

Ordinary support cannot use the exceptional process merely because it is easier than synthetic/state-based diagnosis.

## 11. Privacy/security and safeguarding escalation

### Privacy/security

Stop the affected path and escalate when support reveals or reasonably indicates, for example:

- persistent identifiable query/domain history unexpectedly enabled;
- identifiable client statistics outside the approved baseline;
- raw family/child browsing data copied to an unapproved system;
- exposed credential/token/private key;
- unsafe or over-broad diagnostic collection;
- material protection claims unsupported by evidence;
- deletion verification failure for exceptional diagnostics.

Technical symptom resolution does not close the incident if the privacy/security deviation remains unresolved.

### Safeguarding

A child-safety disclosure/concern is not debugged as a product issue. The dedicated safeguarding procedure owns the route. Immediate danger must not be delayed by UseSafeWeb troubleshooting. Personal/raw disclosures stay out of GitHub and general support analytics.

## 12. Response expectations — no fabricated human SLA

The product must define deterministic **service-response behavior** while routine staffed support remains deferred.

| Severity | Product/system response expectation | Human escalation expectation |
| --- | --- | --- |
| S1 | Immediately stop the affected unsafe path, present the applicable emergency/safeguarding/privacy/security boundary, and do not continue optimistic setup. | Use the owning escalation procedure; emergency direction precedes ordinary troubleshooting. No unsupported public response-time SLA is invented. |
| S2 | Immediately present the current blocking state plus one evidence-backed repair/recheck or removal/recovery option. Do not mark completion while blocked. | Escalate only where the issue class/procedure requires it or safe self-service is unavailable. |
| S3 | Present the limitation before continuation, preserve the non-green protection state, and show the bounded workaround/recovery/help path. | Exceptional escalation only when required by risk/authority. |
| S4 | Provide current source-backed explanation/help with no unnecessary support-case creation. | None by default. |

Additional requirements:

- every support interaction must expose the next safe action or explicit unsupported endpoint; no dead-end success screen;
- if service health can be checked automatically, return that fact before asking the parent to troubleshoot the device;
- repeated equivalent retries without changed evidence are prohibited;
- public/human response-time promises require a separately approved operating model and capacity evidence.

## 13. Deletion, removal and recovery requirements

### Product journey state

- J0 reset/exit clears current session state immediately.
- J1 completion/reset/exit follows TSK-0229 early deletion; if asynchronous cleanup is required, complete within the current maximum 15-minute bound.
- J1 hard expiry remains <=24 hours and non-sliding.
- support cannot resurrect deleted/expired journey state through identity/linkage.

### Exceptional diagnostics

- deletion follows the dedicated diagnostic procedure, not J1 retention;
- closure requires recorded deletion verification;
- deletion failure is itself an incident.

### Device DNS removal/recovery

Android:

1. leave the UseSafeWeb custom Private DNS provider hostname;
2. restore normal platform DNS policy, normally `Automatic` unless the parent independently chooses another setting;
3. verify ordinary DNS/internet recovery with neutral/synthetic checks;
4. set UseSafeWeb DNS state to `Removed` and withdraw protection claim.

iPhone:

1. identify/remove the exact UseSafeWeb DNS profile through the current supported profile-management path;
2. verify ordinary DNS/internet recovery with neutral/synthetic checks;
3. set UseSafeWeb DNS state to `Removed` and withdraw protection claim.

A removal/recovery failure is S2 and must not be hidden behind a completion state.

## 14. Support-burden metrics — privacy-minimal definitions only

`RSK-0002` means there are currently no representative-parent support-burden results. TSK-0042 therefore defines **what later evidence must measure**, not current performance values.

Where the applicable measurement/research gate permits collection, aggregate the minimum fields needed for these metrics:

| Metric | Definition / purpose | Privacy rule |
| --- | --- | --- |
| Issue incidence | Support issues by controlled category/severity divided by the applicable started/completed-journey denominator | Aggregate counts; no domains or persistent user profile. |
| Self-service resolution rate | Issues resolved without human intervention / eligible ordinary issues | No identity needed. |
| Human-assistance incidence | Journeys requiring human intervention / eligible journeys | Only when real-user research/operation is authorized. |
| Active assistance minutes | Active human intervention time by issue category/stage | Structured duration only; no transcript needed. |
| Blocking issue rate | S2 issues / applicable journeys | Aggregate by platform/support category. |
| Unsupported/conflict rate | S4/S5 unsupported/conflict outcomes / applicable journeys | Coarse device/network class only. |
| False-positive incidence | Confirmed UseSafeWeb-caused false positives / applicable activated journeys | Do not store the affected child's browsing history or domain list as metric data. |
| Removal-for-friction/compatibility rate | Removals where the controlled reason is friction/compatibility / applicable activated journeys | Controlled reason code only. |
| Recovery success rate | Removal/recovery cases that restore ordinary DNS behavior / removal/recovery cases | Synthetic/neutral verification result only. |
| Exceptional-diagnostic invocation rate | Approved exceptional diagnostic cases / support cases | Record count/category; raw diagnostics stay separate and temporary. |
| Privacy/security escalation count | Non-identifying count by broad incident category | No sensitive incident payload in analytics. |
| Safeguarding route count | Non-identifying count that safeguarding boundary was invoked | Never store disclosure content in product metrics. |
| Repeated defect cluster | Repeated issue category tied to one owned product/instruction/root cause | Cluster by controlled code/version, not identity. |
| Stale-guidance incidents | Support cases caused by outdated platform/service instruction | Track source/version needing review. |

### Interpretation rules

- Synthetic rehearsals may prove taxonomy, routing, instrumentation logic and recovery mechanics; they cannot prove real support burden.
- Current Experiment-1 assistance thresholds remain future behavioral decision evidence only while L3 is deferred.
- A repeated issue cluster must create owned product/content/automation improvement work rather than normalizing ongoing human intervention.
- Metrics may not become a covert per-family behavioral profile.

## 15. Source ownership and staleness

Support instructions must identify the owning source/version and be reviewable when any of these change:

- supported OS/device family/version;
- Apple/Google platform settings;
- DNS endpoint/profile/transport;
- TLS/service topology;
- filtering baseline/exception mechanism;
- VPN/Private Relay/browser/app resolver behavior;
- accountless data contract;
- privacy/security/safeguarding procedure;
- direct evidence contradicts a current support claim.

If current source/evidence cannot confirm the route, stop presenting it as current and use `Status uncertain` or `Not covered` until reviewed.

## 16. Testable acceptance assertions

A later prototype/implementation/QA suite must be able to prove at least the following:

1. Ordinary support completes without a UseSafeWeb account/login.
2. No password/account-recovery path is required in the active baseline.
3. J0 loss/reset routes safely to restart rather than identity reconstruction.
4. J1, if used, obeys <=24h non-sliding TTL and current early-deletion rules.
5. Deleted/expired J1 cannot be recovered through IP/cookie/fingerprint/account linkage.
6. Android and iPhone support use their currently approved platform-specific DNS mechanisms.
7. Configuration presence alone never yields `Verified`.
8. DNS/service/local-setup failure classes are distinguishable.
9. S2 blocking issues cannot be marked complete while unresolved.
10. Unsupported/conflicting paths end truthfully as action-needed/not-covered/uncertain rather than an invented workaround.
11. False-positive remediation first establishes causality with low-data/synthetic evidence where possible.
12. One false positive cannot disable the whole filtering baseline.
13. A narrow exception is regression-tested and reversible.
14. No persistent per-user allowlist/dashboard is introduced under EXC-0001.
15. Routine diagnostics do not require browsing/query history.
16. Exceptional diagnostics cannot begin without the required necessity/scope/time/access/approval/deletion record.
17. Exceptional diagnostic data is deleted and deletion verified before closure.
18. Privacy/security deviations remain open/escalated even if the immediate technical symptom is fixed.
19. Safeguarding disclosures are routed out of ordinary product troubleshooting.
20. S1–S4 response behavior is deterministic without fabricating a public human SLA.
21. Android removal restores normal DNS policy and withdraws UseSafeWeb protection state.
22. iPhone profile removal restores normal DNS behavior and withdraws UseSafeWeb protection state.
23. Removal/recovery failure remains blocking rather than successful.
24. Support-burden metrics use controlled aggregate fields and exclude browsing/domain history and persistent family profiles.
25. Repeated support clusters create an owned improvement signal.
26. Stale source/version evidence withdraws current instruction rather than preserving stale guidance.
27. Account/dashboard/auth requirements remain excluded unless EXC-0001 is legitimately activated.

## 17. Current evidence/source index

- `Plans/Master/Registers/DECISIONS_TRIGGERS.md` — DEC-0042 accountless-first and related product authority.
- `Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md` — EXC-0001 account/dashboard and EXC-0008 staffed-support boundaries.
- `TSK_0041_BASELINE_DNS_PROTECTION_ACTIVATION_REQUIREMENTS_2026-08-28.md` — current DNS activation, filtering, failure, conflict, false-positive and removal requirements.
- `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md` — J0/J1 state, expiry, deletion and no-linkage contract.
- `TSK_0409_SUPPORTED_OS_DEVICE_NETWORK_LIMIT_MATRIX_2026-08-28.md` — current supported/unsupported/conflict matrix.
- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` — protection-state truth semantics.
- `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md` — issue taxonomy, severity, privacy-safe support/false-positive principles.
- `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md` — bounded exceptional diagnostics and deletion verification.
- `CHILD_SAFETY_ESCALATION_PROCEDURE.md` — safeguarding boundary and official escalation ownership.
- `TSK_0511_SUPPORTED_DEVICE_VERIFICATION_COMPLETION_EVIDENCE_2026-08-28.md` — accepted supported phone-family verification.
- `TSK_0514_EXTERNAL_ENDPOINT_COMPLETION_EVIDENCE_2026-08-28.md` — external-network and removal/recovery evidence.
- `TSK_0512_FILTER_REGRESSION_EVIDENCE_2026-08-28.md` — blocked/allowed/narrow-exception/rollback filtering evidence.
- `TSK_0207_PRIVACY_PERSISTENCE_EVIDENCE_2026-08-28.md` — no persistent query/client-history evidence.

## 18. ACC-0042 result

ACC-0042 requires accountless setup/journey-state recovery, device-configuration lifecycle, AdGuard/DNS integration, false-positive and unsupported-state incidents, remedies, escalation, data-minimising diagnostics, response expectations, deletion/removal/recovery, support-burden metrics and continued exclusion of account-access requirements unless EXC-0001 is activated.

Sections 2–15 define every required domain. Sections 16–17 make the contract independently testable and traceable to current authority/evidence. No account/auth/dashboard or routine staffed-support assumption is introduced, and missing representative-parent evidence remains explicitly unresolved.

**TSK-0042 result: PASS candidate subject to independent verification, GitHub read-back and authoritative runtime reconciliation.**
