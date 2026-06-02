from __future__ import annotations

from .common import *

def quest_id_sort_key(quest_id: str) -> tuple[int, str]:
    suffix = quest_id.rsplit("-", 1)[-1]
    try:
        return (int(suffix), quest_id)
    except ValueError:
        return (sys.maxsize, quest_id)


def discover_quest_ids(repo_root: Path) -> tuple[str, ...]:
    quest_ids = tuple(discover_quest_source_paths(repo_root))
    if not quest_ids:
        return FOUNDATION_QUEST_IDS
    return quest_ids


def missing_foundation_quest_ids(quest_ids: tuple[str, ...]) -> tuple[str, ...]:
    quest_id_set = set(quest_ids)
    return tuple(quest_id for quest_id in FOUNDATION_QUEST_IDS if quest_id not in quest_id_set)


def quest_source_route(relative_path: Path) -> tuple[str, str]:
    parts = relative_path.parts
    if len(parts) != 4 or parts[0] != QUESTS_PATH.as_posix():
        fail(
            f"{questbook_relative(relative_path)}: quest source must live under quests/<lane>/<state>/"
        )
    lane = parts[1]
    state = parts[2]
    if lane not in QUEST_SOURCE_LANES:
        fail(
            f"{questbook_relative(relative_path)}: unsupported quest lane '{lane}'"
        )
    if state not in QUEST_LIFECYCLE_STATES:
        fail(
            f"{questbook_relative(relative_path)}: unsupported quest lifecycle state '{state}'"
        )
    return lane, state


def markdown_quest_key(quest_id: str) -> str:
    match = QUEST_MARKDOWN_KEY_RE.match(quest_id)
    return match.group(1) if match else quest_id


def expected_markdown_quest_lane(quest_id: str) -> str | None:
    for prefix, lane in QUEST_MARKDOWN_ID_LANES.items():
        if quest_id.startswith(prefix):
            return lane
    return None


def markdown_heading_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[f"## {match.group(1).strip()}"] = text[start:end].strip()
    return sections


def validate_quest_markdown_contract(relative_path: Path, text: str) -> None:
    lane, _state = quest_source_route(relative_path)
    quest_id = relative_path.stem
    expected_lane = expected_markdown_quest_lane(quest_id)
    if expected_lane is None:
        fail(
            f"{questbook_relative(relative_path)}: Markdown quest id must use a known lane prefix"
        )
    if expected_lane != lane:
        fail(
            f"{questbook_relative(relative_path)}: quest id routes to lane '{expected_lane}', not '{lane}'"
        )

    h1_match = QUEST_H1_RE.search(text)
    if h1_match is None:
        fail(f"{questbook_relative(relative_path)}: Markdown quest must start with an H1 title")
    if markdown_quest_key(quest_id) not in h1_match.group(1):
        fail(
            f"{questbook_relative(relative_path)}: H1 title must include the quest key"
        )

    if QUEST_MARKDOWN_CONTRACT_MARKER not in text:
        fail(
            f"{questbook_relative(relative_path)}: missing {QUEST_MARKDOWN_CONTRACT_MARKER}"
        )
    sections = markdown_heading_sections(text)
    for heading in QUEST_MARKDOWN_REQUIRED_HEADINGS:
        if heading not in sections:
            fail(
                f"{questbook_relative(relative_path)}: strict Markdown contract must include {heading}"
            )
        if heading in sections and not sections[heading]:
            fail(
                f"{questbook_relative(relative_path)}: strict Markdown contract section {heading} must not be empty"
            )


def validate_questbook_source_topology(repo_root: Path) -> None:
    quests_dir = repo_root / QUESTS_PATH
    if not quests_dir.is_dir():
        fail(f"{questbook_relative(QUESTS_PATH)}: missing required directory")

    for relative_path in (QUESTS_PATH / "README.md", QUESTS_PATH / "AGENTS.md"):
        if not (repo_root / relative_path).is_file():
            fail(f"{questbook_relative(relative_path)}: missing required file")

    for pattern in ("AOA-TECH-Q-*.yaml", "AOT-Q-*.md"):
        for path in sorted(quests_dir.glob(pattern)):
            if path.is_file():
                fail(
                    f"{questbook_relative(path.relative_to(repo_root))}: root-level quest aliases are not allowed"
                )

    for state in QUEST_LIFECYCLE_STATES:
        if (quests_dir / state).exists():
            fail(
                f"{questbook_relative(QUESTS_PATH / state)}: root lifecycle directories are not allowed"
            )

    for lane in QUEST_SOURCE_LANES:
        lane_dir = quests_dir / lane
        if lane_dir.exists():
            for filename in ("README.md", "AGENTS.md"):
                if not (lane_dir / filename).is_file():
                    fail(
                        f"{questbook_relative(QUESTS_PATH / lane / filename)}: missing required file"
                    )

    for path in sorted(quests_dir.rglob("*.yaml")):
        if not path.is_file():
            continue
        relative_path = path.relative_to(repo_root)
        lane, _state = quest_source_route(relative_path)
        if lane != "techniques":
            fail(
                f"{questbook_relative(relative_path)}: YAML work quests belong in the techniques lane"
            )
        if not path.name.startswith("AOA-TECH-Q-"):
            fail(
                f"{questbook_relative(relative_path)}: YAML quest source must use AOA-TECH-Q-*"
            )

    for path in sorted(quests_dir.rglob("*.md")):
        if not path.is_file() or path.name in {"README.md", "AGENTS.md"}:
            continue
        relative_path = path.relative_to(repo_root)
        quest_source_route(relative_path)
        validate_quest_markdown_contract(relative_path, read_text(path))


def discover_quest_source_paths(repo_root: Path) -> dict[str, Path]:
    quest_paths = sorted(
        (
            path
            for path in (repo_root / QUESTS_PATH).glob("**/AOA-TECH-Q-*.yaml")
            if path.is_file()
        ),
        key=lambda path: quest_id_sort_key(path.stem),
    )
    discovered: dict[str, Path] = {}
    for path in quest_paths:
        quest_id = path.stem
        if quest_id in discovered:
            fail(f"{quest_id}: duplicate quest id in quests/")
        discovered[quest_id] = path.relative_to(repo_root)
    return discovered


def questbook_relative(path: Path) -> str:
    return path.as_posix()


def validate_quest_schema_envelope(
    schema_path: Path,
    *,
    title: str,
    schema_version: str,
    required_fields: tuple[str, ...],
) -> None:
    if not schema_path.is_file():
        fail(f"{questbook_relative(schema_path)}: missing required file")
    payload = read_json(schema_path)
    if not isinstance(payload, dict):
        fail(f"{questbook_relative(schema_path)}: schema payload must be a JSON object")
    if payload.get("title") != title:
        fail(f"{questbook_relative(schema_path)}: schema title must be '{title}'")
    if payload.get("type") != "object":
        fail(f"{questbook_relative(schema_path)}: schema type must be 'object'")
    if payload.get("additionalProperties") is not False:
        fail(f"{questbook_relative(schema_path)}: schema must set additionalProperties to false")

    required = payload.get("required")
    if required != list(required_fields):
        fail(
            f"{questbook_relative(schema_path)}: schema required fields must stay aligned with the questbook contract"
        )

    properties = payload.get("properties")
    if not isinstance(properties, dict):
        fail(f"{questbook_relative(schema_path)}: schema properties must be an object")
    schema_version_entry = properties.get("schema_version")
    if not isinstance(schema_version_entry, dict) or schema_version_entry.get("const") != schema_version:
        fail(
            f"{questbook_relative(schema_path)}: schema_version must stay pinned to '{schema_version}'"
        )


def validate_quest_payload_for_projection(
    quest_id: str,
    payload: dict[str, Any],
    source_path: str,
) -> None:
    required_scalar_fields = (
        "title",
        "lane",
        "state",
        "band",
        "kind",
        "difficulty",
        "risk",
        "owner_surface",
        "control_mode",
        "delegate_tier",
        "write_scope",
    )
    for field in required_scalar_fields:
        value = payload.get(field)
        if not isinstance(value, str) or not value:
            fail(f"{source_path}: quest must define string field '{field}'")

    activation = payload.get("activation")
    if not isinstance(activation, dict):
        fail(f"{source_path}: quest must define object field 'activation'")
    activation_mode = activation.get("mode")
    if not isinstance(activation_mode, str) or not activation_mode:
        fail(f"{source_path}: quest must define string field 'activation.mode'")

    harvest = payload.get("harvest")
    if harvest is not None:
        if not isinstance(harvest, dict):
            fail(f"{source_path}: harvest must be an object when present")
        target = harvest.get("target")
        allowed_targets = {
            "none",
            "technique",
            "skill",
            "eval",
            "playbook",
            "agent_contract",
            "memo",
            "routing",
        }
        if not isinstance(target, str) or target not in allowed_targets:
            fail(
                f"{source_path}: harvest.target must be one of "
                f"{', '.join(sorted(allowed_targets))}"
            )


def validate_dispatch_entry_against_schema(
    entry: Any,
    *,
    schema: dict[str, Any],
    location: str,
) -> None:
    if not isinstance(entry, dict):
        fail(f"{location}: dispatch entries must be JSON objects")

    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail(f"{questbook_relative(QUEST_DISPATCH_SCHEMA_PATH)}: schema properties must be an object")

    required = schema.get("required")
    if not isinstance(required, list):
        fail(f"{questbook_relative(QUEST_DISPATCH_SCHEMA_PATH)}: schema required list is missing")

    missing = [field for field in required if field not in entry]
    if missing:
        fail(f"{location}: missing required field(s): {', '.join(missing)}")

    if schema.get("additionalProperties") is False:
        unexpected = sorted(set(entry) - set(properties))
        if unexpected:
            fail(f"{location}: unexpected field(s): {', '.join(unexpected)}")

    for field, value in entry.items():
        schema_entry = properties.get(field)
        if not isinstance(schema_entry, dict):
            continue
        if "const" in schema_entry and value != schema_entry["const"]:
            fail(f"{location}.{field}: value must equal '{schema_entry['const']}'")

        expected_type = schema_entry.get("type")
        if expected_type == "string":
            if not isinstance(value, str):
                fail(f"{location}.{field}: value must be a string")
            pattern = schema_entry.get("pattern")
            if isinstance(pattern, str) and re.fullmatch(pattern, value) is None:
                fail(f"{location}.{field}: value does not match pattern '{pattern}'")
        elif expected_type == "boolean":
            if not isinstance(value, bool):
                fail(f"{location}.{field}: value must be a boolean")
        elif expected_type == "array":
            if not isinstance(value, list):
                fail(f"{location}.{field}: value must be an array")
            item_schema = schema_entry.get("items")
            if isinstance(item_schema, dict) and item_schema.get("type") == "string":
                if not all(isinstance(item, str) for item in value):
                    fail(f"{location}.{field}: every item must be a string")

        enum_values = schema_entry.get("enum")
        if isinstance(enum_values, list) and value not in enum_values:
            formatted = ", ".join(str(item) for item in enum_values)
            fail(f"{location}.{field}: value must be one of {formatted}")


def build_expected_quest_catalog_entry(
    quest_id: str,
    payload: dict[str, Any],
    source_path: str,
) -> dict[str, Any]:
    return {
        "id": quest_id,
        "title": payload["title"],
        "repo": payload["repo"],
        "theme_ref": payload.get("theme_ref", ""),
        "milestone_ref": payload.get("milestone_ref", ""),
        "state": payload["state"],
        "band": payload["band"],
        "kind": payload["kind"],
        "difficulty": payload["difficulty"],
        "risk": payload["risk"],
        "owner_surface": payload["owner_surface"],
        "source_path": source_path,
        "public_safe": payload["public_safe"],
    }


def build_expected_quest_dispatch_entry(
    quest_id: str,
    payload: dict[str, Any],
    source_path: str,
) -> dict[str, Any]:
    validate_quest_payload_for_projection(quest_id, payload, source_path)
    requires_artifacts = QUEST_DISPATCH_ARTIFACTS.get(quest_id)
    if requires_artifacts is None:
        if payload.get("kind") == "harvest":
            requires_artifacts = ["recurrence_evidence", "promotion_decision"]
        else:
            requires_artifacts = ["bounded_plan", "work_result", "verification_result"]
    entry = {
        "schema_version": "quest_dispatch_v1",
        "id": quest_id,
        "repo": payload["repo"],
        "state": payload["state"],
        "band": payload["band"],
        "difficulty": payload["difficulty"],
        "risk": payload["risk"],
        "control_mode": payload["control_mode"],
        "delegate_tier": payload["delegate_tier"],
        "split_required": payload.get("split_required", False),
        "write_scope": payload["write_scope"],
        "requires_artifacts": requires_artifacts,
        "activation_mode": payload["activation"]["mode"],
        "source_path": source_path,
        "public_safe": payload["public_safe"],
    }
    if "fallback_tier" in payload:
        entry["fallback_tier"] = payload.get("fallback_tier")
    if "wrapper_class" in payload:
        entry["wrapper_class"] = payload.get("wrapper_class")
    return entry


def collect_questbook_payloads(
    repo_root: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Path], list[str], list[str]]:
    validate_questbook_source_topology(repo_root)
    quest_source_paths = discover_quest_source_paths(repo_root)
    quest_ids = tuple(quest_source_paths)
    missing_foundation_ids = missing_foundation_quest_ids(quest_ids)
    if missing_foundation_ids:
        missing_quest_id = missing_foundation_ids[0]
        fail(f"{missing_quest_id}.yaml: missing required file")

    quest_payloads: dict[str, dict[str, Any]] = {}
    active_quest_ids: list[str] = []
    closed_quest_ids: list[str] = []
    for quest_id in quest_ids:
        relative_path = quest_source_paths[quest_id]
        lane, state = quest_source_route(relative_path)
        quest_path = repo_root / relative_path
        if not quest_path.is_file():
            fail(f"{questbook_relative(quest_path.relative_to(repo_root))}: missing required file")
        payload = read_yaml(quest_path)
        if not isinstance(payload, dict):
            fail(f"{questbook_relative(quest_path.relative_to(repo_root))}: quest payload must be a YAML mapping")
        if payload.get("schema_version") != "work_quest_v1":
            fail(
                f"{questbook_relative(quest_path.relative_to(repo_root))}: schema_version must be 'work_quest_v1'"
            )
        if payload.get("id") != quest_id:
            fail(f"{questbook_relative(quest_path.relative_to(repo_root))}: id must be '{quest_id}'")
        if payload.get("repo") != "aoa-techniques":
            fail(
                f"{questbook_relative(quest_path.relative_to(repo_root))}: repo must be 'aoa-techniques'"
            )
        if payload.get("lane") != lane:
            fail(
                f"{questbook_relative(quest_path.relative_to(repo_root))}: lane must match path lane"
            )
        if payload.get("state") != state:
            fail(
                f"{questbook_relative(quest_path.relative_to(repo_root))}: state must match path state"
            )
        if payload.get("public_safe") is not True:
            fail(
                f"{questbook_relative(quest_path.relative_to(repo_root))}: public_safe must be true"
            )
        quest_payloads[quest_id] = payload
        if payload.get("state") in CLOSED_QUEST_STATES:
            closed_quest_ids.append(quest_id)
        else:
            active_quest_ids.append(quest_id)
    return quest_payloads, quest_source_paths, active_quest_ids, closed_quest_ids


def build_quest_catalog_projection(repo_root: Path) -> list[dict[str, Any]]:
    quest_payloads, quest_source_paths, _, _ = collect_questbook_payloads(repo_root)
    return [
        build_expected_quest_catalog_entry(
            quest_id,
            quest_payloads[quest_id],
            questbook_relative(quest_source_paths[quest_id]),
        )
        for quest_id in discover_quest_ids(repo_root)
    ]


def build_quest_dispatch_projection(repo_root: Path) -> list[dict[str, Any]]:
    quest_payloads, quest_source_paths, _, _ = collect_questbook_payloads(repo_root)
    return [
        build_expected_quest_dispatch_entry(
            quest_id,
            quest_payloads[quest_id],
            questbook_relative(quest_source_paths[quest_id]),
        )
        for quest_id in discover_quest_ids(repo_root)
    ]


def validate_questbook_surface(repo_root: Path) -> None:
    questbook_path = repo_root / QUESTBOOK_PATH
    integration_path = repo_root / QUESTBOOK_INTEGRATION_PATH
    live_catalog_path = repo_root / QUEST_CATALOG_PATH
    live_dispatch_path = repo_root / QUEST_DISPATCH_PATH
    catalog_path = repo_root / QUEST_CATALOG_EXAMPLE_PATH
    dispatch_path = repo_root / QUEST_DISPATCH_EXAMPLE_PATH

    for path in (
        questbook_path,
        integration_path,
        repo_root / QUEST_SCHEMA_PATH,
        repo_root / QUEST_DISPATCH_SCHEMA_PATH,
        live_catalog_path,
        live_dispatch_path,
        catalog_path,
        dispatch_path,
    ):
        if not path.is_file():
            fail(f"{questbook_relative(path.relative_to(repo_root))}: missing required file")

    validate_quest_schema_envelope(
        repo_root / QUEST_SCHEMA_PATH,
        title="work_quest_v1",
        schema_version="work_quest_v1",
        required_fields=QUEST_SCHEMA_REQUIRED_FIELDS,
    )
    validate_quest_schema_envelope(
        repo_root / QUEST_DISPATCH_SCHEMA_PATH,
        title="quest_dispatch_v1",
        schema_version="quest_dispatch_v1",
        required_fields=QUEST_DISPATCH_REQUIRED_FIELDS,
    )
    dispatch_schema = read_json(repo_root / QUEST_DISPATCH_SCHEMA_PATH)
    if not isinstance(dispatch_schema, dict):
        fail(f"{questbook_relative(QUEST_DISPATCH_SCHEMA_PATH)}: schema payload must be a JSON object")

    integration_text = read_text(integration_path)
    for token in QUESTBOOK_REQUIRED_INTEGRATION_TOKENS:
        if token not in integration_text:
            fail(
                f"{questbook_relative(QUESTBOOK_INTEGRATION_PATH)}: must mention '{token}' explicitly"
            )

    quest_payloads, _quest_source_paths, active_quest_ids, closed_quest_ids = collect_questbook_payloads(repo_root)

    questbook_text = read_text(questbook_path)
    for token in QUESTBOOK_REQUIRED_INDEX_TOKENS:
        if token not in questbook_text:
            fail(f"{questbook_relative(QUESTBOOK_PATH)}: must mention '{token}' explicitly")
    for quest_id in active_quest_ids:
        if quest_id not in questbook_text:
            fail(f"{questbook_relative(QUESTBOOK_PATH)}: must reference active quest id '{quest_id}'")
    for quest_id in closed_quest_ids:
        if quest_id in questbook_text:
            fail(f"{questbook_relative(QUESTBOOK_PATH)}: must not list closed quest id '{quest_id}'")

    expected_catalog = build_quest_catalog_projection(repo_root)
    live_catalog_payload = read_json(live_catalog_path)
    if not isinstance(live_catalog_payload, list):
        fail(f"{questbook_relative(QUEST_CATALOG_PATH)}: payload must be a JSON array")
    if live_catalog_payload != expected_catalog:
        fail(
            f"{questbook_relative(QUEST_CATALOG_PATH)}: live catalog must stay aligned with quests/<lane>/<state>/*.yaml"
        )

    catalog_payload = read_json(catalog_path)
    if not isinstance(catalog_payload, list):
        fail(f"{questbook_relative(QUEST_CATALOG_EXAMPLE_PATH)}: payload must be a JSON array")
    if catalog_payload != expected_catalog:
        fail(
            f"{questbook_relative(QUEST_CATALOG_EXAMPLE_PATH)}: example catalog must stay aligned with quests/<lane>/<state>/*.yaml"
        )
    if catalog_payload != live_catalog_payload:
        fail(
            f"{questbook_relative(QUEST_CATALOG_EXAMPLE_PATH)}: example catalog must match {questbook_relative(QUEST_CATALOG_PATH)}"
        )

    expected_dispatch = build_quest_dispatch_projection(repo_root)
    expected_dispatch_by_id = {
        entry["id"]: entry for entry in expected_dispatch if isinstance(entry, dict) and "id" in entry
    }
    expected_dispatch_ids = [entry["id"] for entry in expected_dispatch if isinstance(entry, dict)]
    live_dispatch_payload = read_json(live_dispatch_path)
    if not isinstance(live_dispatch_payload, list):
        fail(f"{questbook_relative(QUEST_DISPATCH_PATH)}: payload must be a JSON array")
    if len(live_dispatch_payload) != len(expected_dispatch):
        fail(
            f"{questbook_relative(QUEST_DISPATCH_PATH)}: expected {len(expected_dispatch)} dispatch entries"
        )
    for index, (entry, quest_id) in enumerate(zip(live_dispatch_payload, expected_dispatch_ids, strict=True)):
        validate_dispatch_entry_against_schema(
            entry,
            schema=dispatch_schema,
            location=f"{questbook_relative(QUEST_DISPATCH_PATH)}[{index}]",
        )
        requires_artifacts = entry.get("requires_artifacts")
        if not isinstance(requires_artifacts, list) or not requires_artifacts or not all(
            isinstance(item, str) and item for item in requires_artifacts
        ):
            fail(
                f"{questbook_relative(QUEST_DISPATCH_PATH)}: dispatch entry '{quest_id}' must keep a non-empty requires_artifacts list"
            )
        expected_entry = expected_dispatch_by_id[quest_id]
        if entry != expected_entry:
            fail(
                f"{questbook_relative(QUEST_DISPATCH_PATH)}: dispatch entry '{quest_id}' must stay aligned with quests/<lane>/<state>/*.yaml"
            )

    dispatch_payload = read_json(dispatch_path)
    if not isinstance(dispatch_payload, list):
        fail(f"{questbook_relative(QUEST_DISPATCH_EXAMPLE_PATH)}: payload must be a JSON array")
    for index, entry in enumerate(dispatch_payload):
        validate_dispatch_entry_against_schema(
            entry,
            schema=dispatch_schema,
            location=f"{questbook_relative(QUEST_DISPATCH_EXAMPLE_PATH)}[{index}]",
        )
    if dispatch_payload != expected_dispatch:
        fail(
            f"{questbook_relative(QUEST_DISPATCH_EXAMPLE_PATH)}: example dispatch must stay aligned with quests/<lane>/<state>/*.yaml"
        )
    if dispatch_payload != live_dispatch_payload:
        fail(
            f"{questbook_relative(QUEST_DISPATCH_EXAMPLE_PATH)}: example dispatch must match {questbook_relative(QUEST_DISPATCH_PATH)}"
        )


