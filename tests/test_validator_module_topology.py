from __future__ import annotations

import ast
import importlib
import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATE_REPO_PATH = REPO_ROOT / "scripts" / "validate_repo.py"
VALIDATORS_DIR = REPO_ROOT / "scripts" / "validators"
INVENTORY_PATH = REPO_ROOT / "docs" / "validation" / "validator_inventory.json"

OWNER_MODULES = {
    "scripts/validators/common.py",
    "scripts/validators/source_contracts.py",
    "scripts/validators/projection_parity.py",
    "scripts/validators/projection_catalog.py",
    "scripts/validators/projection_decisions.py",
    "scripts/validators/projection_agents_mesh.py",
    "scripts/validators/projection_mechanics.py",
    "scripts/validators/projection_kag.py",
    "scripts/validators/projection_intelligence.py",
    "scripts/validators/questbook.py",
    "scripts/validators/public_hygiene.py",
    "scripts/validators/orchestrator.py",
}
ADAPTER_MODULES = {
    "scripts/validate_repo.py",
    "scripts/validators/__init__.py",
}
SOURCE_RULE_FUNCTIONS = {
    "collect_techniques",
    "validate_frontmatter_schema",
    "validate_kind_axis_alignment",
    "validate_technique_bundle",
    "validate_index",
    "validate_evidence",
    "validate_relations",
}
PROJECTION_RULE_FUNCTIONS = {
    "validate_catalogs",
    "validate_capsules",
    "validate_section_manifests",
    "validate_github_review_template_manifests",
    "validate_kind_manifests",
}
PROJECTION_GROUP_MODULES = {
    "catalog": "scripts/validators/projection_catalog.py",
    "decisions": "scripts/validators/projection_decisions.py",
    "agents_mesh": "scripts/validators/projection_agents_mesh.py",
    "mechanics_projections": "scripts/validators/projection_mechanics.py",
    "kag_export": "scripts/validators/projection_kag.py",
    "technique_intelligence": "scripts/validators/projection_intelligence.py",
    "questbook": "scripts/validators/questbook.py",
    "public_hygiene": "scripts/validators/public_hygiene.py",
}


def load_inventory() -> dict:
    return json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))


def module_ast(relative_path: str) -> ast.Module:
    return ast.parse((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


def defined_names(relative_path: str) -> set[str]:
    tree = module_ast(relative_path)
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }


class ValidatorModuleTopologyTests(unittest.TestCase):
    def test_validate_repo_is_thin_compatibility_adapter(self) -> None:
        text = VALIDATE_REPO_PATH.read_text(encoding="utf-8")
        tree = ast.parse(text)

        self.assertLessEqual(len(text.splitlines()), 12)
        self.assertEqual(set(), defined_names("scripts/validate_repo.py"))
        self.assertNotIn("def validate_", text)
        self.assertNotIn("REQUIRED_SECTIONS", text)
        self.assertNotIn("generated catalog parity", text)

        imports_validators = any(
            isinstance(node, ast.Try)
            and any(
                isinstance(child, ast.ImportFrom)
                and child.module in {"scripts.validators", "validators"}
                for block in (node.body, node.handlers[0].body if node.handlers else [])
                for child in block
            )
            for node in tree.body
        )
        self.assertTrue(imports_validators)
        self.assertIn("raise SystemExit(main())", text)

    def test_validator_package_init_is_reexport_adapter_only(self) -> None:
        text = (VALIDATORS_DIR / "__init__.py").read_text(encoding="utf-8")

        self.assertLessEqual(len(text.splitlines()), 11)
        self.assertEqual(set(), defined_names("scripts/validators/__init__.py"))
        self.assertNotIn("def validate_", text)
        self.assertIn("from .orchestrator import *", text)

    def test_inventory_covers_every_validator_module_and_no_orphans(self) -> None:
        inventory = load_inventory()
        module_entries = inventory["validator_modules"]
        inventory_paths = {entry["path"] for entry in module_entries}
        discovered_paths = {
            path.relative_to(REPO_ROOT).as_posix()
            for path in VALIDATORS_DIR.glob("*.py")
            if path.name != "__init__.py"
        }

        self.assertEqual(OWNER_MODULES, discovered_paths)
        self.assertEqual(
            OWNER_MODULES | {"scripts/validate_repo.py", "scripts/validators/__init__.py"},
            inventory_paths,
        )
        for relative_path in inventory_paths | ADAPTER_MODULES:
            with self.subTest(path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_inventory_module_owners_are_unique_and_bounded(self) -> None:
        inventory = load_inventory()
        module_entries = inventory["validator_modules"]
        owners = [entry["owner"] for entry in module_entries]
        owned_rules = [
            rule for entry in module_entries for rule in entry.get("owns", ())
        ]

        self.assertEqual(len(owners), len(set(owners)))
        self.assertEqual(len(owned_rules), len(set(owned_rules)))
        for entry in module_entries:
            with self.subTest(path=entry["path"]):
                self.assertIn("module_type", entry)
                self.assertTrue(entry.get("owns"))
                self.assertTrue(entry.get("does_not_own"))

    def test_owner_modules_import_cleanly(self) -> None:
        for relative_path in OWNER_MODULES:
            module_name = relative_path.removesuffix(".py").replace("/", ".")
            with self.subTest(module=module_name):
                importlib.import_module(module_name)

    def test_rule_definitions_are_not_duplicated_across_owner_modules(self) -> None:
        seen: dict[str, str] = {}
        duplicates: dict[str, list[str]] = {}

        for relative_path in sorted(OWNER_MODULES):
            for name in defined_names(relative_path):
                if name in seen:
                    duplicates.setdefault(name, [seen[name]]).append(relative_path)
                else:
                    seen[name] = relative_path

        self.assertEqual({}, duplicates)

    def test_source_and_projection_rule_ownership_is_separate(self) -> None:
        source_defs = defined_names("scripts/validators/source_contracts.py")
        catalog_defs = defined_names("scripts/validators/projection_catalog.py")
        kag_defs = defined_names("scripts/validators/projection_kag.py")
        intelligence_defs = defined_names("scripts/validators/projection_intelligence.py")

        self.assertTrue(SOURCE_RULE_FUNCTIONS <= source_defs)
        self.assertTrue(PROJECTION_RULE_FUNCTIONS <= catalog_defs)
        self.assertIn("validate_kag_export", kag_defs)
        self.assertIn("validate_technique_intelligence", intelligence_defs)
        for projection_path in PROJECTION_GROUP_MODULES.values():
            with self.subTest(projection_path=projection_path):
                self.assertFalse(SOURCE_RULE_FUNCTIONS & defined_names(projection_path))
        self.assertFalse(PROJECTION_RULE_FUNCTIONS & source_defs)

    def test_generated_validator_modules_are_projection_only_not_source_meaning(self) -> None:
        inventory = load_inventory()
        entries_by_path = {entry["path"]: entry for entry in inventory["validator_modules"]}

        for group_id, module_path in PROJECTION_GROUP_MODULES.items():
            with self.subTest(group_id=group_id, module_path=module_path):
                entry = entries_by_path[module_path]
                self.assertEqual(group_id, entry["group_id"])
                if entry["module_type"] == "projection":
                    self.assertTrue(entry["projection_only"])
                self.assertNotIn("technique bundle meaning", entry["owns"])
                self.assertNotIn("frontmatter truth axes", entry["owns"])

    def test_generated_lane_groups_match_projection_inventory(self) -> None:
        inventory = load_inventory()
        lanes = json.loads(
            (REPO_ROOT / "config" / "validation_lanes.json").read_text(encoding="utf-8")
        )
        groups = lanes["command_groups"]["generated_check"]
        group_modules = {group["id"]: group["owner_module"] for group in groups}
        inventory_modules = {
            entry["group_id"]: entry["path"]
            for entry in inventory["validator_modules"]
            if "group_id" in entry
        }

        self.assertEqual(PROJECTION_GROUP_MODULES, group_modules)
        self.assertEqual(PROJECTION_GROUP_MODULES, inventory_modules)
        self.assertEqual(
            [
                "decisions",
                "agents_mesh",
                "catalog",
                "mechanics_projections",
                "kag_export",
                "technique_intelligence",
                "questbook",
                "public_hygiene",
            ],
            [group["id"] for group in groups],
        )

    def test_validator_owner_route_card_is_registered_in_agents_mesh(self) -> None:
        route_card = REPO_ROOT / "scripts" / "validators" / "AGENTS.md"
        agents_mesh = json.loads(
            (REPO_ROOT / "config" / "agents_mesh.json").read_text(encoding="utf-8")
        )

        self.assertTrue(route_card.is_file())
        self.assertIn("scripts/validators/AGENTS.md", agents_mesh["canonical_cards"])


if __name__ == "__main__":
    unittest.main()
