# TSK-0317 — Platform Design Preparation Evidence

**Task:** `TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform`  
**Acceptance:** `ACC-0317`  
**Verification:** `VER-0317`  
**Evidence:** `EVD-0317`  
**Action authority:** **A1 / HUMAN_ONLY**  
**Date:** 2026-08-28  
**Disposition tested:** preparation completeness only; **NOT task PASS**.

## Exact evidence set

- Candidate: `TSK_0317_PLATFORM_INSTALL_VERIFICATION_REMOVAL_RECOVERY_DESIGN_CANDIDATE_2026-08-28.md`, publication commit `28156f75728c28333c61c33313007556839329e6`, read-back blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`.
- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `dce5b829c4d447eac180ae1e896e0019292cf971`.
- TSK-0316 friction contract: current accepted runtime PASS; source candidate artifact `TSK_0316_FRICTION_BUDGET_AND_INTERACTION_CHALLENGE_2026-08-28.md`.
- TSK-0408 DNS identity/platform contract, blob `52860ce167fc8a31962cd412772e428d280c8184`.
- TSK-0409 supported OS/device/network matrix: current accepted runtime PASS and source artifact `TSK_0409_SUPPORTED_OS_DEVICE_NETWORK_LIMIT_MATRIX_2026-08-28.md`.
- TSK-0320 protection-state/copy contract: current accepted runtime PASS.
- Runtime selection before candidate publication: TSK-0317 selected TODO for HUMAN_ONLY preparation only; all DEC-0050/CR-0003 fences retained.

## WBS/authority verification

The WBS defines TSK-0317 as L4 / HIGH / A1 / `HUMAN_ONLY`, with hard dependency `TSK-0316` and ACC-0317:

> Automatic profile/config is used only where reliable; fallbacks use canonical endpoint/profile guidance; OS asymmetry and limitations are explicit.

The dependency is satisfied in current runtime. However, `HUMAN_ONLY` is an independent completion boundary: preparation may be automated, but the human design disposition cannot be performed or inferred by AI.

## Preparation checks

| Check | Result | Evidence |
| --- | --- | --- |
| Hard dependency TSK-0316 satisfied | **PASS** | Current runtime records TSK-0316 accepted PASS. |
| Supported-platform scope bounded | **PASS** | Candidate limits current supported design to Android 9+ phones with usable native Private DNS and iPhone/iOS 14+ approved manual profile path; it does not generalise to unaccepted families/managed combinations. |
| Android endpoint semantics correct | **PASS** | Candidate uses hostname `dns.usesafeweb.com`, not the DoH URL or `:853` in normal user input, matching TSK-0408/0409. |
| Apple endpoint/profile semantics correct | **PASS** | Candidate uses the approved DoH Server URL/profile mechanism and explicitly refuses to fabricate/release an unverified `.mobileconfig`. |
| Automatic-versus-manual boundary explicit | **PASS** | Routing/copy/verified artifact delivery/neutral verification may be automated where reliable; Android system setting changes and Apple profile authorization/removal remain user/OS controlled. |
| No false one-click claim | **PASS** | Candidate explicitly prohibits silent system-DNS/profile installation claims and misleading one-click/full-protection language. |
| Canonical fallback preserved | **PASS** | Candidate defines fallback as approved manual platform guidance or safe removal/recovery, not an improvised resolver/client or silent plaintext fallback. |
| Verification truth preserved | **PASS** | Configuration presence/parent confirmation never equals Verified; controlled/synthetic checks are required and real browsing/query history/persistent identity are excluded. |
| Conflict handling explicit | **PASS** | VPN, Private Relay, browser/app custom resolver, blocked transport, captive/managed and unaccepted device/network states demote/stop the protection claim rather than being hidden. |
| Android removal/recovery explicit | **PASS** | Leave custom provider-hostname mode, normally restore Automatic/normal policy, run neutral recovery check, mark Removed. |
| iPhone removal/recovery explicit | **PASS** | Remove exact UseSafeWeb profile/settings, run neutral recovery check, mark Removed. |
| OS asymmetry explicit | **PASS** | Android native DoT hostname and iPhone DoH profile paths are separate; no protocol chooser or universal setup string is presented. |
| Accountless/privacy scope preserved | **PASS** | No mandatory identity, account, child/device profile, payment or browsing-history collection is introduced. |
| Build/release boundary preserved | **PASS** | Candidate is internal provisional L4 only; no profile publication, implementation, participants or launch is authorized. |

## Adversarial checks

1. **Could the Android path be made “more automatic” by inventing a web-to-system-setting mechanism?** No accepted project evidence supports that. The candidate correctly leaves the system setting user/OS controlled.
2. **Could Apple profile download be called automatic setup?** No. Delivery of an already verified profile may be automated, but installation/authorization remains explicit OS/user action. The candidate separates those concepts.
3. **Could the candidate distribute a `.mobileconfig` now?** No. TSK-0408 explicitly leaves exact generated profile artifact/signing/distribution to separately governed implementation/release work. The candidate refuses to fabricate it.
4. **Could parent confirmation satisfy technical verification?** No. TSK-0320/0408 require a distinct system-verification threshold; candidate preserves that boundary.
5. **Could an active VPN, Private Relay or custom browser resolver simply be ignored for simplicity?** No. TSK-0409 treats unresolved coexistence as conflict/uncertainty; candidate preserves the strongest truthful state.
6. **Could removal silently switch to another UseSafeWeb resolver and retain a green state?** No. Removal ends the UseSafeWeb DNS protection claim; fallback does not mean a hidden alternate client/resolver.
7. **Does the candidate prove parent usability or low support burden?** No. `RSK-0002` remains OPEN and the artifact explicitly avoids behavioral claims.
8. **Does technical preparation satisfy HUMAN_ONLY authority?** No. The WBS action-authority boundary remains unsatisfied until a human explicitly disposes the exact candidate.

## ACC-0317 preparation assessment

The candidate contains all technical information necessary for a human to decide ACC-0317 without the AI guessing a product preference:

- automatic configuration is bounded to operations that are actually reliable and non-security-sensitive;
- manual fallbacks use canonical endpoint/profile guidance and safe removal/recovery;
- Android/iPhone OS asymmetry is explicit;
- known limitations and unsupported/conflict states are explicit;
- verification and removal/recovery are testable and privacy-minimal.

The **technical content is a complete PASS candidate**, but the task itself is **NOT PASS** because `HUMAN_ONLY` review/disposition has not occurred.

## Correct stable outcome

**Preparation:** COMPLETE and independently verified.  
**ACC-0317 technical candidate coverage:** COMPLETE.  
**TSK-0317 runtime disposition:** **WAITING** for HUMAN_ONLY review/decision on exact candidate blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`.

Minimum resume condition: the authorized human explicitly `APPROVE`, `REQUEST CHANGES`, or `REJECT` the exact candidate. If approved, independently re-check ACC-0317 against the unchanged blob and then reconcile PASS; approval does not authorize implementation/build/profile publication, participants or launch.