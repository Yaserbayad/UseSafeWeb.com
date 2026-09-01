# TSK-0518 — Independent recovery acceptance plan evidence — 2026-09-01

**Task:** TSK-0518  
**Acceptance:** ACC-0518  
**Verification:** VER-0518  
**Evidence:** EVD-0518  
**Disposition:** PASS at the independent-acceptance-plan definition boundary

## Authoritative outcome

The independent recovery acceptance plan is complete and independently verified. It prevents producer-only self-certification and maps the current recovery surface to durable evidence classes plus severity/blocking rules. This PASS accepts the **acceptance plan only**; it does not assert that a clean-server recovery has been executed, that the approximately-30-minute RTO has been achieved, that production is deployed/activated, or that LG-07 passes.

## Current task authority

Current WBS authority for TSK-0518 is:

- lifecycle: `L5`;
- priority: `CRITICAL`;
- sole hard dependency: `TSK-0446`;
- AI capability/action authority: `A3 / AUTO_ALLOWED`;
- acceptance: `ACC-0518` — `Plan prevents producer-only self-certification and maps every recovery requirement to evidence and severity/blocking rules.`;
- verification: `VER-0518` — peer/reviewer inspection against current acceptance, source baseline, dependencies and required evidence;
- evidence: `EVD-0518`.

`LG-06` is current PASS and unlocks L5. `TSK-0446` is current PASS at its recovery-contract boundary.

## Exact artifacts

- Acceptance plan: `TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_2026-09-01.md`
- Plan version: `1.0.0`
- Plan blob: `9915f59e356c0d06a0c54ce0c9d4bb63f7e0b553`
- Original plan/source commit: `6e72ae53b36acddda4e1b3b548bc8db8eefcedf2`
- Corrected verifier/source commit independently tested: `930d719b928030ea2902e56652554499fb1e4a4e`
- Verifier: `.github/scripts/verify_tsk0518_independent_recovery_acceptance_20260901.py`
- Verifier blob at PASS: `bd900f345beffcb812d145e0f4379615b127c0f1`
- Workflow: `.github/workflows/verify-tsk0518-independent-recovery-acceptance-20260901.yml`
- Workflow blob: `bb5900b70ec93be83902ada1e7021a3786f642d0`
- Automated marker: `TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_AUTOVERIFY_2026-09-01.md`
- Marker blob: `c1c37dd4c080a91e917b313db0ec0c79793333dc`
- Marker commit/read-back: `23893e7b998e334d4d3db63ecaee951d28a15d5d`

## Proven predecessor binding

TSK-0518 consumes, but does not replace, current TSK-0446 and TSK-0413 evidence:

- TSK-0446 contract: `infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md`, blob `18d998e2406e801c7ac08f4daa2e3b763ea9b523`;
- TSK-0446 evidence: `TSK_0446_RECOVERY_SCOPE_CONTRACT_EVIDENCE_2026-09-01.md`, blob `714a5ccf4e7d0dc104ff55c1d87381571ab786f9`;
- TSK-0446 independent verification: run/job `33504115232 / 99843993787` — SUCCESS;
- current TSK-0413 bundle: `infrastructure/adguard-server/tsk-0413-bundle-v1/bundle.json`, blob `f0735e6a508f16de7a9c4510cc2893b972c1786c`;
- current TSK-0413 self-verifier was rerun by TSK-0518 verification and passed.

The plan preserves owner-approved `DEC-0016 / TSK-0413` semantics: persistent query/file logging off; identifiable per-client statistics/history excluded; client-IP anonymization on; ECS off; upstream Quad9 dns10 DoH only; and only minimum anonymized aggregate operational statistics with `1d` retention. Older blanket “statistics off” wording cannot override that current baseline.

## ACC-0518 proof — independence

The plan separates four responsibilities:

1. Cloud / Platform Engineering (`PKG-09`) as producer;
2. QA / Release Acceptance (`PKG-12`) as acceptance owner;
3. a QA-owned workflow/runner or separate authorised verifier as independent executor/observer;
4. SRE / Operations (`PKG-13`) as downstream consumer of independently accepted output.

Producer logs, local tests, screenshots, artifact existence or producer declarations are supporting evidence only. Target criteria requiring a clean Ubuntu host, network/TLS/DNS behavior, backup/restore, restart, timing or external health require direct independent target evidence. Hidden reasoning/inference never satisfies evidence.

## ACC-0518 proof — recovery mapping

The plan contains exactly 20 independently dispositioned recovery rows `RA-01` through `RA-20`, covering:

1. fresh supported owner-handoff Ubuntu target;
2. immutable/trusted source, TSK-0413 bundle and TSK-0446 contract;
3. deterministic prerequisites/packages and unsupported-state fail-closed behavior;
4. exact AdGuard Home version/schema compatibility;
5. protected config/secret handling plus final safe-field projection;
6. listener/firewall/admin exposure;
7. upstream/ECS/anonymization desired state;
8. privacy/log/statistics/history invariants;
9. public DoH/DoT/Private DNS endpoint identity;
10. TLS topology, chain, hostname and private-key protection;
11. filter/allowlist state;
12. privacy-safe functional resolution/blocking/external health;
13. startup/restart behavior;
14. idempotency/partial-state/drift behavior;
15. representative failure injection;
16. protected backup/clean restore;
17. rollback/emergency recovery;
18. independent timed restoration against the TSK-0446 ~30-minute boundary;
19. privacy/security/reproducibility of evidence itself;
20. accepted-version handoff to operations.

Each row has a required evidence class (`DT`, `IR`, `DO`, with producer evidence only supporting) and a default blocking severity.

## Blocking semantics

- `EB` evidence blocker: missing applicable evidence, wrong candidate/target, producer-only evidence, broken evidence linkage/hash, unusable redaction, or hidden-reasoning dependency — blocking regardless of nominal defect severity.
- `S1 Critical`: always blocking, including secret/private-key leaks, public admin exposure, prohibited DNS/query/client history, ECS/privacy drift, wrong resolver identity, TLS trust/hostname failure, unsafe partial exposure, untrusted recovery inputs.
- `S2 High`: always blocking for recovery acceptance, including clean deploy/restore failure, wrong filter/allowlist state, restart/idempotency/failure/rollback failure, external encrypted-DNS health failure, backup/restore failure, or current RTO-target breach.
- `S3`: nonblocking only when it does not waive/weakens an applicable criterion and has explicit impact/workaround/owner/disposition.
- `S4`: cosmetic only.

No numeric tolerance around the current approximately-30-minute target is invented. A measured result above 30:00 remains a blocking deviation until current governing authority supplies a different accepted threshold/disposition.

## Independent verification evidence

- Initial run/job: `33505169380 / 99847397133` — **FAIL**, correctly fail-closed.
- Initial deviation: Markdown table parser retained the trailing `|`; the resulting empty cell shifted evidence/severity indexing and falsely reported `RA-01 has no direct/reproducible evidence class`.
- The plan itself was not changed for that failure.
- Corrective commit: `930d719b928030ea2902e56652554499fb1e4a4e`, changing the parser to strip the row delimiter and require exactly four cells after each `RA-*` ID.
- Final run/job: `33505275372 / 99847736387` — **SUCCESS**.
- Final verifier output:
  - `TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_VERIFY=PASS`;
  - `plan_version=1.0.0`;
  - `dependency=TSK-0446`;
  - `mapped_recovery_rows=20`;
  - `producer_only_self_certification=prohibited`;
  - `privacy_baseline=tsk0413_dec0016_current`;
  - `target_execution_claimed=false`.
- Master-plan structural validation: PASS — 641 tasks, 858 dependency edges, 0 broken links, 0 generated missing task IDs.
- Durable marker: blob `c1c37dd4c080a91e917b313db0ec0c79793333dc`, commit/read-back `23893e7b998e334d4d3db63ecaee951d28a15d5d`.

## Current risks/requirements/interfaces explicitly enforced

- `RSK-0050`: prevents PASS from artifact existence/local behavior/incomplete evidence;
- `REQ-0065`: critical requirements map to verification/evidence/acceptance/decision;
- `REQ-0066`: integrated verification includes functional, network/device, accessibility, security/privacy, performance, failure, recovery and rollback paths;
- `CON-0023`: correctness/security/privacy/reliability/quality remain hard gates;
- `CON-0029`: hidden chain-of-thought is not evidence;
- `INT-0017`: only verified release is handed to operations;
- `INT-0025`: recovery system passes from Cloud/Platform to independent QA acceptance with fresh-server, backup/restore, failure, security/privacy/DNS evidence.

## Non-inference / downstream boundary

This evidence does **not** prove:

- the deployment/recovery script exists or is production-ready;
- an owner-provided clean Ubuntu VM has been restored;
- actual ~30-minute RTO attainment;
- current backup/restore, rollback, idempotency, failure injection, live DNS/TLS health, or production safety;
- Azure control-plane provisioning;
- TSK-0445, TSK-0447, TSK-0455..TSK-0463, TSK-0519 or any other downstream task PASS;
- LG-07 or any later gate PASS;
- production/public/user activation.

Those require their own current dependencies, authority and direct target evidence.

## Final disposition

**TSK-0518: PASS** at the independent-acceptance-plan definition boundary. ACC-0518 is proven: producer-only self-certification is prevented; all 20 current recovery requirements are mapped to independent evidence classes and severity/blocking rules; the approved TSK-0413 privacy-first baseline is preserved; the verifier defect was corrected and the complete independent verification reran successfully; no target execution outcome is inferred.
