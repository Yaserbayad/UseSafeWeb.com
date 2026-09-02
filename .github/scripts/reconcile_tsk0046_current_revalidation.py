from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME = "b0e320a862eaf83b3fea11e565b42621608578eb"
EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "TSK_0046_POST_CR0008_DUAL_MODE_PERFORMANCE_CAPACITY_NFR_REVALIDATION_2026-09-02.md": "8e72d542b68de6f7f5c8c375b63b6229c6d15529",
    "TSK_0046_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "0d01804887723c76edc2a8426dfa00585944b84b",
    "TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "3ba04601ea5574fcd1fb1f58f95922ae94b74ac2",
}
NEW_HEADING = "## TSK-0046 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE PERFORMANCE/CAPACITY NFR REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def current_sections(text: str) -> list[str]:
    return [m.group(0) for m in re.finditer(r"^## TSK-\d{4} current accepted stable state.*?(?=^## |\Z)", text, re.M | re.S)]


for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f"hash mismatch {path}: {actual} != {expected}")

state_path = Path("CURRENT_STATE.md")
state = state_path.read_text(encoding="utf-8")

if NEW_HEADING in state:
    m = re.search(r"^" + re.escape(NEW_HEADING) + r".*?(?=^## |\Z)", state, re.M | re.S)
    if not m:
        raise SystemExit("ambiguous existing TSK-0046 current section")
    existing = m.group(0)
    required = [
        "**PASS**",
        "TSK_0046_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md",
        "33581514882 / 100096620942",
        "`AUTO_ALLOWED`",
    ]
    if all(token in existing for token in required):
        print("TSK0046_CURRENT_STATE_ALREADY_APPLIED=PASS")
        raise SystemExit(0)
    raise SystemExit("existing TSK-0046 section does not match accepted proof")

if blob("CURRENT_STATE.md") != PRE_RUNTIME:
    raise SystemExit("pre-runtime blob mismatch; refuse stale write")
if not state.endswith("\n"):
    raise SystemExit("CURRENT_STATE.md must end with newline")

before_sections = current_sections(state)
if not before_sections:
    raise SystemExit("no current accepted-state sections found")

# Required currently protected boundaries must be present before mutation.
for task_id in ["TSK-0299", "TSK-0485", "TSK-0318", "TSK-0319", "TSK-0301", "TSK-0316", "TSK-0300", "TSK-0317", "TSK-0310", "TSK-0484", "TSK-0538"]:
    if not any(section.startswith(f"## {task_id} current accepted stable state") for section in before_sections):
        raise SystemExit(f"required protected current section missing: {task_id}")

evidence = Path("TSK_0046_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for token in [
    "**ACC-0046 = PASS.**",
    "**VER-0046 = PASS.**",
    "**EVD-0046 = SATISFIED.**",
    "33581514882 / 100096620942",
    "TSK0046_CURRENT_REVALIDATION=PASS",
]:
    if token not in evidence:
        raise SystemExit(f"evidence token missing: {token}")

append = r'''## TSK-0046 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE PERFORMANCE/CAPACITY NFR REVALIDATION

`TSK-0046 — Define performance and capacity NFRs`: **PASS** under current `ACC-0046 / VER-0046 / EVD-0046`, current direct predecessor TSK-0538, `DEC-0053/CR-0006` dual-mode Version-1 scope and `DEC-0054/CR-0007` production-only lifecycle semantics.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0538`.
- Current artifact `TSK_0046_POST_CR0008_DUAL_MODE_PERFORMANCE_CAPACITY_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `8e72d542b68de6f7f5c8c375b63b6229c6d15529`, publication commit `0fbc382c94850fb02376c6f3105a1ea499fa7398`.
- Current durable evidence `TSK_0046_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `0d01804887723c76edc2a8426dfa00585944b84b`, publication commit `be64170b8d542936ff7b38ff752cfffb889e4132`.
- Independent read-only VER-0046 final verifier script blob `340ed4864cf6c63f8c163bb5852a9f16f7de4aa3`, workflow blob `22707f3ee628c2421a5707fdc7ec09b365309d98`; run/job `33581514882 / 100096620942`: **SUCCESS** with `contents: read`.
- Earlier v1/v2 verifier runs `33581329346 / 100096056039` and `33581430881 / 100096368646` are diagnostic-only prose-predicate failures; neither mutated governed state or changed the accepted artifact.
- Historical TSK-0046 proof remains valid for the 2× capacity margin, controlled synthetic DoH/DoT/TLS/filter correctness methodology, p50/p95/p99 evidence, security/privacy/rate-limit invariants, degradation behavior and early capacity-review triggers. Historical CR-0003/separate-pilot sequencing is superseded.
- The inherited WBS phrase `expected pilot load` now maps to the bounded first live-production validation/ramp envelope after LG-09 and all actually applicable prerequisites. Current real-user load before LG-09 is zero; no future cohort/adoption/query-volume number is fabricated.
- DNS, accountless-web and optional-account/session/dashboard/device load models are distinct. Optional account/provider/datastore failure must not block or be misreported as failure of a healthy accountless core.
- Current TSK-0538 provisional internal service targets are preserved. Capacity tests must retain DNS/accountless correctness, authorization, session/ownership isolation, privacy, reconciliation and protection-state truthfulness; no throughput result may be obtained by weakening a hard control.
- Current first-party web.dev review on 2026-09-02 retains Core Web Vitals good thresholds LCP <=2.5s, INP <=200ms and CLS <=0.1 at p75; soft-navigation evidence is bound to exact browser/navigation semantics and synthetic/lab evidence is not mislabeled as field compliance.
- **Non-inference:** L4 NFR-definition PASS only. No real-user/load authorization, production stress test, infrastructure resize/HA/new paid monitoring, web/app/auth implementation, provider/datastore architecture, legal/privacy completion, participant/publication/payment/market/launch, gate or successor PASS is inferred.

### Queue status after current TSK-0046 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific change/reopen semantics, gates and Action Authority. Preserve valid non-uniform historical PASS records where current evidence still proves unchanged acceptance.
'''

stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
base, count = re.subn(r"^\*\*Updated:\*\* .+$", "**Updated:** " + stamp, state, count=1, flags=re.M)
if count != 1:
    raise SystemExit("Updated header replacement failed")
result = base + append

after_sections = current_sections(result)
if len(after_sections) != len(before_sections) + 1:
    raise SystemExit("current accepted-state section count changed unexpectedly")
for section in before_sections:
    if section not in after_sections:
        raise SystemExit("an existing current accepted-state section changed")
if sum(1 for section in after_sections if section.startswith(NEW_HEADING)) != 1:
    raise SystemExit("new TSK-0046 current section count invalid")

state_path.write_text(result, encoding="utf-8")
check = state_path.read_text(encoding="utf-8")
check_sections = current_sections(check)
for section in before_sections:
    if section not in check_sections:
        raise SystemExit("post-write existing current accepted-state section changed")

print(f"PROTECTED_CURRENT_SECTION_COUNT={len(before_sections)}")
print("ALL_EXISTING_CURRENT_ACCEPTED_SECTIONS_PRESERVED=PASS")
print("TSK0046_CURRENT_STATE_RECONCILIATION=PASS")
