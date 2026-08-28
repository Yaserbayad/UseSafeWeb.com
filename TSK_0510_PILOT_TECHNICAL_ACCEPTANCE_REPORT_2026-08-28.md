# TSK-0510 — Pilot Technical Acceptance Report

**Task:** TSK-0510 — Compile signed pilot technical acceptance report  
**Acceptance:** ACC-0510  
**Requirements:** REQ-0065; REQ-0066  
**Interface:** INT-0017  
**Lifecycle:** L2 / Pre-Experiment  
**Date:** 2026-08-28  
**Task owner:** QA / Release Acceptance  
**Reviewer:** UseSafeWeb governed QA evidence review (A3 / AUTO_ALLOWED)  
**Signature mechanism:** durable Git commit/blob plus independent repository audit; this is an evidence signature, **not a fabricated human or legal signature**.

## 1. Decision scope

This report closes the bounded **technical acceptance-report task** only. It does not authorize recruitment, real-participant activation, public launch, legal/privacy approval, Azure control-plane change, or any Project Owner gate decision.

LG-03 Validation Readiness requires a legally, technically, and operationally safe real-participant environment. Its required evidence includes UK route/ICO or verified non-applicability, actual data flow, LIA/DPIA where applicable, notices, Azure region, AdGuard privacy/upstream/ECS, endpoint/TLS, recovery, and no payment/marketing. The legal/regulatory/compliance branch remains owner-deferred/unresolved; therefore **LG-03 overall is not PASS** even though the currently executable technical branch is accepted.

## 2. Exact authority baseline

- `CURRENT_STATE.md` blob at report preparation: `f4a95ca7df5b527717f91c63044a1323abd1e33a`.
- WBS authority: `Plans/Master/WBS/master-wbs.csv`, blob `2e4560103b71bb350b14673ce3e415afc3dbfe3a`.
- Requirement register: `Plans/Master/Registers/REQUIREMENTS.md`, blob `12c3bf6a227ad6ae61e167546a2b8a35d01321d1`.
- Gate register: `Plans/Master/Registers/GATES.md`, blob `692a51b920f3af9c8c937e712d19a0841c57eabf`.
- TSK-0510 hard predecessors are `TSK-0511; TSK-0512; TSK-0207; TSK-0428; TSK-0431; TSK-0011`; current canonical runtime state records all as PASS.

## 3. Mandatory LG-03 readiness evidence mapping

| LG-03 evidence requirement | Technical evidence / disposition | Status | Owner / disposition |
| --- | --- | --- | --- |
| Plan frozen/published | Canonical modular plan is owner-frozen and publication/read-back is recorded in `CURRENT_STATE.md`. | PASS | Project governance; no action. |
| UK route / ICO or verified non-applicability | Owner-deferred legal/regulatory/compliance work remains unresolved until 2027-08-27 or earlier explicit reactivation. | **WAITING — outside technical acceptance** | Project Owner / Privacy-Legal. Blocks LG-03 overall PASS. |
| Actual data flow | `TSK_0428_AZURE_REGION_DATA_PATH_EVIDENCE_2026-08-28.md`, blob `bbcd27772f8a9cad8248c48e9290b52baf71056f`, directly bounds the active child-linked DNS path to supported device -> Azure West Europe UseSafeWeb DNS -> same-host Nginx/AdGuard -> Quad9 dns10. | PASS | Cloud/DevOps; accepted. |
| LIA/DPIA where applicable | Required legal/privacy approval evidence is not asserted by this technical report. | **WAITING — outside technical acceptance** | Privacy-Legal / Project Owner. Blocks LG-03 overall PASS where applicable. |
| Notices | Required notice approval/release is not asserted by this technical report. | **WAITING — outside technical acceptance** | Privacy-Legal / Project Owner. Blocks LG-03 overall PASS where applicable. |
| Azure region | TSK-0428 directly verifies production Azure `westeurope` via IMDS and no active US DNS node. Evidence blob `bbcd27772f8a9cad8248c48e9290b52baf71056f`. | PASS | Cloud/DevOps; accepted. |
| AdGuard privacy / upstream / ECS | TSK-0207 privacy persistence evidence blob `1c16db063e2e84d300b547075721d33c2e020e32`; TSK-0407 upstream/ECS evidence blob `7afeca58e9205234a230d2de702b99648b35347d`; approved config blob `e9975c4e75c2a68131f049da942468d8d1952d8d`. Query/file logging and statistics are disabled, client IP anonymisation is enabled, persistent clients are absent, Quad9 dns10 is exact, ECS is disabled. | PASS | Network / Privacy technical controls; accepted. |
| Endpoint / TLS | Public DNS TSK-0441 evidence blob `91369bbe33eb608361e8b7b771ceca0a5cd42d50`; TLS TSK-0442 evidence blob `cb11394af1e80f15d85bda5d9b000bbf0efd6d20`; renewal/expiry controls TSK-0443 evidence blob `c2f3b3b35c9d8e2ec33f473d72c508ebde30348d`; external endpoint/removal TSK-0514 evidence blob `c5d004d0e0a8c58d1056b3aaad38034ae4188a68`; supported-device TSK-0511 evidence blob `ecd959f93ab7dff62aba6529ce66b45d59c3ed27`. | PASS | Network / QA; accepted. |
| Filtering / allowed-domain behavior | `TSK_0512_FILTER_REGRESSION_EVIDENCE_2026-08-28.md`, blob `cc21f4574a2ca7e721a7da961baef727350af1d3`, proves synthetic block, narrow exception, exact rollback, allowed resolution, and unchanged privacy/upstream invariants. | PASS | QA / Network; accepted. |
| Recovery | Project-controlled clean recovery evidence `TSK_0431_PROJECT_CONTROLLED_RECOVERY_DRILL_EVIDENCE_2026-08-28.md`, blob `2df5c05767fe326e38c609d37888f672dcb9dd48`, proves deterministic isolated recovery, DoH/DoT, filtering rollback, privacy, health and 12-second rebuild. Owner Azure restore evidence `TSK_0431_AZURE_RESTORE_OWNER_EVIDENCE_2026-08-28.md`, blob `e077165e98fa4460fba84466ffe28953ad53dec0`, closes the Azure-native restore boundary. | PASS | Cloud/DevOps + Project Owner evidence boundary; accepted. |
| No payment / marketing in current experiment technical path | TSK-0428 directly found no payment, analytics, email, CDN or application processor in the active child-linked DNS query path. Frozen Experiment-1 scope separately excludes payment testing. | PASS for current technical path | Product scope remains governed separately; no activation authority implied. |

## 4. REQ-0065 traceability evaluation

REQ-0065 requires every critical requirement to map to verification, evidence, acceptance, and a gate or operational decision where applicable.

For the current L2 pilot technical branch:

- supported-device encrypted DNS -> TSK-0511 / ACC-0511 / durable device evidence -> LG-03 technical readiness;
- filtering and allowed-domain behavior -> TSK-0512 / ACC-0512 / durable production regression evidence -> LG-03 technical readiness;
- privacy persistence -> TSK-0207 / ACC-0207 / durable production evidence -> LG-03 technical readiness;
- Azure region/data path -> TSK-0428 / ACC-0428 / durable target evidence -> LG-03 technical readiness;
- restore/rebuild -> TSK-0431 / ACC-0431 + REQ-0052 / durable recovery + owner restore evidence -> LG-03 technical readiness.

All hard predecessor technical requirements for TSK-0510 have direct evidence. Legal/privacy approval requirements that belong to the overall LG-03 gate are explicitly mapped above as WAITING rather than silently treated as technical PASS.

**REQ-0065 disposition for TSK-0510: PASS.**

## 5. REQ-0066 integrated-verification coverage

REQ-0066 requires integrated verification to cover functional, device/network, UX/comprehension, accessibility, security, privacy, performance, failure, recovery, and rollback paths. At this L2 technical-acceptance point, the report distinguishes proven current technical coverage from later product/integrated-release coverage:

| Verification axis | Current L2 evidence | Disposition |
| --- | --- | --- |
| Functional DNS behavior | TSK-0511, TSK-0512, TSK-0514 | PASS |
| Device/network | Android DoT and iPhone DoH on Wi-Fi/cellular plus removal/recovery — TSK-0511/0514 | PASS |
| UX/comprehension | No claim of integrated product UX acceptance is made at L2; broader validation/rehearsal remains governed by later/other tasks and LG-03/LG-04. | NOT CLAIMED / remains gate-scoped |
| Accessibility | No application UI accessibility acceptance is claimed by this DNS technical report; later integrated product acceptance owns it. | NOT CLAIMED / future lifecycle |
| Security | Restricted admin path, default-deny host posture, resolver-abuse protections and TLS controls are already recorded PASS in canonical state, including TSK-0483. | PASS for current DNS technical scope |
| Privacy | TSK-0207 plus approved AdGuard privacy configuration | PASS |
| Performance/capacity | Recovery timing is measured; no broader product/performance capacity acceptance is claimed at this L2 DNS-only point. Later integrated acceptance remains responsible for broader capacity/performance. | PARTIAL / future integrated scope |
| Failure/recovery | External removal recovery, certificate recovery controls, clean-server recovery and Azure-native restore evidence | PASS for current DNS scope |
| Rollback | Filtering exact rollback and recovery fail-safe evidence | PASS for current DNS scope |

The matrix is intentionally not converted into a false claim that future integrated-product UX/accessibility/performance acceptance has already occurred.

**REQ-0066 disposition for TSK-0510:** current mandatory L2 technical verification coverage is explicitly mapped; future integrated-product axes remain identified and are not silently closed. This satisfies the report/traceability obligation without bypassing later lifecycle gates.

## 6. Deviations and unresolved items

1. **LG-03 legal/regulatory/compliance evidence remains unresolved/deferred.** Owner: Project Owner / Privacy-Legal. Disposition: WAITING; no real-participant activation.
2. **No integrated application UX/accessibility acceptance is claimed.** Disposition: future lifecycle/gate work; not a defect in the current DNS technical baseline.
3. **No broad product performance/capacity acceptance is claimed.** Recovery timing is proven; later integrated acceptance owns broader capacity/performance.
4. The historical TSK-0431 recovery workflow had a post-PASS temporary-file cleanup defect; it was separately diagnosed/fixed and did not invalidate the accepted recovery criteria. Durable recovery evidence records the deviation.

No severity-1/2 or critical technical control failure is known in the bounded evidence set used by this report. This statement is limited to the current accepted DNS technical evidence and is not a substitute for future integrated defect/security acceptance.

## 7. Technical acceptance result

All TSK-0510 hard predecessors are current PASS with durable evidence, every applicable L2 technical LG-03 requirement is mapped to evidence, and unresolved non-technical gate conditions are explicit with owner/disposition.

**TSK-0510 technical acceptance report result: PASS candidate, subject to independent repository audit and durable read-back.**

**LG-03 Validation Readiness overall: NOT PASS / remains gated by unresolved owner-deferred legal/privacy/regulatory evidence and any other non-technical readiness conditions.**

## 8. Evidence signature

This report is signed for governance/evidence purposes only by its immutable Git publication identity and independent audit result. No human signature, legal attestation, recruitment authorization, or Project Owner gate decision is fabricated or implied.
