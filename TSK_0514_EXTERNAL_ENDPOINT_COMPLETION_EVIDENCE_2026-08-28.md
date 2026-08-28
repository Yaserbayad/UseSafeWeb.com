# TSK-0514 — External Endpoint and Target-Device Completion Evidence

**Task:** TSK-0514 — Verify the endpoint from external networks and target devices  
**Verification:** VER-0514  
**Evidence:** EVD-0514  
**Acceptance:** ACC-0514  
**Date:** 2026-08-28  
**Environment:** already-supported real phone; qualifying external cellular network; UseSafeWeb encrypted-DNS configuration followed by removal/reset

## Authoritative acceptance contract

ACC-0514 requires: **All target tests pass; network-specific failures are recorded; removing the profile/config restores normal DNS behavior.**

The existing preflight evidence also binds this task to:

- `REQ-0066`: verification from at least one network outside Azure and outside the operator's normal network before pilot approval;
- `REQ-0069`: a verified removal/recovery path that restores normal DNS behavior;
- `CON-0023`: privacy-minimised evidence without unnecessary browsing/content capture;
- `VER-0514`: direct target-system external observation on the supported client/network path.

Preflight: `TSK_0514_EXTERNAL_ENDPOINT_PREFLIGHT_EVIDENCE_2026-08-28.md`, blob `fa30c43920e13f72873f49f0cb90b47430913465`.

## Direct owner observation

On 2026-08-28 the Project Owner supplied the two previously missing privacy-safe observations:

1. **External cellular test: PASS.** The already-supported real phone successfully used UseSafeWeb while on a qualifying external cellular network. No network-specific failure was reported.
2. **Removal/recovery test: PASS.** After removing/resetting UseSafeWeb, normal DNS/internet resolution worked again.

The observation intentionally records only the network class and pass/fail outcomes. No browsing history, DNS history, domain history, screenshot, device identifier, participant identity, or other personal content is retained.

## Acceptance evaluation

- External supported-client/network behavior: **PASS**.
- `REQ-0066` qualifying external-network condition: **PASS**.
- Network-specific failures: **none reported**.
- Removal/reset recovery to normal DNS behavior: **PASS**.
- `REQ-0069` removal/recovery condition: **PASS**.
- Privacy-minimised evidence boundary: **PASS**.

The prior accepted TSK-0442 evidence remains the server-side/real-phone encrypted-DNS/TLS predecessor proof; this record supplies the additional external-network and removal/recovery observations required specifically by TSK-0514.

## Stable outcome

**TSK-0514: PASS.**

ACC-0514 is satisfied by the current owner observation together with the already-accepted predecessor evidence. The L2 eligibility queue must now be recomputed from current `CURRENT_STATE.md`. This PASS does not alter or bypass the separate `TSK-0431` Azure-native recovery-path WAITING boundary, the owner legal hold, or any participant-activation gate.
