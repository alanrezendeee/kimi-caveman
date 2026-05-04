#!/usr/bin/env python3
"""Caveman-compress: rewrite markdown files into terse caveman-speak.

Usage:
    python compress.py <input.md> [output.md]

If output not specified, writes to <input>.caveman.md
Preserves code blocks, URLs, paths, identifiers byte-for-byte.
"""

import re
import sys
from pathlib import Path


# Patterns to compress
FILLER_WORDS = re.compile(
    r'\b(actually|basically|essentially|literally|honestly|obviously|'
    r'clearly|generally|typically|usually|generally|I think|I believe|'
    r'it seems|it appears|you should|you could|you might want to|'
    r'I would recommend|I suggest|please note that|it is important to note that|'
    r'in order to|due to the fact that|at this point in time)\b',
    re.IGNORECASE,
)

ARTICLES = re.compile(r'\b(a|an|the)\b', re.IGNORECASE)

REDUNDANT_PHRASES = [
    (re.compile(r'in order to', re.IGNORECASE), 'to'),
    (re.compile(r'due to the fact that', re.IGNORECASE), 'because'),
    (re.compile(r'at this point in time', re.IGNORECASE), 'now'),
    (re.compile(r'for the purpose of', re.IGNORECASE), 'for'),
    (re.compile(r'with regard to', re.IGNORECASE), 'about'),
    (re.compile(r'in the event that', re.IGNORECASE), 'if'),
]


def is_preserved(line: str) -> bool:
    """Check if line should be preserved as-is."""
    stripped = line.strip()
    # Code blocks
    if stripped.startswith('```'):
        return True
    # Indented code
    if line.startswith('    ') or line.startswith('\t'):
        return True
    # URLs
    if re.match(r'^https?://', stripped):
        return True
    # File paths
    if re.match(r'^[`\w/\\.-]+\.(py|js|ts|go|rs|md|json|yaml|yml|toml|txt)$', stripped):
        return True
    # Already terse (bullet with code)
    if stripped.startswith('- `') or stripped.startswith('* `'):
        return True
    return False


def compress_line(line: str) -> str:
    """Compress a single line of markdown text."""
    if is_preserved(line):
        return line

    original = line

    # Remove redundant phrases
    for pattern, replacement in REDUNDANT_PHRASES:
        line = pattern.sub(replacement, line)

    # Remove filler words (but not at start of sentence if it breaks meaning)
    line = FILLER_WORDS.sub('', line)

    # Remove extra spaces left behind
    line = re.sub(r'  +', ' ', line)
    line = re.sub(r'^ ', '', line)
    line = re.sub(r' $', '', line)

    # If line got too mangled, return original
    if len(line.strip()) < 3 and len(original.strip()) > 10:
        return original

    return line


def compress_markdown(text: str) -> str:
    """Compress full markdown document."""
    lines = text.splitlines()
    result = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        # Toggle code block state
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Preserve code blocks entirely
        if in_code_block:
            result.append(line)
            continue

        # Preserve headers but can trim trailing words
        if stripped.startswith('#'):
            result.append(line)
            continue

        # Compress normal lines
        compressed = compress_line(line)
        result.append(compressed)

    return '\n'.join(result)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python compress.py <input.md> [output.md]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix('.caveman.md')

    if not input_path.exists():
        print(f"Error: {input_path} not found")
        sys.exit(1)

    original_text = input_path.read_text(encoding='utf-8')
    compressed_text = compress_markdown(original_text)

    # Backup original
    backup_path = input_path.with_suffix('.original.md')
    if not backup_path.exists():
        backup_path.write_text(original_text, encoding='utf-8')
        print(f"💾 Backup: {backup_path}")

    output_path.write_text(compressed_text, encoding='utf-8')

    orig_tokens = len(original_text.split())
    new_tokens = len(compressed_text.split())
    saved = orig_tokens - new_tokens
    pct = (saved / orig_tokens * 100) if orig_tokens else 0

    print(f"⛏ Compressed: {input_path} → {output_path}")
    print(f"   {orig_tokens} → {new_tokens} words ({saved} saved, {pct:.1f}%)")


if __name__ == '__main__':
    main()
