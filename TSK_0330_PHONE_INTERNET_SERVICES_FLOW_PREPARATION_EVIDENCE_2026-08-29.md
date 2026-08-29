# TSK-0330 Phone → Internet → Services Flow Preparation Evidence — 2026-08-29

## Disposition

`TSK-0330 — Design Phone → Internet → Services setup flows`: **WAITING / non-PASS**. The exact candidate has been prepared and technically verified, but WBS Action Authority is `HUMAN_ONLY`; Project Owner disposition is required before TSK-0330 can be accepted.

## Authority and dependency

Current WBS blob: `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.

TSK-0330 WBS contract:
- title: `Design Phone → Internet → Services setup flows`;
- lifecycle: L4;
- plan status: `PLANNED`;
- planning-snapshot execution state: `WAITING`;
- dependency: `TSK-0146`;
- priority: `MEDIUM`;
- critical path: `NO`;
- Action Authority: `HUMAN_ONLY`;
- trigger: applicable lifecycle/gate and all hard dependencies satisfied;
- acceptance: each flow has prerequisites, step-by-step actions, verification/confirmation, skip conditions, unsupported/conflict states, troubleshooting, and no misleading completion state.

`TSK-0146` is a frozen WBS PASS dependency with no contradictory current runtime evidence. No additional dependency blocks preparation of TSK-0330.

`DEC-0052 / CR-0005` remains controlling: no pre-product parent/user/participant evidence is required or inferred; human/user validation begins only at L8 after LG-09. Accountless-first remains controlling; deferred account/dashboard/persistence scope is not activated.

## Pinned source basis

The candidate is a task-specific formalization of already accepted current authorities rather than a new product direction:

- `prototype/TSK-0309/BASELINE.md` v1.0.0 — blob `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`;
- `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` v1.0.0 — blob `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`;
- current accepted TSK-0310 behavioral reference, including the owner-approved TSK-0321 accessibility remediation;
- TSK-0320 protection-state semantics as incorporated by the baseline/catalogue;
- current WBS blob above.

The source baseline fixes the accountless critical journey and exact truth states. The instruction catalogue fixes current platform/source behavior, including Android `dns.usesafeweb.com`, iPhone `https://dns.usesafeweb.com/dns-query`, safe conflict/removal/recovery behavior, and the rule that no named external service is currently hard-coded.

## Candidate

Artifact:
- `design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md`
- blob `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7`
- creation commit `faf101dedba2bf9f33014ed892167afd8fc80ee5`

The candidate explicitly remains `not accepted / not PASS` and covers:

1. **Phone layer** — Android/iPhone native-safeguard routes, already-configured skip behavior, parent-confirmed truth state, unsupported/managed states, and safe help/recovery boundaries.
2. **Internet layer** — exact Android/iPhone SafeWeb DNS values, prerequisites, already-configured handling, qualifying technical verification before `Verified`, VPN/Private Relay/custom-resolver/managed/network conflict states, troubleshooting, removal and neutral connectivity recovery.
3. **Services layer** — zero services is valid; no named service is invented; at most one separately current approved service may be routed in the future; parent confirmation remains distinct from system verification.
4. **Protection Map completion** — Phone/Internet/Service remain independent evidence layers; mixed states are allowed; no overall safety score, `100% safe`, `fully protected`, certification, or equivalent completion claim.
5. **Navigation/state integrity** — back/resume/help/limitations/reset/removal behaviors are explicit and do not silently corrupt evidence state.
6. **Deterministic branch matrix** — 12 representative cases cover normal Android/iPhone, already-configured, unsupported, conflicts, managed devices, zero/one service, removal/recovery, and help/reset behavior.

No account, child profile, persistent device list, activity history, browsing/DNS history, payment, broad DNS administration, or new named-service requirement is introduced.

## Preparation verification

Verifier:
- temporary workflow `.github/workflows/verify-tsk0330-candidate.yml`;
- workflow head `b992a29df24bc70a75da876411396a6c8ded5bc9`;
- run `33279766680` — success;
- job `99172831252` — success;
- runner/machine `adguardvm`.

Pinned verification inputs:
- WBS `f23b4f017d1baf73258fa30ecd71549bbfe1b815`;
- TSK-0309 baseline `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`;
- TSK-0323 catalogue `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`;
- TSK-0330 candidate `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7`.

Terminal markers:
- `TSK0330_WBS_AUTHORITY=PASS`;
- `TSK0330_SOURCE_PINS=PASS`;
- `TSK0330_ACCEPTANCE_COVERAGE=PASS`;
- `TSK0330_TEST_MATRIX=12`;
- `TSK0330_SCOPE_TRUTH_GUARDS=PASS`;
- `REPOSITORY_CLEAN=PASS`;
- `TSK0330_CANDIDATE_VERIFICATION=PASS`.

The verifier confirmed the exact WBS title, dependency, HUMAN_ONLY authority, and all seven acceptance elements. It also confirmed required exact endpoint/state terms, all 12 branch cases, scope/claim guards, and the explicit non-PASS owner-decision boundary.

A browser rerun was not required for this preparation boundary because TSK-0330 does not mutate the already accepted prototype; it formalizes already accepted and previously browser-verified behavior into a task-specific design contract. Any later implementation mutation remains subject to its own applicable rendered/runtime verification.

## Downstream sequencing

TSK-0330 must be accepted before its dependent HUMAN_ONLY tasks can close:
- `TSK-0334 — Design support, false-positive, removal, and reconfiguration flows`;
- `TSK-0335 — Design Protection Map and coverage-limit interactions`.

`TSK-0333 — Assemble end-to-end responsive interactive prototype` is AUTO_ALLOWED but depends on TSK-0334 and TSK-0335 (plus frozen-PASS TSK-0146). Therefore LG-06 is **not yet ready** while these active-path L4 tasks remain unresolved.

## HUMAN_ONLY owner decision

Recommended exact approval:

`APPROVE TSK-0330 PHONE INTERNET SERVICES FLOWS`

Alternative:

`REVISE TSK-0330: <specific change>`

Until one of those owner dispositions is received, TSK-0330 remains **WAITING / non-PASS**. No TSK-0330 PASS, LG-06 PASS, L5/L6 authorization, real-user validation, public publication, payment, market activation, or launch authority is inferred.