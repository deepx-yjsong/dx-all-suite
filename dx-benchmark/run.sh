#!/usr/bin/env bash
# dx-benchmark launcher — runs the benchmark CLI from the suite.
# Usage: ./run.sh <preflight|dry-run|run|report|aggregate|dashboard> [args...]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

# Auto-detect suite root (dx-runtime/ + dx-compiler/ siblings).
SUITE_ROOT="$SCRIPT_DIR"
while [ "$SUITE_ROOT" != "/" ]; do
    if [ -d "$SUITE_ROOT/dx-runtime" ] && [ -d "$SUITE_ROOT/dx-compiler" ]; then
        break
    fi
    SUITE_ROOT="$(dirname "$SUITE_ROOT")"
done
if [ "$SUITE_ROOT" = "/" ]; then
    echo "ERROR: Cannot find dx-all-suite root (expected dx-runtime/ and dx-compiler/ siblings)" >&2
    exit 1
fi

# Activate the benchmark venv if setup.sh created one.
if [ -f "$SCRIPT_DIR/venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source "$SCRIPT_DIR/venv/bin/activate"
fi

cd "$SCRIPT_DIR"
exec python3 -m benchmark "$@"
