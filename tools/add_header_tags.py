#!/usr/bin/env python3
"""
Add header tags to markdown cells in Jupyter notebooks.

This script scans Jupyter notebooks for markdown cells that start with
headers (# or ##) and adds appropriate metadata tags like "h1:slug" or "h2:slug".
"""

import json
import re
import sys
from pathlib import Path


def slugify(text: str) -> str:
    """
    Convert text to a slug.

    Converts to lowercase, removes special characters, replaces spaces with hyphens.
    """
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    # Remove characters that aren't alphanumeric, hyphens, or slashes
    text = re.sub(r"[^a-z0-9-/]", '', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text


def get_header_info(cell_content: str) -> tuple[int, str] | None:
    """
    Extract header level and text from markdown cell content.

    Returns (level, text) if the cell starts with a header, None otherwise.
    Level is 1 for #, 2 for ##, etc.
    """
    lines = cell_content.strip().split('\n')
    if not lines:
        return None

    first_line = lines[0].strip()

    # Check for ATX-style headers (# Header)
    match = re.match(r'^(#{1,6})\s+(.+)$', first_line)
    if match:
        level = len(match.group(1))
        text = match.group(2)
        return (level, text)

    # Check for Setext-style headers (underlined with === or ---)
    if len(lines) >= 2:
        second_line = lines[1].strip()
        if re.match(r'^=+$', second_line):
            return (1, first_line)
        if re.match(r'^-+$', second_line):
            return (2, first_line)

    return None


def process_notebook(notebook_path: Path, dry_run: bool = False) -> bool:
    """
    Process a single notebook and add header tags.

    Returns True if the notebook was modified, False otherwise.
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    modified = False
    cells = notebook.get('cells', [])

    for i, cell in enumerate(cells):
        if cell.get('cell_type') != 'markdown':
            continue

        content = cell.get('source', [])
        if isinstance(content, list):
            content = ''.join(content)

        header_info = get_header_info(content)
        if header_info is None:
            continue

        level, text = header_info

        # Only process h1 and h2
        if level not in (1, 2):
            continue

        slug = slugify(text)
        tag = f"h{level}:{slug}"

        # Get existing metadata
        metadata = cell.get('metadata', {})
        tags = metadata.get('tags', [])

        # Add tag if not already present
        if tag not in tags:
            tags.append(tag)
            metadata['tags'] = tags
            cell['metadata'] = metadata
            modified = True
            print(f"  [{i}] Added tag '{tag}' for header: {text}")

    if modified and not dry_run:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
            f.write('\n')  # Add trailing newline

    return modified


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Add header tags to markdown cells in Jupyter notebooks'
    )
    parser.add_argument(
        'paths',
        nargs='+',
        type=Path,
        help='Paths to notebooks or directories to process'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )

    args = parser.parse_args()

    # Collect all notebook paths
    notebook_paths = []
    for path in args.paths:
        if path.is_file() and path.suffix == '.ipynb':
            notebook_paths.append(path)
        elif path.is_dir():
            notebook_paths.extend(path.rglob('*.ipynb'))
        else:
            print(f"Warning: Skipping invalid path: {path}", file=sys.stderr)

    if not notebook_paths:
        print("No notebooks found to process.")
        return 0

    # Process each notebook
    modified_count = 0
    for notebook_path in sorted(notebook_paths):
        print(f"\nProcessing: {notebook_path}")
        if process_notebook(notebook_path, dry_run=args.dry_run):
            modified_count += 1
            if args.dry_run:
                print("  [DRY RUN] Would modify this notebook")
            else:
                print("  Modified")
        else:
            print("  No changes needed")

    print(f"\n{'=' * 60}")
    print(f"Processed {len(notebook_paths)} notebook(s)")
    if args.dry_run:
        print(f"[DRY RUN] Would modify {modified_count} notebook(s)")
    else:
        print(f"Modified {modified_count} notebook(s)")

    return 0


if __name__ == '__main__':
    sys.exit(main())
