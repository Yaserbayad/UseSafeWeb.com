# TSK-0229 — Current Revalidation Evidence under DEC-0052 / CR-0005

**Task:** `TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules`  
**Acceptance:** `ACC-0229`  
**Verification:** `VER-0229`  
**Evidence:** `EVD-0229`  
**Lifecycle:** L4  
**Action authority:** A3 / AUTO_ALLOWED  
**Review date:** 2026-08-29  
**Disposition:** PASS — existing data contract remains current; old pre-product human-validation sequencing is superseded

## 1. Decision

The existing contract `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`, Git blob `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`, remains technically and privacy-design valid under current authority. It is **not duplicated or redesigned**.

The earlier artifact/evidence references to `DEC-0050 / CR-0003` and missing pre-product representative-parent evidence are historical sequencing context only. They are superseded for current execution by owner-approved `DEC-0052 / CR-0005`: parent/user/participant validation is excluded from the pre-product L4–L7 critical path and is first applicable at the controlled integrated-product L8 pilot. No pre-product human-validation evidence is required or claimed for TSK-0229.

`RSK-0002` may remain an open assumption risk where current authority keeps it open, but it is **not a blocker to this L4 PASS** and does not reintroduce pre-product parent/user validation.

## 2. Current canonical contract

Current WBS at revalidation defines TSK-0229 as:

- lifecycle `L4`;
- priority `HIGH`;
- dependency `TSK-0146`;
- capability `A3` / `AUTO_ALLOWED`;
- `ACC-0229`: only fields necessary for the active journey exist; no browsing history or persistent child profile; expiry/deletion and diagnostic boundaries are testable;
- `VER-0229`: review complete evidence, contrary evidence, risks and authority; record stable decision and work unlocked;
- `EVD-0229`: artifact/version, exact source/environment, verification output, date, verifier, deviations and disposition.

The current register references remain compatible:

- `REQ-0018`: no real England participant activation before the applicable legal/privacy/technical readiness gate. CR-0005 moves such activation/testing to the later integrated-product stage; the requirement is not a pre-product blocker.
- `REQ-0019`: processing purpose, data, lawful basis, necessity, recipients, retention, rights and safeguards must reflect actual reality.
- `CON-0007`: persistent identifiable query/file logging remains off; exceptional diagnostics are time-boxed/deleted.
- `CON-0008`: identifiable per-client statistics remain off/excluded unless specifically justified; no browsing/top-domain product metric.
- `INT-0006`: legal/privacy/safeguarding controls must be reflected without unsupported legal conclusions.
- `INT-0007`: implemented data-flow reality must later match the approved inventory/retention/deletion design.
- `RSK-0001`: legal/data readiness can block later real-participant work; it does not require pre-product participant validation.

## 3. ACC-0229 current revalidation

The existing `accountless-journey-data-v1` contract still directly satisfies ACC-0229:

1. **Minimum active-journey state:** J0 browser/session-only state is preferred. Optional J1 server-side state is allowed only where later architecture demonstrates necessity for safe completion, verification, setup-artifact generation or an explicitly supported short accountless resume path.
2. **No persistent identity/profile:** no mandatory account, email, phone, parent/child name, stable customer/device identifier, persistent child/family profile or identity graph is introduced.
3. **No browsing/DNS history:** browsing, URL, DNS-query, visited-domain and activity history are prohibited journey fields; persistent top-domain/client statistics remain outside the model.
4. **Explicit expiry/deletion:** J1 has a fixed non-sliding maximum 24-hour TTL; early deletion is synchronous where possible or bounded to 15 minutes; tokens are not reused; deletion/expiry must read back as no active record.
5. **No linkage:** J0/J1 may not be stitched across sessions or linked to persistent parent/child/device identity, DNS history, IP-derived identity, analytics IDs or household profiles.
6. **Diagnostic separation:** request-level/raw diagnostics are outside J1 and must follow the separately governed exceptional-diagnostic procedure.
7. **Logging/backup boundary:** live token/payload logging and user-level clickstream/session replay are prohibited; J1 is excluded from durable backups by default absent a later explicitly approved exception.
8. **Testability:** fourteen implementation invariants cover schema allowlisting, identity/history exclusion, opaque tokens, TTL, early deletion, no sliding expiry, no linkage/logging, diagnostic separation, backup exclusion, deletion read-back, restart safety and accountless completion.

The 24-hour maximum TTL and 15-minute cleanup bound remain **internal conservative product defaults**, not legal thresholds and not behavioral findings. Shortening is allowed where compatible; broadening/lengthening remains a material data-contract change requiring current necessity/privacy/architecture review and applicable authority.

## 4. Current authoritative external-source review

Current source review on 2026-08-29 found no contradiction requiring a data-contract change:

- **GDPR Article 5(1)(c), data minimisation:** personal data must be adequate, relevant and limited to what is necessary for the processing purpose. Source: `https://eur-lex.europa.eu/legal-content/FR-EN/TXT/?uri=CELEX%3A32016R0679` (accessed 2026-08-29).
- **GDPR Article 5(1)(e), storage limitation:** identifiable personal data should be kept no longer than necessary for the processing purpose. Same EUR-Lex source, accessed 2026-08-29.
- **GDPR Article 25, data protection by design/default:** appropriate technical/organisational measures must implement data-protection principles such as minimisation, and by default only necessary personal data should be processed. Source: `https://eur-lex.europa.eu/legal-content/FR-EN/ALL/?uri=CELEX%3A32016R0679` (accessed 2026-08-29).
- **EDPB Guidelines 4/2019, final version:** data-minimisation guidance says controllers should determine whether the purpose can be achieved with less personal data or without personal data and should delete/anonymise data when identification is no longer needed. Source: `https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en` (accessed 2026-08-29).
- **EDPB 2026 DPbDD summary:** data protection by design/default remains a mandatory continuous duty and explicitly prompts designers to ask whether systems can use less data. Source: `https://www.edpb.europa.eu/system/files/2026-02/edpb-summary-gdpr-data-protection-design-default_en.pdf` (accessed 2026-08-29).

These sources support the contract's minimisation/default-deletion direction. This revalidation does **not** claim that the internal 24-hour/15-minute product defaults are legally mandated, and it does not issue a final legal-compliance conclusion.

## 5. Repository/current-authority audit

Read-only audit workflow `.github/workflows/tsk0229-current-audit.yml`:

- commit: `f0eb9ede4839ab9e2963469eea5179c79211df03`;
- run: `33269218872`;
- job: `99144565511`;
- runner: self-hosted `adguardvm`, Linux x64;
- result: PASS;
- repository clean: PASS.

Observed current authority/evidence:

- WBS task is L4 / HIGH / `A3` / `AUTO_ALLOWED`, dependency `TSK-0146`, ACC/VER/EVD IDs `ACC-0229 / VER-0229 / EVD-0229`.
- Runtime contains an existing `### TSK-0229 accepted stable state` and already records TSK-0229 PASS.
- Existing contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`.
- Existing independent evidence blob: `a087c63a0556db549ead4f40805e435725709251`.
- Current runtime contains `CR-0005`, `DEC-0052`, and the verified pre-product human-validation exclusion semantics.
- Existing contract/evidence satisfy the substantive ACC-0229 data/expiry/deletion/no-linkage/diagnostic requirements but contain old CR-0003/DEC-0050 sequencing references.
- Legacy `.github/workflows/reconcile-tsk0229-pass.yml`, blob `1902590e748e24b707f31e15fbfda92e654172fe`, also contains the superseded CR-0003/DEC-0050/TSK-0187 blocker logic and must not be used as current execution authority.

## 6. Contrary evidence / deviations

No current technical, product, privacy-design or regulatory source reviewed here contradicts the substantive accountless data model.

The sole material deviation is **stale sequencing language** in the 2026-08-28 artifact/evidence/runtime paragraph and legacy reconciliation workflow. Current DEC-0052/CR-0005 supersedes those old human-validation dependencies. The valid data-contract evidence is preserved; the stale sequencing is corrected in current runtime and the obsolete reconciliation workflow is retired rather than rewriting historical evidence as if it never existed.

## 7. Disposition

`ACC-0229`, `VER-0229` and `EVD-0229` remain satisfied under current authority. The existing data contract remains the accepted TSK-0229 artifact.

**TSK-0229: PASS — current under DEC-0052 / CR-0005.**

This PASS does not itself authorize later production implementation, public publication, payment, or launch; those remain governed by their actual lifecycle gates. It does not require or claim pre-product parent/user/participant validation.
