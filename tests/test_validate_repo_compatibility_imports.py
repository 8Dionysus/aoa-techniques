from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoCompatibilityImportTests(unittest.TestCase):
    def test_validate_repo_module_imports_without_pyyaml(self) -> None:
        spec = importlib.util.spec_from_file_location(
            "validate_repo_no_yaml_test", REPO_ROOT / "scripts" / "validate_repo.py"
        )
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        real_import = builtins.__import__

        def block_yaml_import(name: str, *args: object, **kwargs: object) -> object:
            if name == "yaml":
                raise ModuleNotFoundError("No module named 'yaml'")
            return real_import(name, *args, **kwargs)

        sys.modules[spec.name] = module
        try:
            with patch.object(builtins, "__import__", side_effect=block_yaml_import):
                spec.loader.exec_module(module)
        finally:
            sys.modules.pop(spec.name, None)

        self.assertTrue(hasattr(module, "parse_frontmatter"))


if __name__ == "__main__":
    unittest.main()
