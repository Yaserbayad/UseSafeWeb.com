# TSK-0051 — LG-07 Architecture and Delivery Readiness Decision

**Version:** 1.0.0  
**Date:** 2026-09-02  
**Gate:** `LG-07 — Architecture, Security, Privacy and Delivery Readiness`  
**Task:** `TSK-0051 — Decide LG-07 architecture and delivery readiness (legacy G-07)`  
**Authority:** A4 / `AUTO_ALLOWED` inside the frozen product, cost, security, privacy-engineering and delivery boundaries.  
**Decision candidate:** **PASS**, subject to independent verification and durable runtime synchronization.

## 1. Decision boundary

LG-07 accepts the smallest production-capable **architecture and implementation plan** when every objective requirement is evidenced. It unlocks L6 build only after evidence-complete PASS; therefore LG-07 does **not** require completed L6 implementation or target-environment production proof before the gate.

Read together with the gate contract, the ACC-0051 phrase requiring the "first vertical slice/checkpoint" to preserve the accountless core and implement the approved optional Version-1 account/session/dashboard boundary is applied as a **planned initial integrated implementation checkpoint**. It does not rewrite TSK-0048 task order and does not claim any L6 task is already implemented.

## 2. Direct dependency decision

| Dependency | Current decision/evidence | Result |
|---|---|---|
| `TSK-0587` | Owner-approved development resource/cost/tool envelope; zero incremental new spend without a new owner decision; contingency zero; current resource/cost gaps explicitly dispositioned | PASS |
| `TSK-0052 / LG-06` | Current dual-mode Version-1 product/brand/experience freeze with complete accountless core plus bounded optional parent-account/session/dashboard/device lifecycle | PASS |
| `TSK-0049` | Current LG-07 technical architecture/privacy-engineering/security/operations approval component | PASS |

All three direct TSK-0051 predecessors are current durable PASS.

## 3. LG-07 required-evidence matrix

| LG-07 evidence class | Current durable evidence | Gate conclusion |
|---|---|---|
| Architecture / ADRs / Version-1 boundary | `TSK-0321` dual-mode V1 architecture boundary; `TSK-0049` architecture approval component | Complete for L5 design boundary |
| Account/session model | `TSK-0356`, `TSK-0232`, `TSK-0049`; optional Google sign-in/server session remains bounded and never gates accountless core | Complete plan |
| Data / ownership / deletion / recovery | `TSK-0232`, `TSK-0234`, `TSK-0446`, `TSK-0518`, `TSK-0049` | Complete plan |
| Vendor / compatibility / terms-change monitoring | `TSK-0585`, `TSK-0237` | Complete technical/commercial monitoring boundary; legal interpretation remains external |
| Privacy engineering / data minimization / observability | `TSK-0498`, `TSK-0538`, `TSK-0539`, `TSK-0049` | Complete L5 plan |
| Security / threat / authz / CSRF / IDOR / isolation | `TSK-0485`, `TSK-0239`, `TSK-0049` | Complete L5 control plan; downstream implementation tests remain mandatory |
| Typed AdGuard integration | `TSK-0410`, consumed by `TSK-0049` | Complete design contract |
| Measurement / truth-state / operations | `TSK-0498`, `TSK-0539`, `TSK-0049` | Complete plan |
| Verification / acceptance test plan | `TSK-0516` — 32-case master VAT plan with accountless, optional-account, provider/session, authz/IDOR, ownership, DNS, Protection Map, deletion/recovery, privacy/security/accessibility and rollback coverage | Complete plan |
| Recovery / rollback / release checkpoints | `TSK-0047` plus accepted deletion/recovery sources | Complete plan; CR-0007 production-only lifecycle preserved |
| Implementation backlog | `TSK-0048` — all 76 current non-PASS L6 tasks represented exactly once in 55 dependency-ordered slices | Complete implementation plan |
| Infrastructure / operating cost | `TSK-0586` | Complete reproducible cost model with unconfirmed inputs explicit; no invented total |
| Resource / tool / incremental-spend envelope | `TSK-0587` | Owner-approved; no critical engineering-resource gap; zero incremental new spend without new owner decision |
| Residual risks | Current risk register plus `TSK-0049` control-plan review | Residual risks remain governed downstream; no unresolved High/Critical architecture/control-plan gap exists at the L5 design boundary |

## 4. Initial integrated implementation checkpoint — `CP-LG07-01`

`CP-LG07-01` is the first **integrated checkpoint**, not a replacement for the individual TSK-0048 slices. Canonical WBS dependencies and TSK-0048 slice order remain unchanged.

The checkpoint may close only when the dependency-ordered L6 work has produced both sides of the frozen Version-1 boundary:

1. **Accountless core remains complete without login:** public/start journey, anonymous state, routing/setup, DNS/configuration delivery and privacy-safe verification, truthful Protection Map, troubleshooting/removal/recovery and required native/external safeguard guidance are usable without authentication.
2. **Optional parent-account boundary is implemented:** Google sign-in and privacy-minimal server session; minimum parent/device ownership persistence; authenticated dashboard/device lifecycle; curated parent-owned controls; logout/revocation; account/device deletion/recovery.
3. **Security/privacy invariants hold:** server-side ownership checks, CSRF/IDOR/cross-parent isolation, opaque ClientID semantics, query/statistics-history suppression, prohibited-data checks and secret isolation pass their current acceptance tests.
4. **Release evidence is reconstructable:** exact source/config/version, applicable TSK-0516 VAT cases, rollback/recovery evidence and privacy-safe operations signals are retained.
5. **No scope regression:** mandatory login, browsing/query/activity history, child accounts and unrestricted customer DNS administration remain excluded.

TSK-0048 already represents the required work without changing task IDs or dependencies. Relevant optional-account slices include the server-session work beginning at Slice 30, ownership/account lifecycle work at Slice 34, dashboard shell at Slice 38, device provisioning/control work in later dependency waves, and account deletion/settings work before final feature-complete acceptance. Earlier accountless and foundation slices remain prerequisites according to the canonical dependency graph.

This checkpoint structure satisfies ACC-0051 without pretending that Slice 01 alone contains the entire V1 scope and without changing the accepted backlog.

## 5. Residual-risk disposition

The canonical risk register intentionally contains open Critical-exposure risks because many are implementation/operation risks (availability, abuse, false positives, privacy drift, supply chain, vendor/platform change, support sustainability and real-user validation). LG-07 requires those risks to have a production-capable design, mitigation, verification path, owner and contingency; it does not require future operational uncertainty to be eliminated before L6 begins.

Current TSK-0049 evidence explicitly finds **no unresolved High/Critical architecture/control-plan gap within the L5 technical/design component**. High/Critical controls remain blocking at their downstream L6/LG-08/LG-09 verification boundaries. A future contradiction reopens the affected PASS rather than being hidden by this gate decision.

`RSK-0002` human-behavior evidence remains explicitly accepted and non-blocking before L8 under DEC-0052/CR-0005. Legal/regulatory risks and `TSK-0240` remain owner-external for sequencing under CR-0009/DEC-0056; no legal compliance conclusion is created here.

## 6. Cost, authority and environment fences

- Approved incremental new development spend without another owner decision: **0**; contingency: **0**.
- Existing owner-provided/owner-paid resources may be used only within current entitlement/frozen architecture.
- Any new paid service/SKU/plan/resize or material commitment returns to the owner before activation.
- L6 implementation remains subject to each task's current Action Authority, exact dependencies and acceptance criteria.
- CR-0007/DEC-0054 remains controlling: CI/ephemeral verification is allowed; there is no mandatory persistent staging or pilot lifecycle. Production activation remains governed by later gates.
- CR-0009/DEC-0056 legal work remains owner-external; actual law/safety/security/platform/technical reality remains higher authority.

## 7. LG-07 decision

**PASS is justified** if independent verification confirms the current WBS/gate contracts, all direct predecessors, the evidence classes above, the residual-L5 frontier, and the initial integrated checkpoint semantics.

A successful TSK-0051 acceptance means LG-07 architecture/delivery readiness is PASS and L6 may become gate-eligible. It does not itself implement L6 work. `TSK-0050` must then persist the approved baseline/readiness decision in GitHub before the governed frontier is recomputed for actual L6 execution.

## Non-inference

This artifact does not claim completed L6 implementation, target-environment security testing, deployment, production activation, real-user validation, spend, launch, or legal/compliance PASS. Those remain governed by their own tasks and later gates.
