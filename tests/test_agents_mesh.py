from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.agents_mesh_common import active_card_route_issues


REPO_ROOT = Path(__file__).resolve().parents[1]


class AgentsMeshTests(unittest.TestCase):
    def run_repo_script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            (sys.executable, *args),
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_agents_mesh_validators_pass(self) -> None:
        for script in (
            "scripts/validate_agents_md_shape.py",
            "scripts/validate_agents_mesh.py",
            "scripts/build_agents_mesh_index.py",
            "scripts/validate_agents_mesh_index.py",
        ):
            args = (script, "--check") if script.endswith("build_agents_mesh_index.py") else (script,)
            self.run_repo_script(*args)

    def test_generated_mesh_records_only_canonical_cards(self) -> None:
        payload = json.loads((REPO_ROOT / "generated" / "agents_mesh.min.json").read_text())
        self.assertEqual("aoa_techniques_agents_mesh_index_v1", payload["schema_version"])
        self.assertEqual(payload["counts"]["cards"], payload["counts"]["canonical"])
        self.assertEqual(0, payload["counts"]["migration"])

        cards_by_path = {card["path"]: card for card in payload["cards"]}
        self.assertEqual("canonical", cards_by_path["AGENTS.md"]["shape_status"])
        self.assertEqual("canonical", cards_by_path["docs/AGENTS.md"]["shape_status"])
        self.assertEqual(
            "canonical",
            cards_by_path["docs/decisions/AGENTS.md"]["shape_status"],
        )
        self.assertEqual(
            "canonical",
            cards_by_path["docs/guardrails/AGENTS.md"]["shape_status"],
        )
        self.assertIn("mechanics/agon/AGENTS.md", cards_by_path)
        self.assertEqual("canonical", cards_by_path["mechanics/agon/AGENTS.md"]["shape_status"])
        self.assertEqual("canonical", cards_by_path["stats/AGENTS.md"]["shape_status"])

    def test_agents_mesh_config_names_design_sources(self) -> None:
        config = json.loads((REPO_ROOT / "config" / "agents_mesh.json").read_text())
        self.assertEqual("DESIGN.md", config["system_design_ref"])
        self.assertEqual("DESIGN.AGENTS.md", config["design_ref"])
        self.assertEqual(
            "docs/guardrails/AGENTS_MESH_PROTOCOL.md",
            config["authority_ref"],
        )
        self.assertFalse(config["migration_allowed"])

    def test_agents_mesh_validator_ignores_untracked_top_level_dirs(self) -> None:
        with tempfile.TemporaryDirectory(prefix="tmp-agents-mesh-", dir=REPO_ROOT):
            result = subprocess.run(
                (sys.executable, "scripts/validate_agents_mesh.py"),
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_agents_mesh_ignores_dependency_checkouts(self) -> None:
        deps_root = REPO_ROOT / ".deps"
        deps_root.mkdir(exist_ok=True)
        try:
            with tempfile.TemporaryDirectory(dir=deps_root) as checkout:
                (Path(checkout) / "AGENTS.md").write_text(
                    "# Foreign dependency route\n",
                    encoding="utf-8",
                )
                result = subprocess.run(
                    (sys.executable, "scripts/validate_agents_md_shape.py"),
                    cwd=REPO_ROOT,
                    check=False,
                    capture_output=True,
                    text=True,
                )
        finally:
            if not any(deps_root.iterdir()):
                deps_root.rmdir()

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_active_route_guard_rejects_executable_and_structural_residue(self) -> None:
        card = """# AGENTS.md

## Applies to
this path

## Role
local owner

## Read before editing
Read `README.md` before every edit.

## Boundaries
- Do not widen ownership.

## Validation
Select `source-fast`; see VALIDATION.md and config/validation_lanes.json.
```bash
python scripts/validate_repo.py
```

## Closeout
Report the route and remaining risk.
"""
        issues = active_card_route_issues(card)
        self.assertTrue(any("executable fences" in issue for issue in issues))
        self.assertTrue(any("runnable command" in issue for issue in issues))
        self.assertTrue(any("unconditional README" in issue for issue in issues))

    def test_active_route_guard_accepts_on_demand_route_card(self) -> None:
        card = """# AGENTS.md

## Applies to
this path

## Role
local owner

## Read before editing
Read the nearest owner card. Read `README.md` only when the selected task
needs its human map.

## Boundaries
- Do not widen ownership.

## Validation
Select the `source-fast` lane in VALIDATION.md; exact order is
config/validation_lanes.json.

## Closeout
Report the route and remaining risk.
"""
        self.assertEqual([], active_card_route_issues(card))


if __name__ == "__main__":
    unittest.main()
