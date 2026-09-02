# TSK-0587 — Project Owner Decision Packet: Development Resource, Cost and Tool Envelope

**Status:** PREPARED — HUMAN_ONLY decision required  
**Date:** 2026-09-02  
**Task authority:** `TSK-0587 — Approve development resource, cost, and tool envelope`  
**Dependencies:** `TSK-0586` PASS; `TSK-0047` PASS  
**Acceptance:** each required role/cost has an assigned source or explicit gap; critical gaps block LG-07; approved limit, contingency and cost-review cadence are recorded.

## 1. Decision now required

The Project Owner must explicitly approve or replace the development resource/cost/tool envelope. AI may prepare this packet but may not perform the approval because TSK-0587 is `A1 / HUMAN_ONLY`.

## 2. Recommended resource and tool envelope

| Need | Recommended source | Current status / fence |
|---|---|---|
| Product/program/architecture/engineering/security/privacy-engineering/QA/SRE/release/accessibility/content work | ChatGPT Business as primary reasoning/development executor; GitHub Actions for independent deterministic checks; Codex only when repository shell/build/test/runtime execution materially improves correctness | Available for `AUTO_ALLOWED` work; human-only decisions remain owner-controlled |
| Source control / durable authority | Private GitHub repository `Yaserbayad/UseSafeWeb.com`, `main` canonical | Available |
| CI / verification | Existing GitHub Actions entitlement/runners where applicable | Exact incremental billed amount remains unconfirmed; no paid expansion authorized by this packet |
| DNS backend | Self-hosted AdGuard Home on owner-provided Ubuntu 24.04 LTS DNS VM | Existing architecture; software licence fee currently evidenced as $0; VM/network cost is owner-existing/unconfirmed |
| Web/application host | Owner-provided Ubuntu 24.04 LTS web/app VM | Existing architecture; exact Azure SKU/invoice remains unconfirmed |
| Optional account authentication | Firebase Authentication base Google/social route only | Current service-fee assumption $0 on the approved base route; no SMS/phone/MFA/paid Identity Platform activation authorized |
| Optional account datastore | Minimum privacy-safe persistence implementation selected during build within the approved spend envelope | Product/vendor and exact price remain an explicit implementation gap; if no compliant zero-incremental-cost option exists, return to owner before paid activation |
| Secrets | Existing secure owner/runtime mechanism or zero-incremental-cost mechanism satisfying security acceptance | Exact service remains an explicit implementation choice; Git is never an alternative secret store |
| Monitoring/alerting | Privacy-safe existing/self-hosted/included capability first | Exact paid service is not pre-authorized; return to owner if a paid dependency becomes necessary |
| Human authority | Project Owner | Required for HUMAN_ONLY tasks, material spend, scope/policy changes and other current fences |

## 3. Recommended financial envelope

The existing TSK-0586 baseline deliberately does not invent the owner's current Azure/domain/infrastructure bill. Therefore the safest executable development envelope is defined around **incremental new spend**, not an invented all-in monthly total.

### Recommended approval

- **Incremental new recurring or one-time development spend without a new owner approval:** `0` in the applicable billing currency.
- **Existing owner-provided/owner-paid resources and subscriptions:** may be used within their existing entitlement and current frozen architecture, with no automatic upgrade, resize, new paid SKU, paid plan activation, or increased commitment.
- **Contingency pre-authorized:** `0`; a newly required paid service/SKU/plan is a deterministic return-to-owner condition, not an implied contingency draw.
- **Cost review cadence:**
  1. before any action that would create/increase paid commitment;
  2. at each lifecycle gate where the accepted cost/resource assumption is material;
  3. monthly after production has measurable recurring operating cost, or earlier if a TSK-0237 vendor price/quota trigger fires.
- **Unconfirmed existing costs:** Azure VM/disk/network/egress, datastore, secrets, monitoring, CI incremental amount and domain renewal remain explicitly unconfirmed until their actual source/invoice/selected product is available. They must not be guessed or represented as zero.

This envelope maximizes autonomous development while preventing accidental spend. It does not require that all existing owner-paid infrastructure itself costs zero.

## 4. Critical-gap disposition under the recommended envelope

- **No engineering-role critical gap is identified for L6 planning/execution:** current `AUTO_ALLOWED` work can use the approved AI/GitHub execution model; genuine human-only decisions remain separately fenced.
- **No new-spend critical gap is accepted silently:** if an L6 acceptance criterion cannot be satisfied using existing entitlement or a zero-incremental-cost option, the affected task becomes BLOCKED/returns to owner before any paid activation.
- **Existing Azure/runtime bill is not a blocker to this specific development envelope** because the owner already provides the two frozen VMs; however the actual operating-cost total remains unconfirmed and must be reconciled from real billing evidence when it becomes material.
- **Datastore/secrets/monitoring selection remains implementation-bounded:** selection must satisfy privacy/security/recovery requirements and the approved cost envelope; paid activation is not pre-authorized.

## 5. What approval would unlock

If the Project Owner approves the recommended envelope exactly, TSK-0587 can be evidenced and persisted as PASS. Then TSK-0051 (LG-07 architecture and delivery readiness) becomes dependency-eligible because TSK-0052 and TSK-0049 are already current PASS; LG-07 still requires its own complete acceptance verification before any L6 build begins.

## 6. Exact owner approval language

To approve the recommendation without adding scope or spend authority, the Project Owner can state:

> **Approve TSK-0587 recommended envelope:** use existing owner-provided/owner-paid resources and current ChatGPT Business/GitHub/Codex execution capabilities; authorize no incremental paid service, SKU, plan upgrade, resize or new paid commitment without a new owner decision; contingency is zero; review cost before any paid activation, at material lifecycle gates, and monthly after measurable production recurring cost begins. Explicit unconfirmed existing-cost and implementation-selection gaps remain non-guessed and must return to me if they require new spend.

Any different budget cap, contingency, paid tool/service allowance, staffing source, or review cadence should be stated explicitly instead.

## Non-inference

Preparation of this packet is not TSK-0587 approval or PASS, does not authorize spend, does not close any unconfirmed cost, and does not make LG-07 or L6 PASS.
