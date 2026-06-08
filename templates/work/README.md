# Work AI Operating System

This workspace is a local-first operating system for professional knowledge work. It is designed for projects, meetings, decisions, research, customer context, and repeatable operating reviews.

## Start

```bash
python3 tools/scripts/wiki_index.py rebuild
./tools/scripts/llmwiki status
./tools/scripts/llmwiki search "project decision"
```

## Work Loop

1. Capture source material in `raw/ingest/` or the relevant work raw folder.
2. Summarize sources into `wiki/sources/`.
3. Convert durable ideas into `wiki/concepts/`.
4. Record execution in `wiki/work/`.
5. Use `wiki/templates/` for project plans, meeting synthesis, and decision logs.
6. Rebuild the local index before recall-heavy work.

## Folder Map

| Folder | Use |
|---|---|
| `raw/projects/` | Project briefs, plans, status exports, sanitized artifacts |
| `raw/meetings/` | Meeting notes, transcripts, agendas, follow-ups |
| `raw/customers/` | Customer or stakeholder material; sanitize before sharing |
| `raw/operations/` | Cadence, process, dashboards, retrospectives |
| `wiki/work/` | Project pages, decision logs, meeting synthesis, operating reviews |

## Privacy

This template uses generic examples only. In real work use, treat employer, client, customer, partner, deal, financial, and personnel data as private unless explicitly cleared for sharing.
