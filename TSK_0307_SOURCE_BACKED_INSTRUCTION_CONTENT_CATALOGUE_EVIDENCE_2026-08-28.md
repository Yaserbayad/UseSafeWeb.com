# TSK-0307 — Source-Backed Instruction Catalogue Verification Evidence

**Task:** `TSK-0307 — Create the source-backed instruction/content catalogue with applicability and review triggers`  
**Acceptance:** `ACC-0307`  
**Verification:** `VER-0307`  
**Evidence:** `EVD-0307`  
**Date:** 2026-08-28  
**Disposition:** **PASS candidate for runtime reconciliation**

## Exact evidence set

- Catalogue `TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md`, publication commit `c8c0fa314701190a0b5ade9b8e48d6cf6b19ce36`, read-back blob `d717c9b3f66197abe1f3e73361633f222b817e7c`.
- Approved predecessor TSK-0317 candidate blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d` and current runtime TSK-0317 PASS.
- TSK-0408 DNS identity/platform contract blob `52860ce167fc8a31962cd412772e428d280c8184`.
- Current accepted TSK-0409 support matrix, TSK-0320 protection-state contract, TSK-0511 supported-device evidence, TSK-0514 removal/recovery evidence and TSK-0207 privacy-persistence evidence.
- First-party Android/Apple source set was already rechecked and accepted on 2026-08-28 by TSK-0408/TSK-0409; no contradictory newer project evidence exists in current authority.

## Dependency and authority check

- Sole hard dependency TSK-0317: **PASS**.
- WBS action authority: A3 / `AUTO_ALLOWED`.
- Scope: bounded internal provisional L4 content/instruction definition only under DEC-0050/CR-0003.
- No account/persistence, participant, legal-completion, production/publication or L5/L6 authority is consumed or inferred.

## ACC-0307 field-by-field verification

ACC-0307 requires: **Each instruction has official source, platform/version/region, owner, last verification, review trigger, localized variants, known limits, and test reference.**

The catalogue contains nine current instruction classes. Every class was checked against every required field:

| Required field | Result | Verification |
| --- | --- | --- |
| Official/current source | **PASS** | Each registry row binds to current first-party Android/Apple documentation and/or authoritative current UseSafeWeb contracts/evidence appropriate to the instruction. |
| Platform/version | **PASS** | Android entries are bounded to Android phone 9+ with usable native Private DNS; iPhone entries to iOS 14+ approved manual profile path; common states have explicit applicability. |
| Region/locale | **PASS** | Each row declares mechanism/locale applicability without implying market activation; en-GB baseline and provisional tr-TR/ar variants are separated from market scope. |
| Owner | **PASS** | UX/Content, Product/UX and/or Network Engineering ownership is explicit per row. |
| Last verification | **PASS** | Every v1 entry records 2026-08-28. |
| Review trigger | **PASS** | Every row contains source/platform/endpoint/profile/support/conflict/recovery triggers, supplemented by a catalogue-wide trigger matrix. |
| Localized variants | **PASS** | Every instruction class has en-GB plus explicit tr-TR and ar semantic variants; tr-TR/ar are accurately labelled provisional and not native-user validated or market activation. |
| Known limits | **PASS** | Each row captures support/conflict/manual-action/profile-artifact/removal/privacy limits applicable to the instruction. |
| Test reference | **PASS** | Each row maps to current TSK-0409 assertions and/or TSK-0511, TSK-0514, TSK-0207, TSK-0317 evidence. |

## Semantic and contradiction checks

1. **Android mechanism:** PASS. Catalogue consistently uses `dns.usesafeweb.com` as the native Private DNS provider hostname and explicitly rejects an `https://` input for that setting.
2. **Apple mechanism:** PASS. Catalogue binds iPhone setup to the separately verified DoH profile mechanism and never fabricates/releases a production `.mobileconfig`.
3. **Protocol choice:** PASS. No parent-facing instruction asks the user to choose DoH versus DoT.
4. **Automatic/manual boundary:** PASS. Copy and routing may be automated, but OS setting/profile authorization remains user/OS controlled.
5. **Verification truth:** PASS. Profile/setting presence and parent confirmation do not equal `Verified`; conflict states remain uncertainty/not-covered where evidence is insufficient.
6. **Recovery truth:** PASS. Removal/reset ends the UseSafeWeb DNS protection claim; no silent plaintext fallback keeps a green state.
7. **Privacy:** PASS. No browsing/domain history, persistent identity, account or child/device profile is introduced by the instruction set.
8. **Support boundary:** PASS. Unaccepted devices/networks are stopped rather than routed through speculative alternate clients.
9. **Localization boundary:** PASS. Turkish/Arabic variants preserve the English source semantics and are explicitly provisional; no claim of native-language usability validation is made. TSK-0311 still owns final translation-file/fallback architecture.
10. **Market boundary:** PASS. Availability of a language variant is explicitly not treated as geographic activation.

## Adversarial checks

- **Could the catalogue silently expand Android support to tablets/managed devices?** No; it explicitly prohibits that extrapolation.
- **Could translated copy create a new support claim?** No; support is determined by the same TSK-0409 applicability rules in every locale.
- **Could stale platform wording remain indefinitely?** No; source/platform changes are explicit review triggers, and contradictory target evidence makes the affected entry stale.
- **Could iPhone instructions be used before an exact profile artifact is accepted?** No; the setup row and copy require a separately verified environment-specific profile artifact first.
- **Could a VPN/security control be disabled merely to obtain a positive status?** No; the common uncertainty instruction explicitly prohibits that behavior.
- **Does this prove parent comprehension or localization usability?** No; `RSK-0002` remains OPEN and provisional translations are not presented as user validation.

## Final acceptance result

All nine current instruction classes contain every ACC-0307 required metadata field and source/applicability/test binding. The content is consistent with the accepted TSK-0317/0408/0409/0320 contracts and current technical evidence, with no detected unauthorized scope expansion or false verification claim.

**ACC-0307: PASS.**  
**TSK-0307: PASS candidate pending canonical runtime reconciliation and read-back.**

This PASS would define content only; it would not authorize implementation, public profile distribution, participants, market activation, payment, publication or launch.