# TSK-0315 — Accountless End-to-End Service Blueprint

**Task:** TSK-0315 — Create the accountless end-to-end service blueprint from discovery through recovery/removal  
**Acceptance:** ACC-0315  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 SERVICE BLUEPRINT / IMPLEMENTATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0149 public-vs-product outcome separation + TSK-0229 accountless journey data contract + DEC-0050/CR-0003 provisional L4 authority  
**Supporting current technical evidence:** TSK-0408 UseSafeWeb DNS identity/platform mechanism contract  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

Real-participant L3/Experiment-1 behavioral validation is deferred through 2027-08-27 or earlier explicit owner reactivation. This blueprint is therefore a conservative internal service-design contract assembled from frozen owner decisions, accepted technical/synthetic evidence, and current task/requirement/interface authority. It is **not** user-tested or behaviorally validated. There is no current representative-parent evidence proving completion, comprehension, incremental value, support burden, persistence, perceived duplication, or the optimal order/wording of these steps.

`RSK-0002` remains OPEN and materially applies. When L3 is reactivated, contradictory real evidence must reopen affected L4 assumptions. This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real-participant processing, legal completion, payment activation, public release or launch.

## 1. Blueprint objective and scope

Define one coherent accountless service journey that preserves the already-frozen distinction between:

1. **Public website outcome:** discover → understand → trust → decide → start.
2. **Product/setup outcome:** start → configure → verify/confirm truthfully → understand coverage/limits → recover/remove.

Both surfaces share one UseSafeWeb brand/system, but the website is not the setup product and the setup product is not a marketing site.

The current provisional product shape coordinates:

- relevant native phone safeguards;
- UseSafeWeb encrypted DNS baseline protection;
- at most one relevant external-service safeguard step;
- a truthful Protection Map / coverage summary;
- self-service troubleshooting, recovery and removal;
- no mandatory UseSafeWeb account or persistent child profile.

Detailed native-device routing remains owned by TSK-0143; the one-service rule/details remain owned by TSK-0144; the final Protection Map state/copy freeze remains owned by TSK-0320; supported OS/network/bypass coverage remains owned by TSK-0409. This blueprint defines their service boundaries without fabricating unfinished detail.

## 2. Service invariants

1. **Accountless first:** no login, parent name, child name, email, phone number or persistent customer/device identity is required for immediate value.
2. **Necessity before interaction:** every field, choice, confirmation and manual step must have a routing, technical, safety, evidence or recovery reason. Otherwise remove it.
3. **Truthful evidence:** parent confirmation is never represented as system verification.
4. **DNS identity is protocol-specific:** Android native Private DNS uses `dns.usesafeweb.com` as DoT hostname; Apple DoH uses the approved profile/Server URL `https://dns.usesafeweb.com/dns-query`. No universal setup string is invented.
5. **No browsing history:** the service never needs user browsing/domain history to show protection status.
6. **Ephemeral state:** use J0 browser/session state by default; optional J1 transient anonymous state is allowed only under the TSK-0229 necessity/expiry/deletion/no-linkage contract.
7. **Reversible protection:** a parent can remove/reset UseSafeWeb DNS and return the device to normal DNS behavior; removal ends the UseSafeWeb DNS protection claim until reconfigured and reverified.
8. **No complete-safety promise:** DNS protection and native/service safeguards are described as bounded layers with explicit gaps.
9. **Unsupported is a valid outcome:** unsupported/uncertain states are shown rather than hidden or coerced into false completion.
10. **No routine human support dependency:** expected problems use automated/state-specific help. Owner/human intervention is reserved for exceptional technical, security, privacy, legal or safeguarding conditions.
11. **Locale is not market authority:** eventual English/Turkish/Arabic/RTL availability does not imply official non-UK localization/support/legal/channel readiness.
12. **CR-0003 fence:** this blueprint is internal design only while behavioral validation is deferred.

## 3. Evidence vocabulary used by the blueprint

These are service-design evidence classes, not final UI copy. TSK-0320 owns the final state model/copy freeze.

- **System verified:** current supported technical evidence confirms the intended mechanism/state.
- **Parent confirmed:** parent states a native/service safeguard was completed where UseSafeWeb cannot technically verify it. Never relabeled as verified.
- **Configured, unverified:** UseSafeWeb configuration appears present but current verification is unavailable/incomplete.
- **Action needed:** an applicable step is incomplete or failed and has a known next action.
- **Not covered / unsupported:** the capability/path is outside current supported coverage.
- **Uncertain / error:** the service cannot safely determine the state because of conflict, bypass, compatibility or verification failure.
- **Removed:** UseSafeWeb configuration was intentionally removed/reset; protection claim is withdrawn.

The user-facing Protection Map must preserve the difference among these evidence classes even if final labels change later.

## 4. End-to-end service blueprint

| Stage | Parent action | System action | Evidence/state produced | Hard dependency / input | Expected failure or branch | Automated/self-service response | Privacy/data boundary | Owner/human-only exception |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0. Public discovery | Arrives from search/referral/direct URL. | Show concise first-phone outcome, bounded protection promise, free/core-value position, privacy/non-surveillance posture and primary Start action. | None; marketing view only. | TSK-0149; approved claims/content when available. | Parent expects surveillance, child tracking or complete safety. | Explain product boundary before Start; do not collect data to persuade. | No account; no behavioral profile required. | Material claims/policy change requires current authority/legal review where applicable. |
| 1. Understand & trust | Reviews how UseSafeWeb helps and what it cannot protect. | Separate Phone / Internet / Services layers; disclose DNS and platform limits; show privacy and removal principles. | Understanding opportunity only; no fake comprehension score. | Trust/non-surveillance constraints; later TSK-0320 copy/state freeze. | Parent misunderstands DNS as full-device monitoring or complete safety. | Point-of-need explanation and examples; retain explicit gaps. | No child details required. | Claims with legal/safeguarding impact are not silently changed by UX. |
| 2. Decide & start | Chooses Start setup. | Transition from public website to setup context without forcing signup/payment. Initialize J0; create J1 only if later architecture proves necessary. | `not_started`; ephemeral journey initialized. | TSK-0149; TSK-0229. | Browser/session unavailable or later resume requested. | Offer restart; any resume mechanism must stay within TSK-0229 J1 rules. | J0 preferred; no identity/contact. J1 fixed ≤24h only if necessary. | Persistent account/resume expansion requires EXC-0001 trigger + owner approval. |
| 3. Minimal routing intake | Selects only facts needed to route setup, provisionally: locale, device family, coarse platform/version support band, phone state where necessary. | Validate allowed values and route to supported/unsupported path. | Routing state only. | TSK-0229 allowlist; TSK-0143/TSK-0409 will refine supported matrix. | Unsupported/unknown device/version or missing routing fact. | Explain what is unsupported/unknown; permit safe exit/restart; never ask for identity to compensate. | No exact child age/DOB, name, account ID, device serial/fingerprint, location. | Expanding collected data is a material data-contract change if outside TSK-0229. |
| 4. Native phone safeguard | Follows the relevant native-device safeguard instruction or marks already configured where allowed. | Present only approved platform-specific instruction; capture parent-confirmed state unless a current system-verifiable method exists. | `parent confirmed`, `action needed`, `not covered`, or later approved system verification. | TSK-0143 pending; native platform evidence/content catalogue. | Setting unavailable, OS path differs, already configured, parent declines, device managed by another authority. | Show approved alternative/unsupported state; do not imply completion. | Store only controlled state if transient state is needed. | New platform policy, safeguarding/legal conflict or owner-scope change requires escalation. |
| 5. Internet/DNS choice | Proceeds with UseSafeWeb DNS baseline or acknowledges unsupported/conflict path. | Select approved platform-specific mechanism rather than universal FQDN workflow. | `configured_unverified`, `not covered`, or `uncertain` before verification. | TSK-0408 PASS; TSK-0409 will freeze supported matrix. | Platform/network/VPN/browser/app conflict or unsupported mechanism. | Explain conflict; do not claim protection; route to safe recovery/unsupported guidance. | No DNS query history/client profile is created for journey state. | New endpoint/protocol/production promotion or material security topology change needs its owning authority/gate. |
| 6A. Android DNS setup | Enters `dns.usesafeweb.com` in Android Private DNS provider hostname when the combination is supported. | Explain native DoT-by-hostname semantics; check only approved technical signals/synthetic tests. | `configured_unverified` → `verified`, `failed` or `uncertain`. | TSK-0408; TSK-0409 supported combination. | Hostname/certificate/reachability failure, VPN/network override, manufacturer UI difference. | Platform-specific help; synthetic verification; if unresolved, mark failed/uncertain and offer reset to normal DNS policy. | No full token/form payload logs; no real browsing/domain history. | Certificate/service incident beyond runbook, security compromise or policy change escalates. |
| 6B. Apple DNS setup | Installs/uses the approved UseSafeWeb DNS profile for the supported Apple path. | Use full DoH Server URL `https://dns.usesafeweb.com/dns-query`; keep pilot/test/future-production profile identities distinct. | `configured_unverified` → `verified`, `failed` or `uncertain`. | TSK-0408; later release `.mobileconfig` artifact verification; TSK-0409 supported combination. | Profile install fails, device management restriction, VPN/Private Relay/browser/app behavior prevents truthful verification. | Explain specific conflict/unsupported state; provide profile-removal/retry path; never infer verification from profile presence. | Same no-history/no-persistent-identity boundary. | Signing/distribution/public profile release is later implementation/release authority, not this blueprint. |
| 7. DNS verification | Runs UseSafeWeb's supported verification action. | Perform synthetic/controlled checks for intended resolver/allow-block behavior; return truthful state. | `system verified`, `failed`, `uncertain`, or `not covered`. | TSK-0408 verification contract; TSK-0409 matrix; existing accepted pilot technical evidence. | Caches, bypass, captive portal, VPN, browser/app secure DNS, network-specific behavior, service outage. | Distinguish failure from uncertainty; explain recovery; do not ask for browsing history as default diagnostic evidence. | Verification result may be transient state; queried real-user domains are not retained. | Exceptional request-level diagnostics follow separately governed diagnostic procedure and escalation boundary. |
| 8. External service safeguard | If one relevant approved service branch exists, follows its safeguard instruction or confirms already configured. | Present at most one relevant service step; otherwise mark Not covered/none applicable. | Usually `parent confirmed`; system verification only if a future approved mechanism genuinely supports it. | TSK-0144 pending. | Service unsupported, instructions stale, parent lacks account/authority, no relevant service. | Show Not covered/skip with consequence; do not invent generic multi-service coverage. | No service username, credentials, content or activity history in journey state. | Adding integrations/credentials or changing one-service scope requires owning task/authority. |
| 9. Protection Map / coverage summary | Reviews what is protected/configured, what needs action and what is not covered. | Synthesize only evidence actually held across Phone / Internet / Services; expose material limitations. | Provisional evidence-class map; exact final state/copy owned by TSK-0320. | TSK-0229; TSK-0408; later TSK-0320. | A layer is uncertain, unsupported, parent-confirmed only or removed. | Keep that state visible; provide exact next action/help; never coerce all-green completion. | No persistent child profile required to display current journey summary. | Final claims/state taxonomy freeze and material risk acceptance remain governed separately. |
| 10. Completion | Chooses Finish after understanding current state/gaps. | Show completion only for the journey, not “complete safety”; deliver any immediately necessary privacy-safe result; start deletion of transient server state if any. | Journey completed; each layer retains truthful evidence class until state deletion/exit. | TSK-0229 expiry/deletion; later TSK-0320 copy. | Parent leaves with action-needed/not-covered states. | Permit completion with explicit gaps where safe; do not force unsupported steps. | Delete J1 synchronously where possible or ≤15 min after completion; J0 ends with session. | Persisting history/account/dashboard is not allowed without later trigger/approval. |
| 11. Point-of-need help | Opens Help from the failing step. | Use issue-specific decision tree, configuration checks and synthetic tests first. | Updated current state or unresolved escalation state. | Later TSK-0319/TSK-0334; current TSK-0229 diagnostic separation. | Unknown error, repeated failure, possible outage/security/privacy incident. | Offer retry/reset/remove; classify what cannot be solved automatically. | No unrestricted free-text/raw diagnostic collection by default. | Exceptional technical/security/privacy/legal/safeguarding incident can reach owner/qualified human path. |
| 12. Reset/reconfigure | Chooses Start over / retry after a wrong or stale configuration. | Clear current J0/J1 state per contract; re-enter only the necessary branch; do not duplicate retained identity because none exists. | New transient `not_started`/routing state. | TSK-0229. | Old device config remains active while journey state resets. | Explicitly distinguish “reset this website journey” from “remove device protection”; route to removal when needed. | J1 deletion non-sliding and token non-reuse. | None for ordinary reset; material data-contract changes remain owner/governance-bound. |
| 13. Remove UseSafeWeb DNS | Removes custom Android provider or Apple profile. | Guide platform-specific removal; then withdraw verification/protection claim. | `removed`; normal DNS restored when successful. | TSK-0408 accepted removal/recovery contract; current technical evidence. | Removal fails or device policy blocks change. | Platform-specific recovery; explain that unresolved config may remain and do not mark removed without evidence/confirmation appropriate to mechanism. | No history required. | Managed-device/ownership/security incident may require authorized device admin or owner escalation. |
| 14. Post-removal recovery | Confirms normal internet/DNS operation or follows recovery help. | Use neutral synthetic connectivity checks; show UseSafeWeb DNS no longer active. | `removed` / normal DNS restored; no UseSafeWeb protection claim. | Accepted TSK-0514 recovery evidence; TSK-0408. | Normal DNS still fails because of unrelated network/device issue. | Separate UseSafeWeb-removal result from unrelated network failure; avoid claiming root cause without evidence. | No browsing history. | Infrastructure/service incident can escalate through operating runbook when applicable. |
| 15. Exit | Leaves service at any supported stage. | End J0; delete J1 on explicit exit where no transient operation requires it; do not create marketing identity from setup state. | No durable user journey profile. | TSK-0229. | Parent wants long-term dashboard/history. | Explain current accountless model; future persistence is trigger-based, not silently enabled. | No cross-session stitching or household profile. | Persistent-account feature requires separate validated trigger and explicit owner authority. |

## 5. Dependency and unfinished-design map

This blueprint is intentionally explicit about what it does **not** freeze:

| Boundary | Current treatment | Owning next/future task |
| --- | --- | --- |
| Native safeguard routing and supported states | Service slot and truthful evidence boundary only; no fabricated detailed OS instructions. | TSK-0143 |
| External service selection/instruction | At most one relevant service; Not covered/none applicable is valid. | TSK-0144 |
| Protection Map exact labels/copy/transitions | Provisional evidence classes only. | TSK-0320 |
| Supported OS/device/network/bypass matrix | Consume current accepted Android/iPhone pilot evidence; unsupported/conflicts stay explicit. | TSK-0409 |
| Friction budget | Blueprint records necessity rationale; quantitative/interaction challenge follows. | TSK-0316 |
| Detailed install/recovery UX | Blueprint establishes service sequence; final detailed path has separate authority, including HUMAN_ONLY tasks where assigned. | TSK-0317/0319/0330/0334 as applicable |
| Final instruction catalogue/localization | Blueprint carries language/market distinction, not final content. | TSK-0323 and related content/i18n work |
| User testing | Explicitly absent under CR-0003. | Deferred L3 / TSK-0187 when reactivated |

No downstream task is treated as PASS merely because its slot appears here.

## 6. Interaction necessity ledger

To satisfy REQ-0028, each current blueprint interaction has a necessity:

| Interaction | Necessity | Can be removed now? |
| --- | --- | --- |
| Start | Explicit transition from informational public surface to setup state. | No. |
| Locale | Required to render the eventual multilingual/RTL experience correctly; locale is not market identity. | No if multiple locales are active; otherwise can default without asking. |
| Device family | Routes fundamentally different platform mechanisms. | No. |
| Coarse version/support band | Needed only where instructions/support differ. | Ask/derive only when necessary; exact build fingerprint prohibited. |
| Phone state (new/already used/unknown) | Only if it changes native-safeguard routing/already-configured handling. | Remove if later TSK-0143 proves unnecessary. |
| Native safeguard action/confirmation | Coordinates relevant native protection without pretending UseSafeWeb controls it. | No when applicable; skip when not applicable/already configured. |
| DNS setup action | Activates the distinctive UseSafeWeb encrypted-DNS baseline. | No for the current provisional product shape, but unsupported path must be allowed. |
| DNS verification | Prevents configuration/presence from masquerading as active protection. | No where a supported verifier exists. |
| External-service action/confirmation | Adds at most one relevant service safeguard where genuinely applicable. | Remove/skip when no approved relevant service. |
| Review Protection Map | Makes evidence/gaps explicit before completion. | No. |
| Finish | Closes the immediate journey and triggers transient-state deletion. | Could be implicit only if deletion/state semantics and gap visibility remain equally clear; default retain pending later friction work. |
| Help | Required at points with expected recoverable failures. | No, but keep contextual rather than generic where possible. |
| Reset/remove | Required for reversibility and recovery. | No. |
| Account/login/payment | No necessity in active baseline. | **Removed / prohibited from core journey.** |

## 7. Automated support model

Routine support should be state-driven and self-service:

1. identify the current stage and evidence state without persistent identity;
2. show the smallest relevant check, not a generic FAQ wall;
3. use approved configuration inspection/synthetic tests before requesting diagnostics;
4. distinguish `failed` from `uncertain`;
5. offer retry only when it can materially change the result;
6. offer reset/reinstall/remove when safer than repeated troubleshooting;
7. explain the protection consequence of removal/bypass;
8. avoid raw DNS/query history, unrestricted free text and persistent per-user support profiles;
9. close with a confirmed current state or explicit unresolved escalation.

### Exceptional escalation triggers

Escalate out of automated support only for a genuine boundary such as:

- suspected security compromise/abuse;
- privacy/data incident;
- legal/safeguarding question requiring authority/qualified judgment;
- material certificate/DNS infrastructure incident not safely resolved by approved runbook;
- managed-device/ownership restriction needing an authorized administrator;
- contradiction between current platform behavior and canonical instructions that could cause unsafe/misleading guidance;
- repeated unknown failure where broader diagnostics would be necessary.

The escalation path does not authorize routine collection of personal/raw DNS data. Exceptional diagnostics remain separately time-boxed/governed.

## 8. Privacy and data-flow summary

The blueprint deliberately avoids turning service design into a profile system.

**Preferred ordinary path:**

`Public page (no identity) → J0 transient setup state → platform action → synthetic verification result → Protection Map in current session → completion → session ends.`

**Only if later technically necessary:**

`Public page → opaque J1 token + allowlisted transient state → fixed non-sliding ≤24h expiry → early deletion on completion/reset/exit → no cross-session identity linkage.`

Never introduce through this blueprint:

- parent/child identity;
- stable household/device IDs;
- browsing/DNS/domain history;
- child profile/dashboard history;
- IP-to-journey identity linkage;
- service credentials/content;
- payment identity;
- advertising/behavioral tracking;
- persistent support/analytics profile.

## 9. Owner-only / governed decision boundaries

The journey may automate routine technical/configuration decisions, but it must not silently make these consequential decisions:

- activate persistent account/dashboard scope;
- broaden stored personal data or retention beyond TSK-0229;
- change frozen AdGuard/backend/encrypted-DNS direction absent the owning technical/governance authority;
- promote controlled-pilot endpoint/profile artifacts to public production;
- declare a new OS/network combination supported without evidence;
- approve legal/privacy/safeguarding residual risk or legal attestation;
- change material safety/protection claims;
- activate real participants/recruitment while CR-0003 defers L3;
- enable payments or make supporter funding affect protection;
- declare LG-05/LG-06, build, public release or launch PASS.

## 10. Acceptance checklist for ACC-0315

ACC-0315 requires the blueprint to identify parent actions, system actions, evidence states, dependencies, failures, automated support, privacy, and owner-only exceptions.

- **Parent actions:** explicit for discovery, start, routing, native safeguard, DNS setup/verification, service step, review, completion, help, reset, removal and exit.
- **System actions:** explicit for each stage and constrained by current technical/data authority.
- **Evidence states:** explicit, truthful and separated between system verification and parent confirmation.
- **Dependencies:** exact current/future ownership boundaries named; unfinished tasks are not fabricated as complete.
- **Failures:** unsupported, verification, bypass/conflict, install, stale-content, removal and recovery branches represented.
- **Automated support:** point-of-need, synthetic/config-first and privacy-minimal with escalation triggers.
- **Privacy:** accountless J0-first; J1 only under TSK-0229; no browsing/profile/linkage model.
- **Owner-only exceptions:** persistent scope, legal/risk, production/release/launch, payment and other consequential boundaries explicitly fenced.
- **REQ-0028:** interaction necessity ledger supplied.
- **REQ-0029:** platform-specific automatic/profile/configuration behavior is used only where current evidence supports it; technically correct fallbacks/unsupported states are preserved.
- **CON-0010:** no mandatory account.
- **CON-0017:** multilingual capability remains distinct from official market/support activation.
- **INT-0009/INT-0010 limitation:** this artifact contributes a provisional implementation/acceptance contract but cannot satisfy any interface clause that requires a *validated* or real-usability-tested experience while `RSK-0002` remains open.

**TSK-0315 result: PASS candidate subject to independent verification and runtime read-back.**
