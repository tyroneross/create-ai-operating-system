# Personal AI Operating System

A private, local-first workspace for goals, learning, routines, decisions, and personal reviews.

## How it works

This workspace gives personal context a clear file structure. Source material stays in `raw/`. Summaries, decisions, and reusable ideas live in `wiki/`. AI tools start with `AGENTS.md` so they know what to read first.

## Why keep it

- Keep goals, learning, and decisions in one system.
- Preserve source material without mixing it into summaries.
- Make weekly review and recall easier.
- Keep private personal context out of the public template.

## Start

```bash
python3 tools/scripts/wiki_index.py rebuild
./tools/scripts/llmwiki status
./tools/scripts/llmwiki search "personal decision"
```

## Personal loop

1. Capture raw notes, links, and documents in `raw/ingest/` or a relevant personal raw folder.
2. Summarize reusable source material into `wiki/sources/`.
3. Convert durable lessons into `wiki/concepts/`.
4. Record goals, routines, learning plans, or personal decisions in `wiki/life/`.
5. Use `wiki/templates/` for weekly reviews, learning plans, and decision records.
6. Rebuild the local index before recall-heavy work.

## Folder map

| Folder | Use |
|---|---|
| `raw/personal/` | Private personal notes and records |
| `raw/learning/` | Courses, books, articles, practice logs |
| `raw/finance/` | Budget or planning notes; do not commit real account data |
| `raw/health/` | Health or habit notes; keep private |
| `wiki/life/` | Goals, routines, decisions, plans, and reviews |

## Privacy

This template uses generic examples only. Do not publish private journals, family details, addresses, phone numbers, health information, financial records, account numbers, identity documents, or unredacted screenshots.
