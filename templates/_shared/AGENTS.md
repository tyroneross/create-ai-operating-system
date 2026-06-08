# AI Operating System Agent Instructions

This repository is a local-first operating system for knowledge, decisions, and execution. Treat it as a structured workspace, not a document dump.

## Load Order

Read these files before changing the system:

1. `README.md` - template purpose and chosen variant.
2. `_system/OPERATING_MODEL.md` - how the workspace is intended to run.
3. `brain/rules.md` - lifecycle, privacy, and page rules.
4. `brain/voice.md` - writing and response norms.
5. `_system/index.md` - current catalog.
6. `_system/log.md` - chronological operating trail.

## Operating Rules

- Lead with the answer, then support it.
- Use the wiki before answering from memory when the question touches filed knowledge.
- Distinguish source fact, inference, and recommendation.
- Keep raw sources immutable. Write synthesis into `wiki/`.
- Do not put secrets, private identifiers, client/customer names, personal addresses, phone numbers, API keys, or credential material in tracked files.
- Use placeholders in reusable templates. Replace them only inside a private fork or local vault.
- Prefer simple local tooling before adding services or dependencies.

## Source Lifecycle

1. Drop files into `raw/ingest/`.
2. Create or update a source page in `wiki/sources/`.
3. Link durable ideas into `wiki/concepts/`.
4. Rebuild the index with `python3 tools/scripts/wiki_index.py rebuild`.
5. Query with `./tools/scripts/llmwiki search "<query>"`.
6. Append material operations to `_system/log.md`.

## Privacy Gate

Before committing, publishing, syncing, or sharing:

```bash
./checks/offline_check.sh
rg -n --hidden --glob '!.git/**' --glob '!*.db' --glob '!*.sqlite' 'REPLACE_ME|PRIVATE|SECRET|TOKEN|PASSWORD|API_KEY'
```

If the result contains real private data, remove or generalize it before sharing.
