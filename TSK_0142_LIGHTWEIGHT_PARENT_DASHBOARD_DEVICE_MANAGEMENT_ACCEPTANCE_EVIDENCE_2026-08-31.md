# TSK-0142 — Dashboard / Device-Management Acceptance Evidence

**Task:** TSK-0142 — Specify lightweight parent dashboard and device-management requirements  
**Acceptance:** ACC-0142  
**Verification:** VER-0142  
**Evidence:** EVD-0142  
**Date:** 2026-08-31  
**Verifier:** Governed post-publication analytical verification, separate from artifact authoring  
**Result:** PASS CANDIDATE PENDING DETERMINISTIC VERIFICATION AND RUNTIME RECONCILIATION

## 1. Exact artifact under review

- Path: `TSK_0142_LIGHTWEIGHT_PARENT_DASHBOARD_DEVICE_MANAGEMENT_REQUIREMENTS_2026-08-31.md`
- Version: `1.0.0`
- Blob read back from `main`: `77b432e9d06741d0d303de2c2a2524e804cdcf5e`
- Publication commit: `9c8ffc1c933c67861f7549c6caee12f77af0ad7a`

## 2. Eligibility and dependency review

Current WBS `f3c29b5db8b835ef2c896f61335656ea51d8ba1c` defines TSK-0142 as L4, PLANNED/WAITING snapshot, priority MEDIUM, non-critical-path, A3 / `AUTO_ALLOWED`, hard dependencies `TSK-0312; TSK-0041`, ACC-0142 / VER-0142 / EVD-0142.

Post-TSK-0312 queue inspection run/job `33398137149 / 99507545395` confirmed the exact current row and both dependency identifiers.

- `TSK-0312` is current runtime PASS in `CURRENT_STATE.md`, runtime blob `bc95bd395097ace6ab93e368d10812aeeef5fc0f`, with deterministic verifier run/job `33397888358 / 99506708568`.
- `TSK-0041` remains an accepted stable L4 DNS-activation requirements contract. Its relevant acceptance semantics — exact supported activation, current technical verification for DNS S1, conflicts/uncertainty, removal/recovery, narrow false-positive handling and no-history privacy — are unchanged by CR-0006/CR-0007. Optional account/dashboard scope does not alter the DNS endpoint/verification truth and this TSK-0142 artifact does not reuse TSK-0041’s former accountless-only persistence limitation to prohibit the newly authorized dashboard.

**Eligibility result:** PASS. Both hard dependencies currently supply compatible evidence; task authority is AUTO_ALLOWED; no retained human act is required to define this bounded internal product requirement.

## 3. Exact ACC-0142

Current ACC-0142 requires:

> Requirements define parent device list/nickname, add/setup/verify/reinstall/replace/revoke/remove, truthful protection status, Protection Map, curated controls, help and account lifecycle; browsing/query/activity history and unrestricted DNS administration are explicit non-goals.

## 4. Clause-by-clause acceptance review

| ACC-0142 clause | Persisted artifact evidence | Result |
| --- | --- | --- |
| Parent device list | Sections 4–5 define a minimum device-record model and the minimum list presentation. | PASS |
| Device nickname | Section 4 defines parent-chosen nickname/generic default, rename behavior and no required child identity. | PASS |
| Add | DEV-01 defines explicit Add device, supported routing, no silent J0/J1 linkage and no verification inference from record creation. | PASS |
| Setup / continue setup | DEV-02 requires supported Phone → Internet → Service/Protection Map flow and no verification bypass because the record exists. | PASS |
| Verify / re-verify | DEV-03 requires current owning verifier semantics, current-evidence state updates, downgrade on contradiction and no browsing-history dependency. | PASS |
| Reinstall / reconfigure | DEV-04 defines current supported route and withdrawal of stale optimistic state until qualifying evidence returns. | PASS |
| Replace | DEV-05 prevents inheritance of prior S1/S2/history and requires separately approved transfer rules. | PASS |
| Revoke | DEV-06 defines revoke/unlink as ending account management/ownership association, fail-closed uncertainty, and explicitly separates it from physical DNS removal. | PASS |
| Remove protection | DEV-07 routes to current physical removal semantics and uses S6 only with owning evidence/confirmation. | PASS |
| Remove dashboard record | DEV-08 defines record deletion independently from physical DNS/configuration removal. | PASS |
| Truthful protection status | Section 6 requires S1–S6 evidence strength, currentness/freshness, downgrade on contradiction and no ownership-as-verification. | PASS |
| Protection Map | Section 6 explicitly retains TSK-0320/TSK-0313 evidence-state semantics across Phone/Internet/Services while reconciling CR-0006 persistence scope. | PASS |
| Curated controls | Section 8 provides the bounded allowed surface; Section 9 excludes raw DNS administration/filter/upstream/log/history controls. | PASS |
| Help | Section 10 defines privacy-minimal self-service routes for setup, verification, uncertainty, unsupported states, false positives, auth/session, removal and deletion. | PASS |
| Account lifecycle | Section 11 defines logout/session expiry/revocation/account deletion and separates account/device/J0-J1/DNS-removal operations. | PASS |
| Browsing/query/activity history explicit non-goal | Sections 2, 5, 9 and 13 explicitly prohibit history/top-domain/activity surfaces and data requirements. | PASS |
| Unrestricted DNS administration explicit non-goal | Sections 1, 8 and 9 prohibit raw AdGuard administration/credentials, upstream/filter-list/query-log/broad allow-block controls. | PASS |

## 5. Product-scope / CR-0006 reconciliation

The artifact correctly implements the bounded Version-1 scope:

- accountless core remains fully usable without login;
- optional account provides minimum continuity/device management;
- device ownership is account management state, not technical protection evidence;
- no mandatory login, child account/profile, browsing history or broad DNS administration is introduced;
- no new payment/paywall or surveillance scope is introduced.

No material scope expansion requiring owner action was found.

## 6. TSK-0312 account/session reconciliation

The dashboard consumes rather than duplicates TSK-0312:

- valid session is required only for dashboard/account-only functions;
- logout/session expiry/revocation denies account-only access without claiming DNS removal;
- account deletion is distinct from device-record deletion, anonymous J0/J1 deletion and physical DNS removal;
- no local password or SMS flow is introduced;
- no silent anonymous-to-account linkage is introduced.

No contradiction with current TSK-0312 was found.

## 7. TSK-0041 DNS activation compatibility

The current dashboard contract preserves all acceptance-relevant TSK-0041 semantics:

- exact supported platform activation remains separately authoritative;
- configuration/dashboard record presence never creates DNS S1;
- current qualifying system verification is required for DNS S1;
- VPN/Private Relay/browser/network uncertainty produces uncertain/not-covered/action states according to owning evidence;
- removal/recovery remains explicit and reversible;
- false positives use narrow controlled handling rather than broad filter disablement;
- routine verification/support does not require persistent browsing history;
- current no broad/per-device persistent allowlist assumption remains a dashboard non-goal.

CR-0006’s optional account/dashboard decision does not invalidate these DNS truth requirements. **Dependency compatibility: PASS.**

## 8. Protection Map / state-contract reconciliation

TSK-0320 blob `1146f7622f434590dde1253d11f14fb6a87e19de` and TSK-0313 blob `521c9cc5073aa289281acade12a66a9e979e197d` were inspected.

The artifact retains:

- S1 Verified only from current qualifying system evidence;
- S2 parent-confirmed without masquerading as system verification;
- S3 Action needed;
- S4 Not covered;
- S5 Status uncertain/error, including stale/conflicting evidence;
- S6 Removed;
- independent Phone/Internet/Services layers with no aggregate safety score;
- re-verification on material evidence-context change;
- no browsing/history requirement.

The only superseded pre-CR-0006 clause is the absolute absence of any account/dashboard/device registry. DEC-0053 expressly authorizes the minimum persistent account/device domain. The artifact makes this scope delta explicit rather than treating the old persistence prohibition as current authority. No weaker evidence threshold is introduced.

## 9. TSK-0229 data-separation review

The artifact preserves TSK-0229 blob `2955c2762e726f95ec67c33b9abbc5e4b25cb84a`:

- no automatic J0/J1-to-account/device promotion/linkage;
- account activity does not extend anonymous expiry;
- future transfer requires an approved downstream field-level data-flow contract;
- dashboard state never includes browsing/query/activity history;
- device record deletion/account deletion/anonymous deletion/DNS removal remain distinct.

**No-linkage compatibility: PASS.**

## 10. Currentness and stale-status review

A dashboard creates a new risk absent from the original accountless-only model: old positive status can look current. The artifact explicitly controls that risk by requiring evidence actor/currentness/freshness, preserving owning re-verification triggers, permitting historical “last verified” presentation when currentness is unknown, and requiring downgrade to S3/S5/etc. on contradictory/stale evidence. It explicitly refuses to invent a universal verification TTL.

This satisfies truthful-status acceptance without pre-deciding L5 persistence/storage implementation.

## 11. Data-minimisation and security review

The minimum semantic device record is bounded to ownership, nickname/generic label, supported routing context, lifecycle and only the status/evidence metadata necessary for approved device management. It excludes child identity as a requirement, device fingerprinting beyond necessary supported context, browsing/query/activity history, raw DNS admin credentials and broad filter/upstream/log controls.

Authorization/schema/storage/retention/backups remain downstream. No implementation/security pass is inferred.

## 12. Help/account lifecycle/accessibility/localization review

The artifact provides objective self-service outcomes and explicit error classes; inherits WCAG 2.2 AA/mobile-first requirements; requires non-color status distinctions; and preserves English/Turkish/Arabic + RTL technical capability without claiming official non-UK market activation. Real-user comprehension remains unproven until L8.

## 13. Test-case review

The artifact defines `DASH-T01` through `DASH-T20`, covering:

- login-free core;
- empty/add/rename device;
- configuration-vs-verification truth;
- S1/S2/S3/S4/S5/S6 behavior;
- reinstall/reconfigure/replace;
- revoke/unlink versus DNS removal;
- physical removal versus record deletion;
- logout/session/account deletion;
- no browsing/history;
- no raw DNS admin;
- multilingual/RTL/accessibility/non-color semantics.

These are objective/synthetic acceptance inputs and do not fabricate pre-L8 human evidence.

## 14. Contrary-evidence review

No current canonical source inspected contradicts the artifact’s bounded dashboard requirements. In particular, it does not:

- reuse stale accountless-only “no dashboard ever” text against CR-0006;
- weaken S1/S2 evidence semantics;
- treat account ownership/history as technical verification;
- create browsing/query/activity history;
- expose unrestricted/raw AdGuard administration;
- introduce a per-device personalized allowlist;
- make login mandatory;
- infer provider/schema/security/build/legal/privacy/LG-06 acceptance.

## 15. Analytical disposition

Every explicit ACC-0142 dimension is present in the exact persisted artifact, both hard dependencies are current and compatible for the facts consumed, and the CR-0006 persistence change is reconciled without weakening DNS or Protection Map truth.

**Analytical result: ACC-0142 PASS candidate.**

TSK-0142 shall remain non-PASS until a separate deterministic verification of the exact current artifact/dependencies succeeds and that result is durably persisted/read back before runtime reconciliation.
