# AI Operating System Quickstart Guide

This guide shows the normal flow after creating a workspace.

## 1. Choose A Template

Use `work` for projects, meetings, decisions, research, stakeholder context, and operating reviews.

Use `personal` for goals, learning, routines, personal decisions, reviews, and private research.

## 2. Create The Workspace

```bash
npx create-ai-operating-system my-aos --work
cd my-aos
```

For personal use:

```bash
npx create-ai-operating-system my-aos --personal
cd my-aos
```

## 3. Read The Rules

Start here before adding real content:

```bash
sed -n '1,160p' AGENTS.md
sed -n '1,160p' brain/rules.md
sed -n '1,160p' _system/OPERATING_MODEL.md
```

`AGENTS.md` tells AI tools what to read first. `brain/rules.md` explains the file lifecycle and privacy rules. `_system/OPERATING_MODEL.md` explains how the workspace should run.

## 4. Add Source Material

Add real source material only inside a private workspace.

Good first sources:

- A meeting note.
- A project brief.
- A decision note.
- A public article.
- A learning note.

Use `raw/ingest/` for new material when you have not decided where it belongs. Use the specific raw folders once the domain is clear.

## 5. Write The Source Summary

Create or update a page in `wiki/sources/`.

Capture:

- What the source says.
- Why it matters.
- Key dates, decisions, numbers, and constraints.
- Open questions.
- Links to related pages.
- The `raw_ref` that points back to the source.

## 6. Save Reusable Ideas

Use `wiki/concepts/` for ideas that should survive beyond one source.

Examples:

- A decision rule.
- A framework.
- A recurring pattern.
- A question to revisit.

## 7. Record Work Or Personal Execution

For the work template, use `wiki/work/` for projects, decision logs, meeting synthesis, and operating reviews.

For the personal template, use `wiki/life/` for goals, routines, learning plans, decisions, and reviews.

## 8. Rebuild Search

Run this after meaningful edits:

```bash
python3 tools/scripts/wiki_index.py rebuild
```

## 9. Query Before Starting From Memory

```bash
./tools/scripts/llmwiki search "decision log"
./tools/scripts/llmwiki search "weekly review"
./tools/scripts/llmwiki search "project risk"
```

Use search results as the starting point for AI sessions.

## 10. Check Before Sharing

```bash
./checks/offline_check.sh
```

The check looks for local paths, private identifiers, and organization/project-style leakage. It is not a full privacy review. Treat it as a guardrail, not a guarantee.

## 11. Keep The System Current

After each meaningful work session:

1. Save useful answers back into `wiki/` or `outputs/`.
2. Update decisions when they change.
3. Rebuild search.
4. Append material changes to `_system/log.md`.

The goal is simple: future sessions should start from filed context, not from scratch.
