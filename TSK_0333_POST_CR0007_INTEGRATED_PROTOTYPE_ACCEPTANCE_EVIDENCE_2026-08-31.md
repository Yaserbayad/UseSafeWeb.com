# TSK-0333 — Post-CR-0007 Integrated Prototype Acceptance Evidence

**Task:** TSK-0333  
**Acceptance:** ACC-0333  
**Verification:** VER-0333  
**Evidence:** EVD-0333 analytical acceptance  
**Date:** 2026-08-31  
**Disposition:** PASS — pending deterministic evidence publication and guarded runtime reconciliation only

## 1. Current authority and eligibility

Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c` defines TSK-0333 as L4 / MEDIUM, hard dependencies `TSK-0335; TSK-0334; TSK-0146; TSK-0331`, A3 / `AUTO_ALLOWED`, with `ACC-0333 / VER-0333 / EVD-0333`.

All four dependencies are current durable PASS under the current dual-mode Version-1 scope. Relationship graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032` matches the dependency and acceptance/evidence contract. Pre-acceptance runtime blob is `15948b153c5c0c07b93fc894ac9f4ca6c537cce0`.

## 2. Why historical TSK-0333 was not reused as current PASS

The historical 2026-08-30 prototype/evidence was accountless-only and predated the current optional-account/dashboard scope plus the current TSK-0331 dependency. Current ACC-0333 explicitly requires Google sign-in/account creation/return/session lifecycle, lightweight dashboard/device management and account/device lifecycle flows in addition to the complete accountless core.

Therefore the historical artifact remained useful input only; it could not satisfy current acceptance without rebuilding/reconciliation.

## 3. Current accepted product artifacts

- `prototype/TSK-0333/index.html`, blob `9395f0e105d20683b5beafa01b02d7b300e79a8d`.
- `prototype/TSK-0333/model.mjs`, blob `9b7c239024d8ae24371b687aa39de6fa6b2b62b6`.
- `prototype/TSK-0333/app.mjs`, blob `476ea932d95592fabf586f7ba381be0d346117fe`.
- `prototype/TSK-0333/prototype.css`, blob `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.

The rebuilt prototype integrates one deterministic state model across:

- accountless setup/router/native safeguard/DNS/verification/service/Protection Map;
- support, false-positive, limitations, troubleshooting, physical removal, recovery and reconfiguration;
- optional Google sign-in, first account creation, returning account, provider error, session expiry/reauthentication and logout;
- lightweight dashboard/device detail/manage;
- explicit device saving, reverify, reinstall/reconfigure, replacement, revoke/unlink and saved-record deletion;
- account deletion entry and fail-closed unknown destructive-operation handling.

## 4. Current acceptance semantics proven

### Accountless core

The complete core remains usable without login. Android Private DNS and iPhone DoH paths are represented explicitly; only current qualifying technical evidence can create `Verified`. Parent confirmation remains weaker and is never relabelled as verification.

The Protection Map preserves independent Phone / Internet / Service truth and no overall safety score. False-positive/help activity does not rewrite technical evidence. Physical DNS removal produces `Removed`; neutral connectivity recovery cannot restore `Verified`; reconfiguration begins from a fresh action-needed/unverified state.

### Optional account/dashboard path

Google sign-in/account creation is explicit and optional. A newly created account does not silently create a saved device. Anonymous J0/J1 state is not imported, promoted, linked or expiry-extended by sign-in or device saving.

A returning dashboard record is explicitly not technical verification. Saved-record/account presence cannot create `Verified`. Device replacement starts fresh/unverified. Revoke/unlink and record deletion are account-side lifecycle operations and do not claim physical DNS removal.

Provider/session/account failures are account-only and retain signed-out core fallback. Session expiry does not change physical protection; reauthentication does not replay destructive operations automatically. Logout ends account access only. Account deletion is distinct from physical protection removal and unrelated J0/J1 deletion.

### Privacy / safety / accessibility boundaries

The prototype provides no browsing/query/activity history, child profile, raw DNS logs/history, top-sites surface, broad DNS administration, broad per-domain controls or safety score/certification. Browser verification observed no localStorage/sessionStorage/cookie/IndexedDB persistence and no non-local runtime transport.

The UI preserves keyboard skip-link operation, responsive behavior at 320/768/1024/1440 widths, RTL switching, reduced-motion styling and visible textual evidence states.

## 5. Structured verification

Current structured workflow run/job `33432040521 / 99619466660`: SUCCESS on self-hosted `adguardvm` for the rebuilt contract. The final browser workflow also reruns the same structured verifier before browser execution and passed it at the final accepted head.

Observed structured markers:

- `TSK0333_CURRENT_AUTHORITY_BLOBS=PASS`
- `TSK0333_WBS_CONTRACT=PASS`
- `TSK0333_GRAPH_CONTRACT=PASS`
- `TSK0333_DEPENDENCY_RUNTIME=PASS`
- `TSK0333_STRUCTURED_MODEL=PASS`
- `TSK0333_INTERACTION_COVERAGE=PASS`
- `TSK0333_PRIVACY_LIFECYCLE_FENCES=PASS`
- `TSK0333_STATIC_UI_CONTRACT=PASS`
- `TSK0333_POST_CR0007_STRUCTURED_VERIFICATION=PASS`

Structured verifier blob `497d709c40632a9bbd7e1f9513c27699e1f2d0f6`; structured workflow blob `812ab1dbdead44f7cae4d5c9c1c9e7b653766b27`.

## 6. Target-browser verification

Final browser run/job `33432762152 / 99621849637`: **SUCCESS** on self-hosted `adguardvm`.

Verification environment:

- Node `v22.23.2`;
- npm `10.9.8`;
- Playwright `1.62.0` installed into a temporary runner-only directory;
- Chromium / Chrome for Testing `151.0.7922.34`;
- localhost-only static server;
- no product dependency-tree modification.

Observed final browser markers:

- `TSK0333_BROWSER_KEYBOARD=PASS`
- `TSK0333_BROWSER_ACCOUNTLESS_ANDROID=PASS`
- `TSK0333_BROWSER_FALSE_POSITIVE_TRUTH=PASS`
- `TSK0333_BROWSER_REMOVAL_RECOVERY=PASS`
- `TSK0333_BROWSER_IPHONE=PASS`
- `TSK0333_BROWSER_UNSUPPORTED=PASS`
- `TSK0333_BROWSER_NEW_ACCOUNT=PASS`
- `TSK0333_BROWSER_EXPLICIT_DEVICE_SAVE=PASS`
- `TSK0333_BROWSER_RETURNING_DASHBOARD=PASS`
- `TSK0333_BROWSER_DEVICE_REPLACEMENT=PASS`
- `TSK0333_BROWSER_UNKNOWN_AND_RECORD_DELETE=PASS`
- `TSK0333_BROWSER_PROVIDER_ERROR=PASS`
- `TSK0333_BROWSER_SESSION_LOGOUT_DELETE_BOUNDARY=PASS`
- `TSK0333_BROWSER_RTL_RESPONSIVE=PASS`
- `TSK0333_BROWSER_PRIVACY_NO_TRANSPORT=PASS`
- `TSK0333_BROWSER_NO_CONSOLE_ERRORS=PASS`
- `TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS`

Browser verifier blob `966cb53e01e58155350fc9a904cf71bd1a30c748`; browser workflow blob `532b1f6c67516e2e449720f791d91af4ee8fe2bc`.

## 7. Defect/correction evidence precedence

The target-browser campaign found one substantive product defect: the configured Protection Map did not expose its required physical DNS removal path. The product controller was corrected to expose `Remove UseSafeWeb DNS` when configured; the relevant test was not weakened. The later browser run proved removal/recovery PASS.

Two later failures were verifier-only:

1. a strict role selector matched both global and local `Start setup` controls although the required provider-error fallback existed;
2. the privacy assertion required the non-contiguous literal `no activity history` while the actual correct copy was `No browsing history or activity history.`

Only verifier assertions changed for those failures; product semantics did not.

No failing run mutated runtime PASS.

## 8. Non-inference boundary

This evidence proves TSK-0333 only. It does not by itself prove LG-06, L5 architecture/security/privacy/vendor acceptance, production authentication/persistence/deletion, deployment, real-user validation, publication or launch.

`RSK-0002` remains OPEN/non-blocking before L8.

## 9. Acceptance conclusion

The exact current integrated prototype satisfies current ACC-0333 across the complete accountless core plus optional Version-1 account/dashboard/device lifecycle paths, with target-browser proof for responsive/mobile/RTL/accessibility, privacy and failure/recovery behavior.

`ACC-0333 / VER-0333 / EVD-0333`: **PASS**, subject only to deterministic evidence publication and guarded runtime reconciliation/read-back.
