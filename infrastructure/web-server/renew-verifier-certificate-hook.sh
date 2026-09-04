#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# Intended as the deployment hook of externally authorized DNS-01 automation.
# It never reads or changes DNS-provider credentials itself.
exec "${SCRIPT_DIR}/install-verifier-config.sh"
