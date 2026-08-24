from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator

from scripts import validate_abyss_machine_kag_export_bundle as kag_bundle_validator
from scripts import validate_repo


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = REPO_ROOT / "generated"
SCHEMAS_DIR = REPO_ROOT / "schemas"


def load_json(relative_path: str) -> dict:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


class DownstreamFeedContractsTests(unittest.TestCase):
    def assert_router_safe_doc_path(self, doc_path: str) -> None:
        parts = PurePosixPath(doc_path).parts
        self.assertFalse(PurePosixPath(doc_path).is_absolute())
        self.assertNotIn("..", parts)
        self.assertTrue(doc_path.startswith("docs/") or ("/" not in doc_path and doc_path.endswith(".md")))

    def test_expected_downstream_feeds_exist(self) -> None:
        for relative_path in (
            "generated/technique_catalog.min.json",
            "generated/technique_kind_manifest.min.json",
            "generated/technique_promotion_readiness.min.json",
            "generated/technique_capsules.json",
            "generated/technique_sections.full.json",
            "generated/repo_doc_surface_manifest.min.json",
            "generated/technique_feat_cards.min.example.json",
            "generated/kag_export.json",
            "generated/kag_export.min.json",
            "schemas/technique_feat_catalog.schema.json",
        ):
            with self.subTest(path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_catalog_capsules_and_sections_share_ids_and_paths(self) -> None:
        catalog = load_json("generated/technique_catalog.min.json")
        capsules = load_json("generated/technique_capsules.json")
        sections = load_json("generated/technique_sections.full.json")

        catalog_pairs = [
            (entry["id"], entry["technique_path"]) for entry in catalog["techniques"]
        ]
        capsule_pairs = [
            (entry["id"], entry["technique_path"]) for entry in capsules["techniques"]
        ]
        section_pairs = [
            (entry["id"], entry["technique_path"]) for entry in sections["techniques"]
        ]

        self.assertEqual(catalog["catalog_version"], 1)
        self.assertEqual(capsules["capsule_version"], 1)
        self.assertEqual(sections["section_version"], 1)
        self.assertEqual(catalog["source_of_truth"], "markdown-frontmatter-v2")
        self.assertEqual(
            capsules["source_of_truth"],
            "frontmatter-summary+markdown-technique-capsules-v1",
        )
        self.assertEqual(
            sections["source_of_truth"]["technique_markdown"],
            "techniques/**/TECHNIQUE.md",
        )
        self.assertIn("sections", sections["source_of_truth"])
        self.assertEqual(catalog_pairs, capsule_pairs)
        self.assertEqual(catalog_pairs, section_pairs)

        for entry in catalog["techniques"]:
            self.assertIn("kind", entry)
            self.assertIn("summary", entry)
            self.assertIn("validation_strength", entry)
            self.assertIn("review_required", entry)

    def test_promotion_readiness_surface_tracks_canonical_and_promoted_corpus(self) -> None:
        catalog = load_json("generated/technique_catalog.min.json")
        readiness = load_json("generated/technique_promotion_readiness.min.json")

        self.assertEqual(readiness["schema_version"], 1)
        self.assertEqual(readiness["layer"], "aoa-techniques")
        self.assertEqual(readiness["scope"], "published-non-deprecated")
        self.assertEqual(
            readiness["source_of_truth"],
            {
                "catalog": "generated/technique_catalog.min.json",
                "bundles": "techniques/**/TECHNIQUE.md",
                "canonical_readiness_note": "notes/canonical-readiness.md",
                "adverse_effects_review": "notes/adverse-effects-review.md",
            },
        )

        scoped_catalog = [
            (entry["id"], entry["name"], entry["status"])
            for entry in catalog["techniques"]
            if entry["status"] in {"canonical", "promoted"}
        ]
        readiness_entries = [
            (entry["technique_id"], entry["technique_name"], entry["status"])
            for entry in readiness["techniques"]
        ]
        self.assertEqual(readiness_entries, scoped_catalog)
        self.assertTrue(all(isinstance(entry["blockers"], list) for entry in readiness["techniques"]))
        self.assertTrue(
            all(entry["readiness_passed"] == (len(entry["blockers"]) == 0) for entry in readiness["techniques"])
        )

    def test_kag_export_carries_artifact_identity_contract(self) -> None:
        full = load_json("generated/kag_export.json")
        compact = load_json("generated/kag_export.min.json")

        self.assertEqual(full, compact)
        self.assertEqual(full["artifact_identity"], validate_repo.KAG_EXPORT_ARTIFACT_IDENTITY)

        identity = full["artifact_identity"]
        self.assertEqual(identity["artifact_class"], "source_owned_kag_export_capsule")
        self.assertEqual(identity["owner_repo"], "aoa-techniques")
        self.assertEqual(
            identity["authority_ref"],
            "techniques/instruction/capability-boundary/"
            "multi-source-primary-input-provenance/TECHNIQUE.md",
        )
        self.assertEqual(
            identity["trust_layer"],
            [
                "abi_contract_signature",
                "w3c_prov_lineage",
                "slsa_in_toto_provenance",
                "materialized_subject_store",
                "fail_closed_consumer_trust_gate",
            ],
        )
        self.assertIn("machine-local runtime state", identity["privacy_boundary"])
        self.assertIn("KAG substrate authority", identity["privacy_boundary"])
        self.assertIn("generated/kag_export.min.json", identity["content_identity"])
        self.assertIn("exact landed commit:<40-hex-git-SHA>", identity["consumer_expectation"])
        self.assertIn("host_managed trust", identity["consumer_expectation"])
        self.assertIn("consumer trust-gate allow/latest", identity["consumer_expectation"])
        self.assertIn(
            "python scripts/validate_abyss_machine_kag_export_bundle.py --source-ref commit:<EXACT_LANDED_RELEASE_COMMIT> --json",
            identity["verification"],
        )

    def test_kag_export_artifact_bundle_requires_trust_gate_subject_store_and_slsa(self) -> None:
        manifest = load_json("docs/source-lift/artifact-bundles/kag_export.bundle.json")

        self.assertEqual(manifest["schema"], "abyss_machine_artifact_bundle_manifest_v1")
        self.assertEqual(manifest["artifact_class"], "source_owned_kag_export_capsule")
        self.assertEqual(manifest["owner_repo"], "aoa-techniques")
        self.assertTrue(manifest["public_safe"])
        self.assertEqual(manifest["artifact_identity"]["abi_epoch"], "aoa_techniques_kag_export_v1")
        self.assertEqual(manifest["abi_subject"]["path"], "generated/kag_export.min.json")
        self.assertIn(
            {"path": "generated/kag_export.min.json", "role": "kag_export_capsule"},
            manifest["artifact_subjects"],
        )
        self.assertIn(
            {"path": "scripts/validators/projection_kag.py", "role": "validator"},
            manifest["artifact_subjects"],
        )
        self.assertEqual(manifest["lifecycle"]["initial_state"], "candidate")
        self.assertIn("release-ready", manifest["lifecycle"]["promotion_path"])
        self.assertIn("revoked", manifest["lifecycle"]["promotion_path"])
        self.assertTrue(manifest["consumer_contract"]["registry_required"])
        self.assertIn("SLSA/in-toto generation provenance", manifest["consumer_contract"]["consumer_expectation"])
        self.assertIn("durable evidence promotion", manifest["consumer_contract"]["consumer_expectation"])
        self.assertIn("materialized subject-store verification", manifest["consumer_contract"]["consumer_expectation"])
        self.assertIn("source/trust-root matching", manifest["consumer_contract"]["consumer_expectation"])
        self.assertIn("does not define KAG substrate behavior", manifest["consumer_contract"]["consumer_expectation"])
        self.assertIn("trust-gate", manifest["consumer_contract"]["stable_interface"])
        self.assertTrue(manifest["consumer_contract"]["subject_store_required"])
        self.assertEqual(manifest["consumer_contract"]["admission_gate"], "fail_closed_consumer_admission")
        self.assertEqual(manifest["consumer_contract"]["consumer_verdict"], "allow_or_deny_required_before_use")
        self.assertTrue(
            any("evidence-promote" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("materialize-subjects" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("--store-root SUBJECT_STORE_ROOT" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("trust-gate" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("registry-latest" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("--source-repo aoa-techniques" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("--source-ref commit:<EXACT_LANDED_RELEASE_COMMIT>" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )
        self.assertTrue(
            any("--trust-root-mode host_managed" in command for command in manifest["consumer_command"]),
            manifest["consumer_command"],
        )

    def test_kag_artifact_source_ref_is_exact_checked_out_commit(self) -> None:
        source_ref = kag_bundle_validator._exact_git_source_ref(REPO_ROOT)
        self.assertRegex(source_ref, r"^commit:[0-9a-f]{40}$")
        with self.assertRaisesRegex(ValueError, "does not match"):
            kag_bundle_validator._resolve_source_ref("commit:" + ("0" * 40))

    def test_kag_artifact_subject_store_root_rejects_empty_or_repo_root(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-empty path"):
            kag_bundle_validator._resolve_subject_store_root("")
        with self.assertRaisesRegex(ValueError, "repository root"):
            kag_bundle_validator._resolve_subject_store_root(".")
        with self.assertRaisesRegex(ValueError, "repository root"):
            kag_bundle_validator._resolve_subject_store_root(REPO_ROOT)

    def test_kag_artifact_subject_store_scope_restores_owner_state(self) -> None:
        class FakeArtifactBundles:
            DEFAULT_ARTIFACT_SUBJECT_STORE_ROOT = Path("/ambient/subject-store")

        names = kag_bundle_validator.SUBJECT_STORE_ENV_NAMES
        previous_env = {name: os.environ.get(name) for name in names}
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "isolated"
            try:
                with kag_bundle_validator._subject_store_scope(FakeArtifactBundles, target):
                    self.assertEqual(
                        FakeArtifactBundles.DEFAULT_ARTIFACT_SUBJECT_STORE_ROOT,
                        target.resolve(),
                    )
                    for name in names:
                        self.assertEqual(os.environ[name], str(target.resolve()))
                self.assertEqual(
                    FakeArtifactBundles.DEFAULT_ARTIFACT_SUBJECT_STORE_ROOT,
                    Path("/ambient/subject-store"),
                )
                for name, value in previous_env.items():
                    self.assertEqual(os.environ.get(name), value)
            finally:
                for name, value in previous_env.items():
                    if value is None:
                        os.environ.pop(name, None)
                    else:
                        os.environ[name] = value

    def test_kag_artifact_negative_precondition_isolated_from_host_store(self) -> None:
        source_ref = kag_bundle_validator._exact_git_source_ref(REPO_ROOT)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            payload = kag_bundle_validator.validate_bundle(
                kag_bundle_validator.DEFAULT_MANIFEST,
                kag_bundle_validator.DEFAULT_SUBJECT,
                root / "bundle",
                root / "registry",
                root / "subject-store",
                source_ref=source_ref,
                clean=True,
            )

        precondition = payload["pre_materialization_gate"]
        trust_gate = precondition["trust_gate"]
        self.assertTrue(payload["ok"])
        self.assertTrue(precondition["ok"])
        self.assertEqual(trust_gate["verdict"], "deny")
        self.assertEqual(
            trust_gate["blockers"],
            ["required_artifact_subject_store_not_verified"],
        )
        self.assertFalse("/var/lib/abyss-machine/artifacts/subjects" in json.dumps(precondition))

    def test_kag_export_bundle_validator_requires_consumer_verdict(self) -> None:
        manifest = load_json("docs/source-lift/artifact-bundles/kag_export.bundle.json")
        manifest["consumer_contract"].pop("consumer_verdict")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "docs/source-lift/artifact-bundles/kag_export.bundle.json"
            subject_path = root / "generated/kag_export.min.json"
            manifest_path.parent.mkdir(parents=True)
            subject_path.parent.mkdir(parents=True)
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            subject_path.write_text("{}", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "consumer_verdict"):
                kag_bundle_validator._assert_manifest_matches_subject(manifest_path, subject_path)

    def test_kag_export_bundle_sanitizer_redacts_imported_abyss_machine_roots(self) -> None:
        old_repo_root = os.environ.get("ABYSS_MACHINE_REPO_ROOT")
        try:
            os.environ["ABYSS_MACHINE_REPO_ROOT"] = "/opt/abyss-machine"
            sanitized = kag_bundle_validator._sanitize_public_payload(
                {
                    "root": "/opt/abyss-machine",
                    "nested": "/opt/abyss-machine/src/abyss_machine/artifact_bundles.py",
                }
            )
        finally:
            if old_repo_root is None:
                os.environ.pop("ABYSS_MACHINE_REPO_ROOT", None)
            else:
                os.environ["ABYSS_MACHINE_REPO_ROOT"] = old_repo_root

        self.assertEqual(sanitized["root"], "abyss-machine-root-redacted")
        self.assertEqual(
            sanitized["nested"],
            "abyss-machine-root-redacted/src/abyss_machine/artifact_bundles.py",
        )

    def test_kag_export_bundle_sanitizer_reports_tree_changes(self) -> None:
        old_repo_root = os.environ.get("ABYSS_MACHINE_REPO_ROOT")
        try:
            os.environ["ABYSS_MACHINE_REPO_ROOT"] = "/opt/abyss-machine"
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                payload = root / "artifact.verify.json"
                payload.write_text(
                    json.dumps({"root": "/opt/abyss-machine/src/abyss_machine/artifact_bundles.py"}),
                    encoding="utf-8",
                )

                self.assertTrue(kag_bundle_validator._sanitize_public_json_tree(root))
                self.assertFalse(kag_bundle_validator._sanitize_public_json_tree(root))
                self.assertEqual(
                    json.loads(payload.read_text(encoding="utf-8"))["root"],
                    "abyss-machine-root-redacted/src/abyss_machine/artifact_bundles.py",
                )
        finally:
            if old_repo_root is None:
                os.environ.pop("ABYSS_MACHINE_REPO_ROOT", None)
            else:
                os.environ["ABYSS_MACHINE_REPO_ROOT"] = old_repo_root

    def test_repo_doc_surface_manifest_is_router_safe(self) -> None:
        manifest = load_json("generated/repo_doc_surface_manifest.min.json")

        self.assertEqual(manifest["manifest_version"], 1)
        self.assertEqual(manifest["source_of_truth"], "markdown-repo-doc-surfaces-v1")

        docs = manifest["docs"]
        self.assertTrue(docs)
        self.assertEqual(len({entry["doc_id"] for entry in docs}), len(docs))
        self.assertEqual(len({entry["doc_path"] for entry in docs}), len(docs))

        for entry in docs:
            self.assert_router_safe_doc_path(entry["doc_path"])
            self.assertTrue(entry["top_level_sections"])

    def test_router_safe_doc_path_rejects_out_of_scope_locations(self) -> None:
        for doc_path in (
            "../private.md",
            "/tmp/private.md",
            "techniques/history/example/TECHNIQUE.md",
        ):
            with self.subTest(doc_path=doc_path):
                with self.assertRaises(AssertionError):
                    self.assert_router_safe_doc_path(doc_path)

    def test_kind_manifest_min_stays_router_safe(self) -> None:
        manifest = load_json("generated/technique_kind_manifest.min.json")

        self.assertEqual(manifest["manifest_version"], 1)
        self.assertEqual(
            manifest["source_of_truth"],
            {
                "kind_registry": "config/technique_kind_registry.yaml",
                "catalog": "generated/technique_catalog.json",
                "bundles": "techniques/**/TECHNIQUE.md",
            },
        )
        self.assertEqual(
            manifest["selection_order"],
            [
                "workflow",
                "guardrail",
                "validation",
                "composition",
                "distribution",
                "artifact",
                "lift",
                "discovery",
                "handoff",
                "ingest",
                "assessment",
                "recovery",
            ],
        )
        self.assertEqual(len(manifest["kinds"]), len(manifest["selection_order"]))

        all_ids: list[str] = []
        for entry in manifest["kinds"]:
            self.assertEqual(
                {"kind", "summary", "counts", "technique_ids"},
                set(entry),
            )
            self.assertIn(entry["kind"], manifest["selection_order"])
            self.assertTrue(entry["summary"])
            self.assertEqual(
                {"total", "canonical", "promoted", "by_domain"},
                set(entry["counts"]),
            )
            self.assertEqual(
                {
                    "agent-workflows",
                    "docs",
                    "evaluation",
                    "system-recovery",
                    "validation-patterns",
                    "history",
                },
                set(entry["counts"]["by_domain"]),
            )
            self.assertEqual(entry["counts"]["total"], len(entry["technique_ids"]))
            all_ids.extend(entry["technique_ids"])

        catalog = load_json("generated/technique_catalog.min.json")
        self.assertEqual(
            [entry["id"] for entry in catalog["techniques"]],
            sorted(all_ids),
        )

    def test_technique_feat_example_validates_against_schema(self) -> None:
        schema = json.loads(
            (SCHEMAS_DIR / "technique_feat_catalog.schema.json").read_text(encoding="utf-8")
        )
        payload = json.loads(
            (GENERATED_DIR / "technique_feat_cards.min.example.json").read_text(
                encoding="utf-8"
            )
        )

        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(payload)


if __name__ == "__main__":
    unittest.main()
