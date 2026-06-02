"""Shared validation lane loader for aoa-techniques.

The executable command authority lives in ``config/validation_lanes.json``.
This module is only the Python loader/API for CI, release, and tests.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

Command = tuple[str, ...]
LaneDefinition = dict[str, Any]
CommandGroup = dict[str, Any]

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATION_LANES_PATH = REPO_ROOT / "config" / "validation_lanes.json"


def _load_manifest() -> dict[str, Any]:
    payload = json.loads(VALIDATION_LANES_PATH.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError(
            f"{VALIDATION_LANES_PATH}: unsupported schema_version "
            f"{payload.get('schema_version')!r}"
        )
    return payload


def _command(command: object, where: str) -> Command:
    if not isinstance(command, list) or not command:
        raise ValueError(f"{VALIDATION_LANES_PATH}: {where} must be a non-empty list")
    if any(not isinstance(part, str) or not part for part in command):
        raise ValueError(f"{VALIDATION_LANES_PATH}: {where} must contain strings")
    return tuple(command)


def _command_sequence(manifest: dict[str, Any], name: str) -> tuple[Command, ...]:
    sequences = manifest.get("command_sequences")
    if not isinstance(sequences, dict):
        raise ValueError(f"{VALIDATION_LANES_PATH}: command_sequences must be a mapping")
    sequence = sequences.get(name)
    if not isinstance(sequence, list) or not sequence:
        raise ValueError(f"{VALIDATION_LANES_PATH}: missing command sequence {name!r}")
    return tuple(
        _command(command, f"command_sequences.{name}[{idx}]")
        for idx, command in enumerate(sequence)
    )


def _command_groups(manifest: dict[str, Any], name: str) -> tuple[CommandGroup, ...]:
    groups = manifest.get("command_groups")
    if not isinstance(groups, dict):
        raise ValueError(f"{VALIDATION_LANES_PATH}: command_groups must be a mapping")
    group_entries = groups.get(name)
    if not isinstance(group_entries, list) or not group_entries:
        raise ValueError(f"{VALIDATION_LANES_PATH}: missing command group {name!r}")

    parsed_groups: list[CommandGroup] = []
    for idx, group in enumerate(group_entries):
        where = f"command_groups.{name}[{idx}]"
        if not isinstance(group, dict):
            raise ValueError(f"{VALIDATION_LANES_PATH}: {where} must be an object")
        for field in ("id", "label", "command_sequence", "owner_module"):
            if not isinstance(group.get(field), str) or not group[field]:
                raise ValueError(f"{VALIDATION_LANES_PATH}: {where}.{field} is required")
        parsed_groups.append(
            {
                "id": group["id"],
                "label": group["label"],
                "command_sequence": group["command_sequence"],
                "owner_module": group["owner_module"],
                "commands": _command_sequence(manifest, group["command_sequence"]),
            }
        )
    return tuple(parsed_groups)


def flatten_command_groups(groups: tuple[CommandGroup, ...]) -> tuple[Command, ...]:
    return tuple(command for group in groups for command in group["commands"])


def _drift_paths(manifest: dict[str, Any], name: str) -> tuple[str, ...]:
    drift_paths = manifest.get("drift_paths")
    if not isinstance(drift_paths, dict):
        raise ValueError(f"{VALIDATION_LANES_PATH}: drift_paths must be a mapping")
    paths = drift_paths.get(name)
    if not isinstance(paths, list) or not paths:
        raise ValueError(f"{VALIDATION_LANES_PATH}: missing drift path list {name!r}")
    if any(not isinstance(path, str) or not path for path in paths):
        raise ValueError(f"{VALIDATION_LANES_PATH}: drift_paths.{name} must contain strings")
    return tuple(paths)


def _lane_definitions(manifest: dict[str, Any]) -> dict[str, LaneDefinition]:
    lanes = manifest.get("lanes")
    if not isinstance(lanes, dict) or not lanes:
        raise ValueError(f"{VALIDATION_LANES_PATH}: lanes must be a non-empty mapping")

    expected = {
        "source_fast",
        "generated",
        "mechanics_part_local",
        "release",
        "nightly",
        "advisory",
    }
    missing = sorted(expected - set(lanes))
    if missing:
        raise ValueError(f"{VALIDATION_LANES_PATH}: missing lane definitions {missing}")

    for lane_id, lane in lanes.items():
        if not isinstance(lane, dict):
            raise ValueError(f"{VALIDATION_LANES_PATH}: lanes.{lane_id} must be an object")
        if not isinstance(lane.get("label"), str) or not lane["label"]:
            raise ValueError(f"{VALIDATION_LANES_PATH}: lanes.{lane_id}.label is required")
        if lane.get("posture") not in {"blocking", "non_blocking"}:
            raise ValueError(f"{VALIDATION_LANES_PATH}: lanes.{lane_id}.posture is invalid")
        if not isinstance(lane.get("owner_surface"), str) or not lane["owner_surface"]:
            raise ValueError(f"{VALIDATION_LANES_PATH}: lanes.{lane_id}.owner_surface is required")
        if lane["posture"] == "blocking" and not isinstance(lane.get("command_sequence"), str):
            raise ValueError(
                f"{VALIDATION_LANES_PATH}: lanes.{lane_id}.command_sequence is required"
            )
    return lanes


_MANIFEST = _load_manifest()
LANE_DEFINITIONS = _lane_definitions(_MANIFEST)


def command_sequence_for_lane(lane_id: str) -> tuple[Command, ...]:
    lane = LANE_DEFINITIONS.get(lane_id)
    if lane is None:
        raise ValueError(f"{VALIDATION_LANES_PATH}: unknown lane {lane_id!r}")
    sequence_name = lane.get("command_sequence")
    if not isinstance(sequence_name, str) or not sequence_name:
        raise ValueError(
            f"{VALIDATION_LANES_PATH}: lanes.{lane_id} does not define a command sequence"
        )
    return _command_sequence(_MANIFEST, sequence_name)


SOURCE_FAST_COMMAND_SEQUENCE = _command_sequence(_MANIFEST, "source_fast")
GENERATED_CHECK_COMMAND_GROUPS = _command_groups(_MANIFEST, "generated_check")
GENERATED_CHECK_COMMAND_SEQUENCE = flatten_command_groups(GENERATED_CHECK_COMMAND_GROUPS)
MECHANICS_PART_LOCAL_COMMAND_SEQUENCE = _command_sequence(
    _MANIFEST, "mechanics_part_local"
)
RELEASE_CHECK_COMMAND_SEQUENCE = command_sequence_for_lane("release")
NIGHTLY_COMMAND_SEQUENCE = _command_sequence(_MANIFEST, "nightly")
GENERATED_DRIFT_PATHS = _drift_paths(_MANIFEST, "generated")
GENERATED_DRIFT_SNAPSHOT_COMMAND = (
    "git",
    "diff",
    "--binary",
    "--no-ext-diff",
    "--",
    *GENERATED_DRIFT_PATHS,
)
ADVISORY_BOUNDARIES = tuple(LANE_DEFINITIONS["advisory"].get("boundaries", ()))
