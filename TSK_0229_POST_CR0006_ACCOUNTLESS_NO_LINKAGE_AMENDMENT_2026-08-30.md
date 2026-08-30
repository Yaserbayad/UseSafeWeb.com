# TSK-0229 — Post-CR-0006 Accountless Data / Optional-Account Separation Amendment

**Version:** 1.0.0  
**Date:** 2026-08-30  
**Task:** TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules  
**Acceptance:** ACC-0229  
**Authority:** DEC-0053 / CR-0006; DEC-0052 / CR-0005 sequencing retained  
**Base contract:** `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`, `accountless-journey-data-v1`  
**Status represented:** bounded amendment candidate for post-CR-0006 TSK-0229 verification; not L5 persistent-account schema approval, legal-compliance certification, implementation authority, LG-06 PASS, participant authority or launch authority

## 1. Why this amendment is required

The base TSK-0229 contract remains technically and privacy-design valid for the **accountless journey**. Its own material-change rule, however, says that activating account/dashboard persistence requires a new data-contract decision and that J1 must not be silently repurposed into persistent customer history.

DEC-0053 / CR-0006 has now activated an **optional parent account and lightweight dashboard/device-management capability in Version 1**, while preserving the complete accountless core without login. This amendment resolves that specific change without expanding TSK-0229 into the later persistent-account architecture/schema task.

## 2. Base J0/J1 contract remains unchanged

All substantive `accountless-journey-data-v1` invariants remain current:

- J0 browser/session-only state is preferred;
- J1 remains an optional anonymous short-lived server record only where later architecture proves necessity;
- J1 remains subject to a non-sliding hard TTL of no more than 24 hours and the existing early-deletion rules;
- the J1 field allowlist remains unchanged;
- parent/child identity, stable customer/device identifiers, browsing/URL/DNS-query/domain/activity history, persistent child/family profiles, raw diagnostics, marketing attribution and unrestricted free text remain excluded;
- ordinary diagnostics remain separated from J1;
- live token/payload logging and durable J1 backup remain prohibited by default under the base contract;
- accountless completion remains possible without account creation or persistent identity.

The 24-hour and 15-minute values remain conservative internal product defaults, not legal thresholds or behavioral findings.

## 3. Separation from the optional Version-1 account

The optional parent account is a **separate persistent data domain** from J0/J1.

### 3.1 Default rule: no automatic linkage

J0/J1 must not be automatically joined, converted, stitched or promoted into a parent account/device record.

Prohibited automatic mechanisms include:

- storing an account ID, provider subject, email or stable parent/device ID in J1;
- mapping `journey_token` to an account identity;
- cross-session stitching through cookies, fingerprinting, IP address, analytics identifiers or device characteristics;
- copying a J1 history/event trail into an account;
- using DNS/query/domain history to associate an anonymous journey with an account;
- retaining J1 longer because the parent later signs in;
- treating account creation, device ownership or dashboard presence as evidence that DNS protection is technically active.

### 3.2 Explicit user action does not itself authorize data migration

DEC-0053 permits an optional account, and the current TSK-0146 baseline allows any future connection between anonymous and persistent state only through explicit approved user action plus an authorised data-flow design.

Therefore:

1. a parent may explicitly choose the optional account path without changing the J0/J1 contract;
2. signing in or creating an account creates/uses the **separate account data domain** defined by downstream authoritative work;
3. this TSK-0229 amendment authorizes **no automatic or implicit migration** of J1 fields into persistent account/device state;
4. if later UX/architecture requires an explicit "save this setup/device" transition, the exact field-by-field transfer, purpose, necessity, user action, retention, deletion, failure behavior and source/destination identifiers must first be approved in the downstream dual-mode data contract/architecture and verified against privacy/security requirements;
5. such an approved transition must not transfer browsing/query/activity history because those data classes remain prohibited entirely;
6. J1 expiry/deletion remains independent and must not become persistent merely because a separate account exists.

Until that downstream transfer contract exists, the safe rule is **separate account creation/management with no J1-to-account linkage**.

## 4. Persistent-account scope deliberately left downstream

TSK-0229 does not define the persistent account schema. Current authority places that work downstream, including the L5 task for the minimal dual-mode journey/account data model and related privacy/security architecture.

The future persistent domain may contain only the minimum classes already authorised by the post-CR-0006 product baseline: necessary parent identity/provider/account-lifecycle data and necessary parent-owned device ownership/settings/lifecycle data. Exact fields, lawful purpose/basis, recipients, storage, access, retention, backup, deletion, recovery and ownership enforcement are not invented or approved here.

## 5. DNS, diagnostics and observability remain separated

CR-0006 creates no exception to existing DNS privacy controls:

- persistent identifiable query/file logging remains off;
- identifiable per-client statistics remain off/excluded unless specifically justified under current authority;
- no browsing/top-domain metric becomes an account/dashboard feature;
- exceptional request-level diagnostics remain separately governed, time-boxed and deleted;
- account identity must not be used to reconstruct, persist or expose DNS/domain activity history.

## 6. Failure/deletion invariants after CR-0006

The accountless record and optional account must fail and delete independently:

- authentication/provider/account-store failure must not extend J1 TTL;
- account deletion does not imply J1 exists or needs retention;
- J1 deletion/expiry does not claim account or device-account deletion;
- account/device deletion does not claim DNS configuration was removed unless the technical removal is separately verified;
- a failed account transition must not leave a hidden account-to-J1 linkage or make the core journey login-dependent;
- restoring a service or backup must not resurrect an expired/deleted J1 into either anonymous or account state.

## 7. Current authoritative privacy-source check

Current official-source review on 2026-08-30 found no contradiction to the preserved minimisation/separation direction:

- GDPR Article 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary for the purposes; Article 5(1)(e) establishes storage limitation. Official consolidated text: `https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04`.
- GDPR Article 25 requires data-protection principles such as minimisation to be implemented through appropriate measures and, by default, only personal data necessary for each specific purpose to be processed. Official text: `https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04`.
- EDPB Guidelines 4/2019 on Article 25 remain published as the final version and support data protection by design/default. Official EDPB page: `https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en`.

These sources support minimisation/purpose separation. They do **not** establish that the internal J1 24-hour TTL or 15-minute cleanup bound is legally mandated, and this artifact does not issue a final legal-compliance conclusion.

## 8. Current requirement/interface/risk reconciliation

- **REQ-0018:** no real England participant activation is authorised here; DEC-0052 keeps first real-user validation in L8 after LG-09.
- **REQ-0019:** actual processing purposes/data/lawful basis/necessity/recipients/retention/rights/safeguards must match reality; downstream persistent-account work must complete that mapping before applicable later gates.
- **CON-0007:** persistent identifiable query/file logging remains off; exceptional diagnostics stay time-boxed/deleted.
- **CON-0008:** identifiable per-client statistics remain off/excluded unless specifically justified; no browsing/top-domain product metric.
- **INT-0006:** this amendment incorporates the applicable privacy controls without claiming final legal resolution.
- **INT-0007:** later implementation must prove actual data-flow reality matches the approved contracts; no implementation is claimed here.
- **RSK-0001:** unresolved England participant legal/data readiness remains open and blocks applicable later participant work, not this internal L4 data-contract amendment.
- **RSK-0002:** real behavioral/usability/comprehension evidence remains deferred to L8; none is inferred here.

## 9. Post-CR-0006 testable invariants added to the base fourteen

15. **Separate domains:** no J0/J1 schema field contains a persistent account/provider/customer/device-ownership identifier.
16. **No implicit conversion:** signing in/account creation cannot automatically convert J1 into persistent account/device state.
17. **No identity join:** no supported data path joins `journey_token` to account identity absent a separately approved downstream explicit-transfer contract.
18. **TTL independence:** account activity/sign-in cannot extend J1 hard expiry.
19. **No history transfer:** no browsing/query/domain/activity data can be transferred to or exposed by an account/dashboard.
20. **Verification independence:** account/device ownership does not change technical Protection Map verification semantics.
21. **Failure isolation:** failed auth/account persistence cannot create hidden J1 linkage or make accountless core value dependent on login.
22. **Deletion independence:** anonymous-state deletion, account/device deletion and DNS configuration removal are separate operations whose completion must be stated truthfully.

## 10. ACC-0229 post-change disposition

ACC-0229 requires only necessary active-journey fields, no browsing history or persistent child profile, and testable expiry/deletion/diagnostic boundaries.

The base `accountless-journey-data-v1` contract continues to satisfy those requirements. This amendment resolves the only material post-CR-0006 ambiguity by keeping anonymous J0/J1 state separate from the newly activated optional account and by requiring any future explicit transfer to be authorised by the downstream dual-mode data contract rather than silently broadening TSK-0229.

**TSK-0229 is ready for independent post-CR-0006 verification.**
