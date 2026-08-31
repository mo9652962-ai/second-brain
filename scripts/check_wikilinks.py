"""Check Obsidian wikilinks against the Markdown files in the vault."""

import posixpath
import re
import sys
from pathlib import Path


LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")
IGNORED_DIRS = {"node_modules"}


def collect_notes(root: Path) -> list[Path]:
    """Return vault notes while skipping hidden and generated dependency dirs."""
    notes = []
    for path in root.rglob("*.md"):
        relative_parts = path.relative_to(root).parts
        if any(part.startswith(".") or part in IGNORED_DIRS for part in relative_parts):
            continue
        notes.append(path)
    return sorted(notes)


def relative_key(path: Path, root: Path) -> str:
    """Return a case-insensitive, POSIX-style path without its .md suffix."""
    relative = path.relative_to(root).as_posix()
    if relative.casefold().endswith(".md"):
        relative = relative[:-3]
    return relative.casefold()


def build_indexes(notes: list[Path], root: Path) -> tuple[set[str], dict[str, set[str]]]:
    paths = {relative_key(note, root) for note in notes}
    by_name: dict[str, set[str]] = {}
    for note in notes:
        key = relative_key(note, root)
        name = Path(key).name
        by_name.setdefault(name, set()).add(key)
    return paths, by_name


def target_candidates(source: str, target: str) -> tuple[list[str], str]:
    """Resolve root-relative, source-relative, and basename-style Obsidian links."""
    target = target.strip().replace("\\", "/")
    target = target.removesuffix(".md")
    if not target:
        return [], target

    if target.startswith(("http://", "https://")):
        return [], target

    source_dir = posixpath.dirname(source)
    candidates = [posixpath.normpath(target).lstrip("./")]
    source_relative = posixpath.normpath(posixpath.join(source_dir, target))
    if source_relative not in candidates:
        candidates.append(source_relative)

    # A link without a directory is resolved by note name, as Obsidian does.
    if "/" not in target:
        candidates.append(Path(target).name)
    return [candidate.casefold() for candidate in candidates], target


def in_inline_code(line: str, start: int) -> bool:
    """Whether a match starts inside a single-backtick code span."""
    return line[:start].count("`") % 2 == 1


def main() -> int:
    root = Path.cwd()
    notes = collect_notes(root)
    note_paths, note_names = build_indexes(notes, root)
    errors = 0

    for note in notes:
        source = note.relative_to(root).as_posix()
        in_fenced_code = False
        with note.open(encoding="utf-8", errors="replace") as handle:
            for lineno, line in enumerate(handle, 1):
                if re.match(r"^\s*(```|~~~)", line):
                    in_fenced_code = not in_fenced_code
                    continue
                if in_fenced_code:
                    continue
                for match in LINK_PATTERN.finditer(line):
                    if in_inline_code(line, match.start()):
                        continue
                    target = match.group(1).split("|", 1)[0].split("#", 1)[0]
                    candidates, display_target = target_candidates(source, target)
                    if display_target.startswith(("http://", "https://")):
                        continue
                    found = any(
                        candidate in note_paths
                        or candidate in note_names
                        and bool(note_names[candidate] & note_paths)
                        for candidate in candidates
                    )
                    if not found:
                        print(f"⚠ Broken link: {source}:{lineno} → {target}")
                        errors += 1

    if errors:
        print(f"❌ Found {errors} broken wikilinks")
        return 1
    print("✅ All wikilinks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
