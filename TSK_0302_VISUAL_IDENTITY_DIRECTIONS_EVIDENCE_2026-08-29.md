# TSK-0302 — Visual Identity Directions Acceptance Evidence

**Task:** TSK-0302 — Develop and evaluate a small set of coherent visual identity directions  
**Date:** 2026-08-29  
**Acceptance:** ACC-0302 — directions are distinct, accessible, scalable, editable, aligned to brand strategy, and evaluated without premature high-volume asset production.  
**Authority:** DEC-0051 / CR-0004 + accepted TSK-0298 brand strategy + accepted TSK-0299 verbal system

## 1. Exact candidate package read-back

GitHub read-back of `brand/concepts/TSK-0302/` confirms exactly four TSK-0302 candidate files:

| Artifact | Git blob | Publication commit | Role |
| --- | --- | --- | --- |
| `README.md` | `59c01476f22147f5567c4d10fd0a0c122056ae23` | `426cb0b3a614a1770ca27fdafd78c99884be67ec` | Evaluation board / owner decision packet |
| `direction-a-open-path.svg` | `73a939877204da3602f31d0f53d5ef38de3f3cce` | `d86f29dc49f77d992949a59ece67d617fcbd15de` | Direction A — Open Path |
| `direction-b-open-guardrails.svg` | `0d5fc96aa280b90bdea3046ff80553237f3e3a5d` | `1708ddbd944e3edee8cb4583b342d1b8775798fd` | Direction B — Open Guardrails |
| `direction-c-connected-layers.svg` | `90dabad2cf77b26fa0480a7c55a97bd24d7c822b` | `57f6e4b14de98bfb62e75e485cde3ac186760f0e` | Direction C — Connected Layers |

No wordmark, font family, production token set, icon family, social asset pack, stationery, app icon, final logo package or high-volume derivative asset was created. Those remain later work and/or HUMAN_ONLY TSK-0301 authority.

## 2. Automated verification

Read-only GitHub Actions verification:

- Workflow: `Verify TSK-0302 visual directions`
- successful run: `33246716435`
- job: `99085341663`
- workflow revision commit: `22a50aa58f8b4620183d4dfc0855c5af62a33347`
- pre-verification runtime blob: `483f3b891a1cb8f42247b7af5c859eae579efa08`
- conclusion: **SUCCESS**

The initial run `33246691760` failed because the verifier compared only SVG element-type counts and therefore treated A and C as equivalent when both contained three paths plus one circle. No acceptance/state mutation occurred from that failure. The verifier was corrected to compare actual geometry attributes via SHA-256; the acceptance standard was not weakened.

### Successful geometry evidence

- Direction A geometry SHA-256: `9b4dd989ce3cd28954a5d16e098469023f34d501794c3b44721c39c6665c573d`
- Direction B geometry SHA-256: `713ded82177a7631723b97fe8415511c17b173cb6fbee93c7a711d3ffc124f74`
- Direction C geometry SHA-256: `0e992137b5b6185ea8e0da37bff32fc0c901429f12e8fe2669e15d7a89f230b5`

All three are distinct.

### Successful structural evidence

The verifier proved:

- exactly 3 concept SVGs;
- `256 × 256` vector viewBox on each;
- accessible SVG `role=img`, `<title>` and `<desc>` on each;
- basic path/circle geometry only;
- no raster `<image>`;
- no SVG `<text>` / font dependency;
- no JavaScript/script;
- no external resource/data URI;
- no filter, mask or pattern dependency;
- each source below 4 KB;
- geometry signatures are distinct;
- sources are human-readable/editable SVG.

Result lines: `EDITABLE_VECTOR_ONLY=PASS`, `NO_RASTER_FONT_SCRIPT_FILTER_EXTERNAL_RESOURCE=PASS`, `DISTINCT_GEOMETRY_SIGNATURES=PASS`, `TSK0302_AUTOMATED_VERIFICATION=PASS`.

## 3. Accessibility / contrast evidence

The direction board explicitly states that brand colour is not protection-state meaning and that later UI status meaning must remain textual/non-colour-only under TSK-0320/TSK-0314.

Automated WCAG contrast checks against white produced:

| Candidate colour | Contrast vs white | Current permitted role |
| --- | ---: | --- |
| `#12344D` | 12.93:1 | dark identity / text candidate |
| `#147D64` | 5.06:1 | secondary identity / text candidate |
| `#1F2937` | 14.68:1 | dark identity / text candidate |
| `#2563EB` | 5.17:1 | secondary identity / text candidate |
| `#12372A` | 13.08:1 | dark identity / text candidate |
| `#4338CA` | 7.90:1 | secondary identity / text candidate |
| `#C75B12` | 4.26:1 | accent / graphical or large-mark use; **not approved for small normal text** |
| `#B45309` | 5.02:1 | accent candidate; still treated as accent until final-system review |

Every colour intended as a normal-text candidate meets WCAG AA 4.5:1 against white. The lower `#C75B12` accent still exceeds the 3:1 non-text graphical threshold but is explicitly restricted from small normal-text use. Final selected-identity contrast remains subject to TSK-0301 acceptance and later design-system tokens.

## 4. Distinctness and strategic alignment

### A — Open Path

Distinct geometry: three horizontal rounded guardrail segments with an open endpoint.

Brand alignment:
- visually expresses a guided setup path;
- can map loosely to Phone / Internet / Service without claiming identical technical verification;
- open form avoids containment/control symbolism;
- no shield, eye, camera, lock, checkmark or safety score.

Primary risk retained for owner review: may read more as process/navigation than a standalone brand.

### B — Open Guardrails

Distinct geometry: two open rounded rails leading toward a forward point.

Brand alignment:
- directly expresses the accepted “guardrails for safer independence” idea;
- open rather than enclosing/controlling;
- no total-protection shield or monitoring symbol;
- calm rounded construction.

Primary risk retained for owner review: the forward point could be interpreted as media/play/navigation and needs final refinement if selected.

### C — Connected Layers

Distinct geometry: three offset open frames representing separate but connected safeguards.

Brand alignment:
- directly relates to Phone / Internet / Service coordination;
- open frames avoid a single total-protection enclosure;
- creates a potential modular visual grammar without requiring it now;
- no surveillance or certification symbol.

Primary risk retained for owner review: most complex direction at small size and could become generic platform branding if poorly paired later.

## 5. Scalability and editability — PASS

All masters are plain SVG paths/circles with no resolution-bound content. Their core recognition does not depend on embedded fonts, photos, gradients, filters or effects. The evaluation board requires later mono reduction and small/mobile optical testing before final identity approval.

This is sufficient for TSK-0302 concept-stage scalability/editability; it does **not** pre-certify TSK-0301 final small/mobile/mono/readability acceptance.

## 6. High-volume-production restraint — PASS

Exactly three mark concepts and one evaluation board were produced. No derivative family was generated. This intentionally preserves REQ-0025 and the CR-0004 provisional-design boundary rather than spending effort on final polish before owner direction selection and future behavioral validation.

## 7. Behavioral/legal/downstream fence audit — PASS

The board explicitly preserves:

- `RSK-0002 = OPEN`;
- no claim that any direction is parent-preferred/trusted/comprehended;
- no legal approval/compliance/certification claim;
- no publication, payment, market or launch authority;
- no integrated build authority;
- HUMAN_ONLY `TSK-0301` owner selection;
- future representative-parent evidence may reopen affected provisional assumptions.

No visual direction uses a closed shield, eye/camera/tracking motif, child surveillance imagery, safety score, all-green completion symbol, certification badge or total-protection wording.

## 8. ACC-0302 decision

**ACC-0302: PASS.**

All applicable concept-stage acceptance clauses are proven:

1. **distinct** — three different geometry signatures and three different strategic metaphors;
2. **accessible** — usable candidate text colours meet AA contrast, accent limitation is explicit, state semantics never depend on brand colour, SVGs contain accessible titles/descriptions;
3. **scalable** — resolution-independent simple vector geometry;
4. **editable** — plain source-controlled SVG masters with no raster/font/effect dependency;
5. **aligned to brand strategy** — each maps to clear guidance, safer independence and/or separate connected safeguards without surveillance/absolute-safety symbolism;
6. **evaluated** — strengths and risks are documented for each direction;
7. **no premature high-volume production** — three concept masters only.

**Stable disposition:** `TSK-0302 = PASS` under provisional internal L4 semantics, subject to runtime reconciliation/read-back. This does not select a final identity. Final selection/refinement remains HUMAN_ONLY `TSK-0301`.
