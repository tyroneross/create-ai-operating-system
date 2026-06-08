# AI Operating System Quickstart Writeup

Create a private, local-first workspace for AI-assisted work and personal planning.

The system gives AI tools a clear place to read from and write back to: source files in `raw/`, summaries and decisions in `wiki/`, rules in `AGENTS.md` and `brain/`, and local search in `tools/`. Public files stay generic. Real work and personal context belong in a private copy.

## Why It Matters

AI tools work better when context has a stable home. Chat history is hard to reuse. Loose files are hard to search. Private notes are risky to publish by accident.

This template gives the system a simple shape:

- Source material stays intact.
- Summaries and decisions are easy to find.
- AI tools get a clear reading order.
- Work and personal contexts stay separate.
- Privacy checks happen before sharing.

## How It Works

The package creates a Markdown workspace with:

- `AGENTS.md` for AI tool instructions.
- `brain/rules.md` for file, privacy, and update rules.
- `brain/voice.md` for writing style.
- `_system/` files for the operating model, taxonomy, index, and log.
- `raw/` folders for source material.
- `wiki/` pages for source summaries, concepts, decisions, and operating records.
- `tools/scripts/wiki_index.py` for local search.
- `checks/` scripts for basic validation and privacy checks.

Source files belong in `raw/`. Summaries, decisions, and reusable ideas belong in `wiki/`. AI tools start with `AGENTS.md`, follow the rules in `brain/`, and use `_system/index.md` or local search to find context.

## Design Choices

### Two Templates

The package includes a work template and a personal template. Work and personal systems use different page types, review habits, and privacy rules.

### Clear AI Instructions

`AGENTS.md` tells AI tools what to read first, what rules to follow, and how to handle source files, summaries, and privacy checks.

### Source Files Stay Separate

Original material stays in `raw/`. Written knowledge goes in `wiki/`. The separation keeps source material available without turning the workspace into a pile of loose files.

### Safe Placeholder Content

The public template does not include real raw documents, personal profiles, company details, or private project history. Raw folders contain README files that explain what could go there and what to consider before adding real material.

### Local Search

`tools/scripts/wiki_index.py` builds a local SQLite index from Markdown files. The index can be rebuilt at any time.

### Privacy Checks

`checks/offline_check.sh` scans for local paths, private identifiers, and organization/project-style leakage before sharing.

### Plain Files

The main files are Markdown. The scripts are small. The generated database is not the source of truth.

## How To Use It

1. Create a workspace with `npx create-ai-operating-system`.
2. Choose `--work` or `--personal`.
3. Add real source files only inside a private copy.
4. Summarize sources into `wiki/sources/`.
5. Record decisions and reusable ideas in `wiki/`.
6. Rebuild local search.
7. Query the workspace before starting from memory.
8. Run privacy checks before sharing.

## Keep Private

Do not publish real brain/profile files, personal facts, employer details, client/customer details, project history, local paths, raw documents, private source summaries, screenshots, IDs, financial data, health data, or credentials.

Use the public package as a scaffold. Use private clones for real life and work context.

## Credits

Built with inspiration from:

- Andrej Karpathy's LLM Wiki idea file: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Nate Jones' Open Brain / OB1 project: <https://github.com/NateBJones-Projects/OB1>
