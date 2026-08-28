# TSK-0317 — Final Platform Design Acceptance Evidence

**Task:** `TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform`  
**Acceptance:** `ACC-0317`  
**Verification:** `VER-0317`  
**Evidence:** `EVD-0317`  
**Date:** 2026-08-28  
**Disposition:** **PASS candidate for runtime reconciliation**

## Exact evidence set

- Candidate `TSK_0317_PLATFORM_INSTALL_VERIFICATION_REMOVAL_RECOVERY_DESIGN_CANDIDATE_2026-08-28.md`, unchanged read-back blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`, publication commit `28156f75728c28333c61c33313007556839329e6`.
- Preparation evidence `TSK_0317_PLATFORM_DESIGN_PREPARATION_EVIDENCE_2026-08-28.md`, blob `8a233a40ec549a5ded9377048eb1ef365e9b31f3`, publication commit `719ec389e22f5626bab412b8dc6d1223739559eb`.
- Project Owner HUMAN_ONLY approval `TSK_0317_OWNER_APPROVAL_2026-08-28.md`, blob `260fe3795772c2e2928b86844172d5cad8407ba3`, publication commit `7f271d09eb9f2ac8b16d616e9b5ac1868bbbc762`.
- Current runtime pre-state: TSK-0317 WAITING on explicit HUMAN_ONLY disposition; all DEC-0050/CR-0003 fences preserved.
- Canonical WBS blob `dce5b829c4d447eac180ae1e896e0019292cf971` remains the task/dependency/ACC authority.
- Canonical manifest blob `00feca027babfd99dcd1992e3e0abd6ef2d3380b` continues to authorize only bounded provisional L4 work.

## Completion-gate verification

ACC-0317 requires: **Automatic profile/config is used only where reliable; fallbacks use canonical endpoint/profile guidance; OS asymmetry and limitations are explicit.**

| Acceptance element | Result | Direct basis |
| --- | --- | --- |
| Hard dependency `TSK-0316` is satisfied | **PASS** | Current authoritative runtime records the accepted TSK-0316 friction contract as PASS. |
| Required HUMAN_ONLY disposition occurred | **PASS** | Project Owner explicitly approved the exact candidate identified in the immediately preceding decision request; durable approval evidence is blob `260fe3795772c2e2928b86844172d5cad8407ba3`. |
| Candidate is unchanged since approval target was presented | **PASS** | Current read-back blob remains `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`. |
| Automatic behavior is limited to reliable operations | **PASS** | Candidate permits routing, copy, already-verified profile delivery, controlled verification and state rendering only where technically reliable. |
| Security-sensitive OS changes remain user/OS controlled | **PASS** | Android Private DNS setting changes and Apple profile installation/authorization/removal are never represented as silent automation. |
| Android endpoint/mechanism is canonical | **PASS** | Android path uses `dns.usesafeweb.com` as native Private DNS/DoT hostname; no DoH URL or normal `:853` input is substituted. |
| iPhone endpoint/mechanism is canonical | **PASS** | iPhone path uses the separately verified UseSafeWeb DNS Settings profile mechanism with `https://dns.usesafeweb.com/dns-query`; candidate does not fabricate/release a production profile. |
| Canonical fallback is explicit | **PASS** | Fallback is current manual platform guidance or safe removal/recovery, not an improvised resolver/client or silent plaintext fallback under a positive protection claim. |
| OS/platform asymmetry is explicit | **PASS** | Android DoT-hostname and iPhone DoH-profile paths are separate; user is not asked to choose protocol. |
| Supported scope is bounded | **PASS** | Current support design is limited to accepted Android 9+ phone and iPhone/iOS 14+ paths; unaccepted/managed families are not silently generalized. |
| Verification truth is preserved | **PASS** | Configuration presence and parent confirmation never equal `Verified`; current controlled/synthetic verification is required. |
| Conflict/limitation states are explicit | **PASS** | VPN, Private Relay, browser/app resolver, blocked network, captive/managed and unaccepted-platform cases demote/stop the protection claim. |
| Removal/recovery is explicit and reversible | **PASS** | Android returns to normal DNS policy and iPhone removes the exact UseSafeWeb profile/settings; protection claim ends after removal. |
| Privacy/accountless constraints are preserved | **PASS** | No account, identity, child/device profile, browsing/query history or persistent surveillance evidence is introduced. |
| Build/release boundary is preserved | **PASS** | Candidate and owner approval remain provisional internal L4 only; no implementation/build/profile publication/participant/public-launch authority is introduced. |

## Adversarial verification

1. **Approval ambiguity:** none material remains. The owner's `Approved` reply directly followed the exact decision request naming candidate blob `d44daf...` and no competing candidate/change request was introduced.
2. **Could approval authorize silent automation beyond the candidate?** No. Approval is bound to the exact unchanged candidate, whose automatic/manual boundary is explicit.
3. **Could existing technical evidence justify wider device support?** No. The candidate deliberately refuses extrapolation beyond accepted Android-phone/iPhone paths.
4. **Could a positive UI state be retained during unproven VPN/Private Relay/custom-resolver coexistence?** No. Candidate requires uncertainty/not-covered handling.
5. **Could safe recovery be interpreted as plaintext UseSafeWeb fallback?** No. Removal/reset ends the UseSafeWeb protection claim; no hidden fallback is introduced.
6. **Does this establish representative-parent usability?** No. `RSK-0002` remains OPEN and no behavioral validation claim is made.
7. **Does this authorize implementation or profile distribution?** No. The accepted scope remains internal L4 design only.

## Final acceptance result

Every current element of ACC-0317 is satisfied with durable/reconstructable evidence, including the WBS-required HUMAN_ONLY disposition. No contradictory current evidence was found. The accepted design preserves all existing frozen boundaries and introduces no unauthorized scope change.

**ACC-0317: PASS.**  
**TSK-0317: PASS candidate pending only canonical runtime reconciliation and read-back.**

This acceptance does not change `RSK-0002`, `REQ-0022`, LG-03/LG-04/LG-05/LG-06, EXC-0001, or any build/participant/payment/publication/launch authority.