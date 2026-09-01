# TSK-0144 — External-service safeguard requirement

**Version:** 1.0.0-post-CR-0008  
**Date:** 2026-09-01  
**Status:** current requirements freeze candidate  
**Action authority:** A3 / AUTO_ALLOWED  
**Dependency:** TSK-0143 current PASS  
**Acceptance:** ACC-0144 / VER-0144 / EVD-0144

## 1. Decision

UseSafeWeb shall include **at most one relevant external-service safeguard step per setup journey**, selected only from a current approved service-instruction catalogue and only when a parent explicitly identifies that service as relevant.

This requirement is intentionally **service-agnostic**. TSK-0144 does not freeze YouTube, Google, Apple, a social network, a streaming service, or any other vendor as the permanent external-service safeguard. The historical source requires service-selection logic that remains modular as platform/policy context changes and explicitly limits the experience to one relevant service rather than an app catalogue.

This document defines a requirement only. It does **not** assert that any external-service integration, setting, protection, monitoring, or verification is currently implemented or active.

## 2. Governing boundaries

This requirement implements `REQ-0007` and `REQ-0008` and remains subordinate to:

- `CON-0001`: public identity remains UseSafeWeb.com;
- `CON-0002`: AdGuard remains the frozen filtering backend absent a verified material blocker;
- `RSK-0002`: no legal/safeguarding completion is inferred and no child-facing data expansion is authorized;
- `INT-0003`: native-device/profile routing remains a separate device-configuration interface;
- `INT-0004`: encrypted DNS to the AdGuard filtering backend remains a separate DNS path;
- TSK-0143: supported native-device safeguard routing and truthful setup-state boundaries remain unchanged;
- TSK-0320: parent/configuration confirmation can never masquerade as technical protection verification.

The external-service step is **complementary guidance**, not a replacement for native safeguards or AdGuard-backed encrypted DNS.

## 3. Eligibility and selection

A service is eligible for the single external-service step only when all of the following are true:

1. the parent explicitly indicates that the service is relevant to this setup; UseSafeWeb does not scan installed apps, browsing history, DNS history, device activity, account activity, or child behavior to infer relevance;
2. the service exists in the approved, versioned service-instruction catalogue;
3. the catalogue entry has a current source reference, applicability/version scope, last-reviewed date, content owner, expected result, scope-limit statement, fallback, and test case;
4. the current platform/account context needed by the instruction is supported and known without collecting prohibited data; and
5. the instruction can be presented without requiring UseSafeWeb to receive the parent's or child's external-service credentials, tokens, browsing/activity history, contact graph, or content history.

If no service meets every rule, the external-service layer resolves to **Not covered** rather than manufacturing an action.

If more than one service could be relevant, UseSafeWeb shall not enumerate a broad app catalogue or silently rank vendors. The parent may choose **one** currently supported relevant service; after one is chosen, no second external-service safeguard task is created in that journey.

## 4. Supported and unsupported states

### Supported

A selected service is `supported` only when its current catalogue entry passes the eligibility rules above and the exact instruction remains current for the declared context.

### Unsupported / stale / irrelevant

The layer resolves to **Not covered** when:

- the parent says no currently supported service is relevant;
- the selected service has no approved catalogue entry;
- the applicable vendor/platform/account instruction is stale, withdrawn, materially changed, or cannot be verified as current;
- the required setup would demand prohibited data collection or credentials by UseSafeWeb; or
- the service-specific safeguard no longer exists or its scope cannot be represented truthfully.

A transient catalogue/read failure may surface `uncertain/error` while retry/recovery is available, but it must never appear as configured or protected merely because a service was selected.

## 5. Setup behavior

For one eligible selected service, UseSafeWeb shall:

1. name the selected service and the specific safeguard setting/control from the current catalogue entry;
2. state who performs the action (normally the parent in the external service's own interface);
3. show versioned, source-linked setup guidance with applicability and last-reviewed information;
4. state the expected result and material limits before the parent confirms completion;
5. direct the parent to perform the setting in the external service itself; UseSafeWeb shall not proxy credentials or impersonate the parent/child account;
6. provide a clear `I did this` / equivalent parent-confirmation action only after the guidance is shown;
7. record only the minimum approved journey state needed to represent that confirmation; and
8. provide fallback to **Not covered** when current support cannot be established.

No external-service safeguard is silently enabled by UseSafeWeb unless a later separately approved implementation task explicitly authorizes and verifies such an integration.

## 6. Truthful state and evidence semantics

The default evidence for this layer is parent/configuration confirmation, not technical system verification.

- Merely selecting a service creates no protection state.
- Showing instructions creates no protection state.
- Parent confirmation may produce **configured / parent-confirmed** for this service-specific step when the current state model permits it.
- Parent confirmation alone may **never** produce `protected/verified`.
- `protected/verified` would require fresh qualifying technical evidence explicitly defined and implemented by a later approved task; no such evidence is asserted by TSK-0144.
- Unsupported, stale or materially ambiguous instructions must not inherit a green/protected state.
- The state of this service-specific step must never strengthen the technical DNS protection state governed by the effective encrypted-DNS path.

## 7. User-facing framing

Required framing pattern:

> **Extra service setting** — This step applies only to the service you selected. Follow the current service instructions, then tell us when you have completed them. Your confirmation means you configured the setting; it does not prove complete device, internet, DNS, or service protection.

When unsupported:

> **Not covered** — UseSafeWeb does not currently have verified, current guidance for this service/context. We will not guess or mark it protected.

Copy may be shortened or translated downstream, but it must preserve all of these meanings:

- service-specific, not universal;
- complementary, not a replacement for DNS/native controls;
- parent confirmation is not technical verification;
- no complete-safety claim;
- unsupported/stale guidance is not presented as active protection.

## 8. Privacy, safeguarding and security limits

The external-service layer shall not require or create:

- child accounts in UseSafeWeb;
- external-service usernames, passwords, OAuth tokens or session cookies held by UseSafeWeb solely to complete this guidance step;
- browsing/query/activity/content history;
- installed-app inventory or device surveillance;
- persistent child/family behavioral profiles;
- unrestricted customer DNS administration;
- a persistent personal DNS allowlist;
- hidden service detection from DNS traffic or analytics.

Optional UseSafeWeb parent-account/device ownership may persist the approved last-known product state only where separately authorized; it cannot convert parent confirmation into technical verification.

## 9. Content ownership and change control

- **Product** owns the one-service selection policy and eligibility rules.
- **Content** owns catalogue instruction freshness, source reference, applicability/version, last-reviewed date and user-facing guidance.
- **QA** verifies setup-path, scope-limit, unsupported-state and parent-confirmation behavior before a catalogue entry is treated as supported.
- **Privacy/Safeguarding** review is required when a proposed service instruction would add data collection, credentials, account linkage or materially different child-facing processing.

A vendor/platform policy or UI change invalidates the affected supported entry until its instruction is reverified. Stale guidance fails to **Not covered**; it is not left active for convenience.

## 10. Deterministic acceptance assertions

TSK-0144 satisfies its current requirement only if all assertions are true:

1. Exactly one external-service safeguard may be selected per journey.
2. Selection is parent-declared and catalogue-based, not surveillance/inference based.
3. The requirement remains modular/service-agnostic; no permanent vendor is invented by this task.
4. Supported status requires a current versioned catalogue entry with source, applicability, owner, expected result, scope limits, fallback and test.
5. Unsupported/stale/irrelevant cases resolve to Not covered rather than artificial work/protection.
6. Setup guidance is performed in the external service and does not require UseSafeWeb to hold service credentials for this guidance requirement.
7. Parent confirmation remains distinct from technical verification.
8. No parent/service confirmation strengthens the DNS technical protection state.
9. User-facing copy states the service-specific scope and no-complete-protection limit.
10. Content ownership and stale-content invalidation are explicit.
11. The requirement introduces no browsing/query/activity history or child surveillance.
12. Nothing in this artifact claims the safeguard is already implemented, enabled, verified or active.

## 11. Plan trace

- Task: `TSK-0144 — Specify the one relevant external-service safeguard step`
- Dependency: `TSK-0143`
- Requirements: `REQ-0007`; `REQ-0008`
- Constraints: `CON-0001`; `CON-0002`
- Risk: `RSK-0002`
- Interfaces: `INT-0003`; `INT-0004`
- Acceptance: `ACC-0144`
- Verification: `VER-0144`
- Evidence: `EVD-0144`

Historical source semantics preserved: eligibility, supported/unsupported state, one-service limit, parent confirmation, content-update ownership, fallback to Not covered, and service-agnostic selection/routing rather than an app catalogue.

## 12. Non-inference

Acceptance of TSK-0144 does not make any external-service safeguard implementation active; does not approve a specific external vendor; does not establish vendor/legal/privacy compliance; does not prove user protection; and does not imply any L5 architecture, build, release, production, market, participant, or launch gate PASS.
