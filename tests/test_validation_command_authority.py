from __future__ import annotations

import json
import subprocess
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from scripts import ci_gate, release_check, validation_lanes


REPO_ROOT = Path(__file__).resolve().parents[1]


def command_sequence_from_manifest(name: str) -> tuple[tuple[str, ...], ...]:
    manifest = json.loads(
        (REPO_ROOT / "config" / "validation_lanes.json").read_text(encoding="utf-8")
    )
    return tuple(tuple(command) for command in manifest["command_sequences"][name])


def drift_paths_from_manifest(name: str) -> tuple[str, ...]:
    manifest = json.loads(
        (REPO_ROOT / "config" / "validation_lanes.json").read_text(encoding="utf-8")
    )
    return tuple(manifest["drift_paths"][name])


def generated_group_ids_from_manifest() -> tuple[str, ...]:
    manifest = json.loads(
        (REPO_ROOT / "config" / "validation_lanes.json").read_text(encoding="utf-8")
    )
    return tuple(group["id"] for group in manifest["command_groups"]["generated_check"])


class ValidationCommandAuthorityTests(unittest.TestCase):
    def test_validation_lanes_manifest_is_loader_authority(self) -> None:
        self.assertEqual(
            REPO_ROOT / "config" / "validation_lanes.json",
            validation_lanes.VALIDATION_LANES_PATH,
        )
        self.assertEqual(
            command_sequence_from_manifest("source_fast"),
            validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            command_sequence_from_manifest("generated_check"),
            validation_lanes.GENERATED_CHECK_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            (
                "decisions",
                "agents_mesh",
                "catalog",
                "mechanics_projections",
                "kag_export",
                "technique_intelligence",
                "questbook",
                "public_hygiene",
            ),
            tuple(group["id"] for group in validation_lanes.GENERATED_CHECK_COMMAND_GROUPS),
        )
        self.assertEqual(
            generated_group_ids_from_manifest(),
            tuple(group["id"] for group in validation_lanes.GENERATED_CHECK_COMMAND_GROUPS),
        )
        self.assertEqual(
            command_sequence_from_manifest("mechanics_part_local"),
            validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            (("python", "scripts/run_part_local_tests.py"),),
            validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            command_sequence_from_manifest("release_check"),
            validation_lanes.RELEASE_CHECK_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            command_sequence_from_manifest("release_check"),
            validation_lanes.command_sequence_for_lane("release"),
        )
        self.assertEqual(
            command_sequence_from_manifest("nightly"),
            validation_lanes.NIGHTLY_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            drift_paths_from_manifest("generated"),
            validation_lanes.GENERATED_DRIFT_PATHS,
        )
        self.assertEqual(
            (
                "git",
                "diff",
                "--binary",
                "--no-ext-diff",
                "--",
                *validation_lanes.GENERATED_DRIFT_PATHS,
            ),
            validation_lanes.GENERATED_DRIFT_SNAPSHOT_COMMAND,
        )

    def test_validation_lanes_api_resolves_lane_ids_to_command_sequences(self) -> None:
        self.assertEqual(
            command_sequence_from_manifest("source_fast"),
            validation_lanes.command_sequence_for_lane("source_fast"),
        )
        self.assertEqual(
            command_sequence_from_manifest("generated_check"),
            validation_lanes.command_sequence_for_lane("generated"),
        )
        self.assertEqual(
            command_sequence_from_manifest("mechanics_part_local"),
            validation_lanes.command_sequence_for_lane("mechanics_part_local"),
        )
        self.assertEqual(
            command_sequence_from_manifest("nightly"),
            validation_lanes.command_sequence_for_lane("nightly"),
        )

        with self.assertRaisesRegex(ValueError, "does not define a command sequence"):
            validation_lanes.command_sequence_for_lane("advisory")
        with self.assertRaisesRegex(ValueError, "unknown lane"):
            validation_lanes.command_sequence_for_lane("missing")

    def test_ci_gate_executes_lane_sequences_from_loader(self) -> None:
        with patch.object(ci_gate, "run_sequence") as run_sequence:
            ci_gate.run_source_fast()
            run_sequence.assert_called_once_with(validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE)

        with patch.object(ci_gate, "run_command_groups") as run_command_groups:
            with patch.object(ci_gate, "capture_command_output", return_value="stable") as capture:
                ci_gate.run_generated()
            run_command_groups.assert_called_once_with(
                validation_lanes.GENERATED_CHECK_COMMAND_GROUPS
            )
            self.assertEqual(
                [
                    (validation_lanes.GENERATED_DRIFT_SNAPSHOT_COMMAND,),
                    (validation_lanes.GENERATED_DRIFT_SNAPSHOT_COMMAND,),
                ],
                [call.args for call in capture.call_args_list],
            )

        with patch.object(ci_gate, "run_command") as run_command:
            ci_gate.run_release()
            run_command.assert_called_once_with(("python", "scripts/release_check.py"))

        with patch.object(ci_gate, "run_sequence") as run_sequence:
            ci_gate.run_mechanics_part_local()
            run_sequence.assert_called_once_with(
                validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE
            )

        with patch.object(ci_gate, "run_sequence") as run_sequence:
            ci_gate.run_nightly()
            run_sequence.assert_called_once_with(validation_lanes.NIGHTLY_COMMAND_SEQUENCE)

        with patch("builtins.print") as print_call:
            ci_gate.run_advisory()
            self.assertTrue(print_call.called)

    def test_generated_lane_fails_when_projection_snapshot_changes(self) -> None:
        with patch.object(ci_gate, "run_command_groups"):
            with patch.object(
                ci_gate,
                "capture_command_output",
                side_effect=("before", "after"),
            ):
                with redirect_stderr(StringIO()):
                    with self.assertRaises(subprocess.CalledProcessError):
                        ci_gate.run_generated()

    def test_release_check_preserves_entrypoint_without_owning_sequence(self) -> None:
        self.assertEqual(
            "release",
            release_check.RELEASE_LANE_ID,
        )
        self.assertEqual(
            validation_lanes.command_sequence_for_lane("release"),
            release_check.release_lane_commands(),
        )
        release_commands = release_check.release_lane_commands()
        self.assertIn(
            ("python", "scripts/build_questbook_projection.py"),
            release_commands,
        )
        self.assertIn(
            ("python", "scripts/build_questbook_projection.py", "--check"),
            release_commands,
        )
        self.assertIn(
            ("python", "scripts/validate_public_hygiene.py"),
            release_commands,
        )
        release_check_text = (REPO_ROOT / "scripts" / "release_check.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("validation_lanes.command_sequence_for_lane(RELEASE_LANE_ID)", release_check_text)
        self.assertNotIn("RELEASE_CHECK_COMMAND_SEQUENCE", release_check_text)
        self.assertNotIn('("python", "scripts/build_catalog.py")', release_check_text)

    def test_workflow_calls_ci_lane_entrypoints_not_release_check(self) -> None:
        workflow = (REPO_ROOT / ".github" / "workflows" / "repo-validation.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("python scripts/ci_gate.py --mode source-fast", workflow)
        self.assertIn("python scripts/ci_gate.py --mode generated", workflow)
        self.assertNotIn("python scripts/release_check.py", workflow)
        self.assertNotIn("python scripts/run_tests.py", workflow)
        self.assertNotIn("python scripts/validate_repo.py", workflow)

    def test_active_docs_route_to_lane_ids_instead_of_full_sequences(self) -> None:
        active_docs = (
            "AGENTS.md",
            ".github/AGENTS.md",
            "config/AGENTS.md",
            "scripts/AGENTS.md",
            "tests/AGENTS.md",
            "docs/AGENTS.md",
            "docs/decisions/AGENTS.md",
            "docs/RELEASING.md",
        )
        forbidden_sequence_markers = (
            "scripts/build_shadow_review_manifest.py\npython scripts/build_promotion_readiness.py",
            "scripts/build_kag_export.py\npython scripts/build_technique_intelligence.py",
            "scripts/run_tests.py\npython scripts/validate_nested_agents.py\npython scripts/validate_repo.py",
        )

        for relative_path in active_docs:
            text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            with self.subTest(surface=relative_path, route="lane-authority"):
                self.assertTrue(
                    "config/validation_lanes.json" in text
                    or "validation_lanes" in text
                    or "source-fast" in text
                )
            for marker in forbidden_sequence_markers:
                with self.subTest(surface=relative_path, marker=marker):
                    self.assertNotIn(marker, text)

    def test_active_decision_guidance_uses_lanes_not_command_runbooks(self) -> None:
        active_decision_guidance = (
            "docs/decisions/TEMPLATE.md",
            "docs/decisions/AOA-TECH-D-0066-validation-lane-command-authority.md",
            "docs/decisions/AOA-TECH-D-0067-validator-owner-modules.md",
        )
        forbidden_active_commands = (
            "```bash",
            "python scripts/release_check.py",
            "python scripts/run_tests.py",
            "python scripts/validate_repo.py",
            "python -m unittest",
        )

        for relative_path in active_decision_guidance:
            text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            with self.subTest(surface=relative_path, route="lane_or_owner"):
                self.assertRegex(text, r"(source-fast|generated|release|AGENTS\.md)")
            with self.subTest(surface=relative_path, route="authority"):
                self.assertIn("config/validation_lanes.json", text)
            for command in forbidden_active_commands:
                with self.subTest(surface=relative_path, command=command):
                    self.assertNotIn(command, text)

    def test_historical_decision_records_may_preserve_command_evidence(self) -> None:
        decisions_agent = (
            REPO_ROOT / "docs" / "decisions" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        historical_record = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "AOA-TECH-D-0051-review-packet-mechanics-home.md"
        ).read_text(encoding="utf-8")

        self.assertIn("historical verification evidence", decisions_agent)
        self.assertIn("python scripts/release_check.py", historical_record)


if __name__ == "__main__":
    unittest.main()
