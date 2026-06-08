#!/usr/bin/env bash
set -euo pipefail

python3 tools/scripts/wiki_index.py rebuild
./tools/scripts/llmwiki status
./tools/scripts/llmwiki search "operating system" -k 3
./checks/offline_check.sh
