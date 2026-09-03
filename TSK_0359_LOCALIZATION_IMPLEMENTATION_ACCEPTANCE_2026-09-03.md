# TSK-0359 — Localization implementation acceptance evidence

**Date:** 2026-09-03  
**Task:** TSK-0359 — Implement externalized content, locale routing/fallback, RTL layout support, metadata, and locale-specific instruction selection  
**Lifecycle / authority:** L6 / MEDIUM / A3 / `AUTO_ALLOWED`  
**Hard predecessors:** TSK-0311 PASS; TSK-0358 PASS  
**Result:** PASS evidence complete for the current TSK-0359 acceptance contract.

## Canonical implementation

- Pull request: #62 — `TSK-0359: implement source-bound localized journey content`
- Feature head accepted before merge: `e7c1f89d72a47f729970d1b679908fa2338436df`
- Canonical squash merge: `70049dd6e4d5cb3ffbb5c68c8a143bce4e89053e`
- Canonical parent before TSK-0359: `e546d34a67e329ea2ce979193eecb64898bf9830`
- Current instruction authority bound by the implementation: `TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md` at `330e9d13b9d479212ca6c49df3431f19f7107ba5`.
- All nine current instruction IDs are represented in `website/src/content/instruction-bindings.json`; locale direction/fallback/market-activation authority remains `website/src/content/locale-manifest.json`.

## Test-first and review evidence

| Evidence | Run / job | Result | Purpose |
| --- | --- | --- | --- |
| Initial RED | `33705575361` / `100493841999` | Expected failure | Proved missing externalized journey content, deterministic fallback, instruction bindings, and localized operational surfaces before implementation. |
| Review RED — duplicate instruction | `33706105180` / `100495440107` | 34/35 contracts pass; one intended failure | Proved DNS setup rendered the source-bound instruction twice before the focused fix. |
| Review RED — duplicate activation authority | `33706431837` / `100496419539` | 34/35 contracts pass; one intended failure | Proved `journey-content.json` duplicated market-activation state before removal; `locale-manifest.json` remains the single authority. |
| Final branch gate | `33706555973` / `100496805461` | SUCCESS | Exact feature head passed governance/source validation, locked install, contracts, lint/typecheck/build, dependency audits, exact browser-tool installation, and real-browser acceptance. |
| Canonical clean-main gate | `33706792922` / `100497529049` | SUCCESS | Re-ran the same acceptance on canonical merge SHA `70049dd6e4d5cb3ffbb5c68c8a143bce4e89053e`. |

## ACC-0359 / VER-0359 mapping

1. **English, Turkish, and Arabic production locale paths/content render correctly.**
   - Contract suite: 35/35 PASS on canonical main.
   - Production Next.js build generated/validated the localized routes.
   - Real Chromium acceptance: `TSK0359_BROWSER_ACCEPTANCE=PASS`.
2. **Arabic RTL is explicit and usable.**
   - `locale-manifest.json` owns `direction=rtl` for `ar`; English/Turkish remain LTR.
   - Real-browser Arabic RTL, 320px layout, horizontal-overflow, and representative WCAG 2.2 AA axe checks passed.
3. **Fallback/applicability and locale-specific instruction selection fail visibly rather than silently mismatching.**
   - Deterministic requested-locale → declared-fallback → default resolution is tested.
   - Missing values and fallback cycles fail closed.
   - Android/iPhone setup, verification, and removal routes bind the current TSK-0307 instruction IDs by platform and locale; browser tests confirm rendered variants.
4. **SEO/indexing remains explicit.**
   - Operational routes retain `noindex` behavior; browser acceptance checks robots metadata on the TSK-0359 operational surfaces.
5. **Language availability does not activate non-UK markets.**
   - `locale-manifest.json` is the single market-activation authority and keeps `marketActivation=false` for `en-GB`, `tr-TR`, and `ar`.
   - Contract/browser tests reject a duplicated activation field in journey content and verify the manifest flags directly.

## Security, privacy, and governance verification

- No authentication requirement, account dependency, deployment path, external service, analytics transport, browsing/domain-history collection, raw diagnostic persistence, or new sensitive-data category was introduced.
- Protection Map state remains evidence-driven: only fresh qualifying technical evidence can yield `protected/verified`; account ownership, journey completion, or configuration alone cannot manufacture verification.
- React renders localized strings as ordinary escaped content; no HTML injection path was introduced.
- Repository/master-plan validation passed twice in the canonical run: `tasks=641`, `dependency_edges=858`, `broken_links=0`, `generated_missing_task_ids=0`.
- `npm audit --audit-level=high` and `npm audit --omit=dev --audit-level=high` both reported `0 vulnerabilities` on canonical main.
- Lint completed with one inherited non-error warning for `_accountState` in `core-state-machine.ts`; no lint errors occurred.

## Exact canonical target evidence

Canonical run `33706792922` checked out exactly `70049dd6e4d5cb3ffbb5c68c8a143bce4e89053e` and ran on GitHub-hosted Ubuntu 24.04.4 LTS with Node `22.23.2`, Next.js `16.3.3`, React/React DOM `19.2.8`, Playwright `1.62.1`, axe-core `4.13.0`, and Chromium/Chrome for Testing `151.0.7922.34`.

Observed final markers:
- `VALIDATION PASS`
- contract tests: `35` pass, `0` fail
- production build: compiled successfully; TypeScript completed; 55 pages generated
- dependency audits: `0 vulnerabilities`
- `TSK0359_BROWSER_ACCEPTANCE=PASS`
- `TSK0358_BROWSER_ACCEPTANCE=PASS`
- `TSK0361_BROWSER_ACCEPTANCE=PASS`

## Rollback and side-effect boundary

This task changed repository source/content/tests only. It did **not** deploy, distribute profiles, activate a market, process real participants, alter production runtime, or clear any material-action fence. Source rollback is the ordinary revert of canonical merge `70049dd6e4d5cb3ffbb5c68c8a143bce4e89053e`; no external runtime rollback is required for TSK-0359 itself.

## Preserved unresolved fences

- TSK-0360 remains TODO until its required real supported-iPhone and related ACC-0360 / VER-0360 / EVD-0360 evidence exists.
- TSK-0455 remains WAITING for a genuinely qualifying fresh Ubuntu 24.04 LTS target host and required target access/evidence.
- TSK-0399 is not made PASS or executable merely by TSK-0359; its other hard predecessor TSK-0360 remains non-PASS.
- No `GATE-0026` is created or inferred; current lifecycle gates retain their canonical identifiers.
