# TSK-0320 — Current Protection-State Model and Copy Rules

**Task:** TSK-0320 — Freeze the protection-state model and copy rules  
**Acceptance:** ACC-0320 / VER-0320 / EVD-0320  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 2.0.0-post-CR-0008  
**Date:** 2026-09-01  
**Status:** CURRENT FROZEN L4 STATE/COPY CONTRACT; implementation and downstream PASS are not inferred  
**Authority:** current owner-frozen modular Master Planning System; DEC-0053/CR-0006 dual-mode Version-1 scope; DEC-0054/CR-0007 autonomy/production lifecycle; DEC-0055/CR-0008 proportional-evidence/action-authority normalization; current TSK-0315 service blueprint; current accountless/persistent-state separation; current DNS verification/topology contracts.  

## 1. Non-negotiable truth rule

The Protection Map is an **evidence map, not a safety score**. A state is selected only from current evidence for the declared device/layer/path/scope.

**Configuration presence, journey completion, parent confirmation, account ownership, dashboard/device registration, stored device metadata, or a previous successful check are never technical protection verification.** They may prove setup or ownership only. `protected/verified` requires its own current qualifying technical evidence.

No state may imply complete safety, universal enforcement, browsing surveillance, or protection beyond the scope/time actually evidenced.

## 2. Evidence model

The state evaluator consumes evidence records, not UI optimism. Evidence is scoped and ordered by observation/event time.

### E1 — Technical verification evidence
Required fields: mechanism/verifier ID and version, result (`positive`, `negative`, `indeterminate`), device/layer/path scope, observed time, freshness rule or validity boundary, provenance/evidence reference, and any material limitation.

A **qualifying positive E1** is the only evidence class that can establish `protected/verified`. It must be produced by an approved verifier for the exact supported mechanism and scope, be current under that verifier's freshness policy, and have no newer/equally authoritative material contradiction.

### E2 — Configuration / parent-confirmation evidence
Required fields: source (`parent`, installer, approved configuration/control plane), target/scope, action/confirmation, observed time, and provenance reference.

E2 proves setup/configuration only. It has an invariant property: **`qualifies_as_technical_verification = false`**. Account ownership and persistent device registration are E2/context, not E1.

### E3 — Coverage determination
Required fields: result (`covered`, `not-covered`), reason, scope, authoritative source/version, evaluated time.

### E4 — Action condition
Required fields: concrete required action, reason, source/evidence, detected time, affected scope.

### E5 — Removal/revocation event
Required fields: operation (`remove`, `uninstall`, `revoke`, `unlink`, `reset`, `delete configuration`), target/scope, completion/confirmation source, event time, provenance.

### E6 — Verification uncertainty/error
Required fields: condition (`stale`, `missing`, `conflict`, `timeout`, `unreachable`, `verifier-error`, `bypass-uncertain`, `context-changed`), source, time, affected scope, retry/recovery route where known.

Evidence records and state metadata must contain no browsing/query/activity history, raw DNS history, secrets, tokens, or unnecessary child data.

## 3. Canonical six states

### S1 — `protected/verified`
**Entry evidence:** fresh qualifying positive E1 for the exact declared scope, with no current material contradiction and no later removal/out-of-scope event.

**Meaning:** UseSafeWeb has current technical evidence that the specified protection mechanism is active for the stated scope.

**Primary copy:** `Protection verified`

**Supporting copy:** `UseSafeWeb verified this protection step for this setup.` When useful, show verification time/scope. Material path limits must remain visible.

**Never say:** `Fully protected`, `Safe`, `Everything is blocked`, `Your child is protected`, or any universal/continuous assurance not directly proven.

**Durability:** S1 is not permanent. When the owning verifier's freshness boundary expires or the evidence context materially changes, S1 must be re-evaluated; stale verification cannot remain a current protection claim.

### S2 — `configured/parent-confirmed`
**Entry evidence:** current E2 proves setup/configuration/parent confirmation and there is no qualifying current positive E1. No unresolved material contradiction may be hidden by S2.

**Meaning:** setup is confirmed, but technical protection has not been independently verified.

**Primary copy:** `Setup confirmed`

**Mandatory supporting copy:** `Protection has not yet been technically verified.`

**Never say:** `Verified`, `Protected`, `Confirmed by UseSafeWeb`, `Protection active`, or equivalent assurance.

Optional account/device ownership may persist S2-compatible setup context, but ownership or stored status can never promote S2 to S1.

### S3 — `action-needed`
**Entry evidence:** the layer/path is covered/applicable and current reliable evidence identifies a concrete, safe, solvable action required to establish or restore the intended protection. Examples include incomplete required setup, a reliable negative technical check with known remediation, or a changed configuration requiring reconfiguration/reverification.

**Primary copy:** `Action needed`

**Supporting copy:** state the concrete next action and consequence, e.g. `Update this setting, then verify again.` Do not imply protection is active while action remains required.

### S4 — `not-covered`
**Entry evidence:** current authoritative E3 says the exact capability/device/path is unsupported, out of approved scope, or has no approved applicable safeguard.

**Primary copy:** `Not covered`

**Supporting copy:** state the scope reason, e.g. `UseSafeWeb does not cover this on your current setup.`

Do not convert a failed supported setup into S4 merely to avoid showing an error, and do not imply another layer compensates unless separately proven.

### S5 — `uncertain/error`
**Entry evidence:** trustworthy classification cannot currently be made because relevant evidence is missing/stale, materially conflicting, verification is unavailable/timed out/errored, a bypass/context change cannot be resolved, or the current technical path is otherwise indeterminate.

**Primary copy:** `Protection status could not be verified`

**Supporting copy:** give a bounded retry/troubleshooting route, e.g. `Retry verification or follow the troubleshooting steps before relying on this protection.`

S5 is fail-closed for claims: prior S1/S2 may not remain visible as a current positive assurance when current evidence is materially uncertain.

### S6 — `removed`
**Entry evidence:** current E5 establishes completed/confirmed removal, revoke, unlink, uninstall, reset, or equivalent de-enrolment for the relevant configuration/layer, and no later explicit reconfiguration/enrolment supersedes it.

**Primary copy:** `Removed`

**Supporting copy:** `This setup is no longer enrolled through UseSafeWeb.` For DNS-specific removal, state that UseSafeWeb DNS is no longer configured/claimed active on that device.

A removal state contains no protection assurance. A later account/device record alone does not undo S6.

## 4. Deterministic state selection and precedence

Evaluate evidence chronologically and by scope. Newer explicit evidence supersedes older evidence only for the same relevant scope; material conflicts that cannot be safely resolved yield S5.

1. If the latest applicable explicit event is E5 removal/revocation and no later explicit new setup/enrolment supersedes it → **S6**.
2. If current authoritative E3 says the scope is not covered → **S4**.
3. If evidence is materially conflicting, stale beyond its verifier policy, unavailable, or indeterminate such that a truthful current classification cannot be made → **S5**.
4. If a fresh qualifying positive E1 exists with no current contradiction → **S1**.
5. If reliable current evidence identifies a concrete required remediation/action → **S3**.
6. If current E2 proves setup/configuration/parent confirmation but no qualifying positive E1 exists → **S2**.
7. If the layer is applicable but has not been completed and a next setup action is known → **S3**; otherwise insufficient trustworthy evidence → **S5**.

The evaluator may retain underlying evidence facts separately from the one user-visible state. For example, a configuration can still exist while the displayed state is S3 or S5. The UI must not collapse that underlying fact into a positive protection claim.

## 5. Transition contract

### Universal guards

- **Any state → S1:** permitted **only** after new/current qualifying positive E1. No E2/account/device/configuration event can perform this transition.
- **Any non-S6 state → S6:** on completed/confirmed current E5 removal/revocation for that scope.
- **Any state → S4:** when a current authoritative coverage decision makes that exact scope unsupported/not covered.
- **Any positive state → S5:** when its required evidence becomes stale, conflicting, unavailable, or materially indeterminate.

### From S1 `protected/verified`
- → S1 on fresh successful re-verification.
- → S3 on reliable negative evidence with a known safe remedy.
- → S5 when verification expires, conflicts, becomes unavailable, or context changes so the prior result can no longer prove current protection.
- → S4 on authoritative current out-of-scope determination.
- → S6 on completed removal/revocation.
- **Never → S2 merely because verification aged out** if current status is actually indeterminate; use S5 unless reliable current E2 plus resolved/non-conflicting evidence justifies S2.

### From S2 `configured/parent-confirmed`
- → S1 only on qualifying positive E1.
- → S3 on reliable evidence that a concrete corrective action is required.
- → S5 on contradiction/indeterminate verification or unresolved context.
- → S4 on authoritative not-covered determination.
- → S6 on completed removal/revocation.

### From S3 `action-needed`
- → S2 after remediation/setup is confirmed but technical verification is not yet available/successful.
- → S1 if remediation is followed by qualifying positive E1.
- → S5 if remediation result is ambiguous or verifier fails/inconclusive.
- → S4 if authoritative coverage changes to not-covered.
- → S6 on completed removal/revocation.

### From S4 `not-covered`
- remains S4 while authoritative coverage is unchanged.
- → S2 when coverage becomes supported and explicit setup/configuration is then confirmed but not technically verified.
- → S3 when coverage becomes supported and a required setup/remediation action is known.
- → S5 when coverage becomes potentially applicable but the actual state cannot yet be determined.
- → S1 only if coverage is supported **and** qualifying positive E1 exists for the exact scope.
- → S6 only when an applicable previously configured artefact is explicitly removed; do not invent removal for a never-configured unsupported path.

### From S5 `uncertain/error`
- → S1 only on new qualifying positive E1.
- → S2 only when uncertainty/conflict is resolved and reliable current E2 remains without qualifying E1.
- → S3 when reliable evidence resolves uncertainty into a concrete required action.
- → S4 when authoritative coverage proves not-covered.
- → S6 on completed removal/revocation.

### From S6 `removed`
- remains S6 until a later explicit setup/enrolment/configuration event exists.
- → S2 after a later explicit new setup/enrolment/configuration is confirmed and no qualifying positive E1 exists.
- → S3 when a new setup attempt begins but remains incomplete or needs remediation.
- → S5 when a new attempt exists but its resulting state is indeterminate.
- → S4 if the newly evaluated scope is not covered.
- → S1 only when a later new setup is accompanied/followed by qualifying positive E1. If both pieces arrive in one atomic evaluation, direct display of S1 is allowed only when provenance retains the new setup plus independent technical verification; removal history alone is never overwritten by inference.

## 6. DNS and platform truth rules

For UseSafeWeb DNS, profile/provider presence, ClientID existence, endpoint health, successful provisioning, account/device ownership, and parent confirmation are not sufficient for S1. S1 requires the approved technical verifier to demonstrate the intended supported device/path behavior. VPN, Private Relay, browser/app secure DNS, network changes, provider conflicts, timeout, or inability to establish the intended resolver path must yield S5 or S3 according to whether a trustworthy concrete remedy is known.

Native-device or external-service safeguards default to S2 after explicit confirmation unless their owning capability later establishes an approved independent verifier. Unsupported variants use S4; known incomplete supported setup uses S3; ambiguous/conflicting status uses S5.

## 7. Accountless and optional-account persistence

- Accountless journey state and optional persistent parent/device ownership state are separate domains.
- Optional account identity/device ownership authorizes and helps persist approved device-management context only. It is **not protection evidence**.
- Persistent records may retain the selected state metadata only where separately authorized by the data model, but the state must be recomputed from current evidence and freshness rules before being presented as current.
- An old stored `protected/verified` value is not itself E1 and cannot restore S1 after sign-in, resume, reinstall, replacement, or account return.
- No browsing/query/activity history is stored to support any Protection Map state.

Minimum state metadata where persistence is authorized: state ID, reason code, declared scope, evidence references/provenance, evaluated time, verifier/copy version, and freshness/expiry boundary where applicable. Store references/minimal facts, not raw DNS history or secrets.

## 8. Canonical reason codes

At minimum implementations must support semantically equivalent reason codes for:

- `TECH_VERIFIED`
- `CONFIG_CONFIRMED_NO_TECH_VERIFY`
- `TECH_VERIFY_NEGATIVE`
- `REMEDIATION_REQUIRED`
- `OUT_OF_SCOPE`
- `UNSUPPORTED_PATH`
- `VERIFY_STALE`
- `VERIFY_TIMEOUT`
- `VERIFY_UNREACHABLE`
- `VERIFICATION_SERVICE_ERROR`
- `EVIDENCE_CONFLICT`
- `BYPASS_OR_CONTEXT_UNCERTAIN`
- `REMOVED_BY_PARENT`
- `REVOKED`
- `REINSTALLED_AWAITING_VERIFY`

Reason codes are evidence descriptors, not user-facing claims.

## 9. Copy grammar and claim controls

1. Use `verified`/`protection verified` only for S1 and only within the evidenced scope.
2. S2 must explicitly say setup is confirmed **and** protection has not been technically verified.
3. S3 names the required action; it must not use a positive protection badge as its primary state.
4. S4 names the missing scope/coverage honestly; unsupported is not failure and is not cosmetically converted to success.
5. S5 states uncertainty prominently; no success icon/copy may visually override it.
6. S6 states removal consequence; do not retain stale positive status.
7. Journey completion is not protection verification. Preferred completion copy: `Setup complete. Review what UseSafeWeb verified, what you confirmed, what needs action, and what is not covered.`
8. Never use complete-safety promises or language implying UseSafeWeb monitors browsing, messages, location, contacts, photos, social content, or child activity.
9. Translations must preserve evidence strength, uncertainty, scope, and actor. A translated phrase may not strengthen S2 into S1 or imply market activation.
10. UI styling must visibly distinguish S1 from S2; an all-green/equivalent treatment must not make parent confirmation look system-verified.

## 10. Reverification triggers

Re-evaluate an existing state whenever its owning evidence policy requires it, including applicable device/platform mechanism change, reinstall/replacement/removal, VPN/Private Relay/browser/app secure-DNS change, network/environment change relevant to the supported matrix, endpoint/certificate/service/configuration change, verifier failure/contradiction, or evidence freshness expiry.

No universal fabricated TTL is introduced here. Each approved verifier defines its own freshness boundary; absent current qualifying evidence, S1 must be withdrawn to the truthful successor state.

## 11. Required deterministic assertions

A compliant implementation/test suite must prove at least:

1. Parent confirmation alone never yields S1.
2. Configuration/profile/provider/ClientID presence alone never yields S1.
3. Account ownership or dashboard/device registration alone never yields S1.
4. Only fresh qualifying positive E1 can enter S1.
5. A stale positive verification cannot remain S1.
6. Materially conflicting/inconclusive evidence yields S5 unless a stronger current authoritative fact deterministically selects S4/S6.
7. A reliable failed supported setup with a known remedy yields S3, not S4.
8. Unsupported/out-of-scope combinations yield S4 and expose no fake completion state.
9. Completed removal/revocation withdraws any protection claim and yields S6 for that scope.
10. S6 cannot return to S1 from account/device persistence or parent confirmation; new setup plus qualifying E1 is required.
11. A completed journey may contain any mixture of S1–S6 consistent with evidence.
12. S2 copy never contains an unqualified `verified`/`protected` assurance.
13. S1 scope/time limitations remain visible where material; S1 never means complete safety.
14. DNS verification requires no browsing/query/activity history.
15. Anonymous journey state and optional account/device state remain separate; sign-in/resume does not promote evidence strength.
16. Every persisted/displayed state is traceable to evidence refs, reason, evaluation time, scope and copy/verifier version where applicable.
17. Removal, account deletion/device-record deletion, and physical DNS configuration removal remain distinct operations and are represented truthfully.
18. Translated/localized copy cannot strengthen the evidence claim.

## 12. Governance and non-inference

This contract freezes state/evidence/copy semantics only. It does not invent a verifier, support a new platform, approve a datastore/schema, prove implementation, prove legal/privacy compliance, prove real-user comprehension, activate production users, or pass a downstream gate/task. Later implementations must consume this contract without weakening its evidence separation.

The historical 2026-08-28 TSK-0320 contract remains evidence of the earlier accountless/provisional design but is superseded for current task acceptance where CR-0006/CR-0007/CR-0008 and the current dual-mode service blueprint changed the operating context.

## 13. ACC-0320 disposition

`ACC-0320` requires exact evidence and transition rules for `protected/verified`, `configured/parent-confirmed`, `action-needed`, `not-covered`, `uncertain/error`, and `removed`, with no confirmation masquerading as verification.

This version defines the six states; qualifying evidence classes; deterministic precedence; all-state transition guards; accountless/optional-account separation; DNS/platform truth rules; persistence/freshness rules; exact copy controls; reason codes; reverification triggers; and deterministic assertions.

**TSK-0320 result: PASS candidate pending independent verification, GitHub read-back, master-plan validation, and durable runtime reconciliation.**
