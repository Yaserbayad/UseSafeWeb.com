#!/usr/bin/env python3
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / '.github' / 'workflows'
DST = ROOT / '.github' / 'workflow-archive' / 'tsk0489-ag009'
CONTENTS_WRITE = re.compile(r'^\s*contents\s*:\s*write\s*(?:#.*)?$', re.I)
PERSIST_TRUE = re.compile(r'^\s*persist-credentials\s*:\s*true\s*(?:#.*)?$', re.I)
DIRECT = [
    ('WRITE_ALL', re.compile(r'^\s*(?:permissions\s*:\s*)?write-all\s*(?:#.*)?$', re.I)),
    ('PULL_REQUEST_TARGET', re.compile(r'^\s*pull_request_target\s*:\s*(?:#.*)?$', re.I)),
    ('DIRECT_MAIN_PUSH', re.compile(r'\bgit\s+push\b[^\n#]*\b(?:refs/heads/)?main\b', re.I)),
    ('GH_PR_MERGE', re.compile(r'\bgh\s+pr\s+merge\b', re.I)),
    ('GH_WRITE_API', re.compile(r'\bgh\s+api\b[^\n#]*(?:-X|--method)\s+(?:POST|PUT|PATCH|DELETE)\b[^\n#]*(?:/contents\b|/merges\b|/git/refs\b)', re.I)),
    ('CURL_WRITE_API', re.compile(r'\bcurl\b[^\n#]*(?:-X|--request)\s*(?:POST|PUT|PATCH|DELETE)\b[^\n#]*(?:/contents\b|/merges\b|/git/refs\b)', re.I)),
]

archive = []
for path in sorted([*SRC.glob('*.yml'), *SRC.glob('*.yaml')]):
    lines = path.read_text(encoding='utf-8').splitlines()
    active = [line for line in lines if line.strip() and not line.lstrip().startswith('#')]
    has_write = any(CONTENTS_WRITE.search(line) for line in active)
    reasons = []
    if has_write and any(PERSIST_TRUE.search(line) for line in active):
        reasons.append('WRITE_CAPABLE_PERSISTED_CHECKOUT')
    for code, pattern in DIRECT:
        if any(pattern.search(line) for line in active):
            reasons.append(code)
    if reasons:
        archive.append((path, sorted(set(reasons))))

if not archive:
    print('TSK0489_ARCHIVE_RESULT=NOOP')
    raise SystemExit(0)

DST.mkdir(parents=True, exist_ok=True)
manifest = []
for path, reasons in archive:
    target = DST / path.name
    if target.exists():
        raise SystemExit(f'archive target exists: {target}')
    shutil.move(str(path), str(target))
    manifest.append(f'{path.relative_to(ROOT)} -> {target.relative_to(ROOT)} | {",".join(reasons)}')

(DST / 'ARCHIVED_WORKFLOWS.txt').write_text('\n'.join(manifest) + '\n', encoding='utf-8')
print(f'TSK0489_ARCHIVED_WORKFLOW_COUNT={len(archive)}')
for line in manifest:
    print(f'TSK0489_ARCHIVED_WORKFLOW={line}')
