# TSK-0145 — Requirement-to-Evidence Traceability Matrix

**Task:** `TSK-0145`  
**Acceptance:** `ACC-0145`  
**Verification:** `VER-0145`  
**Evidence:** `EVD-0145`  
**Repository / branch:** `Yaserbayad/UseSafeWeb.com` / `main`  
**Source head before publication:** `6c3cd89e4653992219157474e309c25069ad0b15`  
**Date:** 2026-08-28

## Authority and derivation boundary

This file is a **derived, non-authoritative evidence view** for TSK-0145. It does not become a second requirements register, task state store, or owner-decision store.

- Requirements remain owned by `Plans/Master/Registers/REQUIREMENTS.md` (source blob before this publication: `12c3bf6a227ad6ae61e167546a2b8a35d01321d1`).
- Task definitions/dependencies/acceptance/verification/evidence metadata remain owned by `Plans/Master/WBS/master-wbs.csv` (source blob: `dce5b829c4d447eac180ae1e896e0019292cf971`).
- Package purpose, rationale basis, lifecycle obligations and owner/authority remain owned by `Plans/Master/Layers/LAYER_2_PACKAGE_CHARTERS.md`.
- Volatile runtime state remains owned by `CURRENT_STATE.md` (source blob before this publication: `3097079edb8f850a6966b74f0b7a35bea226f860`).
- Authority routing remains owned by `Plans/Master/MANIFEST.yaml` (source blob: `00feca027babfd99dcd1992e3e0abd6ef2d3380b`).
- No requirement is changed, removed, approved, satisfied, or promoted merely by appearing here.

### Field derivation

- **Source**: exact source field from the canonical requirement register.
- **Rationale**: `RB-*` derived from the owning package charter Purpose + Business/customer outcome. It is not a new owner rationale.
- **Priority**: exact canonical requirement priority.
- **Acceptance test**: exact canonical requirement Verification field.
- **Owner**: owning package plus its charter Primary owner/authority.
- **Release target**: `RT-*` derived from the owning package Lifecycle obligations, with an explicit requirement-level timing override only when the requirement itself states one.
- **Status**: requirement disposition, not WBS execution state. `ACTIVE` means the requirement is present and binding in the current canonical register. Special deferred/hold wording is preserved explicitly.
- **Implementing tasks**: canonical task references. Inclusive `TSK-nnnn..TSK-nnnn` notation is used only where the source list is exactly contiguous.
- **Evidence disposition** is deliberately conservative and does not replace task/ACC/EVD authority.

## Rationale basis

| Code | Package | Derived rationale basis | Primary owner / authority |
| --- | --- | --- | --- |
| RB-01 | PKG-01 | Maintain one coherent, current, traceable program baseline and deterministic execution system so authoritative state, evidence and next bounded action remain identifiable. | Project Owner / AI Governor |
| RB-02 | PKG-02 | Define the correct customer problem, product promise, scope, value model, roadmap and decision thresholds so the first-phone product remains focused and evidence-led. | Project Owner / Product |
| RB-03 | PKG-03 | Resolve the highest-value uncertainty with the smallest ethical experiment so behavioral and product decisions rest on observed evidence. | Product Research |
| RB-04 | PKG-04 | Keep the service lawful, privacy-minimal, transparent, child-appropriate and within safeguarding/claims boundaries. | Privacy / Legal / Project Owner |
| RB-05 | PKG-05 | Maintain a coherent, trustworthy and accessible brand system across public, product and support surfaces. | Brand / Product Owner |
| RB-06 | PKG-06 | Create a near-zero-friction, self-service, truthful and accessible end-to-end experience. | UX / Service Design / Content |
| RB-07 | PKG-07 | Implement one secure, accessible, maintainable, accountless-first TypeScript + Next.js application for public and setup journeys. | Software / Frontend / Backend Engineering |
| RB-08 | PKG-08 | Deliver the canonical DNS identity and filtering behavior with truthful limits and without an identifiable browsing-history product. | Network / DNS Engineering |
| RB-09 | PKG-09 | Make the service deployable, rebuildable, restorable, observable and cost-controlled without premature high availability. | Cloud / Platform Engineering |
| RB-10 | PKG-10 | Keep public DNS/web/API/admin/supply-chain surfaces least-privileged, hardened and verifiably controlled. | Security |
| RB-11 | PKG-11 | Provide trustworthy decision evidence using the minimum non-surveillance data with auditable definitions, denominators and uncertainty. | Product Analytics |
| RB-12 | PKG-12 | Ensure PASS means current evidence supports every applicable criterion through independent release/acceptance verification. | QA / Release Acceptance |
| RB-13 | PKG-13 | Prevent or self-recover ordinary failures and turn incidents into verified recovery and corrective action. | SRE / Operations |
| RB-14 | PKG-14 | Produce evidence-backed qualified acquisition within budget and trust constraints rather than optimize reach alone. | Growth / Communications / Partnerships |
| RB-15 | PKG-15 | Keep the bootstrapped service financially visible and sustainable without fundraising work or unnecessary overhead. | Project Owner / Finance |
| RB-16 | PKG-16 | Preserve customer value without routine human support and convert repeated ordinary issues into product/UX/automation fixes. | Customer Experience / Product Operations |

## Release-target basis

| Code | Package | Derived lifecycle / release target |
| --- | --- | --- |
| RT-01 | PKG-01 | Active in every lifecycle stage; depth scales with risk and current gate. |
| RT-02 | PKG-02 | Continuous; highest detail at evaluation, validation synthesis, product definition, pilot decisions, launch scope and Year-1 prioritization. |
| RT-03 | PKG-03 | Required at evaluation/concierge/pilot; conditional elsewhere when uncertainty is decision-material. |
| RT-04 | PKG-04 | Required before and during any real-user processing; scaled down for synthetic/historical stages. |
| RT-05 | PKG-05 | Deliberately minimal before behavioral evidence; required before validated UI and launch assets are finalized. |
| RT-06 | PKG-06 | Required from concierge design through Year-1 maintenance; final polish follows sufficient proposition evidence. |
| RT-07 | PKG-07 | Conditional before validation; required for definition/prototyping, build, verification, pilot, launch and Year-1 maintenance. |
| RT-08 | PKG-08 | Required from feasibility through all live stages; depth increases at pilot/production. |
| RT-09 | PKG-09 | Required from validation readiness through Year 1; feasibility stages remain minimal. |
| RT-10 | PKG-10 | Required before real-user processing and continuously thereafter; scaled for synthetic/historical work. |
| RT-11 | PKG-11 | Required wherever decisions or gates depend on evidence; continuous in Year 1. |
| RT-12 | PKG-12 | Required from validation-readiness verification through every release and Year-1 maintenance. |
| RT-13 | PKG-13 | Required before real-user DNS and continuously thereafter. |
| RT-14 | PKG-14 | Minimal before validation; controlled recruitment at L3; pilot channel tests; required at launch and through Year 1. |
| RT-15 | PKG-15 | Lean from inception; required before spending/contracting/live payments and throughout Year 1. |
| RT-16 | PKG-16 | Begins with validation support measurement; required before pilot/launch and continues through Year 1. |

## Evidence disposition codes

| Code | Meaning |
| --- | --- |
| ED-OPEN | This matrix does not infer requirement-level PASS; linked task/ACC/EVD records remain authoritative. |
| ED-DIRECT | Current runtime contains direct evidence materially supporting this requirement, but no requirement-level PASS is inferred here. |
| ED-PROVEN | Current runtime explicitly states that this requirement's acceptance is satisfied. |

## Requirement matrix

| Requirement | Source | Rationale | Priority | Acceptance test | Owner | Release target | Status | Implementing tasks | Evidence disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-0001 | Owner modularization decision 2026-08-27; predecessor requirement preserved in audit history | RB-01 | MUST | Modular tree, manifest, authority-map and checksum inspection. | PKG-01 / Project Owner / AI Governor | RT-01 | ACTIVE | TSK-0001..TSK-0092 | ED-OPEN |
| REQ-0002 | Owner decision 2026-08-27 | RB-01 | MUST | Authority and reconciliation audit. | PKG-01 / Project Owner / AI Governor | RT-01 | ACTIVE | TSK-0001..TSK-0092 | ED-OPEN |
| REQ-0003 | Owner decision 2026-08-27 | RB-01 | MUST | Schema/state-transition audit. | PKG-01 / Project Owner / AI Governor | RT-01 | ACTIVE | TSK-0003 | ED-OPEN |
| REQ-0004 | Owner decision 2026-08-27 | RB-01 | MUST | Gate evidence audit. | PKG-01 / Project Owner / AI Governor | RT-01 | ACTIVE | TSK-0004 | ED-OPEN |
| REQ-0005 | Owner decision 2026-08-27 | RB-01 | MUST | Write/read-back verification test. | PKG-01 / Project Owner / AI Governor | RT-01 | ACTIVE | TSK-0005 | ED-OPEN |
| REQ-0006 | Owner decision 2026-08-27 | RB-01 | MUST | Task-register completeness validation. | PKG-01 / Project Owner / AI Governor | RT-01 | ACTIVE | TSK-0006 | ED-OPEN |
| REQ-0007 | CURRENT_STATE.md; owner prompt | RB-02 | MUST | Product baseline review. | PKG-02 / Project Owner / Product | RT-02 | ACTIVE | TSK-0093..TSK-0163 | ED-OPEN |
| REQ-0008 | Owner decision 2026-08-27 | RB-02 | MUST | Requirements-to-journey trace and usability test. | PKG-02 / Project Owner / Product | RT-02 | ACTIVE | TSK-0093..TSK-0163 | ED-OPEN |
| REQ-0009 | Owner decision 2026-08-27 | RB-02 | MUST | Brand/product copy review. | PKG-02 / Project Owner / Product | RT-02 | ACTIVE | TSK-0095 | ED-OPEN |
| REQ-0010 | Owner decision 2026-08-27 | RB-02 | MUST | End-to-end account/payment-free journey test. | PKG-02 / Project Owner / Product | RT-02 | ACTIVE | TSK-0096 | ED-OPEN |
| REQ-0011 | Owner decision 2026-08-27 | RB-02 | MUST | Scope, data model, and journey audit. | PKG-02 / Project Owner / Product | RT-02 | ACTIVE | TSK-0097 | ED-OPEN |
| REQ-0012 | Owner decision 2026-08-27 | RB-02 | MUST | Authority matrix audit. | PKG-02 / Project Owner / Product | RT-02 | ACTIVE | TSK-0098 | ED-OPEN |
| REQ-0013 | EXPERIMENT_01_CONCIERGE_VALIDATION.md | RB-03 | MUST | Protocol and cohort evidence review. | PKG-03 / Product Research | RT-03 | ACTIVE | TSK-0164..TSK-0197 | ED-OPEN |
| REQ-0014 | Owner decision 2026-08-27 | RB-03 | MUST | Protocol/non-goal audit. | PKG-03 / Product Research | RT-03 | ACTIVE | TSK-0164..TSK-0197 | ED-OPEN |
| REQ-0015 | Owner decision 2026-08-27 | RB-03 | MUST | Session record and intervention audit. | PKG-03 / Product Research | RT-03 | ACTIVE | TSK-0166 | ED-OPEN |
| REQ-0016 | Owner decision 2026-08-27 | RB-03 | MUST | Analysis report review. | PKG-03 / Product Research | RT-03 | ACTIVE | TSK-0167 | ED-OPEN |
| REQ-0017 | Owner decision 2026-08-27 | RB-03 | MUST | Pilot evidence index audit. | PKG-03 / Product Research | RT-03 | ACTIVE | TSK-0168 | ED-OPEN |
| REQ-0018 | VALIDATION_READINESS_GATE.md | RB-04 | MUST | Gate authorization and evidence audit. | PKG-04 / Privacy / Legal / Project Owner | RT-04; explicit override: before first real England participant | ACTIVE | TSK-0198..TSK-0296 | ED-OPEN |
| REQ-0019 | Owner decision 2026-08-27 | RB-04 | MUST | Data inventory/LIA/DPIA comparison. | PKG-04 / Privacy / Legal / Project Owner | RT-04 | ACTIVE | TSK-0198..TSK-0296 | ED-OPEN |
| REQ-0020 | Owner decision 2026-08-27 | RB-04 | MUST | Notice-to-configuration/claims review. | PKG-04 / Privacy / Legal / Project Owner | RT-04 | ACTIVE | TSK-0200 | ED-OPEN |
| REQ-0021 | Owner decision 2026-08-27 | RB-04 | MUST | Data-flow/log/storage inspection. | PKG-04 / Privacy / Legal / Project Owner | RT-04 | ACTIVE | TSK-0201 | ED-OPEN |
| REQ-0022 | Owner instruction 2026-08-27; prior owner decision 2026-08-27 | RB-04 | MUST | Executed record/self-assessment evidence or current verified non-applicability evidence. | PKG-04 / Privacy / Legal / Project Owner | RT-04; explicit override: 2027-08-27 or earlier owner reactivation, before first real England participant | ACTIVE / SATISFACTION DEFERRED — intentionally unresolved until 2027-08-27 or earlier reactivation | TSK-0202 | ED-OPEN |
| REQ-0023 | Owner decision 2026-08-27 | RB-04 | MUST | Change-trigger checklist and gate evidence. | PKG-04 / Privacy / Legal / Project Owner | RT-04; explicit override: reassess before release after material data/product/vendor/geography change | ACTIVE | TSK-0203 | ED-OPEN |
| REQ-0024 | Owner decision 2026-08-27 | RB-05 | MUST | Brand-system completeness audit. | PKG-05 / Brand / Product Owner | RT-05 | ACTIVE | TSK-0297..TSK-0305 | ED-OPEN |
| REQ-0025 | Owner decision 2026-08-27 | RB-05 | MUST | Lifecycle/dependency audit. | PKG-05 / Brand / Product Owner | RT-05 | ACTIVE | TSK-0297..TSK-0305 | ED-OPEN |
| REQ-0026 | Owner decision 2026-08-27 | RB-05 | MUST | Cross-surface design QA. | PKG-05 / Brand / Product Owner | RT-05 | ACTIVE | TSK-0299 | ED-OPEN |
| REQ-0027 | Owner decision 2026-08-27 | RB-05 | MUST | Asset inventory/version inspection. | PKG-05 / Brand / Product Owner | RT-05 | ACTIVE | TSK-0300 | ED-OPEN |
| REQ-0028 | Owner decision 2026-08-27 | RB-06 | MUST | Journey friction audit. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0306..TSK-0351 | ED-OPEN |
| REQ-0029 | Owner decision 2026-08-27 | RB-06 | MUST | Supported-platform journey test. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0306..TSK-0351 | ED-OPEN |
| REQ-0030 | Owner decision 2026-08-27 | RB-06 | MUST | State-model/copy/E2E assertion test. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0308 | ED-OPEN |
| REQ-0031 | Owner decision 2026-08-27 | RB-06 | MUST | Journey coverage and usability test. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0309 | ED-OPEN |
| REQ-0032 | Owner decision 2026-08-27 | RB-06 | MUST | Design-to-build gate audit. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0310 | ED-OPEN |
| REQ-0033 | Owner technical-stack interview 2026-08-27 | RB-06 | MUST | Automated plus focused manual accessibility/browser/device evidence. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0311 | ED-OPEN |
| REQ-0034 | Owner technical-stack interview 2026-08-27; DEC-0045 | RB-06 | MUST | i18n/RTL architecture, locale-content and pseudo/real-locale tests. | PKG-06 / UX / Service Design / Content | RT-06; explicit override: first public release, with official non-UK activation separately gated by LG-16 | ACTIVE | TSK-0312 | ED-OPEN |
| REQ-0035 | Owner decision 2026-08-27 | RB-06 | MUST | Instruction catalogue and currency audit. | PKG-06 / UX / Service Design / Content | RT-06 | ACTIVE | TSK-0313 | ED-OPEN |
| REQ-0036 | Owner technical-stack interview 2026-08-27 | RB-07 | MUST | Architecture/source/layout plus E2E test. | PKG-07 / Software / Frontend / Backend Engineering | RT-07 | ACTIVE | TSK-0352..TSK-0401 | ED-OPEN |
| REQ-0037 | Owner technical-stack interview 2026-08-27; DEC-0042 | RB-07 | MUST | Anonymous E2E, data-boundary and admin-surface review. | PKG-07 / Software / Frontend / Backend Engineering | RT-07 | ACTIVE | TSK-0352..TSK-0401 | ED-OPEN |
| REQ-0038 | Owner technical-stack interview 2026-08-27 | RB-07 | MUST | Storage/schema/provider/retention inspection. | PKG-07 / Software / Frontend / Backend Engineering | RT-07 | ACTIVE | TSK-0354 | ED-OPEN |
| REQ-0039 | Owner decision 2026-08-27 | RB-07 | MUST | Requirements/design traceability audit. | PKG-07 / Software / Frontend / Backend Engineering | RT-07 | ACTIVE | TSK-0355 | ED-OPEN |
| REQ-0040 | Owner technical-stack interview 2026-08-27 | RB-07 | MUST | CI/CD, test, deploy, secret and rollback verification. | PKG-07 / Software / Frontend / Backend Engineering | RT-07; explicit override: every application release as applicable | ACTIVE | TSK-0356 | ED-OPEN |
| REQ-0041 | Owner decision 2026-08-27 | RB-07 | MUST | Deferred-exception audit. | PKG-07 / Software / Frontend / Backend Engineering | RT-07; explicit override: future persistence/account capability only after its trigger and owner decision | ACTIVE / FUTURE EXCEPTION DEFERRED UNTIL TRIGGER + OWNER DECISION | TSK-0357 | ED-OPEN |
| REQ-0042 | CURRENT_STATE.md | RB-08 | MUST | Decision and change-control audit. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0402..TSK-0427 | ED-DIRECT |
| REQ-0043 | CURRENT_STATE.md | RB-08 | MUST | Configuration and network verification. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0402..TSK-0427 | ED-DIRECT |
| REQ-0044 | Owner decision 2026-08-27 | RB-08 | MUST | Configuration/filesystem/runtime inspection. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0404 | ED-DIRECT |
| REQ-0045 | Owner decision 2026-08-27 | RB-08 | MUST | Configuration/runtime record inspection. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0405 | ED-DIRECT |
| REQ-0046 | Owner decision 2026-08-27 | RB-08 | MUST | Endpoint/profile/instruction compatibility test. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0406 | ED-DIRECT |
| REQ-0047 | Owner decision 2026-08-27 | RB-08 | MUST | Filter acceptance and change-rehearsal evidence. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0407 | ED-DIRECT |
| REQ-0048 | Owner decision 2026-08-27 | RB-08 | MUST | Device/network matrix evidence. | PKG-08 / Network / DNS Engineering | RT-08 | ACTIVE | TSK-0408 | ED-DIRECT |
| REQ-0049 | Owner technical-stack interview 2026-08-27; CURRENT_STATE.md | RB-09 | MUST | VM handoff, Azure metadata, region/data-path and separation verification. | PKG-09 / Cloud / Platform Engineering | RT-09 | ACTIVE | TSK-0428..TSK-0482 | ED-DIRECT |
| REQ-0050 | Owner technical-stack interview 2026-08-27; DEC-0043 | RB-09 | MUST | Architecture/ADR and live topology review. | PKG-09 / Cloud / Platform Engineering | RT-09 | ACTIVE | TSK-0428..TSK-0482 | ED-DIRECT |
| REQ-0051 | Owner technical-stack interview 2026-08-27 | RB-09 | MUST | Clean owner-provided server execution and acceptance report. | PKG-09 / Cloud / Platform Engineering | RT-09 | ACTIVE | TSK-0430 | ED-OPEN |
| REQ-0052 | Owner technical-stack interview 2026-08-27 | RB-09 | MUST | Timed clean-server restore/rebuild drill. | PKG-09 / Cloud / Platform Engineering | RT-09 | ACTIVE | TSK-0431 | ED-PROVEN |
| REQ-0053 | Owner technical-stack interview 2026-08-27 | RB-09 | MUST | Static review, repeat-run, failure-injection, secret scan and direct-host verification. | PKG-09 / Cloud / Platform Engineering | RT-09 | ACTIVE | TSK-0432 | ED-OPEN |
| REQ-0054 | Owner technical-stack interview 2026-08-27 | RB-09 | MUST | Operational/platform backup/restore audit. | PKG-09 / Cloud / Platform Engineering | RT-09 | ACTIVE | TSK-0433 | ED-OPEN |
| REQ-0055 | Owner decision 2026-08-27 | RB-10 | MUST | Threat-model coverage review. | PKG-10 / Security | RT-10 | ACTIVE | TSK-0483..TSK-0495 | ED-OPEN |
| REQ-0056 | Owner technical-stack interview 2026-08-27 reconciled to project security safeguard | RB-10 | MUST | External scan/access/secret/privilege verification. | PKG-10 / Security | RT-10 | ACTIVE | TSK-0483..TSK-0495 | ED-OPEN |
| REQ-0057 | Owner decision 2026-08-27 | RB-10 | MUST | Abuse/load/failure tests. | PKG-10 / Security | RT-10 | ACTIVE | TSK-0485 | ED-DIRECT |
| REQ-0058 | Owner decision 2026-08-27 | RB-10 | MUST | Release security evidence audit. | PKG-10 / Security | RT-10; explicit override: before release where critical/high vulnerability or control failure exists | ACTIVE | TSK-0486 | ED-OPEN |
| REQ-0059 | Owner decision 2026-08-27 | RB-10 | MUST | Diagnostic procedure and deletion test. | PKG-10 / Security | RT-10 | ACTIVE | TSK-0487 | ED-OPEN |
| REQ-0060 | Owner decision 2026-08-27 | RB-11 | MUST | Metric-catalogue audit. | PKG-11 / Product Analytics | RT-11 | ACTIVE | TSK-0496..TSK-0509 | ED-OPEN |
| REQ-0061 | Owner decision 2026-08-27 | RB-11 | MUST | Event/schema/storage inspection. | PKG-11 / Product Analytics | RT-11 | ACTIVE | TSK-0496..TSK-0509 | ED-OPEN |
| REQ-0062 | Owner decision 2026-08-27 | RB-11 | MUST | Data-quality and analysis reproduction. | PKG-11 / Product Analytics | RT-11 | ACTIVE | TSK-0498 | ED-OPEN |
| REQ-0063 | Owner decision 2026-08-27 | RB-11 | MUST | Gate-to-metric traceability. | PKG-11 / Product Analytics | RT-11; explicit override: each applicable evidence-dependent gate | ACTIVE | TSK-0499 | ED-OPEN |
| REQ-0064 | Owner decision 2026-08-27 | RB-11 | MUST | Periodic data-minimization audit. | PKG-11 / Product Analytics | RT-11 | ACTIVE | TSK-0500 | ED-OPEN |
| REQ-0065 | Owner decision 2026-08-27 | RB-12 | MUST | Traceability matrix audit. | PKG-12 / QA / Release Acceptance | RT-12 | ACTIVE | TSK-0510..TSK-0537 | ED-OPEN |
| REQ-0066 | Owner decision 2026-08-27 | RB-12 | MUST | Master test-plan coverage review. | PKG-12 / QA / Release Acceptance | RT-12 | ACTIVE | TSK-0510..TSK-0537 | ED-OPEN |
| REQ-0067 | Owner decision 2026-08-27 | RB-12 | MUST | Acceptance evidence inspection. | PKG-12 / QA / Release Acceptance | RT-12 | ACTIVE | TSK-0512 | ED-OPEN |
| REQ-0068 | Owner decision 2026-08-27 | RB-12 | MUST | Defect/control register audit. | PKG-12 / QA / Release Acceptance | RT-12; explicit override: integrated release, pilot and production acceptance | ACTIVE | TSK-0513 | ED-OPEN |
| REQ-0069 | Owner decision 2026-08-27 | RB-12 | MUST | Corrective-action/regression linkage audit. | PKG-12 / QA / Release Acceptance | RT-12 | ACTIVE | TSK-0514 | ED-OPEN |
| REQ-0070 | Owner technical-stack interview 2026-08-27 | RB-13 | MUST | Probe/metric/alert/runbook test. | PKG-13 / SRE / Operations | RT-13 | ACTIVE | TSK-0538..TSK-0557 | ED-OPEN |
| REQ-0071 | Owner decision 2026-08-27 | RB-13 | MUST | Incident record audit. | PKG-13 / SRE / Operations | RT-13 | ACTIVE | TSK-0538..TSK-0557 | ED-OPEN |
| REQ-0072 | Owner technical-stack interview 2026-08-27 | RB-13 | MUST | Azure backup plus restore/rebuild drill evidence. | PKG-13 / SRE / Operations | RT-13 | ACTIVE | TSK-0540 | ED-OPEN |
| REQ-0073 | Owner technical-stack interview 2026-08-27 | RB-13 | MUST | Maintenance/change/rollback audit. | PKG-13 / SRE / Operations | RT-13 | ACTIVE | TSK-0541 | ED-OPEN |
| REQ-0074 | Owner decision 2026-08-27 | RB-13 | MUST | Operating-model and customer communication audit. | PKG-13 / SRE / Operations | RT-13 | ACTIVE | TSK-0542 | ED-OPEN |
| REQ-0075 | Owner decision 2026-08-27 | RB-14 | MUST | Budget and campaign-spend reconciliation. | PKG-14 / Growth / Communications / Partnerships | RT-14 | ACTIVE | TSK-0558..TSK-0583 | ED-OPEN |
| REQ-0076 | Owner decision 2026-08-27 | RB-14 | MUST | Channel plan and spend audit. | PKG-14 / Growth / Communications / Partnerships | RT-14 | ACTIVE | TSK-0558..TSK-0583 | ED-OPEN |
| REQ-0077 | Owner decision 2026-08-27 | RB-14 | MUST | Channel portfolio audit. | PKG-14 / Growth / Communications / Partnerships | RT-14 | ACTIVE | TSK-0560 | ED-OPEN |
| REQ-0078 | Owner decision 2026-08-27 | RB-14 | MUST | Content inventory/source/value audit. | PKG-14 / Growth / Communications / Partnerships | RT-14 | ACTIVE | TSK-0561 | ED-OPEN |
| REQ-0079 | Owner decision 2026-08-27 | RB-14 | MUST | Account/channel register audit. | PKG-14 / Growth / Communications / Partnerships | RT-14 | ACTIVE | TSK-0562 | ED-OPEN |
| REQ-0080 | Owner decision 2026-08-27 | RB-14 | MUST | Channel decision evidence review. | PKG-14 / Growth / Communications / Partnerships | RT-14 | ACTIVE | TSK-0563 | ED-OPEN |
| REQ-0081 | Owner decision 2026-08-27 | RB-15 | MUST | Roadmap/budget/task audit. | PKG-15 / Project Owner / Finance | RT-15; explicit override: no fundraising program during first two years absent new owner decision | ACTIVE / NO-FUNDRAISING HOLD THROUGH FIRST TWO YEARS ABSENT OWNER CHANGE | TSK-0584..TSK-0627 | ED-OPEN |
| REQ-0082 | Owner decision 2026-08-27 | RB-15 | MUST | Calculation/source audit. | PKG-15 / Project Owner / Finance | RT-15 | ACTIVE | TSK-0584..TSK-0627 | ED-OPEN |
| REQ-0083 | Owner accepted payment defaults 2026-08-27 | RB-15 | MUST | Payment/product/terms/provider/currency E2E review. | PKG-15 / Project Owner / Finance | RT-15; explicit override: before live supporter payments | ACTIVE | TSK-0586; TSK-0588; TSK-0590; TSK-0592; TSK-0593; TSK-0595; TSK-0596 | ED-OPEN |
| REQ-0084 | Owner technical-stack interview 2026-08-27 | RB-15 | MUST | Provider/vendor/reconciliation audit. | PKG-15 / Project Owner / Finance | RT-15; explicit override: before and during live supporter payments | ACTIVE | TSK-0587; TSK-0592; TSK-0595 | ED-OPEN |
| REQ-0085 | Owner decision 2026-08-27 | RB-15 | MUST | Decision/trigger audit. | PKG-15 / Project Owner / Finance | RT-15; explicit trigger: 500 active users causes organizational/commercial review only | ACTIVE | TSK-0588 | ED-OPEN |
| REQ-0086 | Owner decision 2026-08-27 | RB-16 | MUST | Self-service journey and issue simulation. | PKG-16 / Customer Experience / Product Operations | RT-16 | ACTIVE | TSK-0628..TSK-0641 | ED-OPEN |
| REQ-0087 | Owner decision 2026-08-27 | RB-16 | MUST | Root-cause/backlog audit. | PKG-16 / Customer Experience / Product Operations | RT-16 | ACTIVE | TSK-0628..TSK-0641 | ED-OPEN |
| REQ-0088 | Owner decision 2026-08-27 | RB-16 | MUST | Case schema and deletion verification. | PKG-16 / Customer Experience / Product Operations | RT-16 | ACTIVE | TSK-0630 | ED-OPEN |
| REQ-0089 | Owner decision 2026-08-27 | RB-16 | MUST | Event/metric audit. | PKG-16 / Customer Experience / Product Operations | RT-16 | ACTIVE | TSK-0631 | ED-OPEN |
| REQ-0090 | Owner decision 2026-08-27 | RB-16 | MUST | Lifecycle journey test. | PKG-16 / Customer Experience / Product Operations | RT-16 | ACTIVE | TSK-0632 | ED-OPEN |
| REQ-0091 | Owner decision 2026-08-27 | RB-16 | MUST | Scenario/rehearsal evidence. | PKG-16 / Customer Experience / Product Operations | RT-16 | ACTIVE | TSK-0633 | ED-OPEN |

## Coverage and orphan analysis

- Canonical requirement IDs covered by this derived view: `REQ-0001` through `REQ-0091` = **91 requirements**.
- Every canonical requirement row has a non-empty source, priority, owning package, verification/acceptance-test definition and implementation-task mapping.
- The current authoritative runtime reports deterministic planning validation with **0 broken links** and **0 generated missing task IDs**.
- Therefore, against the currently validated canonical relationship system, this derivation identifies **0 orphan requirements**. No requirement is removed or silently authorised by TSK-0145.
- Requirement status and evidence disposition are intentionally separate from WBS/runtime task execution states.

## Verification candidate result

Against `ACC-0145`, this artifact provides a row for every current canonical requirement with source, derived rationale, priority, acceptance test, owner, derived release target, requirement disposition/status, implementing task reference and conservative evidence disposition. The source set is 91/91 covered and no orphan mapping is identified in the current deterministically validated relationship system.

**Publication/read-back is required before TSK-0145 may be recorded PASS.**
