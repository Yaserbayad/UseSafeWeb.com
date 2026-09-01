# TSK-0324 — Post-CR-0007 Dual-Mode UI Component Acceptance Evidence

**Task:** `TSK-0324 — Define lightweight visual identity and reusable UI component rules`  
**Acceptance / Verification / Evidence:** `ACC-0324 / VER-0324 / EVD-0324`  
**Date:** 2026-09-01  
**Action authority:** A3 / `AUTO_ALLOWED`  
**Disposition:** PASS, subject to guarded runtime reconciliation/read-back

## Current contract

Current WBS authority remains L4 / MEDIUM with sole dependency `TSK-0322`. ACC-0324 requires typography, spacing, contrast, focus, controls, feedback, Protection Map states, mobile/desktop behavior, logo/domain use and accessible component specifications.

The sole dependency `TSK-0322` is current-qualified under the post-CR-0007 dual-mode language policy.

## Accepted current artifacts

- `prototype/TSK-0324/UI_COMPONENT_RULES.md` — version `1.1.0-post-cr0007`, blob `8747acdf6e0e98f91e8327b7225bd954956aaef1`.
- `prototype/TSK-0324/COMPONENT_CONTRACT.json` — schema `usesafeweb.tsk0324.component-contract.v1`, version `1.1.0-post-cr0007`, blob `55bc1d643b6b10ed1dbafce8c0ea3dc7c69f168d`.
- bounded dual-mode update commit: `bbc5da09441d5b392a1d4e7933ccfef977be7de8`.
- WCAG-review-date normalization commit: `32ca8f0` from workflow run `33483974575 / 99779640936`.

The shared design-system sources remain byte-identical and are not forked:

- `brand/system/TSK-0300/tokens.css` — `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`.
- `brand/system/TSK-0300/components.css` — `831e92a74b6dda04252d93242cb33bd491a02381`.

## Current-scope correction

The historical TSK-0324 contract contained one stale pre-CR-0006 requirement: `BrandHeader` prohibited account/dashboard navigation. That was no longer compatible with the owner-approved optional parent account/session and lightweight dashboard/device-management scope.

The current contract replaces only that exclusion with bounded dual-mode rules:

- accountless core navigation remains available;
- optional sign-in/account/dashboard navigation may appear only where current IA permits;
- optional account/session/dashboard UI never gates setup, verification, Help, recovery or removal;
- account/session/saved-device/dashboard presence never establishes technical protection evidence;
- saved-device record metadata remains distinct from Protection Map state;
- logout, account deletion, saved-record deletion, revoke/unlink and physical SafeWeb DNS removal remain distinct operations;
- destructive account/device controls are keyboard-operable, visibly focusable and require the current consequence/confirmation pattern;
- unknown destructive results remain uncertain, block duplicate destructive replay and never announce success;
- at 320 px the accountless core path, current protection truth, recovery and removal remain reachable;
- browsing/query/activity history, child profiles/accounts and broad/raw DNS administration remain prohibited.

## Preserved accepted design/accessibility contract

Independent verification proves the existing accepted consumer contract was preserved:

- typography and spacing still consume only the current TSK-0300 token sets;
- contrast, focus and primary/secondary/quiet control rules are unchanged;
- all six current S1–S6 Protection Map states remain supported, so ACC-0324's historical four-state minimum remains satisfied without dropping S5/S6;
- 320/768/1024/1440 responsive acceptance remains explicit;
- visible brand remains `SafeWeb`; `UseSafeWeb.com` remains the domain/project identifier;
- RTL and technical-value LTR rules remain;
- no combined safety score or color-only critical state meaning is allowed;
- text-resize, target-size, heading, focus and keyboard requirements remain.

## Current accessibility source review

Current W3C WCAG 2.2 source classification was rechecked on 2026-09-01. The contract continues to treat the 24×24 CSS-pixel Target Size (Minimum) criterion as Level AA and Focus Appearance as the stronger Level AAA reference; Focus Appearance is not mislabeled as an AA requirement.

The deterministic verifier independently recomputed all accepted contrast pairs and confirmed each accepted pair remains above its required threshold while the prohibited maroon/deep-green critical pair remains below normal-text AA contrast and therefore remains fenced from critical use.

## Deterministic verification

Verifier: `.github/scripts/verify_tsk0324_post_cr0007_dual_mode_20260901.py`, blob `b7e9fd8db2ba1f889bc1183f5ff21d34e5fc7b37`.  
Workflow: `.github/workflows/verify-tsk0324-post-cr0007-dual-mode-20260901.yml`, blob `2433577b2ce7ec6ac7e2cad870ddc75343c04f77`.  
Successful run/job: `33484058318 / 99779915675` on GitHub-hosted Ubuntu 24.04.

Observed markers:

- `TSK0324_CURRENT_BLOBS=PASS`
- `TSK0324_WBS_CONTRACT=PASS`
- `TSK0324_CURRENT_DEPENDENCY=PASS`
- `TSK0324_NORMATIVE_CONTRACT=PASS`
- `TSK0324_PRESERVED_BASE_CONTRACT=PASS`
- `TSK0324_DUAL_MODE_COMPONENTS=PASS`
- `TSK0324_ACCESSIBILITY_MATH_SOURCE_CLASSIFICATION=PASS`
- `TSK0324_LANGUAGE_POLICY_ALIGNMENT=PASS`
- `TSK0324_POST_CR0007_VERIFICATION=PASS`

## Non-inference fence

This PASS proves the current internal L4 reusable UI component/accessibility consumer contract only. It does not self-certify TSK-0321's HUMAN_ONLY integrated accessibility review, public publication, production implementation, participant evidence, payment, market activation or launch.

**TSK-0324: PASS.**
