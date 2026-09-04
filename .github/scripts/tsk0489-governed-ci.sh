#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

PROBE='.github/tsk0489-deliberate-failure.probe'
if [[ -e "$PROBE" ]]; then
  echo 'TSK0489_DELIBERATE_FAILURE=OBSERVED'
  echo 'TSK0489_PROMOTION_ELIGIBLE=NO'
  exit 86
fi

python3 - <<'PY'
import csv
from pathlib import Path

with open('Plans/Master/WBS/master-wbs.csv', newline='', encoding='utf-8-sig') as f:
    rows = [r for r in csv.DictReader(f) if r['Task_ID'] == 'TSK-0489']
assert len(rows) == 1
r = rows[0]
assert r['Dependencies'].strip() == 'TSK-0453; TSK-0491; TSK-0422'
assert (r['Acceptance_ID'], r['Verification_ID'], r['Evidence_ID']) == ('ACC-0489', 'VER-0489', 'EVD-0489')
assert (r['AI_Capability_A0_A4'], r['Action_Authority']) == ('A3', 'AUTO_ALLOWED')
assert r['Acceptance_Criteria'] == 'All approved checks execute on pull/change requests and main; failures block promotion; evidence is retained; test bypass requires recorded owner authority.'

graph = Path('Plans/Master/RELATIONSHIP_INDEX.yaml').read_text(encoding='utf-8')
start = graph.index('  TSK-0489:\n')
end = graph.index('\n  TSK-0490:', start)
block = graph[start:end]
for target, kind in [
    ('TSK-0453', 'depends_on'),
    ('TSK-0491', 'depends_on'),
    ('TSK-0422', 'depends_on'),
    ('ACC-0489', 'acceptance'),
    ('VER-0489', 'verified_by'),
    ('EVD-0489', 'evidence_required'),
    ('INT-0015', 'interface'),
]:
    assert f'- target: {target}\n      type: {kind}' in block

for path, needle in [
    ('Plans/Master/Registers/DECISIONS_TRIGGERS.md', 'DEC-0060'),
    ('Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md', 'CR-0013'),
    ('Plans/Master/Registers/CONSTRAINTS.md', 'CON-0028'),
    ('Plans/Master/Registers/INTERFACES.md', 'INT-0015'),
]:
    assert needle in Path(path).read_text(encoding='utf-8')
PY

echo 'TSK0489_AUTHORITY_BINDINGS=PASS'
python3 tests/repository-structure/verify_structure.py
python3 Plans/Master/Tools/validate_master_plan.py

echo 'TSK0489_GOVERNANCE_VALIDATION=PASS'

cd website
test "$(node --version)" = 'v22.23.2'
test "$(npm --version)" = '10.9.8'
test "$(cat .nvmrc)" = '22.23.2'
test "$(node -p "require('./package.json').packageManager")" = 'npm@10.9.8'
npm ci --ignore-scripts --no-fund --no-audit
NEXT_TELEMETRY_DISABLED=1 npm run validate
npm --silent run sbom > /tmp/tsk0489-sbom.spdx.json
node - <<'NODE'
const fs = require('node:fs');
const s = JSON.parse(fs.readFileSync('/tmp/tsk0489-sbom.spdx.json', 'utf8'));
if (s.spdxVersion !== 'SPDX-2.3') throw new Error('unexpected SPDX version');
if (!Array.isArray(s.packages) || s.packages.length < 1) throw new Error('empty SBOM');
NODE
npm audit --audit-level=high
npm audit --omit=dev --audit-level=high
cd "$ROOT"

echo 'TSK0489_LOCAL_CI_PARITY_ENTRYPOINT=npm run validate'
echo 'TSK0489_DEPENDENCY_SBOM_AUDIT=PASS'

security_verifier='infrastructure/adguard-server/tsk-0490-security-controls-verifier.sh'
bash -n "$security_verifier"
bash "$security_verifier" --synthetic | tee /tmp/tsk0489-security.txt
for marker in FULL_HISTORY_SECRET_SCAN=PASS EXTERNAL_SECRET_INJECTION=PASS SECRET_ROTATION_TEST=PASS SECRET_REVOCATION_TEST=PASS BREAK_GLASS_RECOVERY_TEST=PASS TEMP_SECRET_CLEANUP=PASS SYNTHETIC_ROLLBACK=PASS ACC_0490_SYNTHETIC=PASS; do
  grep -Fq "$marker" /tmp/tsk0489-security.txt
done

echo 'TSK0489_SECURITY_PRIVACY_GATE=PASS'

git diff --check
test -z "$(git status --porcelain=v1)"

echo 'TSK0489_CLEAN_TREE=PASS'
echo 'TSK0489_PROMOTION_ELIGIBLE=YES'
