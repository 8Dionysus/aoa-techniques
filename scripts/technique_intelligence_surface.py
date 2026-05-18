from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REGISTRY_VERSION = 1
DAG_VERSION = 1
AUTHORITY_NOTE = (
    "Technique Intelligence is attention over source moves. It helps agents find, explain, "
    "pack, and route atomic techniques; authored TECHNIQUE.md bundles remain stronger."
)
REGISTRY_SOURCE_OF_TRUTH = {
    "primary": "techniques/**/TECHNIQUE.md",
    "catalog": "generated/technique_catalog.json",
    "capsules": "generated/technique_capsules.json",
    "sections": "generated/technique_sections.full.json",
    "support_manifests": [
        "generated/technique_checklist_manifest.json",
        "generated/technique_example_manifest.json",
        "generated/technique_evidence_note_manifest.json",
    ],
    "review_manifests": [
        "generated/semantic_review_manifest.json",
        "generated/shadow_review_manifest.json",
    ],
    "scout_inputs": [
        "mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json",
        "mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.json",
        "mechanics/distillation/parts/technique-reform-ingress/reports/technique_family_scout.json",
        "mechanics/distillation/parts/technique-reform-ingress/reviews/execution-profile-fixture-sketch-ledger.md",
    ],
}

REGISTRY_PATH = Path("generated/technique_intelligence_registry.json")
REGISTRY_MIN_PATH = Path("generated/technique_intelligence_registry.min.json")
DAG_PATH = Path("generated/technique_intelligence_dag.json")
DAG_MIN_PATH = Path("generated/technique_intelligence_dag.min.json")
READER_PATH = Path("docs/readers/intelligence/TECHNIQUE_INTELLIGENCE.md")

MOVE_SECTION_KEYS = (
    "intent",
    "when_to_use",
    "when_not_to_use",
    "inputs",
    "outputs",
    "core_procedure",
    "contracts",
    "risks",
    "validation",
)

MOVE_LABELS = {
    "intent": "Intent",
    "when_to_use": "When to use",
    "when_not_to_use": "When not to use",
    "inputs": "Inputs",
    "outputs": "Outputs",
    "core_procedure": "Core procedure",
    "contracts": "Contracts",
    "risks": "Risks",
    "validation": "Validation",
}

CAPSULE_FIELDS = (
    "one_line_intent",
    "use_when_short",
    "do_not_use_short",
    "inputs_short",
    "outputs_short",
    "core_contract_short",
    "main_risk_short",
    "validation_short",
)

PROFILE_NAMES = (
    "capsule",
    "small-agent",
    "orchestrator",
    "workflow-handoff",
    "eval-fixture",
)

ROUTE_AWAY_BOUNDARIES = (
    {
        "object_class": "execution_workflow",
        "owner": "nearest workflow or agent-lane owner",
        "cue": "the request asks for a repeatable run path rather than one atomic move",
    },
    {
        "object_class": "proof_verdict",
        "owner": "aoa-evals",
        "cue": "the request asks whether a result is good enough or should pass a gate",
    },
    {
        "object_class": "dispatch_policy",
        "owner": "aoa-routing",
        "cue": "the request asks for global next-surface routing or dispatcher behavior",
    },
    {
        "object_class": "runtime_behavior",
        "owner": "abyss-stack",
        "cue": "the request asks for deployment, service, storage, or lifecycle behavior",
    },
    {
        "object_class": "agent_role_contract",
        "owner": "aoa-agents",
        "cue": "the request asks what an agent role is allowed or expected to be",
    },
    {
        "object_class": "scenario_composition",
        "owner": "aoa-playbooks",
        "cue": "the request asks for a recurring scenario, campaign, or multi-step choreography",
    },
    {
        "object_class": "knowledge_graph_semantics",
        "owner": "aoa-kag",
        "cue": "the request asks for graph truth, inference, or provenance substrate semantics",
    },
    {
        "object_class": "ecosystem_doctrine",
        "owner": "Agents-of-Abyss",
        "cue": "the request asks for AoA constitutional or layer identity doctrine",
    },
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def write_json(path: Path, payload: Any, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if compact:
        encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    else:
        encoded = json.dumps(payload, ensure_ascii=True, indent=2)
    path.write_text(encoded + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compact_text(text: str, *, max_chars: int = 1800) -> str:
    compacted = re.sub(r"\s+", " ", text).strip()
    if len(compacted) <= max_chars:
        return compacted
    return compacted[: max_chars - 3].rstrip() + "..."


def snippet_for(text: str, terms: list[str], *, max_chars: int = 220) -> str:
    compacted = compact_text(text, max_chars=4000)
    lower = compacted.lower()
    positions = [lower.find(term) for term in terms if lower.find(term) >= 0]
    start = max(0, min(positions) - 60) if positions else 0
    snippet = compacted[start : start + max_chars].strip()
    if start > 0:
        snippet = "..." + snippet
    if start + max_chars < len(compacted):
        snippet += "..."
    return snippet


def source_ref(path: str, anchor: str | None = None) -> str:
    if anchor is None or anchor == "":
        return path
    normalized = re.sub(r"[^a-z0-9]+", "-", anchor.lower()).strip("-")
    return f"{path}#{normalized}"


def load_payloads(repo_root: Path) -> dict[str, Any]:
    reports_root = repo_root / "mechanics/distillation/parts/technique-reform-ingress/reports"
    return {
        "catalog": read_json(repo_root / "generated/technique_catalog.json"),
        "capsules": read_json(repo_root / "generated/technique_capsules.json"),
        "sections": read_json(repo_root / "generated/technique_sections.full.json"),
        "checklists": read_json(repo_root / "generated/technique_checklist_manifest.json"),
        "examples": read_json(repo_root / "generated/technique_example_manifest.json"),
        "evidence_notes": read_json(repo_root / "generated/technique_evidence_note_manifest.json"),
        "semantic_reviews": read_json(repo_root / "generated/semantic_review_manifest.json"),
        "shadow_reviews": read_json(repo_root / "generated/shadow_review_manifest.json"),
        "topology_scout": read_json(reports_root / "technique_topology_scout.json"),
        "tree_projection": read_json(reports_root / "technique_tree_projection.json"),
        "family_scout": read_json(reports_root / "technique_family_scout.json"),
    }


def by_id(entries: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {entry["id"]: entry for entry in entries}


def section_lookup(section_entry: dict[str, Any]) -> dict[str, dict[str, str]]:
    return {section["key"]: section for section in section_entry.get("sections", [])}


def note_text(note: dict[str, Any]) -> str:
    parts = [note.get("title", ""), note.get("kind", "")]
    if note.get("intro_markdown"):
        parts.append(note["intro_markdown"])
    if note.get("body_markdown"):
        parts.append(note["body_markdown"])
    for section in note.get("sections", []):
        parts.append(section.get("heading", ""))
        for field in section.get("fields", []):
            parts.append(f"{field.get('key', '')}: {field.get('value_markdown', '')}")
        for item in section.get("items", []):
            parts.append(item.get("text", ""))
        if section.get("markdown"):
            parts.append(section["markdown"])
    return "\n".join(part for part in parts if part)


def checklist_text(checklist: dict[str, Any]) -> str:
    parts = [checklist.get("title", ""), checklist.get("intro_markdown", "")]
    parts.extend(item.get("text", "") for item in checklist.get("items", []))
    return "\n".join(part for part in parts if part)


def parse_fixture_sketches(repo_root: Path) -> dict[str, dict[str, str]]:
    ledger_path = (
        repo_root
        / "mechanics/distillation/parts/technique-reform-ingress/reviews/execution-profile-fixture-sketch-ledger.md"
    )
    if not ledger_path.exists():
        return {}

    fixtures: dict[str, dict[str, str]] = {}
    row_pattern = re.compile(
        r"^\| `(?P<id>AOA-T-\d{4})` `(?P<name>[^`]+)` "
        r"\| (?P<class>[^|]+) "
        r"\| (?P<inputs>[^|]+) "
        r"\| (?P<forbidden>[^|]+) "
        r"\| (?P<expected>[^|]+) "
        r"\| (?P<cue>[^|]+) \|$"
    )
    for line in read_text(ledger_path).splitlines():
        match = row_pattern.match(line.strip())
        if not match:
            continue
        values = {key: value.strip() for key, value in match.groupdict().items()}
        fixtures[values["id"]] = {
            "source_ref": ledger_path.relative_to(repo_root).as_posix(),
            "technique_name": values["name"],
            "fixture_class": values["class"],
            "minimal_input_and_allowed_context": values["inputs"],
            "forbidden_hidden_context_and_trap": values["forbidden"],
            "expected_output": values["expected"],
            "pass_fail_cue_and_owner_warning": values["cue"],
        }
    return fixtures


def build_review_index(payload: dict[str, Any], review_kind: str) -> dict[str, list[dict[str, Any]]]:
    indexed: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for review in payload.get("reviews", []):
        for map_entry in review.get("map_entries", []):
            technique_id = map_entry.get("technique_id")
            if not technique_id:
                continue
            indexed[technique_id].append(
                {
                    "review_kind": review_kind,
                    "review_id": review.get("review_id"),
                    "review_path": review.get("review_path"),
                    "title": review.get("title"),
                    "current_role": map_entry.get("current_role"),
                    **(
                        {"current_shadow_seam": map_entry.get("current_shadow_seam")}
                        if map_entry.get("current_shadow_seam")
                        else {}
                    ),
                    "overall_outcome": review.get("overall_outcome"),
                    "finding_count": len(review.get("findings", [])),
                    "seam_count": len(review.get("seams", [])),
                }
            )
    return indexed


def add_search_doc(
    docs: list[dict[str, Any]],
    *,
    technique_id: str,
    document_type: str,
    source: str,
    text: str,
    section_key: str | None = None,
    section_name: str | None = None,
    order: int,
) -> None:
    if not compact_text(text, max_chars=80):
        return
    document_id = f"{technique_id}:{document_type}:{order:03d}"
    docs.append(
        {
            "document_id": document_id,
            "technique_id": technique_id,
            "document_type": document_type,
            **({"section_key": section_key} if section_key else {}),
            **({"section_name": section_name} if section_name else {}),
            "source_ref": source,
            "text": compact_text(text),
            "content_hash": sha256_text(text),
        }
    )


def build_support_refs_and_docs(
    technique_id: str,
    manifests: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    support_refs: dict[str, list[dict[str, Any]]] = {
        "checklists": [],
        "examples": [],
        "evidence_notes": [],
    }
    search_docs: list[dict[str, Any]] = []

    checklist_entry = manifests["checklists"].get(technique_id, {})
    for order, checklist in enumerate(checklist_entry.get("checklists", []), start=1):
        support_refs["checklists"].append(
            {
                "path": checklist["check_path"],
                "title": checklist["title"],
                "item_count": len(checklist.get("items", [])),
            }
        )
        add_search_doc(
            search_docs,
            technique_id=technique_id,
            document_type="checklist",
            source=checklist["check_path"],
            text=checklist_text(checklist),
            section_name=checklist["title"],
            order=order,
        )

    example_entry = manifests["examples"].get(technique_id, {})
    for order, example in enumerate(example_entry.get("examples", []), start=1):
        support_refs["examples"].append(
            {
                "path": example["example_path"],
                "title": example["title"],
                "body_hash": sha256_text(example.get("body_markdown", "")),
            }
        )
        add_search_doc(
            search_docs,
            technique_id=technique_id,
            document_type="example",
            source=example["example_path"],
            text=f"{example.get('title', '')}\n{example.get('body_markdown', '')}",
            section_name=example.get("title"),
            order=order,
        )

    evidence_entry = manifests["evidence_notes"].get(technique_id, {})
    for order, note in enumerate(evidence_entry.get("notes", []), start=1):
        support_refs["evidence_notes"].append(
            {
                "path": note["note_path"],
                "kind": note["kind"],
                "title": note["title"],
                "shape": note["note_shape"],
            }
        )
        add_search_doc(
            search_docs,
            technique_id=technique_id,
            document_type="evidence_note",
            source=note["note_path"],
            text=note_text(note),
            section_name=note.get("title"),
            order=order,
        )

    return support_refs, search_docs


def build_entry(
    repo_root: Path,
    catalog_entry: dict[str, Any],
    *,
    capsule: dict[str, Any],
    section_entry: dict[str, Any],
    topology_entry: dict[str, Any],
    tree_entry: dict[str, Any],
    family_summary_by_name: dict[str, str],
    fixture: dict[str, str] | None,
    support_refs: dict[str, list[dict[str, Any]]],
    support_search_docs: list[dict[str, Any]],
    semantic_refs: list[dict[str, Any]],
    shadow_refs: list[dict[str, Any]],
) -> dict[str, Any]:
    technique_id = catalog_entry["id"]
    technique_path = catalog_entry["technique_path"]
    source_text = read_text(repo_root / technique_path)
    sections = section_lookup(section_entry)
    source_refs = [
        {
            "field": key,
            "source_ref": source_ref(technique_path, MOVE_LABELS[key]),
            "content_hash": sha256_text(sections[key]["content_markdown"]),
        }
        for key in MOVE_SECTION_KEYS
        if key in sections
    ]

    move = {
        "unit": "attention_bounded_atomic_move",
        "summary": catalog_entry["summary"],
        "intent": sections["intent"]["content_markdown"],
        "applies_when": sections["when_to_use"]["content_markdown"],
        "does_not_apply_when": sections["when_not_to_use"]["content_markdown"],
        "inputs": sections["inputs"]["content_markdown"],
        "outputs": sections["outputs"]["content_markdown"],
        "procedure": sections["core_procedure"]["content_markdown"],
        "contracts": sections["contracts"]["content_markdown"],
        "risks": sections["risks"]["content_markdown"],
        "validation": sections["validation"]["content_markdown"],
        "stop_line": (
            "Stop at the source bundle's stated output and validation boundary; route away "
            "when the request becomes workflow execution, verdict, role law, runtime, or graph truth."
        ),
        "source_refs": source_refs,
    }

    topology = topology_entry.get("topology", {})
    topology_hints = {
        "authority": "scout_only_non_authoritative",
        "family": topology.get("family"),
        "family_summary": family_summary_by_name.get(topology.get("family")),
        "capability_class": topology.get("capability_class", []),
        "substrate": topology.get("substrate", []),
        "execution_profile": topology.get("execution_profile"),
        "risk_posture": topology.get("risk_posture", []),
        "source_refs": [
            "mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json",
            "mechanics/distillation/parts/technique-reform-ingress/reports/technique_family_scout.json",
        ],
    }

    direct_relations = [
        {
            "type": relation["type"],
            "target": relation["target"],
            "authority": "frontmatter_direct_relation",
            "source_ref": source_ref(technique_path, "relations"),
        }
        for relation in catalog_entry.get("relations", [])
    ]

    next_load_refs = [
        {"role": "source_bundle", "path": technique_path},
        {"role": "capsule", "path": f"generated/technique_capsules.json#{technique_id}"},
        {"role": "sections", "path": f"generated/technique_sections.full.json#{technique_id}"},
    ]
    for ref in support_refs["checklists"][:1]:
        next_load_refs.append({"role": "checklist", "path": ref["path"]})
    for ref in support_refs["examples"][:1]:
        next_load_refs.append({"role": "example", "path": ref["path"]})
    for ref in support_refs["evidence_notes"][:2]:
        next_load_refs.append({"role": ref["kind"], "path": ref["path"]})

    search_docs: list[dict[str, Any]] = []
    add_search_doc(
        search_docs,
        technique_id=technique_id,
        document_type="identity",
        source=source_ref(technique_path, "frontmatter"),
        text=" ".join(
            [
                technique_id,
                catalog_entry["name"],
                catalog_entry["domain"],
                catalog_entry["kind"],
                catalog_entry["status"],
                catalog_entry["summary"],
                " ".join(catalog_entry.get("tags", [])),
            ]
        ),
        section_name="frontmatter",
        order=1,
    )
    add_search_doc(
        search_docs,
        technique_id=technique_id,
        document_type="capsule",
        source=f"generated/technique_capsules.json#{technique_id}",
        text="\n".join(str(capsule.get(key, "")) for key in ("summary", *CAPSULE_FIELDS)),
        section_name="capsule",
        order=2,
    )
    for order, key in enumerate(MOVE_SECTION_KEYS, start=10):
        section = sections.get(key)
        if section:
            add_search_doc(
                search_docs,
                technique_id=technique_id,
                document_type=key,
                source=source_ref(technique_path, section["heading"]),
                text=section["content_markdown"],
                section_key=key,
                section_name=section["heading"],
                order=order,
            )
    add_search_doc(
        search_docs,
        technique_id=technique_id,
        document_type="topology_hints",
        source="mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json",
        text=" ".join(
            [
                str(topology_hints.get("family") or ""),
                str(topology_hints.get("execution_profile") or ""),
                " ".join(topology_hints.get("capability_class", [])),
                " ".join(topology_hints.get("substrate", [])),
                " ".join(topology_hints.get("risk_posture", [])),
                str(topology_hints.get("family_summary") or ""),
            ]
        ),
        section_name="topology hints",
        order=90,
    )
    search_docs.extend(support_search_docs)

    for order, review_ref in enumerate(semantic_refs, start=120):
        add_search_doc(
            search_docs,
            technique_id=technique_id,
            document_type="semantic_review",
            source=review_ref["review_path"],
            text=" ".join(
                str(review_ref.get(key) or "")
                for key in ("title", "current_role", "overall_outcome")
            ),
            section_name=review_ref.get("title"),
            order=order,
        )
    for order, review_ref in enumerate(shadow_refs, start=140):
        add_search_doc(
            search_docs,
            technique_id=technique_id,
            document_type="shadow_review",
            source=review_ref["review_path"],
            text=" ".join(
                str(review_ref.get(key) or "")
                for key in ("title", "current_role", "current_shadow_seam", "overall_outcome")
            ),
            section_name=review_ref.get("title"),
            order=order,
        )

    if fixture:
        add_search_doc(
            search_docs,
            technique_id=technique_id,
            document_type="fixture_sketch",
            source=fixture["source_ref"],
            text=" ".join(
                fixture.get(key, "")
                for key in (
                    "fixture_class",
                    "minimal_input_and_allowed_context",
                    "forbidden_hidden_context_and_trap",
                    "expected_output",
                    "pass_fail_cue_and_owner_warning",
                )
            ),
            section_name="execution profile fixture sketch",
            order=160,
        )

    return {
        "id": technique_id,
        "name": catalog_entry["name"],
        "status": catalog_entry["status"],
        "domain": catalog_entry["domain"],
        "kind": catalog_entry["kind"],
        "summary": catalog_entry["summary"],
        "technique_path": technique_path,
        "source": {
            "primary_source_ref": technique_path,
            "source_hash": sha256_text(source_text),
            "catalog_ref": f"generated/technique_catalog.json#{technique_id}",
            "capsule_ref": f"generated/technique_capsules.json#{technique_id}",
            "section_ref": f"generated/technique_sections.full.json#{technique_id}",
        },
        "move": move,
        "capsule": {key: capsule[key] for key in ("summary", *CAPSULE_FIELDS)},
        "topology": {
            "truth": {
                "domain": catalog_entry["domain"],
                "kind": catalog_entry["kind"],
                "relations": "frontmatter_direct_only",
            },
            "tree_projection": {
                "authority": "projection_only_non_authoritative",
                "current_path": tree_entry.get("current_path"),
                "proposed_future_path": tree_entry.get("proposed_future_path"),
                "review_status": tree_entry.get("review_status"),
                "stop_line": tree_entry.get("stop_line"),
                "source_ref": (
                    "mechanics/distillation/parts/technique-reform-ingress/reports/"
                    "technique_tree_projection.json"
                ),
            },
            "hints": topology_hints,
        },
        "relations": {
            "authority": "frontmatter_direct_only",
            "direct": direct_relations,
        },
        "support_refs": support_refs,
        "review_refs": {
            "semantic": semantic_refs,
            "shadow": shadow_refs,
        },
        "fixture_refs": [fixture] if fixture else [],
        "owner_boundaries": {
            "this_repo_owns": [
                "atomic technique meaning",
                "source-linked move sections",
                "direct relation handles",
                "derived lookup packets weaker than source",
            ],
            "route_away": list(ROUTE_AWAY_BOUNDARIES),
            "stop_line": (
                "Use this entry to select or explain one move. Do not treat it as execution, "
                "proof, role, route, runtime, memory, or graph authority."
            ),
        },
        "next_load_refs": next_load_refs,
        "search_documents": search_docs,
    }


def build_technique_intelligence_registry_payload(repo_root: Path) -> dict[str, Any]:
    payloads = load_payloads(repo_root)
    catalog_by_id = by_id(payloads["catalog"]["techniques"])
    capsule_by_id = by_id(payloads["capsules"]["techniques"])
    sections_by_id = by_id(payloads["sections"]["techniques"])
    topology_by_id = by_id(payloads["topology_scout"]["techniques"])
    tree_by_id = by_id(payloads["tree_projection"]["techniques"])
    family_summary_by_name = {
        family["family"]: family.get("summary", "") for family in payloads["family_scout"].get("families", [])
    }
    manifests = {
        "checklists": by_id(payloads["checklists"]["techniques"]),
        "examples": by_id(payloads["examples"]["techniques"]),
        "evidence_notes": by_id(payloads["evidence_notes"]["techniques"]),
    }
    semantic_index = build_review_index(payloads["semantic_reviews"], "semantic")
    shadow_index = build_review_index(payloads["shadow_reviews"], "shadow")
    fixtures = parse_fixture_sketches(repo_root)

    entries = []
    for technique_id in sorted(catalog_by_id):
        support_refs, support_search_docs = build_support_refs_and_docs(technique_id, manifests)
        entries.append(
            build_entry(
                repo_root,
                catalog_by_id[technique_id],
                capsule=capsule_by_id[technique_id],
                section_entry=sections_by_id[technique_id],
                topology_entry=topology_by_id[technique_id],
                tree_entry=tree_by_id[technique_id],
                family_summary_by_name=family_summary_by_name,
                fixture=fixtures.get(technique_id),
                support_refs=support_refs,
                support_search_docs=support_search_docs,
                semantic_refs=semantic_index.get(technique_id, []),
                shadow_refs=shadow_index.get(technique_id, []),
            )
        )

    return {
        "registry_version": REGISTRY_VERSION,
        "authority": AUTHORITY_NOTE,
        "source_of_truth": REGISTRY_SOURCE_OF_TRUTH,
        "technique_count": len(entries),
        "generated_from": {
            "catalog_version": payloads["catalog"].get("catalog_version"),
            "capsule_version": payloads["capsules"].get("capsule_version"),
            "section_version": payloads["sections"].get("section_version"),
            "topology_scout_status": payloads["topology_scout"].get("status"),
            "tree_projection_status": payloads["tree_projection"].get("status"),
        },
        "techniques": entries,
    }


def project_min_registry_payload(full_payload: dict[str, Any]) -> dict[str, Any]:
    techniques = []
    for entry in full_payload["techniques"]:
        search_text = compact_text(
            " ".join(document["text"] for document in entry["search_documents"]),
            max_chars=1200,
        )
        techniques.append(
            {
                "id": entry["id"],
                "name": entry["name"],
                "status": entry["status"],
                "domain": entry["domain"],
                "kind": entry["kind"],
                "summary": entry["summary"],
                "technique_path": entry["technique_path"],
                "move": {
                    "unit": entry["move"]["unit"],
                    "intent": compact_text(entry["move"]["intent"], max_chars=260),
                    "applies_when": compact_text(entry["move"]["applies_when"], max_chars=260),
                    "does_not_apply_when": compact_text(
                        entry["move"]["does_not_apply_when"], max_chars=260
                    ),
                    "inputs": compact_text(entry["move"]["inputs"], max_chars=220),
                    "outputs": compact_text(entry["move"]["outputs"], max_chars=220),
                    "stop_line": entry["move"]["stop_line"],
                    "validation": compact_text(entry["move"]["validation"], max_chars=300),
                    "main_risk": compact_text(entry["move"]["risks"], max_chars=300),
                },
                "topology_hints": {
                    "authority": entry["topology"]["hints"]["authority"],
                    "family": entry["topology"]["hints"].get("family"),
                    "execution_profile": entry["topology"]["hints"].get("execution_profile"),
                    "risk_posture": entry["topology"]["hints"].get("risk_posture", []),
                },
                "direct_relations": [
                    {"type": relation["type"], "target": relation["target"]}
                    for relation in entry["relations"]["direct"]
                ],
                "next_load_refs": entry["next_load_refs"][:4],
                "search_text": search_text,
            }
        )
    return {
        "registry_version": full_payload["registry_version"],
        "authority": full_payload["authority"],
        "source_of_truth": full_payload["source_of_truth"],
        "technique_count": full_payload["technique_count"],
        "techniques": techniques,
    }


def build_technique_intelligence_dag_payload(
    registry_payload: dict[str, Any],
) -> dict[str, Any]:
    nodes: dict[str, dict[str, Any]] = {
        "repo:aoa-techniques": {
            "id": "repo:aoa-techniques",
            "node_type": "repo",
            "label": "aoa-techniques",
            "authority": "source_owner",
        }
    }
    edges: list[dict[str, Any]] = []
    relation_hints: list[dict[str, Any]] = []

    def add_node(node_id: str, node_type: str, label: str, **extra: Any) -> None:
        nodes.setdefault(
            node_id,
            {"id": node_id, "node_type": node_type, "label": label, **extra},
        )

    def add_edge(source: str, target: str, edge_type: str, authority: str) -> None:
        edges.append(
            {
                "source": source,
                "target": target,
                "edge_type": edge_type,
                "authority": authority,
            }
        )

    for entry in registry_payload["techniques"]:
        domain_id = f"domain:{entry['domain']}"
        kind_id = f"{domain_id}:kind:{entry['kind']}"
        family = entry["topology"]["hints"].get("family") or "unscouted"
        family_id = f"{kind_id}:family:{family}"
        technique_node_id = f"technique:{entry['id']}"
        source_node_id = f"source:{entry['id']}"
        capsule_node_id = f"capsule:{entry['id']}"
        support_node_id = f"support:{entry['id']}"

        add_node(domain_id, "domain", entry["domain"], authority="frontmatter_truth")
        add_node(kind_id, "kind", entry["kind"], authority="frontmatter_truth")
        add_node(
            family_id,
            "family_hint",
            family,
            authority="scout_only_non_authoritative",
        )
        add_node(
            technique_node_id,
            "technique",
            f"{entry['id']} {entry['name']}",
            technique_id=entry["id"],
            status=entry["status"],
            source_ref=entry["technique_path"],
            move_unit=entry["move"]["unit"],
        )
        add_node(source_node_id, "source_bundle", entry["technique_path"], source_ref=entry["technique_path"])
        add_node(capsule_node_id, "capsule", entry["id"], source_ref=f"generated/technique_capsules.json#{entry['id']}")
        add_node(support_node_id, "support_refs", entry["id"], source_ref=f"generated/technique_intelligence_registry.json#{entry['id']}")

        add_edge("repo:aoa-techniques", domain_id, "contains_domain", "repo_route")
        add_edge(domain_id, kind_id, "contains_kind", "frontmatter_truth")
        add_edge(kind_id, family_id, "groups_family_hint", "scout_only_non_authoritative")
        add_edge(family_id, technique_node_id, "contains_technique", "navigation_dag")
        add_edge(technique_node_id, source_node_id, "loads_source_bundle", "source_truth")
        add_edge(technique_node_id, capsule_node_id, "loads_capsule", "derived_lookup")
        add_edge(technique_node_id, support_node_id, "loads_support_refs", "derived_lookup")

        for relation in entry["relations"]["direct"]:
            relation_hints.append(
                {
                    "source": technique_node_id,
                    "target": f"technique:{relation['target']}",
                    "relation_type": relation["type"],
                    "authority": "frontmatter_direct_relation_not_dag_order",
                    "source_ref": relation["source_ref"],
                }
            )

    deduped_edges = []
    seen_edges: set[tuple[str, str, str, str]] = set()
    for edge in edges:
        key = (edge["source"], edge["target"], edge["edge_type"], edge["authority"])
        if key in seen_edges:
            continue
        seen_edges.add(key)
        deduped_edges.append(edge)

    return {
        "dag_version": DAG_VERSION,
        "source_registry": "generated/technique_intelligence_registry.json",
        "authority": (
            "Navigation DAG only. Direct technique relations are emitted as bounded hints, "
            "not as DAG order or inference truth."
        ),
        "node_count": len(nodes),
        "edge_count": len(deduped_edges),
        "nodes": [nodes[node_id] for node_id in sorted(nodes)],
        "edges": sorted(deduped_edges, key=lambda edge: (edge["source"], edge["target"], edge["edge_type"])),
        "relation_hints": sorted(
            relation_hints,
            key=lambda edge: (edge["source"], edge["target"], edge["relation_type"]),
        ),
    }


def project_min_dag_payload(full_payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "dag_version": full_payload["dag_version"],
        "source_registry": full_payload["source_registry"],
        "authority": full_payload["authority"],
        "node_count": full_payload["node_count"],
        "edge_count": full_payload["edge_count"],
        "nodes": [
            {
                "id": node["id"],
                "node_type": node["node_type"],
                "label": node["label"],
                **({"technique_id": node["technique_id"]} if "technique_id" in node else {}),
            }
            for node in full_payload["nodes"]
        ],
        "edges": full_payload["edges"],
    }


def build_reader_markdown(registry_payload: dict[str, Any], dag_payload: dict[str, Any]) -> str:
    entries = registry_payload["techniques"]
    status_counts = Counter(entry["status"] for entry in entries)
    domain_counts = Counter(entry["domain"] for entry in entries)
    kind_counts = Counter(entry["kind"] for entry in entries)
    execution_counts = Counter(
        entry["topology"]["hints"].get("execution_profile") or "unscouted" for entry in entries
    )

    lines = [
        "# Technique Intelligence",
        "",
        "Generated reader for source-linked technique intelligence.",
        "",
        "This reader is a route surface, not technique authority. Authored",
        "`TECHNIQUE.md` bundles remain stronger than this file, generated JSON,",
        "search output, scout axes, or graph projections.",
        "",
        "## Current Shape",
        "",
        f"- Registry version: `{registry_payload['registry_version']}`",
        f"- Technique entries: `{registry_payload['technique_count']}`",
        f"- Navigation DAG nodes: `{dag_payload['node_count']}`",
        f"- Navigation DAG edges: `{dag_payload['edge_count']}`",
        "- Core lens: attention over atomic moves",
        "- Scout axes: family, capability, substrate, execution profile, and risk posture stay non-authoritative",
        "",
        "## Operational Route",
        "",
        "Use [Technique Intelligence Guide](../../selection/TECHNIQUE_INTELLIGENCE_GUIDE.md) "
        "for the authored contract. Use [selection AGENTS](../../selection/AGENTS.md#validation) "
        "and root [AGENTS](../../../AGENTS.md#validation) for build, query, "
        "and validation command lanes.",
        "",
        "The local CLI exposes `status`, `query`, `explain`, and `pack` actions. "
        "Treat their output as a route back to authored bundles, not as execution "
        "authority or technique meaning.",
        "",
        "## Counts",
        "",
        "| Axis | Values |",
        "|---|---|",
        f"| Status | {', '.join(f'`{key}` {value}' for key, value in sorted(status_counts.items()))} |",
        f"| Domain | {', '.join(f'`{key}` {value}' for key, value in sorted(domain_counts.items()))} |",
        f"| Kind | {', '.join(f'`{key}` {value}' for key, value in sorted(kind_counts.items()))} |",
        f"| Execution profile hint | {', '.join(f'`{key}` {value}' for key, value in sorted(execution_counts.items()))} |",
        "",
        "## Registry Files",
        "",
        "- [technique_intelligence_registry.json](../../../generated/technique_intelligence_registry.json)",
        "- [technique_intelligence_registry.min.json](../../../generated/technique_intelligence_registry.min.json)",
        "- [technique_intelligence_dag.json](../../../generated/technique_intelligence_dag.json)",
        "- [technique_intelligence_dag.min.json](../../../generated/technique_intelligence_dag.min.json)",
        "",
        "## Technique Move Table",
        "",
        "| Technique | Domain | Kind | Status | Execution hint | Move intent |",
        "|---|---|---|---|---|---|",
    ]
    for entry in sorted(entries, key=lambda item: item["id"]):
        execution = entry["topology"]["hints"].get("execution_profile") or "unscouted"
        intent = compact_text(entry["move"]["intent"], max_chars=140).replace("|", "\\|")
        lines.append(
            f"| [{entry['id']}](../../../{entry['technique_path']}) `{entry['name']}` "
            f"| `{entry['domain']}` | `{entry['kind']}` | `{entry['status']}` "
            f"| `{execution}` | {intent} |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "Use the registry to choose, compare, explain, or pack one move. Leave this",
            "repo when the object becomes execution workflow, proof verdict, dispatch",
            "policy, runtime behavior, role contract, scenario composition, memory",
            "writeback, or graph semantics.",
            "",
        ]
    )
    return "\n".join(lines)


def build_all_outputs(repo_root: Path) -> dict[str, Any]:
    registry = build_technique_intelligence_registry_payload(repo_root)
    registry_min = project_min_registry_payload(registry)
    dag = build_technique_intelligence_dag_payload(registry)
    dag_min = project_min_dag_payload(dag)
    reader = build_reader_markdown(registry, dag)
    return {
        "registry": registry,
        "registry_min": registry_min,
        "dag": dag,
        "dag_min": dag_min,
        "reader": reader,
    }


def write_all_outputs(repo_root: Path) -> None:
    outputs = build_all_outputs(repo_root)
    write_json(repo_root / REGISTRY_PATH, outputs["registry"])
    write_json(repo_root / REGISTRY_MIN_PATH, outputs["registry_min"])
    write_json(repo_root / DAG_PATH, outputs["dag"])
    write_json(repo_root / DAG_MIN_PATH, outputs["dag_min"])
    write_text(repo_root / READER_PATH, outputs["reader"])


def load_registry(repo_root: Path) -> dict[str, Any]:
    return read_json(repo_root / REGISTRY_PATH)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in re.findall(r"[A-Za-z0-9]{2,}", text)]


def entry_matches_filters(entry: dict[str, Any], filters: dict[str, str | None]) -> bool:
    for field in ("status", "domain", "kind"):
        expected = filters.get(field)
        if expected and entry.get(field) != expected:
            return False
    execution_profile = filters.get("execution_profile")
    if execution_profile and entry["topology"]["hints"].get("execution_profile") != execution_profile:
        return False
    risk_posture = filters.get("risk_posture")
    if risk_posture and risk_posture not in entry["topology"]["hints"].get("risk_posture", []):
        return False
    return True


def lexical_score_document(document: dict[str, Any], terms: list[str], phrase: str) -> float:
    text = document["text"].lower()
    score = 0.0
    for term in terms:
        count = text.count(term)
        if count:
            score += 1.0 + min(count, 6) * 0.7
    if phrase and phrase in text:
        score += 5.0
    type_weight = {
        "identity": 2.2,
        "capsule": 2.0,
        "intent": 2.0,
        "when_to_use": 1.9,
        "when_not_to_use": 1.4,
        "inputs": 1.4,
        "outputs": 1.4,
        "contracts": 1.5,
        "risks": 1.3,
        "validation": 1.4,
        "semantic_review": 1.2,
        "shadow_review": 1.2,
        "fixture_sketch": 1.2,
    }.get(document["document_type"], 1.0)
    return score * type_weight


def try_fts5_search(documents: list[dict[str, Any]], terms: list[str]) -> set[str] | None:
    if not terms:
        return set()
    try:
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE VIRTUAL TABLE docs USING fts5(document_id, text)")
        connection.executemany(
            "INSERT INTO docs(document_id, text) VALUES (?, ?)",
            [(document["document_id"], document["text"]) for document in documents],
        )
        query = " OR ".join(terms[:16])
        rows = connection.execute(
            "SELECT document_id FROM docs WHERE docs MATCH ? LIMIT 2000", (query,)
        ).fetchall()
        connection.close()
        return {row[0] for row in rows}
    except sqlite3.Error:
        return None


def search_registry(
    registry_payload: dict[str, Any],
    query: str,
    *,
    limit: int = 5,
    filters: dict[str, str | None] | None = None,
) -> dict[str, Any]:
    filters = filters or {}
    terms = tokenize(query)
    phrase = " ".join(terms)
    scored: dict[str, dict[str, Any]] = {}

    candidate_entries = [
        entry for entry in registry_payload["techniques"] if entry_matches_filters(entry, filters)
    ]
    all_docs = [document for entry in candidate_entries for document in entry["search_documents"]]
    fts_document_ids = try_fts5_search(all_docs, terms)
    backend = "sqlite-fts5+lexical-rerank" if fts_document_ids is not None else "lexical"

    for entry in candidate_entries:
        exact_boost = 0.0
        query_lower = query.lower()
        if entry["id"].lower() in query_lower:
            exact_boost += 1000.0
        if entry["name"].lower() in query_lower:
            exact_boost += 500.0

        matches = []
        total_score = exact_boost
        for document in entry["search_documents"]:
            if fts_document_ids is not None and document["document_id"] not in fts_document_ids:
                score = lexical_score_document(document, terms, phrase) * 0.25
            else:
                score = lexical_score_document(document, terms, phrase)
            if score <= 0:
                continue
            total_score += score
            matches.append(
                {
                    "document_id": document["document_id"],
                    "document_type": document["document_type"],
                    "source_ref": document["source_ref"],
                    "score": round(score, 3),
                    "snippet": snippet_for(document["text"], terms),
                }
            )

        if total_score <= 0:
            continue
        matches.sort(key=lambda item: (-item["score"], item["document_id"]))
        scored[entry["id"]] = {
            "id": entry["id"],
            "name": entry["name"],
            "status": entry["status"],
            "domain": entry["domain"],
            "kind": entry["kind"],
            "summary": entry["summary"],
            "score": round(total_score, 3),
            "candidate_action": "select",
            "topology_hints": {
                "family": entry["topology"]["hints"].get("family"),
                "execution_profile": entry["topology"]["hints"].get("execution_profile"),
                "risk_posture": entry["topology"]["hints"].get("risk_posture", []),
                "authority": entry["topology"]["hints"]["authority"],
            },
            "matched_documents": matches[:5],
            "next_load_refs": entry["next_load_refs"][:4],
        }

    results = sorted(scored.values(), key=lambda item: (-item["score"], item["id"]))[:limit]
    if len(results) > 1 and results[1]["score"] >= results[0]["score"] * 0.85:
        results[0]["candidate_action"] = "compare"
        results[1]["candidate_action"] = "compare"
    return {
        "query": query,
        "backend": backend,
        "filters": {key: value for key, value in filters.items() if value},
        "limit": limit,
        "results": results,
    }


def find_entry(registry_payload: dict[str, Any], technique_id: str) -> dict[str, Any]:
    for entry in registry_payload["techniques"]:
        if entry["id"] == technique_id:
            return entry
    raise KeyError(f"unknown technique id: {technique_id}")


def explain_candidate(
    registry_payload: dict[str, Any], technique_id: str, *, intent: str
) -> dict[str, Any]:
    entry = find_entry(registry_payload, technique_id)
    full_search = search_registry(registry_payload, intent, limit=8)
    own_matches = []
    for document in entry["search_documents"]:
        score = lexical_score_document(document, tokenize(intent), " ".join(tokenize(intent)))
        if score > 0:
            own_matches.append(
                {
                    "document_id": document["document_id"],
                    "document_type": document["document_type"],
                    "source_ref": document["source_ref"],
                    "score": round(score, 3),
                    "snippet": snippet_for(document["text"], tokenize(intent)),
                }
            )
    own_matches.sort(key=lambda item: (-item["score"], item["document_id"]))

    adjacent = [
        {
            "id": result["id"],
            "name": result["name"],
            "score": result["score"],
            "reason": "query-neighbor; compare before using both",
        }
        for result in full_search["results"]
        if result["id"] != technique_id
    ][:3]

    relation_targets = [
        {"id": relation["target"], "type": relation["type"]}
        for relation in entry["relations"]["direct"]
    ]
    return {
        "technique_id": technique_id,
        "name": entry["name"],
        "intent": intent,
        "fit_evidence": own_matches[:5],
        "move": {
            "summary": entry["summary"],
            "applies_when": entry["move"]["applies_when"],
            "does_not_apply_when": entry["move"]["does_not_apply_when"],
            "inputs": entry["move"]["inputs"],
            "outputs": entry["move"]["outputs"],
            "validation": entry["move"]["validation"],
            "stop_line": entry["move"]["stop_line"],
        },
        "negative_cues": entry["move"]["does_not_apply_when"],
        "adjacent_candidates": adjacent,
        "direct_relation_targets": relation_targets,
        "route_away": entry["owner_boundaries"]["route_away"],
        "next_load_refs": entry["next_load_refs"],
        "source_authority": (
            "Open the authored TECHNIQUE.md before using the move in a live change; "
            "the source bundle remains stronger."
        ),
    }


def pack_candidate(
    registry_payload: dict[str, Any], technique_id: str, *, profile: str
) -> dict[str, Any]:
    if profile not in PROFILE_NAMES:
        raise ValueError(f"profile must be one of: {', '.join(PROFILE_NAMES)}")
    entry = find_entry(registry_payload, technique_id)
    base = {
        "profile": profile,
        "technique_id": entry["id"],
        "name": entry["name"],
        "source_ref": entry["technique_path"],
        "authority": "derived packet; source bundle remains stronger",
    }
    if profile == "capsule":
        return {**base, "capsule": entry["capsule"], "next_load_refs": entry["next_load_refs"][:3]}
    if profile == "small-agent":
        return {
            **base,
            "move": {
                key: entry["move"][key]
                for key in (
                    "unit",
                    "intent",
                    "applies_when",
                    "does_not_apply_when",
                    "inputs",
                    "outputs",
                    "contracts",
                    "validation",
                    "stop_line",
                )
            },
            "main_risk": entry["move"]["risks"],
            "fixture_refs": entry["fixture_refs"],
            "next_load_refs": entry["next_load_refs"],
        }
    if profile == "orchestrator":
        return {
            **base,
            "move_summary": entry["summary"],
            "topology": entry["topology"],
            "relations": entry["relations"],
            "review_refs": entry["review_refs"],
            "next_load_refs": entry["next_load_refs"],
        }
    if profile == "workflow-handoff":
        return {
            **base,
            "handoff_intent": "handoff one selected move with source refs and owner stop-lines",
            "move": {
                "intent": entry["move"]["intent"],
                "inputs": entry["move"]["inputs"],
                "outputs": entry["move"]["outputs"],
                "validation": entry["move"]["validation"],
                "stop_line": entry["move"]["stop_line"],
            },
            "owner_boundaries": entry["owner_boundaries"],
            "support_refs": entry["support_refs"],
            "next_load_refs": entry["next_load_refs"],
        }
    return {
        **base,
        "fixture_refs": entry["fixture_refs"],
        "validation": entry["move"]["validation"],
        "risk": entry["move"]["risks"],
        "owner_warning": "Fixture sketches test technique handling only; proof verdicts live outside this repo.",
        "next_load_refs": entry["next_load_refs"],
    }


def status_payload(repo_root: Path) -> dict[str, Any]:
    expected = build_all_outputs(repo_root)
    checks: dict[str, dict[str, Any]] = {}
    file_map = {
        "registry": REGISTRY_PATH,
        "registry_min": REGISTRY_MIN_PATH,
        "dag": DAG_PATH,
        "dag_min": DAG_MIN_PATH,
        "reader": READER_PATH,
    }
    for key, relative_path in file_map.items():
        path = repo_root / relative_path
        exists = path.exists()
        if not exists:
            checks[key] = {"path": relative_path.as_posix(), "exists": False, "up_to_date": False}
            continue
        actual = read_text(path)
        expected_text = (
            expected[key]
            if key == "reader"
            else json.dumps(expected[key], ensure_ascii=True, indent=2) + "\n"
        )
        checks[key] = {
            "path": relative_path.as_posix(),
            "exists": True,
            "up_to_date": actual == expected_text,
            "content_hash": sha256_text(actual),
        }
    registry = expected["registry"]
    return {
        "status": "ok" if all(item["up_to_date"] for item in checks.values()) else "drift",
        "registry_version": registry["registry_version"],
        "technique_count": registry["technique_count"],
        "authority": registry["authority"],
        "search_backend": "sqlite-fts5+lexical-rerank when sqlite FTS5 is available; lexical fallback otherwise",
        "checks": checks,
    }
