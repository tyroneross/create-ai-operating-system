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
  '(/[Uu]sers/[^[:space:]]+|/home/[^[:space:]]+|/Volumes/[^[:space:]]+|[A-Za-z]:\\[Uu]sers\\|PRIVATE_|PERSON_NAME|COMPANY_NAME|EMPLOYER_NAME|CLIENT_NAME|CUSTOMER_NAME|PROJECT_NAME|LOCAL_PATH|EMAIL_ADDRESS|PHONE_NUMBER|API_KEY|ACCESS_TOKEN|SECRET_KEY)' . || true)

if [[ -n "$leaks" ]]; then
  echo "possible private/local content found:" >&2
  echo "$leaks" >&2
  exit 1
fi

echo "offline check passed"
