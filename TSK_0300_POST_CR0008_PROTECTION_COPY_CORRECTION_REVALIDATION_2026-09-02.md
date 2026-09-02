# TSK-0300 — Protection-State Copy Correction Revalidation — Post-CR-0008

**Task:** TSK-0300 — Translate the approved identity into shared tokens, components, templates, and asset conventions  
**Acceptance / Verification / Evidence:** ACC-0300 / VER-0300 / EVD-0300  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent verification, durable evidence publication, guarded runtime reconciliation and exact GitHub read-back.

## 1. Why this narrow revalidation is required

The current TSK-0300 runtime PASS was accepted after the CR-0006 dual-mode correction and remains valid for the owner-approved SafeWeb identity, single-token/component system, six-context architecture, optional-account continuity and no-J0/J1-linkage rules.

A later artifact-specific current-validity audit found one genuine contradiction inside two accepted TSK-0300 reference files: both claimed to use the current TSK-0320 vocabulary while still presenting historical protection-state labels (`Verified`, `You confirmed this is set up`, `Status uncertain`) that are superseded by the current TSK-0320/TSK-0299 copy contract.

Because ACC-0300 includes documented accessibility/state semantics, this contradiction is acceptance-relevant. It requires revalidation but does **not** justify redesigning the identity or replacing the shared system.

## 2. Current authority binding

Current canonical planning inputs remain:

- WBS `Plans/Master/WBS/master-wbs.csv`, blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship index `Plans/Master/RELATIONSHIP_INDEX.yaml`, blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `CURRENT_STATE.md`, blob `235cca98f7a3e1432b88e4581de5d0a80602195a`.

Current TSK-0300 contract remains L4 / HIGH / A3 / AUTO_ALLOWED with direct dependency exactly TSK-0301 and ACC-0300 requiring public/product/help/status/partner/social templates to derive from one token source with implementation values and accessibility states documented.

Current semantic owners relevant to this correction are:

- TSK-0299 current dual-mode verbal system: `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`, blob `ff30500b933b9ecc92325659d49ea4e671d296d2`;
- TSK-0320 current protection-state model/copy rules: `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md`, blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.

TSK-0301 remains the identity owner and current PASS. No current evidence reopens the identity decision.

## 3. Exact contradiction and correction

### 3.1 Shared-system README

Historical/current-pre-correction blob: `f7d013723c8dd967bb8337b44a52a19f32664d41`.

Contradiction: Section 4 stated that reference UI may demonstrate the current TSK-0320 vocabulary only, but listed historical primary labels rather than the current canonical copy.

Corrected `brand/system/TSK-0300/README.md` blob: `a54a2b653720160261b034149cadff62bc399102`, correction commit `7246b9bf4ad93d5467abcd4959d2f503ad9e3b7c`.

It now binds the current six primary labels:

1. `Protection verified`;
2. `Setup confirmed`, with mandatory supporting copy `Protection has not yet been technically verified.`;
3. `Action needed`;
4. `Not covered`;
5. `Protection status could not be verified`;
6. `Removed`.

### 3.2 Status reference template

Historical/current-pre-correction blob: `f4f3b32957c978fe9ea00704bd285a20e3c56aef`.

Corrected `brand/system/TSK-0300/templates/status.html` blob: `8f9971edfc87b2da8174330b9b4be68338a96fb4`, correction commit `97ef01c8a0dd0143378eeb4a0ef32b756fe19417`.

The status reference now presents the same current six-state copy, including the mandatory S2 limitation and current S5 uncertainty wording, while preserving text-plus-evidence and non-color-only presentation.

## 4. Explicit preservation boundary

The correction does **not** alter or reopen:

- `brand/system/TSK-0300/tokens.css`, blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- `brand/system/TSK-0300/components.css`, blob `831e92a74b6dda04252d93242cb33bd491a02381`;
- current dual-mode `templates/public.html`, blob `309f6a1f38474f78cd8a241aad3028fd495f9b8e`;
- current dual-mode `templates/product.html`, blob `872920b6f7af6561a1015e1d8fea55dcf95f1249`;
- owner-approved TSK-0301 identity masters, including the primary/inverse/monochrome/monogram blobs `f93958e3e4a16f9056693072c1b9b8b31fcda852`, `c38709e4239a2d36b340b4d9d630df85a17bb494`, `ef9b6e0d52926f24c7e81bccb4489569067b852f`, `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`;
- the shared color, typography, spacing, radius, focus, component or identity architecture;
- the complete login-free accountless core;
- optional non-coercive parent-account/session/dashboard/device-management continuity;
- separation of anonymous J0/J1 from persistent account state;
- the rule that account/session/dashboard/device ownership never proves protection;
- the prohibition on child profiles, browsing/query/activity history, unrestricted customer DNS administration, remote trackers/scripts, and font-binary delivery.

## 5. Current ACC-0300 mapping

Independent verification must prove:

1. TSK-0300 still has the current WBS/dependency/authority/ACC-VER-EVD contract.
2. Current predecessor TSK-0301 remains durable PASS.
3. The README and status reference use the exact current TSK-0320 primary copy and S2 limitation; stale historical primary labels are no longer used as the canonical current state list/reference.
4. Exactly six reference contexts remain public/product/help/status/partner/social and all use the shared `tokens.css` + `components.css` layer.
5. `tokens.css`, `components.css`, current public/product references and TSK-0301 identity masters remain unchanged from their accepted current blobs.
6. Brand color is never the sole protection-state carrier; state text plus evidence/limitation remains present.
7. Public/product dual-mode references preserve a complete accountless path plus optional non-coercive continuity, with no automatic J0/J1 linkage or protection-by-account inference.
8. No remote styles/scripts/trackers, duplicate identity authority or font-binary deliverable is introduced.
9. No implementation, authentication/provider architecture, persistence schema, legal/privacy completion, participant/publication/payment/market/production/launch/gate or successor PASS is inferred.

## 6. Disposition

The discovered contradiction is corrected by a two-file semantic patch. All other current TSK-0300 assets remain preserved. Subject to independent VER-0300 and durable evidence/read-back, the current TSK-0300 PASS may be reaccepted without redesign or identity reselection.

**ACC-0300 current correction candidate: PASS pending independent VER-0300, EVD-0300 and guarded runtime reconciliation.**
