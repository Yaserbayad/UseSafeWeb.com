# TSK-0042 — User support, exception, recovery and removal requirements verification evidence

**Task:** TSK-0042 — Specify user support, exception, recovery, and removal requirements  
**Acceptance:** ACC-0042  
**Verification:** VER-0042 independent guarded requirements/authority/evidence audit  
**Evidence:** EVD-0042  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## 1. Exact evidence index

- Requirements contract: `TSK_0042_USER_SUPPORT_EXCEPTION_RECOVERY_REMOVAL_REQUIREMENTS_2026-08-28.md`
- Contract blob: `bf9e1ece69b5ccfc38c1cb44d69de6545b7865dc`
- Contract creation commit: `7e4030e26ed188a4649ed06904c1a183289b5b63`
- Current WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Current selection workflow: `.github/workflows/select-tsk0042.yml`, blob `84b18e8a31da927a97c0dd4b2caf36657cb55a2c`
- Selection workflow run: `33192484731` — completed successfully; it directly parsed the current WBS row and asserted TSK-0042 lifecycle/priority/authority/dependencies/ACC text before selecting it in `CURRENT_STATE.md`.
- DEC-0042 source: `Plans/Master/Registers/DECISIONS_TRIGGERS.md` — accountless-first active owner decision.
- EXC-0001/EXC-0008 source: `Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md`, blob `20a4e9727e888539d05436a1f4a91f886f83ab04`.
- INT-0001/INT-0002 source: `Plans/Master/Registers/INTERFACES.md` — canonical baseline/eligibility and acceptance/gate evidence contracts.
- TSK-0041 DNS activation contract: blob `95a5292223f1d2c3c8f79d4c889ad91e917478b2`.
- TSK-0041 independent evidence: blob `66cdc50ae2fbb9ec4501b408837d01aafcba876d`.
- TSK-0229 accountless journey data contract: blob `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`.
- TSK-0409 supported OS/device/network matrix: blob `09318534ec097849cbe8c7391e2a1acc3ba5a79a`.
- TSK-0320 protection-state contract: blob `1146f7622f434590dde1253d11f14fb6a87e19de`.
- Existing support/false-positive intake: `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`, blob `9fab42f97e3e96023de89a8ed266acc21c0f06ab`.
- Exceptional diagnostic logging procedure: blob `f9e1bb52582a69bc385aa69c93d02febb7b5cffa`.
- Child-safety escalation procedure: blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`.
- TSK-0511 supported-device completion evidence: blob `ecd959f93ab7dff62aba6529ce66b45d59c3ed27`.
- TSK-0514 external endpoint/removal evidence: blob `c5d004d0e0a8c58d1056b3aaad38034ae4188a68`.
- TSK-0512 filtering regression evidence: blob `cc21f4574a2ca7e721a7da961baef727350af1d3`.
- TSK-0207 privacy-persistence evidence: blob `1c16db063e2e84d300b547075721d33c2e020e32`.

## 2. Eligibility / authority audit

The current authoritative runtime selects TSK-0042 as the highest eligible provisional-L4 AUTO_ALLOWED task after TSK-0313. The selection workflow directly inspected the current WBS and asserted:

- `Lifecycle_Stage = L4`;
- `Priority = MEDIUM`;
- `AI_Capability_A0_A4 = A3`;
- `Action_Authority = AUTO_ALLOWED`;
- hard dependencies exactly `TSK-0041; TSK-0146`;
- ACC-0042 contains the accountless support/recovery domains and the explicit EXC-0001 account-access exclusion.

The same runtime records both direct predecessors as current PASS. TSK-0187 remains ineligible because it requires representative-parent evidence; TSK-0140 remains human-review-bound. No owner decision, participant act, legal attestation, build/release act or account-scope activation is needed to define this bounded internal requirements contract.

## 3. Single-authority / non-duplication audit

The contract does not create competing mutable authorities:

- DEC-0042 remains owner of accountless-first product direction.
- EXC-0001 remains owner of any future account/auth/dashboard activation condition.
- EXC-0008 remains owner of any future routine staffed-support activation condition.
- TSK-0229 remains owner of J0/J1 data, expiry, deletion and no-linkage semantics.
- TSK-0041/TSK-0409 remain owner of current DNS activation and supported/conflict behavior.
- TSK-0320 remains owner of Protection Map truth states.
- The existing false-positive, exceptional-diagnostic and safeguarding procedures remain operational owners of their specialized processes.
- TSK-0042 only defines the cross-domain product/support requirements that consume those authorities.

No new account store, support-ticket database, per-user allowlist, diagnostic dataset, DNS truth model or safeguarding procedure is created.

## 4. ACC-0042 clause-by-clause audit

ACC-0042 requires:

> Requirements identify accountless setup/journey-state recovery, device-configuration lifecycle, AdGuard/DNS integration, false-positive and unsupported-state incidents; remedies, escalation, data-minimising diagnostics, response expectations, deletion/removal/recovery and support-burden metrics are explicit. Account-access requirements remain excluded unless EXC-0001 is activated.

| ACC-0042 requirement | Contract proof | Audit result |
| --- | --- | --- |
| Accountless setup/journey-state recovery | §§2 and 5 define no-login support, J0 loss/reset behavior, J1 valid/expired/deleted behavior, restart without identity recovery and no retention extension for troubleshooting. | PASS |
| Device-configuration lifecycle | §6 defines not-configured, configured-unverified, verified, conflict/uncertain, unsupported, removal-in-progress, removed and recovery-verified states. | PASS |
| AdGuard/DNS integration incidents | §7 consumes TSK-0041/0409, preserves Android DoT vs iPhone DoH mechanisms and enumerates endpoint/TLS/filtering/service/resolver/conflict/stale/removal failure classes. | PASS |
| False-positive incidents | §8 requires low-data/synthetic reproduction where possible, causality, narrow reversible exception, allowed + blocked regression and truthful state update. | PASS |
| Unsupported-state incidents | §9 covers VPN, Private Relay, custom DNS, captive portal, managed devices/networks, transport blocking, IPv6-only/NAT64 and other matrix limitations without invented coexistence. | PASS |
| Remedies | §§4, 7–9 and 13 require one bounded repair/recheck, explicit unsupported result, or removal/recovery rather than generic retry/optimistic success. | PASS |
| Escalation | §§4, 10 and 11 separate ordinary support, exceptional diagnostics, privacy/security and safeguarding escalation. | PASS |
| Data-minimising diagnostics | §10 preserves the least-data hierarchy and delegates exceptional logging to the accepted TSK-0227 procedure with necessity/scope/time/access/approval/deletion controls. | PASS |
| Response expectations | §12 defines deterministic S1–S4 product/system response behavior while explicitly refusing to fabricate a human SLA under deferred EXC-0008. | PASS |
| Deletion/removal/recovery | §13 binds J0/J1 deletion, exceptional-diagnostic deletion verification and platform-specific Android/iPhone DNS removal/recovery. | PASS |
| Support-burden metrics | §14 defines issue incidence, self-service resolution, human assistance, assistance minutes, blocking/unsupported/false-positive/removal/recovery/diagnostic/escalation/staleness metrics with privacy constraints and no current behavioral result claim. | PASS |
| Account-access exclusion | §§2, 16 and 18 prohibit account/login/password recovery/auth/dashboard requirements unless EXC-0001 is legitimately activated. | PASS |

All ACC-0042 clauses are explicit and independently testable.

## 5. Contradiction / safety audit

### Accountless baseline

DEC-0042 states no mandatory UseSafeWeb account and optional account only after validated need and approval. EXC-0001 adds the specific trigger and current prohibition. The contract is strictly narrower: it treats missing/expired journey state as a restart/recovery problem, never as a reason to introduce authentication.

### Routine staffed support

EXC-0008 keeps routine staffed customer support deferred. Therefore ACC-0042's “response expectations” cannot legitimately be interpreted as a public human-response SLA. The contract instead defines deterministic product/system responses by severity and only uses human escalation where an existing specialized procedure/authority requires it. This is the conservative interpretation consistent with current owner authority.

### DNS/support truth

TSK-0041 already proves the current product requirements must preserve Apple DoH versus Android native DoT, current verification before positive state, truthful conflict handling, narrow false-positive remediation, no-history diagnostics and removal/recovery. TSK-0042 consumes those requirements without widening support claims.

### Diagnostic privacy

The exceptional diagnostic procedure explicitly keeps persistent identifiable query logging off by default and requires a concrete incident, necessity, exact fields, fixed time window, restricted storage/access, approver and deletion verification before closure. TSK-0042 makes that procedure the only exceptional request-level diagnostic path rather than adding a weaker alternative.

### Safeguarding

The child-safety procedure explicitly separates UseSafeWeb product support from emergency/safeguarding investigation. TSK-0042 routes safeguarding out of product troubleshooting and stores no raw disclosure in GitHub/analytics.

## 6. Behavioral-evidence boundary

`RSK-0002` remains OPEN. The contract deliberately does not claim:

- representative parents can self-serve successfully;
- the real support issue rate is low;
- human-assistance minutes are acceptable;
- false-positive/compatibility burden is acceptable in the target cohort;
- the proposed support copy/sequence is comprehended or preferred;
- a staffed-support model is unnecessary forever.

Section 14 defines future privacy-minimal metrics so those unknowns can be measured when the relevant behavioral gate is authorized. Synthetic/internal tests may validate taxonomy/routing/recovery/instrumentation logic only.

## 7. Verification disposition

**VER-0042 independent guarded audit result: PASS.**

ACC-0042 is fully satisfied by the read-back contract at blob `bf9e1ece69b5ccfc38c1cb44d69de6545b7865dc`. No current contrary authority or direct evidence was found that invalidates the contract. The result remains bounded to provisional internal L4 requirements under DEC-0050/CR-0003 and does not authorize LG-05/LG-06, implementation/build, participants, legal completion, payment, publication or launch.

**Runtime state may move TSK-0042 to PASS only after this evidence file is itself persisted/read back and the reconciliation write verifies exact current blobs/preconditions.**
