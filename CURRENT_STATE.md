# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`  
**Runtime authority:** this file owns volatile execution state. Planning authority is the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and mapped by `Plans/Master/MANIFEST.yaml`. The WBS owns task definitions/dependencies; the relationship index owns traversal; Layer 5 owns execution/evidence rules. Generated views and external trackers are non-authoritative.

## Canonical planning activation

**Status: ACTIVE / OWNER-FROZEN / PUBLISHED / READ-BACK VERIFIED.**

- Owner freeze: **PASS — TSK-0017**, explicit owner acceptance at `2026-08-27T19:38:36Z`.
- Manifest schema: `usesafeweb.master-planning-system.v1.1`.
- Frozen planning publication commit on `main`: `fce408f34470c0a0883ab978685b5265fdec4b97`.
- Repository tree at that publication commit: `937818821a6e537fba36ac39f740d3efa5b36499`.
- Canonical `Plans/` subtree Git tree: `e6c78a67a191e04ea85fbb68caf18b854067c3de`.
- `Plans/SHA256SUMS.txt` SHA-256: `8d34fc3389898d3543124d80ee596220ad80d098f565283046c186511d8f4b26`.
- Deterministic planning validation: **PASS — 641 tasks, 849 dependency edges, 0 broken links, 51/51 checksum entries**.
- Publication verification: the GitHub `main` `Plans/` subtree tree SHA exactly matched the validated publication kit tree SHA, proving identical paths, modes and blob bytes; branch/read-back comparison after fast-forward was identical.
- **TSK-0009: PASS** — owner-frozen `Plans/` tree published to `main` with no unrelated publication changes.
- **TSK-0011: PASS** — canonical GitHub publication/read-back identity verified against the approved local package.
- **TSK-0010: PASS** — runtime checkpoint references the frozen modular authority and actual LG-03 state; exact GitHub read-back confirmed.

The planning freeze does **not** imply deployment, legal clearance, participant activation, supporter-payment activation or public launch.

## Frozen project/product identity

- Public brand/domain: **UseSafeWeb / UseSafeWeb.com**.
- Product: **UseSafeWeb — First Phone Safety Setup**.
- Initial customer: parent/caregiver around a roughly 10–12-year-old child's first independently used smartphone.
- Initial validation market: England / UK.
- Trust posture: **Simple guardrails. Clear limits. No invasive monitoring.**
- Backend: **AdGuard Home**, frozen unless a verified critical blocker requires reopening.
- Core product baseline: **accountless-first** under `DEC-0042`; no mandatory UseSafeWeb account, persistent parent identity/dashboard or customer-facing AdGuard control plane unless `EXC-0001` is explicitly activated after validated need and owner approval.
- Recovery/topology baseline under `DEC-0043`: one AdGuard node initially; owner supplies two separate fresh Ubuntu 24.04 LTS Azure VMs (AdGuard/DNS and web/app); Azure control-plane provisioning/configuration is owner-managed; direct-host Bash deployment/recovery; approximately 30-minute recovery accepted; tested rebuild/restore required.
- Hosting provider: **Microsoft Azure**.
- Experiment-1 child-linked DNS region: **Azure West Europe (`westeurope`), Netherlands**.
- Selected upstream: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard remains the filtering/policy layer.

## Business/product decision

Business evaluation phases 1–42 remain complete.

**Decision: MODIFY — PROCEED TO VALIDATION, NOT FULL LAUNCH.**

No MCP/integrated product build is authorised before the applicable behavioral/product gates. Full launch remains unauthorised.

## Current gate

### LG-03 — Validation Readiness (legacy G-02)

**State: IN PROGRESS.** Technical/privacy/security/operational readiness may proceed. LG-03 cannot PASS for real-participant activation while required legal evidence remains unresolved unless current verified evidence establishes non-applicability.

Current preserved readiness facts:

- owner/environment fact collection completed;
- Azure West Europe selected for Experiment 1;
- controller facts remain individual / Netherlands / pre-revenue;
- mandatory AdGuard privacy target remains: persistent identifiable query logging off, file query logging off, identifiable per-client statistics off/excluded unless justified, IP anonymisation where operational records can contain addresses, ECS off, selected Quad9 DoH upstream, no browsing-history/top-domain product metric, diagnostics necessary/time-boxed/deleted;
- Experiment 1 protocol remains designed but execution/recruitment is not authorised until LG-03 and LG-04 PASS.

## Owner legal-work hold

`OWNER_LEGAL_HOLD_2026-08-27` remains active through **2027-08-27** unless the owner explicitly reactivates it earlier.

- Exactly **26** WBS tasks remain `Plan_Status=DEFERRED` + runtime `WAITING` under this hold.
- Historical legal/privacy/compliance evidence is preserved; the hold does not rewrite prior PASS evidence.
- The hold is not a waiver, exemption, legal-clearance proof or LG-03 evidence.
- Real England participant activation remains blocked if required legal evidence is still unresolved when activation is considered.

## Current technical and preparation execution state

- Azure control-plane creation/configuration: **owner-managed / outside project execution**.
- `TSK-0434` and `TSK-0436`: **NOT_APPLICABLE + PASS** as verified exclusions only; they are not proof of live Azure implementation/security.
- `TSK-0435` — verify owner-provided Azure `westeurope` pilot VM handoff: **WAITING** until the fresh Ubuntu 24.04 LTS AdGuard/DNS VM exists, is reachable and approved access metadata is available without exposing secrets.
- `TSK-0438` — verify current UseSafeWeb.com DNS/registrar control and renewal state: **WAITING**. Current repository/history preserves that the domain was acquired but does not contain direct current registrar account-control, renewal/expiry or authorised DNS-zone control evidence; no connected registrar/DNS account integration is available. Deterministic resolution check: provider-authorised read/change evidence or equivalent registrar/DNS control evidence must show the ownership path, current renewal/expiry state and responsible owner without exposing credentials/secrets.
- `TSK-0483` — resolver abuse/amplification protection: **WAITING** for an actual reachable resolver/target environment even though its planning predecessor exclusions are satisfied.
- `TSK-0166` — create pseudonymous participant record and metric schema: **PASS**. Evidence: `EXPERIMENT_01_CONCIERGE_VALIDATION.md` blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`, §5 Mandatory measurements plus §9/§11 privacy/aggregate rules, reviewed 2026-08-27 against ACC-0166 / REQ-0013, REQ-0014, REQ-0015, CON-0025, CON-0009 and INT-0005. It contains participant ID, qualification, device/path, safeguard state, activation, time, assistance, abandonment, comprehension, false-positive and 14-day fields; it expressly excludes browsing/domain-history metrics. Predecessors `TSK-0223` and `TSK-0164` are PASS. Deviations: none against ACC-0166.
- `TSK-0168` — create qualification screener: **PASS**. Evidence: `EXPERIMENT_01_CONCIERGE_VALIDATION.md` blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`, §2 Cohort qualification, reviewed 2026-08-27 against ACC-0168 / REQ-0013, REQ-0014, REQ-0017, CON-0025, CON-0009 and INT-0005. It covers caregiver responsibility, first-phone age/stage, phone timing, iPhone/Android platform, willingness to make real safety-setting changes and non-surveillance fit; it does not require exact DOB or child name. Predecessor `TSK-0164` is PASS. Deviations: none against ACC-0168.
- `TSK-0225` — create protection-claims checklist: **PASS**. Evidence: `PROTECTION_CLAIMS_CHECKLIST.md` commit `bc0a9dd773ee3ebd53b6aad216ded00c88f38fb5`, blob `4bfc83421318fe761d06f9a63e052e3bff36070a`, read back 2026-08-27. The checklist directly tests `Protected — verified`, `Configured — parent confirmed`, `Action needed`, `Not covered`, DNS scope/limits, app/service limits, VPN/alternate secure DNS/Private Relay uncertainty, removal/recovery, and narrow exception handling; failures downgrade/block claims rather than infer coverage. Predecessor `TSK-0219` is PASS. Deviations: none against ACC-0225.
- `TSK-0227` — create exceptional diagnostic-logging procedure: **PASS**. Evidence: `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md` commit `8db17d22e0c21dd224ce50d2473010125f92aa1b`, blob `f9e1bb52582a69bc385aa69c93d02febb7b5cffa`, read back 2026-08-27. The runbook requires incident/ticket ID, necessity, exact approved fields/scope, approver, explicit UTC start/end, restricted access, user-notice decision, deletion owner, baseline restoration and recorded deletion verification; it prohibits open-ended logging, GitHub raw logs and reuse for analytics/profiling. Predecessor `TSK-0224` is PASS. Deviations: none against ACC-0227.
- `TSK-0228` — define child-safety concern and disclosure escalation boundary: **PASS**. Evidence: `CHILD_SAFETY_ESCALATION_PROCEDURE.md` commit `067e21119b89f2a072507e7f860a71d62983ff91`, blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`, read back 2026-08-27; official England/UK routes were reverified the same date from GOV.UK, NSPCC/Childline and CEOP. The procedure separates product support from safeguarding, sends immediate danger to 999, provides local children's social care/101, NSPCC, Childline and CEOP routes as applicable, limits data capture, keeps personal/raw disclosures out of GitHub and escalates internally to the Project Owner. Predecessor `TSK-0219` is PASS. Deviations: none against ACC-0228.
- `TSK-0214` — create retention/deletion execution checklist: **PASS**. Evidence: `RETENTION_DELETION_EXECUTION_CHECKLIST.md` commit `cbe1b42165be3d9403c1df49bcf6b62a5cdfab50`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`, read back 2026-08-27. The checklist identifies controlled data locations, responsible owners, per-participant and experiment-close deletion triggers/due-date fields, deletion and verification methods, aggregate/anonymised outputs, GitHub exclusions, and fail-closed exception handling. Predecessors `TSK-0224` and `TSK-0166` are PASS. Deviations: none against ACC-0214.
- `TSK-0165` — create facilitator script and intervention taxonomy: **PASS**. Evidence: `EXPERIMENT_01_FACILITATOR_GUIDE.md` commit `3236c556fb1bbb30a6be826c1d43aac32771d66d`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`, read back 2026-08-27. The guide preserves the frozen hypothesis and journey, requires intervention duration/reason, separates usability help, safety/privacy correction and safeguarding escalation, and prohibits silent facilitator completion; participant actions and any facilitator-performed action are explicitly recorded. Predecessors `TSK-0166` and `TSK-0228` are PASS. Deviations: none against ACC-0165.
- `TSK-0169` — create pilot support and false-positive intake process: **PASS**. Evidence: `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md` commit `f89a3865c083bec669bf494fa2ea2a0614c472f2`, blob `9fab42f97e3e96023de89a8ed266acc21c0f06ab`, read back 2026-08-27. Every issue requires pseudonymous participant ID, category, severity, intervention minutes, privacy-safe evidence, action, outcome and closure; exceptional request-level diagnostics route through TSK-0227, false positives use narrow/reversible correction and re-test, and safeguarding routes through TSK-0228. Predecessors `TSK-0227` and `TSK-0165` are PASS. Deviations: none against ACC-0169.

## Runtime safeguards

- Runtime states are only `TODO`, `WAITING`, `BLOCKED`, `PASS`; no persistent RUNNING/claim/lease state.
- PASS requires all applicable current acceptance criteria with durable/reconstructable evidence.
- Secrets, tokens, credentials, private keys and unnecessary personal/raw DNS data must not be committed to GitHub.
- No real participant activation until LG-03 and LG-04 permit it.
- No public launch until the later production/launch gates pass.
- No Azure control-plane mutation by project automation under the current owner handoff boundary.

## Exact next execution path

1. Continue independent eligible non-deferred LG-03 preparation while `TSK-0435`, `TSK-0438` and target-environment work wait.
2. Reconcile existing canonical artifacts before creating duplicates; mark PASS only where every current acceptance criterion is directly evidenced.
3. Recompute eligibility after every confirmed durable mutation.
4. Do not recruit/activate real participants until LG-03 and LG-04 PASS.
