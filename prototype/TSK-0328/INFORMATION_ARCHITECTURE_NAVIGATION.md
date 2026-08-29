# TSK-0328 — Information Architecture and Navigation Model

**Version:** 1.0.0  
**Status:** internal L4 implementation/QA contract  
**Owner:** UX/UI  
**Action authority:** A3 / AUTO_ALLOWED  
**Sequencing:** DEC-0052 / CR-0005  
**Human-validation claim:** none  
**Build/publication authority:** none

## 1. Purpose and authority

This contract defines the smallest current information architecture and navigation model for SafeWeb. It converts the accepted TSK-0325 end-to-end journey into a deterministic public-to-setup architecture without adding an account, dashboard, unnecessary content section, persistent profile, marketing detour, or unsupported technical path.

Current source order for this artifact:

1. Current owner-frozen planning authority and DEC-0052 / CR-0005.
2. `prototype/TSK-0325/SERVICE_BLUEPRINT.md` v1.0.0 — current normal/exception journey and touchpoint authority.
3. `TSK_0318_PUBLIC_PRODUCT_SETUP_IA_DESIGN_CANDIDATE_2026-08-28.md` plus its accepted HUMAN_ONLY disposition — prior approved public-vs-product IA structure, reused only where still compatible with current authority.
4. `prototype/TSK-0309/BASELINE.md` v1.0.0 — frozen accountless journey/state/accessibility boundary.
5. `prototype/TSK-0324/UI_COMPONENT_RULES.md` v1.0.0 — current navigation/component/accessibility consumer rules.
6. TSK-0322/0323/0320 authorities for language, technical instructions and evidence-state truth.
7. This artifact — current route/screen/navigation ownership and requirement mapping.

Where TSK-0318 uses older `UseSafeWeb` visible identity or CR-0003 sequencing, current authority supersedes those details. Visible product identity is `SafeWeb`; `UseSafeWeb.com` is the domain/project identifier. The structural decision to keep the public website distinct from the operational setup surface remains valid.

## 2. Architecture decision

SafeWeb has exactly **two connected experience systems** in the current baseline:

1. **Public information system** — discovery, explanation, compatibility/limits, privacy, stable help and the explicit decision to start setup.
2. **Operational setup system** — transient accountless routing, setup, verification, Protection Map, troubleshooting, removal/recovery and reset.

Primary handoff:

`Public Home / information page → Start setup → /setup operational shell`

The public system explains; it never creates protection state. The setup system acts on transient journey state; it does not become a marketing site or account dashboard.

## 3. Explicit exclusions: sections and navigation that do not exist

The current IA has **no**:

- Login, Sign up, Account, Dashboard, Profile or child/device-history section;
- Pricing/checkout gate before core value;
- customer-facing AdGuard administration console;
- browsing/activity/DNS-query history section;
- generic Apps/Integrations marketplace;
- community/forum or routine staffed-support portal;
- public per-device/session/status URLs;
- separate navigation section for every technical instruction;
- separate page for each S1–S6 state;
- mandatory onboarding tour, newsletter capture, waitlist or identity form;
- duplicate support matrix, privacy authority, technical catalogue or Protection Map semantics.

A new section requires current necessity under `REQ-0028`, owning authority, privacy/scope review and an explicit architecture update.

## 4. Public information architecture

### Primary public navigation

Use this minimal information navigation when the public site is implemented:

- **Home**
- **How it works**
- **Compatibility & limits**
- **Privacy**
- **Help**
- **Start setup** — primary action, visually distinct from informational navigation

`SafeWeb` wordmark/Home returns to `/`. No Login/Dashboard/Account/Pricing item exists.

### Public route model

| Route ID | Route intent | User goal | Content responsibility | Primary next action | Requirement trace | Index intent |
| --- | --- | --- | --- | --- | --- | --- |
| `PUB-HOME` | `/` | Decide whether SafeWeb is relevant and understand the bounded first-phone proposition. | Product + Content | `Start setup`; secondary How/Compatibility/Privacy/Help. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 | Index only after publication authority. |
| `PUB-HOW` | `/how-it-works` | Understand Phone / Internet / Service layers and evidence-based Protection Map without a complete-safety claim. | Product + Content; technical claims from owning sources | `Start setup`; Compatibility. | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Index only after publication authority. |
| `PUB-COMPAT` | `/compatibility` | Learn current supported/unsupported boundaries before or during setup. | Product + technical support-matrix/instruction owner | `Start setup` when support remains plausible; Help otherwise. | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Index only when source-current and publication-authorized. |
| `PUB-PRIVACY` | `/privacy` | Understand accountless/non-surveillance/data-restraint principles and current privacy boundaries. | Privacy + Product + Content | `Start setup`; return. | REQ-0028; CON-0010; CON-0017; INT-0009; INT-0010 | Index only after owning privacy/publication authority. |
| `PUB-HELP` | `/help` | Find stable self-service setup, verification, removal and recovery guidance without exposing journey data. | UX/Support + technical/content owners | Relevant stable help branch; `Start setup`; return. | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Stable general help may index after publication authority; session-specific help never does. |
| `PUB-NOTICES` | controlled required-notices slot, route chosen only by owning publication/legal work | Read actually approved required notices when they exist. | Legal/Privacy owner | Return to origin. | REQ-0028; CON-0017; owning legal controls | No route/publication is created by this L4 IA; owner decides indexability. |

### Public duplication controls

- Home contains summary only; How it works owns conceptual explanation.
- Compatibility owns descriptive support/limit truth; Help links to it rather than maintaining a second support matrix.
- Privacy owns privacy/non-surveillance detail; setup uses point-of-need summaries/links only.
- TSK-0323 remains technical instruction source; public pages do not fork device procedures.
- TSK-0320/0322 remain state/claim authority; public pages cannot manufacture `Verified` or completion state.
- Required legal/notices content is a controlled slot, not invented content or implied legal completion.

## 5. Operational setup route strategy

The operational experience uses **one generic route family** rather than user-specific URLs:

- entry: `/setup`
- all logical screens/states are rendered inside the setup shell from transient in-memory journey state;
- no child, parent, device identifier, protection state, DNS result, provider, error diagnosis or other journey fact is encoded in the URL;
- no screen-specific route is required merely for analytics/SEO;
- setup is noindex/operational when implemented.

A framework may internally represent screen/state identifiers, but they are not public resource URLs and do not become persistence/account identifiers.

## 6. Setup shell navigation

The setup shell is task-driven. It does **not** show the full public primary navigation.

Persistent utility affordances, only when relevant:

- `Help` — opens contextual self-service help without changing protection state;
- `Limitations` — opens current scope/limit explanation without changing protection state;
- `Exit` — leaves setup for public Home or the safe prior public context;
- `Start over` — shown only when a reset is meaningful; clears transient journey state but does not remove device DNS;
- `Remove SafeWeb DNS` — shown only when current journey evidence indicates SafeWeb DNS may be configured and the platform removal path applies.

The current step/progress indicator, if displayed, is informational. It must not become unrestricted navigation that lets the user jump over required routing/setup/verification preconditions.

Browser Back/Refresh/return-from-OS behavior must never promote stale state. If current in-memory state is available, return to the truthful current logical screen. If it is lost, use `SCR-RESET-LOST` and restart routing rather than pretending persistent resume exists.

## 7. Logical screen inventory

Logical screens may be visually combined when doing so reduces friction **without** hiding state, changing requirement ownership or bypassing a required transition. Each logical screen below remains independently testable.

| Screen ID | Logical screen | User goal | TSK-0325 touchpoint | Required trace | Main exits |
| --- | --- | --- | --- | --- | --- |
| `SCR-START` | Setup start/router | Begin intentionally and choose Android, iPhone or unsupported/other. | TP-01 + TP-02 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Native safeguard; Not covered; Help; Exit. |
| `SCR-NATIVE` | Native safeguard | Set or confirm the applicable OS-native safeguard without treating confirmation as system verification. | TP-03 | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | DNS setup; Not covered/uncertain; Help; Exit. |
| `SCR-DNS-SETUP` | SafeWeb DNS setup | Perform the exact current platform-specific encrypted-DNS action. | TP-04 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Verify; Help; Remove when applicable; Exit. |
| `SCR-VERIFY` | DNS verification | Learn what current technical evidence says about SafeWeb DNS. | TP-05 | REQ-0028; REQ-0029; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Service/Map; Action needed; Status uncertain; Not covered; Help; Remove. |
| `SCR-SERVICE` | Optional service safeguard | Configure or skip zero/one currently approved relevant service without inventing another service. | TP-06 | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Protection Map; Help. |
| `SCR-MAP` | Protection Map | Review Phone / Internet / Service evidence states and limits independently. | TP-07 | REQ-0028; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Fix applicable item; Help; Remove; Exit. |
| `SCR-TROUBLESHOOT` | Action-needed troubleshooting | Understand one known evidence-backed corrective action after a supported failure. | TP-08 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Recheck only after changed condition; Remove/recovery; Help; Exit. |
| `SCR-NOT-COVERED` | Unsupported/not covered | Understand that the current combination is unsupported/out-of-scope and stop optimistic progression. | TP-13 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Compatibility; Help; Start over; Exit. |
| `SCR-UNCERTAIN` | Status uncertain | Understand that current evidence cannot safely establish protection and see the next safe check if one exists. | TP-08 + TP-13 | REQ-0028; REQ-0029; REQ-0030; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Help; recheck after changed condition; Remove; Exit. |
| `SCR-FALSE-POSITIVE` | Legitimate-content blocked help | Resolve/report an apparent false positive without confusing DNS-path verification with filtering correctness or inventing a bypass. | TP-12; TP-09/10 if removal is chosen | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Return; current approved self-service path; Remove/recovery; Exit. |
| `SCR-HELP` | Contextual help | Get source-current self-service guidance without changing journey/protection state. | TP-12 | REQ-0028; REQ-0029 where technical; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Return to exact prior logical screen; Limitations; Remove/recovery where applicable; Exit. |
| `SCR-LIMITS` | Contextual limitations | Understand current support/evidence boundary without changing journey state. | TP-13 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Return; public Compatibility; Help; Exit. |
| `SCR-REMOVE` | Remove SafeWeb DNS | Remove the exact current SafeWeb DNS configuration and withdraw the active DNS protection claim. | TP-09 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Recovery check; Help. |
| `SCR-RECOVERY` | Post-removal recovery | Confirm ordinary connectivity after removal without presenting that result as SafeWeb protection. | TP-10 | REQ-0028; REQ-0029; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | Start over; Help; Exit. |
| `SCR-RESET-LOST` | Start over / lost transient state | Return to a clean routing state when the parent intentionally resets or transient state is unavailable. | TP-11 | REQ-0028; REQ-0031; CON-0010; CON-0017; INT-0009; INT-0010 | `SCR-START`. |

No standalone “Completion” screen is mandatory. `SCR-MAP` is the truthful end-of-journey review; the parent may exit from it without an extra acknowledgement whose only purpose is ceremony.

## 8. Normal path

The canonical supported path is:

`PUB-HOME / other public page → Start setup → SCR-START → SCR-NATIVE → SCR-DNS-SETUP → SCR-VERIFY → [SCR-SERVICE when currently applicable] → SCR-MAP → Exit`

Rules:

- zero external services is valid;
- already-configured native/DNS branches may skip duplicate configuration only under TSK-0325 truth rules;
- no signup/payment/marketing screen is inserted;
- `Verified` can be rendered only from qualifying current technical evidence.

## 9. Exception-path navigation

### Already configured

`SCR-START → SCR-NATIVE (confirm/skip duplicate native setup) → [skip duplicate DNS configuration only when safe] → SCR-VERIFY → SCR-SERVICE/Map`

The navigation shortcut never bypasses verification truth.

### Unsupported / not covered

`SCR-START or later applicability check → SCR-NOT-COVERED → Compatibility / Help / Start over / Exit`

No speculative alternate client/setup path is offered.

### Failed activation / verification

`SCR-VERIFY → SCR-TROUBLESHOOT or SCR-UNCERTAIN → [changed condition] → SCR-VERIFY`

If SafeWeb configuration breaks resolution or the parent chooses rollback:

`SCR-TROUBLESHOOT/UNCERTAIN → SCR-REMOVE → SCR-RECOVERY → Start over / Help / Exit`

No unchanged-condition retry loop exists.

### False positive

`SCR-MAP or contextual Help → SCR-FALSE-POSITIVE → Return` when current service remains configured, or `→ SCR-REMOVE → SCR-RECOVERY` when removal is the safe chosen recovery.

No user-facing bypass/allowlist control is invented by this IA.

### Resume/interruption

- Help/Limitations: return to the exact prior logical screen with the same active in-memory state.
- Return from OS: resume the current setup screen only while truthful transient state exists; verification must be re-established as required by the owning state contract.
- Lost page/process state: `SCR-RESET-LOST → SCR-START`; no hidden persistent resume/account is invented.

### Removal

`SCR-MAP / troubleshooting / applicable Help → SCR-REMOVE → SCR-RECOVERY → Start over / Exit`

S6 `Removed` withdraws active SafeWeb DNS protection wording.

### Support

Any critical setup screen → `SCR-HELP` → exact prior screen. Stable reference topics may open `PUB-HELP`, `PUB-COMPAT` or `PUB-PRIVACY` when doing so reduces duplication. Returning from public reference content must not manufacture or mutate protection state.

## 10. Navigation hierarchy and back behavior

### Public

- normal browser navigation is allowed between public information pages;
- public header/footer navigation does not carry setup state;
- `Start setup` is the only primary public-to-operational transition.

### Setup

- primary task action advances only through a valid state transition;
- Help/Limitations are utility detours and return to the prior logical screen;
- browser Back must not be used as an evidence-state machine. Returning to an earlier rendered screen cannot undo an OS action or revive a stale `Verified` state;
- Start over clears web journey state only; it is separate from Remove SafeWeb DNS;
- Remove is available only when applicable, never on an untouched unsupported path;
- Exit does not claim device configuration was removed.

## 11. Information/state placement

### Allowed in public URLs

Only non-user-specific public route/locale information. No device or protection state.

### Allowed in setup URL

Generic `/setup` plus non-sensitive presentation context if a consuming framework requires it. Locale may be represented without implying identity/market activation. No parent/child/device/provider/protection/result/error identifiers.

### Allowed in active setup memory

Only the minimum transient routing/evidence state needed by the accepted journey. This IA does not create a new persistence basis.

### Forbidden architecture-level persistence assumptions

- login/session account lifecycle;
- localStorage/sessionStorage/cookie persistence merely to support resume;
- persistent child/device profile;
- journey history/status history;
- marketing identity created from setup activity.

If runtime implementation later adds persistence, it must be separately authorized by the owning data/privacy/product contracts; TSK-0328 acceptance cannot be inherited automatically.

## 12. Language and RTL navigation

EN/TR/AR are presentation variants of the **same** architecture, not separate products or market branches.

- no separate onboarding/route hierarchy by language is required by this IA;
- a language switch, if implemented, is a utility control rather than a journey step and must not create an account/persistent identity;
- `SafeWeb`, `UseSafeWeb.com`, `dns.usesafeweb.com`, and technical endpoints remain LTR/untranslated in Arabic UI;
- surrounding Arabic navigation may use RTL layout;
- logical next/back semantics and screen IDs remain identical across locales;
- language availability never implies non-UK market/legal/support activation.

## 13. Accessibility navigation requirements

- one `h1` per rendered logical screen; programmatic screen transitions focus the current `h1` under the TSK-0309/0324 contract;
- skip/navigation landmarks are semantic where applicable;
- public nav and setup utilities are keyboard-operable with visible focus;
- mobile layout must not hide Help/Limitations/Exit behind an inaccessible gesture-only control;
- state/error/help routes are reachable without mouse-only operation;
- current step/progress is not conveyed by color alone;
- no visual order may contradict keyboard/reading order;
- screen transitions, checking and error feedback preserve current accessible announcement rules.

## 14. Screen-to-goal completeness test

Every logical setup screen has exactly one primary user goal:

1. route (`SCR-START`);
2. establish native safeguard state (`SCR-NATIVE`);
3. configure DNS (`SCR-DNS-SETUP`);
4. determine DNS evidence state (`SCR-VERIFY`);
5. handle optional service (`SCR-SERVICE`);
6. understand current coverage (`SCR-MAP`);
7. repair a known failure (`SCR-TROUBLESHOOT`);
8. understand unsupported scope (`SCR-NOT-COVERED`);
9. understand unresolved evidence (`SCR-UNCERTAIN`);
10. address legitimate-content blocking (`SCR-FALSE-POSITIVE`);
11. get contextual help (`SCR-HELP`);
12. understand limits (`SCR-LIMITS`);
13. remove SafeWeb DNS (`SCR-REMOVE`);
14. recover ordinary connectivity (`SCR-RECOVERY`);
15. restart when state is intentionally reset/lost (`SCR-RESET-LOST`).

No screen exists solely to collect identity, increase page count, force an acknowledgement, upsell, or create marketing analytics.

## 15. ACC-0328 path coverage

The architecture explicitly covers all TSK-0325 required paths:

| Required path | Architecture coverage |
| --- | --- |
| Normal | Public → SCR-START → NATIVE → DNS → VERIFY → optional SERVICE → MAP. |
| Already configured | NATIVE/SETUP may skip duplicate work, but VERIFY remains truth authority. |
| Unsupported | SCR-NOT-COVERED + Compatibility/Help/Exit. |
| Failed activation | VERIFY → TROUBLESHOOT/UNCERTAIN → changed-condition recheck or REMOVE/RECOVERY. |
| False positive | MAP/Help → FALSE-POSITIVE → return or REMOVE/RECOVERY. |
| Resume | Help/Limitations state-neutral return; lost transient state → RESET-LOST. |
| Removal | REMOVE → RECOVERY → Start over/Exit. |
| Support | Any critical screen → contextual HELP → exact prior screen or stable public reference. |

## 16. Accepted source/version set

- `prototype/TSK-0325/SERVICE_BLUEPRINT.md` v1.0.0 — blob `1701f5f7b13ac8f7fa3092e39005b3da7627c89f`.
- `TSK_0318_PUBLIC_PRODUCT_SETUP_IA_DESIGN_CANDIDATE_2026-08-28.md` — blob `64f0e6382a5ce166c0aad2ad2e86a3796c5df379`; prior HUMAN_ONLY owner approval/evidence remain historical design authority for the compatible public/product split.
- `prototype/TSK-0309/BASELINE.md` v1.0.0 — blob `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`.
- `prototype/TSK-0324/UI_COMPONENT_RULES.md` v1.0.0 — blob `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`.
- `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` v1.0.0 — blob `d12c1e707f0390915002b27bf3a5073d0135d466`.
- `Plans/Master/WBS/master-wbs.csv` — blob `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.

## 17. Change control and non-inference fence

A material architecture change requires impact review when it adds/removes a current public section, setup screen, account/persistence mechanism, route-visible state, mandatory interaction, navigation path around verification, platform/service scope, recovery/removal path, language architecture or state/claim semantic.

This contract is internal L4 architecture evidence only. It does not self-certify HUMAN_ONLY `TSK-0308` or `TSK-0321`, does not prove real-parent/native-speaker comprehension, and does not authorize production implementation, public publication, participant processing, payment, market activation or launch. `RSK-0002` remains OPEN.
