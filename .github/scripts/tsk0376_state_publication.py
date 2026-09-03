#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path

BASE_COMMIT = "ce48a5f5fd754e95775a7fab571dba1b2d65ee81"
PRE_STATE_BLOB = "7e8230993f5a3fa487857754d095a8f9598b36b5"
EVIDENCE_PATH = Path("TSK_0376_ACCOUNTLESS_STATE_MACHINE_ACCEPTANCE_2026-09-03.md")
STATE_PATH = Path("CURRENT_STATE.md")
RESULT_TEXT = "PASS — ACC-0376 fully evidenced; runtime publication guard passed."
HEADING = "## TSK-0376 current accepted stable state — PASS (2026-09-03)"
TIMESTAMP_RE = re.compile(rb"\*\*Updated:\*\* ([^\n]+)\n")
ISO_RE = re.compile(r"^2026-09-03T\d{2}:\d{2}:\d{2}Z$")


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read_base_state() -> bytes:
    return subprocess.check_output(["git", "show", f"{BASE_COMMIT}:CURRENT_STATE.md"])


def normalized_timestamp(data: bytes) -> tuple[bytes, str]:
    matches = list(TIMESTAMP_RE.finditer(data))
    if len(matches) != 1:
        raise AssertionError("CURRENT_STATE.md must contain exactly one Updated timestamp")
    match = matches[0]
    stamp = match.group(1).decode("utf-8")
    normalized = data[: match.start()] + b"**Updated:** <STAMP>\n" + data[match.end() :]
    return normalized, stamp


def parse_final_evidence() -> tuple[str, str, str]:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    if any(token in text for token in ("__RESULT__", "__SYNC_RUN_ID__", "__SYNC_TIMESTAMP__")):
        raise AssertionError("unresolved evidence placeholder")
    if f"**Result:** {RESULT_TEXT}" not in text:
        raise AssertionError("final PASS result missing from EVD-0376")
    run_match = re.search(r"Publication guard run: `([0-9]+)`\.", text)
    time_match = re.search(r"Publication timestamp: `([^`]+)`\.", text)
    if not run_match or not time_match:
        raise AssertionError("publication run/timestamp missing from EVD-0376")
    run_id = run_match.group(1)
    timestamp = time_match.group(1)
    if not ISO_RE.fullmatch(timestamp):
        raise AssertionError("invalid publication timestamp")
    evidence_blob = git_blob_sha(EVIDENCE_PATH.read_bytes())
    return run_id, timestamp, evidence_blob


def render_section(run_id: str, evidence_blob: str) -> bytes:
    return f"""{HEADING}

- Runtime state: **PASS**.
- Acceptance authority: `ACC-0376` / `VER-0376` / `EVD-0376` — all state transitions defined/tested; illegal transitions rejected; parent-confirmed and technically verified evidence remain separate; resume/retry is deterministic and does not duplicate completed work.
- Canonical implementation: PR `#78`; accepted feature head `b423c0304354b22b3151e1660f3e06299ff11f0a`; canonical merge `ce48a5f5fd754e95775a7fab571dba1b2d65ee81`.
- Direct acceptance: feature run/job `33730514968` / `100569122644` **PASS**; clean-main run/job `33730835303` / `100570144399` **PASS**; focused contract 6/6 and complete current website contract suite 74/74.
- `EVD-0376`: `TSK_0376_ACCOUNTLESS_STATE_MACHINE_ACCEPTANCE_2026-09-03.md` @ blob `{evidence_blob}`.
- Guarded evidence/runtime publication: run `{run_id}` from exact pre-mutation `CURRENT_STATE.md` blob `{PRE_STATE_BLOB}`; only the top `Updated` timestamp and this appended TSK-0376 stable-state section are permitted runtime-state changes.
- Journey-0 remains accountless/session-scoped with fixed 24-hour hard expiry, exact-key validation, safe malformed/expired restart, bounded verification retry, and no retained browsing/query/domain/hostname/raw-DNS history.
- Preserved fences: no deployment, profile distribution, participant processing, runtime/market activation, or downstream lifecycle-gate activation is created or inferred by this PASS.

### Queue effect

- Current successors may consume TSK-0376 only after this exact evidence/runtime publication is merged to canonical `main` and independently read-back verified; no downstream task or gate PASS is inferred.
""".encode("utf-8")


def verify_base_state() -> bytes:
    current = STATE_PATH.read_bytes()
    if git_blob_sha(current) != PRE_STATE_BLOB:
        raise AssertionError("CURRENT_STATE.md is not the exact guarded pre-mutation blob")
    base = read_base_state()
    if git_blob_sha(base) != PRE_STATE_BLOB or current != base:
        raise AssertionError("guarded base does not match canonical implementation head")
    if b"## TSK-0376 current accepted stable state" in current:
        raise AssertionError("TSK-0376 runtime section already exists in guarded base")
    return current


def verify_draft() -> None:
    verify_base_state()
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    expected = {
        "__RESULT__": 1,
        "__SYNC_RUN_ID__": 1,
        "__SYNC_TIMESTAMP__": 1,
    }
    for token, count in expected.items():
        if text.count(token) != count:
            raise AssertionError(f"draft evidence placeholder {token} count is not {count}")
    for marker in ("ACC-0376", "VER-0376", "EVD-0376", "33730514968", "33730835303"):
        if marker not in text:
            raise AssertionError(f"required evidence marker missing: {marker}")


def verify_final() -> None:
    run_id, timestamp, evidence_blob = parse_final_evidence()
    base = read_base_state()
    if git_blob_sha(base) != PRE_STATE_BLOB:
        raise AssertionError("canonical base CURRENT_STATE blob drifted")
    current = STATE_PATH.read_bytes()
    base_normalized, _ = normalized_timestamp(base)
    current_normalized, current_timestamp = normalized_timestamp(current)
    if current_timestamp != timestamp:
        raise AssertionError("CURRENT_STATE timestamp does not match EVD publication timestamp")
    section = render_section(run_id, evidence_blob)
    separator = b"\n" if base.endswith(b"\n") else b"\n\n"
    expected = base_normalized + separator + section
    if current_normalized != expected:
        raise AssertionError("CURRENT_STATE contains changes outside Updated timestamp plus exact TSK-0376 append")
    if current.count(HEADING.encode("utf-8")) != 1:
        raise AssertionError("TSK-0376 runtime section multiplicity invalid")


def status() -> str:
    current_blob = git_blob_sha(STATE_PATH.read_bytes())
    if current_blob == PRE_STATE_BLOB:
        verify_draft()
        return "true"
    verify_final()
    return "false"


def sync(run_id: str, timestamp: str) -> None:
    if not run_id.isdigit():
        raise AssertionError("run id must be numeric")
    if not ISO_RE.fullmatch(timestamp):
        raise AssertionError("timestamp must be an exact UTC publication timestamp")
    base = verify_base_state()
    verify_draft()

    evidence = EVIDENCE_PATH.read_text(encoding="utf-8")
    evidence = evidence.replace("__RESULT__", RESULT_TEXT)
    evidence = evidence.replace("__SYNC_RUN_ID__", run_id)
    evidence = evidence.replace("__SYNC_TIMESTAMP__", timestamp)
    EVIDENCE_PATH.write_text(evidence, encoding="utf-8")
    evidence_blob = git_blob_sha(EVIDENCE_PATH.read_bytes())

    updated = TIMESTAMP_RE.sub(f"**Updated:** {timestamp}\n".encode("utf-8"), base, count=1)
    separator = b"\n" if updated.endswith(b"\n") else b"\n\n"
    STATE_PATH.write_bytes(updated + separator + render_section(run_id, evidence_blob))
    verify_final()


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("verify")
    sync_parser = sub.add_parser("sync")
    sync_parser.add_argument("--run-id", required=True)
    sync_parser.add_argument("--timestamp", required=True)
    args = parser.parse_args()

    if args.command == "status":
        print(status())
    elif args.command == "verify":
        verify_final()
        print("TSK0376_STATE_PUBLICATION_VERIFY=PASS")
    else:
        sync(args.run_id, args.timestamp)
        print("TSK0376_STATE_PUBLICATION_SYNC=PASS")


if __name__ == "__main__":
    main()
