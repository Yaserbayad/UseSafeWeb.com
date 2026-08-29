from datetime import datetime, timezone
from pathlib import Path

p = Path("CURRENT_STATE.md")
text = p.read_text()
marker = "## TSK-0310 partial verification reconciliation — 2026-08-29"
if marker in text:
    print("RUNTIME_ALREADY_RECONCILED=PASS")
    raise SystemExit(0)

lines = text.splitlines()
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
for i, line in enumerate(lines):
    if line.startswith("**Updated:** "):
        lines[i] = f"**Updated:** {stamp}"
        break
else:
    raise RuntimeError("CURRENT_STATE.md missing Updated marker")

appendix = """

## TSK-0310 partial verification reconciliation — 2026-08-29

`TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation`: **WAITING / non-PASS**. Durable partial evidence is `TSK_0310_PROTOTYPE_PARTIAL_EVIDENCE_2026-08-29.md`, blob `edde3ebc641e392b6bde6cdc0896a4e3d60d8317`. Corrected verification run `33259265518` / job `99118278984` reached `MODEL_TESTS=PASS` for source/model, negative-path, configuration, security/privacy, removal/reset and state-integrity checks. Target-browser execution did not run because the current self-hosted runner reported `BROWSER_RUNTIME=UNAVAILABLE`; therefore VER-0310 remains incomplete and PASS is prohibited.

Deterministic resolution condition: provide an approved isolated browser-capable verification environment, rerun the rendered functional/negative/configuration/security-privacy/removal-reset checks, capture exact environment/result evidence, and then independently evaluate ACC-0310/VER-0310. This state does not authorize installing a browser on the operational AdGuard runner or incurring hosted-runner cost.

### Independent executable L4 work

Fresh post-verification dependency derivation identified `TSK-0297 — Publish concise brand guidelines, source/editable asset library, versioning, ownership, and usage rules` as the independent dependency-satisfied L4 task. Its exact WBS dependency `TSK-0300` is durable PASS; priority `MEDIUM`; Action Authority `AUTO_ALLOWED`. `RSK-0002` remains OPEN and all CR-0004 legal/privacy/participant/build/publication/payment/market/launch fences remain unchanged.

### Exact next authoritative step

Execute `TSK-0297` against its current ACC-0297 / VER-0297 / EVD-0297 contract, then persist/read-back the stable outcome and recompute eligibility.
"""

p.write_text("\n".join(lines) + appendix)
print("RUNTIME_RECONCILIATION_EDIT=PASS")
