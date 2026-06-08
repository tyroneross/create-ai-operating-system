#!/usr/bin/env python3
"""Build and query the local Markdown index.

Markdown remains canonical. The SQLite database under `.system-cache/` is
derived and can be deleted or rebuilt at any time.
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = ROOT / ".system-cache"
DB_PATH = CACHE_DIR / "wiki.db"
INDEX_PATH = ROOT / "_system" / "index.md"

EXCLUDED_DIRS = {
    ".git",
    ".system-cache",
    ".vector",
    "node_modules",
    "raw",
    "outputs",
}


@dataclass
class Page:
    page_id: str
    title: str
    page_type: str
    status: str
    path: Path
    body: str


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def slug_from_path(path: Path) -> str:
    return path.stem.lower().replace(" ", "-")


def iter_markdown_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path == INDEX_PATH:
            continue
        paths.append(path)
    return sorted(paths)


def read_pages() -> list[Page]:
    pages: list[Page] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        title = fm.get("title") or path.stem.replace("-", " ").title()
        page_id = fm.get("id") or slug_from_path(path)
        page_type = fm.get("type") or path.relative_to(ROOT).parts[0]
        status = fm.get("status") or "seedling"
        pages.append(Page(page_id, title, page_type, status, path, body.strip()))
    return pages


def connect() -> sqlite3.Connection:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def rebuild_database(pages: list[Page]) -> None:
    conn = connect()
    conn.executescript(
        """
        drop table if exists pages;
        drop table if exists pages_fts;

        create table pages (
            page_id text primary key,
            title text not null,
            page_type text not null,
            status text not null,
            path text not null,
            body text not null,
            updated_at text not null
        );
        """
    )
    try:
        conn.execute(
            "create virtual table pages_fts using fts5(page_id unindexed, title, page_type, body)"
        )
        has_fts = True
    except sqlite3.OperationalError:
        has_fts = False

    now = datetime.now().isoformat(timespec="seconds")
    for page in pages:
        rel = str(page.path.relative_to(ROOT))
        conn.execute(
            "insert into pages values (?, ?, ?, ?, ?, ?, ?)",
            (page.page_id, page.title, page.page_type, page.status, rel, page.body, now),
        )
        if has_fts:
            conn.execute(
                "insert into pages_fts values (?, ?, ?, ?)",
                (page.page_id, page.title, page.page_type, page.body),
            )
    conn.commit()
    conn.close()


def rebuild_index(pages: list[Page]) -> None:
    groups: dict[str, list[Page]] = {}
    for page in pages:
        groups.setdefault(page.page_type, []).append(page)

    lines = [
        "# Index",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
    ]
    for group in sorted(groups):
        lines.append(f"## {group.title()}")
        lines.append("")
        for page in sorted(groups[group], key=lambda item: item.title.casefold()):
            rel = page.path.relative_to(ROOT)
            lines.append(f"- `{page.page_id}` - {page.title} [{page.status}] ({rel})")
        lines.append("")
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def rebuild() -> int:
    pages = read_pages()
    rebuild_database(pages)
    rebuild_index(pages)
    print(f"indexed {len(pages)} pages")
    print(f"wrote {INDEX_PATH.relative_to(ROOT)}")
    print(f"wrote {DB_PATH.relative_to(ROOT)}")
    return 0


def status() -> int:
    pages = read_pages()
    db_status = "present" if DB_PATH.exists() else "missing"
    print(f"root: {ROOT}")
    print(f"pages: {len(pages)}")
    print(f"database: {db_status}")
    return 0


def escape_fts_query(query: str) -> str:
    terms = re.findall(r"[A-Za-z0-9_'-]+", query)
    return " OR ".join(terms) if terms else query


def search(query: str, limit: int) -> int:
    if not DB_PATH.exists():
        rebuild()
    conn = connect()
    try:
        rows = conn.execute(
            """
            select p.page_id, p.title, p.page_type, p.status, p.path,
                   snippet(pages_fts, 3, '[', ']', ' ... ', 16) as snippet
            from pages_fts
            join pages p on p.page_id = pages_fts.page_id
            where pages_fts match ?
            limit ?
            """,
            (escape_fts_query(query), limit),
        ).fetchall()
    except sqlite3.OperationalError:
        pattern = f"%{query}%"
        rows = conn.execute(
            """
            select page_id, title, page_type, status, path, substr(body, 1, 240) as snippet
            from pages
            where title like ? or body like ?
            limit ?
            """,
            (pattern, pattern, limit),
        ).fetchall()
    finally:
        conn.close()

    for row in rows:
        print(f"{row['page_id']} | {row['title']} | {row['status']} | {row['path']}")
        snippet = " ".join(str(row["snippet"] or "").split())
        if snippet:
            print(f"  {snippet}")
    if not rows:
        print("no results")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local Markdown index")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("rebuild")
    sub.add_parser("status")
    search_parser = sub.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("-k", "--limit", type=int, default=8)
    args = parser.parse_args(argv)

    if args.command == "rebuild":
        return rebuild()
    if args.command == "status":
        return status()
    if args.command == "search":
        return search(args.query, args.limit)
    raise SystemExit(f"unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
