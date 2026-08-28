# TSK-0046 — Privacy-Safe DNS Host Capacity Baseline Evidence

**Task:** TSK-0046 — Define performance and capacity NFRs  
**Date:** 2026-08-28  
**Evidence class:** read-only point-in-time production-host capacity baseline  
**Target:** `adguardvm` / `srv.UseSafeWeb.com`

## Evidence boundary

This evidence records only privacy-safe host/resource/service metadata needed to ground performance/capacity planning. It does not read AdGuard query logs, DNS/domain history, client statistics, browsing data, participant identifiers, secrets, credentials, request payloads or customer traffic.

This is a **point-in-time baseline**, not a maximum-capacity benchmark and not proof of a future pilot load envelope.

## Execution evidence

Workflow: `.github/workflows/capture-tsk0046-host-baseline.yml`  
Workflow creation commit: `f8497932c718569bb6022881444cbe2bb9c8f9a4`  
Run: `33204389341`  
Job: `98961605638`  
Runner: `adguardvm`  
Machine: `adguardvm`  
Repository token permission: `contents: read` only.  
Result: **PASS**.

The job first required the accepted production machine-id SHA-256:

`e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`

No sudo or repository write was used by the host-capture job.

## Observed point-in-time baseline

- Logical CPUs: **2**.
- CPU model: **Intel(R) Xeon(R) Platinum 8370C CPU @ 2.80GHz**.
- Total memory: **4,105,707,520 bytes** (~3.82 GiB).
- Used memory snapshot: **909,778,944 bytes** (~0.85 GiB; ~22.2% of total).
- Available memory snapshot: **3,195,928,576 bytes** (~2.98 GiB; ~77.8% of total).
- Root filesystem total: **30,084,825,088 bytes** (~28.02 GiB).
- Root filesystem used: **4,082,577,408 bytes** (~3.80 GiB).
- Root filesystem available: **25,985,470,464 bytes** (~24.20 GiB).
- Root filesystem used: **14%**.
- Load average: **0.00 / 0.02 / 0.00** (1m / 5m / 15m).
- AdGuardHome service: **active**.
- Nginx service: **active**.
- AdGuardHome RSS snapshot: **153,300 KiB** (~149.7 MiB).
- AdGuardHome CPU snapshot: **0.0%**.
- Total Nginx RSS snapshot: **28,044 KiB** (~27.4 MiB).

## Interpretation limits

The observed host is lightly loaded at the capture instant and has substantial memory/disk headroom, but these observations **must not be converted into a QPS capacity claim**. A capacity claim requires a controlled privacy-safe synthetic load test using the TSK-0046 load model and acceptance rules.

The current production AdGuard abuse controls remain part of the accepted security baseline (`ratelimit=20`, IPv4 aggregation `/24`, IPv6 aggregation `/56`, empty whitelist, `refuse_any=true`). Capacity testing must not disable or weaken those controls merely to produce a larger number.

## Stable evidence outcome

**Host baseline capture: PASS.**

This evidence may ground TSK-0046 specification thresholds and later test planning. It does not authorize real-participant traffic, production stress testing, scaling, HA, infrastructure purchase or topology change.
