from __future__ import annotations

from .common import *
from .source_contracts import *

INTELLIGENCE_BANNED_KEYS = {
    "activate",
    "activation",
    "invocation",
    "invoke",
    "invoked",
}

def validate_no_banned_intelligence_keys(value: Any, location: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in INTELLIGENCE_BANNED_KEYS:
                fail(f"{location}: Technique Intelligence registry must not expose '{key}' keys")
            validate_no_banned_intelligence_keys(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_no_banned_intelligence_keys(child, f"{location}[{index}]")

def validate_technique_intelligence(
    repo_root: Path, records: list[TechniqueRecord], schema_store: dict[str, Any]
) -> None:
    try:
        from technique_intelligence_surface import (
            DAG_MIN_PATH,
            DAG_PATH,
            READER_PATH,
            REGISTRY_MIN_PATH,
            REGISTRY_PATH,
            build_all_outputs,
            project_min_dag_payload,
            project_min_registry_payload,
        )
    except ModuleNotFoundError:
        from scripts.technique_intelligence_surface import (
            DAG_MIN_PATH,
            DAG_PATH,
            READER_PATH,
            REGISTRY_MIN_PATH,
            REGISTRY_PATH,
            build_all_outputs,
            project_min_dag_payload,
            project_min_registry_payload,
        )

    expected = build_all_outputs(repo_root)
    actual_registry = read_json(repo_root / REGISTRY_PATH)
    actual_registry_min = read_json(repo_root / REGISTRY_MIN_PATH)
    actual_dag = read_json(repo_root / DAG_PATH)
    actual_dag_min = read_json(repo_root / DAG_MIN_PATH)
    actual_reader = read_text(repo_root / READER_PATH)

    if actual_registry != expected["registry"]:
        fail(
            f"{repo_root / REGISTRY_PATH}: generated Technique Intelligence registry is out of date; "
            "run 'python scripts/build_technique_intelligence.py'"
        )
    if actual_registry_min != expected["registry_min"]:
        fail(
            f"{repo_root / REGISTRY_MIN_PATH}: generated Technique Intelligence min registry is out of date; "
            "run 'python scripts/build_technique_intelligence.py'"
        )
    if actual_dag != expected["dag"]:
        fail(
            f"{repo_root / DAG_PATH}: generated Technique Intelligence DAG is out of date; "
            "run 'python scripts/build_technique_intelligence.py'"
        )
    if actual_dag_min != expected["dag_min"]:
        fail(
            f"{repo_root / DAG_MIN_PATH}: generated Technique Intelligence min DAG is out of date; "
            "run 'python scripts/build_technique_intelligence.py'"
        )
    if actual_reader != expected["reader"]:
        fail(
            f"{repo_root / READER_PATH}: generated Technique Intelligence reader is out of date; "
            "run 'python scripts/build_technique_intelligence.py'"
        )

    registry_schema = resolve_schema_ref("technique_intelligence_registry.schema.json", schema_store)
    dag_schema = resolve_schema_ref("technique_intelligence_dag.schema.json", schema_store)
    validate_schema_instance(actual_registry, registry_schema, str(repo_root / REGISTRY_PATH), schema_store)
    validate_schema_instance(actual_dag, dag_schema, str(repo_root / DAG_PATH), schema_store)

    if project_min_registry_payload(actual_registry) != actual_registry_min:
        fail(f"{repo_root / REGISTRY_MIN_PATH}: min registry must stay a projection of full registry")
    if project_min_dag_payload(actual_dag) != actual_dag_min:
        fail(f"{repo_root / DAG_MIN_PATH}: min DAG must stay a projection of full DAG")

    record_ids = [record.id for record in sorted(records, key=lambda record: record.id)]
    registry_ids = [entry["id"] for entry in actual_registry["techniques"]]
    if registry_ids != record_ids:
        fail(f"{repo_root / REGISTRY_PATH}: registry IDs must stay aligned with collected techniques")
    if actual_registry["technique_count"] != len(records):
        fail(f"{repo_root / REGISTRY_PATH}: technique_count must match collected techniques")

    validate_no_banned_intelligence_keys(actual_registry, str(repo_root / REGISTRY_PATH))
    for entry in actual_registry["techniques"]:
        hints = entry["topology"]["hints"]
        if hints.get("authority") != "scout_only_non_authoritative":
            fail(f"{entry['id']}: topology hints must stay scout-only")
        if entry["move"].get("unit") != "attention_bounded_atomic_move":
            fail(f"{entry['id']}: registry move unit must stay attention-bounded")
        for document in entry["search_documents"]:
            if document["technique_id"] != entry["id"]:
                fail(f"{entry['id']}: search document technique_id mismatch")
            if not document["text"].strip():
                fail(f"{entry['id']}: search document text must not be empty")
            if not document["source_ref"].strip():
                fail(f"{entry['id']}: search document source_ref must not be empty")

    if actual_dag["node_count"] != len(actual_dag["nodes"]):
        fail(f"{repo_root / DAG_PATH}: node_count must match nodes length")
    if actual_dag["edge_count"] != len(actual_dag["edges"]):
        fail(f"{repo_root / DAG_PATH}: edge_count must match edges length")
