# UseSafeWeb.com — Current Authoritative State

**Updated:** 2026-08-28T10:08:00Z  
**Branch:** `main`  
**Mode:** `SERIAL LIGHT`

`CURRENT_STATE.md` owns volatile runtime state only. Planning authority remains the owner-frozen modular system rooted at `Plans/Master/MASTER_PLAN.md` and routed by `Plans/Master/MANIFEST.yaml`; WBS owns task definitions/dependencies, relationship index owns traversal, and Layer 5 owns execution/evidence rules.

## Canonical planning authority

**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0001 PUBLISHED AND READ-BACK VERIFIED.**

- Current validated `Plans/` tree: `c42616e92f0624aaf5caf788b2383a1402393dfd`.
- CR-0001 publication commit: `904ca6cb0beca7a868d5ca64729d94f5b4d7217d`.
- Validation: 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 targets, 0 broken links, 0 generated missing task IDs, 51 checksum entries valid.

## Frozen technical identity

- Target: `srv.UseSafeWeb.com` / `adguardvm`, Ubuntu 24.04 LTS, Azure `westeurope`.
- AdGuard Home: **v0.107.79**.
- Upstream baseline: `https://dns10.quad9.net/dns-query`; ECS off; AdGuard remains the filtering layer.
- Client resolver: `dns.usesafeweb.com`.
- DoH contract: `https://dns.usesafeweb.com/dns-query`.
- Android native pilot transport: DoT `dns.usesafeweb.com:853`.

## Persistent autonomous server execution

GitHub is the active execution bridge for eligible AUTO_ALLOWED host work. Repository-scoped runner `adguardvm` runs as `azureusr` through a persistent systemd service with non-interactive sudo. Ordinary host jobs are restricted to trusted `main`, read-only repository permissions, no persisted checkout credentials, and serialized `usesafeweb-adguard-server` concurrency.

Current direct fingerprint evidence proves two genuinely separate handed-off Azure VMs are now reachable through GitHub Actions:

- production runner `adguardvm`: Azure VM `adguardvm`, VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`, machine-id SHA-256 `e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`, Ubuntu 24.04, West Europe, AdGuard/Nginx active;
- recovery runner `adguartestdvm_correct`: Azure VM `adguartestdvm`, VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`, Ubuntu 24.04, West Europe, AdGuard/Nginx inactive.

This supersedes the earlier duplicate-runner condition in which `adguartestdvm` incorrectly executed on production. Corrected identity evidence: `TSK_0431_RECOVERY_RUNNER_CORRECTED_EVIDENCE_2026-08-28.md`, blob `1c8137ae89a5785d12fd1ec5b178488162b5bcd3`; dual-runner run `33161281851`, jobs `98816079276` and `98816079544`: PASS.

## Current technical task state

### PASS

- `TSK-0435` — Azure VM handoff — evidence blob `57de1a4187288870da7655973ac09bf907674d89`.
- `TSK-0437` — host security baseline, revalidated after TLS-proxy installation and current Ubuntu patch repair — base evidence blob `bb9221657a65c254975f61762af73b16a3e50241`; current revalidation evidence `TSK_0437_POST_TLS_PATCH_REVALIDATION_EVIDENCE_2026-08-28.md`, blob `b23bb28960efe28526626b36dfa2d52339a521e8`; reconciliation run `33159129601` / job `98809042724`: PASS.
- `TSK-0438` — domain/control owner condition.
- `TSK-0439` — pilot device DNS methods — evidence blob `f9af8b18cdc85bfe9b120661776172ab8581c2c9`.
- `TSK-0440` — encrypted-DNS hostname/path — evidence blob `9e0f15d0e1f11c892cf51317b705ac21c9563e53`.
- `TSK-0441` — public DNS for `dns.usesafeweb.com` independently verified from system, Cloudflare, Google and Quad9 resolvers with exact A `52.157.109.120` and no AAAA/CNAME — evidence: `TSK_0441_PUBLIC_DNS_EVIDENCE_2026-08-28.md`, blob `91369bbe33eb608361e8b7b771ceca0a5cd42d50`; verification run `33156757093`, jobs `98801252982` and `98801253193`: PASS.
- `TSK-0442` — TLS certificate acceptance fully satisfied after owner-observed real-phone encrypted-DNS success and fresh server-side revalidation — evidence: `TSK_0442_TLS_CERTIFICATE_EVIDENCE_2026-08-28.md`, blob `cb11394af1e80f15d85bda5d9b000bbf0efd6d20`; server revalidation run `33160416730` / job `98813254928`: PASS.
- `TSK-0443` — certificate renewal dry-run, Nginx deploy hook, daily expiry monitoring, owner alert route and recovery runbook fully verified — evidence: `TSK_0443_CERTIFICATE_RENEWAL_ALERT_EVIDENCE_2026-08-28.md`, blob `c2f3b3b35c9d8e2ec33f473d72c508ebde30348d`; production renewal run `33162046237` / job `98818564431`: PASS; external monitor run `33161991492` / job `98818390448`: PASS; final monitor blob `b565df52182e325d1d416a07be31f152078fd373`; runbook blob `881d797ea6f69879d0c8696d61e596733c38c3c5`.
- `TSK-0203` — supported AdGuard release installed — evidence blob `382b70ca971739712ff8ad5668d03841d5493d62`.
- `TSK-0201` — restricted authenticated administration/change path — evidence blob `ae06672e1cebdf87d006b85b80e5a7977f4e69b9`.
- `TSK-0204` — persistent query logging and file query logging explicitly disabled — corrected evidence: `TSK_0204_QUERYLOG_PRIVACY_EVIDENCE_2026-08-27.md`, blob `aa84d93d33d789fe4ff74ea12bcc2e5ffccd5b06`.
- `TSK-0205` — identifiable per-client statistics disabled — evidence: `TSK_0205_CLIENT_STATS_PRIVACY_EVIDENCE_2026-08-27.md`, blob `47fb0e0e6b64ceab965b2ca0ee259b40a98032c6`.
- `TSK-0206` — client-IP anonymisation enabled while query logging/statistics remain disabled — evidence: `TSK_0206_CLIENT_IP_ANONYMIZATION_EVIDENCE_2026-08-27.md`, blob `5905136433d930c2325a877e10a45e8540ac6a80`.
- `TSK-0483` — resolver abuse/amplification protections verified — evidence: `TSK_0483_RESOLVER_ABUSE_PROTECTION_EVIDENCE_2026-08-27.md`, blob `8a6426707fe9c9c8cd08f6b55e25d6b48bb8b28c`.
- `TSK-0407` — exact Quad9 dns10 DoH upstream with ECS disabled verified — evidence: `TSK_0407_QUAD9_DNS10_ECS_EVIDENCE_2026-08-27.md`, blob `7afeca58e9205234a230d2de702b99648b35347d`.
- `TSK-0406` — conservative versioned filtering baseline, narrow exception path and exact rollback verified — policy: `infrastructure/adguard-server/filter-policy-v1.yaml`, blob `333a4ef8cd34719d66056aa608ab19473f839634`; evidence: `TSK_0406_FILTERING_POLICY_EVIDENCE_2026-08-27.md`, blob `bb4514b4af7c1c5e616b7875f98e86962fee0325`.
- `TSK-0202` — secret-safe approved AdGuard settings exported/versioned and proven exactly equal to current live post-TLS-proxy safe settings — artifact: `infrastructure/adguard-server/approved-adguard-config-v1.json` v1.1.0, blob `e9975c4e75c2a68131f049da942468d8d1952d8d`; settings SHA-256 `fcedf8b67b5d4c43544d5a57b9f74b6a45e6f3be1d778c6fb6183e83802ac49d`; reconciliation evidence: `TSK_0202_ADGUARD_CONFIG_RECONCILIATION_EVIDENCE_2026-08-28.md`, blob `3d9ac577cfe75fb33d317d3e00905ebab91c3a45`; independent reconciliation run `33159129601` / job `98809042724`: PASS.
- `TSK-0429` — privacy-minimal AdGuard backup scope documented and independently verified against current DPIA/retention/live state — policy: `infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md`, blob `e62b48a3e746b1be90881bbffab3b7680384cc16`; evidence: `TSK_0429_PRIVACY_MINIMAL_BACKUP_SCOPE_EVIDENCE_2026-08-27.md`, blob `b77c6d7a2e17adc5e653151b55137467a8c5b62f`.
- `TSK-0430` — encrypted configuration backup created, independently audited and directly decrypted by the authorised owner — evidence: `TSK_0430_ENCRYPTED_CONFIG_BACKUP_EVIDENCE_2026-08-27.md`, blob `de1820cb2a9fc5b175c5e5eb1e18b45e6a430a82`; ciphertext SHA-256 `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`; owner recipient fingerprint `SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`; owner-side decrypted configuration SHA-256 `d8b6eae3b85edbaa1c49e318354389dc616099ecb3d2d90eff3c3dd8c663e1f2`.
- `TSK-0166` — pseudonymous Experiment-1 participant record/metric schema created and independently audited with direct predecessor proof — artifact: `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md`, blob `c7706fceced87c797b8cd92179198754e2b08ffe`; evidence: `TSK_0166_PARTICIPANT_RECORD_SCHEMA_EVIDENCE_2026-08-28.md`, blob `d043370a9c1efc99ccf8f65b813733b4c832c3f0`; independent audit run `33130737625` / job `98719395096`: PASS.
- `TSK-0168` — Experiment-1 qualification screener created and independently audited — artifact: `EXPERIMENT_01_QUALIFICATION_SCREENER.md`, blob `d35d3e0abfc3882d648df3c0c7458e216853b592`; evidence: `TSK_0168_QUALIFICATION_SCREENER_EVIDENCE_2026-08-28.md`, blob `760f881100e6221640c8afa86108665dc4ba1792`; independent audit run `33130918142` / job `98719985132`: PASS.
- `TSK-0214` — Experiment-1 retention/deletion execution checklist independently verified with direct predecessor proof — artifact: `RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`; evidence: `TSK_0214_RETENTION_DELETION_CHECKLIST_EVIDENCE_2026-08-28.md`, blob `0740743793e53c655f3ca447fddd51fd70b8d6e5`; independent audit run `33152847430` / job `98788653014`: PASS.
- `TSK-0225` — protection-claims checklist independently verified with direct predecessor proof — artifact: `PROTECTION_CLAIMS_CHECKLIST.md`, blob `4bfc83421318fe761d06f9a63e052e3bff36070a`; evidence: `TSK_0225_PROTECTION_CLAIMS_CHECKLIST_EVIDENCE_2026-08-28.md`, blob `94206b6f41e401df396d79f4366122ebfa37f6d8`; corrected independent audit run `33153183138` / job `98789746523`: PASS.
- `TSK-0227` — exceptional diagnostic-logging procedure independently verified with direct predecessor proof — artifact: `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md`, blob `f9e1bb52582a69bc385aa69c93d02febb7b5cffa`; evidence: `TSK_0227_EXCEPTIONAL_DIAGNOSTIC_LOGGING_EVIDENCE_2026-08-28.md`, blob `3455c9077585a4727084ff61a791c31a90b9ad75`; independent audit run `33153403025` / job `98790453195`: PASS.
- `TSK-0228` — child-safety concern/disclosure escalation boundary independently verified with current official-source revalidation — artifact: `CHILD_SAFETY_ESCALATION_PROCEDURE.md`, blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`; evidence: `TSK_0228_CHILD_SAFETY_ESCALATION_EVIDENCE_2026-08-28.md`, blob `6c72844979f417e09c313fc7569f0db588c2c15a`; independent repository audit run `33153607319` / job `98791113929`: PASS.
- `TSK-0165` — Experiment-1 facilitator guide and intervention taxonomy independently verified against current runtime predecessors, frozen protocol and accepted participant schema — artifact: `EXPERIMENT_01_FACILITATOR_GUIDE.md`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`; evidence: `TSK_0165_FACILITATOR_GUIDE_EVIDENCE_2026-08-28.md`, blob `77992d668649d1f647126f4e1b08aeb1d04bb993`; independent audit run `33153850640` / job `98791885998`: PASS.
- `TSK-0169` — Experiment-1 support and false-positive intake process independently verified against current runtime predecessors and privacy/diagnostic controls — artifact: `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`, blob `9fab42f97e3e96023de89a8ed266acc21c0f06ab`; evidence: `TSK_0169_SUPPORT_FALSE_POSITIVE_INTAKE_EVIDENCE_2026-08-28.md`, blob `30a4d4380f0aa475a90c1719408663d7a43df384`; independent audit run `33155547694` / job `98797333013`: PASS.

### TSK-0204 corrected stable state

Downstream read-only TSK-0202 inspection exposed a previously unverified latent configuration: global `querylog.enabled=false`, but persisted `querylog.file_enabled=true`. Official AdGuard documentation defines these as separate controls. Current AdGuard implementation returns before adding records when global logging is disabled, so no active query-history leakage was evidenced; nevertheless the file-write capability contradicted the frozen project requirement and stale TSK-0204 PASS was correctly reopened.

The canonical control script was hardened to manage the separate persisted scalar while AdGuard is stopped, with a root-only target-local rollback copy, post-restart API readiness polling, exact invariant checks, and a corrected privileged rollback guard. Final script blob: `3018fedb5292c5c302a74ff8b42cada18aec26b5`.

First corrective run `33126239702` / job `98704969927` reached persisted `enabled=false` + `file_enabled=false` but failed on a transient HTTP 404 during immediate post-restart API verification and was not accepted. A separate read-only audit run `33126279381` / job `98705094275` then proved the desired state was stable: both persisted settings false, control API/query-log endpoints HTTP 200, synthetic query not retained, zero query-log items, zero non-empty `querylog.json*` files, and dns10/ECS/anonymisation/statistics/filter invariants preserved.

After hardening rollback and API-readiness handling, final pinned control run `33126344825` / job `98705307945`: **PASS**. It detected `file_enabled=false` already in place, made no second direct YAML edit, cleared historical query-log state, re-proved both persisted controls false, API `enabled=false`, anonymisation enabled, fresh synthetic query retained `false`, query-log item count `0`, no non-empty query-log file, and unchanged upstream/privacy/filter invariants.

ACC-0204 is fully satisfied at the stronger evidence level.

### TSK-0202 accepted stable state

Post-TLS safe export run `33158010249` / job `98805347681`: **PASS**. It asserted the current resolver/privacy/filter/admin/abuse invariants and emitted only a non-sensitive allowlist. Versioned artifact `infrastructure/adguard-server/approved-adguard-config-v1.json` v1.1.0 is blob `e9975c4e75c2a68131f049da942468d8d1952d8d`, with settings SHA-256 `fcedf8b67b5d4c43544d5a57b9f74b6a45e6f3be1d778c6fb6183e83802ac49d`.

Independent reconciliation run `33159129601` / job `98809042724`: **PASS**. It proved exact live-to-artifact equality, secret-field exclusion, zero persistent clients, query logging/file logging/statistics disabled, client-IP anonymisation enabled, dns10/ECS/filter invariants preserved, AdGuard admin `127.0.0.1:3000`, loopback-only local DoH backend enabled for the path-restricted TLS proxy, AdGuard native TLS listener disabled, and no non-empty query-log file.

Evidence: `TSK_0202_ADGUARD_CONFIG_RECONCILIATION_EVIDENCE_2026-08-28.md`, blob `3d9ac577cfe75fb33d317d3e00905ebab91c3a45`. ACC-0202 remains fully satisfied. Its `REQ-0022` reference remains unresolved under the owner-deferred UK representative/ICO work and does not authorize real England participant activation.

### TSK-0429 accepted stable state

The exact WBS row defines TSK-0429 as `A3`, `AUTO_ALLOWED`, HIGH, critical path, hard predecessors `TSK-0437` + `TSK-0011`, acceptance `ACC-0429`.

Read-only live scope preflight run `33127459481` / job `98708878287`: **PASS**. It established current root-only config/secret/rollback permissions, logging/statistics/anonymisation state, zero persistent clients/user rules/query-log files, and absence of configured TLS private material.

Policy v1.0.0 at `infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md` defines:

- included data: raw current `AdGuardHome.yaml` + non-secret verification manifest only;
- exclusions: plaintext `admin.env`, stale rollback copies, DNS/query history, client statistics/records, participant/research data, diagnostics, caches/logs/reinstallable binaries, and current-absent TLS private material;
- encryption: confidentiality + integrity/authentication before durable/off-host retention, owner-authorised decryption, secret material separate from archive/Git/logs;
- retention: event-based latest verified + at most one previous verified generation, with immediate plaintext/failed-copy deletion rather than an invented calendar period;
- access: root during execution plus owner/explicit owner-authorised recovery path only;
- location: root-only staging on current West Europe/Netherlands DNS VM; future off-host location remains inside approved Azure/EU boundary and requires actual owner-managed target verification;
- deletion: project-controlled files deleted and absence verified; provider-side deletion verified only when a real provider target exists.

First audit run `33127565783` / job `98709225350` was not accepted because a literal static wording assertion mismatched the policy text; no target mutation occurred. Corrected independent audit run `33127643804` / job `98709483562`: **PASS**, proving policy/source alignment, source blobs, current live assumptions, no policy secret material, no TLS private material, and no query-log files.

ACC-0429 is fully satisfied.

### TSK-0430 accepted stable state

The exact WBS row defines TSK-0430 as `A3`, `AUTO_ALLOWED`, HIGH, critical path, with hard predecessors `TSK-0202`, `TSK-0429`, `TSK-0011`, acceptance `ACC-0430`.

Server-side backup creation run `33128004795` / job `98710652627`: **PASS**. Independent retained-backup audit run `33128142374` / job `98711096972`: **PASS**. The retained root-only encrypted archive was created at `2026-08-27T23:56:12Z`, size `21121` bytes, ciphertext SHA-256 `bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde`, with no plaintext staging or prohibited query history retained.

On 2026-08-28 the Project Owner executed the repository-pinned owner-side verifier from an owner-controlled workstation. The verifier re-streamed and locally reverified the exact retained ciphertext/sidecar, successfully decrypted it with the owner-held private key, verified package/member and manifest scope, verified the raw configuration checksum without printing configuration contents, and returned `TSK_0430_OWNER_DECRYPTION=PASS`. The owner recipient fingerprint matched `SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U`; decrypted configuration SHA-256 was `d8b6eae3b85edbaa1c49e318354389dc616099ecb3d2d90eff3c3dd8c663e1f2`.

No private-key material or passphrase was supplied to GitHub, ChatGPT or project evidence. ACC-0430 is fully satisfied.

### TSK-0166 accepted stable state

The exact WBS row defines TSK-0166 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessors `TSK-0223; TSK-0164`, acceptance `ACC-0166`.

Because the predecessors were historical planning PASS records, their labels were not accepted as sufficient evidence by themselves. Current durable `EXPERIMENT_01_CONCIERGE_VALIDATION.md`, blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`, directly reconstructs ACC-0164: qualification, real actions, intervention rules, metrics, thresholds, stop conditions, Wave A/controlled refinement/Wave B and aggregate decision output. Current durable `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly reconstructs ACC-0223's minimum-data/prohibited-field baseline.

The versioned empty template `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md` contains 37 controlled schema fields, including every ACC-0166 measurement class, no uncontrolled participant free text, explicit prohibited-field controls, no participant records, and no authorisation for recruitment or live processing.

Independent read-only audit run `33130737625` / job `98719395096`: **PASS**. It returned `TSK_0164_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0223_DIRECT_PREDECESSOR_PROOF=PASS`, 19/19 required acceptance field classes present, 37 total controlled fields, zero prohibited field tokens, exact schema blob match and `TSK_0166_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0166_PARTICIPANT_RECORD_SCHEMA_EVIDENCE_2026-08-28.md`, blob `d043370a9c1efc99ccf8f65b813733b4c832c3f0`. ACC-0166 is fully satisfied. This does not activate Experiment 1 or override the validation-readiness gate.

### TSK-0168 accepted stable state

The exact WBS row defines TSK-0168 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0164`, acceptance `ACC-0168`.

Current durable `EXPERIMENT_01_CONCIERGE_VALIDATION.md`, blob `bc801da11d7a7f2a5315d1cdca4f0d134afe7805`, directly re-proves the historical predecessor's frozen qualification semantics. The v1.0.0 screener `EXPERIMENT_01_QUALIFICATION_SCREENER.md` covers caregiver setup responsibility, broad first-phone age/stage, bounded phone timing, iPhone/Android, willingness for real appropriate changes and non-surveillance fit, while explicitly prohibiting child name/exact DOB and unnecessary location/activity data.

Independent read-only audit run `33130918142` / job `98719985132`: **PASS**. It re-proved TSK-0164, checked all eight ACC-0168 items, verified that the screener's controlled outputs align to the accepted TSK-0166 schema, matched the exact screener blob and returned `TSK_0168_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0168_QUALIFICATION_SCREENER_EVIDENCE_2026-08-28.md`, blob `760f881100e6221640c8afa86108665dc4ba1792`. ACC-0168 is fully satisfied. This preparation artifact does not authorise recruitment or participant processing.

### TSK-0214 accepted stable state

The exact WBS row defines TSK-0214 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessors `TSK-0224; TSK-0166`, acceptance `ACC-0214`.

Historical/planning predecessor labels were not accepted as sufficient evidence by themselves. Current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly re-proves TSK-0224's retention schedule, while current accepted `EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md`, blob `c7706fceced87c797b8cd92179198754e2b08ffe`, directly proves the no-participant-records-in-GitHub boundary.

The existing `RETENTION_DELETION_EXECUTION_CHECKLIST.md`, blob `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`, identifies controlled data locations, owner, exact due-date rules, deletion/verification methods, aggregate-output restrictions, structured deletion evidence, and fail-closed exception handling.

Independent read-only audit run `33152847430` / job `98788653014`: **PASS**. It returned `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0166_CURRENT_ARTIFACT_BOUNDARY_PROOF=PASS`, `TSK_0214_ACCEPTANCE_CLASSES=6/6`, exact checklist blob match and `TSK_0214_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0214_RETENTION_DELETION_CHECKLIST_EVIDENCE_2026-08-28.md`, blob `0740743793e53c655f3ca447fddd51fd70b8d6e5`. ACC-0214 is fully satisfied. This verifies preparation only; no participant processing/deletion occurred and no validation-readiness gate was bypassed.

### TSK-0225 accepted stable state

The exact WBS row defines TSK-0225 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0219`, acceptance `ACC-0225`.

Historical/planning predecessor labels were not accepted as sufficient evidence by themselves. Current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly re-proves TSK-0224, and current `PILOT_PRIVACY_NOTICE.md`, blob `331f263388dfacfa73b6e9e556277d4230864ce8`, directly re-proves TSK-0219's parent/child notice, no-complete-safety/no-generic-unverified-no-logs language, and explicit release conditions.

The existing `PROTECTION_CLAIMS_CHECKLIST.md`, blob `4bfc83421318fe761d06f9a63e052e3bff36070a`, explicitly separates all four truth states, limits DNS and native/app claims, handles VPN/alternate-DNS/Private Relay ambiguity, requires removal/recovery, constrains exceptions, and requires current evidence without child browsing/domain history.

Initial audit run `33153150939` / job `98789641926` was not accepted because a literal assertion did not normalize Markdown emphasis in the child notice; it failed before any product/state mutation. The verifier was corrected without changing requirements or artifacts.

Corrected independent read-only audit run `33153183138` / job `98789746523`: **PASS**. It returned `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0219_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0225_ACCEPTANCE_CLASSES=7/7`, exact claims-checklist blob match and `TSK_0225_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0225_PROTECTION_CLAIMS_CHECKLIST_EVIDENCE_2026-08-28.md`, blob `94206b6f41e401df396d79f4366122ebfa37f6d8`. ACC-0225 is fully satisfied. This is preparation only and does not prove protection on a real participant device or authorize recruitment/processing.

### TSK-0227 accepted stable state

The exact WBS row defines TSK-0227 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0224`, acceptance `ACC-0227`.

The predecessor planning label was not accepted as sufficient evidence by itself. Current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly re-proves TSK-0224's retention and deletion boundaries.

The existing `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md`, blob `f9e1bb52582a69bc385aa69c93d02febb7b5cffa`, requires incident/ticket identity, explicit necessity, exact field/scope allowlisting, approval, restricted access, preselected UTC start/end, notice decision, minimisation hierarchy, baseline restoration, deletion and recorded deletion verification; indefinite logging, GitHub raw diagnostic data and silent extension are prohibited.

Independent read-only audit run `33153403025` / job `98790453195`: **PASS**. It returned `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0227_ACCEPTANCE_CLASSES=9/9`, exact diagnostic-runbook blob match and `TSK_0227_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0227_EXCEPTIONAL_DIAGNOSTIC_LOGGING_EVIDENCE_2026-08-28.md`, blob `3455c9077585a4727084ff61a791c31a90b9ad75`. ACC-0227 is fully satisfied. No exceptional logging was enabled and no participant data was collected.

### TSK-0228 accepted stable state

The exact WBS row defines TSK-0228 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessor `TSK-0219`, acceptance `ACC-0228`.

The predecessor planning label was not accepted as sufficient evidence by itself. Current `VALIDATION_READINESS_GATE.md`, blob `b3b0efd0cc0f40faa1ecab190c7469b8dff12ec1`, directly re-proves TSK-0224 and current `PILOT_PRIVACY_NOTICE.md`, blob `331f263388dfacfa73b6e9e556277d4230864ce8`, directly re-proves TSK-0219.

The existing `CHILD_SAFETY_ESCALATION_PROCEDURE.md`, blob `18c6ac79c3fa5db21c5e591e81fe5b6611cd7bf1`, separates ordinary product support from urgent safeguarding, routes England/UK concerns through 999/local children's social care/101/NSPCC/Childline/CEOP as appropriate, minimises personal/raw disclosure collection and assigns internal escalation to the Project Owner.

Independent repository audit run `33153607319` / job `98791113929`: **PASS**. It returned `TSK_0224_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0219_DIRECT_PREDECESSOR_PROOF=PASS`, `TSK_0228_ACCEPTANCE_CLASSES=4/4`, exact procedure blob match and `TSK_0228_INDEPENDENT_REPOSITORY_AUDIT=PASS`.

A separate current authoritative-source check on 2026-08-28 reverified GOV.UK child-abuse/local-council routes, current NSPCC and Childline numbers, and the CEOP concerned-adult online sexual-abuse/grooming route; no material contradiction requiring an artifact change was found. Evidence: `TSK_0228_CHILD_SAFETY_ESCALATION_EVIDENCE_2026-08-28.md`, blob `6c72844979f417e09c313fc7569f0db588c2c15a`. ACC-0228 is fully satisfied. No real safeguarding disclosure or participant data was processed.

### TSK-0165 accepted stable state

The exact WBS row defines TSK-0165 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessors `TSK-0166; TSK-0228`, acceptance `ACC-0165`.

Both hard predecessors were confirmed as current runtime PASS. The existing `EXPERIMENT_01_FACILITATOR_GUIDE.md`, blob `7d80c1338acc1a5a4c1ff30c020ca39021d8dcb3`, preserves the frozen Experiment-1 hypothesis and journey, requires every intervention to be timed/classified with duration/reason/outcome, distinguishes usability/technical/compatibility help from safety/privacy correction and safeguarding escalation, and explicitly prevents silent facilitator completion or facilitator takeover from being counted as self-service success.

Independent read-only audit run `33153850640` / job `98791885998`: **PASS**. It returned `TSK_0166_RUNTIME_PREDECESSOR=PASS`, `TSK_0228_RUNTIME_PREDECESSOR=PASS`, `TSK_0165_PROTOCOL_ALIGNMENT=PASS`, `TSK_0165_SCHEMA_ALIGNMENT=PASS`, `TSK_0165_ACCEPTANCE_CLASSES=4/4`, exact facilitator-guide blob match and `TSK_0165_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0165_FACILITATOR_GUIDE_EVIDENCE_2026-08-28.md`, blob `77992d668649d1f647126f4e1b08aeb1d04bb993`. ACC-0165 is fully satisfied. This is protocol preparation only and does not authorise recruitment, participant processing, live facilitation, or child-linked DNS activation.

### TSK-0169 accepted stable state

The exact WBS row defines TSK-0169 as L2 / A3 / `AUTO_ALLOWED` / MEDIUM with hard predecessors `TSK-0227; TSK-0165`, acceptance `ACC-0169`.

Both hard predecessors were confirmed as current runtime PASS. The existing `EXPERIMENT_01_SUPPORT_FALSE_POSITIVE_INTAKE.md`, blob `9fab42f97e3e96023de89a8ed266acc21c0f06ab`, requires a pseudonymous participant ID, category, severity, intervention time, privacy-safe evidence, action, outcome and closure for every issue; false-positive handling is narrow/reversible/re-tested, and genuinely necessary request-level diagnostics are routed through TSK-0227 rather than broad query-history collection.

Independent read-only audit run `33155547694` / job `98797333013`: **PASS**. It returned `TSK_0227_RUNTIME_PREDECESSOR=PASS`, `TSK_0165_RUNTIME_PREDECESSOR=PASS`, `TSK_0169_ACCEPTANCE_CLASSES=8/8`, `TSK_0169_PRIVACY_BOUNDARY=PASS`, `TSK_0169_DIAGNOSTIC_REFERENCE=PASS`, exact intake artifact blob match and `TSK_0169_INDEPENDENT_AUDIT=PASS`.

Evidence: `TSK_0169_SUPPORT_FALSE_POSITIVE_INTAKE_EVIDENCE_2026-08-28.md`, blob `30a4d4380f0aa475a90c1719408663d7a43df384`. ACC-0169 is fully satisfied. This is support-process preparation only; no participant support case, diagnostic logging or participant processing occurred.

### TSK-0441 accepted stable state

The exact WBS/runtime preflight defines TSK-0441 as L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0440; TSK-0435; TSK-0011`, all satisfied, acceptance `ACC-0441`.

After the owner completed the Cloudflare-side record, independent read-only verification run `33156757093` executed on two repository-scoped self-hosted runners. Jobs `98801252982` (`adguardvm`) and `98801253193` (`adguartestdvm`) both returned the exact same public state: the system resolver, Cloudflare `1.1.1.1`, Google `8.8.8.8` and Quad9 `9.9.9.9` resolve `dns.usesafeweb.com` to `52.157.109.120`, with no AAAA or CNAME observed.

Evidence: `TSK_0441_PUBLIC_DNS_EVIDENCE_2026-08-28.md`, blob `91369bbe33eb608361e8b7b771ceca0a5cd42d50`. ACC-0441 is fully satisfied. This proves public DNS only and does not prove TLS/DoH/DoT readiness or authorize participant activation.

### TSK-0437 current revalidation

A post-TLS reconciliation found five newly installable Ubuntu Python 3.12 packages, so the historical current-patch proof was not preserved blindly. Patch repair run `33158277980` / job `98806231226` upgraded all five and proved no pending upgrades and no reboot requirement.

Post-TLS production audit run `33158990648` / job `98808581681` and independent reconciliation run `33159129601` / job `98809042724` then proved Ubuntu 24.04, current patches, effective SSH hardening, AdGuard/Nginx active, UFW deny-incoming/allow-outgoing with exact allowed TCP ports 22/80/443/853, externally bound service ports exactly 22/443/853, admin `127.0.0.1:3000`, plain DNS `127.0.0.1:53` only, path-restricted Nginx, no Nginx access logging, no non-empty AdGuard query-log files and preserved privacy/filter controls.

Evidence: `TSK_0437_POST_TLS_PATCH_REVALIDATION_EVIDENCE_2026-08-28.md`, blob `b23bb28960efe28526626b36dfa2d52339a521e8`. ACC-0437 is current PASS.

### TSK-0442 accepted stable state

The exact WBS row defines TSK-0442 as L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0441; TSK-0011`, both satisfied, acceptance `ACC-0442`.

After certificate issuance and the path-restricted same-host TLS proxy were implemented, the Project Owner completed the requested supported real-phone encrypted-DNS validation and reported that the real phone test was working. Fresh production revalidation run `33160416730` / job `98813254928` then independently proved exact production identity, certificate hostname validity, more than 30 days remaining validity, root-owned mode-0600 private key, local certificate-chain/hostname verification on 443/853, TLS 1.0/1.1 rejection, TLS 1.2 acceptance, admin and plain-DNS loopback-only boundaries, encrypted listeners 443/853, public non-DoH/admin 404 behavior and UFW encrypted-DNS-only exposure.

Evidence: `TSK_0442_TLS_CERTIFICATE_EVIDENCE_2026-08-28.md`, blob `cb11394af1e80f15d85bda5d9b000bbf0efd6d20`. ACC-0442 is fully satisfied. This does not by itself authorize participant recruitment/activation or bypass later readiness/legal gates.

### TSK-0443 accepted stable state

The exact WBS row defines TSK-0443 as L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0442; TSK-0011`, both satisfied, acceptance `ACC-0443`.

Production preflight found Certbot 2.9.0 with `certbot.timer` already enabled/active twice daily but no deploy hook and no host-local owner notification channel. Governed production run `33162046237` / job `98818564431`, guarded by the exact production Azure VM ID, installed root-owned deploy hook `/etc/letsencrypt/renewal-hooks/deploy/10-usesafeweb-reload-nginx.sh` at mode 0755, SHA-256 `980197605ee3230c4c4463817ff53a734a5f9c9aa9b6c2b1672cd168a35de8e5`. The hook validates Nginx configuration before reload and was directly invoked successfully.

The same job ran `certbot renew --dry-run --no-random-sleep-on-renew`; Certbot reported all simulated renewals succeeded for `dns.usesafeweb.com`. Post-dry-run verification re-proved hostname/key validity, local TLS on 443/853, admin loopback-only 3000, plain DNS loopback-only 53, and active/enabled Certbot timer.

Daily expiry monitor `.github/workflows/certificate-expiry-monitor.yml`, blob `b565df52182e325d1d416a07be31f152078fd373`, now runs schedule-only at 06:17 UTC with `contents: read` and `issues: write`. Successful independent external monitor run `33161991492` / job `98818390448` on `adguartestdvm_correct` validated both TCP 443 and 853 using TLS 1.3 with 89 days remaining and no errors. Installation route proof created GitHub issue #1, assigned it to `Yaserbayad`, then closed it after successful delivery proof. Direct issue read-back confirmed owner assignment and closed/completed state.

Recovery documentation is `infrastructure/adguard-server/TLS_CERTIFICATE_RENEWAL_RUNBOOK.md`, blob `881d797ea6f69879d0c8696d61e596733c38c3c5`. It covers normal renewal, dry-run verification, 30-day alert handling, diagnosis, safe real renewal, Nginx reload, DoH/DoT validation, emergency replacement, no-plaintext-DNS fallback, and privacy-safe evidence rules.

Evidence: `TSK_0443_CERTIFICATE_RENEWAL_ALERT_EVIDENCE_2026-08-28.md`, blob `c2f3b3b35c9d8e2ec33f473d72c508ebde30348d`. ACC-0443 is fully satisfied.

### WAITING — TSK-0431

`TSK-0431` — test pilot restore or rebuild procedure: **WAITING on the owner-managed Azure-native backup/restore path required by REQ-0052; not PASS**.

The exact WBS row is L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0430; TSK-0011`, both satisfied. ACC-0431 requires a functional test target that passes encrypted-DNS and privacy checks with recovery time/issues recorded. REQ-0052 requires a timed clean-server drill covering host baseline, packages, AdGuard, server-managed configuration recovery, firewall/network, endpoint, TLS, filters, privacy, startup, Azure-native backup/restore, verification and health.

The prior machine-identity blocker is resolved. Direct dual-runner fingerprint run `33161281851` proves the corrected runner `adguartestdvm_correct` executes on independent Azure VM `adguartestdvm`, West Europe, Ubuntu 24.04, Azure VM ID `6e92a026-964c-4118-8312-f1d31c6ff4d2`, machine-id SHA-256 `e09868443c476b30eae778d191ceedee57ed6f27a74856eae1d0709c68f1c852`, with AdGuard/Nginx inactive. Production remains VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`. Evidence: `TSK_0431_RECOVERY_RUNNER_CORRECTED_EVIDENCE_2026-08-28.md`, blob `1c8137ae89a5785d12fd1ec5b178488162b5bcd3`.

Authoritative contract inspection run `33161362741` / job `98816346637` confirms CON-0004/CON-0019 keep Azure control-plane creation/configuration owner-managed. No Azure control-plane connector is available and no current durable evidence identifies the Azure-native backup/restore interface or restoration step required by REQ-0052.

No recovery mutation has been started on the corrected VM. Deterministic resumption condition: the owner identifies/provides the Azure-native backup/restore path or evidence. The timed clean-server recovery drill may then execute on `adguartestdvm_correct` and must not use production as the destructive target.

### External/provider and legal boundaries

- TSK-0441 Cloudflare DNS is satisfied and independently verified. Any further Cloudflare account/zone mutation remains owner/provider-controlled unless an explicitly authorized interface becomes available.
- Azure control-plane provisioning/configuration remains owner-managed. The corrected recovery VM handoff is independently verified, but TSK-0431 still requires an owner-managed Azure-native backup/restore path/evidence before the full recovery drill can satisfy REQ-0052.
- TSK-0442 TLS target-device acceptance and TSK-0443 certificate renewal/expiry alerting are satisfied; broader participant/public readiness remains governed by downstream technical, validation, privacy/legal and activation gates.
- Owner-deferred UK representative/ICO fee planning remains unresolved until 2027-08-27 or earlier explicit reactivation; technical work does not imply validation-readiness legal gate PASS or authorize real England participant activation.

## Runtime safeguards

- Runtime states only `TODO`, `WAITING`, `BLOCKED`, `PASS`.
- PASS requires all applicable current acceptance criteria with durable/reconstructable proof.
- Current contradictory direct evidence reopens stale PASS rather than being ignored.
- No secrets, credentials, password hashes, private keys, unnecessary personal data, or raw DNS query history may be exported to GitHub.
- Plain DNS 53 remains non-public. TSK-0442 TLS and TSK-0443 certificate renewal/expiry controls are PASS, but broader participant/public readiness remains gated by applicable downstream readiness, validation, privacy/legal and activation evidence.
- Azure control-plane remains owner-managed; runner autonomy applies to handed-off VM/repository-authorized tasks only after target identity and scope are verified.

## Queue status after TSK-0443

The last L2 queue recomputation selected TSK-0443 as the sole ready item before its execution. TSK-0443 is now PASS, so that selection result is superseded. The L2 queue has not yet been recomputed against this new runtime state.

## Exact next authoritative step

Recompute the current L2 queue with TSK-0443 PASS and TSK-0431 held WAITING only on the owner-managed Azure-native backup/restore path required by REQ-0052. Continue the highest-priority eligible `AUTO_ALLOWED` L2 work after direct dependency/gate verification. Do not start the TSK-0431 recovery drill until its Azure-native recovery input is identified, and do not bypass participant-activation, legal, Azure control-plane, provider, or public-service readiness boundaries.
