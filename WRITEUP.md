# AI Operating System Writeup

## Bottom Line

This project packages a privacy-safe, local-first AI Operating System template. The unique move is combining a compiled LLM-maintained wiki with an explicit operating layer: agent instructions, source lifecycle, decision records, work/personal variants, local query tooling, and privacy gates.

## Inspiration

The template is inspired by two public patterns:

- Andrej Karpathy's LLM Wiki gist: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Nate Jones' Open Brain / OB1 project: <https://github.com/NateBJones-Projects/OB1>

Karpathy's pattern frames the wiki as a compounding Markdown artifact between raw sources and the user. OB1 frames memory as infrastructure that multiple AI tools can use. This template takes a narrower path: a local file workspace that an agent can operate safely without requiring hosted memory infrastructure.

## Unique Aspects

### 1. The Wiki Is A Compiled Operating Layer

Raw source folders are not the product. The useful layer is the maintained wiki: source summaries, concept pages, decisions, reviews, and operating records. That keeps future agents from re-deriving context from scratch on every question.

### 2. Agents Get A Load Order

The generated `AGENTS.md` tells agents what to read first and what rules win on conflict. This makes the workspace more predictable than a normal folder of notes.

### 3. Work And Personal Are Separate Templates

Work and personal systems have different privacy risks and operating cadences. The package creates two variants instead of pretending one page taxonomy fits both.

### 4. Raw Folders Ship As Guidance, Not Content

The public template does not include real raw documents. Raw folders contain README files explaining what could go there, what tradeoffs to consider, and what to summarize into the wiki.

### 5. Privacy Is A Release Gate

The generated `checks/offline_check.sh` scans for local paths, common private identifiers, and organization/project-style leakage. It is not a perfect DLP tool, but it makes privacy review part of the normal workflow.

### 6. The Index Is Rebuildable

`tools/scripts/wiki_index.py` builds a local SQLite index from Markdown. The database is derived state, not canonical state. The canonical material remains portable Markdown.

### 7. It Is Small Enough To Understand

The package avoids hosted services, vector databases, cloud APIs, and large dependency trees. That makes it easier to inspect, fork, and adapt.

## How It Compares

| System | What It Optimizes For | This Template's Difference |
|---|---|---|
| Karpathy LLM Wiki | LLM-maintained Markdown knowledge base | Adds npm scaffolding, two variants, privacy gates, and local checks |
| Open Brain / OB1 | AI memory infrastructure across tools | Keeps the canonical layer as files and does not require a hosted database or gateway |
| NotebookLM | Source-grounded notebook analysis and generated artifacts | Keeps source lifecycle, rules, and decisions in editable local Markdown |
| Obsidian | Durable local notes and links | Adds agent-specific operating rules and repeatable ingest/query/check workflows |
| Mem | AI-assisted notes, document understanding, search, and chat | Keeps the workspace portable and vendor-neutral |

## What To Keep Private

Do not publish real brain/profile files, personal facts, employer details, client/customer details, project history, local paths, raw documents, private source summaries, screenshots, IDs, financial data, health data, or credentials.

Use the public package as a scaffold. Use private clones for real life and work context.

## Source Notes

- Karpathy's gist describes a persistent Markdown wiki built and maintained by an LLM from raw sources, with index/log files and Obsidian as a useful interface.
- OB1 describes an open memory infrastructure layer for AI tools.
- NotebookLM official help documents source import, source-grounded chat, summaries, Drive sync, URL import limits, and audio import behavior.
- Obsidian official docs describe local links and Canvas as durable files.
- Mem's help center describes PDF/image understanding, search, and chat over uploaded files.

## Research References

- Karpathy LLM Wiki: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Open Brain / OB1: <https://github.com/NateBJones-Projects/OB1>
- NotebookLM source import help: <https://support.google.com/notebooklm/answer/16215270>
- Obsidian Canvas help: <https://obsidian.md/help/plugins/canvas>
- Obsidian internal links help: <https://obsidian.md/help/links>
- Mem PDF and image understanding help: <https://help.mem.ai/features/pdf-and-image-understanding>
