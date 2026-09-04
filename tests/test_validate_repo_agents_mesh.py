from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoAgentsMeshTests(unittest.TestCase):
    def test_active_mesh_source_has_no_retired_spark_card(self) -> None:
        self.assertTrue((REPO_ROOT / "config" / "agents_mesh.json").is_file())
        self.assertFalse((REPO_ROOT / ".agents" / "spark").exists())
if __name__ == "__main__":
    unittest.main()
