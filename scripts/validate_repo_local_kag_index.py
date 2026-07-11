#!/usr/bin/env python3
"""Check the owner-local KAG index family with the canonical aoa-kag builder."""

from __future__ import annotations

import os
import hashlib
import subprocess
import sys
from collections.abc import Mapping
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable, Iterator
from urllib.request import urlopen


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = "kag/indexes/source_surface_index.json"
GENERATOR_PATH = Path("scripts/generate_repo_local_kag_index.py")
AOA_KAG_REF = "a8045bdfecd4256b93736805b7303048a993ae01"
GENERATOR_SHA256 = "1a922a33feb3b42003bf50554355a18e4422fb45cc5bb7c510484dad20ce199f"
GENERATOR_URL = (
    "https://raw.githubusercontent.com/8Dionysus/aoa-kag/"
    f"{AOA_KAG_REF}/{GENERATOR_PATH.as_posix()}"
)


def resolve_aoa_kag_root(
    env: Mapping[str, str] = os.environ,
    repo_root: Path = REPO_ROOT,
) -> Path:
    override = env.get("AOA_KAG_ROOT")
    candidates = [Path(override).expanduser()] if override else []
    candidates.append(repo_root.parent / "aoa-kag")

    for candidate in candidates:
        generator = candidate / GENERATOR_PATH
        if generator.is_file():
            return candidate.resolve()

    raise FileNotFoundError(
        "aoa-kag index builder is unavailable; set AOA_KAG_ROOT or place "
        "aoa-kag beside aoa-techniques"
    )


def fetch_generator(
    destination: Path,
    *,
    opener: Callable[..., object] = urlopen,
) -> Path:
    print(f"[repo-local-kag-index] fetching pinned builder {AOA_KAG_REF}", file=sys.stderr)
    with opener(GENERATOR_URL, timeout=30) as response:  # type: ignore[attr-defined]
        content = response.read()  # type: ignore[attr-defined]
    digest = hashlib.sha256(content).hexdigest()
    if digest != GENERATOR_SHA256:
        raise RuntimeError(
            f"downloaded aoa-kag generator digest mismatch: expected {GENERATOR_SHA256}, got {digest}"
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)
    return destination


def generator_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_pinned_generator(path: Path, *, label: str) -> Path:
    digest = generator_digest(path)
    if digest != GENERATOR_SHA256:
        raise RuntimeError(
            f"{label} aoa-kag generator digest mismatch: "
            f"expected {GENERATOR_SHA256}, got {digest}"
        )
    return path


@contextmanager
def canonical_generator(
    env: Mapping[str, str] = os.environ,
    repo_root: Path = REPO_ROOT,
) -> Iterator[Path]:
    try:
        aoa_kag_root = resolve_aoa_kag_root(env, repo_root)
    except FileNotFoundError:
        with TemporaryDirectory(prefix="aoa-kag-index-builder-") as temp_dir:
            yield fetch_generator(Path(temp_dir) / GENERATOR_PATH)
        return
    generator = aoa_kag_root / GENERATOR_PATH
    if generator_digest(generator) == GENERATOR_SHA256:
        yield generator
        return
    if env.get("AOA_KAG_ROOT"):
        yield require_pinned_generator(generator, label="AOA_KAG_ROOT")
        return
    with TemporaryDirectory(prefix="aoa-kag-index-builder-") as temp_dir:
        yield fetch_generator(Path(temp_dir) / GENERATOR_PATH)


def command(generator: Path, repo_root: Path = REPO_ROOT) -> tuple[str, ...]:
    return (
        sys.executable,
        str(generator),
        "--repo-root",
        str(repo_root),
        "--output",
        INDEX_PATH,
        "--index-family",
        "--check",
    )


def main() -> int:
    try:
        with canonical_generator() as generator:
            return subprocess.run(command(generator), cwd=REPO_ROOT, check=False).returncode
    except (OSError, RuntimeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
