# TSK-0330 — Phone → Internet → Services Setup Flows — Candidate

**Status:** HUMAN_ONLY decision candidate; not accepted / not PASS  
**Task:** `TSK-0330 — Design Phone → Internet → Services setup flows`  
**Current sequencing:** `DEC-0052 / CR-0005`  
**Product boundary:** accountless-first; no persistent dashboard/account scope  
**Visible product identity:** `SafeWeb`

## 1. Purpose and authority

This candidate formalizes the already accepted SafeWeb critical journey into the task-specific three-layer setup contract required by TSK-0330. It does not introduce a new product direction and does not replace the owning source authorities.

Primary current sources:

- `prototype/TSK-0309/BASELINE.md` v1.0.0 — frozen implementation-ready experience baseline;
- `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` v1.0.0 — current implementation-facing device/service instruction catalogue;
- `prototype/TSK-0310/` — accepted behavioral reference, including the TSK-0321-approved accessibility remediation;
- TSK-0320 protection-state semantics as incorporated by the baseline/catalogue;
- `DEC-0052 / CR-0005` — no pre-product parent/user testing; later L8 human validation only after LG-09.

No account, child profile, persistent device list, activity history, browser/DNS history, payment step, broad DNS administration, or named external-service requirement is introduced here.

## 2. Global flow invariants

Every Phone → Internet → Services route obeys these rules:

1. **One layer never certifies another.** Phone/native safeguard, Internet/DNS, and Service are independent evidence layers.
2. **Parent confirmation is not system verification.** Parent-completed/native/service steps use `You confirmed this is set up` unless a separately approved technical verifier exists.
3. **Internet `Verified` requires current qualifying technical evidence.** Configuration presence alone is insufficient.
4. **Unsupported means stop safely.** No untested VPN/client/profile/account workaround may be invented.
5. **Already configured means skip duplicate work.** Preserve truthful state and continue only when prerequisites are known.
6. **Conflict means do not force green status.** VPN, Private Relay, browser/app resolver, managed policy, blocked encrypted DNS, captive portal, or other unproven tuples become `Action needed`, `Status uncertain`, or `Not covered` according to evidence.
7. **Removal withdraws the protection claim.** Removal/recovery yields `Removed`; plaintext/default DNS must never remain labelled protected.
8. **Zero external services is valid.** At most one separately current approved named-service instruction may be offered; currently none is hard-coded.
9. **No routine identity/data entry.** The flow needs no parent/child identity, account, payment, or diagnostic form.
10. **Help and limitations are non-destructive.** They must not silently mutate journey/evidence state.

Authorized evidence states remain exactly:

- `Verified`
- `You confirmed this is set up`
- `Action needed`
- `Status uncertain`
- `Not covered`
- `Removed`

## 3. Layer 1 — Phone

### 3.1 Entry prerequisites

The parent has selected a currently supported phone family from the router:

- Android phone on a supported route; or
- iPhone on a supported route.

If the device/platform/version/management tuple is outside current accepted support, route directly to `Not covered` / Limitations. Do not fabricate instructions.

### 3.2 Android Phone flow

**Applicability:** current supported Android phone where an approved native parental-control route is actually applicable.

1. Ask whether the relevant native safeguard is already configured.
2. If **already configured**, do not repeat setup; record `You confirmed this is set up` and continue to Internet.
3. If **setup is needed**, route only to the current Google-owned approved mechanism applicable to that exact device/account state.
4. Keep Google credential/account actions inside Google-owned surfaces; SafeWeb collects none.
5. After the parent reports completion, record `You confirmed this is set up`; do not label it `Verified` from confirmation alone.
6. If the route is unknown, managed, OEM-specific without current evidence, or prerequisites do not match, retain `Status uncertain` or `Not covered` and allow the Internet layer to proceed independently when its own prerequisites pass.

**Skip condition:** already configured and parent confirms current state.  
**Unsupported/conflict:** unknown OEM route, management restriction, unmatched version/account prerequisites.  
**Recovery/help:** show current official-platform guidance; never weaken employer/school/security controls to obtain a positive state.

### 3.3 iPhone Phone flow

**Applicability:** current supported iPhone route where Apple Screen Time / Content & Privacy Restrictions is relevant.

1. Ask whether the relevant Apple native safeguard is already configured.
2. If **already configured**, skip duplicate setup and record `You confirmed this is set up`.
3. If **setup is needed**, route to Apple’s current Screen Time / Content & Privacy Restrictions flow.
4. Keep Apple/family/account actions inside Apple-owned surfaces; SafeWeb collects no credentials.
5. After parent-reported completion, record `You confirmed this is set up`, not `Verified`.
6. If management/family/account prerequisites prevent the approved route, use `Status uncertain` or `Not covered`; do not substitute an unrelated supervision product.

**Skip condition:** already configured and parent confirms current state.  
**Unsupported/conflict:** managed/restricted/unmatched/stale route.  
**Recovery/help:** use current Apple-owned guidance without bypassing management authority.

### 3.4 Phone-layer exit

Proceed to Internet with one explicit Phone state. A non-positive Phone state does **not** block Internet setup unless the same platform condition also makes the Internet path unsupported or unsafe.

## 4. Layer 2 — Internet

### 4.1 Android Internet / SafeWeb DNS

**Prerequisites:** supported Android phone; Private DNS provider-hostname control exists and is usable; no known policy block that makes configuration unsafe or unsupported.

1. Open Android **Private DNS** using current device wording/search if needed.
2. Choose **Private DNS provider hostname**.
3. Enter exactly `dns.usesafeweb.com` — no `https://` prefix and no `:853` suffix.
4. Save using the OS-owned action.
5. Return to SafeWeb.
6. Run the approved technical verification.
7. Set Internet state:
   - `Verified` only if the qualifying technical check succeeds and no known conflict invalidates it;
   - `Action needed` when a known repair is required;
   - `Status uncertain` when evidence is inconclusive/conflicting;
   - `Not covered` when the tuple is unsupported.

**Already configured:** if the exact current SafeWeb hostname is already present, do not force re-entry; run current verification before any `Verified` state.  
**Conflict states:** VPN, browser/app custom resolver, managed policy, blocked encrypted DNS, captive portal, or unproven route.  
**Troubleshooting:** present one evidence-backed next action; retry verification only after the relevant condition changes.  
**Removal/recovery:** leave custom SafeWeb provider mode, normally restore Android `Automatic`, run neutral connectivity check, set SafeWeb Internet state to `Removed`.

### 4.2 iPhone Internet / SafeWeb DNS

**Prerequisites:** supported iPhone/iOS route; exact separately verified SafeWeb DNS profile artifact is available; local/manual profile installation is allowed; device is not management-blocked.

1. Deliver only the exact separately verified SafeWeb DNS profile artifact.
2. Let iOS show the profile and request explicit user installation permission.
3. The profile must use exactly `https://dns.usesafeweb.com/dns-query`.
4. Complete the iOS-owned installation flow; SafeWeb must not claim silent/background installation.
5. Return to SafeWeb.
6. Run the approved technical verification.
7. Set Internet state using the same evidence rules as Android: `Verified`, `Action needed`, `Status uncertain`, or `Not covered`.

**Already configured:** profile presence alone does not establish `Verified`; re-run the approved technical check.  
**Conflict states:** VPN, Private Relay, custom resolver, managed restriction, network conflict, profile-only evidence, or unknown profile ownership.  
**Troubleshooting:** give one source-backed next action; never imply a green state from installation alone.  
**Removal/recovery:** remove the exact SafeWeb profile under current iOS profile-management flow, run neutral connectivity check, set Internet state to `Removed`; if device/profile is management-owned, stop and follow that authority.

### 4.3 Unsupported Internet route

If the platform/device/network/profile tuple is outside current support:

- show `Not covered` with a concise reason;
- provide Limitations/Help only;
- do not offer speculative setup steps;
- do not offer SafeWeb removal if SafeWeb was never configured through this journey.

## 5. Layer 3 — Services

### 5.1 Entry rule

Service protection is optional and bounded. Build the selectable set only from separately current approved named-service instruction records.

Current catalogue state: **no named external service is hard-coded**.

### 5.2 Service flow

1. Determine whether a currently approved supported named-service record exists.
2. If none exists, skip service setup and represent the Service layer as `Not covered` or the baseline’s explicit no-applicable-service outcome; do not manufacture a provider recommendation.
3. If one or more approved records exist in the future, ask only which **one** currently supported service is actually used/planned; zero remains valid.
4. Present at most one service instruction.
5. Keep provider credentials/account actions inside provider-owned surfaces.
6. Parent-reported completion is `You confirmed this is set up` unless a future separately approved technical verifier exists.
7. Stale/ambiguous provider guidance becomes `Status uncertain`; unsupported provider/service becomes `Not covered`.

**Skip condition:** zero relevant approved services.  
**Unsupported:** no current approved named-service record, unsupported provider/account/region/version, or stale source.  
**Troubleshooting:** use current provider-owned guidance only; never infer service use from browsing/DNS/app history.

## 6. Protection Map completion

After the three layers, show a Protection Map with Phone / Internet / Service independently.

Completion rules:

- no overall safety score;
- no `100% safe`, `fully protected`, certification, or equivalent claim;
- `Verified` may appear only on a layer with qualifying current system evidence;
- parent-confirmed layers remain visibly distinct;
- `Action needed`, `Status uncertain`, and `Not covered` remain visible rather than being hidden to create a success screen;
- Service `Not covered` is a valid completed journey outcome when no approved relevant service exists;
- a journey can complete with mixed layer states while remaining truthful about gaps.

## 7. Back, resume, Help, Limitations and reset behavior

- **Back:** returns to the prior appropriate screen without silently upgrading/downgrading an evidence state.
- **Resume within current journey:** restore only the in-memory journey state already authorized by the accountless baseline; no persistent identity/device profile is introduced.
- **Help:** return to the originating screen/state after assistance unless the user explicitly chooses another recovery/removal action.
- **Limitations:** informational only; does not mutate protection evidence.
- **Reset / Start over:** returns to Discovery and clears in-memory journey state; it does not itself alter OS settings.
- **Removal:** is a deliberate OS/profile change and must be completed separately before state becomes `Removed`.

## 8. Deterministic branch matrix

| Test ID | Branch | Expected outcome |
| --- | --- | --- |
| `TC-0330-01` | Android normal | Phone parent-confirmed → Android Private DNS exact hostname → qualifying technical verify → Service skip/no approved service → mixed truthful Protection Map. |
| `TC-0330-02` | iPhone normal | Phone parent-confirmed → exact approved DoH profile flow → qualifying technical verify → Service skip/no approved service → mixed truthful Protection Map. |
| `TC-0330-03` | Phone already configured | Native setup skipped; state remains parent-confirmed, not system-verified. |
| `TC-0330-04` | Android DNS already configured | No forced re-entry; technical re-verification required before `Verified`. |
| `TC-0330-05` | iPhone profile already present | Profile presence does not equal `Verified`; technical re-verification required. |
| `TC-0330-06` | Unsupported phone | Route to `Not covered`/Limitations; no speculative setup. |
| `TC-0330-07` | DNS conflict | Use `Action needed` or `Status uncertain`; one safe next action; bounded retry only after changed condition. |
| `TC-0330-08` | Managed/restricted device | Do not bypass management authority; use `Status uncertain` / `Not covered` as evidence requires. |
| `TC-0330-09` | Zero relevant service | Skip service setup; no provider invented; completed journey remains valid. |
| `TC-0330-10` | Future one approved service | At most one instruction; parent confirmation remains distinct from system verification. |
| `TC-0330-11` | Removal/recovery | Remove exact SafeWeb DNS config/profile; neutral connectivity check; Internet state `Removed`; no residual protection claim. |
| `TC-0330-12` | Help/Limitations/back/reset | Navigation does not corrupt evidence state; reset clears journey state without altering OS settings. |

## 9. Acceptance mapping

TSK-0330 acceptance requires every flow to include prerequisites, step-by-step actions, verification/confirmation, skip conditions, unsupported/conflict states, troubleshooting, and no misleading completion state.

This candidate maps those requirements as follows:

- **Prerequisites:** §§3.1, 4.1, 4.2, 5.1;
- **step-by-step actions:** §§3.2–3.3, 4.1–4.2, 5.2;
- **verification/confirmation:** §§2–6;
- **skip conditions / already configured:** §§3.2–3.3, 4.1–4.2, 5.2;
- **unsupported/conflict states:** §§3–5;
- **troubleshooting/recovery:** §§3–5 and §7;
- **truthful completion:** §6;
- **representative deterministic tests:** §8.

## 10. HUMAN_ONLY decision boundary

This file is a prepared candidate only. It does not mark TSK-0330 PASS and does not claim Project Owner approval.

Recommended owner disposition after verification:

`APPROVE TSK-0330 PHONE INTERNET SERVICES FLOWS`

Alternative:

`REVISE TSK-0330: <specific change>`

Only an explicit owner disposition may close the HUMAN_ONLY boundary. Approval does not authorize L5/L6, real-user testing, publication, launch, account/dashboard scope, or any unrelated consequential action.