#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / '.github' / 'workflows'
DIRECT_RULES = [
    ('WRITE_ALL', re.compile(r'^\s*(?:permissions\s*:\s*)?write-all\s*(?:#.*)?$', re.I)),
    ('PULL_REQUEST_TARGET', re.compile(r'^\s*pull_request_target\s*:\s*(?:#.*)?$', re.I)),
    ('DIRECT_MAIN_PUSH', re.compile(r'\bgit\s+push\b[^\n#]*\b(?:refs/heads/)?main\b', re.I)),
    ('GH_PR_MERGE', re.compile(r'\bgh\s+pr\s+merge\b', re.I)),
    ('GH_WRITE_API', re.compile(r'\bgh\s+api\b[^\n#]*(?:-X|--method)\s+(?:POST|PUT|PATCH|DELETE)\b[^\n#]*(?:/contents\b|/merges\b|/git/refs\b)', re.I)),
    ('CURL_WRITE_API', re.compile(r'\bcurl\b[^\n#]*(?:-X|--request)\s*(?:POST|PUT|PATCH|DELETE)\b[^\n#]*(?:/contents\b|/merges\b|/git/refs\b)', re.I)),
]
CONTENTS_WRITE = re.compile(r'^\s*contents\s*:\s*write\s*(?:#.*)?$', re.I)
CHECKOUT = re.compile(r'\buses\s*:\s*actions/checkout@', re.I)
PERSIST_FALSE = re.compile(r'^\s*persist-credentials\s*:\s*false\s*(?:#.*)?$', re.I)
GIT_PUSH = re.compile(r'\bgit\s+push\b', re.I)
SCRIPT_REF = re.compile(r'(?<![A-Za-z0-9_.-])((?:\./)?(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.(?:sh|py|js|mjs|cjs|ts))\b')
LOCAL_USES = re.compile(r'^\s*(?:-\s*)?uses\s*:\s*(\./[^\s#]+)', re.I)

violations = []
write_surfaces = []
reachable = set()
paths = sorted([*WORKFLOWS.glob('*.yml'), *WORKFLOWS.glob('*.yaml')])


def executable_refs(lines):
    refs = set()
    for raw in lines:
        stripped = raw.lstrip()
        if not stripped or stripped.startswith('#'):
            continue
        for ref in SCRIPT_REF.findall(raw):
            refs.add(ref.removeprefix('./'))
        local = LOCAL_USES.search(raw)
        if local:
            ref = local.group(1).removeprefix('./').rstrip('/')
            candidate = ROOT / ref
            if candidate.is_dir():
                for name in ('action.yml', 'action.yaml'):
                    action = candidate / name
                    if action.is_file():
                        refs.add(str(action.relative_to(ROOT)))
                        break
            elif candidate.is_file():
                refs.add(ref)
    return refs


def scan_reachable(rel, write_capable, seen):
    if rel in seen:
        return
    seen.add(rel)
    path = ROOT / rel
    if not path.is_file():
        return
    reachable.add(rel)
    lines = path.read_text(encoding='utf-8').splitlines()
    for lineno, raw in enumerate(lines, 1):
        stripped = raw.lstrip()
        if not stripped or stripped.startswith('#'):
            continue
        if write_capable and GIT_PUSH.search(raw):
            violations.append((rel, lineno, 'WRITE_WORKFLOW_GIT_PUSH', raw.strip()))
        for code, pattern in DIRECT_RULES:
            if pattern.search(raw):
                violations.append((rel, lineno, code, raw.strip()))
    for child in executable_refs(lines):
        scan_reachable(child, write_capable, seen)


for path in paths:
    lines = path.read_text(encoding='utf-8').splitlines()
    rel = str(path.relative_to(ROOT))
    active_lines = [line for line in lines if line.strip() and not line.lstrip().startswith('#')]
    has_write = any(CONTENTS_WRITE.search(line) for line in active_lines)
    if has_write:
        write_surfaces.append(rel)
        if any(CHECKOUT.search(line) for line in active_lines) and not any(PERSIST_FALSE.search(line) for line in active_lines):
            violations.append((rel, 1, 'WRITE_CAPABLE_CHECKOUT_CREDENTIALS_NOT_DISABLED', 'actions/checkout requires persist-credentials: false'))
    for lineno, raw in enumerate(lines, 1):
        stripped = raw.lstrip()
        if not stripped or stripped.startswith('#'):
            continue
        for code, pattern in DIRECT_RULES:
            if pattern.search(raw):
                violations.append((rel, lineno, code, raw.strip()))
    seen = set()
    for child in executable_refs(lines):
        scan_reachable(child, has_write, seen)

for rel in write_surfaces:
    print(f'TSK0489_WORKFLOW_WRITE_SURFACE={rel}')
if violations:
    print('TSK0489_WORKFLOW_GOVERNANCE=FAIL')
    for rel, lineno, code, text in sorted(set(violations)):
        print(f'TSK0489_WORKFLOW_VIOLATION={rel}:{lineno}:{code}:{text}')
    sys.exit(1)

print('TSK0489_WORKFLOW_GOVERNANCE=PASS')
print(f'TSK0489_WORKFLOW_COUNT={len(paths)}')
print(f'TSK0489_WRITE_SURFACE_COUNT={len(write_surfaces)}')
print(f'TSK0489_REACHABLE_EXECUTABLE_COUNT={len(reachable)}')
