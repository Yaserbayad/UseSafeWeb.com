#!/usr/bin/env bash
set -euo pipefail

echo "HOME=$HOME"
echo "RUNNER_TOOL_CACHE=${RUNNER_TOOL_CACHE:-}"
echo "RUNNER_TEMP=${RUNNER_TEMP:-}"
echo "PATH=$PATH"

echo '---NODE_CANDIDATES---'
find /home/azureusr/t/actions-runner/externals /home/azureusr/.nvm /usr/local /opt -type f -name node -perm -u+x 2>/dev/null | head -n 30 || true

echo '---PLAYWRIGHT_PACKAGE_CANDIDATES---'
find /home/azureusr /opt /usr/local -type f -path '*/node_modules/playwright/package.json' 2>/dev/null | head -n 30 || true

echo '---PLAYWRIGHT_CORE_CANDIDATES---'
find /home/azureusr /opt /usr/local -type f -path '*/node_modules/playwright-core/package.json' 2>/dev/null | head -n 30 || true

echo '---PYTHON_PLAYWRIGHT---'
python3 - <<'PY'
try:
 import playwright
 print('PYTHON_PLAYWRIGHT=YES', getattr(playwright,'__file__',None))
except Exception as e:
 print('PYTHON_PLAYWRIGHT=NO', type(e).__name__, str(e))
PY

echo 'TSK0332_BROWSER_RUNTIME_INSPECTION=PASS'
