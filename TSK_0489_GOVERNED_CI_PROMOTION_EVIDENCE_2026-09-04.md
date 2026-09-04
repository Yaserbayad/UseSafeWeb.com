# EVD-0489 — Governed CI and conditional promotion evidence

**Task:** TSK-0489 — Add CI pipeline and automated checks
**Acceptance:** ACC-0489
**Verification:** VER-0489
**Evidence:** EVD-0489
**Disposition:** PASS
**Canonical implementation merge:** `655b9bcdf1c10eef0edbdce626742e2bbbd09e1e` (PR #99)

## Verified acceptance chain

1. **Authority and prerequisites:** TSK-0489 remained A3 / AUTO_ALLOWED with hard predecessors TSK-0453, TSK-0491, and TSK-0422 current PASS under the runtime authority; ACC-0489 / VER-0489 / EVD-0489 and INT-0015 graph bindings were verified. DEC-0060 / CR-0013 authorize deterministic evidence-gated promotion while preserving all material-action fences.
2. **Deliberate fail-closed proof:** PR #99 deliberately failed on source head `bd881ce0...`; workflow run `33873219678` observed the intentional failure, exited before promotion, retained artifact `9936761738`, and PR #99 remained unmerged.
3. **Final exact-head PR proof:** final PR source head `5ec96d4e15a9c40337fdb3c0cddf30540db20bc2` passed the governed CI run `33874683518` including `governed-ci` and `promotion-eligibility`; TSK-0453 exact-head run `33874683404` also passed. Immediately before merge, canonical `main` was still `4640494fc673dec57676ca41aed3ea23c5ecccb4` and PR #99 was mergeable on that exact source head.
4. **Conditional promotion:** PR #99 was merged only after the applicable exact-head contexts were green. Canonical merge commit is `655b9bcdf1c10eef0edbdce626742e2bbbd09e1e`.
5. **Post-merge main proof:** push run `33874954545` on exact canonical `main` `655b9bcdf1c10eef0edbdce626742e2bbbd09e1e` passed both `governed-ci` (job `101029614234`) and `promotion-eligibility` (job `101029954615`). TSK-0453 post-merge run `33874954622` also passed.
6. **Local/CI parity:** the canonical local-equivalent entrypoint executed by CI is `npm run validate`; post-merge evidence reports `TSK0489_LOCAL_CI_PARITY_ENTRYPOINT=npm run validate`. The run passed 111/111 contract tests, lint with zero errors, typecheck, production build, SPDX SBOM generation/validation, and both npm vulnerability audits with zero vulnerabilities.
7. **Security/privacy and repository integrity:** the post-merge run reports `TSK0489_GOVERNANCE_VALIDATION=PASS`, `TSK0489_DEPENDENCY_SBOM_AUDIT=PASS`, `FULL_HISTORY_SECRET_SCAN=PASS`, `TSK0489_SECURITY_PRIVACY_GATE=PASS`, `TSK0489_CLEAN_TREE=PASS`, and `TSK0489_GOVERNED_CI=PASS`.
8. **Retained executable evidence:** artifact `9937487977`, name `tsk-0489-governed-ci-33874954545-1`, size 8842 bytes, retained until 2026-10-04, digest `sha256:b76210e6aa646a2f029e07adafd6493736b0c73fb66edebea9248170d5923554`.
9. **Material-action fence proof:** the post-merge run explicitly records `TSK0489_DEPLOYMENT_ACTION=NONE`, `TSK0489_ACTIVATION_ACTION=NONE`, `TSK0489_PARTICIPANT_ACTION=NONE`, `TSK0489_SERVICE_MUTATION=NONE`, `TSK0489_PAYMENT_ACTION=NONE`, `TSK0489_LAUNCH_ACTION=NONE`, and `TSK0489_MATERIAL_ACTION_FENCES=PASS`.

## Post-merge workflow classification

The same `main` push also triggered eight historical task-acceptance workflows for TSK-0376, TSK-0491, TSK-0360, TSK-0369, TSK-0499, TSK-0243, TSK-0380, and TSK-0375. Each is a task-scoped historical evidence workflow, not a current universal promotion context. Their failure boundary is the same obsolete hard-coded WBS blob assertion (`eb35f3b10356396c5117e3f47d0b0378953e2157`) before their substantive task tests run; current canonical WBS blob before this reconciliation is `f3399492a6da5e168cc2bca92762c17c91358b9f`. These failures therefore do not contradict the current governed gate or product validation evidence and are retained here as classified post-merge evidence rather than silently ignored.

## ACC-0489 disposition

ACC-0489 is satisfied: approved governed checks execute on pull/change requests and `main`; the deliberate failure blocked promotion; successful promotion required exact-head green evidence; evidence is retained; no bypass was used; post-merge `main` reran the governed checks successfully; local/CI parity is explicit; and deployment/material-action authority remained absent.

This PASS does **not** authorize deployment, activation, participant processing, service mutation/revocation, payment, telemetry activation, launch, or any other separately fenced material action.
