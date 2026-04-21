#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import pathlib
import sys
from typing import Any

import jsonschema

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from build_agon_epistemic_technique_candidates import (  # noqa: E402
    BuildError,
    ITEM_KEY,
    OUT,
    REGISTRY_ID,
    RUNTIME_POSTURE,
    SRC,
    WAVE,
    build,
    load_source,
)

EXPECTED_COUNT = 10
KEY_FIELD = "technique_id"
REQUIRED_FIELDS = ['candidate_outputs', 'forbidden_effects', 'live_protocol', 'owner_repo', 'practice_boundary', 'runtime_effect', 'status', 'supports_move_extensions', 'technique_id']
FORBIDDEN_EFFECTS = ['live_verdict_authority', 'durable_scar_write', 'retention_execution', 'rank_mutation', 'trust_mutation', 'tree_of_sophia_promotion', 'kag_promotion', 'hidden_scheduler_action', 'assistant_contestant_drift', 'auto_doctrine_rewrite']
ALLOWED_RUNTIME = ['none', 'candidate_only', 'local_dry_run_candidate_only', 'local_rehearsal_candidate_only']
ITEM_SCHEMA = ROOT / "schemas" / "agon-epistemic-technique-candidate.schema.json"
REGISTRY_SCHEMA = ROOT / "schemas" / "agon-epistemic-technique-candidate-registry.schema.json"


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def schema_error(validator: jsonschema.Draft202012Validator, instance: Any) -> str | None:
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if not errors:
        return None
    error = errors[0]
    path = ".".join(str(part) for part in error.path) or "<root>"
    return f"schema violation at {path}: {error.message}"


def make_item_validator() -> jsonschema.Draft202012Validator:
    return jsonschema.Draft202012Validator(load_json(ITEM_SCHEMA))


def make_registry_validator() -> jsonschema.Draft202012Validator:
    schema = copy.deepcopy(load_json(REGISTRY_SCHEMA))
    schema["properties"][ITEM_KEY]["items"] = load_json(ITEM_SCHEMA)
    return jsonschema.Draft202012Validator(schema)


def validate_item(item: Any, item_validator: jsonschema.Draft202012Validator) -> str | None:
    if not isinstance(item, dict):
        return "item must be an object"
    schema_problem = schema_error(item_validator, item)
    if schema_problem:
        return schema_problem
    for field in REQUIRED_FIELDS:
        if field not in item:
            return f"missing required field {field} in {item}"
    key = item.get(KEY_FIELD)
    if not isinstance(key, str) or not key:
        return f"{KEY_FIELD} must be a non-empty string"
    if item.get("owner_repo") != "aoa-techniques":
        return f"{key} owner_repo must be aoa-techniques"
    if item.get("live_protocol") is not False:
        return f"{key} live_protocol must be false"
    if item.get("runtime_effect") not in ALLOWED_RUNTIME:
        return f"{key} invalid runtime_effect: {item.get('runtime_effect')}"
    forbidden_effects = item.get("forbidden_effects")
    if not isinstance(forbidden_effects, list) or not all(isinstance(effect, str) for effect in forbidden_effects):
        return f"{key} forbidden_effects must be a string array"
    for forbidden in FORBIDDEN_EFFECTS:
        if forbidden not in forbidden_effects:
            return f"{key} missing forbidden_effect {forbidden}"
    return None


def validate() -> int:
    try:
        data = load_source()
        expected = build()
    except BuildError as exc:
        return fail(str(exc))

    if data.get("registry_id") != REGISTRY_ID:
        return fail(f"source registry_id must be {REGISTRY_ID}")
    if data.get("wave") != WAVE:
        return fail(f"source wave must be {WAVE}")
    if data.get("runtime_posture") != RUNTIME_POSTURE:
        return fail(f"source runtime_posture must be {RUNTIME_POSTURE}")

    items = data.get(ITEM_KEY)
    if not isinstance(items, list):
        return fail(f"source {ITEM_KEY} must be an array")
    if len(items) != EXPECTED_COUNT:
        return fail(f"expected {EXPECTED_COUNT} items in {ITEM_KEY}, got {len(items)}")

    item_validator = make_item_validator()
    seen: set[str] = set()
    for item in items:
        err = validate_item(item, item_validator)
        if err:
            return fail(err)
        key = item[KEY_FIELD]
        if key in seen:
            return fail(f"duplicate item key {key}")
        seen.add(key)

    if not OUT.exists():
        return fail(f"missing generated registry {OUT}")
    registry = load_json(OUT)
    if registry != expected:
        return fail("generated registry does not match source rebuild")
    registry_problem = schema_error(make_registry_validator(), registry)
    if registry_problem:
        return fail(registry_problem)

    print(json.dumps({"ok": True, "item_key": ITEM_KEY, "count": len(items)}, sort_keys=True))
    return 0


def main() -> int:
    return validate()


if __name__ == "__main__":
    raise SystemExit(main())
