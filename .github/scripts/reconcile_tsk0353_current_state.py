from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "0a0fc742d3e0d54dbb07c29275b4d5e1358c4fd4",
    "TSK_0353_POST_CR0008_AUTHORIZATION_SESSION_ACCOUNT_LIFECYCLE_NFRS_2026-09-02.md": "3cb7c248b6d121e1c8d9db47accdf639998edc93",
    "TSK_0353_POST_CR0008_CURRENT_NFR_EVIDENCE_2026-09-02.md": "a87a0fa9e3fbf227869d7ef81f68c1828d7944bb",
}

HEADING = "## TSK-0353 current accepted stable state — 2026-09-02 — POST-CR-0008 AUTHORIZATION/SESSION/ACCOUNT-LIFECYCLE NFR"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


runtime_path = Path("CURRENT_STATE.md")
old = runtime_path.read_text(encoding="utf-8")

if HEADING in old:
    section = old.split(HEADING, 1)[1]
    for value in ["**PASS**", "3cb7c248b6d121e1c8d9db47accdf639998edc93", "a87a0fa9e3fbf227869d7ef81f68c1828d7944bb", "33589319072", "100119889794"]:
        assert value in section, value
    print("TSK0353_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0353_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0353")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0230", "TSK-0484"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0353", "VER-0353", "EVD-0353")
print("TSK0353_STATE_WBS_CONTRACT=PASS")

evidence = Path("TSK_0353_POST_CR0008_CURRENT_NFR_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in ["ACC-0353 = PASS", "VER-0353 = PASS", "EVD-0353 = SATISFIED", "33589319072", "100119889794", "TSK0353_CURRENT_NFR=PASS"]:
    assert value in evidence, value
print("TSK0353_STATE_EVIDENCE_BINDING=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0353 — Define authentication, authorization, session and account-lifecycle NFRs`: **PASS** under current `ACC-0353 / VER-0353 / EVD-0353`, current direct predecessors TSK-0230 / TSK-0484 and the current dual-mode Version-1 accountless-first product boundary.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0230; TSK-0484`.
- Current artifact `TSK_0353_POST_CR0008_AUTHORIZATION_SESSION_ACCOUNT_LIFECYCLE_NFRS_2026-09-02.md`, version `1.0.0-post-CR0008`, blob `3cb7c248b6d121e1c8d9db47accdf639998edc93`, publication commit `5b12d4d78589c5c76013422dfa98ab8fab2ab64d`.
- Durable evidence `TSK_0353_POST_CR0008_CURRENT_NFR_EVIDENCE_2026-09-02.md`, blob `a87a0fa9e3fbf227869d7ef81f68c1828d7944bb`, publication commit `b089aed4ade87d9f25deb62b8abf2cef5e583e8f`.
- Independent read-only VER-0353: verifier script blob `9c60b5b087eaf9dd2a2a79e9440997bb89d7fa67`; workflow blob `ef2bc9ac92ab11886859af397c91ae602f511b10`; run/job `33589319072 / 100119889794`; conclusion **SUCCESS**, no verifier correction cycle.
- Token rule: Firebase/Google identity is accepted only after backend signature/issuer/audience/expiry/subject verification and applicable CSRF/revocation checks; immutable provider subject/UID, not email, anchors identity.
- Session rule: server-managed host cookie is `Secure`, `HttpOnly`, explicit `SameSite=Lax` baseline, non-sliding and maximum 7 days; recent authentication `<=5 minutes` is required before session issue and high-risk account operations.
- Authorization rule: every account/device operation derives parent identity from the verified session and performs server-side parent-to-object ownership authorization; opaque IDs/ClientID are never authorization or technical protection evidence.
- Lifecycle rule: current-browser logout, global/security revocation and account deletion remain distinct; deletion/revocation is reconciled across required domains and never implies physical DNS/profile removal without separate proof.
- Failure rule: provider or ownership-datastore failure grants no account authority and cannot disable the independently healthy accountless core; ambiguous consequential mutations reconcile before retry/success.
- Privacy rule: security events are operational/security-only, contain no raw tokens/cookies/email/DNS history, and durable collection is blocked until exact necessary bounded retention/deletion is defined under TSK-0230.
- **ACC-0353 = PASS. VER-0353 = PASS. EVD-0353 = SATISFIED.**
- **Non-inference:** this is L4 NFR-definition PASS only; it does not activate Firebase/Google, implement accounts/sessions/datastore/AdGuard integration, authorize real-user processing, create legal compliance, pass a lifecycle gate, publish, activate a market, launch or infer successor PASS.

### Queue status after current TSK-0353 acceptance

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
"""

candidate = base + append
assert mask_updated(candidate) == mask_updated(old) + append
print("TSK0353_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
runtime_path.write_text(candidate, encoding="utf-8")
written = runtime_path.read_text(encoding="utf-8")
assert HEADING in written
for value in ["3cb7c248b6d121e1c8d9db47accdf639998edc93", "a87a0fa9e3fbf227869d7ef81f68c1828d7944bb", "33589319072 / 100119889794", "ACC-0353 = PASS. VER-0353 = PASS. EVD-0353 = SATISFIED."]:
    assert value in written, value
print("TSK0353_STATE_CANDIDATE=PASS")
print("TSK0353_STATE_RECONCILIATION=PASS")
