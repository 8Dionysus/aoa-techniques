from __future__ import annotations

from pathlib import Path

from .common import fail

try:
    from scripts import decision_indexes
except ImportError:  # pragma: no cover - direct script import fallback
    import decision_indexes  # type: ignore


def validate_decision_indexes(repo_root: Path) -> None:
    issues = decision_indexes.validate_decision_index_surfaces(repo_root)
    if issues:
        location, message = issues[0]
        fail(f"{location}: {message}")
