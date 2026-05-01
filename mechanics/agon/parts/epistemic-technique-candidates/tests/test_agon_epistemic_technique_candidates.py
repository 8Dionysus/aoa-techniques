from __future__ import annotations

import json
import pathlib
import subprocess
import sys

PART_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = pathlib.Path(__file__).resolve().parents[5]


def test_generated_registry_shape():
    reg = json.loads(
        (PART_ROOT / "generated" / "agon_epistemic_technique_candidates.min.json").read_text(encoding="utf-8")
    )
    assert reg["wave"] == "XV"
    assert reg["runtime_posture"] in ("candidate_only", "pre_protocol_candidate_only")
    assert reg["count"] == 10
    assert len(reg["techniques"]) == 10
    for item in reg["techniques"]:
        assert item["live_protocol"] is False
        assert "auto_doctrine_rewrite" in item.get("forbidden_effects", [])


def test_builder_check_and_validator():
    assert (
        subprocess.run(
            [
                sys.executable,
                str(PART_ROOT / "scripts" / "build_agon_epistemic_technique_candidates.py"),
                "--check",
            ],
            cwd=REPO_ROOT,
        ).returncode
        == 0
    )
    assert (
        subprocess.run(
            [sys.executable, str(PART_ROOT / "scripts" / "validate_agon_epistemic_technique_candidates.py")],
            cwd=REPO_ROOT,
        ).returncode
        == 0
    )
