# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-27  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`  
**Runtime authority:** this file owns volatile execution state. Planning authority is the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and mapped by `Plans/Master/MANIFEST.yaml`. The WBS owns task definitions/dependencies; the relationship index owns traversal; Layer 5 owns execution/evidence rules. Generated views and external trackers are non-authoritative.

## Canonical planning activation

**Status: ACTIVE / OWNER-FROZEN / PUBLISHED / READ-BACK VERIFIED.**

- Owner freeze: **PASS — TSK-0017**, explicit owner acceptance at `2026-08-27T19:38:36Z`.
- Frozen planning publication commit: `fce408f34470c0a0883ab978685b5265fdec4b97`.
- Frozen `Plans/` subtree Git tree: `e6c78a67a191e04ea85fbb68caf18b854067c3de`.
- Deterministic planning validation: **PASS — 641 tasks, 849 dependency edges, 0 broken links, 51/51 checksum entries**.
- `TSK-0009`: **PASS** — frozen planning tree published to `main`.
- `TSK-0011`: **PASS** — exact publication/read-back identity verified.
- `TSK-0010`: **PASS** — runtime checkpoint rebaselined to the frozen modular authority.

The planning freeze does not imply deployment, participant activation, supporter-payment activation, or public launch.

## Owner communication constraint

Latest explicit owner instruction at `2026-08-27T20:17:22Z`: routine status, reminders, execution summaries, and next-step outputs must **not surface owner-suppressed deferred work** unless the owner explicitly reactivates it. The frozen WBS remains authoritative for its stored dispositions; this communication instruction changes what is surfaced, not historical evidence.

## Frozen project/product identity

- Brand/domain: **UseSafeWeb / UseSafeWeb.com**.
- Product: **UseSafeWeb — First Phone Safety Setup**.
- Initial customer: parent/caregiver around a roughly 10–12-year-old child's first independently used smartphone.
- Initial validation market: England / UK.
- Trust posture: **Simple guardrails. Clear limits. No invasive monitoring.**
- Backend: **AdGuard Home**, frozen unless a verified critical blocker requires reopening.
- Core baseline: **accountless-first** under `DEC-0042`; no mandatory account, persistent parent dashboard, or customer-facing AdGuard control plane unless `EXC-0001` is explicitly activated after validated need and owner approval.
- Topology/recovery baseline under `DEC-0043`: one AdGuard node initially; owner supplies separate fresh Ubuntu 24.04 LTS Azure VMs for AdGuard/DNS and web/app; Azure control-plane provisioning/configuration is owner-managed; direct-host Bash deployment/recovery; approximately 30-minute recovery accepted; tested rebuild/restore required.
- Hosting provider: Microsoft Azure.
- Experiment-1 DNS region: Azure West Europe (`westeurope`), Netherlands.
- Selected upstream: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard remains the filtering/policy layer.

## Business/product decision

Business evaluation phases 1–42 remain complete.

**Decision: MODIFY — PROCEED TO VALIDATION, NOT FULL LAUNCH.**

No integrated product build is authorised before the applicable behavioral/product gates. Full launch remains unauthorised.

## Current gate

### LG-03 — Validation Readiness

**State: IN PROGRESS / TECHNICAL TARGET ACTIVE.**

Current preserved readiness facts:

- owner/environment fact collection completed;
- Azure West Europe selected for Experiment 1;
- mandatory AdGuard privacy target remains: persistent identifiable query logging off, file query logging off, identifiable per-client statistics off/excluded unless justified, IP anonymisation where operational records can contain addresses, ECS off, selected Quad9 DoH upstream, no browsing-history/top-domain product metric, diagnostics necessary/time-boxed/deleted;
- Experiment 1 protocol remains designed but execution/recruitment is not authorised until the applicable gates PASS.

## Owner inputs reconciled

### TSK-0438 — UseSafeWeb.com registrar/DNS control and renewal state

**State: PASS.**

Project Owner explicitly confirmed the domain-side task is complete and `UseSafeWeb.com` is registered/currently controlled. This owner-controlled condition requires no further screenshot unless explicitly reopened.

### TSK-0435 — owner-provided Azure `westeurope` pilot VM handoff

**State: PASS.**

Target: `srv.UseSafeWeb.com` / Azure VM `adguardvm`.

Acceptance evidence is durably recorded in `TSK_0435_HANDOFF_EVIDENCE_2026-08-27.md`, final blob `57de1a4187288870da7655973ac09bf907674d89`, following target runs at `2026-08-27T20:34:37Z` and `2026-08-27T20:41:57Z` with verifier `infrastructure/adguard-server/verify-handoff.sh` blob `0264b6ad15554fd289f4bdbf0ee49b9e959e7843`.

Final accepted result:

- Ubuntu `24.04`: PASS.
- Azure IMDS reachable and parsed: PASS.
- Azure location `westeurope`: PASS.
- Azure OS type Linux: PASS.
- VM identity `adguardvm`, size `Standard_B2ls_v2`: recorded.
- Approved SSH deployment path: PASS on the non-privileged rerun.
- `srv.UseSafeWeb.com` resolves on-target to `52.157.109.120`: PASS.
- Fresh-handoff exposure inventory: only SSH externally listening (`0.0.0.0:22`, `[::]:22`) plus expected loopback/system listeners; no AdGuard listener yet.
- IMDS public IPv4 field absent: warning/not-applicable only, not an acceptance failure.
- Final verifier status: **`OVERALL=PASS failures=0 warnings=1`**.
- Evidence contains no credential, token, private key, subscription/resource ID, or raw DNS history.

ACC-0435 is fully satisfied. The earlier sudo-run SSH-environment failure is retained in the evidence artifact for auditability and is superseded for acceptance by the clean rerun.

## Preserved PASS preparation evidence

- `TSK-0434`, `TSK-0436` — owner-control-plane exclusions verified; actual host/security verification remains separate.
- `TSK-0166` — participant metric schema — `EXPERIMENT_01_CONCIERGE_VALIDATION.md`.
- `TSK-0168` — qualification screener — `EXPERIMENT_01_CONCIERGE_VALIDATION.md`.
- `TSK-0225` — protection-claims checklist — `PROTECTION_CLAIMS_CHECKLIST.md`, blob `4bfc83421318fe761d06f9a63e052e3bff36070a`.
- `TSK-0227` — exceptional diagnostic procedure — `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md`, blob `f9e1bb52582a69bc385aa69c93d02febb7b5cffa`.
- `TSK-0228` — child-safety escalation boundary — `CHILD_SAFETY_ESCALATION_PROCEDURE.md`, blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`.
- `TSK-0214` — retention/deletion checklist — `RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`.
- `TSK-0165` — facilitator/intervention guide — `EXPERIMENT_01_FACILITATOR_GUIDE.md`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`.
- `TSK-0169` — support/false-positive intake — `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`, blob `9fab42f97e3e96023de89a8ed266acc21c0f06ab`.
- Current recurring governance checkpoint evidence remains in `LG_03_CHECKPOINT_2026-08-27.md`.

## Newly unlocked technical state

- `TSK-0435`: PASS.
- `TSK-0438`: PASS.
- `TSK-0437` — apply host security baseline: **TODO / eligible**; target is now accepted and reachable.
- `TSK-0440` — select pilot encrypted-DNS hostname/path: **TODO / eligible**; VM and domain prerequisites are satisfied.
- `TSK-0439`, `TSK-0441`, `TSK-0442`, `TSK-0443`: remain dependency-driven downstream work.
- `TSK-0483` — resolver abuse/amplification protection: target-environment prerequisite is now available; execute when its remaining WBS dependencies permit.

Security/host hardening takes precedence over endpoint design under the project priority rules.

## Runtime safeguards

- Runtime states are only `TODO`, `WAITING`, `BLOCKED`, `PASS`; no persistent RUNNING/claim/lease state.
- PASS requires all applicable current acceptance criteria with durable/reconstructable evidence.
- Secrets, tokens, credentials, private keys and unnecessary personal/raw DNS data must not be committed to GitHub.
- No real participant activation until the applicable gates permit it.
- No public launch until later production/launch gates pass.
- No Azure control-plane mutation by project automation under the current owner handoff boundary.

## Current execution direction

Proceed with `TSK-0437` host-security baseline first, persisting a stable outcome before selecting the next eligible task. Then recompute eligibility; `TSK-0440` is independently available unless a new current security/technical blocker changes priority.
