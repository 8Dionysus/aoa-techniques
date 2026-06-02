from __future__ import annotations

from .common import *
from .source_contracts import *

from .projection_catalog import *

def build_family_scout_payload(
    catalog: dict[str, Any], family_scout: dict[str, Any], kind_overlay: dict[str, Any]
) -> dict[str, Any]:
    catalog_entries = catalog.get("techniques")
    if not isinstance(catalog_entries, list):
        fail("generated/technique_catalog.json: techniques must be a list")
    catalog_by_id = {entry["id"]: entry for entry in catalog_entries}
    family_entries = family_scout_entries_by_id(family_scout, TECHNIQUE_FAMILY_SCOUT_PATH)
    overlay_entries = kind_overlay_entries_by_id(kind_overlay, TECHNIQUE_KIND_OVERLAY_PATH)

    families_payload: list[dict[str, Any]] = []
    for family in family_scout["families"]:
        family_id = family["id"]
        family_catalog_entries = sorted(
            [
                catalog_by_id[technique_id]
                for technique_id, overlay_entry in overlay_entries.items()
                if overlay_entry.get("family") == family_id and technique_id in catalog_by_id
            ],
            key=kind_group_sort_key,
        )
        families_payload.append(
            {
                "family": family_id,
                "summary": family["summary"],
                "typical_domains": list(family["typical_domains"]),
                "typical_kinds": list(family["typical_kinds"]),
                "counts": {
                    "total": len(family_catalog_entries),
                    "canonical": sum(
                        1 for entry in family_catalog_entries if entry["status"] == "canonical"
                    ),
                    "promoted": sum(
                        1 for entry in family_catalog_entries if entry["status"] == "promoted"
                    ),
                    "by_domain": ordered_domain_counts(family_catalog_entries),
                    "by_kind": ordered_kind_counts(family_catalog_entries),
                },
                "technique_ids": [entry["id"] for entry in family_catalog_entries],
                "techniques": [kind_manifest_entry(entry) | {"kind": entry["kind"]} for entry in family_catalog_entries],
            }
        )

    unassigned_ids = sorted(
        technique_id
        for technique_id in catalog_by_id
        if technique_id not in overlay_entries or not overlay_entries[technique_id].get("family")
    )

    return {
        "report_version": FAMILY_SCOUT_REPORT_VERSION,
        "status": "scout-only-non-authoritative",
        "source_of_truth": FAMILY_SCOUT_SOURCE_OF_TRUTH,
        "authority_note": FAMILY_SCOUT_AUTHORITY_NOTE,
        "families": families_payload,
        "unassigned_technique_ids": unassigned_ids,
    }

def build_family_scout_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Technique Family Scout",
        "",
        "This file is generated from the current kind registry, family scout, kind overlay, and generated catalog.",
        "Do not edit it by hand; rebuild through [reports AGENTS](AGENTS.md#validation).",
        "",
        FAMILY_SCOUT_AUTHORITY_NOTE,
        "",
        "Use this report when you want to inspect likely family clusters without promoting `family` into frontmatter, schema, or validator-required bundle truth.",
        "",
        "## Scout Scope",
        "",
        "| family | summary | total | canonical | promoted |",
        "|---|---|---|---|---|",
    ]

    for family in report["families"]:
        counts = family["counts"]
        lines.append(
            "| "
            f"`{family['family']}` | "
            f"{escape_markdown_table_cell(family['summary'])} | "
            f"`{counts['total']}` | "
            f"`{counts['canonical']}` | "
            f"`{counts['promoted']}` |"
        )

    lines.extend(
        [
            "",
            f"Unassigned family suggestions: `{len(report['unassigned_technique_ids'])}`.",
            "",
        ]
    )

    for family in report["families"]:
        counts = family["counts"]
        lines.extend(
            [
                f"## `{family['family']}`",
                "",
                family["summary"],
                "",
                f"Typical domains: {', '.join(f'`{domain}`' for domain in family['typical_domains'])}.",
                f"Typical kinds: {', '.join(f'`{kind}`' for kind in family['typical_kinds'])}.",
                "",
                f"Counts: `total` {counts['total']}, `canonical` {counts['canonical']}, `promoted` {counts['promoted']}.",
                "",
                "| technique | domain | kind | status | summary |",
                "|---|---|---|---|---|",
            ]
        )
        for technique in family["techniques"]:
            lines.append(
                "| "
                f"{selection_technique_link(technique, TECHNIQUE_REFORM_REPORT_LINK_PREFIX)} | "
                f"`{technique['domain']}` | "
                f"`{technique['kind']}` | "
                f"`{technique['status']}` | "
                f"{escape_markdown_table_cell(technique['summary'])} |"
            )
        if not family["techniques"]:
            lines.append("| _No overlay techniques currently map here._ | - | - | - | - |")
        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            f"- {FAMILY_SCOUT_AUTHORITY_NOTE}",
            "- Family suggestions may inform later clustering work, but bundle frontmatter remains the stronger source of meaning.",
            "- Do not use this report to add automatic remaps or new required metadata in this wave.",
            "",
        ]
    )
    return "\n".join(lines)

def seam_label(seam: tuple[str, str]) -> str:
    return f"{seam[0]} vs {seam[1]}"

def format_keyword_hits(hits: list[str]) -> str:
    if not hits:
        return "none"
    return ", ".join(f"`{hit}`" for hit in hits)

def catalog_entry_signal_text(entry: dict[str, Any], overlay_entry: dict[str, Any] | None) -> str:
    tags = entry.get("tags")
    tag_text = " ".join(tag for tag in tags if isinstance(tag, str)) if isinstance(tags, list) else ""
    family = overlay_entry.get("family") if isinstance(overlay_entry, dict) else ""
    return " ".join(
        part
        for part in (entry.get("name", ""), entry.get("summary", ""), tag_text, str(family or ""))
        if part
    ).lower()

def matched_keywords(text: str, keywords: tuple[str, ...]) -> list[str]:
    matches: list[str] = []
    for keyword in keywords:
        if keyword in text and keyword not in matches:
            matches.append(keyword)
    return matches

def kind_tie_break_rule_map(registry: dict[str, Any]) -> dict[str, str]:
    rules = registry.get("tie_break_rules")
    if not isinstance(rules, list):
        fail(f"{TECHNIQUE_KIND_REGISTRY_PATH}: tie_break_rules must be a list")
    mapping: dict[str, str] = {}
    for rule in rules:
        if not isinstance(rule, str) or ":" not in rule:
            fail(f"{TECHNIQUE_KIND_REGISTRY_PATH}: tie_break_rules must contain '<seam>: <rule>' strings")
        seam, detail = rule.split(":", 1)
        mapping[seam.strip()] = detail.strip()
    return mapping

def ambiguity_verdict(current_hits: list[str], other_hits: list[str]) -> str:
    if len(other_hits) > len(current_hits):
        return "candidate remap"
    if len(other_hits) >= len(current_hits) and other_hits:
        return "revisit later"
    return "keep current kind"

def build_kind_ambiguity_audit_markdown(
    catalog: dict[str, Any],
    registry: dict[str, Any],
    family_scout: dict[str, Any],
    kind_overlay: dict[str, Any],
) -> str:
    catalog_entries = catalog.get("techniques")
    if not isinstance(catalog_entries, list):
        fail("generated/technique_catalog.json: techniques must be a list")
    family_entries = family_scout_entries_by_id(family_scout, TECHNIQUE_FAMILY_SCOUT_PATH)
    overlay_entries = kind_overlay_entries_by_id(kind_overlay, TECHNIQUE_KIND_OVERLAY_PATH)
    tie_break_rules = kind_tie_break_rule_map(registry)
    catalog_by_id = {entry["id"]: entry for entry in catalog_entries}

    lines = [
        "# Kind Ambiguity Audit",
        "",
        "This file is generated from the current kind registry, family scout, kind overlay, and generated catalog.",
        "Do not edit it by hand; rebuild through [reports AGENTS](AGENTS.md#validation).",
        "",
        KIND_AMBIGUITY_AUTHORITY_NOTE,
        "",
        "Use this audit to inspect likely tie-break seams before proposing any later remap wave.",
        "",
    ]

    for seam in KIND_AMBIGUITY_SEAMS:
        left_kind, right_kind = seam
        keyword_map = KIND_AMBIGUITY_KEYWORDS[seam]
        candidates: list[tuple[int, str, dict[str, Any], dict[str, Any] | None, list[str], list[str], bool]] = []

        for technique_id, entry in catalog_by_id.items():
            if entry.get("kind") not in seam:
                continue
            overlay_entry = overlay_entries.get(technique_id)
            signal_text = catalog_entry_signal_text(entry, overlay_entry)
            left_hits = matched_keywords(signal_text, keyword_map[left_kind])
            right_hits = matched_keywords(signal_text, keyword_map[right_kind])
            current_hits = left_hits if entry["kind"] == left_kind else right_hits
            other_hits = right_hits if entry["kind"] == left_kind else left_hits
            family_has_both = False
            family = overlay_entry.get("family") if isinstance(overlay_entry, dict) else None
            if isinstance(family, str) and family in family_entries:
                typical_kinds = set(family_entries[family]["typical_kinds"])
                family_has_both = left_kind in typical_kinds and right_kind in typical_kinds
            if not other_hits and not family_has_both:
                continue
            score = len(other_hits) * 3 + len(current_hits) + (2 if family_has_both else 0)
            candidates.append((score, technique_id, entry, overlay_entry, current_hits, other_hits, family_has_both))

        candidates.sort(key=lambda item: (-item[0], kind_group_sort_key(item[2])))

        lines.extend(
            [
                f"## `{left_kind}` vs `{right_kind}`",
                "",
                f"Tie-break rule: {tie_break_rules[seam_label(seam)]}",
                "",
            ]
        )

        if not candidates:
            lines.extend(
                [
                    "_No current candidates crossed this seam strongly enough to flag in the scout audit._",
                    "",
                ]
            )
            continue

        for _score, _technique_id, entry, overlay_entry, current_hits, other_hits, family_has_both in candidates[:6]:
            family = overlay_entry.get("family") if isinstance(overlay_entry, dict) else None
            opposing_kind = right_kind if entry["kind"] == left_kind else left_kind
            family_note = ""
            if isinstance(family, str) and family_has_both:
                family_note = (
                    f" Scout family `{family}` already spans both `{left_kind}` and `{right_kind}`."
                )
            verdict = ambiguity_verdict(current_hits, other_hits)
            lines.extend(
                [
                    f"- {selection_technique_link(entry, TECHNIQUE_REFORM_REPORT_LINK_PREFIX)} - {entry['name']} (`{entry['domain']}`, current `{entry['kind']}`): "
                    f"current-kind cues {format_keyword_hits(current_hits)}; opposing `{opposing_kind}` cues {format_keyword_hits(other_hits)}.{family_note} "
                    f"Verdict: `{verdict}`."
                ]
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            f"- {KIND_AMBIGUITY_AUTHORITY_NOTE}",
            "- Use the registry tie-break rules first, then this audit as a bounded scout aid only.",
            "- A later remap wave should still review bundle meaning directly before changing any frontmatter.",
            "",
        ]
    )
    return "\n".join(lines)

def topology_axis_value_ids(axis_registry: dict[str, Any]) -> dict[str, set[str]]:
    values_by_axis: dict[str, set[str]] = {}
    for axis in axis_registry["axes"]:
        values_by_axis[axis["id"]] = {value["id"] for value in axis["values"]}
    return values_by_axis

def append_unique_values(target: list[str], values: tuple[str, ...] | list[str]) -> None:
    for value in values:
        if value not in target:
            target.append(value)

def filtered_axis_values(values: list[str], allowed_values: set[str]) -> list[str]:
    return [value for value in values if value in allowed_values]

def topology_signal_text(entry: dict[str, Any], overlay_entry: dict[str, Any] | None) -> str:
    return catalog_entry_signal_text(entry, overlay_entry)

def infer_capability_class(
    entry: dict[str, Any], overlay_entry: dict[str, Any] | None, allowed_values: set[str]
) -> list[str]:
    values: list[str] = []
    append_unique_values(values, TOPOLOGY_CAPABILITY_BY_KIND.get(entry["kind"], ()))
    signal_text = topology_signal_text(entry, overlay_entry)
    for value, keywords in TOPOLOGY_KEYWORD_RULES["capability_class"].items():
        if matched_keywords(signal_text, keywords):
            values.append(value)
    values = filtered_axis_values(values, allowed_values)
    if not values:
        values = ["interpret"]
    return list(dict.fromkeys(values))[:3]

def infer_substrate(
    entry: dict[str, Any], overlay_entry: dict[str, Any] | None, allowed_values: set[str]
) -> list[str]:
    values: list[str] = []
    append_unique_values(values, TOPOLOGY_SUBSTRATE_BY_DOMAIN.get(entry["domain"], ()))
    signal_text = topology_signal_text(entry, overlay_entry)
    for value, keywords in TOPOLOGY_KEYWORD_RULES["substrate"].items():
        if matched_keywords(signal_text, keywords):
            values.append(value)
    values = filtered_axis_values(values, allowed_values)
    if not values:
        values = ["docs"]
    return list(dict.fromkeys(values))[:4]

def infer_risk_posture(
    entry: dict[str, Any], overlay_entry: dict[str, Any] | None, allowed_values: set[str]
) -> list[str]:
    values: list[str] = []
    signal_text = topology_signal_text(entry, overlay_entry)
    for value, keywords in TOPOLOGY_KEYWORD_RULES["risk_posture"].items():
        if matched_keywords(signal_text, keywords):
            values.append(value)
    if entry.get("reversibility") == "hard":
        values.append("irreversible")
    if not any(value in values for value in ("mutating", "public-share", "security-sensitive", "irreversible")):
        values.insert(0, "read-only")
    values = filtered_axis_values(values, allowed_values)
    return list(dict.fromkeys(values))[:4] or ["read-only"]

def infer_execution_profile(
    entry: dict[str, Any], risk_posture: list[str], allowed_values: set[str]
) -> str:
    high_risk = {"mutating", "public-share", "security-sensitive", "irreversible"}
    if high_risk.intersection(risk_posture):
        value = "orchestration-required"
    elif entry["kind"] in TOPOLOGY_EXECUTION_PROFILE_BY_KIND:
        value = TOPOLOGY_EXECUTION_PROFILE_BY_KIND[entry["kind"]]
    else:
        value = "small-agent"
    if value not in allowed_values:
        value = "small-agent"
    return value

def topology_scout_entry(
    entry: dict[str, Any],
    overlay_entry: dict[str, Any] | None,
    allowed_values_by_axis: dict[str, set[str]],
) -> dict[str, Any]:
    risk_posture = infer_risk_posture(entry, overlay_entry, allowed_values_by_axis["risk_posture"])
    topology = {
        "family": overlay_entry.get("family") if isinstance(overlay_entry, dict) else None,
        "capability_class": infer_capability_class(
            entry, overlay_entry, allowed_values_by_axis["capability_class"]
        ),
        "substrate": infer_substrate(entry, overlay_entry, allowed_values_by_axis["substrate"]),
        "execution_profile": infer_execution_profile(
            entry, risk_posture, allowed_values_by_axis["execution_profile"]
        ),
        "risk_posture": risk_posture,
    }
    return {
        "id": entry["id"],
        "name": entry["name"],
        "domain": entry["domain"],
        "kind": entry["kind"],
        "status": entry["status"],
        "summary": entry["summary"],
        "technique_path": entry["technique_path"],
        "topology": topology,
    }

def count_scalar_values(entries: list[dict[str, Any]], axis: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in entries:
        value = entry["topology"][axis]
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))

def count_list_values(entries: list[dict[str, Any]], axis: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in entries:
        for value in entry["topology"][axis]:
            counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))

def build_topology_scout_payload(
    catalog: dict[str, Any],
    axis_registry: dict[str, Any],
    kind_overlay: dict[str, Any],
) -> dict[str, Any]:
    catalog_entries = catalog.get("techniques")
    if not isinstance(catalog_entries, list):
        fail("generated/technique_catalog.json: techniques must be a list")
    overlay_entries = kind_overlay_entries_by_id(kind_overlay, TECHNIQUE_KIND_OVERLAY_PATH)
    allowed_values_by_axis = topology_axis_value_ids(axis_registry)
    entries = [
        topology_scout_entry(entry, overlay_entries.get(entry["id"]), allowed_values_by_axis)
        for entry in sorted(catalog_entries, key=kind_group_sort_key)
    ]

    return {
        "report_version": TOPOLOGY_SCOUT_REPORT_VERSION,
        "status": "scout-only-non-authoritative",
        "source_of_truth": TOPOLOGY_SCOUT_SOURCE_OF_TRUTH,
        "authority_note": TOPOLOGY_SCOUT_AUTHORITY_NOTE,
        "frontmatter_truth_axes": list(axis_registry["frontmatter_truth_axes"]),
        "axis_order": list(TOPOLOGY_SCOUT_AXIS_ORDER),
        "axis_value_counts": {
            "capability_class": count_list_values(entries, "capability_class"),
            "substrate": count_list_values(entries, "substrate"),
            "execution_profile": count_scalar_values(entries, "execution_profile"),
            "risk_posture": count_list_values(entries, "risk_posture"),
        },
        "techniques": entries,
    }

def markdown_value_list(values: list[str]) -> str:
    return ", ".join(f"`{value}`" for value in values)

def build_topology_scout_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Technique Topology Scout",
        "",
        "This file is generated from the topology axis registry, kind overlay, and generated catalog.",
        "Do not edit it by hand; rebuild through [reports AGENTS](AGENTS.md#validation).",
        "",
        TOPOLOGY_SCOUT_AUTHORITY_NOTE,
        "",
        "Use this report to inspect likely capability, substrate, execution, and risk contours before proposing schema, template, or frontmatter migration.",
        "",
        "## Scout Scope",
        "",
        f"- Techniques covered: `{len(report['techniques'])}`",
        f"- Frontmatter truth axes: {markdown_value_list(report['frontmatter_truth_axes'])}",
        f"- Scout axes: {markdown_value_list(report['axis_order'])}",
        "",
    ]

    for axis in report["axis_order"]:
        lines.extend(
            [
                f"## `{axis}` Counts",
                "",
                "| value | count |",
                "|---|---:|",
            ]
        )
        for value, count in report["axis_value_counts"][axis].items():
            lines.append(f"| `{value}` | `{count}` |")
        lines.append("")

    lines.extend(
        [
            "## Technique Projection",
            "",
            "| technique | domain | kind | family | capability | substrate | execution | risk |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for entry in report["techniques"]:
        topology = entry["topology"]
        family = topology["family"] or "unassigned"
        lines.append(
            "| "
            f"{selection_technique_link(entry, TECHNIQUE_REFORM_REPORT_LINK_PREFIX)} | "
            f"`{entry['domain']}` | "
            f"`{entry['kind']}` | "
            f"`{family}` | "
            f"{markdown_value_list(topology['capability_class'])} | "
            f"{markdown_value_list(topology['substrate'])} | "
            f"`{topology['execution_profile']}` | "
            f"{markdown_value_list(topology['risk_posture'])} |"
        )

    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            f"- {TOPOLOGY_SCOUT_AUTHORITY_NOTE}",
            "- This projection may guide review packs, but bundle frontmatter remains stronger.",
            "- A later migration must still read bundle meaning directly before changing schema, templates, validators, or frontmatter.",
            "",
        ]
    )
    return "\n".join(lines)

def count_entry_field(entries: list[dict[str, Any]], field_name: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in entries:
        value = entry[field_name]
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))

def tree_projection_entry(entry: dict[str, Any], overlay_entry: dict[str, Any] | None) -> dict[str, Any]:
    family = overlay_entry.get("family") if isinstance(overlay_entry, dict) else None
    id_placement = TREE_ID_PLACEMENT.get(entry["id"])
    if id_placement is not None:
        proposed_trunk, proposed_shelf, review_status = id_placement
    elif isinstance(family, str) and family in TREE_FAMILY_PLACEMENT:
        proposed_trunk, review_status = TREE_FAMILY_PLACEMENT[family]
        proposed_shelf = family
    else:
        proposed_trunk = "unassigned"
        proposed_shelf = "unassigned"
        review_status = "unassigned-hold"

    proposed_future_path = (
        f"techniques/{proposed_trunk}/{proposed_shelf}/{entry['name']}/TECHNIQUE.md"
    )
    rationale_cues = [
        f"family:{family or 'unassigned'}",
        f"domain:{entry['domain']}",
        f"kind:{entry['kind']}",
        f"status:{entry['status']}",
        f"review_status:{review_status}",
    ]
    if id_placement is not None:
        rationale_cues.append(f"tree_id_placement:{proposed_trunk}/{proposed_shelf}")

    return {
        "id": entry["id"],
        "name": entry["name"],
        "domain": entry["domain"],
        "kind": entry["kind"],
        "status": entry["status"],
        "summary": entry["summary"],
        "current_path": entry["technique_path"],
        "family": family,
        "proposed_trunk": proposed_trunk,
        "proposed_shelf": proposed_shelf,
        "proposed_future_path": proposed_future_path,
        "review_status": review_status,
        "rationale_cues": rationale_cues,
        "stop_line": TREE_REVIEW_STATUS_STOP_LINES[review_status],
    }

def build_tree_projection_payload(
    catalog: dict[str, Any],
    kind_overlay: dict[str, Any],
) -> dict[str, Any]:
    catalog_entries = catalog.get("techniques")
    if not isinstance(catalog_entries, list):
        fail("generated/technique_catalog.json: techniques must be a list")
    overlay_entries = kind_overlay_entries_by_id(kind_overlay, TECHNIQUE_KIND_OVERLAY_PATH)
    entries = [
        tree_projection_entry(entry, overlay_entries.get(entry["id"]))
        for entry in sorted(catalog_entries, key=kind_group_sort_key)
    ]
    raw_review_status_counts = count_entry_field(entries, "review_status")

    return {
        "report_version": TREE_PROJECTION_REPORT_VERSION,
        "status": "projection-only-non-authoritative",
        "source_of_truth": TREE_PROJECTION_SOURCE_OF_TRUTH,
        "authority_note": TREE_PROJECTION_AUTHORITY_NOTE,
        "frontmatter_truth_axes": ["domain", "kind"],
        "target_path_shape": TREE_PROJECTION_TARGET_PATH_SHAPE,
        "review_status_order": list(TREE_PROJECTION_REVIEW_STATUS_ORDER),
        "trunk_counts": count_entry_field(entries, "proposed_trunk"),
        "shelf_counts": count_entry_field(entries, "proposed_shelf"),
        "review_status_counts": {
            status: raw_review_status_counts.get(status, 0)
            for status in TREE_PROJECTION_REVIEW_STATUS_ORDER
        },
        "techniques": entries,
    }

def build_tree_projection_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Technique Tree Projection",
        "",
        "This file is generated from the technique tree contract, family shelf review, kind overlay, and generated catalog.",
        "Do not edit it by hand; rebuild through [reports AGENTS](AGENTS.md#validation).",
        "",
        TREE_PROJECTION_AUTHORITY_NOTE,
        "",
        "Use this projection to audit current trunk and shelf placement, compare path drift, and review future placement changes before any new directory move.",
        "",
        "## Projection Scope",
        "",
        f"- Techniques covered: `{len(report['techniques'])}`",
        f"- Frontmatter truth axes: {markdown_value_list(report['frontmatter_truth_axes'])}",
        f"- Target path shape: `{report['target_path_shape']}`",
        "",
        "## Review Status Counts",
        "",
        "| review status | count |",
        "|---|---:|",
    ]

    for status in report["review_status_order"]:
        count = report["review_status_counts"].get(status, 0)
        lines.append(f"| `{status}` | `{count}` |")

    lines.extend(["", "## Trunk Counts", "", "| trunk | count |", "|---|---:|"])
    for trunk, count in report["trunk_counts"].items():
        lines.append(f"| `{trunk}` | `{count}` |")

    lines.extend(["", "## Shelf Counts", "", "| shelf | count |", "|---|---:|"])
    for shelf, count in report["shelf_counts"].items():
        lines.append(f"| `{shelf}` | `{count}` |")

    lines.extend(
        [
            "",
            "## Technique Projection",
            "",
            "| technique | current path | family | proposed trunk | proposed shelf | review status | proposed future path |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for entry in report["techniques"]:
        family = entry["family"] or "unassigned"
        lines.append(
            "| "
            f"{selection_technique_link({'id': entry['id'], 'technique_path': entry['current_path']}, TECHNIQUE_REFORM_REPORT_LINK_PREFIX)} | "
            f"`{entry['current_path']}` | "
            f"`{family}` | "
            f"`{entry['proposed_trunk']}` | "
            f"`{entry['proposed_shelf']}` | "
            f"`{entry['review_status']}` | "
            f"`{entry['proposed_future_path']}` |"
        )

    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            f"- {TREE_PROJECTION_AUTHORITY_NOTE}",
            "- This projection can audit current paths and choose review targets, but it is not source truth for bundle meaning or future moves.",
            "- Any later path change must read bundle meaning directly, choose one bounded subtree, and update links, generated surfaces, validators, docs, and decision records together.",
            "- `family` remains scout-only; `domain` and `kind` remain current frontmatter truth.",
            "",
        ]
    )
    return "\n".join(lines)

def validate_kind_scout_reports(repo_root: Path) -> None:
    reports_dir = repo_root / TECHNIQUE_REFORM_REPORTS_DIR
    markdown_path = reports_dir / "technique_family_scout.md"
    json_path = reports_dir / "technique_family_scout.json"
    audit_path = reports_dir / "kind_ambiguity_audit.md"
    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    registry = load_kind_registry(repo_root)
    family_scout = load_family_scout(repo_root)
    kind_overlay = load_kind_overlay(repo_root)

    expected_report = build_family_scout_payload(catalog, family_scout, kind_overlay)
    expected_markdown = build_family_scout_markdown(expected_report)
    expected_audit = build_kind_ambiguity_audit_markdown(
        catalog, registry, family_scout, kind_overlay
    )
    actual_report = read_json(json_path)
    actual_markdown = read_text(markdown_path)
    actual_audit = read_text(audit_path)

    if actual_report != expected_report:
        fail(
            f"{json_path}: generated family scout report is out of date; run "
            f"'python scripts/build_kind_manifest.py'"
        )
    if actual_markdown != expected_markdown:
        fail(
            f"{markdown_path}: generated family scout markdown is out of date; run "
            f"'python scripts/build_kind_manifest.py'"
        )
    if actual_audit != expected_audit:
        fail(
            f"{audit_path}: generated kind ambiguity audit is out of date; run "
            f"'python scripts/build_kind_manifest.py'"
        )
    if actual_report.get("status") != "scout-only-non-authoritative":
        fail(f"{json_path}: status must stay 'scout-only-non-authoritative'")
    if actual_report.get("authority_note") != FAMILY_SCOUT_AUTHORITY_NOTE:
        fail(f"{json_path}: authority_note must stay stable")
    if "non-authoritative" not in actual_markdown or "non-authoritative" not in actual_audit:
        fail(f"{repo_root}: kind scout reports must stay explicitly non-authoritative")

def validate_topology_scout_reports(repo_root: Path) -> None:
    reports_dir = repo_root / TECHNIQUE_REFORM_REPORTS_DIR
    json_path = reports_dir / "technique_topology_scout.json"
    markdown_path = reports_dir / "technique_topology_scout.md"
    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    axis_registry = load_topology_axes_registry(repo_root)
    kind_overlay = load_kind_overlay(repo_root)

    expected_report = build_topology_scout_payload(catalog, axis_registry, kind_overlay)
    expected_markdown = build_topology_scout_markdown(expected_report)
    actual_report = read_json(json_path)
    actual_markdown = read_text(markdown_path)

    if actual_report != expected_report:
        fail(
            f"{json_path}: generated topology scout report is out of date; run "
            f"'python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py'"
        )
    if actual_markdown != expected_markdown:
        fail(
            f"{markdown_path}: generated topology scout markdown is out of date; run "
            f"'python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py'"
        )
    if actual_report.get("status") != "scout-only-non-authoritative":
        fail(f"{json_path}: status must stay 'scout-only-non-authoritative'")
    if actual_report.get("authority_note") != TOPOLOGY_SCOUT_AUTHORITY_NOTE:
        fail(f"{json_path}: authority_note must stay stable")
    if actual_report.get("frontmatter_truth_axes") != ["domain", "kind"]:
        fail(f"{json_path}: frontmatter_truth_axes must stay ['domain', 'kind']")
    if "non-authoritative" not in actual_markdown or "bundle frontmatter remains stronger" not in actual_markdown:
        fail(f"{markdown_path}: topology scout report must stay explicitly non-authoritative")

def validate_tree_projection_reports(repo_root: Path) -> None:
    reports_dir = repo_root / TECHNIQUE_REFORM_REPORTS_DIR
    json_path = reports_dir / "technique_tree_projection.json"
    markdown_path = reports_dir / "technique_tree_projection.md"
    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    kind_overlay = load_kind_overlay(repo_root)

    expected_report = build_tree_projection_payload(catalog, kind_overlay)
    expected_markdown = build_tree_projection_markdown(expected_report)
    actual_report = read_json(json_path)
    actual_markdown = read_text(markdown_path)

    if actual_report != expected_report:
        fail(
            f"{json_path}: generated tree projection report is out of date; run "
            f"'python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py'"
        )
    if actual_markdown != expected_markdown:
        fail(
            f"{markdown_path}: generated tree projection markdown is out of date; run "
            f"'python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py'"
        )
    if actual_report.get("status") != "projection-only-non-authoritative":
        fail(f"{json_path}: status must stay 'projection-only-non-authoritative'")
    if actual_report.get("authority_note") != TREE_PROJECTION_AUTHORITY_NOTE:
        fail(f"{json_path}: authority_note must stay stable")
    if actual_report.get("frontmatter_truth_axes") != ["domain", "kind"]:
        fail(f"{json_path}: frontmatter_truth_axes must stay ['domain', 'kind']")
    if actual_report.get("target_path_shape") != TREE_PROJECTION_TARGET_PATH_SHAPE:
        fail(f"{json_path}: target_path_shape must stay stable")
    if (
        "non-authoritative" not in actual_markdown
        or "not source truth for bundle meaning" not in actual_markdown
    ):
        fail(f"{markdown_path}: tree projection report must stay explicitly non-authoritative")
