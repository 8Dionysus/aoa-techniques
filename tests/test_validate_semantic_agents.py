from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "validate_semantic_agents.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_semantic_agents", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ValidateSemanticAgentsTests(unittest.TestCase):
    @staticmethod
    def write_route_card(path: Path, *, validation: str | None = None) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        validation = validation or (
            "Select the source-fast lane; see [VALIDATION.md](../VALIDATION.md) "
            "and config/validation_lanes.json."
        )
        path.write_text(
            "\n".join(
                (
                    "# AGENTS.md",
                    "",
                    "## Applies to",
                    "This selected route-card fixture.",
                    "",
                    "## Role",
                    "This fixture describes a bounded owner route. No secrets.",
                    "",
                    "## Read before editing",
                    "Read the source surface and its owner route.",
                    "",
                    "## Boundaries",
                    "Do not claim semantic meaning from this structural fixture.",
                    "",
                    "## Validation",
                    validation,
                    "",
                    "## Closeout",
                    "Report the changed surface, checks run, and skipped routes.",
                    "",
                )
            ),
            encoding="utf-8",
        )

    def build_fixture(self, root: Path, module) -> None:
        for spec in module.REQUIRED_DOCS:
            self.write_route_card(root / spec.path)

    def test_repository_semantic_docs_validate(self) -> None:
        module = load_validator()
        self.assertEqual(module.validate(REPO_ROOT), [])

    def test_missing_required_doc_fails(self) -> None:
        module = load_validator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.build_fixture(root, module)
            missing = root / module.REQUIRED_DOCS[0].path
            missing.unlink()
            issues = module.validate(root)
        self.assertTrue(any("file is missing" in issue for issue in issues))

    def test_missing_validation_route_fails(self) -> None:
        module = load_validator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.build_fixture(root, module)
            target_spec = module.REQUIRED_DOCS[0]
            target = root / target_spec.path
            self.write_route_card(
                target,
                validation="Select the source-fast lane; see [VALIDATION.md](../VALIDATION.md).",
            )
            issues = module.validate(root)
        self.assertTrue(any("config/validation_lanes.json" in issue for issue in issues))

    def test_safe_prose_rewording_does_not_fail(self) -> None:
        module = load_validator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.build_fixture(root, module)
            target = root / module.REQUIRED_DOCS[1].path
            self.write_route_card(target)
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "No secrets.",
                    "Never include secrets.",
                ),
                encoding="utf-8",
            )
            self.assertEqual(module.validate(root), [])


if __name__ == "__main__":
    unittest.main()
