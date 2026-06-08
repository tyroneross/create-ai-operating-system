# System Rules

## Source Of Truth

Markdown is the source of truth. Generated indexes under `.system-cache/` can be rebuilt and should not be treated as canonical.

## Layers

| Layer | Purpose | Write Policy |
|---|---|---|
| `raw/` | Immutable source material and ingestion drop zone | Keep original material unchanged |
| `wiki/sources/` | Source summaries with citations back to raw material | Draft or update during ingest |
| `wiki/concepts/` | Durable ideas, frameworks, claims, and reusable models | Update when synthesis changes |
| Variant folders | Work or personal operating pages | Keep specific to the selected template |
| `_system/` | Indexes, logs, and operating model | Update after material changes |
| `outputs/` | Answers, drafts, health reports | Append when useful |

## Page Status

- `seedling`: useful first draft, not fully reviewed.
- `sprout`: reviewed enough for normal recall.
- `evergreen`: stable and high confidence.
- `superseded`: preserved for history but replaced by a newer page.

## Frontmatter Minimum

```yaml
---
id: example-page-id
title: "Example Page"
type: concept
status: seedling
created: 2026-01-01
updated: 2026-01-01
tags: [example]
---
```

## Source Pages

Every source page should answer normal future questions without reopening the raw file. Preserve:

- What the source says.
- Why it matters.
- Important dates, numbers, decisions, and constraints.
- Links to related pages.
- `raw_ref:` pointing to the source or placeholder.
- Confidence and open questions.

## Privacy

Default to public-safe placeholders in this template. In private use, classify sensitive data before writing it:

- `public`: safe to publish.
- `internal`: useful in the local system but not public.
- `restricted`: requires explicit human review before sharing.
- `secret`: never commit, publish, or sync.

Do not track passwords, API keys, tokens, private addresses, identity documents, financial account numbers, medical details, or unredacted customer/client records.

## Update Protocol

When editing a page:

1. Read the current page and outbound links.
2. Update content with source-backed claims.
3. Bump `updated:`.
4. Add or fix related links.
5. Rebuild `_system/index.md` with `python3 tools/scripts/wiki_index.py rebuild`.
6. Append a short entry to `_system/log.md` for material changes.
