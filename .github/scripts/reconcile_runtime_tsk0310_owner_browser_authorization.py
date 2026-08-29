from datetime import datetime, timezone
from pathlib import Path

p = Path("CURRENT_STATE.md")
text = p.read_text()
marker = "## TSK-0310 owner browser authorization — 2026-08-29"
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

## TSK-0310 owner browser authorization — 2026-08-29

The Project Owner explicitly authorizes installing Chromium/browser-test capability on operational runner `adguardvm` for the bounded purpose of completing current automated project testing, including `TSK-0310`. The browser may remain installed through the current testing tranche and is to be removed after that tranche when no longer needed.

This current owner instruction supersedes the earlier TSK-0310-specific runtime fence that prohibited installing browser/container capability on `adguardvm` merely to close the browser-evidence gap. The override is limited to browser-test tooling and required runtime dependencies; it does not authorize unrelated server changes, new production functionality, participant processing, public publication, payment, market activation, or launch.

Implementation must remain reversible and least-change: prefer a pinned Playwright-managed Chromium installation on Ubuntu 24.04, install only required browser runtime dependencies, do not alter AdGuard/Nginx configuration, do not expose a new listening service, retain privacy-safe verification evidence, and recheck AdGuard/Nginx health after installation/testing.

`TSK-0310` remains non-PASS until current rendered functional, negative, configuration, security/privacy, and removal/reset verification succeeds and durable evidence is accepted.

### Exact next authoritative step

Install the bounded Chromium test capability on `adguardvm`, verify server health is unchanged, execute the complete current `VER-0310` browser acceptance suite, retain durable evidence, then reconcile the stable task outcome.
"""

p.write_text("\n".join(lines) + appendix)
print("RUNTIME_TSK0310_OWNER_AUTH_EDIT=PASS")
