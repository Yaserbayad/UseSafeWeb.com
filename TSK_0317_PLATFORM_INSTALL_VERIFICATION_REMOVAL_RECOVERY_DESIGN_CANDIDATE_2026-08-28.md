# TSK-0317 — Platform Install, Verification, Removal and Recovery Design Candidate

**Task:** `TSK-0317 — Design the simplest technically correct install, verification, removal, and recovery path for each supported platform`  
**Acceptance:** `ACC-0317`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Authority:** `DEC-0050` / `CR-0003` provisional internal L4 only  
**Action authority:** **A1 / HUMAN_ONLY**  
**Artifact status:** **CANDIDATE / HUMAN DECISION REQUIRED / NOT PASS**  
**Date:** 2026-08-28

## 1. Authority and evidence boundary

This candidate prepares the TSK-0317 design but does **not** perform or fabricate the HUMAN_ONLY decision required by the WBS. AI may assemble the strongest source-grounded candidate and verification packet; the human authority must accept, reject or change the design before TSK-0317 can be considered complete.

The candidate is limited to the currently accepted provisional L4 support baseline. It does not authorize implementation, public profile distribution, production application changes, real participants, legal completion, payment, publication or launch. `RSK-0002` remains OPEN: no representative-parent evidence proves that these flows are easy, understood, preferred or low-support.

## 2. Inputs and inherited contracts

This design consumes, without redefining, the following accepted contracts:

- TSK-0316 friction/minimisation contract: remove unnecessary product interactions; retain irreducible OS/security actions; never manufacture a one-click claim.
- TSK-0408 DNS identity/platform contract: one service identity with platform-specific mechanisms — Android native Private DNS uses DoT hostname `dns.usesafeweb.com`; iPhone uses the approved DoH Server URL/profile mechanism `https://dns.usesafeweb.com/dns-query`.
- TSK-0409 support matrix: current public-facing support baseline is Android 9+ phones with usable native Private DNS hostname control and iPhone/iOS 14+ with the approved manual DNS Settings profile path; other device families/managed combinations remain unsupported or not-yet-supported unless separately proven.
- TSK-0320 truth-state model: system verification, parent confirmation, action-needed, not-covered, uncertain/error and removed states must never be conflated.
- Existing technical evidence proves the accepted endpoint, TLS, representative supported-device verification, external-network checks and removal/recovery for the bounded tested paths; this design does not extend those proofs to untested combinations.

## 3. Design principles

1. **Route; do not teach protocols.** The parent should not choose DoH versus DoT. Platform routing determines the approved mechanism.
2. **Automate only what is technically reliable and authority-safe.** Automatic routing, copy actions, profile-file preparation/download, neutral verification checks and state rendering may be automated where proven. System DNS changes and OS security/profile authorization are never represented as silently automated when the platform still requires user action.
3. **One current support path per supported platform.** Do not present alternative DNS clients, VPNs or speculative workarounds merely to increase apparent coverage.
4. **Verification determines the protection claim.** Configuration presence or parent confirmation alone cannot produce `Verified`.
5. **Failure is truthful.** Known incompatibility becomes `Action needed`, `Not covered` or `Status uncertain`; it is never hidden behind more confirmations.
6. **Removal is first-class.** Every supported setup path has a corresponding supported removal/recovery path.
7. **No surveillance evidence.** Verification uses controlled/synthetic checks and never needs real browsing/query history or a persistent child/device identity.

## 4. Common routing before platform instructions

The setup surface should establish only the minimum context needed to choose the correct supported path.

1. Determine/confirm device family only when it cannot be safely derived without persistent fingerprinting.
2. Determine OS/support band only when it changes support or instructions.
3. Evaluate current known blockers that can be detected safely without invasive data collection.
4. If the combination is not currently supported, stop the optimistic setup path and render the correct `Not covered` / `Status uncertain` state plus safe exit/recovery guidance.
5. If supported, route directly to the platform-specific path below. Do not display a protocol chooser.

No login, parent/child identity, payment, persistent device profile or browsing history is required to route the current accountless journey.

## 5. Android 9+ phone — candidate path

### 5.1 Eligibility

Use this path only when the current device is an Android phone on Android 9+ and native `Private DNS provider hostname` control is present, usable and not known to be policy-blocked.

Do **not** silently generalise this path to Android tablets, ChromeOS, managed devices or Android-derived devices that have not been separately accepted.

### 5.2 Install/configuration flow

1. Present one concise explanation: UseSafeWeb will configure the phone's native encrypted DNS baseline; it does not provide complete device safety and does not replace native parental controls.
2. Present the Android Private DNS instructions using current platform wording/source ownership; OEM navigation wording may vary, so content must be version/source maintained rather than frozen to an invented universal menu path.
3. Instruct the parent to select the platform's custom/private provider-hostname mode.
4. Present **exactly** the hostname `dns.usesafeweb.com`.
5. Provide a copy action where useful. Do not append `:853` in the normal Android input and do not show the HTTPS DoH URL.
6. The parent performs the OS-required save/apply action. UseSafeWeb must not say that the website silently changed the system DNS setting.
7. Return to the UseSafeWeb surface for verification. If the OS/browser cannot return automatically, the user may navigate back normally; do not add a second confirmation merely for telemetry.

### 5.3 Automatic versus manual boundary

**May be automated when reliable:** platform routing, hostname display/copy, contextual instructions, verification attempt, state rendering, neutral retry after a changed condition.

**Must remain user/OS controlled under the current baseline:** opening/changing the Android Private DNS setting, selecting provider-hostname mode, entering/pasting the hostname and saving/applying the system setting.

No current accepted evidence supports a silent web-based Android system-DNS change, and this candidate prohibits claiming one.

### 5.4 Verification

After configuration, run the approved controlled verification automatically when technically feasible. Otherwise show one deliberate `Check protection` / `Recheck` action.

`Verified` requires current technical evidence that the intended encrypted path is active and the approved controlled allow/block checks behave as expected. Parent confirmation, settings-screen presence or successful hostname resolution alone is insufficient.

If a VPN, browser/app custom resolver, network block or other current conflict makes the effective path uncertain, render `Status uncertain`/`Not covered` as defined by the accepted support/truth contracts rather than issuing a green state.

### 5.5 Removal and recovery

1. Provide `Remove UseSafeWeb DNS` from help/recovery, not as normal happy-path friction.
2. Guide the parent back to Android Private DNS and leave the custom UseSafeWeb provider-hostname mode.
3. Restore the platform's normal policy, normally `Automatic`, unless the parent independently chooses another non-UseSafeWeb setting.
4. Run a neutral/synthetic connectivity check where feasible; never ask for browsing history.
5. Mark the UseSafeWeb DNS layer `Removed`; no protection claim remains until the supported path is configured and verified again.

If UseSafeWeb configuration causes loss of resolution, the safe recovery is removal/reset to normal platform DNS behavior. Do not silently fall back to plaintext while continuing to claim UseSafeWeb protection.

## 6. iPhone / iOS 14+ — candidate path

### 6.1 Eligibility

Use this path only for the currently accepted iPhone/iOS 14+ manual DNS Settings profile baseline where profile installation is allowed and the exact supported path is not blocked by management/security conditions.

Do not generalise current iPhone evidence to iPad, Mac, managed/supervised devices or other Apple families without separate acceptance.

### 6.2 Install/configuration flow

1. Present one concise explanation: the UseSafeWeb DNS profile configures the approved encrypted DNS baseline; it does not provide complete device safety.
2. Offer only the exact currently approved/versioned UseSafeWeb profile artifact once that release artifact has itself passed its owning artifact-level verification. **This L4 candidate does not fabricate or release a `.mobileconfig` file.**
3. The profile's DNS Settings mechanism must use the approved DoH Server URL `https://dns.usesafeweb.com/dns-query` and the correct UseSafeWeb/environment identity defined by TSK-0408.
4. Downloading/preparing the verified profile may be automated, but profile installation remains an explicit iOS/user authorization action.
5. Guide the parent through the current Apple profile-installation route using current source/version-controlled instructions rather than assuming one immutable settings path.
6. Do not claim silent installation, background authorization or automatic weakening of an unrelated iOS security control.
7. Return to UseSafeWeb for verification after the OS reports the profile installed.

### 6.3 Automatic versus manual boundary

**May be automated when reliable:** platform routing, delivery of an already verified profile artifact, version/applicability checks, contextual instructions, verification attempt and state rendering.

**Must remain user/OS controlled:** approving/installing the profile, any security-sensitive profile authorization and removal of the profile.

If current iOS security policy, management or Stolen Device Protection prevents the normal approved flow, do not advise weakening unrelated security merely to obtain a positive UseSafeWeb state. Show `Action needed`, `Not covered` or `Status uncertain` according to the owning support rule.

### 6.4 Verification

Profile presence is only configuration evidence, not `Verified` protection. Run the approved controlled verifier automatically where feasible; otherwise expose one deliberate check/recheck action.

An active VPN, iCloud Private Relay or other resolver/tunnel path whose coexistence has not been directly accepted prevents a universal `Verified` claim. Preserve the accepted conflict/uncertainty rule; do not claim that such features definitely disable or definitely preserve UseSafeWeb unless exact current evidence proves it.

### 6.5 Removal and recovery

1. Identify the exact installed UseSafeWeb DNS profile.
2. Guide the parent to remove that profile through the current Apple profile-management route.
3. Removal of the profile removes its associated UseSafeWeb DNS settings.
4. Run a neutral/synthetic connectivity check where feasible.
5. Mark UseSafeWeb DNS `Removed`; do not retain a protection claim.

If the profile path creates a material connectivity problem, removal is the safe recovery action. Do not invent a client-side alternate resolver while continuing to claim the current UseSafeWeb path is active.

## 7. Conflict and unsupported-state handling

The design must explicitly stop or demote the protection state for at least these current cases:

| Condition | Design outcome |
| --- | --- |
| Unsupported OS/device family | `Not covered`; do not improvise another client. |
| Managed/locked DNS/profile controls | `Not covered` or `Status uncertain` until exact supported policy path exists. |
| Captive portal before normal network access | Complete ordinary network access first; no UseSafeWeb protection claim until verified. |
| Android network blocks intended DoT/TCP 853 | `Action needed`/`Status uncertain`; removal/recovery available; no silent plaintext fallback claim. |
| Apple network blocks intended DoH/HTTPS endpoint | `Action needed`/`Status uncertain`; removal/recovery available. |
| VPN changes/owns DNS path | `Status uncertain`/not covered until exact coexistence is accepted; do not instruct disabling required employer/school/security VPN merely to make the UI green. |
| iCloud Private Relay coexistence unproven | `Status uncertain`; do not claim definite compatibility or incompatibility. |
| Browser/app custom encrypted resolver | The affected traffic is not included in a universal system-DNS protection claim unless directly proven. |
| IPv6-only/NAT64-only current combination | `Not covered`/not-yet-supported until directly accepted. |

Adding confirmations cannot convert an unsupported/conflicting path into a supported one.

## 8. Fallback policy

`Fallback` in TSK-0317 means **the canonical approved manual platform guidance or safe removal/recovery path**, not an unreviewed resolver/client workaround.

- Android fallback is the current native hostname guidance plus safe reset to normal DNS when the intended path cannot operate.
- iPhone fallback is the exact verified profile/manual installation guidance plus safe profile removal when the intended path cannot operate.
- There is no universal hostname/URL input and no silent plaintext fallback under an active UseSafeWeb protection claim.
- Server-side upstream fallback remains owned by the resolver/operations contract and is not redefined here.

## 9. Parent-facing action vocabulary

Candidate CTAs should describe the immediate truthful action, for example:

- `Start setup`
- `Copy DNS hostname`
- `Get UseSafeWeb profile` only when the exact profile artifact is approved for that environment
- `Check protection`
- `Try again` only after a changed condition
- `Remove UseSafeWeb DNS`

Do not use:

- `Protect this phone in one click`
- `Turn on UseSafeWeb automatically` when OS action remains
- `Fully protected`
- `Works on every Android/iPhone`
- `One setting protects every app/network`
- `Install and forget`

## 10. Minimum candidate happy paths

### Android

`Start → supported Android route → native Private DNS instruction → copy/paste dns.usesafeweb.com → user saves OS setting → controlled verification → truthful Protection Map state`

### iPhone

`Start → supported iPhone route → obtain exact verified UseSafeWeb DoH profile → explicit iOS profile install/authorization → controlled verification → truthful Protection Map state`

Recovery remains available from every failure/uncertain state and after completion.

These are design paths, not measured click-count or usability claims.

## 11. Acceptance assertions for human review

The HUMAN_ONLY reviewer should be able to approve/reject each assertion explicitly:

1. Only currently supported Android-phone and iPhone paths are presented as supported.
2. Android uses hostname `dns.usesafeweb.com`; iPhone uses the approved DoH profile/Server URL mechanism; users never choose the protocol.
3. No Android system setting is claimed to change silently from the web surface.
4. No Apple profile is claimed to install without explicit OS/user authorization.
5. Any automatically delivered Apple profile must first be the exact separately verified artifact for the correct environment/version.
6. Configuration presence and parent confirmation never equal `Verified`.
7. Verification uses controlled/synthetic evidence without browsing/query history or persistent identity.
8. Known VPN/Private Relay/browser/app/network conflicts demote or bound the protection claim rather than being hidden.
9. Unsupported/managed/unaccepted paths stop with truthful status rather than receiving speculative workarounds.
10. Android removal restores normal platform DNS policy and ends the UseSafeWeb DNS protection claim.
11. iPhone removal deletes the exact UseSafeWeb profile/settings and ends the UseSafeWeb DNS protection claim.
12. Failure recovery never silently falls back to plaintext while retaining a UseSafeWeb protection claim.
13. Automatic actions are limited to routing, safe content/profile delivery where already verified, neutral verification and state rendering; security-sensitive OS changes remain user/OS controlled.
14. OS asymmetry and known limitations are explicit without unnecessary technical jargon.
15. The design remains accountless, reversible, privacy-minimal and compatible with the current provisional L4 scope.

## 12. Human decision packet

The smallest required HUMAN_ONLY disposition is on this exact candidate:

- **APPROVE** — accept the candidate as the TSK-0317 design baseline for provisional internal L4;
- **REQUEST CHANGES** — identify only the assertions/path elements to change;
- **REJECT** — reject the candidate and state the conflicting requirement/decision.

Approval of this design would satisfy the human decision component only if the exact candidate and acceptance assertions are explicitly accepted and independent acceptance verification finds no remaining ACC-0317 gap.

Approval would **not** authorize build, profile publication, participants or launch.

## 13. Candidate result

The candidate provides one technically correct bounded path for each currently supported platform, uses automatic behavior only where current evidence permits it, preserves canonical endpoint/profile fallback guidance, makes Android/iPhone asymmetry explicit, defines truthful verification and conflict behavior, and gives each supported path a reversible removal/recovery flow.

**TSK-0317 remains NOT PASS because its WBS action authority is HUMAN_ONLY and the required human design disposition has not yet occurred.**