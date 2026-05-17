from __future__ import annotations

import re
import unittest
from urllib.parse import unquote
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCAL_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class DocsSurfaceGuardrailsTestCase(unittest.TestCase):
    def test_current_surface_index_covers_flat_docs_markdown(self) -> None:
        index = (REPO_ROOT / "docs" / "guardrails" / "CURRENT_SURFACE_INDEX.md").read_text(
            encoding="utf-8"
        )

        flat_docs = sorted((REPO_ROOT / "docs").glob("*.md"))
        self.assertGreater(len(flat_docs), 0)
        for path in flat_docs:
            relative = path.relative_to(REPO_ROOT).as_posix()
            with self.subTest(surface=relative):
                self.assertIn(f"`{relative}`", index)

    def test_active_root_and_docs_markdown_links_resolve(self) -> None:
        markdown_files = (
            sorted(REPO_ROOT.glob("*.md"))
            + sorted((REPO_ROOT / "docs").rglob("*.md"))
            + sorted((REPO_ROOT / "examples").rglob("*.md"))
        )
        self.assertGreater(len(markdown_files), 0)

        for path in markdown_files:
            relative = path.relative_to(REPO_ROOT).as_posix()
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                for target in LOCAL_LINK_PATTERN.findall(line):
                    if (
                        "://" in target
                        or target.startswith("#")
                        or target.startswith("mailto:")
                    ):
                        continue
                    target_path = target.split("#", 1)[0].strip()
                    if not target_path:
                        continue
                    if target_path.startswith("<") and target_path.endswith(">"):
                        target_path = target_path[1:-1]
                    target_path = unquote(target_path)
                    resolved = (path.parent / target_path).resolve()
                    with self.subTest(
                        surface=relative, line=line_number, target=target
                    ):
                        self.assertTrue(
                            resolved == REPO_ROOT or REPO_ROOT in resolved.parents
                        )
                        self.assertTrue(resolved.exists())

    def test_generated_readers_have_named_districts(self) -> None:
        index = (REPO_ROOT / "docs" / "guardrails" / "CURRENT_SURFACE_INDEX.md").read_text(
            encoding="utf-8"
        )
        protocol = (
            REPO_ROOT / "docs" / "guardrails" / "THEMATIC_DISTRICT_PROTOCOL.md"
        ).read_text(encoding="utf-8")

        for target in (
            "docs/source-lift/",
            "docs/review/",
            "docs/selection/",
            "docs/readers/",
            "docs/readers/source-lift/",
            "docs/readers/kind/",
            "docs/readers/repo/",
            "docs/readers/review/",
            "docs/readers/selection/",
            "docs/readers/runtime/",
            "TECHNIQUE_SECTIONS.md",
            "EVIDENCE_NOTE_SURFACES.md",
            "TECHNIQUE_KINDS.md",
            "TECHNIQUE_CAPSULES.md",
            "REPO_DOC_SURFACES.md",
            "SHADOW_PATTERNS.md",
            "TECHNIQUE_SELECTION.md",
            "SELECTION_PATTERNS.md",
            "KAG_SOURCE_LIFT_GUIDE.md",
            "TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "EVIDENCE_NOTE_PROVENANCE_GUIDE.md",
            "CANONICAL_RUBRIC.md",
            "CANONICAL_REVIEW_GUIDE.md",
            "SEMANTIC_REVIEW_GUIDE.md",
            "TECHNIQUE_SHADOW_GUIDE.md",
            "TECHNIQUE_SELECTION_GUIDE.md",
            "TECHNIQUE_KIND_GUIDE.md",
            "TECHNIQUE_KIND_HANDOFF_PACK.md",
            "TECHNIQUE_CAPSULE_GUIDE.md",
            "LINK_AND_SHAPE_HYGIENE_PROTOCOL.md",
            "HYGIENE_GUARDRAIL_INDEX.md",
        ):
            with self.subTest(target=target):
                self.assertIn(target, index + protocol)

    def test_thematic_protocol_names_owner_homes_and_generated_reader_limits(self) -> None:
        protocol = (
            REPO_ROOT / "docs" / "guardrails" / "THEMATIC_DISTRICT_PROTOCOL.md"
        ).read_text(encoding="utf-8")

        for target in (
            "legacy/receipts/",
            "mechanics/<slug>/",
            "generated/",
            "techniques/**/",
            "Generated JSON belongs in `generated/`",
            "Generated Markdown readers are not source authority",
            "KAG/source-lift guide contracts belong in `docs/source-lift/`",
            "Review, maturity, semantic-review, and shadow/caution guide contracts belong in",
            "Selection, kind, handoff, and capsule guide contracts belong in",
        ):
            with self.subTest(target=target):
                self.assertIn(target, protocol)

    def test_tree_contract_is_not_a_full_migration_ledger(self) -> None:
        tree_contract = (REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("legacy/receipts/", tree_contract)
        self.assertIn("final-tree-migration-ledger.md", tree_contract)
        self.assertNotIn("The first pilot migration moves", tree_contract)
        self.assertNotIn("The twenty-eighth pilot migration moves", tree_contract)

    def test_root_examples_are_indexed_and_not_root_markdown(self) -> None:
        self.assertFalse((REPO_ROOT / "WALKTHROUGH.md").exists())

        examples_readme = (REPO_ROOT / "examples" / "README.md").read_text(
            encoding="utf-8"
        )
        required_sections = (
            "## Source Surfaces",
            "## Demonstrates",
            "## Boundary",
            "## Checks",
            "## Closeout",
        )

        for path in sorted((REPO_ROOT / "examples").glob("*.md")):
            if path.name in {"AGENTS.md", "README.md"}:
                continue
            relative_name = path.name
            body = path.read_text(encoding="utf-8")
            with self.subTest(example=relative_name):
                self.assertIn(relative_name, examples_readme)
                for section in required_sections:
                    self.assertIn(section, body)

    def test_decisions_readme_indexes_all_decision_records(self) -> None:
        decisions_readme = (REPO_ROOT / "docs" / "decisions" / "README.md").read_text(
            encoding="utf-8"
        )

        for path in sorted((REPO_ROOT / "docs" / "decisions").glob("*.md")):
            if path.name in {"AGENTS.md", "README.md", "TEMPLATE.md"}:
                continue
            with self.subTest(decision=path.name):
                self.assertIn(f"]({path.name})", decisions_readme)

    def test_docs_entrypoints_route_to_mechanics_without_part_runbook_index(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        mechanics_readme = (REPO_ROOT / "mechanics" / "README.md").read_text(
            encoding="utf-8"
        )

        for surface_name, content in (
            ("docs/README.md", docs_readme),
            ("docs/START_HERE.md", start_here),
        ):
            with self.subTest(surface=surface_name, route="mechanics-atlas"):
                self.assertIn("mechanics/README.md", content)
            for forbidden in (
                "## Mechanic Evidence Routes",
                "External Evidence Sprint Runbook",
                "External Evidence Ledger",
                "External Import Runbook",
                "External Technique Candidates",
                "Cross-Layer Technique Candidates",
                "Agon Move Technique Bridge",
                "Chaos Stress Program",
                "Recovery Practice Bridge",
                "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
                "mechanics/agon/parts/move-technique-bridge/README.md",
            ):
                with self.subTest(surface=surface_name, forbidden=forbidden):
                    self.assertNotIn(forbidden, content)

        for expected in (
            "External Evidence Sprint Runbook",
            "External Evidence Ledger",
            "External Import Runbook",
            "External Technique Candidates",
            "Cross-Layer Technique Candidates",
            "Agon Move Technique Bridge",
            "Chaos Stress Program",
            "Recovery Practice Bridge",
            "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
            "mechanics/agon/parts/move-technique-bridge/README.md",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, mechanics_readme)


if __name__ == "__main__":
    unittest.main()
