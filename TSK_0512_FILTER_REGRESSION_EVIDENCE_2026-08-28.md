# TSK-0512 — Baseline Filtering and Allowed-Domain Verification Evidence

**Task:** TSK-0512 — Verify baseline filtering and allowed-domain behavior  
**Acceptance:** ACC-0512  
**Verification:** VER-0512  
**Evidence:** EVD-0512  
**Date:** 2026-08-28  
**Target:** production self-hosted runner / host `adguardvm`

## Exact artifact/environment

- Workflow commit/run source: `217f7172efd52f467cf2bde5555c9bc65130350d`
- Workflow blob: `c2c22648c956dca388bec658676978bb5b5855d8`
- Filter policy blob: `333a4ef8cd34719d66056aa608ab19473f839634`
- CURRENT_STATE blob at run checkout: `c050dda72a0fa684e2efdc444d3d577289ab7d63`
- Filter policy version: `1.0.0`
- Active list required and verified by the target test: AdGuard DNS filter only.
- Frozen upstream/privacy invariants are asserted directly from the persisted production configuration.

## Fresh target verification

The preceding workflow step completed successfully on `adguardvm`. It is assertion-based and fails the job before this evidence step if any required condition is not directly observed.

Therefore this run directly verified all of the following on the target environment:

- filtering enabled with the one-list conservative baseline;
- zero pre-existing user rules and zero whitelist filters;
- randomized synthetic `.invalid` test name begins unfiltered/not-found;
- temporary exact synthetic block rule is observed as `FilteredBlackList`;
- matching narrow explicit allow exception is observed as `NotFilteredWhiteList`;
- exact pre-test user-rule set is restored and observed again as unfiltered/not-found;
- filter-list state is unchanged after rollback;
- persisted production policy still has protection/filtering enabled with default blocking mode;
- active filter remains exactly AdGuard DNS filter; AdAway remains outside the active baseline;
- Quad9 `dns10` upstream remains exact and ECS remains disabled;
- query logging remains disabled, client-IP anonymisation remains enabled, and statistics remain disabled;
- post-rollback `example.com` returns successful DNS resolution with at least one answer.

The synthetic block/allow/rollback mutation is guarded by a cleanup trap and the successful run proves the exact prior user-rule state was restored before evidence publication.

## Exception workflow

The current policy's narrow exception mechanism is directly exercised: reproduce synthetically, apply an exact block, apply the minimum matching allow exception, verify allowed behavior returns, then restore the exact prior rule set. The whole filtering baseline is never disabled.

## Privacy/evidence boundary

The regression uses only `example.com` and a randomized reserved `.invalid` synthetic name. Persistent query logging and identifiable statistics remain disabled. No participant browsing history, raw DNS history, participant identity, device identifier, credential, token or private key is written to this evidence.

## Acceptance evaluation

- Expected blocked synthetic test fails safely: **PASS**.
- Allowed-domain resolution succeeds: **PASS**.
- Narrow exception workflow works: **PASS**.
- Exact rollback restores the pre-test rule set: **PASS**.
- Privacy/upstream invariants remain intact: **PASS**.
- Evidence is tied to exact target artifacts/config and contains no participant browsing history: **PASS**.

**Stable outcome: TSK-0512 = PASS.**

This PASS is bounded to ACC-0512 and does not authorize participant activation or later release gates.
