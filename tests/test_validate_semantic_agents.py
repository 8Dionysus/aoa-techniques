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
    def test_repository_semantic_docs_validate(self) -> None:
        module = load_validator()
        self.assertEqual(module.validate(REPO_ROOT), [])

    def test_missing_required_doc_fails(self) -> None:
        module = load_validator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for spec in module.REQUIRED_DOCS:
                path = root / spec.path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# AGENTS.md\n" + "\n".join(spec.required_snippets) + "\n", encoding="utf-8")
            missing = root / module.REQUIRED_DOCS[0].path
            missing.unlink()
            issues = module.validate(root)
        self.assertTrue(any("file is missing" in issue for issue in issues))

    def test_missing_required_snippet_fails(self) -> None:
        module = load_validator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for spec in module.REQUIRED_DOCS:
                path = root / spec.path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# AGENTS.md\n" + "\n".join(spec.required_snippets) + "\n", encoding="utf-8")
            target_spec = module.REQUIRED_DOCS[0]
            target = root / target_spec.path
            first_snippet = target_spec.required_snippets[0]
            target.write_text("# AGENTS.md\n" + "\n".join(target_spec.required_snippets[1:]) + "\n", encoding="utf-8")
            issues = module.validate(root)
        self.assertTrue(any(first_snippet in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
