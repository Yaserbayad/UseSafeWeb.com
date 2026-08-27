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
- Selected client resolver identity: `dns.usesafeweb.com`.
- Canonical iPhone DoH endpoint: `https://dns.usesafeweb.com/dns-query`.
- Native Android pilot transport: DoT to `dns.usesafeweb.com` on TCP 853, under the frozen DoH/DoT-where-supported package boundary.

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

### TSK-0437 — apply host security baseline

**State: WAITING — target execution required; design/artifact complete.**

The exact frozen WBS row is `A3 / AUTO_ALLOWED`, HIGH, critical-path, and requires idempotent/reversible execution. ACC-0437 requires: only required ports/services exposed; restricted admin access; current patches applied; baseline evidence captured.

Prepared artifact:

- `infrastructure/adguard-server/harden-host.sh`
- GitHub commit: `60f1ab7eec5ca1ba232868594ac53bf945aee7e0`
- GitHub blob: `fa93e592d8fd2ad4cd81cb4531dbfd6e3191fe30`
- Local SHA-256 of byte-identical tested content: `3bf342d7181126d8cafd43b5a41b4e10447ae10241b1f1adef9aa8e2733b4313`
- `bash -n`: PASS.
- Negative/fail-closed sandbox test: PASS — the script refused a non-target environment instead of applying changes.
- ShellCheck was not available in the sandbox; an attempted sandbox install exceeded the tool execution window, so no ShellCheck result is claimed.

The script is grounded in current Ubuntu documentation for UFW, unattended security updates and OpenSSH configuration. It is intentionally bounded: it applies available Ubuntu upgrades; enables scheduled unattended security updates; requires proof that the current SSH session authenticated with a public key before disabling password/keyboard-interactive/direct-root SSH; uses an early OpenSSH drop-in with syntax/effective-value checks and rollback on SSH/UFW application failure; enables UFW default-deny inbound/default-allow outbound while retaining SSH only; disables UFW logging at this stage; audits effective SSH settings, UFW rules, pending upgrades and external listeners. It refuses to layer UFW when `nftables.service` is active.

**Deterministic target action:** from the existing non-root SSH session, execute:

`bash harden-host.sh --apply`

Do **not** prepend `sudo`; the wrapper intentionally captures the original SSH session context and then elevates only the bounded apply stage.

Stable result semantics:

- `OVERALL=PASS` → bind output as target evidence and promote TSK-0437 to PASS after GitHub persistence/read-back.
- `OVERALL=WAITING_REBOOT` → patches/configuration are retained as valid partial work; reboot the VM, reconnect, run `sudo bash harden-host.sh --audit`, and promote only after clean PASS.
- `OVERALL=FAIL` → do not continue dependent host work; preserve the non-secret output, classify the exact failure, and correct only the proven cause.

### TSK-0440 — select pilot encrypted-DNS hostname and path

**State: PASS.**

Selected endpoint:

- hostname: `dns.usesafeweb.com`
- canonical DoH URL: `https://dns.usesafeweb.com/dns-query`
- path: `/dns-query`
- HTTPS port: 443
- `srv.usesafeweb.com` remains a separate host/administrative identity.

Durable decision/evidence:

- `infrastructure/adguard-server/DNS_ENDPOINT_DECISION.md`
- GitHub commit: `7d88c598e367f75a1bf2c4f8960ea41e5c066c21`
- GitHub blob: `9e0f15d0e1f11c892cf51317b705ac21c9563e53`
- local pre-publication SHA-256: `db029e1525cc83d9c50a5997da88bb6cd13c74ddaeb64d0d7339a94668ffac14`

Current AdGuard Home documentation was reviewed for the native `/dns-query` DoH route, TLS/certificate-name compatibility, HTTPS/DoH behavior, and reverse-proxy mode. A security adversarial review identified that AdGuard's documented HTTPS port may serve both web UI and DoH; the decision was corrected before publication so TSK-0440 selects only the stable client identity/path and does **not** force a TLS-termination architecture that could expose administration. Downstream deployment must keep the admin surface non-public: direct AdGuard TLS is acceptable only if that is proven; otherwise a same-host path-limited reverse proxy may expose only `/dns-query` and forward to loopback AdGuard DoH mode.

Additional boundary:

- the resolver DNS record is DNS-only/direct to the Azure resolver, not website-CDN/proxy fronted;
- no AAAA record until public IPv6 is verified;
- no user-specific ClientID hostname/path for the accountless Experiment-1 baseline.

ACC-0440 is fully satisfied: uniqueness, documentation, certificate compatibility, AdGuard compatibility, Network Engineering review and Security review all PASS.

### TSK-0439 — define supported pilot device configuration methods

**State: PASS.**

Durable artifact/evidence:

- `infrastructure/adguard-server/PILOT_DEVICE_DNS_CONFIGURATION_METHODS.md`
- GitHub commit: `06f99c199e9bdec6600e25deb24e152fec50fb99`
- GitHub blob: `f9af8b18cdc85bfe9b120661776172ab8581c2c9`
- official Apple, Android/Google and AdGuard Home documentation reviewed 2026-08-27.

Supported Experiment-1 phone methods:

- **iPhone / iOS 14+** — manually installed Apple DNS Settings profile using DoH at `https://dns.usesafeweb.com/dns-query`.
- **Android 9+ with a verifiable native Private DNS provider-hostname control** — DoT to `dns.usesafeweb.com` on TCP 853.

The artifact provides explicit install, verification, removal/restore and known-limit procedures for each supported family. It explicitly excludes older unsupported OS versions, Android variants without the required native control, app/VPN DNS substitutes, plaintext DNS, user-specific ClientID paths, and non-phone device classes from the Experiment-1 baseline. Verification is defined as platform configuration state plus a privacy-safe synthetic allowed/blocked DNS test set; server-side encrypted-transport evidence remains separately required. No ordinary browsing-history logging is needed.

ACC-0439 is fully satisfied: both supported platforms have install, verification, removal and known-limit methods; unsupported variants are explicit; the accountless/minimum-data and DoH/DoT-where-supported boundaries are preserved.

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

## Current technical state

- `TSK-0435`: PASS.
- `TSK-0438`: PASS.
- `TSK-0440`: PASS.
- `TSK-0439`: PASS.
- `TSK-0437`: WAITING only for target execution/verification of the published hardening artifact.
- `TSK-0441` — create public DNS records for the pilot endpoint: **WAITING on a supported DNS-provider execution path**. Desired record is not claimed created. Current tools expose no DNS-provider account connector/plugin.
- `TSK-0483` — implement resolver abuse/amplification protections: **WAITING on an actual resolver service/configuration surface**. The fresh accepted VM currently has no AdGuard listener/service, so its implementation/test acceptance cannot truthfully be satisfied yet.
- Later TLS/deployment tasks remain dependency-driven.

## Material technical sequencing issue

A current WBS dependency must be reconciled before the AdGuard installation chain can advance: `TSK-0203 — Install supported AdGuard release` currently depends on `TSK-0483`, while ACC-0483 requires implemented/tested resolver rate limiting/denial and amplification controls. The accepted fresh VM has no resolver service yet, so ACC-0483 cannot be executed/tested before a resolver exists. No false PASS is permitted. This is preserved as a technical dependency inconsistency to resolve through the smallest governed WBS correction before selecting TSK-0203/TSK-0483 execution.

## Runtime safeguards

- Runtime states are only `TODO`, `WAITING`, `BLOCKED`, `PASS`; no persistent RUNNING/claim/lease state.
- PASS requires all applicable current acceptance criteria with durable/reconstructable evidence.
- Secrets, tokens, credentials, private keys and unnecessary personal/raw DNS data must not be committed to GitHub.
- No real participant activation until the applicable gates permit it.
- No public launch until later production/launch gates pass.
- No Azure control-plane mutation by project automation under the current owner handoff boundary.

## Current execution boundary

The current LG-03/L2 autonomous tranche is now exhausted without fabricating external state:

1. **TSK-0437** is highest priority and needs the published hardening script executed on `srv.UseSafeWeb.com` from the existing non-root SSH session.
2. **TSK-0441** needs actual DNS-provider access/change execution; no supported connector is presently available.
3. **TSK-0483** cannot meet its acceptance until a resolver service exists, exposing the WBS dependency inconsistency described above.

Later L4/L5/L8/L12 tasks whose raw dependencies may already be PASS are not selected while the current LG-03/L2 technical gate has these unresolved conditions. Resume by reconciling the first changed condition, rereading current authority, and recomputing eligibility.
