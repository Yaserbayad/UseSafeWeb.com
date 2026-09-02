# TSK-0586 — Pre-development Infrastructure and Operating Cost Baseline

**Task:** TSK-0586 — Build pre-development infrastructure and operating cost baseline  
**Acceptance / Verification / Evidence:** ACC-0586 / VER-0586 / EVD-0586  
**Lifecycle / Priority / Authority:** L5 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Gate:** contributes to LG-07 Architecture, Security, Privacy and Delivery Readiness  
**Direct predecessor:** TSK-0236 current PASS

## 1. Decision and evidence boundary

Freeze the **pre-development cost model and reconciliation method**, not a fabricated monthly bill.

The current canonical project evidence does **not** identify the exact Azure VM SKUs, disk SKUs, public-IP SKU, outbound-data tier, selected application datastore, selected secrets/monitoring service, or a current Azure invoice. Therefore an exact current monthly Azure/runtime total cannot be confirmed from canonical evidence and is deliberately recorded as **UNCONFIRMED** rather than guessed.

This is consistent with REQ-0082: every financial figure must be sourced and hypotheses must not be presented as forecasts. ACC-0586 also explicitly requires every unpriced risk to be made explicit rather than invented.

The model below is sufficient to reproduce low/base/high operating-cost envelopes once the missing exact inputs exist. It also records the currently evidenced zero-fee software/authentication assumptions separately from infrastructure cost so that `$0` vendor components can never be misrepresented as a `$0` service.

This task does **not**:

- create, resize, configure or purchase Azure resources;
- select a datastore, secrets service, monitoring vendor or paid plan;
- activate Firebase Authentication with Identity Platform, SMS/phone authentication or billing;
- accept vendor terms or contracts on behalf of the owner;
- authorize material/unbudgeted spend;
- create a fundraising program;
- treat supporter revenue as guaranteed cost coverage;
- invent a user/device/query/request forecast;
- infer LG-07, L6, production, payment or launch PASS.

## 2. Current authority and source register

| Input | Source / date | Current fact consumed | Cost treatment here |
| --- | --- | --- | --- |
| TSK-0586 task contract | `Plans/Master/WBS/master-wbs.csv`, current WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`, read 2026-09-02 | L5 / MEDIUM / A3 / AUTO_ALLOWED; dependency exactly TSK-0236; ACC requires sourced component costs, DNS/infrastructure/application separation, low/base/high scenarios and explicit unpriced risk | Governing acceptance |
| Capacity model | `TSK_0236_POST_CR0008_PILOT_INITIAL_LAUNCH_CAPACITY_MODEL_2026-09-02.md`, version `1.0.0-post-CR0008`, blob `bd2816ebf60ce6b160d5dbe3e303ca2faf96aeaf`, publication commit `c69cfa355721e5be413201f8a64675485d5f79f4` | Current future production load is unfrozen; numeric throughput/headroom is unproven; >=2x verified capacity is required over an approved expected peak; Azure scaling is evidence-triggered | No load/spend forecast invented |
| Current auth / AdGuard vendor review | `TSK_0585_CURRENT_AUTH_VENDOR_COST_TERMS_EXIT_REVIEW_2026-09-02.md`, blob `101fb63ed4367b514a36f5a07ee271be7cd7a5c3`, publication commit `fd8b89ef42509a092c17a0e140cc8236472cda1c`, official-source review dated 2026-09-02 | Base Firebase Authentication Google/social route has current `$0` authentication-service-fee assumption on Spark; no SMS path; Identity Platform optional. AdGuard Home self-hosted software licence cost `$0`; no separate AdGuard Home API subscription fee evidenced. Infrastructure remains separate. | Binding dated vendor assumptions, subject to refresh triggers |
| Azure topology constraint | `Plans/Master/Registers/CONSTRAINTS.md`, CON-0004, current read 2026-09-02 | Owner provides two Ubuntu 24.04 LTS VMs manually: one DNS/AdGuard VM and one web/app VM; Azure control-plane provisioning/configuration remains owner-managed | Two-VM topology is a quantity baseline, not a price |
| Optional account / free-core constraint | `Plans/Master/Registers/CONSTRAINTS.md`, CON-0010/CON-0011, current read 2026-09-02 | Complete core value remains usable without login and without card/trial; optional account exists; supporter mechanism follows value | Authentication/payment costs cannot become a prerequisite for core value |
| Bootstrapped/fundraising constraints | `Plans/Master/Registers/CONSTRAINTS.md`, CON-0012/CON-0013; `Plans/Master/Registers/REQUIREMENTS.md`, REQ-0081/REQ-0082, current read 2026-09-02 | Small bootstrapped AI-operated product; no fundraising program for approximately two years without a new owner decision; figures must be sourced | No fundraising or speculative financing included |
| Supporter requirement | `Plans/Master/Registers/REQUIREMENTS.md`, REQ-0083, current read 2026-09-02 | Approved future supporter choices are fixed GBP £2/month or £20/year, EUR €2/month or €20/year, USD $2/month or $20/year; no live FX; Stripe and PayPal; cancel anytime | Prices are product constraints only, not revenue forecasts |
| Economics interface | `Plans/Master/Registers/INTERFACES.md`, INT-0031, current read 2026-09-02 | Economics inputs must be sourced; scenarios are not forecasts; product/support implications explicit | Model/reporting rule |
| GTM budget interface | `Plans/Master/Registers/INTERFACES.md`, INT-0020, current read 2026-09-02 | USD 20–50 is a GTM discretionary budget boundary | **Excluded from infrastructure total**; not reused as infra budget |
| Sustainability risk | `Plans/Master/Registers/RISKS.md`, RSK-0005, current read 2026-09-02 | Support burden can make the free + supporter model unsustainable; economics must be updated from evidence | Remains OPEN; tracked separately from invented revenue |

### 2.1 CR-0006 reconciliation of inherited ACC wording

ACC-0586 contains inherited wording referring to the former accountless baseline and Firebase/auth being conditional on EXC-0001. Current higher authority DEC-0053/CR-0006 has activated the bounded optional-parent-account capability.

Accordingly, this baseline applies the current meaning:

- the **accountless core** still has no authentication-service dependency and no authentication-service fee;
- the **optional account path** is active in Version 1, with the current initial Firebase Google/social authentication route carrying the dated `$0` service-fee assumption from TSK-0585 while it remains on the current base Spark route and within current constraints;
- paid Identity Platform, SMS/phone auth, MFA messaging or another paid auth path is **not** activated or priced into the current baseline;
- any such change reopens the relevant vendor/cost/privacy/security review before reliance.

## 3. Cost accounting structure

Use one monthly normalized model for operating comparisons. Annual/non-monthly charges are amortized only for planning comparison and retain their actual billing cadence separately.

Define:

- `C_dns_vm` = actual monthly DNS/AdGuard VM compute charge;
- `C_web_vm` = actual monthly web/application VM compute charge;
- `C_disk` = actual monthly managed-disk/storage charges for both hosts;
- `C_backup` = actual monthly backup/snapshot/recovery-storage charges;
- `C_public_ip` = actual monthly public-IP/network fixed charges;
- `C_egress` = actual monthly metered outbound/network charge;
- `C_datastore` = actual monthly minimum optional-account datastore charge;
- `C_secrets` = actual monthly secrets/key-management charge if a paid service is selected;
- `C_monitoring` = actual monthly monitoring/logging/alerting charge if billable;
- `C_ci` = actual incremental monthly CI/build/runtime charge attributable to UseSafeWeb;
- `C_domain` = monthly-normalized domain/DNS/certificate charge where an actual paid line item exists;
- `C_other` = any other approved project operating line item with a source;
- `F_auth` = authentication service fee for the current active auth route;
- `F_adguard` = AdGuard Home software/API subscription fee.

Current total equation:

`C_month = C_dns_vm + C_web_vm + C_disk + C_backup + C_public_ip + C_egress + C_datastore + C_secrets + C_monitoring + C_ci + C_domain + C_other + F_auth + F_adguard`

A numeric `C_month` is **not valid** until every material non-zero/unknown component has an exact source or a documented zero-cost proof for the selected implementation.

## 4. Current component register

| Cost component | Current quantity / architecture fact | Current numeric amount | Source/date/assumption | Status / evidence required before numeric total |
| --- | --- | ---: | --- | --- |
| DNS/AdGuard Azure VM compute | 1 owner-provided Ubuntu 24.04 LTS DNS VM under CON-0004 | **UNCONFIRMED** | CON-0004; TSK-0236; 2026-09-02. Current canonical evidence contains no exact SKU/invoice. | Bind exact VM SKU, region, pricing model/discount and owner invoice/export. |
| Web/application Azure VM compute | 1 owner-provided Ubuntu 24.04 LTS web/app VM under CON-0004 | **UNCONFIRMED** | CON-0004; 2026-09-02. No exact SKU/invoice is canonical. | Bind exact VM SKU, region, pricing model/discount and owner invoice/export. |
| Managed disks/storage | At least storage needed by the two owner-provided VMs; exact SKU/size/billing not frozen here | **UNCONFIRMED** | TSK-0585 infrastructure-cost separation; 2026-09-02 | Exact disk/storage SKU, size, redundancy and invoice/pricing source. |
| Backup/snapshot/recovery storage | Required only according to accepted recovery/data contracts; production A-domain backup remains separately constrained | **UNCONFIRMED** | TSK-0236 plus current recovery/data boundaries; 2026-09-02 | Exact selected backup mechanism, retained scope, schedule, storage amount, legal/privacy authority and price. |
| Public IP / fixed network services | Exact current Azure network SKUs not recorded canonically | **UNCONFIRMED** | CON-0004 topology boundary; 2026-09-02 | Exact public-IP/network SKU and bill/export. |
| Network egress | Future workload envelope is unfrozen; no billable egress volume is invented | **UNCONFIRMED** | TSK-0236; 2026-09-02 | Actual meter/rate plus measured privacy-safe aggregate volume or approved synthetic envelope. |
| Quad9 upstream | Exact dns10 endpoint is frozen; no project-specific paid upstream contract/line item is evidenced in the current cost authority | **UNCONFIRMED / no charge asserted** | TSK-0411/TSK-0236 topology evidence; 2026-09-02 | Do not assign `$0` unless a current authoritative vendor/payment source proves it; reopen if a paid term appears. |
| AdGuard Home software licence | Self-hosted AdGuard Home | **$0 software licence fee** | TSK-0585 official-source review dated 2026-09-02 | Recheck on licence/distribution/integration change. GPL obligations are not reduced to a price question. |
| AdGuard Home API subscription | Self-hosted documented REST/OpenAPI | **No separate API subscription fee evidenced** | TSK-0585 official-source review dated 2026-09-02 | Recheck if API/commercial model changes. Do not treat absence of a fee as a perpetual guarantee. |
| Accountless-core authentication service | Accountless core does not use authentication | **$0** | DEC-0053/CR-0006 + CON-0010/0011; current 2026-09-02 | Structural design fact; reopens only if owner changes mandatory-login boundary. |
| Optional-account base Firebase Authentication | Google/social only; base Spark route; no SMS/phone/MFA/Identity Platform activation | **$0 service-fee assumption** | TSK-0585 official-source review dated 2026-09-02 | Refresh vendor pricing/limits/terms before consequential provider change/paid activation and monitor quota/threshold triggers. |
| Identity Platform / SMS / phone / paid auth | Not active in current V1 route | **$0 current spend; not authorized as active service** | TSK-0585; 2026-09-02 | If proposed, obtain current exact provider price/terms and applicable authority before activation. |
| Optional-account datastore | Logical minimum persistence required; product/vendor not yet selected by this task | **UNCONFIRMED** | TSK-0233/0232/0234 architecture; 2026-09-02 | Exact datastore product, region, quota, backup/retention model, price and legal/privacy acceptance. |
| Secrets/key management | Exact implementation not selected here | **UNCONFIRMED** | TSK-0585 infrastructure categories and current security boundary; 2026-09-02 | Selected mechanism and incremental project price; never place secrets in Git to avoid cost. |
| Monitoring/logging/alerting | Required evidence/operations capability; provider/cost not frozen here | **UNCONFIRMED** | TSK-0236 observability requirements; 2026-09-02 | Selected service/tool and actual incremental price. Prohibited DNS/browsing history may not be enabled to obtain observability. |
| CI/build/runtime | Exact incremental project charge not canonically identified | **UNCONFIRMED** | Current delivery architecture; 2026-09-02 | Actual project-attributable billed amount or documented included/no-incremental-cost entitlement. |
| Domain/DNS/certificate renewal | UseSafeWeb.com is frozen identity but current renewal/billing amount is not recorded in the cost authority used by this task | **UNCONFIRMED** | CON-0001 and current domain boundary; 2026-09-02 | Exact registrar/DNS/certificate charge and renewal cadence. |
| Support labour / owner time | Economic risk exists, but no current paid staffing commitment or measured production support load is available | **UNPRICED NON-CASH / FUTURE ACTUAL** | RSK-0005; 2026-09-02 | Track measured active support minutes/volume when real operation exists; do not invent wage or opportunity-cost rate. |
| GTM discretionary spend | Separate growth budget | **Excluded from this infrastructure model** | INT-0020; CON-0014 | Track under GTM economics, not as infrastructure. |
| Fundraising | Not an operating program | **$0 planned program spend in this baseline** | REQ-0081; CON-0013 | Requires a new owner decision to create a fundraising program. |

## 5. Low / base / high scenarios

These are **planning envelopes, not forecasts**. They deliberately preserve unresolved variables instead of fabricating prices or demand.

### 5.1 LOW — minimum pre-development / architecture floor

Purpose: represent the smallest currently frozen infrastructure topology without optional paid expansions.

Quantity assumptions:

- `n_dns = 1` DNS VM;
- `n_web = 1` web/app VM;
- no mandatory staging environment under DEC-0054/CR-0007;
- no extra DNS region/node;
- no paid Identity Platform/SMS/phone auth;
- no paid acquisition/GTM amount inside this model;
- no fundraising program;
- only the storage/network/domain components actually required by the two-host architecture.

Formula:

`C_low = C_dns_vm + C_web_vm + C_disk_low + C_public_ip_low + C_egress_low + C_domain + F_auth + F_adguard + C_other_low`

Current known fee terms:

- `F_auth = $0` for the current initial base Google/social authentication-service path and `$0` for the accountless core;
- `F_adguard = $0` software licence; no separate API subscription fee is evidenced.

**Current numerical result:** **UNCONFIRMED** because Azure/network/storage/domain inputs are not fully priced in canonical evidence.

### 5.2 BASE — smallest production-capable Version-1 operating envelope

Purpose: represent the intended LG-07/L6 design target once the selected minimum persistence, recovery, secret and observability components are frozen.

Quantity assumptions:

- same one-DNS-VM + one-web/app-VM baseline unless evidence proves another topology is required;
- minimum optional-account datastore needed by approved persistence/ownership semantics;
- backup/recovery mechanism required by accepted recovery/data contracts;
- minimum secret handling and operational monitoring required for production capability;
- current accountless-first + optional-account product boundary unchanged;
- no separate mandatory staging environment;
- current auth and AdGuard vendor fee assumptions unchanged until a refresh trigger.

Formula:

`C_base = C_low + C_backup + C_datastore + C_secrets + C_monitoring + C_ci + Delta_disk + Delta_network + C_other_base`

`Delta_*` means only the additional amount over the LOW envelope; no double counting is allowed.

**Current numerical result:** **UNCONFIRMED** until exact selected services/SKUs and current prices/invoices are bound.

### 5.3 HIGH — evidence-triggered scale / resilience envelope

Purpose: bound future cost reasoning if measured capacity/reliability evidence requires more resources. It is not preauthorization to scale.

Let:

- `n_dns >= 1` = evidence-justified DNS node count;
- `n_web >= 1` = evidence-justified web/app instance count;
- `C_scaled_data`, `C_scaled_backup`, `C_scaled_monitoring`, `C_scaled_network` = exact selected scaled-service costs.

Formula:

`C_high = n_dns*C_dns_vm + n_web*C_web_vm + C_scaled_disk + C_scaled_backup + C_scaled_network + C_scaled_datastore + C_scaled_secrets + C_scaled_monitoring + C_scaled_ci + C_domain + F_auth_scaled + F_adguard + C_other_high`

Rules:

1. `n_dns`, `n_web`, workload and traffic quantities remain **UNFROZEN** until evidence supplies them.
2. TSK-0236 requires >=2x verified capacity over the approved expected peak; this is a **capacity margin**, not an instruction to double infrastructure spend.
3. Diagnose/optimize first; reduce the supported/ramped envelope when necessary; scale only on evidence.
4. CON-0004 keeps Azure control-plane actions owner-managed. This cost scenario cannot create/resize resources.
5. New region/US node, material spend, new contracts, new paid provider tiers and market changes retain their own authority.

**Current numerical result:** **UNCONFIRMED by design**; presenting a dollar high case without exact scale quantities and source prices would violate REQ-0082.

## 6. Source-binding procedure for the missing prices

Before any numeric total is relied upon, bind each unknown component to an evidence row containing:

1. provider/service and exact product/SKU/tier;
2. exact region and billing currency;
3. pricing model (PAYG/reservation/credit/discount or other actual owner arrangement);
4. price source URL, invoice/export, contract or provider statement;
5. source timestamp and effective period;
6. quantity/unit assumption and owner of that quantity;
7. formula from unit price x quantity to monthly-normalized amount;
8. tax/credit treatment if material and actually known;
9. whether the value is an **actual**, **approved budget**, **quoted price**, or **scenario assumption**;
10. refresh trigger/expiry.

Do not back-solve a VM SKU from observed CPU/RAM alone. TSK-0236's historical 2-vCPU/~3.82-GiB snapshot is point-in-time resource evidence and explicitly is not a pricing/SKU or capacity-throughput claim.

## 7. Monthly operating reconciliation

Once operating bills exist, calculate:

- `Actual_month` = sum of project-attributable invoiced/billed operating line items for the month;
- `Fixed_month` = charges independent of measured workload within the current tier;
- `Variable_month` = metered network/storage/request/usage charges;
- `Support_minutes_month` = measured active human support minutes, recorded separately from cash cost unless an actual paid rate/contract exists;
- `Cost_per_verified_active_device` only after both `Actual_month` and an approved privacy-safe verified-active denominator exist.

Rules:

- no DNS query/domain/browsing-history data is needed or permitted to calculate infrastructure cost;
- no supporter conversion rate/revenue is assumed merely because fixed supporter prices are approved;
- no Stripe/PayPal revenue is netted against cost before actual provider/payment evidence exists;
- owner time remains a separate non-cash sustainability signal until a sourced valuation method is explicitly approved;
- refunds, credits, discounts and taxes are recorded from actual source records, not estimated silently;
- material unexplained variance reopens the affected cost assumption before later gate reliance.

## 8. Cost control and refresh triggers

Recalculate or reopen the affected part of this baseline when any of the following occurs:

- exact Azure SKU/region/pricing model or invoice becomes available;
- VM/disk/network/backup topology changes;
- expected load or `C_verified` changes enough to trigger TSK-0236 capacity review;
- a datastore/secrets/monitoring/CI product is selected or changes tier;
- Firebase Authentication pricing, limits, processing facts or terms materially change;
- Identity Platform, SMS/phone auth, MFA messaging or another paid auth capability is proposed;
- AdGuard Home licence/API/commercial model or frozen version changes materially;
- domain/DNS/certificate provider or renewal price changes;
- a new region/node/resilience topology is proposed;
- a material contract or unbudgeted spend is required;
- actual monthly cost materially diverges from the last source-bound envelope;
- support burden activates RSK-0005 sustainability review.

## 9. Budget and authority boundaries

- **Azure control plane:** CON-0004 remains owner-managed. This artifact can identify a cost/scale need but cannot perform the Azure action.
- **Material spend/new contracts:** retain their current human authority where applicable.
- **GTM:** the USD 20–50/month discretionary GTM boundary is separate and is not an infrastructure budget.
- **Supporter mechanism:** fixed prices are product constraints, not revenue forecasts or permission to gate core safety.
- **Fundraising:** no fundraising program for approximately two years absent a new owner decision.
- **Free core:** no card/trial/login requirement may be introduced to make the cost model work.

If the smallest production-capable architecture cannot be sustained within later approved cost authority, the correct action is to reduce/re-architect/review scope under current governance—not to invent funding, silently weaken protection/privacy/recovery, or create unauthorized spend.

## 10. Known unpriced risks

| Risk | Why unpriced now | Safe disposition |
| --- | --- | --- |
| Exact Azure monthly compute | VM SKUs/invoice not in canonical evidence | Require owner-provided billing/SKU evidence; no guessed price |
| Disk/public IP/network/egress | Exact SKU/tier/usage absent | Bind provider meter + actual/synthetic approved quantity |
| Datastore | Product/tier not selected | Keep cost unknown until architecture selection and privacy/legal constraints are satisfied |
| Backup/recovery storage | Final production backup mechanism and account-data backup conditions not fully frozen | Price only after exact mechanism/scope/retention is approved |
| Secrets/monitoring/CI | Exact paid implementation not selected/incremental entitlement not proven | Bind actual selected service/entitlement before numeric total |
| Domain/DNS/certificate | Current renewal amount absent from this canonical cost evidence | Bind registrar/provider invoice/renewal record |
| Support burden | No production users/actual support observations yet | Measure real active minutes/volume later; no invented wage/rate |
| Future scale | Load and node counts unfrozen | Use TSK-0236 evidence triggers; do not pre-buy or forecast |
| Optional paid auth | Not part of current initial route | Reopen vendor/cost/security/privacy review before activation |

## 11. ACC-0586 trace

| ACC-0586 element | Evidence in this artifact | Disposition |
| --- | --- | --- |
| source/date/assumption for each cost | Sections 2, 4, 6 | SATISFIED; unknown values explicitly identify missing evidence |
| separate Azure/infrastructure, DNS and application costs | Sections 3–5 | SATISFIED |
| accountless baseline has no authentication-service cost/dependency | Sections 2.1, 4 | SATISFIED under current CR-0006 semantics |
| Firebase/auth cost conditional/current optional-account treatment | Sections 2.1, 4, 8 | SATISFIED: optional account active; initial base Google/social route uses current `$0` fee assumption; paid variants require reopen |
| low/base/high scenarios | Section 5 | SATISFIED as source-bound equations/envelopes, explicitly not forecasts |
| every unpriced risk explicit rather than invented | Sections 1, 4, 6, 10 | SATISFIED |
| current project constraints preserved | Sections 1, 7–9 | SATISFIED |

## 12. Candidate stable disposition

**Candidate ACC-0586 = PASS**, subject to VER-0586 read-back/reviewer inspection of this exact artifact and durable runtime synchronization.

This candidate PASS means a reproducible, source-disciplined pre-development infrastructure/operating cost baseline exists. It deliberately does **not** claim that the current Azure monthly bill is known, that an infrastructure budget has been approved, that a datastore/provider has been selected, that paid authentication/payment processing is active, that supporter revenue exists, that fundraising is authorized, that scaling is authorized, that RSK-0005 or RSK-0001 is closed, that LG-07 has passed, or that L6/public production/launch is authorized.