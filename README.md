# create-ai-operating-system

Scaffold a local-first AI Operating System for either work or personal use.

An AI Operating System is a structured Markdown workspace for capture, synthesis, recall, decisions, and execution. It gives AI agents a durable operating layer: raw-source discipline, compiled wiki pages, agent rules, lifecycle logs, and local search.

## Create A Workspace

```bash
npx create-ai-operating-system my-aos --personal
cd my-aos
python3 tools/scripts/wiki_index.py rebuild
./tools/scripts/llmwiki status
```

Work template:

```bash
npx create-ai-operating-system work-aos --work
```

Personal template:

```bash
npx create-ai-operating-system personal-aos --personal
```

## What It Creates

- `AGENTS.md` for Codex, Claude Code, and other agentic coding tools.
- `brain/rules.md` and `brain/voice.md` as the behavior layer.
- `_system/OPERATING_MODEL.md`, `_system/TAXONOMY.md`, `_system/index.md`, and `_system/log.md`.
- `raw/` folders with README placeholders instead of real source files.
- `wiki/` pages for source summaries, durable concepts, and work/personal operating records.
- `tools/scripts/wiki_index.py` for local SQLite-backed Markdown indexing.
- `tools/scripts/llmwiki` as a read-only query wrapper.
- `checks/` scripts for smoke tests and privacy-oriented offline checks.

## Two Templates

| Template | Best for | Core pages |
|---|---|---|
| `work` | Projects, meetings, decisions, research, customer/stakeholder context, operating reviews | Project page, decision log, meeting synthesis, project plan |
| `personal` | Goals, learning, routines, personal decisions, reviews, private research | Personal operating model, weekly review, learning plan, decision log |

Both templates use mock descriptions and placeholders. They do not ship personal content, company names, project history, local install paths, raw PDFs, or private source summaries.

## Why This Is Different

This template sits between lightweight personal wikis and heavier AI memory infrastructure.

- **Compiled knowledge, not repeated retrieval.** It follows the LLM Wiki pattern: raw sources are preserved, but the useful working layer is a maintained Markdown wiki that compounds over time. See Andrej Karpathy's LLM Wiki gist: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>.
- **An operating layer, not just notes.** It adds load order, agent rules, lifecycle logs, privacy gates, page status, source summaries, and work/personal operating templates.
- **Local-first by default.** It creates plain files and a rebuildable local SQLite index. You can use Obsidian or any editor because the system is Markdown-first.
- **Two intentional variants.** Work and personal systems have different risks, page types, and cadences; the scaffolder keeps them separate.
- **Privacy is built into the template boundary.** Raw folders contain guidance files, not real source examples. The generated checks scan for local paths, employer/project-style identifiers, and obvious private markers before sharing.
- **Lighter than a hosted memory platform.** Open Brain/OB1 emphasizes shared memory infrastructure across AI tools. This template focuses on a portable file workspace an agent can operate directly. See OB1: <https://github.com/NateBJones-Projects/OB1>.

## Comparison

| Approach | Strength | Difference in this template |
|---|---|---|
| Karpathy LLM Wiki | Persistent Markdown wiki compiled by an LLM from raw sources | This package turns the pattern into a reusable work/personal scaffold with privacy gates and local checks |
| Open Brain / OB1 | Cross-tool AI memory infrastructure and open protocol | This is file-native and dependency-light; no database service, AI gateway, or hosted stack required |
| NotebookLM | Source-grounded notebook chat and generated study artifacts | This keeps the operating layer in editable local files with explicit lifecycle and agent rules |
| Obsidian | Durable local Markdown vault, internal links, graph/canvas workflows | This adds agent-operating instructions, source lifecycle, and CLI checks around a Markdown vault |
| Mem | AI notes, document understanding, search, and chat | This avoids vendor lock-in by keeping the canonical layer as local Markdown plus rebuildable indexes |

## Research References

- Karpathy LLM Wiki: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Open Brain / OB1: <https://github.com/NateBJones-Projects/OB1>
- NotebookLM source import help: <https://support.google.com/notebooklm/answer/16215270>
- Obsidian Canvas help: <https://obsidian.md/help/plugins/canvas>
- Obsidian internal links help: <https://obsidian.md/help/links>
- Mem PDF and image understanding help: <https://help.mem.ai/features/pdf-and-image-understanding>

## Privacy Model

The public package is intentionally generic.

Do not publish:

- Employer, client, customer, partner, personnel, project, or deal details.
- Local machine paths.
- Private raw documents.
- Source summaries copied from your private workspace.
- Emails, phone numbers, addresses, identity documents, financial account data, health details, API keys, tokens, or screenshots.

Use real content only in a private clone.

## Local Development

```bash
npm test
npm run smoke
npm pack --dry-run
node bin/create-ai-operating-system.js .tmp/demo --work --force
```

## Publishing

```bash
npm publish --access public
```

## License

Apache-2.0
