from __future__ import annotations

from pathlib import Path

from .common import fail

try:
    from scripts.agents_mesh_common import build_agents_mesh_index, compact_json, load_mesh_config
except ImportError:  # pragma: no cover - direct script import fallback
    from agents_mesh_common import build_agents_mesh_index, compact_json, load_mesh_config  # type: ignore


def expected_agents_mesh_index(repo_root: Path) -> str:
    return compact_json(build_agents_mesh_index(repo_root))


def validate_agents_mesh_projection(repo_root: Path) -> None:
    config = load_mesh_config(repo_root)
    generated_path = repo_root / config["generated_ref"]
    if not generated_path.is_file():
        fail(f"{config['generated_ref']}: file is missing")
    expected = expected_agents_mesh_index(repo_root)
    actual = generated_path.read_text(encoding="utf-8")
    if actual != expected:
        fail(f"{config['generated_ref']} is stale; run 'python scripts/build_agents_mesh_index.py'")
