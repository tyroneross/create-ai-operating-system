# AI Operating System Writeup

## Bottom Line

This project packages a privacy-safe, local-first AI Operating System template. It gives people a ready folder structure for source files, summaries, decisions, work records, personal records, local search, and AI tool instructions.

## What It Is

The package creates a Markdown workspace with:

- `AGENTS.md` for AI tool instructions.
- `brain/rules.md` for file, privacy, and update rules.
- `brain/voice.md` for writing style.
- `_system/` files for the operating model, taxonomy, index, and log.
- `raw/` folders for source material.
- `wiki/` pages for source summaries, concepts, decisions, and operating records.
- `tools/scripts/wiki_index.py` for local search.
- `checks/` scripts for basic validation and privacy checks.

## What Makes It Special

### 1. It Starts With Two Templates

The package includes a work template and a personal template. Work and personal systems use different page types, review habits, and privacy rules.

### 2. It Gives AI Tools Clear Instructions

The generated `AGENTS.md` tells AI tools what to read first, what rules to follow, and how to handle source files, summaries, and privacy checks.

### 3. It Keeps Source Files Separate From Written Knowledge

Source files belong in `raw/`. Summaries, decisions, and reusable ideas belong in `wiki/`. This keeps original material available without turning the whole system into a pile of loose files.

### 4. It Ships Safe Placeholder Content

The public template does not include real raw documents, personal profiles, company details, or private project history. Raw folders contain README files that explain what could go there and what to consider before adding real material.

### 5. It Includes Local Search

`tools/scripts/wiki_index.py` builds a local SQLite index from Markdown files. The index can be rebuilt at any time.

### 6. It Makes Privacy Review Part Of The Workflow

`checks/offline_check.sh` scans for local paths, private identifiers, and organization/project-style leakage before sharing.

### 7. It Stays Easy To Inspect

The main files are Markdown. The scripts are small. The generated database is not the source of truth.

## What To Keep Private

Do not publish real brain/profile files, personal facts, employer details, client/customer details, project history, local paths, raw documents, private source summaries, screenshots, IDs, financial data, health data, or credentials.

Use the public package as a scaffold. Use private clones for real life and work context.

## Credits

This project was built with inspiration from:

- Andrej Karpathy's LLM Wiki idea file: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Nate Jones' Open Brain / OB1 project: <https://github.com/NateBJones-Projects/OB1>
