# TSK-0307 — Current Source-Backed Instruction Catalogue Revalidation Acceptance Evidence

**Task:** TSK-0307 — Create the source-backed instruction/content catalogue with applicability and review triggers  
**Acceptance / Verification / Evidence:** ACC-0307 / VER-0307 / EVD-0307  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Current accepted artifact

- `TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `73a7028e247833bfe7e98487d9e079a51d36d424`
- publication commit `330e9d13b9d479212ca6c49df3431f19f7107ba5`

The current artifact preserves the historical nine instruction classes and ACC metadata model while refreshing first-party platform sources, changing stale parent-facing `UseSafeWeb` copy to the owner-approved `SafeWeb` / `SafeWeb DNS`, retaining literal technical `usesafeweb.com` endpoints, and adding the current Apple managed/security-policy caution from current TSK-0317. It does not introduce a new installation mechanism.

## 2. Current canonical and predecessor proof

Independent VER-0307 hash-locked:

- WBS `Plans/Master/WBS/master-wbs.csv` — `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship graph `Plans/Master/RELATIONSHIP_INDEX.yaml` — `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `CURRENT_STATE.md` — `6cc78a81d3b503902c915a2b02d88b81f75b8342`;
- current predecessor `TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md` — `37173d2f9cb970a7b5e6a83af90c8f868f9fbfa8`.

VER-0307 parsed the exact WBS row and proved:

- L4 / HIGH / A3 / `AUTO_ALLOWED`;
- direct dependency exactly `TSK-0317`;
- exact `ACC-0307 / VER-0307 / EVD-0307` IDs;
- ACC requires official source, platform/version/region, owner, last verification, review trigger, localized variants, known limits and test reference.

Markers:
- `TSK0307_CURRENT_WBS=PASS`;
- `TSK0307_CURRENT_PREDECESSOR=PASS`;
- `TSK0307_PREDECESSOR_ALIGNMENT=PASS`.

Current TSK-0317 remains the platform-path owner for Android/iPhone install/verify/remove/recover semantics and binds current visible SafeWeb naming, exact technical endpoints, complete accountless core, optional-account orthogonality, explicit user/OS actions and the rule not to weaken required security controls merely to obtain a positive protection state.

## 3. Historical provenance preserved

Historical catalogue:

- `TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md` — blob `d717c9b3f66197abe1f3e73361633f222b817e7c`.

Historical evidence:

- `TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_EVIDENCE_2026-08-28.md` — blob `7bc98f1b18f3a20c9a6be75138a4704b2002bf2f`.

The historical package remains provenance for the nine-class structure, per-entry metadata, applicability, limits, recovery semantics and trigger-based maintenance. Its stale generic parent-facing `UseSafeWeb` naming is superseded for current acceptance.

Marker: `TSK0307_HISTORICAL_PROVENANCE=PASS`.

## 4. Current first-party source review

Current source review was refreshed on 2026-09-02 and independently checked for both semantic binding and live reachability:

1. Android Help — Private DNS: `https://support.google.com/android/answer/9654714`.
2. Android `DevicePolicyManager`: `https://developer.android.com/reference/android/app/admin/DevicePolicyManager`.
3. Android `LinkProperties`: `https://developer.android.com/reference/android/net/LinkProperties`.
4. Apple DNS Settings payload: `https://support.apple.com/guide/deployment/dns-settings-payload-settings-dep86469ba99/web`.
5. Apple iPhone configuration profile install/remove: `https://support.apple.com/guide/iphone/install-or-remove-configuration-profiles-iph6c493b19/ios`.
6. Apple Personal Safety profile removal guidance: `https://support.apple.com/guide/personal-safety/ips327569a75/web`.

Current semantic facts bound by the catalogue and verifier include Android's Private DNS provider-hostname model, DNS-only scope, DNS-over-TLS specified-host semantics, current Private-DNS-active/server-name APIs, Apple's HTTPS/TLS DNS Settings semantics, explicit user permission for profile installation, current profile-management location, and managed/security-policy removal cautions.

Markers:
- `TSK0307_OFFICIAL_SOURCE_SET=PASS`;
- `TSK0307_CURRENT_SOURCE_SEMANTICS=PASS`;
- `TSK0307_OFFICIAL_SOURCE_REACHABILITY=6/6_PASS`.

## 5. Current nine-entry registry proof

VER-0307 parsed the current Markdown registry table structurally and proved exactly nine rows in the expected order:

- `INS-AND-SETUP-01`;
- `INS-AND-VERIFY-01`;
- `INS-AND-REMOVE-01`;
- `INS-IOS-SETUP-01`;
- `INS-IOS-VERIFY-01`;
- `INS-IOS-REMOVE-01`;
- `INS-COMMON-UNCERTAIN-01`;
- `INS-COMMON-NOTCOVERED-01`;
- `INS-COMMON-RECOVERY-01`.

Every row contains purpose, platform/version, region/locale applicability, official/current source, owner, last verified, review trigger, known limits and test reference; all current rows use `2026-09-02` as last verified.

Marker: `TSK0307_REGISTRY_FIELDS=9/9_PASS`.

## 6. Current naming, localization, truth and recovery proof

Independent verification proved:

- parent-facing instruction variants use `SafeWeb` / `SafeWeb DNS`, not generic `UseSafeWeb` copy;
- literal technical endpoints remain `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query` where owned and applicable;
- all nine instruction-class sections contain en-GB plus provisional tr-TR and ar variants;
- accountless setup/verification/help/removal remains complete;
- account/session/device ownership never substitutes for technical verification;
- no browsing/query/activity-history requirement is introduced;
- managed/security controls are not weakened simply to make SafeWeb appear protected;
- profile removal ends only the profile-owned DNS configuration claim;
- no silent plaintext fallback may retain a SafeWeb protection claim;
- consequential failed platform actions are reconciled before replay rather than blindly retried.

Markers:
- `TSK0307_SAFEWEB_NAMING=PASS`;
- `TSK0307_LOCALIZED_VARIANTS=9/9_PASS`;
- `TSK0307_TRUTH_SAFETY_RECOVERY=PASS`;
- `TSK0307_HISTORICAL_CURRENT_RECONCILIATION=PASS`.

## 7. Independent VER-0307

Final verifier identities:

- script `.github/scripts/verify_tsk0307_current_revalidation.py` — blob `34fb3b8532375ba7b6e080f44256f6f0ab9a0ddf`;
- workflow `.github/workflows/verify-tsk0307-current-revalidation.yml` — blob `00077c7dac9a5001001a077ea4e7482f76dea4c6`;
- workflow permission: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- final run `33586673039`;
- final job `100112160467`;
- conclusion: **SUCCESS**.

Final structural markers:

- `TSK0307_INPUT_HASHES=PASS`;
- `TSK0307_CURRENT_WBS=PASS`;
- `TSK0307_CURRENT_PREDECESSOR=PASS`;
- `TSK0307_HISTORICAL_PROVENANCE=PASS`;
- `TSK0307_PREDECESSOR_ALIGNMENT=PASS`;
- `TSK0307_REGISTRY_FIELDS=9/9_PASS`;
- `TSK0307_OFFICIAL_SOURCE_SET=PASS`;
- `TSK0307_CURRENT_SOURCE_SEMANTICS=PASS`;
- `TSK0307_SAFEWEB_NAMING=PASS`;
- `TSK0307_LOCALIZED_VARIANTS=9/9_PASS`;
- `TSK0307_TRUTH_SAFETY_RECOVERY=PASS`;
- `TSK0307_HISTORICAL_CURRENT_RECONCILIATION=PASS`;
- `TSK0307_NON_INFERENCE=PASS`;
- `TSK0307_CURRENT_ACC=PASS`;
- `TSK0307_CURRENT_VER=PASS`;
- `TSK0307_CURRENT_EVD_READY=PASS`;
- `TSK0307_CURRENT_REVALIDATION=PASS`.

External stage marker:
- `TSK0307_OFFICIAL_SOURCE_REACHABILITY=6/6_PASS`.

## 8. Diagnostic verifier corrections

Earlier failed verifier runs are retained as diagnostic evidence only. None changed the catalogue or runtime state. They exposed and corrected verifier defects including:

- an anomalous working-tree text read after the file hash had already been proven; immutable tracked reads were changed to `git show HEAD:<path>`;
- Markdown delimiters around `SafeWeb` / `SafeWeb DNS`;
- source-host scanning that initially included the legitimate technical SafeWeb DNS endpoint;
- visible-copy checking that initially included later historical-reconciliation prose;
- Markdown formatting around historical/current naming statements;
- a repeated-grammar assumption in the comma-separated non-inference list.

All corrections preserved the same ACC semantics and progressively increased structural precision.

## 9. Acceptance disposition

- Current WBS/dependency contract — **PASS**.
- Current TSK-0317 predecessor compatibility — **PASS**.
- Historical nine-class provenance — **PASS**.
- Current first-party source set/semantics/reachability — **PASS**.
- Nine registry rows and all ACC metadata — **PASS**.
- SafeWeb visible naming and exact technical endpoint distinction — **PASS**.
- Nine localized variant groups — **PASS**.
- Truth/safety/recovery boundaries — **PASS**.
- Historical/current reconciliation — **PASS**.
- Non-inference boundaries — **PASS**.

**ACC-0307 = PASS. VER-0307 = PASS. EVD-0307 = SATISFIED.**

**TSK-0307 current revalidation: PASS, pending only durable runtime reconciliation/read-back.**

## 10. Non-inference

This is internal L4 instruction/content definition only. It does not distribute a production Apple profile, implement account/session/dashboard behavior, prove native-speaker/representative-parent comprehension, complete legal/privacy review, publish publicly, process participants, activate payment/market, pass LG-06, launch, or infer any successor PASS.
