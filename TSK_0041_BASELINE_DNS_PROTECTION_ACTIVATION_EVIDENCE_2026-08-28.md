# TSK-0041 — Baseline DNS-protection activation verification evidence

**Task:** TSK-0041 — Specify baseline DNS-protection activation requirements  
**Acceptance:** ACC-0041  
**Verification:** VER-0041 independent guarded requirements/evidence audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Requirements contract: `TSK_0041_BASELINE_DNS_PROTECTION_ACTIVATION_REQUIREMENTS_2026-08-28.md`
- Contract blob: `95a5292223f1d2c3c8f79d4c889ad91e917478b2`
- Contract commit: `12df8964d2e5d6185c4097c9317810aa16d6cb30`
- TSK-0408 DNS identity/platform contract blob: `52860ce167fc8a31962cd412772e428d280c8184`
- TSK-0409 support matrix blob: `09318534ec097849cbe8c7391e2a1acc3ba5a79a`
- TSK-0409 independent evidence blob: `87aac1d2affacacdbf1007581bce64d2383f5359`
- TSK-0511 supported-device evidence blob: `ecd959f93ab7dff62aba6529ce66b45d59c3ed27`
- TSK-0514 external endpoint/removal evidence blob: `c5d004d0e0a8c58d1056b3aaad38034ae4188a68`
- TSK-0406 filtering evidence blob: `bb4514b4af7c1c5e616b7875f98e86962fee0325`
- TSK-0512 filter regression evidence blob: `cc21f4574a2ca7e721a7da961baef727350af1d3`
- TSK-0207 privacy persistence evidence blob: `1c16db063e2e84d300b547075721d33c2e020e32`
- False-positive process blob: `9fab42f97e3e96023de89a8ed266acc21c0f06ab`
- TSK-0320 truth-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- Current hard predecessor: `TSK-0143 = PASS`.

## Authority and predecessor audit

The post-TSK-0559 queue identified TSK-0041 as the highest dependency-ready AUTO_ALLOWED L4 task after excluding TSK-0187 for representative-parent evidence and TSK-0140 for unavailable owner/multi-role review. A separate state-selection run then rechecked TSK-0041 as L4/A3/AUTO_ALLOWED/MEDIUM with direct predecessor TSK-0143 current PASS.

DEC-0050/CR-0003 permits this bounded internal requirements work because ACC-0041 can be fully evaluated from existing technical evidence without real-participant behavior. `RSK-0002` remains explicitly open.

## ACC-0041 clause audit

ACC-0041 requires: `Requirements cover endpoint format, DoH setup, filtering verification, fail-safe behavior, uninstall/removal, Private Relay/VPN conflicts, false positives, and no-history constraints.`

### Endpoint format — PASS

The contract freezes one service identity while keeping protocol input platform-specific:

- Android native Private DNS: hostname `dns.usesafeweb.com` using DoT/853.
- Apple DNS Settings profile: full DoH Server URL `https://dns.usesafeweb.com/dns-query`.

It prohibits a universal endpoint field and exposure of AdGuard admin/control credentials.

### DoH setup — PASS, reconciled to current platform authority

The Apple path explicitly uses the required DoH Server URL/profile. The legacy acceptance phrase cannot override newer accepted target evidence that Android native Private DNS is DoT-by-hostname. The contract records this reconciliation explicitly rather than fabricating an Android DoH UI workflow.

### Filtering verification — PASS

The contract requires controlled/synthetic verification of the intended UseSafeWeb path, including allowed and filtering evidence, and distinguishes transport reachability from functioning UseSafeWeb filtering. Current TSK-0512 target evidence directly proves blocked, allowed, narrow-exception and exact-rollback behavior while privacy/upstream invariants stay intact.

### Fail-safe behavior — PASS

Endpoint/authentication failure, unresolved effective resolver path, service outage and unsupported conflicts cannot retain a positive protection claim. The product must use Action needed/Status uncertain/Not covered, avoid hidden plain-DNS “protected” fallback, offer safe removal/recovery, and avoid instructing parents to weaken unrelated security/privacy/management controls just to produce S1.

The contract deliberately does not invent one universal OS-level fail-open/fail-closed behavior beyond direct platform evidence.

### Uninstall/removal — PASS

Android returns from the UseSafeWeb custom Private DNS provider to normal platform DNS policy and iPhone removes the exact UseSafeWeb DNS profile. Both terminate the UseSafeWeb protection claim and require neutral recovery checks. Direct TSK-0511/0514 evidence already proves removal/recovery on the accepted phone families.

### Private Relay / VPN conflicts — PASS

The contract consumes the TSK-0409 conflict matrix: Private Relay coexistence is unproven and therefore S5; Android/Apple VPNs can control tunnel DNS and therefore generic coexistence cannot be presumed; browser/app custom resolvers cannot inherit a universal system-DNS protection claim.

### False positives — PASS

The requirements preserve the already verified privacy-safe false-positive principles: reproduce synthetically where possible, identify whether filtering is actually causal, apply the narrowest explicit exception, retest allowed plus blocked behavior, keep the change reversible, and never disable the whole baseline for one site.

The active accountless baseline does **not** create a persistent per-parent/per-device personalized allowlist/dashboard. Current evidence proves a narrow technical exception mechanism only; individualized exception architecture remains a separate future decision if ever justified.

### No-history constraints — PASS

Activation/verification requires no browsing/domain history or persistent child/device identity. Query logging/file logging/identifiable statistics remain off and client-IP anonymisation remains enabled. Direct TSK-0207 production evidence proves no persistent raw query/domain history, identifiable client/statistics history or unapproved raw backup in controlled project locations.

## Cross-evidence audit

### Supported platform scope — PASS

Requirements do not expand beyond TSK-0409's accepted Android 9+ phone / iPhone iOS14+ family baselines and explicit unsupported/conflict rows.

### Protection-state truth — PASS

TSK-0320 semantics are preserved: configuration presence is not verification, contradictory evidence demotes positive state, unsupported is S4, uncertainty is S5, and removal is S6.

### Filtering evidence — PASS

TSK-0406/0512 prove the conservative one-list baseline, allowed-domain behavior, synthetic block, narrow explicit exception and rollback. The requirements do not claim complete online safety or require more aggressive lists.

### Privacy — PASS

TSK-0207 direct persistence evidence and the false-positive process prohibit routine query-history collection. Exceptional diagnostics remain separately governed and are not activated by TSK-0041.

## Adversarial findings and unresolved uncertainty

1. **Legacy “DoH setup” wording is narrower than current platform reality.** Treating it as a universal DoH requirement would contradict direct accepted Android evidence. The correct stable interpretation is Apple DoH plus Android native DoT under one encrypted-DNS activation contract.
2. **A future product verifier still needs implementation-level evidence.** Existing server/device tests prove the technical ingredients and required semantics; they do not by themselves prove the final web/app activation verifier UI/API.
3. **VPN/Private Relay/browser coexistence remains incomplete.** The requirements preserve uncertainty rather than pretending every request is covered.
4. **No per-device exception feature exists.** The global narrow exception mechanism must not be accidentally exposed as a persistent parent control plane under the accountless baseline.
5. **No universal fail-open/fail-closed platform promise is justified.** The product truth requirement is to never retain a UseSafeWeb protection claim when the intended path is unverified.
6. **Behavioral comprehension remains untested.** `RSK-0002` remains OPEN; no statement that parents understand or can easily execute these requirements is made.

## Stable verification decision

The durable requirements contract directly satisfies every ACC-0041 clause, reconciles its historical DoH wording to stronger current target evidence, and is grounded in direct filtering/device/removal/privacy proof without expanding product scope or claiming real-user validation.

**Stable outcome: TSK-0041 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the L4 queue. TSK-0313 is expected to become dependency-ready because its other predecessors TSK-0144 and TSK-0146 are already PASS, but it must be selected only after direct verification of all three predecessor states and its own acceptance/authority under CR-0003.
