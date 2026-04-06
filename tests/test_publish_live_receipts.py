from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "publish_live_receipts.py"


def load_module():
    spec = importlib.util.spec_from_file_location("publish_live_receipts", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def build_receipt(event_kind: str = "technique_promotion_receipt") -> dict:
    return {
        "event_kind": event_kind,
        "event_id": "evt-technique-001",
        "observed_at": "2026-04-06T20:05:00Z",
        "run_ref": "run-technique-001",
        "session_ref": "session:test-technique-closeout",
        "actor_ref": "aoa-techniques:promotion-wave",
        "object_ref": {
            "repo": "aoa-techniques",
            "kind": "technique",
            "id": "AOA-T-0089",
            "version": "main",
        },
        "evidence_refs": [
            {
                "kind": "technique_bundle",
                "ref": "repo:aoa-techniques/techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
            }
        ],
        "payload": {
            "promotion_state": "promoted",
            "source_ref": "repo:aoa-techniques/techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
        },
    }


class TechniquePublishLiveReceiptsTests(unittest.TestCase):
    def test_publish_live_receipts_appends_once_and_skips_duplicates(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            input_path = tmp_path / "receipt.json"
            log_path = tmp_path / "technique-receipts.jsonl"
            input_path.write_text(json.dumps(build_receipt(), indent=2) + "\n", encoding="utf-8")

            receipts = module.load_receipts([input_path])
            appended, skipped = module.append_new_receipts(log_path=log_path, receipts=receipts)
            self.assertEqual(appended, 1)
            self.assertEqual(skipped, 0)

            appended, skipped = module.append_new_receipts(log_path=log_path, receipts=receipts)
            self.assertEqual(appended, 0)
            self.assertEqual(skipped, 1)

    def test_publish_live_receipts_rejects_unsupported_event_kind(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            input_path = tmp_path / "receipt.json"
            input_path.write_text(
                json.dumps(build_receipt(event_kind="memo_writeback_receipt"), indent=2) + "\n",
                encoding="utf-8",
            )

            with self.assertRaises(module.ReceiptPublishError):
                module.load_receipts([input_path])


if __name__ == "__main__":
    unittest.main()
