# TSK-0315 — Accountless service blueprint verification evidence

**Task:** TSK-0315 — Create the accountless end-to-end service blueprint from discovery through recovery/removal  
**Acceptance:** ACC-0315  
**Verification:** VER-0315 independent guarded artifact/authority audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Blueprint artifact: `TSK_0315_ACCOUNTLESS_END_TO_END_SERVICE_BLUEPRINT_2026-08-28.md`
- Blueprint blob: `f428f346d6e994d093b651d7b934e8610498c350`
- Blueprint commit: `9dc5be3d6e669b644a2459ebdf569cb7a6756568`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Requirements register blob: `12c3bf6a227ad6ae61e167546a2b8a35d01321d1`
- Constraints register blob: `125c10fba67cf4448d9b14ef268327c298e568cb`
- Interfaces register blob: `b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c`
- Layer-5 execution/evidence rules blob: `a3586d011b6bb48d7f6119f58429cfdde99e34c2`
- TSK-0229 accountless journey data contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- TSK-0408 DNS identity/platform mechanism contract blob: `52860ce167fc8a31962cd412772e428d280c8184`
- Current WBS hard predecessors: `TSK-0149 = PASS`, `TSK-0229 = PASS`.

## Authority/precondition audit

- WBS classifies TSK-0315 as L4 / A3 / AUTO_ALLOWED / HIGH.
- Hard dependencies are TSK-0149 and TSK-0229; both are current PASS in canonical task state.
- ACC-0315 does not require representative-parent, cohort, behavioral-metric or usability evidence. It can be satisfied as bounded internal service design under DEC-0050/CR-0003.
- `RSK-0002` remains OPEN. The blueprint explicitly states that representative-parent completion, comprehension, incremental value, support burden, persistence, perceived duplication and optimal ordering/wording are not proven.
- The blueprint does not authorize implementation, LG-05/LG-06, L5/L6, participants, legal completion, payment, public release or launch.

## Requirement/constraint/interface audit

### REQ-0028 — interaction necessity

PASS. The artifact contains an explicit interaction necessity ledger covering Start, locale, device family, coarse version/support band, phone state, native safeguard action/confirmation, DNS setup, DNS verification, external-service action, Protection Map review, Finish, Help, Reset/Remove, and the deliberately absent account/login/payment steps. Each retained interaction has a routing/technical/safety/evidence/recovery rationale or is explicitly conditional/removable.

### REQ-0029 — technically correct platform-specific configuration

PASS for this blueprint's level of authority. The blueprint consumes the accepted TSK-0408 contract and keeps Android native Private DNS as DoT hostname `dns.usesafeweb.com`, Apple DoH as the approved profile/HTTPS Server URL, and unsupported/conflict states explicit. It does not fabricate a universal platform setup mechanism. Full supported-combination coverage remains correctly owned by TSK-0409.

### CON-0010 — accountless baseline

PASS. No mandatory account, login, parent/child identity, email, phone, stable device/customer ID or dashboard history is introduced. J0 session state is preferred; any J1 use remains conditional on TSK-0229 necessity/expiry/deletion/no-linkage rules.

### CON-0017 — multilingual availability versus market authority

PASS. The blueprint preserves eventual English/Turkish/Arabic/RTL capability while explicitly refusing to equate technical language availability with official non-UK localization/support/legal/channel readiness.

### INT-0009 / INT-0010

PASS for the current TSK-0315 contribution, with a mandatory limitation. The artifact provides exact service stages, states, failure/recovery boundaries, privacy rules and owner-only exceptions that later implementation/QA contracts can consume. It explicitly does **not** claim that the interface's broader “validated experience specification” or real-usability/comprehension expectations are satisfied while L3 is deferred and `RSK-0002` remains open.

## ACC-0315 clause audit

ACC-0315 requires the blueprint to identify parent actions, system actions, evidence states, dependencies, failures, automated support, privacy, and owner-only exceptions.

### Parent actions — PASS

The stage table explicitly covers public discovery, understand/trust, start, minimal routing, native safeguard, Android/iPhone DNS setup, DNS verification, external-service safeguard, Protection Map review, completion, contextual help, reset/reconfigure, DNS removal, post-removal recovery and exit.

### System actions — PASS

Every stage defines the system responsibility separately from the parent action: render/route, initialize transient state, present only approved platform instructions, execute synthetic verification, synthesize evidence states, delete transient state, provide point-of-need recovery and withdraw protection claims after removal.

### Evidence states — PASS

The blueprint defines provisional evidence classes and preserves the key truth boundary: `system verified` is distinct from `parent confirmed`; configured-but-unverified, action-needed, unsupported/not-covered, uncertain/error and removed are represented. Final UI labels/copy remain correctly owned by TSK-0320.

### Dependencies — PASS

The blueprint names TSK-0143, TSK-0144, TSK-0320 and TSK-0409 as unfinished owning boundaries and explicitly states that their slots do not make those tasks PASS. It consumes current accepted TSK-0229 and TSK-0408 without fabricating unfinished native-service/state-matrix detail.

### Failure/recovery — PASS

Unsupported devices, installation/configuration failures, certificate/reachability issues, VPN/browser/app/network conflict, verification uncertainty, stale instructions, profile-removal/reset, unrelated post-removal network failure and exceptional incident paths are represented. Safe recovery consistently removes/withdraws the UseSafeWeb DNS protection claim rather than silently failing over to an unverified protected state.

### Automated support — PASS

Routine support is point-of-need, state-specific, configuration/synthetic-check first, retry only when useful, and reset/remove capable. Exceptional escalation is limited to security/privacy/legal/safeguarding, material infrastructure/certificate, managed-device authority, contradictory platform behavior or unknown failure requiring broader diagnostics.

### Privacy — PASS

The blueprint is J0-first and J1-conditional, prohibits browsing/DNS/domain history, stable identity/profile/linkage, service credentials, payment identity, behavioral tracking and persistent support/analytics profiles, and carries TSK-0229 deletion semantics through completion/reset/exit.

### Owner-only / governed exceptions — PASS

Persistent account/dashboard scope, broader data/retention, frozen backend direction, public-production promotion, unsupported-platform support declarations, legal/privacy/safeguarding risk decisions, material claims, participant activation, payment, LG-05/LG-06/build/public release/launch are fenced from autonomous UX execution.

## Adversarial findings and unresolved uncertainty

1. **No behavioral validation:** the sequence may still be too long, confusing or duplicative; no representative parent has validated it. This remains `RSK-0002`, not a hidden assumption.
2. **Native phone safeguard detail is intentionally incomplete:** TSK-0143 has not yet frozen platform routing. The blueprint treats it as a contract slot and parent-confirmed/unsupported boundary rather than inventing instructions.
3. **External service detail is intentionally incomplete:** TSK-0144 has not yet frozen the one relevant service step. `Not covered/none applicable` remains valid.
4. **Protection Map labels are provisional:** TSK-0320 still owns exact evidence/transition/copy rules. TSK-0315 defines only the service evidence distinction needed for the blueprint.
5. **Supported network/bypass coverage is incomplete:** TSK-0409 still owns the OS/device/network matrix; TSK-0315 does not promote controlled-pilot Android/iPhone evidence into universal support.
6. **INT-0009's name contains “Validated experience specification”:** current CR-0003 authority prevents this blueprint from satisfying any real-user-validation meaning of that interface. The artifact records the limitation instead of overstating PASS.

No current evidence requires a mandatory account, persistent child profile, browsing/query history or a universal cross-platform DNS setup workflow. No acceptance clause requires those capabilities.

## Stable verification decision

The durable blueprint directly covers every ACC-0315 clause, respects its current requirements/constraints/interfaces, explicitly preserves unfinished downstream ownership, and carries the mandatory CR-0003/`RSK-0002` evidence limitation.

**Stable outcome: TSK-0315 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the current L4 queue. Likely newly unlocked tasks include TSK-0316 and TSK-0320, but neither is to be assumed selected until priority, authority, acceptance, current dependencies and CR-0003 are rechecked against the durable queue.
