from __future__ import annotations

import argparse
import sys
from pathlib import Path

from validate_repo import (
    QUEST_CATALOG_EXAMPLE_PATH,
    QUEST_CATALOG_PATH,
    QUEST_DISPATCH_EXAMPLE_PATH,
    QUEST_DISPATCH_PATH,
    build_quest_catalog_projection,
    build_quest_dispatch_projection,
    read_json,
    write_json_file,
)


def write_projection(repo_root: Path) -> None:
    catalog_payload = build_quest_catalog_projection(repo_root)
    dispatch_payload = build_quest_dispatch_projection(repo_root)

    write_json_file(repo_root / QUEST_CATALOG_PATH, catalog_payload, compact=True)
    write_json_file(repo_root / QUEST_DISPATCH_PATH, dispatch_payload, compact=True)
    write_json_file(repo_root / QUEST_CATALOG_EXAMPLE_PATH, catalog_payload, compact=False)
    write_json_file(repo_root / QUEST_DISPATCH_EXAMPLE_PATH, dispatch_payload, compact=False)


def check_projection(repo_root: Path) -> int:
    expected_catalog = build_quest_catalog_projection(repo_root)
    expected_dispatch = build_quest_dispatch_projection(repo_root)
    checks = (
        (QUEST_CATALOG_PATH, expected_catalog),
        (QUEST_DISPATCH_PATH, expected_dispatch),
        (QUEST_CATALOG_EXAMPLE_PATH, expected_catalog),
        (QUEST_DISPATCH_EXAMPLE_PATH, expected_dispatch),
    )
    for relative_path, expected in checks:
        path = repo_root / relative_path
        if not path.is_file():
            print(f"[error] {relative_path.as_posix()}: file is missing", file=sys.stderr)
            return 1
        actual = read_json(path)
        if actual != expected:
            print(
                f"[error] {relative_path.as_posix()}: questbook projection is stale; "
                "run 'python scripts/build_questbook_projection.py'",
                file=sys.stderr,
            )
            return 1
    print("[ok] questbook projections are current")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build questbook generated projections.")
    parser.add_argument("--check", action="store_true", help="fail if projections are stale")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    if args.check:
        return check_projection(repo_root)

    write_projection(repo_root)
    for relative_path in (
        QUEST_CATALOG_PATH,
        QUEST_DISPATCH_PATH,
        QUEST_CATALOG_EXAMPLE_PATH,
        QUEST_DISPATCH_EXAMPLE_PATH,
    ):
        print(f"[ok] wrote {relative_path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
