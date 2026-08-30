# TSK-0146 Accountless-First Product Baseline Acceptance Evidence — 2026-08-30

## Disposition

`TSK-0146 — Freeze accountless-first product baseline and optional-account trigger`: **PASS**, subject to canonical runtime reconciliation/read-back.

This record resolves a runtime-evidence gap discovered while preflighting downstream `TSK-0333`. The WBS row carried `COMPLETED_CANDIDATE / PASS`, but `CURRENT_STATE.md` contained older statements that TSK-0146 was not current runtime PASS and no standalone TSK-0146 acceptance evidence existed. No downstream hard dependency is allowed to rely on the WBS planning snapshot alone.

## Current WBS contract

WBS blob: `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.

- task: `TSK-0146`;
- lifecycle: L4;
- priority: CRITICAL;
- dependencies: none;
- Action Authority: `AUTO_ALLOWED`;
- acceptance: product brief states no mandatory UseSafeWeb account, preserves immediate value, defines the exact future persistence/account trigger and owner authority, and supersedes the v1.4 dashboard-first mandate;
- acceptance / verification / evidence: `ACC-0146 / VER-0146 / EVD-0146`;
- requirement/interface basis: `REQ-0007; REQ-0008; CON-0001; CON-0002; INT-0003; INT-0004`.

## Current accepted source basis

Independent run `33303321786` / job `99235333227` on self-hosted runner `adguardvm` pinned and reviewed:

- minimum product scope `TSK_0141_PROVISIONAL_MINIMUM_PRODUCT_SCOPE_AND_NON_GOALS_2026-08-28.md`, blob `c72bfd906fdca4a106dcd7d4ff458a2577e32c90`;
- product brief `TSK_0140_PROVISIONAL_PRODUCT_BRIEF_CANDIDATE_2026-08-28.md`, blob `334bd2e8513d3800573e1d1e9ec569ae3ff50432`;
- accountless data contract `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`, blob `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`;
- unresolved-decisions/trigger register `TSK_0138_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-28.md`, blob `d782f26d5d48b0902b044d8bbab48569bdee0ea2`;
- requirements register blob `12c3bf6a227ad6ae61e167546a2b8a35d01321d1`;
- constraints register blob `be3eb5cd63b02d0d9f654da3040874e42cf58f6b`;
- interfaces register blob `b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c`.

The current Project Owner frozen boundary also remains accountless-first, with optional persistent account/dashboard deferred until its explicit trigger and approval.

## ACC-0146 proof

### 1. No mandatory UseSafeWeb account

Current scope explicitly defines the first product as accountless-first, requires accountless start with no mandatory UseSafeWeb login, and excludes mandatory authentication/Google sign-in/customer login from the active minimum. The accountless data contract separately prohibits mandatory account/login/email/name/stable identifiers for the immediate journey.

**Result:** SATISFIED.

### 2. Immediate value preserved

The active journey is defined to complete Phone → Internet → Services → truthful Protection Map without persistent identity, login, payment, or engagement gate. The data contract explicitly requires supported immediate completion without account creation or persistent identity.

**Result:** SATISFIED.

### 3. Exact future persistence/account trigger and owner authority

`UPA-009 / EXC-0001` defines the deferred exception. Activation requires:

1. a validated persistence, multi-device, recovery, supporter, or equivalent material need;
2. evidence that accountless alternatives are inadequate for that need;
3. privacy, security, architecture and UX review of the proposed persistent model;
4. satisfaction of the exact EXC-0001 trigger; and
5. a later explicit Project Owner decision authorizing activation.

Until then, the safe/current baseline is **no mandatory account/authentication/persistent dashboard**. `UPA-010` separately keeps a persistent parent dashboard/device list deferred and requires the same EXC-0001 evidence plus a specific dashboard necessity/minimisation case. TSK-0229 further requires a new data-contract decision if an approved EXC-0001 account model is ever activated; short-lived accountless state must not be silently repurposed into persistent history.

**Result:** SATISFIED.

### 4. Dashboard-first mandate superseded

Current product/scope/decision authorities explicitly prohibit restoring historical dashboard-first architecture by inference, keep dashboard/device-list scope deferred, and make accountless-first the active product baseline. This is the controlling current semantic baseline over any older v1.4 dashboard-first mandate.

**Result:** SATISFIED.

## Verification

Source/contract verification run/job `33303321786 / 99235333227`: SUCCESS.

Terminal markers:
- `TSK0146_WBS_AUTHORITY=PASS`;
- `TSK0146_NO_MANDATORY_ACCOUNT=PASS`;
- `TSK0146_IMMEDIATE_VALUE=PASS`;
- `TSK0146_OPTIONAL_PERSISTENCE_TRIGGER=PASS`;
- `TSK0146_OWNER_AUTHORITY=PASS`;
- `TSK0146_DASHBOARD_FIRST_SUPERSEDED=PASS`;
- `REPOSITORY_CLEAN=PASS`.

A prior diagnostic run/job `33303243964 / 99235121171` established why reconciliation was necessary: WBS showed TSK-0146 as a PASS candidate, while older runtime text explicitly said it was not current runtime PASS and no direct accepted runtime record existed.

## Acceptance conclusion

`ACC-0146` is fully satisfied by current owner/product/data/decision authority and current source evidence. `VER-0146=PASS`; `EVD-0146=SATISFIED` by this record plus the pinned verification run.

This PASS freezes the accountless-first baseline and the explicit deferred trigger/authority for any future persistence/account/dashboard. It does **not** activate EXC-0001, create an account/dashboard, authorize persistence, or imply any later lifecycle/gate/public-launch authority.