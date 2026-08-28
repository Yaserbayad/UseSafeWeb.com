# TSK-0512 — Filtering Regression Result

**Date:** 2026-08-28  
**Run source commit:** `f0a4225f12be4bf595b25da1edfadbe5c90e308d`  
**Target:** production host `adguardvm`  
**Regression outcome:** **PASS**

- Workflow blob: `02d191c657a5e01df5bd130ea63f08e32b96f9b6`
- Filter policy blob: `333a4ef8cd34719d66056aa608ab19473f839634`
- CURRENT_STATE blob at run checkout: `c050dda72a0fa684e2efdc444d3d577289ab7d63`
- Exact active baseline asserted: one enabled AdGuard DNS filter; no whitelist filters; no pre-existing user rules.
- Randomized reserved `.invalid` synthetic name was verified unfiltered before mutation.
- Temporary exact block was verified as `FilteredBlackList`.
- Matching narrow allow exception was verified as `NotFilteredWhiteList`.
- Exact pre-test user-rule set was restored and filter-list state remained unchanged.
- Persisted protection/filtering/default-blocking, Quad9 dns10, ECS-off, query-log-off, anonymisation-on and statistics-off invariants all passed assertions.
- Post-rollback `example.com` resolved successfully with at least one DNS answer.
- Cleanup/rollback assertions completed before this PASS result was published.
- No participant browsing history or raw DNS history was collected or retained.

ACC-0512 requires expected blocked tests to fail safely, allowed tests to resolve, the exception workflow to work, and results to be recorded without participant browsing history. **All applicable criteria are directly covered by this successful target-environment assertion run.**

**Stable acceptance result: TSK-0512 = PASS.**
