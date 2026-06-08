# Personal AI Operating System

This workspace is a local-first operating system for personal goals, learning, routines, decisions, and durable self-reflection.

## Start

```bash
python3 tools/scripts/wiki_index.py rebuild
./tools/scripts/llmwiki status
./tools/scripts/llmwiki search "personal decision"
```

## Personal Loop

1. Capture raw notes, links, and documents in `raw/ingest/` or a relevant personal raw folder.
2. Summarize reusable source material into `wiki/sources/`.
3. Convert durable lessons into `wiki/concepts/`.
4. Record goals, routines, learning plans, or personal decisions in `wiki/life/`.
5. Use `wiki/templates/` for weekly reviews, learning plans, and decision records.
6. Rebuild the local index before recall-heavy work.

## Folder Map

| Folder | Use |
|---|---|
| `raw/personal/` | Private personal notes and records |
| `raw/learning/` | Courses, books, articles, practice logs |
| `raw/finance/` | Budget or planning notes; do not commit real account data |
| `raw/health/` | Health or habit notes; keep private |
| `wiki/life/` | Goals, routines, decisions, plans, and reviews |

## Privacy

This template uses generic examples only. Do not publish private journals, family details, addresses, phone numbers, health information, financial records, account numbers, identity documents, or unredacted screenshots.
