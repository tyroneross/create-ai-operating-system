# Operating Model

This AI Operating System turns raw context into reusable, queryable operating knowledge.

## Core Idea

Raw sources are preserved. The wiki holds the summaries, decisions, and reusable ideas. AI tools read the wiki first, update it deliberately, and keep a log of changes. Useful answers are saved back into the workspace instead of disappearing into chat history.

## Daily Loop

1. Capture new material in `raw/ingest/`.
2. Convert useful material into source pages.
3. Extract durable ideas into concept pages.
4. Use variant-specific templates for decisions, plans, meetings, reviews, or personal operating records.
5. Rebuild the local index.
6. Query before answering from memory.

## What Makes This An Operating System

- It has rules (`brain/rules.md`).
- It has a voice contract (`brain/voice.md`).
- It has typed source, concept, and operating pages.
- It has a lifecycle log.
- It has local search.
- It separates public template structure from private content.

## Agent Contract

Agents should:

- Use `_system/index.md` and `llmwiki` before answering filed-knowledge questions.
- Create synthesis pages when an answer is likely to be reused.
- Preserve raw/source provenance.
- Avoid irreversible structural changes without explicit direction.
- Keep all publishable examples generic.
