#!/usr/bin/env python3
"""Check the owner-local KAG index family with the canonical aoa-kag builder."""

from __future__ import annotations

import os
import subprocess
import sys
from collections.abc import Mapping
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_VIEW_PATH = "kag/indexes/source_surface_index.json"
GENERATOR_PATH = Path("scripts/generate_repo_local_kag_index.py")
VALIDATOR_PATH = Path("scripts/validate_repo_local_kag_family.py")
AOA_KAG_REF = "14ee1e33e43749d23c557b3ef526eca7edb36196"
HISTORY_REPO_ENV = "AOA_REPO_LOCAL_KAG_HISTORY_REPO"
HISTORY_REF_ENV = "AOA_REPO_LOCAL_KAG_HISTORY_REF"
EVENT_HISTORY_REF_ENV = "AOA_REPO_LOCAL_KAG_EVENT_HISTORY_REF"
OWNER_REPO = "aoa-techniques"


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


def resolve_history_refs(
    env: Mapping[str, str] = os.environ,
    repo_root: Path = REPO_ROOT,
) -> tuple[str | None, str | None]:
    if env.get(HISTORY_REPO_ENV) == OWNER_REPO:
        history_ref = env.get(HISTORY_REF_ENV, "").strip()
        event_history_ref = env.get(EVENT_HISTORY_REF_ENV, "").strip()
        if history_ref:
            return history_ref, event_history_ref or history_ref

    completed = subprocess.run(
        ("git", "-C", str(repo_root), "merge-base", "HEAD", "origin/main"),
        check=False,
        capture_output=True,
        text=True,
    )
    history_ref = completed.stdout.strip()
    if completed.returncode or not history_ref:
        return None, None
    return history_ref, history_ref


def commands(
    aoa_kag_root: Path,
    repo_root: Path = REPO_ROOT,
    *,
    history_ref: str | None = None,
    event_history_ref: str | None = None,
) -> tuple[tuple[str, ...], ...]:
    base = (
        sys.executable,
        str(aoa_kag_root / GENERATOR_PATH),
        "--repo-root",
        str(repo_root),
        "--output",
        SOURCE_VIEW_PATH,
        "--portable-family",
    )
    history_args = (
        ("--history-ref", history_ref, "--event-history-ref", event_history_ref or history_ref)
        if history_ref
        else ()
    )
    return (
        (*base, *history_args, "--check"),
        (*base, "--incremental", *history_args, "--check"),
        (
            sys.executable,
            str(aoa_kag_root / VALIDATOR_PATH),
            "--repo-root",
            str(repo_root),
            "--source-index",
            SOURCE_VIEW_PATH,
        ),
    )


def main() -> int:
    try:
        aoa_kag_root = require_pinned_checkout(resolve_aoa_kag_root())
        history_ref, event_history_ref = resolve_history_refs()
        for command in commands(
            aoa_kag_root,
            history_ref=history_ref,
            event_history_ref=event_history_ref,
        ):
            result = subprocess.run(command, cwd=REPO_ROOT, check=False)
            if result.returncode:
                return result.returncode
        return 0
    except (OSError, RuntimeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
