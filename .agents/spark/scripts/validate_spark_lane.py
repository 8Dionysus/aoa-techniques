#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path(".agents/spark/registry.json")
SCHEMA_VERSION = "aoa_techniques_spark_lane_registry_v1"
SCENARIO_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

REQUIRED_SCENARIO_FILES = (
    "README.md",
    "PROMPT.md",
    "templates/result.md",
    "templates/handoff.md",
    "examples/result.example.md",
)

REQUIRED_README_MARKERS = (
    "## Scope",
    "## Done Signal",
    "## Stop-line",
    "## Handoff Route",
)

REQUIRED_RESULT_MARKERS = (
    "Scenario:",
    "Status: done",
    "Scope:",
    "Files read:",
    "Findings:",
    "Changes made:",
    "Validation run:",
    "Skipped checks:",
    "Remaining risk:",
    "Next owner route:",
)

REQUIRED_HANDOFF_MARKERS = (
    "Scenario:",
    "Status: handoff",
    "Reason for handoff:",
    "Scope read:",
    "Findings:",
    "Files likely affected:",
    "Validation already run:",
    "Validation still needed:",
    "Stop-line:",
    "Suggested next prompt:",
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require_string(problems: list[str], where: str, value: object) -> None:
    if not isinstance(value, str) or not value.strip():
        problems.append(f"{where} must be a non-empty string")


def require_string_list(problems: list[str], where: str, value: object) -> None:
    if not isinstance(value, list) or not value:
        problems.append(f"{where} must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            problems.append(f"{where}[{index}] must be a non-empty string")


def rel_exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()


def read_text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def release_lane_runs_spark_validator(root: Path) -> bool:
    lanes_path = root / "config" / "validation_lanes.json"
    if not lanes_path.is_file():
        return False
    try:
        lanes = load_json(lanes_path)
    except json.JSONDecodeError:
        return False
    sequences = lanes.get("command_sequences")
    if not isinstance(sequences, dict):
        return False
    release_sequence = sequences.get("release_check")
    if not isinstance(release_sequence, list):
        return False
    return [
        "python",
        ".agents/spark/scripts/validate_spark_lane.py",
    ] in release_sequence


def require_markers(
    problems: list[str],
    root: Path,
    rel: str,
    markers: tuple[str, ...],
) -> None:
    path = root / rel
    if not path.is_file():
        problems.append(f"missing file: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            problems.append(f"{rel} missing marker: {marker}")


def validate_scenario(root: Path, scenario: dict[str, Any], seen_ids: set[str]) -> list[str]:
    problems: list[str] = []
    scenario_id = scenario.get("scenario_id")
    where = f"scenarios[{scenario_id or '?'}]"

    for key in (
        "scenario_id",
        "role",
        "path",
        "prompt_ref",
        "result_template_ref",
        "handoff_template_ref",
        "result_example_ref",
        "done_signal",
        "stop_line",
    ):
        require_string(problems, f"{where}.{key}", scenario.get(key))
    require_string_list(problems, f"{where}.default_validation", scenario.get("default_validation"))

    if isinstance(scenario_id, str):
        if not SCENARIO_ID_RE.match(scenario_id):
            problems.append(f"{where}.scenario_id must be lowercase kebab-case")
        if scenario_id in seen_ids:
            problems.append(f"duplicate scenario_id: {scenario_id}")
        seen_ids.add(scenario_id)

    path = scenario.get("path")
    if isinstance(path, str):
        scenario_dir = root / path
        if not scenario_dir.is_dir():
            problems.append(f"{where}.path does not exist as directory: {path}")
        for rel in REQUIRED_SCENARIO_FILES:
            expected = f"{path}/{rel}"
            if not (root / expected).is_file():
                problems.append(f"{where} missing required scenario file: {expected}")

    for key in (
        "prompt_ref",
        "result_template_ref",
        "handoff_template_ref",
        "result_example_ref",
    ):
        value = scenario.get(key)
        if isinstance(value, str) and not (root / value).is_file():
            problems.append(f"{where}.{key} does not exist: {value}")

    if isinstance(path, str):
        require_markers(problems, root, f"{path}/README.md", REQUIRED_README_MARKERS)
    prompt_ref = scenario.get("prompt_ref")
    if isinstance(prompt_ref, str) and (root / prompt_ref).is_file():
        prompt = read_text(root, prompt_ref)
        if "done-or-handoff" not in prompt:
            problems.append(f"{prompt_ref} must mention done-or-handoff")

    result_ref = scenario.get("result_template_ref")
    if isinstance(result_ref, str):
        require_markers(problems, root, result_ref, REQUIRED_RESULT_MARKERS)
    handoff_ref = scenario.get("handoff_template_ref")
    if isinstance(handoff_ref, str):
        require_markers(problems, root, handoff_ref, REQUIRED_HANDOFF_MARKERS)
    example_ref = scenario.get("result_example_ref")
    if isinstance(example_ref, str):
        require_markers(problems, root, example_ref, REQUIRED_RESULT_MARKERS)

    return problems


def validate_packet_dir(
    root: Path,
    packet_dir: Path,
    required_markers: tuple[str, ...],
    scenario_ids: set[str],
) -> list[str]:
    problems: list[str] = []
    if not packet_dir.exists():
        return problems
    for path in sorted(packet_dir.glob("*.md")):
        if path.name == "README.md":
            continue
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        for marker in required_markers:
            if marker not in text:
                problems.append(f"{rel} missing marker: {marker}")
        scenario_line = next((line for line in text.splitlines() if line.startswith("Scenario:")), "")
        scenario_id = scenario_line.partition(":")[2].strip()
        if scenario_id and scenario_id not in scenario_ids:
            problems.append(f"{rel} names unknown scenario: {scenario_id}")
    return problems


def validate(root: Path) -> list[str]:
    problems: list[str] = []
    registry_path = root / REGISTRY_PATH
    if not registry_path.exists():
        return [f"missing Spark registry: {REGISTRY_PATH}"]

    try:
        registry = load_json(registry_path)
    except json.JSONDecodeError as exc:
        return [f"{REGISTRY_PATH} is not valid JSON: {exc}"]

    if not isinstance(registry, dict):
        return [f"{REGISTRY_PATH} must be a JSON object"]

    if registry.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"schema_version must be {SCHEMA_VERSION}")
    expected_refs = {
        "authority_ref": ".agents/spark/README.md",
        "agents_ref": ".agents/spark/AGENTS.md",
        "notebook_ref": ".agents/spark/SPARK_EXTRAPOLATION_NOTEBOOK.md",
        "swarm_ref": ".agents/spark/SWARM.md",
    }
    for key, expected in expected_refs.items():
        if registry.get(key) != expected:
            problems.append(f"{key} must be {expected}")
        if not rel_exists(root, expected):
            problems.append(f"{key} target does not exist: {expected}")

    storage_refs = registry.get("storage_refs")
    if not isinstance(storage_refs, dict):
        problems.append("storage_refs must be an object")
        storage_refs = {}
    for key in ("handoffs", "handoffs_open", "handoffs_closed", "results"):
        require_string(problems, f"storage_refs.{key}", storage_refs.get(key))
        value = storage_refs.get(key)
        if isinstance(value, str) and not rel_exists(root, value):
            problems.append(f"storage_refs.{key} target does not exist: {value}")

    schema_refs = registry.get("schema_refs")
    if not isinstance(schema_refs, dict):
        problems.append("schema_refs must be an object")
        schema_refs = {}
    for key in ("registry", "result", "handoff"):
        require_string(problems, f"schema_refs.{key}", schema_refs.get(key))
        value = schema_refs.get(key)
        if isinstance(value, str):
            if not rel_exists(root, value):
                problems.append(f"schema_refs.{key} target does not exist: {value}")
            else:
                try:
                    load_json(root / value)
                except json.JSONDecodeError as exc:
                    problems.append(f"{value} is not valid JSON: {exc}")

    scenarios = registry.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        problems.append("scenarios must be a non-empty list")
        scenarios = []

    seen_ids: set[str] = set()
    registered_paths: set[str] = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            problems.append("scenarios entries must be objects")
            continue
        path = scenario.get("path")
        if isinstance(path, str):
            registered_paths.add(path)
        problems.extend(validate_scenario(root, scenario, seen_ids))

    scenarios_root = root / ".agents/spark/scenarios"
    discovered_paths = (
        {
            path.relative_to(root).as_posix()
            for path in scenarios_root.iterdir()
            if path.is_dir()
        }
        if scenarios_root.is_dir()
        else set()
    )
    if registered_paths != discovered_paths:
        missing = sorted(discovered_paths - registered_paths)
        stale = sorted(registered_paths - discovered_paths)
        if missing:
            problems.append(f"Spark scenarios missing from registry: {', '.join(missing)}")
        if stale:
            problems.append(
                "registry scenario paths missing from .agents/spark/scenarios/: "
                + ", ".join(stale)
            )

    require_string_list(problems, "validation_commands", registry.get("validation_commands"))

    spark_readme = root / ".agents/spark/README.md"
    if spark_readme.exists():
        readme = spark_readme.read_text(encoding="utf-8")
        for scenario_id in sorted(seen_ids):
            if f"`{scenario_id}`" not in readme and f"[{scenario_id}]" not in readme:
                problems.append(f".agents/spark/README.md does not mention scenario: {scenario_id}")

    agents = root / ".agents/spark/AGENTS.md"
    if agents.exists():
        agents_text = agents.read_text(encoding="utf-8")
        for required in (
            "done-or-handoff",
            ".agents/spark/registry.json",
            "python .agents/spark/scripts/validate_spark_lane.py",
        ):
            if required not in agents_text:
                problems.append(f".agents/spark/AGENTS.md does not mention {required}")

    swarm = root / ".agents/spark/SWARM.md"
    if swarm.exists() and ".agents/spark/registry.json" not in swarm.read_text(encoding="utf-8"):
        problems.append(".agents/spark/SWARM.md does not mention .agents/spark/registry.json")

    if not release_lane_runs_spark_validator(root):
        problems.append(
            "config/validation_lanes.json release_check lane does not run "
            ".agents/spark/scripts/validate_spark_lane.py"
        )

    problems.extend(
        validate_packet_dir(root, root / ".agents/spark/results", REQUIRED_RESULT_MARKERS, seen_ids)
    )
    problems.extend(
        validate_packet_dir(root, root / ".agents/spark/handoffs/open", REQUIRED_HANDOFF_MARKERS, seen_ids)
    )
    problems.extend(
        validate_packet_dir(root, root / ".agents/spark/handoffs/closed", REQUIRED_HANDOFF_MARKERS, seen_ids)
    )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the aoa-techniques Spark lane.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()

    problems = validate(root)
    if problems:
        print("Spark lane validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("Spark lane validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
