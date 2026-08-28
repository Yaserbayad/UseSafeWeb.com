# TSK-0318 — Public Website and Product/Setup IA Design Candidate

**Task:** `TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems`  
**Acceptance:** `ACC-0318`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Action authority:** **A1 / HUMAN_ONLY**  
**Authority:** TSK-0315 accountless service blueprint + TSK-0316 friction contract + TSK-0317 approved platform setup design + TSK-0307 instruction catalogue + TSK-0320 protection-state contract + TSK-0314 accessibility NFR + DEC-0050/CR-0003  
**Artifact status:** **CANDIDATE / HUMAN DECISION REQUIRED / NOT PASS**  
**Date:** 2026-08-28

## 1. Authority and evidence boundary

This candidate prepares the information architecture required by TSK-0318 but does not perform or fabricate its HUMAN_ONLY design disposition.

The design is limited to the current **accountless-first provisional internal L4** product. It does not reintroduce login, persistent parent dashboard, child/device profiles, browsing/query/activity history, unrestricted DNS administration, payment gating, participant processing, public launch, or any other scope excluded or deferred by current authority.

`RSK-0002` remains OPEN. There is no representative-parent evidence proving that this IA is optimally understood, preferred, or sufficiently easy. `REQ-0022` remains unresolved under the legal hold. Any legal/compliance page listed below is therefore an **IA slot with controlled readiness**, not evidence that legal content is complete or publication-ready.

## 2. Core IA decision

UseSafeWeb is one service with **two distinct connected systems**:

1. **Public website** — discovery, explanation, trust, compatibility, privacy, help and the decision to start.
2. **Product/setup surface** — route the current device, configure applicable safeguards, verify what can be verified, show truthful coverage, troubleshoot, remove/recover and exit.

The transition is explicit:

`Public website → Start setup → Product/setup surface`

The setup surface may link back to public reference content, but it must not become a marketing/navigation site. The public site may explain the product, but it must not pretend that reading a page configured or verified a device.

## 3. Global navigation and surface rules

### Public website primary navigation

- **Home**
- **How it works**
- **Compatibility & limits**
- **Privacy**
- **Help**
- **Start setup** — primary action, visually distinct from informational navigation

No `Login`, `Dashboard`, `Account`, `Pricing`, or mandatory checkout item exists in the current active baseline.

### Product/setup navigation

The setup surface is task/state driven rather than site-navigation driven:

- current step / concise progress context where useful;
- contextual `Help`;
- safe `Start over` where appropriate;
- `Remove UseSafeWeb DNS` where technically relevant;
- `Exit` / return to public site;
- no marketing carousel, blog navigation, account menu or unrelated upsell during setup.

### Shared invariants

- Same UseSafeWeb identity and terminology across both systems.
- Shared accessibility, privacy, language/fallback, claims and source-version rules.
- Public content can explain layers and limitations; setup state can link to that explanation without forcing it as an extra mandatory step.
- A public page cannot manufacture `Verified`, `Protected`, or completion state.
- Setup states cannot silently create SEO-indexable per-user/session URLs containing device/journey information.

## 4. Public website IA

| Surface / route intent | One purpose | Entry | Exit / primary next action | Content owner | SEO / index intent | Privacy requirement | Accessibility requirement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Home** `/` | State the bounded first-phone proposition, what UseSafeWeb covers, what it does not cover, and offer Start. | Direct URL, search, referral, public internal links. | `Start setup`; secondary links to How it works / Compatibility / Privacy / Help. | Product + Content | **Index** when publication is later authorized; canonical public landing surface. | No account/identity requirement; no setup-state leakage into public analytics; current telemetry remains separately governed. | WCAG 2.2 AA target; clear heading structure, visible focus, concise primary CTA, text-resize/reflow support. |
| **How it works** | Explain the Phone / Internet / Service layers and truthful Protection Map concept without complete-safety claims. | Home, search, contextual setup reference link. | `Start setup`, Compatibility, Privacy, back to referring setup context when technically safe. | Product + Content + Network for DNS claims | **Index** after release authorization. | No child/device data needed. | Layer explanation must not rely on color/icon alone; jargon expansion and readable headings required. |
| **Compatibility & limits** | Explain currently supported device families/mechanisms and known unsupported/uncertain conditions before setup. | Home, search, setup unsupported/uncertain reference link. | `Start setup` only when current support can still be determined in setup; Help otherwise. | Product + Network Engineering + Content | **Index** after source-current release review. | No fingerprinting or identity required to read support information. | Tables/accordions, if used, must be keyboard/screen-reader operable; unsupported states expressed in text. |
| **Privacy / non-surveillance** | Explain accountless-first operation, no browsing/query-history product model, transient journey-state principles, recipients at the approved high level, and deletion/removal boundaries. | Home/footer, setup reference, search. | `Start setup`, Help, return. | Privacy + Product + Content | **Index** when approved for publication. | Must reflect current canonical privacy contract; no invented final legal approval or unresolved REQ-0022 claim. | Plain-language summary plus accessible structured detail; links meaningful out of context. |
| **Help & recovery** | Route common pre-setup, setup, verification, removal and connectivity problems to source-backed help. | Public navigation, setup contextual help, search. | Relevant help branch, Start, Remove/recovery instructions, return to setup/public context. | Support/UX + Network Engineering + Content | **Index selectively** for stable general help pages; issue/session-specific state must not be indexed. | No unrestricted free-text/raw diagnostic collection by default; no browsing history. | Decision trees keyboard/screen-reader operable; error/help states announced and recoverable. |
| **Legal / required notices slot** | Provide any actually approved legally required public notice/contact/policy material once the owning legal work authorizes it. | Footer/reference links where required. | Return to originating context. | Legal/Privacy owner; not UX by inference | **Index/noindex determined by the owning legal/publication decision**, not invented here. | `REQ-0022` and deferred legal/contact work remain unresolved; placeholders must not be published as completed legal facts. | Structured headings, accessible links, readable content. |
| **Start transition** | Move from public information to the operational accountless setup context with the smallest explicit user action. | Primary CTA from Home/How/Compatibility/Help. | Product/setup `Start / route` surface. | Product/UX | **No separate index target required**; transition action, not marketing content. | Initialize J0 only; J1 only if TSK-0229 necessity contract permits. | CTA name describes destination/action; no ambiguous “Continue” from unrelated context. |

### Public-site duplication controls

- Home contains the shortest proposition/limits summary; detailed explanations live in their owning page rather than being copied in full across every page.
- Compatibility owns support truth; Help may link to it but does not maintain a second independent support matrix.
- Privacy owns non-surveillance/data semantics; setup displays only point-of-need summaries plus a link.
- How it works owns conceptual layer explanation; setup owns actual device state.
- Legal notices remain governed by their legal owner and are not recreated as marketing copy.

## 5. Product/setup IA

The setup IA follows the already accepted TSK-0315 journey and TSK-0316 friction constraints. It is **not** a mandatory one-screen-per-row rule: adjacent steps may be combined when doing so reduces friction without obscuring state, accessibility, safety or evidence truth.

| Product/setup surface/state | One purpose | Entry | Exit / next action | Content owner | SEO / index intent | Privacy requirement | Accessibility requirement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Start / minimal router** | Establish only the minimum transient context needed to select a supported setup path. | Public `Start setup`, restart. | Native-safeguard step, DNS setup, or Not covered/uncertain branch. | Product/UX | **Noindex / operational** when implemented. | J0 preferred; no identity/contact; request device/OS facts only when routing requires them. | Form controls explicitly labelled; validation/errors programmatically associated; no forced locale selection when safe default exists. |
| **Native safeguard** | Present the relevant approved native-device safeguard step, or truthfully skip/not-cover it. | Router. | DNS setup or Action needed/Not covered. | Product/UX + Content; source technical owner where applicable | **Noindex** | Store only transient state if required; no child details. | Step/status conveyed by text; current instructions source-versioned; skip/already-configured handling is keyboard accessible. |
| **Android DNS setup** | Guide the supported Android user through native Private DNS hostname configuration. | Supported Android route. | Verification, Help, Remove/recovery, Exit. | UX + Network Engineering | **Noindex** | No DNS history or persistent device identity. | Exact hostname can be copied accessibly; instructions do not depend on gesture/visual-only directions. |
| **iPhone DNS setup** | Guide the supported iPhone user through the exact separately verified UseSafeWeb DNS-profile install/authorization path. | Supported iPhone route when exact profile artifact is eligible. | Verification, Help, Remove/recovery, Exit. | UX + Network Engineering | **Noindex** | No identity; profile delivery must not embed user/device tracking identifiers. | Clear handoff to OS; return/re-entry instructions; no claim of silent installation. |
| **Verification** | Determine whether current technical evidence supports Verified, Action needed, Uncertain or Not covered. | After DNS setup; explicit recheck after changed condition. | Protection Map on supported result; issue-specific help; removal/recovery. | Network Engineering + UX | **Noindex** | Controlled/synthetic checks only; no real browsing/query history or persistent identity. | Loading/result/error changes announced; retry action labelled; result not color-only. |
| **External-service safeguard** | Present at most one relevant approved external-service safeguard when applicable. | After core DNS verification/routing according to current journey. | Protection Map; Help; skip/not-covered where valid. | Product/Content | **Noindex** | No service credentials/usernames/activity history stored by UseSafeWeb journey. | Parent-confirmed state clearly differs from system verification; skip/not-covered accessible. |
| **Protection Map / coverage summary** | Show current Phone / Internet / Service evidence states, limits and exact next actions without forcing all-green completion. | After applicable setup steps; from help/recheck where state changes. | Finish/exit without extra acknowledgement, fix Action-needed item, Help, Remove. | Product/UX; state semantics TSK-0320 | **Noindex** | No persistent child/device profile required; current transient state only. | Every status has textual name/description; logical reading order; focus management after updates. |
| **Action needed** | Present one known repair for a failed/incomplete supported condition. | Verification or step failure. | Recheck after changed condition, Help, Remove/Exit. | UX + Network Engineering | **Noindex** | Minimal diagnostic facts only. | Error and repair relationship explicit; no retry loop without changed condition. |
| **Status uncertain** | State that UseSafeWeb cannot safely determine the effective protection path. | VPN/Private Relay/custom resolver/network/managed ambiguity. | Contextual explanation, Help, Remove/Exit; recheck only after condition changes. | UX + Network Engineering | **Noindex** | Do not collect invasive data to force certainty. | Uncertainty is explicit text, not downgraded visual styling alone. |
| **Not covered** | Stop optimistic progression for an unsupported/unaccepted combination. | Router or conflict/support evaluation. | Compatibility reference, Help, Exit; no speculative alternate client. | Product/UX + Network Engineering | **Noindex** | No identity collection to waitlist/track by default. | Clear reason and next safe option; user is not trapped. |
| **Help / issue-specific troubleshooting** | Resolve the current failure with the smallest relevant decision tree and automatic check. | Contextual Help from any setup state. | Return to step, Recheck, Reset, Remove, exceptional escalation. | Support/UX + Network Engineering | **Noindex** | No unrestricted raw/free-text diagnostics by default. | Decision tree accessible by keyboard/screen reader; preserves current context. |
| **Start over / reset journey** | Clear transient web journey state and restart routing without pretending device configuration was removed. | User-invoked recovery. | Start/router. | Product/UX | **Noindex** | Clear J0/J1 according to TSK-0229; no cross-session linkage. | Consequence explained before any material state loss; distinguish from device removal. |
| **Remove UseSafeWeb DNS** | Guide platform-specific removal of the active UseSafeWeb DNS configuration. | Help/Protection Map/failure state. | Recovery check / Removed state. | UX + Network Engineering | **Noindex** | No browsing history required. | Exact removal action and consequences stated; OS handoff and return path accessible. |
| **Removed / recovery result** | Confirm UseSafeWeb DNS claim ended and distinguish successful normal-connectivity recovery from unrelated network failure. | Removal flow. | Start again, Help, Exit/public site. | UX + Network Engineering | **Noindex** | No durable user/device state needed. | Result announced and textually clear; retry/help options reachable. |
| **Completion / exit** | End the current setup journey while preserving truthful layer states until transient deletion/exit. | Protection Map after user chooses to leave/finish. | Public site or browser exit. | Product/UX | **Noindex** | J1 deletion according to TSK-0229; no marketing identity generated from setup state. | No unnecessary mandatory Finish confirmation; explicit gaps remain visible. |

## 6. Connection model between public and product systems

### Allowed connections

- Public `Start setup` → setup router.
- Setup Help → stable public Help/Compatibility/Privacy reference where that reduces duplication.
- Public Compatibility → Start setup, where the setup surface performs the actual current routing/verification.
- Setup Exit/Removed → public Home or Help.
- Public How it works → Start setup.

### Disallowed or misleading connections

- Public content must not deep-link directly to a `Verified` state.
- Search-indexed URLs must not expose transient journey/device state.
- Marketing pages must not read or display a persistent child/device profile because the current baseline has none.
- Setup must not redirect through signup/payment before core value.
- Help must not create a second independent support matrix or endpoint source of truth.
- A legal-content placeholder must not be surfaced publicly as if approved/legal completion existed.

## 7. Route/state ownership and persistence

- Public routes contain no user-specific state.
- Operational setup routes should use generic semantic routes/state containers; sensitive or identifying state is not placed in the URL.
- J0 browser/session state is default.
- Any J1 transient anonymous state follows TSK-0229 necessity, expiry, deletion and no-linkage semantics; the IA does not create a new persistence reason.
- No account/session lifecycle is introduced by navigation structure.
- Browser Back/Refresh/return-from-OS behavior must not transform stale configuration into a verified state; verification/state contracts still govern.

## 8. SEO/indexing contract

**Indexable candidate surfaces after publication authority:** Home, How it works, Compatibility & limits, Privacy, stable general Help, and any approved public legal page according to its owner.

**Noindex operational surfaces:** router, native/DNS setup, verification, Protection Map, issue-specific troubleshooting, reset/removal/recovery, operational error/uncertainty/not-covered/completion states.

Rationale: operational pages are transient task/state surfaces, not independent search destinations, and must not expose session/device state or create stale duplicated instructions in search results.

This is an IA **intent**, not evidence that robots/meta/header controls are implemented.

## 9. Completeness / no-duplication cross-check

| Critical service need from TSK-0315 | IA owner surface | Missing? | Duplicated authority? |
| --- | --- | --- | --- |
| Discover / proposition | Public Home | No | No |
| Understand layers/limits | Public How it works | No | Setup links rather than duplicates full explanation |
| Compatibility/support limits | Public Compatibility + setup router | No | Compatibility owns descriptive matrix; router owns current path selection |
| Trust/privacy | Public Privacy + point-of-need setup summary | No | Privacy owns detail |
| Start | Public Start transition + setup router | No | Clear system boundary |
| Native safeguard | Setup Native safeguard | No | Detailed instruction remains source-catalogue-owned |
| Android/iPhone DNS setup | Platform-specific setup | No | One mechanism per accepted platform |
| Technical verification | Verification | No | TSK-0320/technical evidence owns state truth |
| One external service | External-service safeguard | No | TSK-0144 owns relevance/content rule |
| Truthful coverage | Protection Map | No | TSK-0320 owns state/copy semantics |
| Unsupported/uncertain | Dedicated states + Compatibility | No | No false success branch |
| Help/troubleshooting | Contextual Help + stable public Help | No | Issue tree vs stable reference separated |
| Reset vs remove | Separate Reset and Remove surfaces | No | Consequences not conflated |
| Post-removal recovery | Removed/recovery result | No | No protection claim retained |
| Exit/deletion | Completion/exit | No | TSK-0229 owns deletion semantics |

No critical current service-blueprint stage is absent. Public explanation and operational setup are connected without duplicating mutable technical/support truth into independent authorities.

## 10. Human review assertions

The HUMAN_ONLY reviewer should explicitly accept/reject these assertions:

1. Public website and setup product are separate connected systems rather than one mixed navigation tree.
2. The public site contains only Home, How it works, Compatibility & limits, Privacy, Help, controlled legal-notice slot and Start transition needed by the current scope.
3. Login/account/dashboard/pricing/payment are absent from the active core IA.
4. The setup IA follows the accepted accountless journey and does not create mandatory marketing/education screens.
5. Android and iPhone setup remain platform-specific.
6. Verification, Protection Map, uncertain/not-covered, help, reset, removal and recovery are first-class operational states/surfaces.
7. Each page/screen/state has one defined purpose, entry, exit/next action, content owner, SEO/index intent, privacy requirement and accessibility requirement.
8. Public stable information may be indexable only after release authority; operational/session/state surfaces are noindex by design.
9. No user/device/transient journey data is placed in indexable URLs or public content.
10. Stable public pages own explanatory detail; setup uses concise point-of-need summaries/links instead of duplicating mutable support/privacy/technical truth.
11. Resetting the website journey is not conflated with removing device DNS protection.
12. Legal-page IA presence does not assert unresolved legal content/contacts are complete.
13. Turkish/Arabic/content availability does not activate a market.
14. No IA choice changes the accepted protection-state evidence rules or turns parent confirmation into system verification.
15. The IA remains provisional internal L4 only and does not authorize implementation/publication/launch.

## 11. Human decision packet

Required disposition on this exact candidate:

- **APPROVE** — accept as the provisional internal L4 IA baseline;
- **REQUEST CHANGES** — identify the specific page/screen/ownership/index/privacy/accessibility/connection assertion to change;
- **REJECT** — identify the conflicting requirement or decision.

Approval would satisfy the HUMAN_ONLY decision component only after independent acceptance verification confirms the unchanged candidate satisfies ACC-0318. Approval would not authorize implementation or public release.

## 12. Candidate result

The candidate defines distinct but connected public and setup systems; assigns one purpose, entry, exit, owner, SEO/index intent, privacy and accessibility requirement to every current page/screen/state; covers every critical accepted service-blueprint stage; avoids duplicated mutable technical/support authority; preserves accountless/friction/truth/recovery boundaries; and introduces no unauthorized scope.

**TSK-0318 remains NOT PASS because its WBS action authority is HUMAN_ONLY and the required human design disposition has not occurred.**