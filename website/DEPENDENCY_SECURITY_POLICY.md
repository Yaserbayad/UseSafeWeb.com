# Dependency inventory, update policy, and SBOM baseline

**Task:** TSK-0491  
**Owner:** Security  
**Baseline source commit:** `cb8bce01ca8a70de27a41a8fe35570d8a2920701`

## Controlled dependency surface

The tracked executable dependency surface is the `website/` npm application. `website/package.json` declares direct dependencies and `website/package-lock.json` is the committed npm lockfile that fixes the exact resolved dependency tree. The CI SBOM is generated from that lockfile and therefore records resolved package versions independently of local `node_modules` state.

Current repository inspection found **container images: none** in the tracked execution surface: there is no Dockerfile/Compose definition and no workflow `container`, `services`, or image reference. A future container image must be added to this inventory and pinned by immutable digest before it can satisfy this policy.

### Direct dependency inventory

| Package | Requested version/range | Class | Exact-resolution authority |
| --- | --- | --- | --- |
| next | 16.3.3 | runtime | `package-lock.json` |
| react | 19.2.8 | runtime | `package-lock.json` |
| react-dom | 19.2.8 | runtime | `package-lock.json` |
| @types/node | ^20 | development | `package-lock.json` |
| @types/react | ^19 | development | `package-lock.json` |
| @types/react-dom | ^19 | development | `package-lock.json` |
| eslint | 9.39.5 | development | `package-lock.json` |
| eslint-config-next | 16.3.3 | development | `package-lock.json` |
| prettier | 3.9.6 | development | `package-lock.json` |
| typescript | ^5 | development | `package-lock.json` |

The requested range is not treated as the installed version when it is a range. The exact resolved version is the corresponding `node_modules/<package>.version` record in the committed lockfile and the generated SPDX SBOM.

## Deterministic install and SBOM

- Install with the frozen toolchain from TSK-0380: Node `22.23.2`, npm `10.9.8`, then `npm ci`.
- Do not hand-edit `package-lock.json`; dependency changes must be made through npm and committed with the resulting lockfile delta.
- Generate the application SBOM with `npm run sbom`. The command uses `npm sbom --package-lock-only --sbom-format=spdx --sbom-type=application`, so CI reads the committed lockfile rather than relying on mutable local installation state.
- CI parses the generated document and requires SPDX `2.3` plus a non-empty package list.

npm documents that `package-lock.json` represents the exact dependency tree used for reproducible installs, and that `npm sbom` can generate SPDX or CycloneDX output from package-lock-only state.

## Update and vulnerability policy

Security owns dependency disposition. Dependency-changing pull requests must include the package manifest and lockfile together and must pass the repository contract, formatting, lint, type, build, SBOM, and audit checks before acceptance.

Routine review:

1. Review direct dependency freshness at least monthly while the application is under active development and whenever a dependency-changing pull request is proposed.
2. Use `npm outdated` for available-version review and `npm audit` for registry advisory review. Review results before changing the lockfile; do not run an automatic force upgrade as an unreviewed remediation.
3. Apply the smallest compatible update that resolves the issue, then rerun the full deterministic validation and SBOM checks.

Severity disposition:

| Severity | Required disposition |
| --- | --- |
| Critical | Stop acceptance until remediated or a current, explicitly authorized, time-bounded exception is recorded. |
| High | CI fails through `npm audit --audit-level=high`; remediate before acceptance unless a current, explicitly authorized, time-bounded exception exists. |
| Moderate | Security reviews the advisory and records upgrade or no-change rationale at the next dependency review; escalate if exploitability or project context makes the actual risk higher. |
| Low | Review during the routine dependency cycle; update when compatible or record why the current version remains appropriate. |

`npm audit --audit-level=high` changes the failure threshold; it does not hide lower-severity findings, so moderate/low findings remain visible for review.

## Exception record

An exception is not implicit. It must identify the affected package/version, advisory or reason, severity, project exposure, compensating control if any, responsible owner, approval authority, decision date, and expiry/review date. Missing or expired approval means the exception does not satisfy acceptance. Critical/high unresolved findings without a valid exception block TSK-0491 PASS and any dependent release condition that relies on this control.

## Change-control boundary

This policy governs dependency inventory, lockfile integrity, SBOM generation, and vulnerability/update disposition only. It does not authorize external deployment, live-device actions, participant processing, telemetry activation, or any other material operation.
