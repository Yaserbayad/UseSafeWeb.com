# TSK-0143 — Native-device safeguard routing verification evidence

**Task:** TSK-0143 — Specify native-device safeguard routing requirements  
**Acceptance:** ACC-0143  
**Verification:** VER-0143 independent guarded product/source audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Routing contract: `TSK_0143_NATIVE_DEVICE_SAFEGUARD_ROUTING_REQUIREMENTS_2026-08-28.md`
- Contract blob: `20b588c27bc0d71249bec2c83f33cf551afa4ff0`
- Contract commit: `d4913bc67bac9bba3e4d5e713c269e7b921326e4`
- TSK-0141 minimum scope blob: `c72bfd906fdca4a106dcd7d4ff458a2577e32c90`
- TSK-0138 assumptions/decisions blob: `d782f26d5d48b0902b044d8bbab48569bdee0ea2`
- TSK-0315 service blueprint blob: `f428f346d6e994d093b651d7b934e8610498c350`
- TSK-0316 friction contract blob: `07df8b1909809a069e3ddba1ff10b688d2f5a5e0`
- TSK-0320 protection-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- TSK-0409 support matrix blob: `09318534ec097849cbe8c7391e2a1acc3ba5a79a`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Hard dependency: `TSK-0146 = PASS` in current canonical task/runtime state.

## Authority and semantic audit

Canonical DEC-0009 freezes the user-visible shape as native safeguards first, real AdGuard baseline, one relevant service, truthful Protection Map and quiet completion. TSK-0141 MIN-05 explicitly retains a native-safeguards-first flow with already-configured/skip handling and says the incremental-value/friction hypothesis is unvalidated. TSK-0138 UPA-003 explicitly keeps the proposition “native-safeguards-first reduces duplication” UNKNOWN and requires the safe default to preserve skip/already-configured behavior while removing avoidable steps.

Therefore TSK-0143 is authorized to freeze **routing/truth/staleness requirements**, but not to claim observed user value or to invent a new UseSafeWeb parental-control system.

## Current first-party platform audit — checked 2026-08-28

### Apple

Apple UK currently documents Screen Time / Family Sharing parental controls for a child's iPhone and Content & Privacy Restrictions for web/content/app/purchase/settings controls. Apple also documents Screen Time passcode protection for chosen settings.

Sources:
- https://support.apple.com/en-gb/guide/iphone/iph00ba7d632/ios
- https://support.apple.com/en-gb/105121
- https://support.apple.com/en-gb/126533

**Disposition:** supports routing the iPhone native layer to Apple's current parental-control ecosystem. It does not supply a UseSafeWeb system verifier and does not justify hard-coding one fixed menu path indefinitely.

### Google / Android

Google currently documents Family Link supervision on Android and states most Family Link supervision tools do not work on iPhones/iPads. Current Android Help also documents an on-device parental-controls PIN path for Android 17+ where available, with an option to use Family Link.

Sources:
- https://support.google.com/android/answer/16766047
- https://support.google.com/families/answer/9116646?hl=en
- https://support.google.com/families/answer/9037996?hl=en
- https://support.google.com/families/answer/9055704?hl=en

**Disposition:** supports Android routing to current Google/Android parental-control mechanisms and directly contradicts treating Family Link as an equivalent iPhone device-supervision route.

## ACC-0143 clause audit

ACC-0143 requires: `Requirements cover supported platform states, already-configured handling, parent confirmation, unsupported paths, stale guidance, and verification limitations.`

### Supported platform states — PASS

The contract first gates native routing on the current TSK-0409 supported phone family and then defines six native route states: already-configured confirmed, needs setup, unknown, not applicable, unsupported/blocked and removed/disabled. It does not expand DNS/platform support merely because a vendor control exists.

### Already-configured handling — PASS

Already-correct safeguards are explicitly skipped rather than forced through reconfiguration. The parent is asked only for the minimum confirmation of the approved control category, no screenshot/settings dump is required by default, and contradictory evidence demotes the state to uncertainty.

### Parent confirmation — PASS

Parent completion/confirmation yields TSK-0320 S2 only. The contract explicitly prohibits `Verified`/system-confirmed wording and keeps native state independent of DNS verification.

### Unsupported paths — PASS

Unsupported device/version/account/management-policy and unresolved UI/instruction mismatch states stop the affected native branch. Clearly unsupported paths use S4; ambiguous/conflicting paths use S5. Other independent layers may continue only if their own support conditions pass; no substitute task is invented merely to make the map complete.

### Stale guidance — PASS

Every instruction is required to carry platform/mechanism, applicability, official source, source title, last-verified date, content version, expected result, fallback, owner and review trigger. Apple/Google changes, major OS changes, contradictory target evidence, unavailable/redirected guidance and new security/privacy/safeguarding concerns trigger re-review. Stale guidance is not silently reused.

### Verification limitations — PASS

The current native layer has no approved UseSafeWeb system verifier for Screen Time, Family Link or Android on-device parental controls. Positive native state is therefore parent-confirmed S2; presence of an account/app/menu is not evidence of configuration; DNS success is not evidence of native-control state.

## Cross-contract consistency audit

- **TSK-0141:** PASS. Native-first is retained but remains provisional/unvalidated and the task does not expand into a full parental-control suite.
- **TSK-0316:** PASS. Already-configured and not-applicable branches remove duplicate friction; only branch-changing inputs are retained.
- **TSK-0320:** PASS. S1/S2/S3/S4/S5/S6 evidence strength is preserved and parent confirmation never masquerades as verification.
- **TSK-0409:** PASS. Native routing is gated by current supported phone-family state and does not promote untested device families.
- **Privacy/non-surveillance:** PASS. Apple/Google credentials and broad surveillance data/features are not required or copied into UseSafeWeb state.

## Adversarial findings and unresolved uncertainty

1. **Exact native setting list is not frozen here.** The canonical product does not currently define one immutable set of Apple/Google settings. Inventing such a list in TSK-0143 would overreach the task and become stale quickly; exact versioned instructions remain owned by the instruction catalogue.
2. **Android now has more than one native-control route.** Android 17+ may expose on-device PIN controls, while Family Link remains the account-managed ecosystem. The contract therefore routes by actual applicability instead of assuming Family Link is always the sole Android path.
3. **Family Link is not equivalent on iPhone/iPad.** Google explicitly states most supervision tools do not work there. The contract prevents a cross-platform false equivalence.
4. **Apple/Google account prerequisites can create friction.** UseSafeWeb does not collect platform credentials/account data and does not claim that account setup is behaviorally acceptable. `RSK-0002`/UPA-003 remain open.
5. **No current native-control system verifier exists.** This prevents S1 and makes parent confirmation the strongest current positive native evidence.
6. **Native-first value is still unknown.** No representative-parent evidence establishes that this order reduces work; later L3 evidence must reopen affected assumptions if contradictory.

## Stable verification decision

The durable routing contract directly satisfies every ACC-0143 clause, resolves the platform family semantically from canonical product authority, uses current first-party evidence for Apple/Google mechanism applicability, and preserves all CR-0003/RSK-0002 limitations.

**Stable outcome: TSK-0143 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute current provisional-L4 eligibility. TSK-0144 is expected to become dependency-ready but must be checked against its exact current authority/acceptance before execution.
