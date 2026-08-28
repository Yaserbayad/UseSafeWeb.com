# TSK-0319 — Troubleshooting/Recovery Design Preparation Evidence

**Task:** `TSK-0319 — Design automated verification, issue-specific troubleshooting, safe reset/reinstall/remove, and point-of-need help`  
**Acceptance:** `ACC-0319`  
**Action authority:** **A1 / HUMAN_ONLY**  
**Date:** 2026-08-28  
**Disposition tested:** preparation completeness only; **NOT task PASS**.

## Exact evidence set

- Candidate `TSK_0319_AUTOMATED_VERIFICATION_TROUBLESHOOTING_RECOVERY_HELP_DESIGN_CANDIDATE_2026-08-28.md`, publication commit `674c83b716039cd2165c41f0b223ebc1dc551560`, exact Git blob `86de353dd8446f02ed48c80638391a3caa852e59`.
- Current runtime selected TSK-0319 TODO for preparation only.
- Hard dependencies TSK-0315 and TSK-0320 are current runtime PASS.
- Accepted inputs: TSK-0042 support/recovery requirements, TSK-0317 platform setup design, TSK-0307 instruction catalogue, TSK-0409 support matrix, TSK-0207 privacy-persistence evidence, TSK-0514 removal/recovery evidence, TSK-0229 accountless state contract.

## WBS / authority verification

TSK-0319 is L4 / HIGH / A1 / `HUMAN_ONLY`. ACC-0319 requires the top expected failures to have concise decision trees, automatic checks where possible, privacy limits, recovery confirmation, and exceptional escalation criteria.

Dependencies are satisfied. HUMAN_ONLY remains the independent completion boundary; AI preparation cannot self-approve the design.

## ACC-0319 preparation checks

| Check | Result | Evidence |
| --- | --- | --- |
| Top expected failures have concise decision trees | **PASS** | Candidate defines 14 bounded trees covering unsupported/unknown device, Android, iPhone, verification/filtering, captive portal, VPN/managed tunnel, Private Relay/custom resolver, stale guidance, Android/iPhone removal, journey-state loss, service outage, privacy/security and safeguarding. |
| Automatic checks used where possible | **PASS** | Seven-check library covers service health, support tuple, DNS path, filtering, conflict, recovery and journey-state resume using synthetic/state evidence. |
| Checks reduce user work before device changes | **PASS** | Common triage runs service/support evidence before unnecessary configuration changes where applicable. |
| Retry behavior bounded | **PASS** | Recheck requires a materially changed condition/new evidence; repeated equivalent loops are prohibited and a circuit breaker routes to truthful unresolved/removal/escalation outcome. |
| Verification truth preserved | **PASS** | Setting/profile presence and parent confirmation never equal Verified; unresolved conflict stays uncertain/not covered. |
| Privacy limits explicit | **PASS** | Routine diagnostics exclude browsing/query history, raw DNS logs, persistent identity/fingerprint, credentials, unrestricted free-text dumps and persistent support identity. |
| Reset/reinstall/remove distinguished | **PASS** | Web journey reset is explicitly separated from Android/iPhone device configuration removal; reinstall is limited to exact verified profile/current supported path. |
| Android removal/recovery explicit | **PASS** | Leaves custom provider mode, normally restores Automatic/normal policy, withdraws protection claim and runs neutral recovery check. |
| iPhone removal/recovery explicit | **PASS** | Removes exact UseSafeWeb profile/settings, withdraws protection claim and runs neutral recovery check. |
| Recovery confirmation explicit | **PASS** | Completion requires configuration removed/reset or external management boundary stated, claim withdrawn, neutral check and truthful restored/still-failed/uncertain result. |
| VPN/security control boundary preserved | **PASS** | Design prohibits disabling required work/school/security/privacy controls merely to obtain green status. |
| Point-of-need help explicit | **PASS** | Help placement is mapped to router, native/DNS setup, verification, uncertain/not-covered, Protection Map, removal and post-removal states. |
| Exceptional escalation criteria explicit | **PASS** | Privacy/security, secret exposure, safeguarding, service-wide incidents, managed-admin boundary, stale source, authorized false-positive change and exceptional diagnostics are separated from routine self-service. |
| No routine staffed-support SLA invented | **PASS** | EXC-0008 boundary is preserved; deterministic product response does not create an unapproved human SLA. |
| Accountless-first preserved | **PASS** | No login/account/email/phone/persistent support identity is needed for routine recovery. |
| Build/public boundary preserved | **PASS** | Automatic checks are design intents, not implemented evidence; no diagnostics collection, implementation or public use is authorized. |

## Adversarial checks

1. **Could generic retries conceal a failure?** No. Retry requires changed evidence and ends at truthful unresolved/removal/escalation state.
2. **Could a service outage cause repeated device changes?** No. Service health is checked first where applicable.
3. **Could VPN/Private Relay conflicts be “solved” by weakening unrelated controls?** No; the design forbids that and preserves uncertainty.
4. **Could troubleshooting ask for browsing history to diagnose DNS?** No; routine evidence is synthetic/state-based only.
5. **Could Reset imply DNS was removed?** No; web-state reset and device removal are separate flows.
6. **Could connectivity recovery leave UseSafeWeb marked protected?** No; removal withdraws the protection claim before/independent of recovery confirmation.
7. **Could a residual post-removal network failure be falsely blamed on UseSafeWeb?** No; cause remains unproven unless evidence establishes it.
8. **Could exceptional diagnostics become routine?** No; they remain separately governed and approval-bounded.
9. **Could privacy/security or safeguarding be treated as ordinary support?** No; both leave the normal troubleshooting path.
10. **Does this prove representative-parent self-service success?** No. `RSK-0002` remains OPEN.
11. **Does preparation satisfy HUMAN_ONLY authority?** No. Human disposition remains required.

## Correct stable outcome

**Preparation:** COMPLETE and independently verified.  
**ACC-0319 technical/design coverage:** COMPLETE.  
**TSK-0319 runtime disposition:** **WAITING** for HUMAN_ONLY review/decision on exact candidate blob `86de353dd8446f02ed48c80638391a3caa852e59`.

Minimum resume condition: authorized human explicitly `APPROVE`, `REQUEST CHANGES`, or `REJECT` the exact candidate. Approval would be followed by independent final ACC-0319 re-check before runtime PASS. No approval authorizes implementation, diagnostics collection, staffed support, participant/public use or launch.