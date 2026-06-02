from __future__ import annotations

from .common import *


def strip_allowlisted_public_urls(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        url = match.group(0)
        if url.startswith(PUBLIC_HYGIENE_ALLOWED_URL_PREFIXES):
            return ""
        return url

    return PUBLIC_HYGIENE_URL_RE.sub(replace, text)


def blocked_public_hygiene_patterns(text: str) -> tuple[str, ...]:
    candidate = strip_allowlisted_public_urls(text)
    matches = [
        description
        for description, pattern in PUBLIC_HYGIENE_BLOCKED_PATTERNS
        if pattern.search(candidate)
    ]
    return tuple(matches)


def iter_public_hygiene_paths(repo_root: Path) -> tuple[Path, ...]:
    paths: list[Path] = []

    root_files = sorted(
        path
        for path in repo_root.iterdir()
        if path.is_file()
        and path.name not in PUBLIC_HYGIENE_EXCLUDED_ROOT_FILES
    )
    paths.extend(root_files)

    for relative_dir in PUBLIC_HYGIENE_SCAN_DIRS:
        base = repo_root / relative_dir
        if not base.exists():
            continue
        paths.extend(sorted(path for path in base.rglob("*") if path.is_file()))

    return tuple(sorted(paths, key=lambda path: path.relative_to(repo_root).as_posix()))


def validate_public_hygiene(repo_root: Path) -> None:
    for path in iter_public_hygiene_paths(repo_root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        for line_number, line in enumerate(lines, start=1):
            matches = blocked_public_hygiene_patterns(line)
            if matches:
                blocked = ", ".join(matches)
                fail(f"{path}:{line_number}: public surface matches blocked pattern(s): {blocked}")
