# TSK-0043 — Post-CR-0006 Cross-Functional Requirements Review

**Task:** `TSK-0043`  
**Acceptance:** `ACC-0043`  
**Authority:** `DEC-0053 / CR-0006`, `DEC-0054 / CR-0007`  
**Date:** 2026-09-01  
**Disposition:** candidate current review pending independent verification/stable-state reconciliation.

## Sources reviewed

Current canonical requirements/WBS and change authority were reviewed together with the accepted post-change L4 evidence for TSK-0141, TSK-0146, TSK-0229, TSK-0312, TSK-0333 and TSK-0321. Historical account-exclusion wording is treated as superseded where CR-0006 changed acceptance.

## Critical contradiction review

| Class | Current resolution | Critical conflict |
| --- | --- | --- |
| Accountless core vs optional account | Core safety setup/protection/removal remains fully usable without login; account is optional continuity/management. | None |
| Optional account vs privacy minimisation | Persistent identity/device ownership is limited to the minimum account domain; browsing/query/activity history and child profiles remain excluded. | None |
| Anonymous state vs persistent account | J0/J1 remains short-lived/separate; no automatic import/link/promotion/expiry extension on sign-in. | None |
| Account/device ownership vs protection truth | Ownership/saved-device state never creates `Verified`; current technical evidence remains required. | None |
| Dashboard/device management vs broad DNS administration | Dashboard is lightweight lifecycle/continuity management; unrestricted/raw AdGuard/DNS administration remains excluded. | None |
| Account deletion vs DNS/device removal | Account deletion, device-record deletion/revoke, anonymous-state deletion and physical DNS removal are distinct operations with distinct truth states. | None |
| Destructive operations vs reliability | Unknown destructive-operation result is reconciled; no blind automatic replay. | None |
| Authentication UX vs provider/security architecture | L4 defines required product states; exact Google/Firebase vendor/privacy/session/token/datastore controls remain downstream L5–L7 acceptance. | None |
| Accessibility vs responsive/account expansion | Final no-overlay TSK-0321 review passes focused 320px/200% reflow, full TSK-0333 Chromium regression and the full current mechanical accessibility suite. | None |
| Self-service vs account lifecycle | Ordinary sign-in/session/dashboard/device/deletion/recovery problems have self-service paths; human/operator route remains exceptional and criterion-driven. | None |
| Integrated-product-first sequencing vs user evidence | CR-0005 excludes pre-L8 human/user validation; no behavioral validation is inferred from internal/automated L4 acceptance. | None |
| CR-0007 autonomy vs retained authority | Objective in-scope work/gates may be automatic when evidence-complete; material scope/market/contract/identity/nondelegable boundaries remain separately controlled. | None |

## Noncritical items

1. **NCF-0043-01 — legacy `G-04` wording.** Where ACC-0043 retains legacy `G-04`, resolve it through the current canonical gate mapping rather than treating it as a second gate authority. Owner: planning/governance authority. Due: whenever affected gate text is next materially amended.
2. **NCF-0043-02 — historical pre-CR-0006 artifacts.** Historical accountless-only artifacts may remain for provenance but must not be used as current acceptance where CR-0006 changed scope. Owner: task/evidence verifier. Due: at each affected successor/gate evaluation; current TSK-0309 and TSK-0628 requalification explicitly addresses this.

Neither item changes product scope or creates a critical contradiction.

## Review outcome

Current review identifies **0 unresolved critical requirement conflicts**. Remaining noncritical interpretation items have explicit owners and deterministic gate/change-relative due conditions. Current requirements do not contradict the frozen dual-mode Version-1 scope, privacy-minimisation boundary, accountless-core guarantee, current gate/action authority, or the integrated-product-first sequencing rule.

This review does not itself make TSK-0043 or LG-06 PASS and does not infer provider/privacy/security architecture, implementation, real-user validation, legal completion, release, production activation, publication, payment or launch.