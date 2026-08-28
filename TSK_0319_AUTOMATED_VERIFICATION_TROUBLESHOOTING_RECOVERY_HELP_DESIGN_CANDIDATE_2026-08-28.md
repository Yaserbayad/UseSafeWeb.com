# TSK-0319 — Automated Verification, Troubleshooting, Recovery and Point-of-Need Help Design Candidate

**Task:** `TSK-0319 — Design automated verification, issue-specific troubleshooting, safe reset/reinstall/remove, and point-of-need help`  
**Acceptance:** `ACC-0319`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Action authority:** **A1 / HUMAN_ONLY**  
**Authority:** TSK-0315 service blueprint + TSK-0320 protection-state model + TSK-0042 support/recovery requirements + TSK-0317 approved platform setup design + TSK-0307 instruction catalogue + TSK-0409 support matrix + TSK-0207 privacy-persistence evidence + TSK-0514 removal/recovery evidence + DEC-0050/CR-0003  
**Artifact status:** **CANDIDATE / HUMAN DECISION REQUIRED / NOT PASS**  
**Date:** 2026-08-28

## 1. Boundary

This candidate prepares the HUMAN_ONLY troubleshooting/recovery design. It does not perform the human design decision, implement a verifier, mutate device settings, activate staffed support, collect diagnostics, publish profile/software, or authorize public/participant use.

`RSK-0002` remains OPEN: no representative-parent evidence proves these decision trees are easy or sufficient. The design therefore optimizes for minimum steps and truthful state based on current accepted technical evidence, not fabricated support-success metrics.

## 2. Design principles

1. **Classify before remedy.** Use the existing TSK-0042 issue taxonomy; do not start with generic `Try again`.
2. **Check service/system evidence before blaming the device.** Run privacy-safe automatic checks where they can reduce user work.
3. **One changed condition per retry.** Equivalent repeated retries without new evidence are prohibited.
4. **No green state without evidence.** Setting/profile presence and parent confirmation never substitute for system verification.
5. **No surveillance diagnostics.** Routine checks use configuration/state, synthetic traffic and non-identifying health evidence; no browsing/query history.
6. **Recovery is always reachable.** Supported DNS setup can move toward safe remove/reset/recovery without account/login.
7. **Do not defeat unrelated security controls.** Required work/school/security VPNs or privacy controls are not disabled merely to make UseSafeWeb appear successful.
8. **Separate web reset from device removal.** Restarting accountless journey state does not mean DNS/profile configuration was removed.
9. **Exceptional escalation is narrow.** Human/security/privacy/legal/safeguarding routes exist only where current authority requires them; no routine staffed-support dependency is invented.

## 3. Automatic-check library

These are design intents. Implementation requires later authority and tests.

| Check | Purpose | Allowed inputs | Output | Privacy / failure boundary |
| --- | --- | --- | --- | --- |
| `CHK-SVC-HEALTH` | Determine whether current UseSafeWeb encrypted-DNS service/endpoint is healthy before device troubleshooting. | Current service health/synthetic endpoint evidence; no user identity. | `healthy`, `degraded`, `unavailable`, `unknown`. | No user request history; unknown cannot become healthy by assumption. |
| `CHK-SUPPORT-TUPLE` | Determine whether device/OS/network path is within current support matrix using only necessary routing facts. | Device family, coarse supported OS band, current relevant network/conflict facts when safely detectable/confirmed. | `supported`, `conditional`, `not_covered`, `unknown`. | No fingerprint/device serial/account identity; uncertain facts remain unknown. |
| `CHK-DNS-PATH` | Test whether approved UseSafeWeb encrypted resolver path is active/reachable for the current supported tuple. | Controlled/synthetic requests to approved endpoints. | `verified_path`, `failed`, `uncertain`. | No real browsing/domain history; configuration presence alone is insufficient. |
| `CHK-FILTER` | Confirm approved synthetic allow/block behavior after the intended resolver path is established. | Controlled test names/fixtures only. | `pass`, `fail`, `uncertain`. | No real user domain history. |
| `CHK-CONFLICT` | Identify known current conflict class where evidence is available. | Non-invasive current state/user-confirmed fact, e.g. VPN/Private Relay/custom resolver presence where safely knowable. | conflict class or `not_determined`. | Do not fingerprint or inspect unrelated content/traffic to force detection. |
| `CHK-RECOVERY` | Confirm ordinary DNS/internet connectivity after UseSafeWeb removal/reset. | Neutral/synthetic connectivity and DNS checks. | `normal_restored`, `still_failed`, `uncertain`. | Does not imply UseSafeWeb protection; no browsing history. |
| `CHK-JOURNEY-STATE` | Decide whether J0/J1 can safely resume or must restart. | Current J0 or valid opaque J1 token/state under TSK-0229. | `resume`, `restart`, `expired/deleted`. | No reconstruction via IP/fingerprint/account; no retention extension. |

## 4. Common triage sequence

For a setup/verification problem:

1. Preserve current truthful TSK-0320 state; do not optimistically advance.
2. Classify the issue from the smallest available symptom/current step.
3. Run `CHK-SVC-HEALTH` when relevant before asking the parent to change device settings.
4. Run/check `CHK-SUPPORT-TUPLE` when compatibility may explain the failure.
5. Use the issue-specific tree below.
6. Recheck only after a changed condition/configuration.
7. If no safe supported repair remains, present `Not covered`/`Status uncertain` or removal/recovery rather than more guesses.

## 5. Issue-specific decision trees

### DT-01 — Unsupported or unknown device/OS

**Trigger:** router cannot establish a current supported Android-phone or iPhone tuple.

1. `CHK-SUPPORT-TUPLE`.
2. If `not_covered` → show TSK-0320 `Not covered`; link to current Compatibility & limits; **do not** improvise another DNS client/VPN/profile.
3. If `unknown` because one necessary support fact is missing → ask only that fact; rerun once.
4. If still unknown → `Status uncertain` or `Not covered` according to TSK-0409; Exit/Help available.
5. If supported → route to exact platform setup.

**Recovery confirmation:** none required because no UseSafeWeb configuration should have been introduced; if partial config exists, route to exact removal tree.

### DT-02 — Android Private DNS setup not accepted / not active

**Trigger:** supported Android path, parent cannot save/apply or verification fails after entering hostname.

1. Confirm current instruction is `dns.usesafeweb.com`, not URL/port.
2. `CHK-SVC-HEALTH`.
3. If service unavailable/degraded → stop device-change loop; show `Action needed`/service issue plus removal option.
4. If service healthy → `CHK-DNS-PATH`.
5. If path fails and current evidence identifies network blocking intended DoT/TCP 853 → `Status uncertain`/Action needed; explain network condition; do not silently use plaintext.
6. If device setting is unavailable/locked/managed → `Not covered` under current self-service baseline.
7. If a known VPN/custom resolver conflict exists → DT-06.
8. Otherwise give one source-backed setting recheck; then rerun verification once after change.
9. Continued failure → issue-specific Help or Remove UseSafeWeb DNS; no generic retry loop.

**Recovery:** Android removal tree DT-09.

### DT-03 — iPhone profile not installed / profile verification fails

**Trigger:** supported iPhone path but exact verified profile cannot be installed, is absent, or DNS verification fails.

1. Confirm the setup is using the exact separately verified profile artifact for the current environment; do not generate/use an unverified replacement.
2. `CHK-SVC-HEALTH`.
3. If service issue → stop reinstall loop; show current service condition and removal option if profile exists.
4. If iOS/management/security policy blocks installation → `Not covered`/Action needed according to current support matrix; do not tell user to weaken unrelated security controls.
5. If profile installed → `CHK-DNS-PATH`; profile presence alone remains unverified.
6. If VPN/Private Relay/another resolver may affect path → DT-06/DT-07.
7. If current source-backed profile instruction may be stale → DT-08.
8. Otherwise allow one reinstall of the exact verified profile after removing the old UseSafeWeb profile, then recheck once.
9. Continued failure → `Status uncertain`/Help/Remove; no green state.

**Recovery:** iPhone removal tree DT-10.

### DT-04 — Verification endpoint reachable but filtering check fails

**Trigger:** intended path appears reachable but approved synthetic allow/block behavior does not pass.

1. Keep state `Action needed`/uncertain; do not report Verified.
2. Run `CHK-SVC-HEALTH` and `CHK-FILTER` once with current approved synthetic fixture.
3. If service/config regression evident → stop user-device changes; classify service/filtering incident.
4. If effective resolver path uncertain → DT-06/07 or support-matrix branch.
5. If a false-positive/exception symptom is specifically reported → use governed false-positive procedure, not broad filter disablement.
6. If cause remains unclear → issue-specific Help and safe removal option; exceptional diagnostics only through separately approved diagnostic procedure.

**Privacy:** no real visited domains requested to prove filter operation.

### DT-05 — Captive portal / network requires pre-authentication

1. If ordinary network access is not yet established, mark UseSafeWeb state not verified/uncertain.
2. Explain that captive-portal access must be completed under normal network behavior first; no protection claim during unresolved portal condition.
3. If UseSafeWeb config prevents reaching required portal and no supported safe coexistence exists → offer platform removal/reset.
4. After ordinary connectivity established, the parent may restart/reconfigure and run one current verification.
5. If the network still blocks intended encrypted DNS → remain `Status uncertain`/not covered for that network.

### DT-06 — VPN / managed tunnel / custom resolver conflict

1. Establish only the minimum fact that a competing resolver/tunnel may exist; do not inspect unrelated traffic.
2. If exact coexistence is not currently accepted → `Status uncertain`/not covered for affected traffic.
3. Do **not** instruct disabling required employer/school/security VPN or management merely to produce green state.
4. Explain current protection boundary and allow Exit/Remove UseSafeWeb DNS.
5. Recheck only if the user independently changes the condition or future accepted compatibility evidence exists.

**Escalation:** only if there is evidence of a UseSafeWeb security/privacy defect, not ordinary unsupported coexistence.

### DT-07 — iCloud Private Relay or browser/app resolver uncertainty

1. Do not assert compatibility or incompatibility beyond current TSK-0409 evidence.
2. Use `Status uncertain` for the affected path where coexistence cannot be proven.
3. Explain that an app/browser/private relay may use a different resolver path; do not claim whole-device/whole-app coverage.
4. Do not ask parent to weaken unrelated privacy/security merely for green status.
5. Offer Help/Exit/Remove; recheck only after changed condition/new supported evidence.

### DT-08 — Stale or contradictory instruction

1. If current OS/service behavior contradicts the source-backed instruction, stop presenting that instruction as current.
2. Mark affected setup path `Status uncertain`/`Not covered` until instruction owner re-verifies source/platform/applicability.
3. Do not tell the parent to experiment through guessed settings.
4. If UseSafeWeb configuration was partially applied, provide the last current verified removal path where still safe; otherwise escalate content/technical review before new instructions.
5. Record only privacy-safe evidence needed to update TSK-0307; no user identity required.

### DT-09 — Android remove/reset and recovery

1. Explain that **Start over** clears the web journey only; **Remove UseSafeWeb DNS** changes device DNS.
2. For removal, guide parent out of custom Private DNS provider-hostname mode and back to normal platform policy, normally `Automatic`.
3. Withdraw UseSafeWeb DNS protection claim immediately after removal action is confirmed appropriately; state becomes `Removed` rather than Verified.
4. Run `CHK-RECOVERY`.
5. If `normal_restored` → show Removed / normal connectivity restored.
6. If `still_failed` → state that connectivity issue remains and may be unrelated; do not reactivate UseSafeWeb claim or guess root cause.
7. If setting is managed/locked and removal cannot be performed → show exact owner/admin boundary; do not bypass management.

### DT-10 — iPhone remove/reset and recovery

1. Distinguish web journey reset from profile removal.
2. Identify/remove the exact UseSafeWeb DNS profile through current Apple profile-management route.
3. Removal ends UseSafeWeb DNS protection claim.
4. Run `CHK-RECOVERY`.
5. `normal_restored` → Removed / recovery confirmed.
6. `still_failed` → explain unresolved connectivity separately; no false UseSafeWeb causation claim.
7. If profile removal is managed/blocked → show current device-management boundary; do not improvise deletion/bypass.

### DT-11 — Accountless journey state lost/expired

1. `CHK-JOURNEY-STATE`.
2. Valid J0/J1 → resume only minimal permitted state; never infer stale Verified without current recheck.
3. Missing/expired/deleted/invalid J1 → restart necessary step(s); do not recover through account/email/IP/fingerprinting.
4. Reset deletes transient state per TSK-0229; device configuration remains separate.
5. If parent needs long-term persistence, record only as future product evidence; do not activate EXC-0001 scope.

### DT-12 — Suspected service outage

1. `CHK-SVC-HEALTH` before device troubleshooting.
2. If `unavailable/degraded` → present service issue/Action needed; stop repeated user configuration changes.
3. Offer safe removal/recovery if current configuration materially disrupts connectivity.
4. If health later changes, one recheck is allowed.
5. Operational escalation follows current service incident/runbook ownership; do not expose admin credentials or customer-facing AdGuard control plane.

### DT-13 — Privacy/security anomaly

**Examples:** prohibited persistent query history, exposed secret, unsafe diagnostic collection, deletion-verification failure, unsupported protection claim.

1. Stop affected diagnostic/setup path.
2. Preserve privacy-safe evidence only; raw sensitive/query data does not go to GitHub.
3. Do not continue ordinary troubleshooting as if issue were cosmetic.
4. Route through owning privacy/security incident process and Project Owner/delegated authority where required.
5. Resume affected functionality only after owning risk/evidence boundary is satisfied.

This is an **exceptional escalation**, not routine customer support.

### DT-14 — Safeguarding disclosure/concern

1. Exit product troubleshooting on the disclosure/concern.
2. Do not ask for unnecessary details or put personal/raw disclosure in GitHub/analytics.
3. Follow the dedicated child-safety/safeguarding procedure; immediate danger is not delayed for product debugging.
4. No ordinary product status can close a safeguarding matter.

## 6. Point-of-need help placement

Help should appear where the user can act on it, not as a forced tour:

| Current state | Default help content |
| --- | --- |
| Router unsupported/unknown | Compatibility reason + exact supported boundary + safe exit. |
| Native safeguard step | Current source-backed instruction + already-configured/unsupported handling. |
| Android DNS setup | Exact hostname instruction + wrong-value check + removal link. |
| iPhone profile setup | Exact verified-profile requirement + OS authorization/removal link. |
| Verification Action needed | One issue-specific tree based on current failed check; not generic FAQ dump. |
| Status uncertain | Explain which unresolved conflict class prevents a trustworthy claim and what, if anything, can safely change. |
| Not covered | Explain current unsupported boundary; no speculative workaround. |
| Protection Map | Help attaches to the specific layer/state rather than generic support. |
| Removal | Platform-specific removal + recovery confirmation. |
| Post-removal failed connectivity | Clarify UseSafeWeb removed state versus unrelated network failure; exceptional service issue only if evidence supports it. |

## 7. Retry budget

- Automatic verification may run on initial entry/configuration when technically reliable.
- One explicit/automatic recheck is allowed after each **materially changed condition**: corrected hostname/profile, completed OS action, network change, removal/reinstall, service recovery, or other evidence-producing change.
- A failure with no changed condition must not loop automatically or encourage repeated clicks.
- After two materially different bounded repairs fail for the same supported issue, default to truthful unresolved state + removal/recovery or exceptional escalation only when the issue class warrants it. This is a design circuit breaker, not a public support SLA.

## 8. Diagnostics/data contract

Routine troubleshooting may use only:

- current transient journey/protection state;
- supported tuple facts necessary for routing;
- synthetic endpoint/filter/connectivity tests;
- non-identifying service health/configuration evidence;
- minimum user confirmation where the system cannot observe an OS action.

Routine troubleshooting must **not** collect:

- browsing/domain history;
- raw DNS query logs;
- persistent child/device identity/fingerprint;
- credentials/service usernames;
- unrestricted free-text dumps;
- persistent support case identity merely to remember a routine issue.

Exceptional identifiable/request-level diagnostics remain outside this design and require the separately governed procedure/authority.

## 9. Recovery confirmation contract

A removal/recovery flow is complete only when:

1. the relevant UseSafeWeb configuration is removed/reset or the user is truthfully told removal is blocked by an external management boundary;
2. the UseSafeWeb protection claim is withdrawn (`Removed`), never left green because connectivity returned;
3. a neutral/synthetic recovery check is run where feasible;
4. `normal_restored`, `still_failed`, or `uncertain` is shown truthfully;
5. any remaining failure is not falsely attributed to UseSafeWeb without evidence;
6. transient J0/J1 cleanup follows TSK-0229 where the web journey is ended/reset.

## 10. Exceptional escalation criteria

Escalate beyond self-service only when current evidence indicates one of these governed boundaries:

- privacy/security incident or unsafe/prohibited data persistence;
- credential/secret exposure;
- safeguarding disclosure/concern;
- service-wide resolver/certificate/filtering outage requiring operator action;
- managed-device/network boundary requiring the actual authorized administrator;
- stale/contradictory source where no current safe instruction exists;
- material false-positive correction requiring an authorized configuration change;
- exceptional diagnostics genuinely required under their separate approval procedure;
- unresolved issue that exposes a material canonical product/safety defect rather than ordinary unsupported compatibility.

Do not escalate merely because a parent needs a routine supported instruction. `EXC-0008` continues to defer routine staffed support.

## 11. Human review assertions

The HUMAN_ONLY reviewer should explicitly accept/reject:

1. Triage uses current issue classes before remedy.
2. Service-health/support checks occur before unnecessary device changes where applicable.
3. The automatic-check library is limited to privacy-safe synthetic/state evidence.
4. The design covers unsupported device, Android setup, iPhone profile, filtering verification, captive portal, VPN/managed tunnel, Private Relay/custom resolver, stale guidance, Android removal, iPhone removal, journey-state loss, outage, privacy/security and safeguarding branches.
5. Each common failure has a concise bounded next action rather than a generic retry loop.
6. Verification and parent confirmation remain distinct.
7. Retry requires changed conditions/new evidence and has a circuit breaker.
8. Required work/school/security/privacy controls are not weakened solely for a green status.
9. Reset web journey and remove device configuration remain distinct actions.
10. Removal always withdraws the UseSafeWeb protection claim.
11. Recovery uses neutral/synthetic confirmation and separates unrelated residual connectivity failure.
12. Routine troubleshooting collects no browsing/query history or persistent identity.
13. Exceptional diagnostics remain separately governed.
14. Privacy/security and safeguarding cases leave ordinary product troubleshooting.
15. Routine staffed support/SLA is not introduced.
16. The design remains provisional internal L4 and authorizes no implementation/public use.

## 12. Human decision packet

Required disposition on this exact candidate:

- **APPROVE** — accept as the provisional internal L4 troubleshooting/recovery/help baseline;
- **REQUEST CHANGES** — identify specific decision tree/check/retry/recovery/escalation assertion to change;
- **REJECT** — identify conflicting requirement/decision.

Approval satisfies the human-decision component only after independent final ACC-0319 verification confirms the exact unchanged candidate. It does not authorize implementation, diagnostics collection, staffed support, participant/public use or launch.

## 13. Candidate result

This candidate provides concise decision trees for the current highest-probability failure classes, a privacy-safe automatic-check library, point-of-need help placement, changed-condition retry rules, safe reset/remove/recovery confirmation and narrow exceptional escalation criteria. It preserves TSK-0320 truth, TSK-0409 support limits, TSK-0042 support/privacy boundaries and current accountless scope.

**TSK-0319 remains NOT PASS because its WBS action authority is HUMAN_ONLY and the required human design disposition has not occurred.**