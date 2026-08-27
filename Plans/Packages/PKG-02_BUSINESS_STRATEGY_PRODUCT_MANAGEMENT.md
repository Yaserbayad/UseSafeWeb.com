# PKG-02 - Business Strategy & Product Management

> **Layer 3 package module.** This file is a semantic retrieval map. It intentionally does not duplicate structured entity definitions that appeared in the monolithic Layer 3 package view. Those definitions have one authoritative owner after migration.

## Governing context

- Charter and package boundaries: [Layer 2 - Package Charters](../Layers/LAYER_2_PACKAGE_CHARTERS.md) — `PKG-02`.
- Package/lifecycle obligations: [Lifecycle Obligations Register](../Registers/LIFECYCLE_OBLIGATIONS.md) — filter `Package=PKG-02`.
- Phase definitions: [Phase Register](../Registers/PHASES.md) — filter `Parent package=PKG-02`.
- Deliverable definitions: [Deliverable Register](../Registers/DELIVERABLES.md) — filter `Package=PKG-02`.
- Work-package definitions: [Work-Package Register](../Registers/WORK_PACKAGES.md) — filter `Package=PKG-02`.
- Executable task definitions: [Authoritative WBS](../WBS/master-wbs.csv) — filter `Package_ID=PKG-02`.
- Acceptance/verification/evidence: [Verification, Evidence and Acceptance Register](../Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md) using task IDs from the WBS.
- Risks, decisions, interfaces and requirements: traverse by stable IDs through [RELATIONSHIP_INDEX.yaml](../RELATIONSHIP_INDEX.yaml).

## Source Layer-3 transformation

The monolith's `PKG-02 Master Plan` package summary and its repeated lifecycle/phase/deliverable/work-package/task tables were classified as **redundant structured views (duplication class B)** because the same entities are completely defined in the Section 6 master registers. They were therefore replaced by these references without changing any IDs, hierarchy, status, dependency, acceptance, evidence, authority, or lifecycle semantics.
