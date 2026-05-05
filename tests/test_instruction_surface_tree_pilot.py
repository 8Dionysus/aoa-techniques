from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0012",
        "deterministic-context-composition",
        "composition",
        "techniques/docs/deterministic-context-composition",
        "techniques/instruction/instruction-surface/deterministic-context-composition",
    ),
    (
        "AOA-T-0013",
        "single-source-rule-distribution",
        "distribution",
        "techniques/docs/single-source-rule-distribution",
        "techniques/instruction/instruction-surface/single-source-rule-distribution",
    ),
    (
        "AOA-T-0024",
        "upstream-mirroring-with-provenance",
        "distribution",
        "techniques/docs/upstream-mirroring-with-provenance",
        "techniques/instruction/instruction-surface/upstream-mirroring-with-provenance",
    ),
    (
        "AOA-T-0027",
        "cross-agent-skill-propagation",
        "distribution",
        "techniques/docs/cross-agent-skill-propagation",
        "techniques/instruction/instruction-surface/cross-agent-skill-propagation",
    ),
    (
        "AOA-T-0029",
        "nested-rule-loading",
        "composition",
        "techniques/docs/nested-rule-loading",
        "techniques/instruction/instruction-surface/nested-rule-loading",
    ),
    (
        "AOA-T-0030",
        "fragmented-agent-context",
        "composition",
        "techniques/docs/fragmented-agent-context",
        "techniques/instruction/instruction-surface/fragmented-agent-context",
    ),
    (
        "AOA-T-0035",
        "profile-preset-composition",
        "composition",
        "techniques/docs/profile-preset-composition",
        "techniques/instruction/instruction-surface/profile-preset-composition",
    ),
)

LIVE_LINK_SURFACES = (
    "docs/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md",
    "mechanics/audit/parts/external-evidence-ledger/README.md",
    "mechanics/audit/parts/promotion-wave-a-runbook/README.md",
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/config/cross_layer_candidate_registry.seed.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/examples/cross_layer_candidate_registry_entry.example.json",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "mechanics/distillation/parts/long-gap-reentry/README.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class InstructionSurfaceTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_instruction_tree(self) -> None:
        for technique_id, slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, kind, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual("docs", frontmatter["domain"])
                self.assertEqual(kind, frontmatter["kind"])
                self.assertNotIn("tree_path", frontmatter)

    def test_instruction_trunk_has_route_card(self) -> None:
        text = (REPO_ROOT / "techniques" / "instruction" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = " ".join(text.split())

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("instruction-surface", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)
        self.assertIn("generated context authority", flat_text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-instruction-surface-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("AoA constitutional law", receipt)
        self.assertIn("runtime role law", receipt)
        self.assertIn("generated context authority", receipt)

    def test_live_links_point_to_current_paths(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LIVE_LINK_SURFACES
        )

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", text)
                self.assertNotIn(f"{old_path}/TECHNIQUE.md", text)

    def test_review_sources_point_to_current_paths_but_keep_pilot_accounting(self) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "instruction-surface-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review)
                self.assertIn(old_path, review)
                self.assertIn(new_path, review)


if __name__ == "__main__":
    unittest.main()
