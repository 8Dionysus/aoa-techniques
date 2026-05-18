from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts import technique_intelligence_surface as surface


REPO_ROOT = Path(__file__).resolve().parents[1]
BANNED_KEYS = {"activate", "activation", "invocation", "invoke", "invoked"}


def iter_keys(value: object) -> list[str]:
    keys: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            keys.append(key)
            keys.extend(iter_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.extend(iter_keys(child))
    return keys


class TechniqueIntelligenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.outputs = surface.build_all_outputs(REPO_ROOT)
        cls.registry = cls.outputs["registry"]
        cls.dag = cls.outputs["dag"]

    def test_registry_covers_current_corpus_as_attention_bounded_moves(self) -> None:
        ids = [entry["id"] for entry in self.registry["techniques"]]

        self.assertEqual(107, self.registry["technique_count"])
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("attention over source moves", self.registry["authority"])
        self.assertTrue(
            all(
                entry["move"]["unit"] == "attention_bounded_atomic_move"
                for entry in self.registry["techniques"]
            )
        )
        self.assertTrue(
            all(
                entry["topology"]["hints"]["authority"] == "scout_only_non_authoritative"
                for entry in self.registry["techniques"]
            )
        )

    def test_registry_uses_no_activation_shape_keys(self) -> None:
        self.assertTrue(BANNED_KEYS.isdisjoint(iter_keys(self.registry)))

    def test_registry_schema_accepts_generated_payload(self) -> None:
        schema = json.loads(
            (REPO_ROOT / "schemas/technique_intelligence_registry.schema.json").read_text(
                encoding="utf-8"
            )
        )

        Draft202012Validator(schema).validate(self.registry)

    def test_min_registry_is_projection(self) -> None:
        self.assertEqual(
            surface.project_min_registry_payload(self.registry),
            self.outputs["registry_min"],
        )

    def test_query_exact_id_and_explain_are_source_linked(self) -> None:
        result = surface.search_registry(self.registry, "AOA-T-0002 source truth layout", limit=3)
        self.assertEqual("AOA-T-0002", result["results"][0]["id"])
        self.assertTrue(result["results"][0]["matched_documents"])

        explanation = surface.explain_candidate(
            self.registry,
            "AOA-T-0002",
            intent="source truth docs conflict canonical guidance",
        )
        self.assertEqual("AOA-T-0002", explanation["technique_id"])
        self.assertTrue(explanation["fit_evidence"])
        self.assertIn("TECHNIQUE.md", explanation["next_load_refs"][0]["path"])
        self.assertIn("source bundle remains stronger", explanation["source_authority"].lower())

    def test_pack_profiles_preserve_stop_lines_and_fixture_refs(self) -> None:
        small_agent = surface.pack_candidate(self.registry, "AOA-T-0056", profile="small-agent")
        self.assertEqual("small-agent", small_agent["profile"])
        self.assertEqual("attention_bounded_atomic_move", small_agent["move"]["unit"])
        self.assertTrue(small_agent["fixture_refs"])
        self.assertIn("source bundle remains stronger", small_agent["authority"])

        handoff = surface.pack_candidate(self.registry, "AOA-T-0002", profile="workflow-handoff")
        self.assertIn("owner_boundaries", handoff)
        self.assertTrue(handoff["owner_boundaries"]["route_away"])

    def test_dag_schema_and_projection_keep_relations_as_hints(self) -> None:
        schema = json.loads(
            (REPO_ROOT / "schemas/technique_intelligence_dag.schema.json").read_text(
                encoding="utf-8"
            )
        )

        Draft202012Validator(schema).validate(self.dag)
        self.assertEqual(surface.project_min_dag_payload(self.dag), self.outputs["dag_min"])
        self.assertEqual(self.dag["node_count"], len(self.dag["nodes"]))
        self.assertEqual(self.dag["edge_count"], len(self.dag["edges"]))
        self.assertTrue(self.dag["relation_hints"])
        self.assertTrue(
            all(
                hint["authority"] == "frontmatter_direct_relation_not_dag_order"
                for hint in self.dag["relation_hints"]
            )
        )


if __name__ == "__main__":
    unittest.main()
