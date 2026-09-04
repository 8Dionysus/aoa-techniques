from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts import ci_gate, release_check, validate_repo_local_kag_index, validation_lanes


REPO_ROOT = Path(__file__).resolve().parents[1]
COMMAND_BLOCK_LINE = re.compile(
    r"^\s*(?:\$\s*)?(?:python(?:3)?|git|gh|pytest|pip|uv|make|bash|sh|find|"
    r"cargo|npm|node|ruff|mypy|jq|rg|curl|docker|podman|\./)\s"
)
REPO_COMMAND_LITERAL = re.compile(
    r"python (?:scripts/|mechanics/|\.agents/|-m (?:unittest|pytest|pip))|"
    r"git (?:diff --|status --|status -|mv )"
)


def markdown_command_nonowners() -> tuple[Path, ...]:
    paths: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        relative = path.relative_to(REPO_ROOT)
        if path.name in {"AGENTS.md", "VALIDATION.md"}:
            continue
        if relative.parts and relative.parts[0] == ".deps":
            continue
        if relative.parts[:2] == (".agents", "skills"):
            continue
        if relative.parts and relative.parts[0] == "techniques":
            continue
        paths.append(path)
    return tuple(sorted(paths))


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
        self.assertIn(
            ("python", "scripts/validate_source_contracts.py"),
            validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE,
        )
        self.assertIn(
            ("python", "scripts/validate_local_stats_port.py"),
            validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            ("python", "scripts/validate_repo_local_kag_index.py"),
            validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE[0],
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
        self.assertIn(
            ("python", "scripts/validate_local_stats_port.py"),
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
        self.assertNotIn("python scripts/validate_source_contracts.py", workflow)
        self.assertIn("repository: 8Dionysus/aoa-kag", workflow)
        self.assertIn("repository: 8Dionysus/aoa-stats", workflow)
        self.assertIn("AOA_KAG_ROOT:", workflow)
        self.assertIn("AOA_STATS_ROOT:", workflow)
        self.assertIn("AOA_REPO_LOCAL_KAG_HISTORY_REF:", workflow)
        self.assertIn("AOA_REPO_LOCAL_KAG_EVENT_HISTORY_REF:", workflow)
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn(f"ref: {validate_repo_local_kag_index.AOA_KAG_REF}", workflow)
        self.assertNotIn("uses: 8Dionysus/aoa-kag/", workflow)

    def test_repo_local_kag_adapter_resolves_sibling_builder(self) -> None:
        with TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            repo_root = workspace / "aoa-techniques"
            generator = workspace / "aoa-kag" / "scripts" / "generate_repo_local_kag_index.py"
            validator = workspace / "aoa-kag" / "scripts" / "validate_repo_local_kag_family.py"
            repo_root.mkdir()
            generator.parent.mkdir(parents=True)
            generator.touch()
            validator.touch()

            aoa_kag_root = validate_repo_local_kag_index.resolve_aoa_kag_root(
                {}, repo_root
            )
            self.assertEqual((workspace / "aoa-kag").resolve(), aoa_kag_root)
            commands = validate_repo_local_kag_index.commands(
                aoa_kag_root,
                repo_root,
                history_ref="base-sha",
                event_history_ref="event-base-sha",
            )
            self.assertIn("--incremental", commands[1])
            self.assertIn("base-sha", commands[0])
            self.assertIn("event-base-sha", commands[0])
            self.assertEqual(
                str(validator),
                commands[2][1],
            )

    def test_repo_local_kag_adapter_resolves_owner_history_boundary(self) -> None:
        history = validate_repo_local_kag_index.resolve_history_refs(
            {
                "AOA_REPO_LOCAL_KAG_HISTORY_REPO": "aoa-techniques",
                "AOA_REPO_LOCAL_KAG_HISTORY_REF": "base-sha",
                "AOA_REPO_LOCAL_KAG_EVENT_HISTORY_REF": "event-base-sha",
            },
            REPO_ROOT,
        )
        self.assertEqual(("base-sha", "event-base-sha"), history)

    def test_repo_local_kag_adapter_accepts_pinned_checkout(self) -> None:
        with TemporaryDirectory() as temp_dir:
            aoa_kag_root = Path(temp_dir) / "aoa-kag"
            with patch.object(subprocess, "run") as run:
                run.return_value.returncode = 0
                run.return_value.stdout = validate_repo_local_kag_index.AOA_KAG_REF + "\n"
                self.assertEqual(
                    aoa_kag_root,
                    validate_repo_local_kag_index.require_pinned_checkout(aoa_kag_root),
                )

    def test_repo_local_kag_adapter_rejects_other_checkout(self) -> None:
        with patch.object(subprocess, "run") as run:
            run.return_value.returncode = 0
            run.return_value.stdout = "0" * 40 + "\n"
            with self.assertRaisesRegex(RuntimeError, "must resolve"):
                validate_repo_local_kag_index.require_pinned_checkout(Path("aoa-kag"))

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

    def test_on_demand_routes_execute_root_tests(self) -> None:
        validation = (REPO_ROOT / "VALIDATION.md").read_text(encoding="utf-8")
        tests_card = (REPO_ROOT / "tests" / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("### Root test surface", validation)
        self.assertIn("python scripts/run_tests.py", validation)
        self.assertIn("Root test surface", tests_card)

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

    def test_markdown_nonowners_do_not_store_command_blocks(self) -> None:
        offenders: list[str] = []
        for path in markdown_command_nonowners():
            relative = path.relative_to(REPO_ROOT).as_posix()
            lines = path.read_text(encoding="utf-8").splitlines()
            index = 0
            while index < len(lines):
                if not lines[index].lstrip().startswith("```"):
                    index += 1
                    continue
                start = index + 1
                index += 1
                body: list[str] = []
                while index < len(lines) and not lines[index].lstrip().startswith("```"):
                    body.append(lines[index])
                    index += 1
                if any(COMMAND_BLOCK_LINE.match(line) for line in body):
                    offenders.append(f"{relative}:{start}")
                index += 1

        self.assertEqual([], offenders)

    def test_markdown_nonowners_do_not_store_repo_command_literals(self) -> None:
        offenders: list[str] = []
        for path in markdown_command_nonowners():
            relative = path.relative_to(REPO_ROOT).as_posix()
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                if REPO_COMMAND_LITERAL.search(line):
                    offenders.append(f"{relative}:{line_number}")

        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main()
