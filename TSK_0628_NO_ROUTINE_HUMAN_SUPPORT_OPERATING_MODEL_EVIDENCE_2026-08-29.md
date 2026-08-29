# TSK-0628 — No-Routine-Human-Support Operating Model Acceptance Evidence

**Task:** `TSK-0628 — Define the no-routine-human-support operating model across setup, verification, troubleshooting, recovery, removal, and lifecycle events`  
**Acceptance:** `ACC-0628`  
**Date:** 2026-08-29  
**Disposition:** **PASS candidate for runtime reconciliation**

## Exact evidence set

- Artifact: `TSK_0628_NO_ROUTINE_HUMAN_SUPPORT_OPERATING_MODEL_2026-08-29.md`, exact Git blob `bb81ec47fd4badd06ded70d146365281c2874390`, publication commit `25ec7bfa2968ea424badf6c890943397872eedc0`.
- WBS inspection run `33241609024`, job `99071804111`: TSK-0628 is L4 / HIGH / A3 / `AUTO_ALLOWED`, sole dependency `TSK-0319`, acceptance `ACC-0628`.
- Current runtime: TSK-0319 PASS with approved troubleshooting/recovery candidate blob `86de353dd8446f02ed48c80638391a3caa852e59` and final acceptance evidence blob `2dc4ab8ba336b28652a85e6deec0e79291e56477`.
- Controlling support requirements: `TSK_0042_USER_SUPPORT_EXCEPTION_RECOVERY_REMOVAL_REQUIREMENTS_2026-08-28.md`, blob `bf9e1ece69b5ccfc38c1cb44d69de6545b7865dc`.
- Service blueprint: `TSK_0315_ACCOUNTLESS_END_TO_END_SERVICE_BLUEPRINT_2026-08-28.md` (current accepted runtime PASS).
- Supporting accepted contracts: TSK-0320 truth states, TSK-0307 source-backed instructions, TSK-0229 accountless state, TSK-0311 localization architecture, EXC-0001 and EXC-0008.

## ACC-0628 criterion

**“Top ordinary issues map to prevention, automatic checks, in-product help, AI assistance, or recovery; human route is exceptional and bounded.”**

## Independent checks

| Check | Result | Evidence |
| --- | --- | --- |
| Ordinary support model is explicitly no-routine-human | **PASS** | Default sequence is prevention → automatic check → truthful state → issue-specific help → bounded AI → recovery/removal; staffed interaction is not the default. |
| All current ordinary TSK-0042 issue classes are covered | **PASS** | Matrix covers SETUP, JOURNEY_STATE, DNS_REACHABILITY, FILTERING_FALSE_POSITIVE, COMPATIBILITY_CONFLICT, REMOVAL_RECOVERY, STALE_GUIDANCE, SERVICE_OUTAGE, GUIDANCE and OTHER/unsupported. |
| Prevention is explicit | **PASS** | Supported-tuple routing, source currency, limitation disclosure, filter policy and current support matrix are used before failure where applicable. |
| Automatic checks are explicit and bounded | **PASS** | Model consumes TSK-0319 service-health, support-tuple, DNS-path, filter, conflict, recovery and journey-state checks and preserves privacy/evidence limits. |
| In-product help is issue-specific | **PASS** | Help is mapped at router, native safeguard, Android/iPhone setup, verification, Protection Map, removal, post-removal and stale-guidance points. |
| AI assistance is bounded to existing authority | **PASS** | AI can explain/select approved branches but cannot invent support methods, mutate admin/service state, request prohibited data, claim verification or self-authorize exceptions. |
| Recovery/removal is first-class | **PASS** | Android/iPhone exact removal, protection-claim withdrawal and neutral recovery confirmation remain available without account creation. |
| Hidden human completion is impossible by definition | **PASS** | Any owner/operator/support person materially completing an ordinary task disqualifies that case from automatic/self-service resolution. |
| Human routes are exceptional and criterion-driven | **PASS** | Privacy/security, safeguarding, service/operator incident, managed-admin, governed filter change, exceptional diagnostics, stale source and material legal/scope cases have named bounded routes. |
| Routine staffed-support SLA is not invented | **PASS** | EXC-0008 remains controlling; model explicitly prohibits a public response-time promise and does not activate a team/chat/ticket SLA. |
| Accountless-first is preserved | **PASS** | Routine support requires no login, email, phone, names, account recovery or persistent support identity. |
| Privacy-minimal support is preserved | **PASS** | Browsing/query history, raw DNS logs, credentials, fingerprinting and unrestricted diagnostic dumps are excluded from routine support. |
| Verification truth is preserved | **PASS** | Parent/profile/AI/help completion cannot create `Verified`; unsupported/uncertain states remain truthful. |
| Security/privacy controls are not weakened | **PASS** | Model bars disabling unrelated work/school/security/privacy controls merely to obtain success. |
| Retry loop has a circuit breaker | **PASS** | Equivalent retry without changed evidence is prohibited; terminal truthful outcomes and exceptional routes are defined. |
| Lifecycle events are covered | **PASS** | Platform/source drift, endpoint/profile changes, certificate issues, filtering changes, J0/J1 expiry, localization drift and removal/exit have operating behavior and owner boundaries. |
| Later measurement semantics expose human assistance | **PASS** | Prevented/automatic/self-service/AI-assisted/exceptional-human/unresolved definitions are distinct; hidden-human cases cannot enter automated numerator. |
| Implementation verification is testable | **PASS** | Sixteen explicit assertions define a later rehearsal/implementation acceptance surface. |

## Adversarial checks

1. **Could ordinary failure silently become “contact support”?** No. Human routing requires a named exceptional criterion; unsupported ordinary issues terminate truthfully without routine staffed completion.
2. **Could AI become a second support authority?** No. It is subordinate to approved instructions, decision trees and truth-state contracts.
3. **Could AI or a parent statement fabricate technical verification?** No.
4. **Could a service outage trigger repeated user reconfiguration?** No; service health precedes repeated device changes.
5. **Could a false positive be solved by disabling protection broadly?** No; only the governed narrow reversible exception path is permitted.
6. **Could privacy-invasive diagnostics become a convenience fallback?** No; exceptional collection remains separately governed and approval-bounded.
7. **Could a human operator intervention be counted as automation success?** No; the measurement definition explicitly excludes it.
8. **Could this artifact be misread as proof that real parents need no support?** No. `RSK-0002` remains OPEN and behavioral validation remains deferred.
9. **Does this activate staffed support, telemetry, diagnostics, accounts, implementation or launch?** No.

## Conclusion

The exact artifact satisfies every current ACC-0628 requirement with durable, testable design evidence. **TSK-0628 qualifies for runtime PASS** for provisional internal L4 operating-model definition only.

This PASS does not prove real-user self-service performance, implement support automation/AI, activate telemetry or staffed support, authorize diagnostic collection, process participants, complete legal work, publish the service, activate payment, or authorize launch.