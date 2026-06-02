from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoQuestbookIntelligenceTests(unittest.TestCase):
    def test_work_quest_schema_lane_matches_yaml_source_route(self) -> None:
        schema = validate_repo.read_json(REPO_ROOT / "schemas" / "quest.schema.json")
        self.assertEqual(["techniques"], schema["properties"]["lane"]["enum"])

    def write_valid_surface(self, repo_root: Path) -> None:
        write_text(
            repo_root / "QUESTBOOK.md",
            (REPO_ROOT / "QUESTBOOK.md").read_text(encoding="utf-8"),
        )
        write_text(
            repo_root
            / "mechanics"
            / "growth-cycle"
            / "parts"
            / "questbook-integration"
            / "README.md",
            (
                REPO_ROOT
                / "mechanics"
                / "growth-cycle"
                / "parts"
                / "questbook-integration"
                / "README.md"
            ).read_text(encoding="utf-8"),
        )
        write_text(
            repo_root / "schemas" / "quest.schema.json",
            (REPO_ROOT / "schemas" / "quest.schema.json").read_text(encoding="utf-8"),
        )
        write_text(
            repo_root / "schemas" / "quest_dispatch.schema.json",
            (REPO_ROOT / "schemas" / "quest_dispatch.schema.json").read_text(encoding="utf-8"),
        )
        for relative_path in (
            "quests/README.md",
            "quests/AGENTS.md",
            "quests/techniques/README.md",
            "quests/techniques/AGENTS.md",
            "quests/agon/README.md",
            "quests/agon/AGENTS.md",
        ):
            write_text(
                repo_root / relative_path,
                (REPO_ROOT / relative_path).read_text(encoding="utf-8"),
            )
        for quest_path in sorted((REPO_ROOT / "quests").glob("*/*/*")):
            if not quest_path.is_file() or quest_path.suffix not in {".yaml", ".md"}:
                continue
            relative_path = quest_path.relative_to(REPO_ROOT)
            write_text(
                repo_root / relative_path,
                quest_path.read_text(encoding="utf-8"),
            )
        write_text(
            repo_root / "generated" / "quest_catalog.min.json",
            (REPO_ROOT / "generated" / "quest_catalog.min.json").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "generated" / "quest_dispatch.min.json",
            (REPO_ROOT / "generated" / "quest_dispatch.min.json").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "generated" / "quest_catalog.min.example.json",
            (REPO_ROOT / "generated" / "quest_catalog.min.example.json").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "generated" / "quest_dispatch.min.example.json",
            (REPO_ROOT / "generated" / "quest_dispatch.min.example.json").read_text(
                encoding="utf-8"
            ),
        )

    def test_valid_questbook_surface_passes(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)

            validate_repo.validate_questbook_surface(repo_root)

    def test_missing_lane_agents_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            (repo_root / "quests" / "agon" / "AGENTS.md").unlink()

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quests/agon/AGENTS.md: missing required file",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_additive_second_wave_quest_is_projected(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)

            catalog_ids = [
                entry["id"] for entry in validate_repo.build_quest_catalog_projection(repo_root)
            ]
            dispatch_ids = [
                entry["id"] for entry in validate_repo.build_quest_dispatch_projection(repo_root)
            ]

        self.assertIn("AOA-TECH-Q-0005", catalog_ids)
        self.assertIn("AOA-TECH-Q-0005", dispatch_ids)

    def test_missing_quest_file_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            (
                repo_root
                / "quests"
                / "techniques"
                / "captured"
                / "AOA-TECH-Q-0003.yaml"
            ).unlink()

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "AOA-TECH-Q-0003.yaml: missing required file",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_wrong_repo_value_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            quest_path = repo_root / "quests" / "techniques" / "done" / "AOA-TECH-Q-0002.yaml"
            write_text(
                quest_path,
                quest_path.read_text(encoding="utf-8").replace(
                    "repo: aoa-techniques",
                    "repo: aoa-skills",
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "repo must be 'aoa-techniques'",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_invalid_harvest_target_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            quest_path = (
                repo_root
                / "quests"
                / "techniques"
                / "captured"
                / "AOA-TECH-Q-0005.yaml"
            )
            write_text(
                quest_path,
                quest_path.read_text(encoding="utf-8").replace(
                    "target: technique",
                    "target: generated_surface",
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "harvest.target must be one of",
            ):
                validate_repo.build_quest_dispatch_projection(repo_root)

    def test_dispatch_example_drift_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "generated" / "quest_dispatch.min.example.json",
                (repo_root / "generated" / "quest_dispatch.min.example.json")
                .read_text(encoding="utf-8")
                .replace(
                    '"source_path": "quests/techniques/captured/AOA-TECH-Q-0004.yaml"',
                    '"source_path": "quests/techniques/captured/AOA-TECH-Q-9999.yaml"',
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "example dispatch must stay aligned",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_missing_live_catalog_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            (repo_root / "generated" / "quest_catalog.min.json").unlink()

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quest_catalog.min.json: missing required file",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_fixture_live_catalog_drift_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "generated" / "quest_catalog.min.example.json",
                (repo_root / "generated" / "quest_catalog.min.example.json")
                .read_text(encoding="utf-8")
                .replace(
                    '"source_path": "quests/techniques/captured/AOA-TECH-Q-0004.yaml"',
                    '"source_path": "quests/techniques/captured/AOA-TECH-Q-9999.yaml"',
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "example catalog must stay aligned",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_live_dispatch_drift_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "generated" / "quest_dispatch.min.json",
                (repo_root / "generated" / "quest_dispatch.min.json")
                .read_text(encoding="utf-8")
                .replace(
                    '"source_path":"quests/techniques/captured/AOA-TECH-Q-0004.yaml"',
                    '"source_path":"quests/techniques/captured/AOA-TECH-Q-9999.yaml"',
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quest_dispatch.min.json: dispatch entry 'AOA-TECH-Q-0004' must stay aligned",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_missing_activation_fails_with_validation_error(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            quest_path = repo_root / "quests" / "techniques" / "done" / "AOA-TECH-Q-0001.yaml"
            quest_text = quest_path.read_text(encoding="utf-8")
            write_text(
                quest_path,
                quest_text[: quest_text.index("activation:")]
                + quest_text[quest_text.index("anchor_ref:") :],
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quests/techniques/done/AOA-TECH-Q-0001.yaml: quest must define object field 'activation'",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_root_level_quest_alias_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            source = (
                repo_root
                / "quests"
                / "techniques"
                / "captured"
                / "AOA-TECH-Q-0003.yaml"
            )
            write_text(
                repo_root / "quests" / "AOA-TECH-Q-0003.yaml",
                source.read_text(encoding="utf-8"),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "root-level quest aliases are not allowed",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_markdown_quest_contract_is_required(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            quest_path = (
                repo_root
                / "quests"
                / "agon"
                / "captured"
                / "AOT-Q-AGON-0002-epistemic-technique-candidates.md"
            )
            write_text(
                quest_path,
                quest_path.read_text(encoding="utf-8").replace(
                    "source_contract: quest_markdown_contract_v1\n\n",
                    "",
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "missing source_contract: quest_markdown_contract_v1",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_live_dispatch_optional_field_must_match_schema(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            dispatch_path = repo_root / "generated" / "quest_dispatch.min.json"
            dispatch_payload = json.loads(dispatch_path.read_text(encoding="utf-8"))
            dispatch_payload[0]["fallback_tier"] = None
            write_text(dispatch_path, json.dumps(dispatch_payload, indent=2) + "\n")

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "generated/quest_dispatch.min.json\\[0\\]\\.fallback_tier: value must be a string",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_example_dispatch_optional_field_must_match_schema(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            dispatch_path = repo_root / "generated" / "quest_dispatch.min.example.json"
            dispatch_payload = json.loads(dispatch_path.read_text(encoding="utf-8"))
            dispatch_payload[0]["wrapper_class"] = None
            write_text(dispatch_path, json.dumps(dispatch_payload, indent=2) + "\n")

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "generated/quest_dispatch.min.example.json\\[0\\]\\.wrapper_class: value must be a string",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_example_payload_matches_feat_schema(self) -> None:
        schema = json.loads(
            (REPO_ROOT / "schemas" / "technique_feat_catalog.schema.json").read_text(
                encoding="utf-8"
            )
        )
        payload = json.loads(
            (REPO_ROOT / "generated" / "technique_feat_cards.min.example.json").read_text(
                encoding="utf-8"
            )
        )

        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(payload)


if __name__ == "__main__":
    unittest.main()
