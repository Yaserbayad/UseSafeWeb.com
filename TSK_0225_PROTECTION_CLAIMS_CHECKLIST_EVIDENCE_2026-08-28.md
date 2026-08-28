# TSK-0225 — Protection Claims Checklist Evidence

**Task:** TSK-0225  
**Acceptance:** ACC-0225  
**Evidence date:** 2026-08-28  
**Result:** PASS

## Authority and dependency proof

The exact canonical WBS row defines TSK-0225 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0219`. ACC-0225 requires a checklist that tests protected/confirmed/action-needed/not-covered distinctions, DNS limits, app/VPN/Private Relay limits, and removal/exception handling.

Historical/planning predecessor labels were not accepted by themselves.

- `TSK-0224`, the predecessor of TSK-0219, was directly re-proven from current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, including the current retention boundaries.
- `TSK-0219` was directly re-proven from current `PILOT_PRIVACY_NOTICE.md`, blob `331f263388dfacfa73b6e9e556277d4230864ce8`: it contains separate parent and child-readable sections, expressly rejects complete-safety claims, forbids a generic unverified “no logs” claim, and contains explicit release conditions before participant use.

## Accepted artifact

`PROTECTION_CLAIMS_CHECKLIST.md`, blob `4bfc83421318fe761d06f9a63e052e3bff36070a`.

ACC-0225 mapping:

1. **Truth states:** `Protected — verified`, `Configured — parent confirmed`, `Action needed`, and `Not covered` are defined separately; parent confirmation cannot become technical verification.
2. **DNS limits:** the checklist limits DNS claims to domain-resolution behavior and explicitly excludes complete-device/in-app safety inference.
3. **App/native-service limits:** native Apple/Google/app/service controls remain separate layers and are never implied by DNS activation.
4. **VPN/alternate-DNS/Private Relay limits:** ambiguous or bypassed network paths force re-verification or downgrade to `Action needed`/`Not covered`.
5. **Removal/recovery:** supported paths require clear removal and recovery; unavailable recovery blocks activation/claiming for that path.
6. **Exceptions/false positives:** exceptions must be narrow, explainable, reversible, tested, and must not silently disable the baseline.
7. **Evidence/fail-safe behavior:** verified claims require current evidence; unsupported or ambiguous states are shown rather than hidden; child browsing/domain history is not required to prove claims.

## Independent verification

Initial audit run `33153150939` / job `98789641926` was **not accepted** because the verifier compared an unformatted literal against Markdown-emphasised child-notice text. It failed before any state/artifact mutation.

The verifier was corrected to normalize Markdown emphasis only; no product artifact or acceptance requirement changed.

Corrected GitHub Actions run `33153183138`, job `98789746523`, completed successfully on the repository-scoped `adguardvm` runner with exact `main` checkout, `contents: read`, and no persisted checkout credentials.

Corrected audit output:

- `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`
- `TSK_0219_DIRECT_PREDECESSOR_PROOF=PASS`
- `TSK_0225_ACCEPTANCE_CLASSES=7/7`
- `TSK_0225_ARTIFACT_BLOB=4bfc83421318fe761d06f9a63e052e3bff36070a`
- `TSK_0225_INDEPENDENT_AUDIT=PASS`

## Boundary

This PASS verifies a pre-experiment protection-claims checklist only. It does not prove that any real device is protected, does not authorise recruitment or participant processing, and does not change the unresolved validation-readiness/legal/provider gates.
