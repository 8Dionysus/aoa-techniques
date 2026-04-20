from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_agon_technique_binding_candidates_current() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build_agon_technique_binding_candidates.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_agon_technique_binding_candidate_shape() -> None:
    data = json.loads((ROOT / "generated" / "agon_technique_binding_candidates.min.json").read_text())
    assert data["wave"] == "IV"
    assert data["total_candidates"] == 12
    assert all(c["bridge_kind"] == "practice_candidate" for c in data["candidates"])
