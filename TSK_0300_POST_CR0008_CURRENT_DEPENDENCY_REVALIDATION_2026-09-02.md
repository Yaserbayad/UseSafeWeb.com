# TSK-0300 — Current Dependency-Complete Revalidation — Post-CR-0008

**Task:** TSK-0300 — Translate the approved identity into shared tokens, components, templates, and asset conventions  
**Acceptance / Verification / Evidence:** ACC-0300 / VER-0300 / EVD-0300  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Date:** 2026-09-02 UTC  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE

## 1. Revalidation purpose

Current TSK-0301 is now durable PASS under its dependency-complete post-CR-0008 revalidation, with the Project Owner's existing SafeWeb identity and all identity masters unchanged. TSK-0300 therefore requires current predecessor proof before its historical PASS can stand as current acceptance.

The historical shared brand system remains structurally valid, but current TSK-0318 exposes one CR-0006 semantic contradiction in the historical public/product reference wording: it stated that the current baseline had no Login/Dashboard/Account surfaces, while the current dual-mode IA includes an optional public Sign in / Manage devices entry plus account/session/dashboard/device-management surfaces.

This revalidation corrects only that current-scope contradiction. It does **not** redesign or reselect the SafeWeb identity and does not create a second brand system.

## 2. Current authoritative contract

Current canonical WBS blob: `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.  
Current relationship-index blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`.

The current WBS/graph contract previously read from these unchanged blobs establishes:

- lifecycle `L4`;
- priority `HIGH`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- hard dependency exactly `TSK-0301`;
- `ACC-0300 / VER-0300 / EVD-0300`;
- ACC-0300: public/product/help/status/partner/social templates derive from one token source, with implementation values and accessibility states documented.

The independent verifier must parse the current WBS directly again before acceptance.

## 3. Current predecessor and identity binding

Current TSK-0301 runtime state is PASS under:

- current revalidation artifact `TSK_0301_POST_CR0008_CURRENT_DEPENDENCY_REVALIDATION_2026-09-01.md`, blob `12c5de46b5ca880752d6f244e9bc2320e9689fa3`;
- current evidence `TSK_0301_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `c8935b9cfebe06fe1260b04d7af3c84318a6b5e0`;
- state commit `685746ae21df990c2e1b02049b104ce643748d00`.

Owner identity approval remains unchanged:

- `TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md`, blob `66f4b545c03571649a8baa4c0fe3d1df564b5949`;
- visible brand exactly `SafeWeb`;
- Concept A wordmark-first;
- primary dark green `#173F35` and warm maroon `#7A2E36` with the already-approved accessibility fallback.

Identity specification remains `brand/identity/TSK-0301/README.md`, blob `b8ffd2ed234465a238558a7b94e56274de49696a`.

Exact identity masters remain unchanged:

- primary `f93958e3e4a16f9056693072c1b9b8b31fcda852`;
- inverse `c38709e4239a2d36b340b4d9d630df85a17bb494`;
- monochrome `ef9b6e0d52926f24c7e81bccb4489569067b852f`;
- monogram `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`.

**Identity reselection required: NO. Identity redesign required: NO.**

## 4. Shared-system artifact disposition

The core implementation architecture remains unchanged:

- `brand/system/TSK-0300/tokens.css`, blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f` — still the sole mutable implementation token source;
- `brand/system/TSK-0300/components.css`, blob `831e92a74b6dda04252d93242cb33bd491a02381` — still consumes shared values through `var(--sw-...)`;
- all TSK-0301 identity masters remain referenced rather than copied/forked.

No color, typography, spacing, radius, sizing, focus, component or identity-master value was changed by this revalidation.

### Narrow corrected artifacts

1. `brand/system/TSK-0300/README.md`
   - historical blob `4baa67f565c14c3034fca47bb5fad0b9ff71b091`;
   - current blob `f7d013723c8dd967bb8337b44a52a19f32664d41`;
   - correction commit `1f73d3d37558f263d1ae4e12fe706312c3622023`.

   Current rules now explicitly preserve the complete accountless core while allowing optional parent-account/session/dashboard/device-management continuity, prohibit automatic J0/J1 linkage, keep lifecycle operations distinct, and retain SafeWeb naming/protection-state truth.

2. `brand/system/TSK-0300/templates/public.html`
   - historical blob `0146960a0f5b2abfe2458f0210ed750f0147d3b9`;
   - current blob `309f6a1f38474f78cd8a241aad3028fd495f9b8e`;
   - correction commit `eb055dfb58eedb0d90106cf19f6ca58827387015`.

   It retains `Start setup` as primary and adds only a secondary optional `Sign in / Manage devices` reference with `Continue without account`, no automatic anonymous-state linkage and no protection-by-account implication.

3. `brand/system/TSK-0300/templates/product.html`
   - historical blob `169acf5c8fc2c1f841111b99b8da1cfb6e9c5836`;
   - current blob `872920b6f7af6561a1015e1d8fea55dcf95f1249`;
   - correction commit `a88b316bd9642d7654cd318e7a5b5c4fe5f31fe6`.

   It preserves task-first accountless setup while demonstrating the current post-core choice between `Finish without account` and optional `Sign in to manage devices`; sign-in/dashboard presence never upgrades technical verification.

The other four context templates remain unchanged unless independent verification proves a contradiction.

## 5. Current dual-mode compatibility

Current TSK-0318 dual-mode IA artifact `TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md`, blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`, requires:

- public and product/setup systems to remain distinct;
- complete core value without authentication;
- optional but visible/non-coercive account continuity;
- public Start setup plus optional Sign in / Manage devices;
- accountless completion plus optional sign-in/manage choice;
- no automatic J0/J1 linkage;
- dashboard/device ownership not to substitute for protection verification;
- distinct logout/unlink/device-record/account-deletion/anonymous-state/DNS-removal operations.

Current TSK-0316 friction acceptance adds the same accountless-first/non-coercive continuity and ambiguous-consequential-effect rules. The corrected TSK-0300 reference layer now conforms without changing its shared token/component/identity architecture.

## 6. ACC-0300 current acceptance mapping

Independent verification must prove:

1. **Single implementation token source:** `tokens.css` remains the only mutable brand-value/token source.
2. **Six required contexts:** exactly public/product/help/status/partner/social reference templates remain present and all load the shared token/component layer.
3. **Shared component/asset conventions:** templates use TSK-0301 masters by reference and do not fork identity geometry or define a second brand palette.
4. **Accessibility/state semantics:** brand color is not the sole carrier of protection state; explicit textual/evidence semantics remain documented; low-contrast display usage retains the approved fallback rule.
5. **Current dual-mode compatibility:** public/product references preserve login-free core value while permitting optional account continuity without coercion, automatic J0/J1 linkage or protection-by-account inference.
6. **No remote/script/duplicate authority:** no remote styles/scripts/trackers or duplicated brand hex palette appears in templates/components.
7. **SafeWeb naming:** visible generic brand/product copy remains `SafeWeb` / `SafeWeb DNS`; technical identifiers remain literal only when technically required.
8. **No redesign/reselection:** exact TSK-0301 identity masters and token/component architecture remain unchanged.
9. **No downstream inference:** no integrated build, provider/auth architecture, persistent schema/storage, legal/privacy completion, participant/publication/payment/market/production/launch or gate PASS is inferred.

## 7. Preservation boundary

Before any runtime mutation, independent verification must hash-lock current accepted runtime sections for:

- corrected TSK-0299;
- TSK-0485;
- synchronized TSK-0318;
- synchronized TSK-0319;
- current TSK-0301;
- current TSK-0316.

Pre-runtime-mutation canonical runtime blob: `16e545c765219e7d1da735b45045f3a9a3621816`.

## 8. Candidate conclusion

The shared brand system requires **narrow semantic requalification, not redesign**. The token source, component layer, owner-approved SafeWeb identity and masters remain unchanged. The three corrected reference/convention files remove the one verified CR-0006 contradiction while preserving all current accountless-first, protection-truth, accessibility and governance fences.

**Candidate disposition: ACC-0300 current PASS pending independent VER-0300 and durable EVD/runtime read-back.**
