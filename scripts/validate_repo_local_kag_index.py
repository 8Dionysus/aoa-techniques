#!/usr/bin/env python3
"""Check the owner-local KAG index family with the canonical aoa-kag builder."""

from __future__ import annotations

import os
import subprocess
import sys
from collections.abc import Mapping
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = "kag/indexes/source_surface_index.json"
GENERATOR_PATH = Path("scripts/generate_repo_local_kag_index.py")
VALIDATOR_PATH = Path("scripts/validate_repo_local_kag_family.py")
AOA_KAG_REF = "790457eb4806586c255c2b4a9ec4a8f08789a330"


def resolve_aoa_kag_root(
    env: Mapping[str, str] = os.environ,
    repo_root: Path = REPO_ROOT,
) -> Path:
    override = env.get("AOA_KAG_ROOT")
    candidates = [Path(override).expanduser()] if override else []
    candidates.append(repo_root.parent / "aoa-kag")

    for candidate in candidates:
        if all(
            (candidate / path).is_file()
            for path in (GENERATOR_PATH, VALIDATOR_PATH)
        ):
            return candidate.resolve()

    raise FileNotFoundError(
        "aoa-kag KAG tooling is unavailable; set AOA_KAG_ROOT or place "
        "aoa-kag beside aoa-techniques"
    )


def require_pinned_checkout(aoa_kag_root: Path) -> Path:
    completed = subprocess.run(
        ("git", "-C", str(aoa_kag_root), "rev-parse", "HEAD"),
        check=False,
        capture_output=True,
        text=True,
    )
    ref = completed.stdout.strip()
    if completed.returncode or ref != AOA_KAG_REF:
        raise RuntimeError(
            f"aoa-kag checkout must resolve {AOA_KAG_REF}; got {ref or 'unresolved'}"
        )
    return aoa_kag_root


def commands(
    aoa_kag_root: Path,
    repo_root: Path = REPO_ROOT,
) -> tuple[tuple[str, ...], ...]:
    base = (
        sys.executable,
        str(aoa_kag_root / GENERATOR_PATH),
        "--repo-root",
        str(repo_root),
        "--output",
        INDEX_PATH,
        "--index-family",
    )
    return (
        (*base, "--check"),
        (*base, "--incremental", "--check"),
        (
            sys.executable,
            str(aoa_kag_root / VALIDATOR_PATH),
            "--repo-root",
            str(repo_root),
            "--source-index",
            INDEX_PATH,
        ),
    )


def main() -> int:
    try:
        aoa_kag_root = require_pinned_checkout(resolve_aoa_kag_root())
        for command in commands(aoa_kag_root):
            result = subprocess.run(command, cwd=REPO_ROOT, check=False)
            if result.returncode:
                return result.returncode
        return 0
    except (OSError, RuntimeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
