#!/usr/bin/env python3
from pathlib import Path
import subprocess

BASE = "d941ccf5ede60878d355c3b6395c9c689f75cf44"
source_path = Path(".github/scripts/tmp-cr0013-apply.py")
src = source_path.read_text(encoding="utf-8")

old_guard = '''    if sh("git", "rev-parse", "HEAD^", capture=True) != BASE_SHA:
        # The staging trigger commit must be exactly one commit above the authoritative base.
        head_parent = sh("git", "rev-parse", "HEAD^", capture=True)
        if head_parent != BASE_SHA:
            raise SystemExit(f"Unexpected staging ancestry: parent={head_parent} expected={BASE_SHA}")
'''
new_guard = '''    actual_head = sh("git", "rev-parse", "HEAD", capture=True)
    if actual_head != BASE_SHA:
        raise SystemExit(f"Unexpected source base: head={actual_head} expected={BASE_SHA}")
'''
if src.count(old_guard) != 1:
    raise SystemExit("Expected apply_source ancestry guard not found exactly once")
src = src.replace(old_guard, new_guard, 1)

for old, new in [
    ("TEMP_WORKFLOW.unlink(missing_ok=False)", "TEMP_WORKFLOW.unlink(missing_ok=True)"),
    ("TEMP_SCRIPT.unlink(missing_ok=False)", "TEMP_SCRIPT.unlink(missing_ok=True)"),
]:
    if src.count(old) != 1:
        raise SystemExit(f"Expected temp cleanup call not found exactly once: {old}")
    src = src.replace(old, new, 1)

out = Path("/tmp/cr0013-apply.py")
out.write_text(src, encoding="utf-8")
subprocess.run(["git", "checkout", "--detach", BASE], check=True)
subprocess.run(["python3", str(out), "apply"], check=True)
