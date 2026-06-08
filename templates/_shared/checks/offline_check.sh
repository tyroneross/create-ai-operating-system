#!/usr/bin/env bash
set -euo pipefail

required=(
  "AGENTS.md"
  "README.md"
  "brain/rules.md"
  "brain/voice.md"
  "_system/OPERATING_MODEL.md"
  "_system/TAXONOMY.md"
  "_system/index.md"
  "tools/scripts/wiki_index.py"
  "tools/scripts/llmwiki"
)

for path in "${required[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "missing required file: $path" >&2
    exit 1
  fi
done

python3 tools/scripts/wiki_index.py status >/dev/null

leaks=$(rg -n --hidden --glob '!.git/**' --glob '!checks/offline_check.sh' --glob '!*.db' --glob '!*.sqlite' \
  '/Users/|WorkWiki|ObsidianVault|WorkLLMWiki|Desktop/LLM Wiki|Cisco|Csco|Akamai|IBM|Marine|OpenAI|Anthropic|Menlo|Fireworks|Strategic Initiatives|Product Operations|Business Innovator|Equity|MLT|Hyperscale|CSDI|Nvidia|ShearShare|tyroneross|Tyrone' . || true)

if [[ -n "$leaks" ]]; then
  echo "possible private/local content found:" >&2
  echo "$leaks" >&2
  exit 1
fi

echo "offline check passed"
