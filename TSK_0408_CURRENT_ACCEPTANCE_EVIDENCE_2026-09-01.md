# TSK-0408 current acceptance evidence — 2026-09-01

**Disposition:** **PASS**  
**Task:** `TSK-0408 — Define one coherent UseSafeWeb DNS identity and approved platform-specific endpoint/profile mechanisms`  
**Acceptance / verification / evidence:** `ACC-0408 / VER-0408 / EVD-0408`  
**Authority:** `A3 / AUTO_ALLOWED`; `DEC-0053 / CR-0006`; `DEC-0054 / CR-0007`.  
**Current revalidation:** `TSK_0408_POST_CR0007_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `a6b41ff7462dab630aad9e7640950b0d3467f040`.  
**Independent verification:** GitHub Actions run `33497169433`, job `99821919358` — SUCCESS.  
**Verification head:** `3293a3fcae7e1258eab947bfb4218186b275d75a`.  

## Acceptance result

PASS. The current contract preserves the proven single service identity `UseSafeWeb DNS`, canonical resolver hostname `dns.usesafeweb.com`, Android native DoT-by-hostname behavior, Apple DoH profile/Server-URL behavior, TLS identity, truthful verification/removal/fallback rules and the prohibition on browsing/query-history evidence or a false universal setup string.

CR-0007 supersedes only the old mandatory pilot/staging/future-production lifecycle framing. Current environment separation is satisfied by one production service identity plus explicitly non-production local/dev/CI/ephemeral/preview/mock/synthetic/dry-run evidence; staging or a bounded ramp is conditional on a specific verified risk, not a required customer lifecycle.

No FQDN, path, profile identifier, callback URL, support endpoint, account/dashboard route, AdGuard `/control` exposure or administrator secret is invented by this acceptance. Optional account functionality does not make core DNS protection login-dependent.

## Contrary evidence and limitations

No current acceptance-relevant contradiction was found. This PASS is an L4/current-dependency qualification only. It does not approve LG-07, AdGuard implementation, production activation, publication, live-user processing, payment, market activation or launch. Later implementation/runtime criteria still require their own current evidence.

## Work unlocked

`TSK-0413` may use this current TSK-0408 PASS as its direct hard-dependency evidence, subject to its own current acceptance, secret boundary, version-compatibility requirements and independent verification.