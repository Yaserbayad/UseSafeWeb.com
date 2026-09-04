#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / '.github' / 'workflows'

RULES = [
    ('CONTENTS_WRITE', re.compile(r'^\s*contents\s*:\s*write\s*(?:#.*)?$', re.I)),
    ('WRITE_ALL', re.compile(r'^\s*(?:permissions\s*:\s*)?write-all\s*(?:#.*)?$', re.I)),
    ('PERSIST_CREDENTIALS_TRUE', re.compile(r'^\s*persist-credentials\s*:\s*true\s*(?:#.*)?$', re.I)),
    ('PULL_REQUEST_TARGET', re.compile(r'^\s*pull_request_target\s*:\s*(?:#.*)?$', re.I)),
    ('DIRECT_MAIN_PUSH', re.compile(r'\bgit\s+push\b[^\n#]*\b(?:refs/heads/)?main\b', re.I)),
    ('GH_PR_MERGE', re.compile(r'\bgh\s+pr\s+merge\b', re.I)),
    ('GH_WRITE_API', re.compile(r'\bgh\s+api\b[^\n#]*(?:-X|--method)\s+(?:POST|PUT|PATCH|DELETE)\b[^\n#]*(?:/contents\b|/merges\b|/git/refs\b)', re.I)),
    ('CURL_WRITE_API', re.compile(r'\bcurl\b[^\n#]*(?:-X|--request)\s*(?:POST|PUT|PATCH|DELETE)\b[^\n#]*(?:/contents\b|/merges\b|/git/refs\b)', re.I)),
]

violations = []
paths = sorted([*WORKFLOWS.glob('*.yml'), *WORKFLOWS.glob('*.yaml')])
for path in paths:
    rel = path.relative_to(ROOT)
    for lineno, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        stripped = raw.lstrip()
        if not stripped or stripped.startswith('#'):
            continue
        for code, pattern in RULES:
            if pattern.search(raw):
                violations.append((str(rel), lineno, code, raw.strip()))

if violations:
    print('TSK0489_WORKFLOW_GOVERNANCE=FAIL')
    for rel, lineno, code, text in violations:
        print(f'TSK0489_WORKFLOW_VIOLATION={rel}:{lineno}:{code}:{text}')
    sys.exit(1)

print('TSK0489_WORKFLOW_GOVERNANCE=PASS')
print(f'TSK0489_WORKFLOW_COUNT={len(paths)}')
