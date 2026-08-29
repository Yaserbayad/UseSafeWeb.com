# SafeWeb — Approved Identity System

**Task:** TSK-0301  
**Status:** owner-approved identity system with editable/versioned masters; reusable application tokens/templates and production export packaging are created by TSK-0300  
**Owner approval record:** `TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md`

## 1. Canonical visible brand

The visible product/brand name is exactly **SafeWeb**.

- spelling/case: `SafeWeb`;
- `UseSafeWeb.com` is the domain/project identifier, not the visible brand wordmark;
- do not render `UseSafeWeb`, `Use SafeWeb`, `Safe Web`, `Safewipe`, or another variant as the brand name.

## 2. Primary identity direction

The approved identity is the Project Owner's selected **Concept A**: a minimalist wordmark-first system.

Core qualities:

- simple;
- clear;
- direct;
- memorable;
- calm;
- modern;
- trustworthy;
- warm without becoming decorative or alarmist.

The name itself is the primary logo. A separate shield/lock/security symbol is not part of the primary identity.

### Primary light-surface wordmark

- `Safe`: `#173F35` dark forest green;
- `Web`: `#7A2E36` warm maroon;
- preferred background: `#F6F4EF` off-white.

The division is semantic only as a brand composition: it must not be described as a protection score, safety state, verification state, risk class, product tier or technical boundary.

### Dark-surface display treatment

On the approved dark green brand field `#173F35`:

- `Safe`: `#F6F4EF`;
- `Web`: `#7A2E36` for large display-brand use where legibility is visually confirmed.

Because maroon and the dark-green field are close in luminance, this two-colour display treatment is **not** the default for small marks, compact UI, status content, or accessibility-critical text. Use the one-colour off-white fallback in those contexts.

### Monochrome treatments

Required fallbacks:

- dark monochrome wordmark on light backgrounds;
- off-white/white monochrome wordmark on dark backgrounds;
- single-colour mark for print, constrained contrast, grayscale, embossed/engraved, tiny and technical contexts.

No critical information may depend on the green/maroon split.

## 3. Editable / versioned master set

The approved TSK-0301 identity masters are source-controlled SVG text masters:

- `safeweb-wordmark-primary.svg` — primary `Safe` green / `Web` maroon lockup;
- `safeweb-wordmark-inverse.svg` — approved large dark-brand-surface treatment;
- `safeweb-wordmark-monochrome.svg` — single-colour fallback using `currentColor`;
- `safeweb-monogram.svg` — compact `Sw` secondary mark.

All four are plain editable SVG/XML, versioned in GitHub and contain no embedded raster image, script, remote resource or font file. They use the declared editable font stack `Avenir Next, Segoe UI, Helvetica Neue, Arial, sans-serif` as the working Concept-A typographic source. No font file is exposed or embedded.

This master set fixes the approved naming, colour split, hierarchy and composition. TSK-0300 must package reusable application assets/tokens and, where deterministic cross-platform reproduction requires it, create approved font-independent outlined/export variants from the owner-approved visual direction. TSK-0301 does not pretend a proprietary font file or unverified vector outline already exists.

## 4. Wordmark construction

The approved visual reference is Concept A's clean modern sans-serif wordmark treatment, with restrained custom character shaping and spacing.

Rules:

- preserve a single horizontal wordmark as the primary lockup;
- no icon inserted before, inside or after the primary wordmark;
- do not add a tagline into the primary logo lockup;
- do not outline, shadow, bevel, gradient-fill, texture or distort the wordmark;
- do not arbitrarily recolour individual letters beyond the approved `Safe`/`Web` split;
- do not mirror, stretch, condense, rotate or rearrange the letters;
- do not substitute a different visible brand name.

## 5. Monogram / favicon

Secondary compact identifier: **`Sw`**.

Preferred two-colour treatment:

- rounded dark-green field `#173F35`;
- `S`: `#F6F4EF`;
- `w`: `#7A2E36` where size/contrast permits;
- otherwise use a one-colour off-white monogram.

The monogram is for compact identity contexts such as favicon/app-like tile/avatar where the full wordmark is impractical. It is not a replacement for the full wordmark on normal public/product headers.

## 6. Approved palette

| Role | Value | Use |
| --- | --- | --- |
| Primary dark green | `#173F35` | primary identity, headings/brand surfaces where contrast permits |
| Deep green | `#0F2D23` | stronger dark surface / supporting identity tone |
| Warm maroon | `#7A2E36` | `Web` wordmark accent and restrained brand accent |
| Off-white | `#F6F4EF` | primary light background and inverse wordmark |
| Muted sage | `#A7BEAD` | low-emphasis decorative/supporting brand accent |

### Colour-governance rule

Brand colours must never replace the protection-state semantics defined by TSK-0320 or other product-state rules. Statuses such as protected, needs attention, not covered, uncertain or failed must remain explicitly textual/non-colour-only.

## 7. Accessibility and readability

Static WCAG relative-luminance calculation on the approved palette establishes approximately:

- `#173F35` on `#F6F4EF`: **10.6:1**;
- `#7A2E36` on `#F6F4EF`: **8.4:1**;
- `#F6F4EF` on `#173F35`: **10.6:1**;
- `#7A2E36` on `#173F35`: **1.3:1**.

The primary light-surface two-colour wordmark therefore has strong luminance separation from the off-white background. The maroon-on-dark-green display combination is low-contrast and must be treated as a large decorative/brand-mark exception, not normal text. For small/compact/accessibility-critical dark-background use, render the complete wordmark or monogram in `#F6F4EF`.

Logo marks are not used as substitutes for readable product instructions. Body copy, CTA labels, states, errors and instructions follow their own WCAG/product-content requirements.

## 8. Minimum-size / responsive use

- use the full wordmark only when `SafeWeb` remains immediately readable;
- switch to the `Sw` monogram for favicon/tiny-square identity contexts;
- use the monochrome master where the green/maroon split becomes visually unstable;
- never remove characters or abbreviate the public brand to `SW` in ordinary prose;
- preserve clear surrounding space; do not crowd the mark with controls, status badges or legal copy.

Exact production pixel/mm minimums are derived in TSK-0300 from the actual export set/render tests rather than fabricated here.

## 9. Multilingual / RTL use

`SafeWeb` is a proper brand name and remains **Latin-script, LTR and untranslated** in English, Turkish and Arabic interfaces.

In RTL layouts:

- isolate the wordmark/brand token as LTR;
- do not mirror or reverse it;
- do not reorder `Safe` and `Web`;
- do not transliterate it inside the logo;
- surrounding Arabic copy may be RTL independently.

This preserves one coherent identity while allowing the product/content system to localize normally.

## 10. Iconography, imagery and visual language

The identity should remain visually restrained and human rather than security-theatrical.

Avoid as brand motifs:

- shields;
- padlocks;
- eyes;
- cameras;
- tracking/radar motifs;
- child silhouettes;
- certification/check-seal badges implying verified or complete safety;
- warning-triangle-heavy styling;
- hacker/cyber-neon clichés;
- fear-based imagery.

Preferred supporting visual language:

- simple geometry;
- generous whitespace;
- calm photography/illustration when imagery is needed;
- ordinary family/device context without surveillance framing;
- restrained rounded forms that are compatible with the approved monogram tile;
- no decorative complexity that competes with the wordmark.

## 11. Layout principles

- mobile-first readability;
- generous whitespace;
- short hierarchy;
- few simultaneous visual accents;
- dark green as the dominant identity colour;
- maroon as a warm secondary accent rather than a warning colour;
- off-white as the preferred calm light canvas;
- no dense dashboard aesthetic for the accountless-first setup experience.

## 12. Cross-surface hierarchy

### Public website

Use the full `SafeWeb` wordmark prominently in header/brand contexts. Keep public messaging distinct from the setup surface while sharing this identity system.

### Setup/product surface

Use the same wordmark, palette and primitives, but prioritize instructions, protection-state truth and task completion over branding. Do not let decorative branding obscure setup status or uncertainty.

### Technical/support/recovery content

Prefer monochrome or high-contrast identity treatments where clarity dominates. The actual domain `UseSafeWeb.com` or resolver hostname may be shown when technically necessary without turning `Use` into visible brand naming.

## 13. Rationale against accepted brand criteria

| Accepted TSK-0298/0299 criterion | Identity response |
| --- | --- |
| Calm / non-alarmist | restrained wordmark, dark green/off-white foundation |
| Clear / practical | name-first identity with no symbolic decoding required |
| Protective, not controlling | avoids surveillance/control iconography |
| Truthful | no shield/check/certification mark implying complete safety |
| Privacy-respecting | no eye/camera/tracking motifs |
| Simple self-service orientation | minimal visual hierarchy suitable for setup flows |
| Cross-surface reuse | full wordmark + compact monogram + monochrome fallbacks |
| Multilingual/RTL support | invariant LTR brand token with isolated RTL behavior |
| Warmth requested by owner | maroon `Web` treatment and restrained secondary accents |

## 14. Authority / non-inference

This identity is owner-approved for provisional internal L4 work under DEC-0051/CR-0004. It does **not** prove representative-parent comprehension/preference and does not satisfy legal, participant, build, publication, payment, market or launch gates.

`RSK-0002` remains OPEN. Future contradictory representative-parent evidence may require re-evaluation before downstream freeze/launch progression.
