# create-ai-operating-system

Scaffold a local-first AI Operating System for either work or personal use.

An AI Operating System is a structured Markdown workspace for capture, summaries, recall, decisions, and execution. It gives AI tools clear rules, organized files, local search, and privacy checks.

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

## What Makes It Special

- It creates two starting points: one for work and one for personal use.
- It gives AI tools a clear reading order through `AGENTS.md`.
- It separates source files from the summaries and decisions written into `wiki/`.
- It ships placeholder raw folders instead of real source examples.
- It includes local search through a rebuildable SQLite index.
- It includes privacy checks before sharing.
- It keeps the main workspace in Markdown so it stays easy to inspect and edit.
- It keeps work and personal material separate because they have different privacy risks and review habits.

## Privacy Model

The public package is intentionally generic.

Do not publish:

- Employer, client, customer, partner, personnel, project, or deal details.
- Local machine paths.
- Private raw documents.
- Source summaries copied from your private workspace.
- Emails, phone numbers, addresses, identity documents, financial account data, health details, API keys, tokens, or screenshots.

Use real content only in a private clone.

## Credits

This project was built with inspiration from:

- Andrej Karpathy's LLM Wiki idea file: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Nate Jones' Open Brain / OB1 project: <https://github.com/NateBJones-Projects/OB1>

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
