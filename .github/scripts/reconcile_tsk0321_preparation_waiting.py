#!/usr/bin/env python3
from pathlib import Path

path = Path('CURRENT_STATE.md')
text = path.read_text(encoding='utf-8')
marker = '## TSK-0321 prepared HUMAN_ONLY accessibility-review boundary — 2026-08-29'

if marker in text:
    print('RUNTIME_TSK0321_PREPARATION_NOOP=PASS')
    raise SystemExit(0)

section = r'''## TSK-0321 prepared HUMAN_ONLY accessibility-review boundary — 2026-08-29

`TSK-0321 — Review design and content against accessibility requirements`: **WAITING / non-PASS**. The accessibility review and a narrow remediation candidate have been prepared and fully verified as an overlay, but WBS Action Authority is `HUMAN_ONLY`; the remediation has not been applied to authoritative TSK-0310 and Project Owner approval has not yet been given.

- Review harness: `prototype/TSK-0321/accessibility-review.mjs`, blob `0cfca762a0d83be7716194e13e940876e71534b4`.
- Remediation candidate: `prototype/TSK-0321/REMEDIATION_CANDIDATE.css`, blob `5363c391cfdf96e4b454abb78f9ca4d8680caed1`; not applied to authoritative TSK-0310.
- Durable preparation evidence: `TSK_0321_ACCESSIBILITY_REVIEW_PREPARATION_EVIDENCE_2026-08-29.md`, blob `452536cb21b25b13b6c4f5d16bb2d015a66eeb1e`.
- Baseline full review run `33277211438` / job `99165918877` found 5 acceptance failures from 200% text reflow and 2 RTL technical-value conformance failures; all other tested accessibility/runtime checks passed.
- Final candidate-overlay run `33277610648` / job `99166984554`, Chromium `151.0.7922.34`, Playwright `1.62.0`: `A11Y_CHECKS=667`, `A11Y_FAILURES=0`, `A11Y_ACCEPTANCE_FAILURES=0`, all tested 200% reflow, RTL/LTR isolation, contrast, screen/state, headings/focus, keyboard/native controls, target floor, 320/768/1024/1440, reduced-motion, network/privacy and browser-runtime checks PASS.
- Two noncritical integrated-product notes remain recorded: `A11Y-LIVE-001` (scope broad `aria-live` unless manual screen-reader review supports it) and `A11Y-SKIP-001` (production repeated-navigation shell should provide a bypass/skip mechanism). They are not treated as unresolved critical barriers to the internal prototype review.
- AdGuard Home/Nginx remained active; loopback test listener was removed; repository-clean check passed.
- `RSK-0002` remains OPEN. `DEC-0052 / CR-0005` sequencing remains unchanged. No real-user/native-speaker validation, legal/privacy completion, production build, publication, participant processing, payment, market activation or launch authority is inferred.

### Deterministic resolution condition

Project Owner must provide one explicit disposition for this exact reviewed candidate:

- `APPROVE TSK-0321 ACCESSIBILITY REMEDIATION AND REVIEW`; or
- `REVISE TSK-0321: <specific change>`.

Approval authorizes applying the exact remediation to authoritative TSK-0310, rerunning both TSK-0310 rendered-browser acceptance and the full TSK-0321 accessibility review against actual source, and final ACC/VER/EVD processing. Preparation evidence alone is insufficient for PASS.
'''

path.write_text(text.rstrip() + '\n\n' + section.rstrip() + '\n', encoding='utf-8')
print('RUNTIME_TSK0321_PREPARATION_EDIT=PASS')
