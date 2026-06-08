# AI Operating System Quickstart

A private, local-first workspace for AI-assisted work and personal planning.

## Why This Exists

Most AI sessions lose context because source files, decisions, notes, and follow-up work live in different places. This package creates one Markdown workspace with clear rules for humans and AI tools.

The public template is safe by default. It ships placeholders and folder guidance, not real source files, personal details, company history, or private project examples.

## How It Works

- Source material stays in `raw/`.
- Summaries, decisions, and reusable ideas live in `wiki/`.
- `AGENTS.md` tells AI tools what to read first and how to use the workspace.
- The work and personal templates use different page types and privacy rules.
- A small SQLite index makes Markdown pages easier to query.
- Local checks scan for private paths and common sensitive markers before sharing.

## Start A Workspace

Create a personal workspace with the `create-ai-operating-system` package:

```bash
npx create-ai-operating-system my-aos --personal
cd my-aos
```

Or create a work workspace:

```bash
npx create-ai-operating-system work-aos --work
cd work-aos
```

Read the rules, then build the index:

```bash
sed -n '1,120p' AGENTS.md
python3 tools/scripts/wiki_index.py rebuild
./tools/scripts/llmwiki status
```

## Templates

| Template | Best for | Core pages |
|---|---|---|
| `work` | Projects, meetings, decisions, research, stakeholder context, operating reviews | Project page, decision log, meeting synthesis, project plan |
| `personal` | Goals, learning, routines, personal decisions, reviews, private research | Personal operating model, weekly review, learning plan, decision log |

Both templates use mock descriptions and placeholders. They do not ship personal content, company names, project history, local install paths, raw PDFs, or private source summaries.

## Use The Workspace

1. Read the operating files:

   ```bash
   sed -n '1,160p' AGENTS.md
   sed -n '1,160p' brain/rules.md
   sed -n '1,160p' _system/OPERATING_MODEL.md
   ```

2. Add real source material only in a private copy. Start with `raw/ingest/` or the relevant raw folder.

3. Create or update a source summary in `wiki/sources/`. The summary should capture what the source says, why it matters, key decisions, open questions, and links to related pages.

4. Move reusable ideas into `wiki/concepts/`. Record project or personal execution in the variant folder: `wiki/work/` for work, `wiki/life/` for personal.

5. Rebuild search:

   ```bash
   python3 tools/scripts/wiki_index.py rebuild
   ```

6. Query the workspace:

   ```bash
   ./tools/scripts/llmwiki search "decision log"
   ```

7. Run checks before sharing:

   ```bash
   ./checks/offline_check.sh
   ```

See [GUIDE.md](GUIDE.md) for the longer walkthrough.

## Files Created

- `AGENTS.md` tells AI tools what to read first.
- `brain/rules.md` and `brain/voice.md` define update rules and writing style.
- `_system/` holds the operating model, taxonomy, index, and log.
- `raw/` contains README placeholders instead of real source files.
- `wiki/` contains source summaries, reusable ideas, and work/personal records.
- `tools/scripts/wiki_index.py` builds local search.
- `tools/scripts/llmwiki` provides read-only search.
- `checks/` runs smoke tests and privacy checks.

## Privacy

The public package is intentionally generic.

Do not publish:

- Employer, client, customer, partner, personnel, project, or deal details.
- Local machine paths.
- Private raw documents.
- Source summaries copied from your private workspace.
- Emails, phone numbers, addresses, identity documents, financial account data, health details, API keys, tokens, or screenshots.

Use real content only in a private clone.

## Credits

Built with inspiration from:

- Andrej Karpathy's LLM Wiki idea file: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Nate Jones' Open Brain / OB1 project: <https://github.com/NateBJones-Projects/OB1>

## Local Development

```bash
npm test
npm run smoke
npm pack --dry-run
node bin/create-ai-operating-system.js .tmp/demo --work --force
```

## License

Apache-2.0
