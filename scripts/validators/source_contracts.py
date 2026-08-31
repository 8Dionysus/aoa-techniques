from __future__ import annotations

import csv

from .common import *


SOURCE_FAST_REQUIRED_SOURCE_FILES = (
    "DESIGN.md",
    "DESIGN.AGENTS.md",
    "TECHNIQUE_INDEX.md",
    "memo/AGENTS.md",
    "docs/DOMAIN_MAP.md",
    "docs/TECHNIQUE_ATOM_CONTRACT.md",
    "docs/TECHNIQUE_TOPOLOGY_CONTRACT.md",
    "docs/TECHNIQUE_TREE_CONTRACT.md",
    "docs/review/CANONICAL_RUBRIC.md",
    "docs/review/CANONICAL_REVIEW_GUIDE.md",
    "docs/review/SEMANTIC_REVIEW_GUIDE.md",
    "docs/review/TECHNIQUE_SHADOW_GUIDE.md",
    "docs/selection/TECHNIQUE_SELECTION_GUIDE.md",
    "docs/selection/TECHNIQUE_INTELLIGENCE_GUIDE.md",
    "docs/selection/TECHNIQUE_KIND_GUIDE.md",
    "docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md",
    "schemas/technique.schema.json",
    "schemas/evidence-note.schema.json",
    "schemas/relation.schema.json",
    "schemas/index-entry.schema.json",
    TECHNIQUE_KIND_REGISTRY_PATH,
    TECHNIQUE_FAMILY_SCOUT_PATH,
    TECHNIQUE_TOPOLOGY_AXES_PATH,
    TECHNIQUE_KIND_OVERLAY_PATH,
    TECHNIQUE_KIND_OVERLAY_CSV_PATH,
)
MEMO_AGENTS_NAME = "memo/AGENTS.md"
HOST_SPECIFIC_MEMO_ROOT = "/srv/AbyssOS/aoa-memo"
MEMO_AGENTS_VALIDATION_COMMANDS = (
    'python "$AOA_MEMO_ROOT/scripts/memory/validate_local_memo_port.py" --path memo',
    'python "$AOA_MEMO_ROOT/scripts/memory/build_local_memo_port_index.py" --path memo --check',
)


def validate_source_fast_required_files(repo_root: Path) -> None:
    for relative_path in SOURCE_FAST_REQUIRED_SOURCE_FILES:
        if not (repo_root / relative_path).is_file():
            fail(f"{repo_root}: missing source-fast source file '{relative_path}'")


def validate_memo_agents_portable_validation_route(repo_root: Path) -> None:
    memo_agents_path = repo_root / MEMO_AGENTS_NAME
    if not memo_agents_path.is_file():
        fail(f"{repo_root}: missing source-fast source file '{MEMO_AGENTS_NAME}'")
    text = memo_agents_path.read_text(encoding="utf-8")
    if HOST_SPECIFIC_MEMO_ROOT in text:
        fail(
            f"{MEMO_AGENTS_NAME}: memo validation route must not default AOA_MEMO_ROOT "
            f"to host-specific {HOST_SPECIFIC_MEMO_ROOT}"
        )
    if "AOA_MEMO_ROOT:?" not in text:
        fail(
            f"{MEMO_AGENTS_NAME}: memo validation route must require an explicit "
            "AOA_MEMO_ROOT instead of guessing a sibling checkout path"
        )
    for command in MEMO_AGENTS_VALIDATION_COMMANDS:
        if command not in text:
            fail(f"{MEMO_AGENTS_NAME}: memo validation route must include `{command}`")


def validate_frontmatter_schema(
    frontmatter: dict[str, Any], technique_path: Path, schema_store: dict[str, Any]
) -> None:
    schema = resolve_schema_ref("technique.schema.json", schema_store)
    validate_schema_instance(frontmatter, schema, str(technique_path), schema_store)


def validate_kind_axis_alignment(repo_root: Path, schema_store: dict[str, Any]) -> None:
    registry_path = repo_root / TECHNIQUE_KIND_REGISTRY_PATH
    registry = load_kind_registry(repo_root)

    selection_order = registry.get("selection_order")
    if selection_order != list(KIND_ORDER):
        fail(f"{registry_path}: selection_order must match KIND_ORDER exactly")

    registry_ids = list(kind_registry_values_by_id(registry, registry_path))
    if registry_ids != list(KIND_ORDER):
        fail(f"{registry_path}: values[*].id must match KIND_ORDER exactly")

    for schema_name in ("technique.schema.json", "index-entry.schema.json"):
        schema = resolve_schema_ref(schema_name, schema_store)
        kind_schema = schema.get("properties", {}).get("kind")
        if not isinstance(kind_schema, dict):
            fail(f"{schema_name}: missing properties.kind")
        if kind_schema.get("enum") != list(KIND_ORDER):
            fail(f"{schema_name}: kind enum must match KIND_ORDER exactly")


def kind_registry_values_by_id(registry: dict[str, Any], registry_path: Path | str) -> dict[str, dict[str, Any]]:
    values = registry.get("values")
    if not isinstance(values, list):
        fail(f"{registry_path}: values must be a list")

    values_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(values):
        location = f"{registry_path}.values[{index}]"
        if not isinstance(item, dict):
            fail(f"{location}: value entry must be an object")
        kind_id = item.get("id")
        if not isinstance(kind_id, str) or not kind_id:
            fail(f"{location}: id must be a non-empty string")
        if kind_id in values_by_id:
            fail(f"{location}: duplicate kind id '{kind_id}'")
        summary = item.get("summary")
        if not isinstance(summary, str) or not summary.strip():
            fail(f"{location}: summary must be a non-empty string")
        for list_key in ("choose_when", "not_when"):
            field_value = item.get(list_key)
            if not isinstance(field_value, list) or not field_value:
                fail(f"{location}: {list_key} must be a non-empty list")
            if not all(isinstance(entry, str) and entry.strip() for entry in field_value):
                fail(f"{location}: {list_key} must contain only non-empty strings")
        values_by_id[kind_id] = item
    return values_by_id


def family_scout_entries_by_id(scout: dict[str, Any], scout_path: Path | str) -> dict[str, dict[str, Any]]:
    families = scout.get("families")
    if not isinstance(families, list):
        fail(f"{scout_path}: families must be a list")

    entries_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(families):
        location = f"{scout_path}.families[{index}]"
        if not isinstance(item, dict):
            fail(f"{location}: family entry must be an object")
        family_id = item.get("id")
        if not isinstance(family_id, str) or not family_id:
            fail(f"{location}: id must be a non-empty string")
        if family_id in entries_by_id:
            fail(f"{location}: duplicate family id '{family_id}'")
        summary = item.get("summary")
        if not isinstance(summary, str) or not summary.strip():
            fail(f"{location}: summary must be a non-empty string")
        typical_domains = item.get("typical_domains")
        if not isinstance(typical_domains, list) or not typical_domains:
            fail(f"{location}: typical_domains must be a non-empty list")
        if not all(isinstance(domain, str) and domain in DOMAIN_VALUES for domain in typical_domains):
            fail(f"{location}: typical_domains must stay inside DOMAIN_VALUES")
        typical_kinds = item.get("typical_kinds")
        if not isinstance(typical_kinds, list) or not typical_kinds:
            fail(f"{location}: typical_kinds must be a non-empty list")
        if not all(isinstance(kind, str) and kind in KIND_VALUES for kind in typical_kinds):
            fail(f"{location}: typical_kinds must stay inside KIND_VALUES")
        entries_by_id[family_id] = item
    return entries_by_id


def kind_overlay_entries_by_id(overlay: dict[str, Any], overlay_path: Path | str) -> dict[str, dict[str, Any]]:
    entries = overlay.get("entries")
    if not isinstance(entries, list):
        fail(f"{overlay_path}: entries must be a list")

    entries_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(entries):
        location = f"{overlay_path}.entries[{index}]"
        if not isinstance(item, dict):
            fail(f"{location}: overlay entry must be an object")
        entry_id = item.get("id")
        if not isinstance(entry_id, str) or not entry_id:
            fail(f"{location}: id must be a non-empty string")
        if entry_id in entries_by_id:
            fail(f"{location}: duplicate overlay id '{entry_id}'")
        for field_name in ("name", "domain", "status", "kind"):
            field_value = item.get(field_name)
            if not isinstance(field_value, str) or not field_value:
                fail(f"{location}: {field_name} must be a non-empty string")
        entries_by_id[entry_id] = item
    return entries_by_id


def kind_overlay_csv_entries_by_id(csv_path: Path) -> dict[str, dict[str, str]]:
    expected_fields = ["id", "name", "domain", "status", "kind", "family"]
    try:
        with csv_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != expected_fields:
                fail(f"{csv_path}: header must be {','.join(expected_fields)}")
            entries_by_id: dict[str, dict[str, str]] = {}
            for row_number, row in enumerate(reader, start=2):
                if None in row:
                    fail(f"{csv_path}:{row_number}: row has extra columns")
                entry_id = str(row.get("id") or "")
                if not entry_id:
                    fail(f"{csv_path}:{row_number}: id must be a non-empty string")
                if entry_id in entries_by_id:
                    fail(f"{csv_path}:{row_number}: duplicate overlay id '{entry_id}'")
                for field_name in ("name", "domain", "status", "kind"):
                    if not str(row.get(field_name) or ""):
                        fail(f"{csv_path}:{row_number}: {field_name} must be a non-empty string")
                entries_by_id[entry_id] = {field: str(row.get(field) or "") for field in expected_fields}
    except FileNotFoundError as exc:
        raise ValidationError(f"{csv_path}: missing kind overlay CSV") from exc
    return entries_by_id


def validate_kind_overlay_csv_parity(
    overlay_entries: dict[str, dict[str, Any]],
    csv_entries: dict[str, dict[str, str]],
    *,
    csv_path: Path,
) -> None:
    if set(csv_entries) != set(overlay_entries):
        missing = sorted(set(overlay_entries) - set(csv_entries))
        extra = sorted(set(csv_entries) - set(overlay_entries))
        detail_parts: list[str] = []
        if missing:
            detail_parts.append(f"missing {missing}")
        if extra:
            detail_parts.append(f"extra {extra}")
        fail(f"{csv_path}: rows must cover the YAML overlay exactly once ({'; '.join(detail_parts)})")

    for technique_id, overlay_entry in overlay_entries.items():
        csv_entry = csv_entries[technique_id]
        for field_name in ("name", "domain", "status", "kind"):
            expected = str(overlay_entry.get(field_name) or "")
            actual = csv_entry[field_name]
            if actual != expected:
                fail(
                    f"{csv_path}: {technique_id} {field_name} must match YAML overlay "
                    f"({expected}), got {actual}"
                )
        expected_family = str(overlay_entry.get("family") or "")
        if csv_entry["family"] != expected_family:
            fail(
                f"{csv_path}: {technique_id} family must match YAML overlay "
                f"({expected_family}), got {csv_entry['family']}"
            )


def validate_family_scout_alignment(repo_root: Path) -> None:
    scout_path = repo_root / TECHNIQUE_FAMILY_SCOUT_PATH
    scout = load_family_scout(repo_root)
    if scout.get("schema_version") != 1:
        fail(f"{scout_path}: schema_version must be 1")
    if scout.get("axis_name") != "technique_family":
        fail(f"{scout_path}: axis_name must stay 'technique_family'")
    if scout.get("status") != "scout-foundation":
        fail(f"{scout_path}: status must stay 'scout-foundation'")
    family_scout_entries_by_id(scout, scout_path)


def validate_topology_axes_registry(repo_root: Path) -> None:
    registry_path = repo_root / TECHNIQUE_TOPOLOGY_AXES_PATH
    registry = load_topology_axes_registry(repo_root)
    if registry.get("schema_version") != 1:
        fail(f"{registry_path}: schema_version must be 1")
    if registry.get("axis_name") != "technique_topology_scout_axes":
        fail(f"{registry_path}: axis_name must stay 'technique_topology_scout_axes'")
    if registry.get("status") != "scout-foundation":
        fail(f"{registry_path}: status must stay 'scout-foundation'")
    authority_note = registry.get("authority_note")
    if not isinstance(authority_note, str) or "does not add required frontmatter fields" not in authority_note:
        fail(f"{registry_path}: authority_note must keep the non-frontmatter boundary explicit")
    if "must not remap bundle meaning automatically" not in authority_note:
        fail(f"{registry_path}: authority_note must reject automatic remap authority")
    if registry.get("frontmatter_truth_axes") != ["domain", "kind"]:
        fail(f"{registry_path}: frontmatter_truth_axes must stay ['domain', 'kind']")

    source_of_truth = registry.get("source_of_truth")
    if not isinstance(source_of_truth, list) or not source_of_truth:
        fail(f"{registry_path}: source_of_truth must be a non-empty list")
    for source_path in source_of_truth:
        if not isinstance(source_path, str) or not source_path:
            fail(f"{registry_path}: source_of_truth entries must be non-empty strings")
        if not (repo_root / source_path).is_file():
            fail(f"{registry_path}: source_of_truth entry '{source_path}' must exist")

    axes = registry.get("axes")
    if not isinstance(axes, list):
        fail(f"{registry_path}: axes must be a list")
    axis_ids = [axis.get("id") for axis in axes if isinstance(axis, dict)]
    if axis_ids != list(TOPOLOGY_SCOUT_AXIS_ORDER):
        fail(f"{registry_path}: axes must follow TOPOLOGY_SCOUT_AXIS_ORDER exactly")

    for axis_index, axis in enumerate(axes):
        location = f"{registry_path}.axes[{axis_index}]"
        if not isinstance(axis, dict):
            fail(f"{location}: axis entry must be an object")
        axis_id = axis["id"]
        if axis.get("status") != "design-axis-scout":
            fail(f"{location}: status must stay 'design-axis-scout'")
        if axis.get("cardinality") != TOPOLOGY_SCOUT_AXIS_CARDINALITY[axis_id]:
            fail(
                f"{location}: cardinality must stay '{TOPOLOGY_SCOUT_AXIS_CARDINALITY[axis_id]}'"
            )
        purpose = axis.get("purpose")
        if not isinstance(purpose, str) or not purpose.strip():
            fail(f"{location}: purpose must be a non-empty string")
        values = axis.get("values")
        if not isinstance(values, list) or not values:
            fail(f"{location}: values must be a non-empty list")
        seen_values: set[str] = set()
        for value_index, value in enumerate(values):
            value_location = f"{location}.values[{value_index}]"
            if not isinstance(value, dict):
                fail(f"{value_location}: value must be an object")
            value_id = value.get("id")
            if not isinstance(value_id, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", value_id):
                fail(f"{value_location}: id must be kebab-case")
            if value_id in seen_values:
                fail(f"{value_location}: duplicate value id '{value_id}'")
            seen_values.add(value_id)
            summary = value.get("summary")
            if not isinstance(summary, str) or not summary.strip():
                fail(f"{value_location}: summary must be a non-empty string")
            choose_when = value.get("choose_when")
            if not isinstance(choose_when, list) or not choose_when:
                fail(f"{value_location}: choose_when must be a non-empty list")
            if not all(isinstance(item, str) and item.strip() for item in choose_when):
                fail(f"{value_location}: choose_when must contain only non-empty strings")


def validate_kind_overlay(repo_root: Path, records: list[TechniqueRecord]) -> None:
    overlay_path = repo_root / TECHNIQUE_KIND_OVERLAY_PATH
    overlay_csv_path = repo_root / TECHNIQUE_KIND_OVERLAY_CSV_PATH
    overlay = load_kind_overlay(repo_root)
    if overlay.get("schema_version") != 1:
        fail(f"{overlay_path}: schema_version must be 1")
    if overlay.get("source_catalog_version") != 1:
        fail(f"{overlay_path}: source_catalog_version must be 1")
    if overlay.get("source_of_truth") != "kind-overlay":
        fail(f"{overlay_path}: source_of_truth must stay 'kind-overlay'")

    family_scout_path = repo_root / TECHNIQUE_FAMILY_SCOUT_PATH
    family_entries = family_scout_entries_by_id(load_family_scout(repo_root), family_scout_path)
    overlay_entries = kind_overlay_entries_by_id(overlay, overlay_path)
    validate_kind_overlay_csv_parity(
        overlay_entries,
        kind_overlay_csv_entries_by_id(overlay_csv_path),
        csv_path=overlay_csv_path,
    )
    records_by_id = {record.id: record for record in records}

    if set(overlay_entries) != set(records_by_id):
        missing = sorted(set(records_by_id) - set(overlay_entries))
        extra = sorted(set(overlay_entries) - set(records_by_id))
        detail_parts: list[str] = []
        if missing:
            detail_parts.append(f"missing {missing}")
        if extra:
            detail_parts.append(f"extra {extra}")
        fail(f"{overlay_path}: entries must cover the current corpus exactly once ({'; '.join(detail_parts)})")

    for technique_id, overlay_entry in overlay_entries.items():
        record = records_by_id[technique_id]
        if overlay_entry["name"] != record.name:
            fail(f"{overlay_path}: {technique_id} name must match bundle frontmatter")
        if overlay_entry["domain"] != record.domain:
            fail(f"{overlay_path}: {technique_id} domain must match bundle frontmatter")
        if overlay_entry["status"] != record.status:
            fail(f"{overlay_path}: {technique_id} status must match bundle frontmatter")
        if overlay_entry["kind"] != record.kind:
            fail(f"{overlay_path}: {technique_id} kind must match bundle frontmatter")
        family = overlay_entry.get("family")
        if family is not None:
            if not isinstance(family, str) or not family:
                fail(f"{overlay_path}: {technique_id} family must be a non-empty string when present")
            if family not in family_entries:
                fail(f"{overlay_path}: {technique_id} family '{family}' is not declared in {family_scout_path}")


def normalize_section_markdown(raw_markdown: str) -> str:
    return raw_markdown.lstrip("\r\n").rstrip()


def parse_subsections(markdown: str) -> tuple[TechniqueSection, ...]:
    _intro_markdown, sections = split_markdown_sections(markdown, level=3)
    return sections


def parse_sections(body: str) -> tuple[TechniqueSection, ...]:
    _intro_markdown, sections = split_markdown_sections(body, level=2)
    return sections


def split_markdown_sections(
    markdown: str, *, level: int
) -> tuple[str, tuple[TechniqueSection, ...]]:
    if level == 2:
        heading_re = SECTION_RE
    elif level == 3:
        heading_re = SUBSECTION_RE
    else:  # pragma: no cover - current callers only need level 2 or 3
        raise ValueError(f"unsupported markdown heading level {level}")

    sections: list[TechniqueSection] = []
    intro_lines: list[str] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    active_fence: tuple[str, int] | None = None

    def append_line(line: str) -> None:
        if current_heading is None:
            intro_lines.append(line)
        else:
            current_lines.append(line)

    def flush_current() -> None:
        nonlocal current_heading, current_lines
        if current_heading is None:
            return
        sections.append(
            TechniqueSection(
                heading=current_heading,
                markdown=normalize_section_markdown("".join(current_lines)),
            )
        )
        current_heading = None
        current_lines = []

    for line in markdown.splitlines(keepends=True):
        stripped_line = line.rstrip("\r\n")
        fence_match = FENCE_DELIMITER_RE.match(stripped_line)
        if fence_match is not None:
            delimiter = fence_match.group(1)
            delimiter_key = (delimiter[0], len(delimiter))
            if active_fence is None:
                active_fence = delimiter_key
            elif delimiter_key[0] == active_fence[0] and delimiter_key[1] >= active_fence[1]:
                active_fence = None
            append_line(line)
            continue

        if active_fence is None:
            heading_match = heading_re.match(stripped_line)
            if heading_match is not None:
                flush_current()
                current_heading = heading_match.group(1).strip()
                current_lines = []
                continue

        append_line(line)

    flush_current()
    return normalize_section_markdown("".join(intro_lines)), tuple(sections)


def normalize_plain_text(text: str) -> str:
    return WHITESPACE_RE.sub(" ", text).strip()


def markdown_line_to_plain_text(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith(("## ", "### ")):
        return ""
    if stripped.startswith("|") and stripped.endswith("|"):
        return ""

    stripped = LEADING_LIST_MARKER_RE.sub("", stripped)
    stripped = MARKDOWN_LINK_RE.sub(r"\1", stripped)
    stripped = INLINE_CODE_RE.sub(r"\1", stripped)
    stripped = stripped.replace("**", "").replace("*", "")
    return normalize_plain_text(stripped)


def markdown_to_plain_text(markdown: str) -> str:
    return normalize_plain_text(
        " ".join(
            plain_line
            for plain_line in (markdown_line_to_plain_text(line) for line in markdown.splitlines())
            if plain_line
        )
    )


def capsule_markdown_items(markdown: str) -> list[str]:
    items: list[str] = []
    current_item_lines: list[str] = []

    def flush_current_item() -> None:
        if not current_item_lines:
            return
        plain_item = markdown_line_to_plain_text(" ".join(current_item_lines))
        if plain_item:
            items.append(plain_item)
        current_item_lines.clear()

    for raw_line in markdown.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            flush_current_item()
            continue
        if LEADING_LIST_MARKER_RE.match(stripped):
            flush_current_item()
            current_item_lines.append(stripped)
            continue
        if current_item_lines and (raw_line.startswith(" ") or raw_line.startswith("\t")):
            current_item_lines.append(stripped)
            continue
        flush_current_item()
    flush_current_item()
    return items


def first_sentence(markdown: str) -> str:
    plain_text = markdown_to_plain_text(markdown)
    if not plain_text:
        return ""
    return re.split(r"(?<=[.!?])\s+", plain_text, maxsplit=1)[0].strip()


def finalize_capsule_text(text: str, truncated: bool) -> str:
    compact = normalize_plain_text(text).rstrip(" .,;:")
    if not compact:
        return ""
    return compact + ("..." if truncated else ".")


def truncate_capsule_text(text: str, max_words: int) -> str:
    normalized = normalize_plain_text(text)
    if not normalized:
        return ""

    words = normalized.split()
    if len(words) <= max_words:
        return finalize_capsule_text(normalized, truncated=False)
    return finalize_capsule_text(" ".join(words[:max_words]), truncated=True)


def capsule_compare_text(text: str) -> str:
    comparable = normalize_plain_text(text.replace("...", "").rstrip("."))
    for prefix in DERIVED_CAPSULE_PREFIXES:
        if comparable.startswith(prefix):
            comparable = comparable[len(prefix) :]
            break
    return normalize_plain_text(comparable)


DERIVED_CAPSULE_PREFIXES = (
    "Intent: ",
    "Use when ",
    "Avoid when ",
    "Needs ",
    "Produces ",
    "Core contract: ",
    "Main risk: ",
    "Validate by checking ",
)


def ensure_derived_capsule_text(candidate: str, source_markdown: str, max_words: int) -> str:
    source_plain = markdown_to_plain_text(source_markdown)
    if not source_plain:
        return candidate
    if capsule_compare_text(candidate) != capsule_compare_text(source_plain):
        return candidate

    source_words = source_plain.split()
    if len(source_words) <= 1:
        return candidate

    forced_budget = max(1, min(max_words, len(source_words) - 1))
    for prefix in DERIVED_CAPSULE_PREFIXES:
        if candidate.startswith(prefix):
            prefix_word_count = len(prefix.rstrip(": ").split())
            source_budget = max(1, forced_budget - prefix_word_count)
            return f"{prefix}{truncate_capsule_text(source_plain, source_budget)}"
    return truncate_capsule_text(source_plain, forced_budget)


def join_with_or(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} or {items[1]}"
    return f"{', '.join(items[:-1])}, or {items[-1]}"


def join_with_semicolons(items: list[str]) -> str:
    return "; ".join(item for item in items if item)


def capsule_sections_by_heading(record: TechniqueRecord) -> dict[str, TechniqueSection]:
    sections_by_heading = {section.heading: section for section in record.sections}
    missing = [heading for heading in CAPSULE_SECTION_HEADINGS if heading not in sections_by_heading]
    if missing:
        expected = ", ".join(f"'## {heading}'" for heading in CAPSULE_SECTION_HEADINGS)
        actual = ", ".join(f"'## {heading}'" for heading in missing)
        fail(
            f"{record.technique_path}: capsule source requires sections [{expected}]; "
            f"missing [{actual}]"
        )
    return sections_by_heading


def capsule_bullets_or_sentence(markdown: str, fallback_count: int) -> list[str]:
    items = capsule_markdown_items(markdown)
    if items:
        return items[:fallback_count]
    sentence = first_sentence(markdown)
    return [sentence] if sentence else []


def summarize_capsule_intent(markdown: str) -> str:
    sentence = first_sentence(markdown)
    candidate = truncate_capsule_text(sentence, 14)
    return ensure_derived_capsule_text(candidate, markdown, 12)


def summarize_capsule_use_when(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Use when {join_with_or(capsule_bullets_or_sentence(markdown, 2))}",
        20,
    )
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_do_not_use(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Avoid when {join_with_or(capsule_bullets_or_sentence(markdown, 2))}",
        20,
    )
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_inputs(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Needs {join_with_semicolons(capsule_bullets_or_sentence(markdown, 3))}",
        18,
    )
    return ensure_derived_capsule_text(candidate, markdown, 14)


def summarize_capsule_outputs(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Produces {join_with_semicolons(capsule_bullets_or_sentence(markdown, 3))}",
        18,
    )
    return ensure_derived_capsule_text(candidate, markdown, 14)


def summarize_capsule_contract(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Core contract: {join_with_semicolons(capsule_bullets_or_sentence(markdown, 2))}",
        20,
    )
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_risk(markdown: str) -> str:
    subsection_map = {section.heading: section.markdown for section in parse_subsections(markdown)}
    for heading in ("Failure modes", "Negative effects", "Misuse patterns"):
        subsection_markdown = subsection_map.get(heading)
        if not subsection_markdown:
            continue
        signals = capsule_bullets_or_sentence(subsection_markdown, 1)
        if signals:
            candidate = truncate_capsule_text(f"Main risk: {signals[0]}", 20)
            return ensure_derived_capsule_text(candidate, subsection_markdown, 16)

    candidate = truncate_capsule_text(f"Main risk: {first_sentence(markdown)}", 20)
    return ensure_derived_capsule_text(candidate, markdown, 16)


def summarize_capsule_validation(markdown: str) -> str:
    candidate = truncate_capsule_text(
        f"Validate by checking {join_with_semicolons(capsule_bullets_or_sentence(markdown, 3))}",
        22,
    )
    return ensure_derived_capsule_text(candidate, markdown, 18)


def validate_risks_markdown(risks_markdown: str, technique_path: Path) -> None:
    intro_markdown, subsections = split_markdown_sections(risks_markdown, level=3)
    if not subsections:
        fail(
            f"{technique_path}: '## Risks' must include fixed '###' subsections for the "
            f"rich risks contract"
        )

    if intro_markdown:
        fail(f"{technique_path}: '## Risks' must not include prose before its first '###' subsection")

    actual_headings = tuple(section.heading for section in subsections)
    if actual_headings != RISK_SUBSECTION_HEADINGS:
        expected = ", ".join(f"'### {heading}'" for heading in RISK_SUBSECTION_HEADINGS)
        actual = ", ".join(f"'### {heading}'" for heading in actual_headings) or "(none)"
        fail(
            f"{technique_path}: '## Risks' must use the fixed subsection order "
            f"[{expected}], found [{actual}]"
        )

    for subsection in subsections:
        if not subsection.markdown:
            fail(f"{technique_path}: risk subsection '### {subsection.heading}' must not be empty")


def validate_sections(body: str, technique_path: Path) -> tuple[TechniqueSection, ...]:
    sections = parse_sections(body)
    present_sections = [section.heading for section in sections]
    for required_section in REQUIRED_SECTIONS:
        occurrence_count = present_sections.count(required_section)
        if occurrence_count == 0:
            fail(f"{technique_path}: missing required section '## {required_section}'")
        if occurrence_count > 1:
            fail(f"{technique_path}: required section '## {required_section}' must appear exactly once")

    for optional_section in OPTIONAL_TEMPLATE_SECTIONS:
        occurrence_count = present_sections.count(optional_section)
        if occurrence_count > 1:
            fail(f"{technique_path}: optional section '## {optional_section}' must appear at most once")

    allowed_sections = set(REQUIRED_SECTIONS) | set(OPTIONAL_TEMPLATE_SECTIONS)
    unexpected_sections = [heading for heading in present_sections if heading not in allowed_sections]
    if unexpected_sections:
        unexpected = ", ".join(f"'## {heading}'" for heading in unexpected_sections)
        fail(f"{technique_path}: unexpected top-level sections found [{unexpected}]")

    expected_order = tuple(
        heading for heading in TECHNIQUE_SECTION_ORDER if heading in present_sections
    )
    if tuple(present_sections) != expected_order:
        expected = ", ".join(f"'## {heading}'" for heading in expected_order)
        actual = ", ".join(f"'## {heading}'" for heading in present_sections) or "(none)"
        fail(
            f"{technique_path}: top-level sections must stay in standard order [{expected}], "
            f"found [{actual}]"
        )

    sections_by_heading = {section.heading: section for section in sections}
    for optional_section in OPTIONAL_TEMPLATE_SECTIONS:
        section = sections_by_heading.get(optional_section)
        if section is not None and not section.markdown:
            fail(f"{technique_path}: optional section '## {optional_section}' must not be empty")

    risk_sections = [section for section in sections if section.heading == "Risks"]
    if len(risk_sections) != 1:
        fail(f"{technique_path}: '## Risks' must appear exactly once")
    validate_risks_markdown(risk_sections[0].markdown, technique_path)

    return sections


def validate_support_dirs(technique_dir: Path) -> None:
    for support_dir_name in REQUIRED_SUPPORT_DIRS:
        support_dir = technique_dir / support_dir_name
        if not support_dir.is_dir():
            fail(f"{technique_dir}: missing support directory '{support_dir_name}/'")
        markdown_files = sorted(support_dir.rglob("*.md"))
        if not markdown_files:
            fail(f"{technique_dir}: support directory '{support_dir_name}/' is empty")


def validate_support_references(body: str, technique_dir: Path, technique_path: Path) -> None:
    for relative_path in sorted(set(match.group(0) for match in SUPPORT_PATH_RE.finditer(body))):
        pure_path = PurePosixPath(relative_path)
        if not pure_path.parts or pure_path.parts[0] not in REQUIRED_SUPPORT_DIRS:
            fail(f"{technique_path}: referenced support path '{relative_path}' is not allowed")
        if any(part == ".." for part in pure_path.parts):
            fail(
                f"{technique_path}: referenced support path '{relative_path}' must stay inside the technique bundle"
            )

        target = technique_dir.joinpath(*pure_path.parts)
        if not target.is_file():
            fail(f"{technique_path}: referenced support path '{relative_path}' does not exist")


def normalize_intro_markdown(lines: list[str]) -> str:
    return "\n".join(lines).rstrip()


def parse_checklist_file(check_path: Path, repo_root: Path) -> TechniqueChecklist:
    lines = read_text(check_path).splitlines()
    nonblank_indexes = [index for index, line in enumerate(lines) if line.strip()]
    if not nonblank_indexes:
        fail(f"{check_path}: checklist file must start with a '# ' title and at least one item")

    title_index = nonblank_indexes[0]
    title_line = lines[title_index]
    if not title_line.startswith("# ") or title_line.startswith("##"):
        fail(f"{check_path}: first meaningful line must be a single '# ' title")

    title = title_line[2:].strip()
    if not title:
        fail(f"{check_path}: checklist title must not be empty")

    index = title_index + 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    intro_lines: list[str] = []
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.startswith("- "):
            break
        if line.startswith("#"):
            fail(f"{check_path}: headings after the checklist title are not supported")
        if line.startswith((" ", "\t")):
            fail(f"{check_path}: indented intro or wrapped checklist content is not supported")
        intro_lines.append(line)
        index += 1

    while index < len(lines) and not lines[index].strip():
        index += 1

    items: list[ChecklistItem] = []
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith("- "):
            item_text = line[2:].strip()
            if not item_text:
                fail(f"{check_path}: checklist items must not be empty")
            items.append(ChecklistItem(text=item_text))
            index += 1
            continue
        if line.startswith((" ", "\t")):
            fail(f"{check_path}: nested bullets or wrapped checklist items are not supported")
        if line.startswith("#"):
            fail(f"{check_path}: headings after the checklist title are not supported")
        fail(f"{check_path}: prose after checklist items is not supported")

    if not items:
        fail(f"{check_path}: checklist file must include at least one top-level '- ' item")

    return TechniqueChecklist(
        check_path=check_path.relative_to(repo_root).as_posix(),
        title=title,
        intro_markdown=normalize_intro_markdown(intro_lines),
        items=tuple(items),
    )


def parse_checklists(repo_root: Path, technique_dir: Path) -> tuple[TechniqueChecklist, ...]:
    checks_dir = technique_dir / "checks"
    checklist_paths = sorted(
        checks_dir.rglob("*.md"), key=lambda path: path.relative_to(repo_root).as_posix()
    )
    return tuple(parse_checklist_file(path, repo_root) for path in checklist_paths)


def parse_example_file(example_path: Path, repo_root: Path) -> TechniqueExample:
    lines = read_text(example_path).splitlines()
    nonblank_indexes = [index for index, line in enumerate(lines) if line.strip()]
    if not nonblank_indexes:
        fail(f"{example_path}: example file must start with a '# ' title")

    title_index = nonblank_indexes[0]
    title_line = lines[title_index]
    if not title_line.startswith("# ") or title_line.startswith("##"):
        fail(f"{example_path}: first meaningful line must be a single '# ' title")

    title = title_line[2:].strip()
    if not title:
        fail(f"{example_path}: example title must not be empty")

    body_markdown = normalize_section_markdown("\n".join(lines[title_index + 1 :]))
    return TechniqueExample(
        example_path=example_path.relative_to(repo_root).as_posix(),
        title=title,
        body_markdown=body_markdown,
    )


def parse_examples(repo_root: Path, technique_dir: Path) -> tuple[TechniqueExample, ...]:
    examples_dir = technique_dir / "examples"
    example_paths = sorted(
        examples_dir.rglob("*.md"), key=lambda path: path.relative_to(repo_root).as_posix()
    )
    return tuple(parse_example_file(path, repo_root) for path in example_paths)


def parse_titled_markdown_file(markdown_path: Path, kind_label: str) -> tuple[str, list[str], int]:
    lines = read_text(markdown_path).splitlines()
    nonblank_indexes = [index for index, line in enumerate(lines) if line.strip()]
    if not nonblank_indexes:
        fail(f"{markdown_path}: {kind_label} file must start with a '# ' title")

    title_index = nonblank_indexes[0]
    title_line = lines[title_index]
    if not title_line.startswith("# ") or title_line.startswith("##"):
        fail(f"{markdown_path}: first meaningful line must be a single '# ' title")

    title = title_line[2:].strip()
    if not title:
        fail(f"{markdown_path}: {kind_label} title must not be empty")

    return title, lines, title_index


def extract_top_level_section_headings(
    markdown_path: Path, lines: list[str], title_index: int
) -> tuple[str, ...]:
    top_level_sections = tuple(
        line[3:].strip() for line in lines[title_index + 1 :] if line.startswith("## ")
    )
    if not top_level_sections:
        fail(
            f"{markdown_path}: repo-doc source must include at least one top-level '## ' heading"
        )
    return top_level_sections


def split_typed_note_body(note_path: Path, body: str) -> tuple[str, tuple[TechniqueSection, ...]]:
    intro_markdown, sections = split_markdown_sections(body, level=2)
    if not sections:
        fail(f"{note_path}: typed note must include top-level '## ' sections")
    return intro_markdown, sections


def top_level_meaningful_indexes(lines: list[str]) -> list[int]:
    return [
        index
        for index, line in enumerate(lines)
        if line.strip() and not line.startswith((" ", "\t"))
    ]


def normalize_indented_markdown(lines: list[str]) -> str:
    trimmed = list(lines)
    while trimmed and not trimmed[0].strip():
        trimmed.pop(0)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()

    if not trimmed:
        return ""

    indents = [
        len(line) - len(line.lstrip(" "))
        for line in trimmed
        if line.strip() and line.startswith(" ")
    ]
    min_indent = min(indents) if indents else 0

    normalized_lines: list[str] = []
    for line in trimmed:
        if min_indent and line.startswith(" " * min_indent):
            normalized_lines.append(line[min_indent:])
        else:
            normalized_lines.append(line)

    return "\n".join(normalized_lines).rstrip()


def field_value_markdown(first_value: str, continuation_lines: list[str]) -> str:
    continuation_markdown = normalize_indented_markdown(continuation_lines)
    if first_value and continuation_markdown:
        return f"{first_value}\n{continuation_markdown}"
    if continuation_markdown:
        return continuation_markdown
    return first_value


def item_text_markdown(first_text: str, continuation_lines: list[str]) -> str:
    continuation_markdown = normalize_indented_markdown(continuation_lines)
    if first_text and continuation_markdown:
        return f"{first_text}\n{continuation_markdown}"
    if continuation_markdown:
        return continuation_markdown
    return first_text


def parse_note_section_payload(
    note_path: Path, heading: str, section_markdown: str
) -> EvidenceNoteSection:
    lines = section_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    top_level_lines = [lines[index] for index in top_level_indexes]
    key_value_matches = [NOTE_FIELD_RE.fullmatch(line) for line in top_level_lines]

    if top_level_lines and all(match is not None for match in key_value_matches):
        fields: list[NoteField] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            match = NOTE_FIELD_RE.fullmatch(chunk_lines[0])
            if match is None:
                fail(f"{note_path}: section '{heading}' must keep key/value bullet structure")
            fields.append(
                NoteField(
                    key=match.group(1).strip(),
                    value_markdown=field_value_markdown(
                        match.group(2).rstrip(), chunk_lines[1:]
                    ),
                )
            )

        return EvidenceNoteSection(
            heading=heading,
            payload_type=NOTE_PAYLOAD_FIELDS,
            fields=tuple(fields),
            items=(),
            markdown="",
        )

    if top_level_lines and all(line.startswith("- ") for line in top_level_lines):
        items: list[NoteItem] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            item_text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
            if not item_text:
                fail(f"{note_path}: section '{heading}' contains an empty bullet item")
            items.append(NoteItem(text=item_text))

        return EvidenceNoteSection(
            heading=heading,
            payload_type=NOTE_PAYLOAD_ITEMS,
            fields=(),
            items=tuple(items),
            markdown="",
        )

    return EvidenceNoteSection(
        heading=heading,
        payload_type=NOTE_PAYLOAD_MARKDOWN,
        fields=(),
        items=(),
        markdown=section_markdown,
    )


def parse_note_file(note_path: Path, repo_root: Path) -> TechniqueNote:
    title, lines, title_index = parse_titled_markdown_file(note_path, "note")
    note_path_str = note_path.relative_to(repo_root).as_posix()
    kind = expected_evidence_kind(note_path_str)
    body = "\n".join(lines[title_index + 1 :])

    if kind not in TYPED_NOTE_SECTION_SCOPES:
        return TechniqueNote(
            note_path=note_path_str,
            kind=kind,
            title=title,
            note_shape=NOTE_SHAPE_OPAQUE,
            intro_markdown="",
            sections=(),
            body_markdown=normalize_section_markdown(body),
        )

    expected_title = TYPED_NOTE_TITLES[kind]
    if title != expected_title:
        fail(f"{note_path}: typed note title must be '{expected_title}', found '{title}'")

    intro_markdown, parsed_sections = split_typed_note_body(note_path, body)
    actual_headings = tuple(section.heading for section in parsed_sections)
    expected_headings = TYPED_NOTE_SECTION_SCOPES[kind]
    if actual_headings != expected_headings:
        expected = ", ".join(f"'## {heading}'" for heading in expected_headings)
        actual = ", ".join(f"'## {heading}'" for heading in actual_headings) or "none"
        fail(
            f"{note_path}: typed note sections must stay in standard order [{expected}], "
            f"found [{actual}]"
        )

    sections = tuple(
        parse_note_section_payload(note_path, section.heading, section.markdown)
        for section in parsed_sections
    )
    return TechniqueNote(
        note_path=note_path_str,
        kind=kind,
        title=title,
        note_shape=NOTE_SHAPE_TYPED,
        intro_markdown=intro_markdown,
        sections=sections,
        body_markdown="",
    )


def parse_notes(repo_root: Path, technique_dir: Path) -> tuple[TechniqueNote, ...]:
    notes_dir = technique_dir / "notes"
    note_paths = sorted(notes_dir.rglob("*.md"), key=lambda path: path.relative_to(repo_root).as_posix())
    return tuple(parse_note_file(path, repo_root) for path in note_paths)


def split_optional_frontmatter(markdown_path: Path) -> tuple[str | None, str]:
    text = read_text(markdown_path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def review_template_scopes_payload() -> dict[str, Any]:
    return {
        spec["template_id"]: {
            "template_type": spec["template_type"],
            "section_scope": list(spec["section_scope"]),
        }
        for spec in GITHUB_REVIEW_TEMPLATE_SPECS
    }


def validate_issue_template_metadata(
    template_path: Path, metadata: dict[str, Any]
) -> dict[str, str]:
    if tuple(metadata.keys()) != REVIEW_TEMPLATE_METADATA_KEYS:
        fail(
            f"{template_path}: issue template metadata must use exact keys "
            f"{list(REVIEW_TEMPLATE_METADATA_KEYS)}"
        )

    validated: dict[str, str] = {}
    for key in REVIEW_TEMPLATE_METADATA_KEYS:
        value = metadata[key]
        if not isinstance(value, str) or not value.strip():
            fail(f"{template_path}: metadata field '{key}' must be a non-empty string")
        validated[key] = value
    return validated


def parse_review_template_sections(
    template_path: Path, body: str, expected_headings: tuple[str, ...]
) -> tuple[TechniqueSection, ...]:
    intro_markdown, sections = split_markdown_sections(body, level=2)
    if not sections:
        fail(f"{template_path}: template body must include top-level '## ' sections")
    if intro_markdown != "":
        fail(f"{template_path}: template body must start directly with its first '## ' section")
    actual_headings = tuple(section.heading for section in sections)
    if actual_headings != expected_headings:
        expected = ", ".join(f"'## {heading}'" for heading in expected_headings)
        actual = ", ".join(f"'## {heading}'" for heading in actual_headings) or "none"
        fail(
            f"{template_path}: review-template sections must stay in standard order "
            f"[{expected}], found [{actual}]"
        )
    return sections


def parse_review_template_section_payload(
    template_path: Path,
    template_type: str,
    heading: str,
    section_markdown: str,
) -> ReviewTemplateSection:
    lines = section_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    top_level_lines = [lines[index] for index in top_level_indexes]
    checkbox_matches = [TEMPLATE_CHECKBOX_RE.fullmatch(line) for line in top_level_lines]
    field_matches = [TEMPLATE_FIELD_RE.fullmatch(line) for line in top_level_lines]

    if top_level_lines and all(match is not None for match in checkbox_matches):
        checkboxes: list[ReviewTemplateCheckbox] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            match = TEMPLATE_CHECKBOX_RE.fullmatch(chunk_lines[0])
            if match is None:
                fail(f"{template_path}: section '{heading}' must keep checkbox structure")
            text = item_text_markdown(match.group(2).strip(), chunk_lines[1:])
            if not text:
                fail(f"{template_path}: section '{heading}' contains an empty checkbox item")
            checkboxes.append(
                ReviewTemplateCheckbox(text=text, checked=match.group(1).lower() == "x")
            )

        return ReviewTemplateSection(
            heading=heading,
            payload_type=REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES,
            fields=(),
            items=(),
            checkboxes=tuple(checkboxes),
            markdown="",
        )

    if (
        template_type == REVIEW_TEMPLATE_TYPE_ISSUE
        and top_level_lines
        and all(match is not None for match in field_matches)
    ):
        fields: list[ReviewTemplateField] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            match = TEMPLATE_FIELD_RE.fullmatch(chunk_lines[0])
            if match is None:
                fail(f"{template_path}: section '{heading}' must keep field-bullet structure")
            key = match.group(1).strip()
            if not key:
                fail(f"{template_path}: section '{heading}' contains an empty field key")
            fields.append(
                ReviewTemplateField(
                    key=key,
                    value_markdown=field_value_markdown(match.group(2).rstrip(), chunk_lines[1:]),
                )
            )

        return ReviewTemplateSection(
            heading=heading,
            payload_type=REVIEW_TEMPLATE_PAYLOAD_FIELDS,
            fields=tuple(fields),
            items=(),
            checkboxes=(),
            markdown="",
        )

    if top_level_lines and all(line.startswith("- ") for line in top_level_lines):
        items: list[ReviewTemplateItem] = []
        for order, start_index in enumerate(top_level_indexes, start=1):
            end_index = (
                top_level_indexes[order] if order < len(top_level_indexes) else len(lines)
            )
            chunk_lines = lines[start_index:end_index]
            item_text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
            if not item_text:
                fail(f"{template_path}: section '{heading}' contains an empty item")
            items.append(ReviewTemplateItem(text=item_text))

        return ReviewTemplateSection(
            heading=heading,
            payload_type=REVIEW_TEMPLATE_PAYLOAD_ITEMS,
            fields=(),
            items=tuple(items),
            checkboxes=(),
            markdown="",
        )

    return ReviewTemplateSection(
        heading=heading,
        payload_type=REVIEW_TEMPLATE_PAYLOAD_MARKDOWN,
        fields=(),
        items=(),
        checkboxes=(),
        markdown=section_markdown,
    )


def path_exists_with_exact_case(repo_root: Path, relative_path: Path) -> bool:
    current = repo_root
    for part in relative_path.parts:
        if part in {"", "."}:
            continue
        if not current.is_dir():
            return False
        entries = {entry.name: entry for entry in current.iterdir()}
        next_path = entries.get(part)
        if next_path is None:
            return False
        current = next_path
    return current.exists()


def parse_github_review_templates(repo_root: Path) -> tuple[GitHubReviewTemplate, ...]:
    templates: list[GitHubReviewTemplate] = []
    duplicate_pull_request_template = Path(".github") / "pull_request_template.md"
    if path_exists_with_exact_case(repo_root, duplicate_pull_request_template):
        fail(
            f"{repo_root / duplicate_pull_request_template}: competing pull request template path is not allowed; "
            "keep .github/PULL_REQUEST_TEMPLATE.md as the sole canonical PR template"
        )

    for spec in GITHUB_REVIEW_TEMPLATE_SPECS:
        template_path = repo_root / spec["template_path"]
        if not template_path.is_file():
            fail(f"{template_path}: missing required GitHub review template")

        raw_frontmatter, body = split_optional_frontmatter(template_path)
        template_type = spec["template_type"]
        metadata: dict[str, str] | None

        if template_type == REVIEW_TEMPLATE_TYPE_ISSUE:
            if raw_frontmatter is None:
                fail(f"{template_path}: issue template must start with YAML frontmatter")
            metadata = validate_issue_template_metadata(
                template_path, parse_frontmatter(raw_frontmatter, template_path)
            )
        else:
            if raw_frontmatter is not None:
                fail(f"{template_path}: pull request template must not use YAML frontmatter")
            metadata = None

        sections = parse_review_template_sections(template_path, body, spec["section_scope"])
        parsed_sections = tuple(
            parse_review_template_section_payload(
                template_path, template_type, section.heading, section.markdown
            )
            for section in sections
        )
        templates.append(
            GitHubReviewTemplate(
                template_id=spec["template_id"],
                template_path=template_path.relative_to(repo_root).as_posix(),
                template_type=template_type,
                metadata=metadata,
                sections=parsed_sections,
            )
        )

    return tuple(templates)


def semantic_review_id_from_path(review_path: Path) -> str:
    stem = review_path.stem
    suffix = "_SEMANTIC_REVIEW"
    if not stem.endswith(suffix):
        fail(f"{review_path}: semantic review filename must end with '{suffix}.md'")
    review_id = stem[: -len(suffix)].lower()
    if not review_id:
        fail(f"{review_path}: semantic review filename must include a non-empty review id")
    return review_id


def split_semantic_review_body(
    review_path: Path, body: str
) -> tuple[str, tuple[TechniqueSection, ...]]:
    intro_markdown, sections = split_markdown_sections(body, level=2)
    if not sections:
        fail(f"{review_path}: semantic review doc must include top-level '## ' sections")
    return intro_markdown, sections


def extract_last_outcome(markdown: str) -> str | None:
    matches = list(re.finditer(r"Outcome:\s*(.+)", markdown))
    if not matches:
        return None
    return matches[-1].group(1).strip()


def parse_semantic_review_map_entries(
    review_path: Path, repo_root: Path, map_markdown: str
) -> tuple[SemanticReviewMapEntry, ...]:
    lines = [line.rstrip() for line in map_markdown.splitlines() if line.strip()]
    if len(lines) < 3:
        fail(f"{review_path}: semantic review map must include a header, divider, and one row")
    if lines[0] != SEMANTIC_REVIEW_MAP_HEADER:
        fail(
            f"{review_path}: semantic review map must start with exact header "
            f"'{SEMANTIC_REVIEW_MAP_HEADER}'"
        )
    if lines[1] != SEMANTIC_REVIEW_MAP_DIVIDER:
        fail(
            f"{review_path}: semantic review map must use exact divider "
            f"'{SEMANTIC_REVIEW_MAP_DIVIDER}'"
        )

    entries: list[SemanticReviewMapEntry] = []
    row_re = re.compile(r"^\| \[([A-Za-z0-9-]+)\]\(([^)]+)\) \| (.+) \|$")
    for row_order, line in enumerate(lines[2:], start=1):
        match = row_re.fullmatch(line)
        if match is None:
            fail(f"{review_path}: semantic review map row {row_order} is malformed")
        technique_id = match.group(1).strip()
        target = match.group(2).strip()
        current_role = match.group(3).strip()
        if not current_role:
            fail(f"{review_path}: semantic review map row {row_order} must include current role")

        resolved_target = review_path.parent.joinpath(*PurePosixPath(target).parts).resolve()
        try:
            technique_path = resolved_target.relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            fail(
                f"{review_path}: semantic review map row {row_order} points outside the repo: "
                f"'{target}'"
            )
        if not resolved_target.is_file():
            fail(
                f"{review_path}: semantic review map row {row_order} points to missing file "
                f"'{target}'"
            )

        entries.append(
            SemanticReviewMapEntry(
                technique_id=technique_id,
                technique_path=technique_path,
                current_role=current_role,
            )
        )

    return tuple(entries)


def parse_semantic_review_seams(
    review_path: Path, seam_markdown: str
) -> tuple[SemanticReviewSeam, ...]:
    intro_markdown, parsed_seams = split_markdown_sections(seam_markdown, level=3)
    if not parsed_seams:
        fail(f"{review_path}: semantic review '## Seam Review' must include '### ' subsections")
    if intro_markdown:
        fail(f"{review_path}: semantic review '## Seam Review' must not include prose before seams")

    seams: list[SemanticReviewSeam] = []
    for section in parsed_seams:
        heading = section.heading
        body_markdown = section.markdown
        if not body_markdown:
            fail(f"{review_path}: semantic review seam '{heading}' must not be empty")

        lines = body_markdown.splitlines()
        nonblank_indexes = [line_index for line_index, line in enumerate(lines) if line.strip()]
        if not nonblank_indexes:
            fail(f"{review_path}: semantic review seam '{heading}' must contain a question")
        question_index = nonblank_indexes[0]
        question_line = lines[question_index].strip()
        if not question_line.startswith(SEMANTIC_REVIEW_QUESTION_PREFIX):
            fail(
                f"{review_path}: semantic review seam '{heading}' must start with "
                f"'{SEMANTIC_REVIEW_QUESTION_PREFIX}'"
            )
        question = question_line[len(SEMANTIC_REVIEW_QUESTION_PREFIX) :].strip()
        if not question:
            fail(f"{review_path}: semantic review seam '{heading}' question must not be empty")

        analysis_markdown = normalize_section_markdown("\n".join(lines[question_index + 1 :]))
        if not analysis_markdown:
            fail(f"{review_path}: semantic review seam '{heading}' must include analysis markdown")
        outcome = extract_last_outcome(analysis_markdown)
        if outcome is None:
            fail(
                f"{review_path}: semantic review seam '{heading}' must include an "
                f"'{SEMANTIC_REVIEW_OUTCOME_MARKER}' marker"
            )

        seams.append(
            SemanticReviewSeam(
                heading=heading,
                question=question,
                analysis_markdown=analysis_markdown,
                outcome=outcome,
            )
        )

    return tuple(seams)


def parse_semantic_review_findings(
    review_path: Path, findings_markdown: str
) -> tuple[tuple[SemanticReviewFinding, ...], str]:
    lines = findings_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    if len(top_level_indexes) < 2:
        fail(
            f"{review_path}: semantic review '## Findings' must include bullet findings and "
            f"'{SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )

    last_index = top_level_indexes[-1]
    overall_line = lines[last_index].strip()
    if not overall_line.startswith(SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX):
        fail(
            f"{review_path}: semantic review '## Findings' must end with "
            f"'{SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )
    overall_outcome = overall_line[len(SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX) :].strip()
    if not overall_outcome:
        fail(f"{review_path}: semantic review overall outcome must not be empty")

    findings: list[SemanticReviewFinding] = []
    item_indexes = top_level_indexes[:-1]
    for order, start_index in enumerate(item_indexes, start=1):
        line = lines[start_index]
        if not line.startswith("- "):
            fail(
                f"{review_path}: semantic review findings must use top-level '- ' bullets before "
                f"the overall outcome"
            )
        end_index = item_indexes[order] if order < len(item_indexes) else last_index
        chunk_lines = lines[start_index:end_index]
        text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
        if not text:
            fail(f"{review_path}: semantic review finding {order} must not be empty")
        findings.append(SemanticReviewFinding(text=text))

    return tuple(findings), overall_outcome


def parse_semantic_review_file(review_path: Path, repo_root: Path) -> SemanticReview:
    title, lines, title_index = parse_titled_markdown_file(review_path, "semantic review")
    review_id = semantic_review_id_from_path(review_path)
    review_path_str = review_path.relative_to(repo_root).as_posix()
    body = "\n".join(lines[title_index + 1 :])

    intro_markdown, sections = split_semantic_review_body(review_path, body)
    if len(sections) < 4:
        fail(
            f"{review_path}: semantic review doc must include map, seam review, findings, and "
            f"next step sections"
        )

    headings = [section.heading for section in sections]
    if not headings[0].endswith(" Map"):
        fail(f"{review_path}: first semantic review section must end with ' Map'")
    if headings[1] != "Seam Review":
        fail(f"{review_path}: second semantic review section must be '## Seam Review'")
    if headings[-2] != "Findings":
        fail(f"{review_path}: penultimate semantic review section must be '## Findings'")
    if headings[-1] != "Next Step":
        fail(f"{review_path}: final semantic review section must be '## Next Step'")
    if headings.count("Findings") != 1:
        fail(f"{review_path}: semantic review doc must contain exactly one '## Findings'")
    if headings.count("Next Step") != 1:
        fail(f"{review_path}: semantic review doc must contain exactly one '## Next Step'")

    map_section = sections[0]
    seam_section = sections[1]
    context_sections = sections[2:-2]
    findings_section = sections[-2]
    next_step_section = sections[-1]

    map_entries = parse_semantic_review_map_entries(review_path, repo_root, map_section.markdown)
    seams = parse_semantic_review_seams(review_path, seam_section.markdown)
    context_notes = tuple(
        SemanticReviewContextNote(
            heading=section.heading,
            markdown=section.markdown,
            outcome=extract_last_outcome(section.markdown),
        )
        for section in context_sections
    )
    findings, overall_outcome = parse_semantic_review_findings(
        review_path, findings_section.markdown
    )

    return SemanticReview(
        review_id=review_id,
        review_path=review_path_str,
        title=title,
        intro_markdown=intro_markdown,
        map_heading=map_section.heading,
        map_entries=map_entries,
        seams=seams,
        context_notes=context_notes,
        findings=findings,
        overall_outcome=overall_outcome,
        next_step_markdown=next_step_section.markdown,
    )


def parse_semantic_reviews(repo_root: Path) -> tuple[SemanticReview, ...]:
    review_paths = sorted(
        (repo_root / SEMANTIC_REVIEW_PACKET_DIR).glob("*_SEMANTIC_REVIEW.md"),
        key=lambda path: path.relative_to(repo_root).as_posix(),
    )
    return tuple(parse_semantic_review_file(path, repo_root) for path in review_paths)


def shadow_review_id_from_path(review_path: Path) -> str:
    stem = review_path.stem
    suffix = "_SHADOW_REVIEW"
    if not stem.endswith(suffix):
        fail(f"{review_path}: shadow review filename must end with '{suffix}.md'")
    review_id = stem[: -len(suffix)].lower()
    if not review_id:
        fail(f"{review_path}: shadow review filename must include a non-empty review id")
    return review_id


def parse_shadow_review_map_entries(
    review_path: Path, repo_root: Path, map_markdown: str
) -> tuple[ShadowReviewMapEntry, ...]:
    lines = [line.rstrip() for line in map_markdown.splitlines() if line.strip()]
    if len(lines) < 3:
        fail(f"{review_path}: shadow review map must include a header, divider, and one row")
    if lines[0] != SHADOW_REVIEW_MAP_HEADER:
        fail(
            f"{review_path}: shadow review map must start with exact header "
            f"'{SHADOW_REVIEW_MAP_HEADER}'"
        )
    if lines[1] != SHADOW_REVIEW_MAP_DIVIDER:
        fail(
            f"{review_path}: shadow review map must use exact divider "
            f"'{SHADOW_REVIEW_MAP_DIVIDER}'"
        )

    entries: list[ShadowReviewMapEntry] = []
    row_re = re.compile(r"^\| \[([A-Za-z0-9-]+)\]\(([^)]+)\) \| (.+) \| (.+) \|$")
    for row_order, line in enumerate(lines[2:], start=1):
        match = row_re.fullmatch(line)
        if match is None:
            fail(f"{review_path}: shadow review map row {row_order} is malformed")
        technique_id = match.group(1).strip()
        target = match.group(2).strip()
        current_role = match.group(3).strip()
        current_shadow_seam = match.group(4).strip()
        if not current_role:
            fail(f"{review_path}: shadow review map row {row_order} must include current role")
        if not current_shadow_seam:
            fail(
                f"{review_path}: shadow review map row {row_order} must include current shadow seam"
            )

        resolved_target = review_path.parent.joinpath(*PurePosixPath(target).parts).resolve()
        try:
            technique_path = resolved_target.relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            fail(
                f"{review_path}: shadow review map row {row_order} points outside the repo: "
                f"'{target}'"
            )
        if not resolved_target.is_file():
            fail(
                f"{review_path}: shadow review map row {row_order} points to missing file "
                f"'{target}'"
            )

        entries.append(
            ShadowReviewMapEntry(
                technique_id=technique_id,
                technique_path=technique_path,
                current_role=current_role,
                current_shadow_seam=current_shadow_seam,
            )
        )

    return tuple(entries)


def parse_shadow_review_seams(
    review_path: Path, seam_markdown: str
) -> tuple[ShadowReviewSeam, ...]:
    matches = list(SUBSECTION_RE.finditer(seam_markdown))
    if not matches:
        fail(f"{review_path}: shadow review '## Seam Review' must include '### ' subsections")

    intro = normalize_section_markdown(seam_markdown[: matches[0].start()])
    if intro:
        fail(f"{review_path}: shadow review '## Seam Review' must not include prose before seams")

    seams: list[ShadowReviewSeam] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(seam_markdown)
        heading = match.group(1).strip()
        body_markdown = normalize_section_markdown(seam_markdown[start:end])
        if not body_markdown:
            fail(f"{review_path}: shadow review seam '{heading}' must not be empty")

        lines = body_markdown.splitlines()
        nonblank_indexes = [line_index for line_index, line in enumerate(lines) if line.strip()]
        if not nonblank_indexes:
            fail(f"{review_path}: shadow review seam '{heading}' must contain a question")
        question_index = nonblank_indexes[0]
        question_line = lines[question_index].strip()
        if not question_line.startswith(SHADOW_REVIEW_QUESTION_PREFIX):
            fail(
                f"{review_path}: shadow review seam '{heading}' must start with "
                f"'{SHADOW_REVIEW_QUESTION_PREFIX}'"
            )
        question = question_line[len(SHADOW_REVIEW_QUESTION_PREFIX) :].strip()
        if not question:
            fail(f"{review_path}: shadow review seam '{heading}' question must not be empty")

        analysis_markdown = normalize_section_markdown("\n".join(lines[question_index + 1 :]))
        if not analysis_markdown:
            fail(f"{review_path}: shadow review seam '{heading}' must include analysis markdown")
        outcome = extract_last_outcome(analysis_markdown)
        if outcome is None:
            fail(
                f"{review_path}: shadow review seam '{heading}' must include an "
                f"'{SHADOW_REVIEW_OUTCOME_MARKER}' marker"
            )

        seams.append(
            ShadowReviewSeam(
                heading=heading,
                question=question,
                analysis_markdown=analysis_markdown,
                outcome=outcome,
            )
        )

    return tuple(seams)


def parse_shadow_review_findings(
    review_path: Path, findings_markdown: str
) -> tuple[tuple[ShadowReviewFinding, ...], str]:
    lines = findings_markdown.splitlines()
    top_level_indexes = top_level_meaningful_indexes(lines)
    if len(top_level_indexes) < 2:
        fail(
            f"{review_path}: shadow review '## Findings' must include bullet findings and "
            f"'{SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )

    last_index = top_level_indexes[-1]
    overall_line = lines[last_index].strip()
    if not overall_line.startswith(SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX):
        fail(
            f"{review_path}: shadow review '## Findings' must end with "
            f"'{SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX}'"
        )
    overall_outcome = overall_line[len(SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX) :].strip()
    if not overall_outcome:
        fail(f"{review_path}: shadow review overall outcome must not be empty")

    findings: list[ShadowReviewFinding] = []
    item_indexes = top_level_indexes[:-1]
    for order, start_index in enumerate(item_indexes, start=1):
        line = lines[start_index]
        if not line.startswith("- "):
            fail(
                f"{review_path}: shadow review findings must use top-level '- ' bullets before "
                f"the overall outcome"
            )
        end_index = item_indexes[order] if order < len(item_indexes) else last_index
        chunk_lines = lines[start_index:end_index]
        text = item_text_markdown(chunk_lines[0][2:].strip(), chunk_lines[1:])
        if not text:
            fail(f"{review_path}: shadow review finding {order} must not be empty")
        findings.append(ShadowReviewFinding(text=text))

    return tuple(findings), overall_outcome


def parse_shadow_review_file(review_path: Path, repo_root: Path) -> ShadowReview:
    title, lines, title_index = parse_titled_markdown_file(review_path, "shadow review")
    review_id = shadow_review_id_from_path(review_path)
    review_path_str = review_path.relative_to(repo_root).as_posix()
    body = "\n".join(lines[title_index + 1 :])

    intro_markdown, sections = split_semantic_review_body(review_path, body)
    if len(sections) != 4:
        fail(
            f"{review_path}: shadow review doc must include exactly map, seam review, findings, "
            f"and next step sections"
        )

    headings = [section.heading for section in sections]
    if not headings[0].endswith(" Map"):
        fail(f"{review_path}: first shadow review section must end with ' Map'")
    if headings[1] != "Seam Review":
        fail(f"{review_path}: second shadow review section must be '## Seam Review'")
    if headings[2] != "Findings":
        fail(f"{review_path}: third shadow review section must be '## Findings'")
    if headings[3] != "Next Step":
        fail(f"{review_path}: final shadow review section must be '## Next Step'")

    map_section, seam_section, findings_section, next_step_section = sections
    map_entries = parse_shadow_review_map_entries(review_path, repo_root, map_section.markdown)
    seams = parse_shadow_review_seams(review_path, seam_section.markdown)
    findings, overall_outcome = parse_shadow_review_findings(review_path, findings_section.markdown)

    return ShadowReview(
        review_id=review_id,
        review_path=review_path_str,
        title=title,
        intro_markdown=intro_markdown,
        map_heading=map_section.heading,
        map_entries=map_entries,
        seams=seams,
        findings=findings,
        overall_outcome=overall_outcome,
        next_step_markdown=next_step_section.markdown,
    )


def parse_shadow_reviews(repo_root: Path) -> tuple[ShadowReview, ...]:
    review_paths = sorted(
        (repo_root / SHADOW_REVIEW_PACKET_DIR).glob("*_SHADOW_REVIEW.md"),
        key=lambda path: path.relative_to(repo_root).as_posix(),
    )
    return tuple(parse_shadow_review_file(path, repo_root) for path in review_paths)


def validate_repo_doc_surface_specs(repo_root: Path) -> None:
    if len(REPO_DOC_SURFACE_SPECS) != 21:
        fail("REPO_DOC_SURFACE_SPECS must contain exactly the 21 authoritative public route/canon/status files")
    if len(REPO_DOC_SURFACE_GROUP_SPECS) != len(REPO_DOC_SURFACE_GROUP_ORDER):
        fail("REPO_DOC_SURFACE_GROUP_SPECS must contain exactly one spec per surface group")

    seen_groups: set[str] = set()
    for spec in REPO_DOC_SURFACE_GROUP_SPECS:
        group = spec["group"]
        if group not in REPO_DOC_SURFACE_GROUP_ORDER:
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS: unsupported group '{group}'")
        if group in seen_groups:
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS: duplicate group '{group}'")
        seen_groups.add(group)
        if not spec["heading"].strip():
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS[{group}]: heading must not be empty")
        if not spec["note"].strip():
            fail(f"REPO_DOC_SURFACE_GROUP_SPECS[{group}]: note must not be empty")

    if tuple(spec["group"] for spec in REPO_DOC_SURFACE_GROUP_SPECS) != REPO_DOC_SURFACE_GROUP_ORDER:
        fail("REPO_DOC_SURFACE_GROUP_SPECS must follow REPO_DOC_SURFACE_GROUP_ORDER")

    seen_doc_ids: set[str] = set()
    seen_doc_paths: set[str] = set()
    doc_ids = {spec["doc_id"] for spec in REPO_DOC_SURFACE_SPECS}

    for spec in REPO_DOC_SURFACE_SPECS:
        doc_id = spec["doc_id"]
        doc_path = spec["doc_path"]
        surface_group = spec["surface_group"]
        bounded_role = spec["bounded_role"]

        if doc_id in seen_doc_ids:
            fail(f"REPO_DOC_SURFACE_SPECS: duplicate doc_id '{doc_id}'")
        if doc_path in seen_doc_paths:
            fail(f"REPO_DOC_SURFACE_SPECS: duplicate doc_path '{doc_path}'")
        seen_doc_ids.add(doc_id)
        seen_doc_paths.add(doc_path)

        if surface_group not in seen_groups:
            fail(
                f"REPO_DOC_SURFACE_SPECS[{doc_id}]: surface_group '{surface_group}' must be declared in REPO_DOC_SURFACE_GROUP_SPECS"
            )
        if not bounded_role.strip():
            fail(f"REPO_DOC_SURFACE_SPECS[{doc_id}]: bounded_role must not be empty")

        target = repo_root / doc_path
        if not target.is_file():
            fail(f"REPO_DOC_SURFACE_SPECS[{doc_id}]: missing source doc '{doc_path}'")

    seen_questions: set[str] = set()
    for spec in REPO_DOC_NAVIGATION_SPECS:
        question = spec["question"]
        if question in seen_questions:
            fail(f"REPO_DOC_NAVIGATION_SPECS: duplicate question '{question}'")
        seen_questions.add(question)
        if not question.strip():
            fail("REPO_DOC_NAVIGATION_SPECS: question must not be empty")

        doc_id_list = tuple(spec["doc_ids"])
        if not doc_id_list:
            fail(f"REPO_DOC_NAVIGATION_SPECS[{question}]: doc_ids must not be empty")
        for doc_id in doc_id_list:
            if doc_id not in doc_ids:
                fail(f"REPO_DOC_NAVIGATION_SPECS[{question}]: unknown doc_id '{doc_id}'")
        if not spec["note"].strip():
            fail(f"REPO_DOC_NAVIGATION_SPECS[{question}]: note must not be empty")


def parse_repo_doc_surface_file(repo_root: Path, spec: dict[str, str]) -> RepoDocSurface:
    doc_path = repo_root / spec["doc_path"]
    title, lines, title_index = parse_titled_markdown_file(doc_path, "repo doc surface")
    return RepoDocSurface(
        doc_id=spec["doc_id"],
        doc_path=spec["doc_path"],
        title=title,
        surface_group=spec["surface_group"],
        bounded_role=spec["bounded_role"],
        top_level_sections=extract_top_level_section_headings(doc_path, lines, title_index),
    )


def parse_repo_doc_surfaces(repo_root: Path) -> tuple[RepoDocSurface, ...]:
    validate_repo_doc_surface_specs(repo_root)
    return tuple(parse_repo_doc_surface_file(repo_root, spec) for spec in REPO_DOC_SURFACE_SPECS)


def validate_selection_working_set_specs(repo_root: Path) -> None:
    reviews_by_path = {
        review.review_path: review for review in parse_semantic_reviews(repo_root)
    }

    for spec in WORKING_SET_SPECS:
        review_doc = spec["review_doc"]
        if review_doc not in reviews_by_path:
            fail(
                f"{Path(review_doc).name}: review-backed working set '{spec['title']}' points to a "
                f"missing semantic review doc"
            )

        actual_ids = tuple(entry.technique_id for entry in reviews_by_path[review_doc].map_entries)
        expected_ids = tuple(spec["technique_ids"])
        if actual_ids != expected_ids:
            fail(
                f"{Path(review_doc).name}: working set '{spec['title']}' must match semantic review "
                f"map entry order {expected_ids}, found {actual_ids}"
            )


def validate_shadow_working_set_specs(records: list[TechniqueRecord], repo_root: Path) -> None:
    records_by_id = {record.id: record for record in records}
    reviews_by_path = {
        review.review_path: review for review in parse_shadow_reviews(repo_root)
    }

    for spec in SHADOW_WORKING_SET_SPECS:
        review_doc = spec["review_doc"]
        if review_doc not in reviews_by_path:
            fail(
                f"{Path(review_doc).name}: review-backed shadow working set '{spec['title']}' points "
                f"to a missing shadow review doc"
            )

        technique_ids = tuple(spec["technique_ids"])
        if not technique_ids:
            fail(f"{Path(review_doc).name}: shadow working set '{spec['title']}' must not be empty")

        actual_ids = tuple(entry.technique_id for entry in reviews_by_path[review_doc].map_entries)
        if actual_ids != technique_ids:
            fail(
                f"{Path(review_doc).name}: shadow working set '{spec['title']}' must match shadow "
                f"review map entry order {technique_ids}, found {actual_ids}"
            )

        for technique_id in technique_ids:
            record = records_by_id.get(technique_id)
            if record is None:
                fail(
                    f"{Path(review_doc).name}: shadow working set '{spec['title']}' "
                    f"references unknown technique '{technique_id}'"
                )
            if record.status != "canonical":
                fail(
                    f"{Path(review_doc).name}: shadow working set '{spec['title']}' "
                    f"must stay canonical-only, found '{technique_id}' with status '{record.status}'"
                )
            if "adverse_effects_review" not in {note.kind for note in record.notes}:
                fail(
                    f"{Path(review_doc).name}: shadow working set '{spec['title']}' "
                    f"requires typed adverse-effects reviews for '{technique_id}'"
                )


def validate_shadow_question_specs(records: list[TechniqueRecord]) -> None:
    records_by_id = {record.id: record for record in records}
    shadow_targets = {
        technique_id
        for spec in SHADOW_WORKING_SET_SPECS
        for technique_id in spec["technique_ids"]
    }

    for spec in SHADOW_COMMON_QUESTION_SPECS:
        target_id = spec["target_id"]
        record = records_by_id.get(target_id)
        if record is None:
            fail(f"SHADOW_COMMON_QUESTION_SPECS: unknown target_id '{target_id}'")
        if record.status != "canonical":
            fail(f"SHADOW_COMMON_QUESTION_SPECS: target_id '{target_id}' must be canonical")
        if target_id not in shadow_targets:
            fail(
                f"SHADOW_COMMON_QUESTION_SPECS[{target_id}]: target must belong to a declared "
                "shadow working set"
            )


def validate_repo_doc_navigation_specs(repo_root: Path) -> None:
    validate_repo_doc_surface_specs(repo_root)
    surfaces_by_id = {
        surface.doc_id: surface for surface in parse_repo_doc_surfaces(repo_root)
    }

    for spec in REPO_DOC_NAVIGATION_SPECS:
        for doc_id in spec["doc_ids"]:
            if doc_id not in surfaces_by_id:
                fail(
                    f"REPO_DOC_NAVIGATION_SPECS[{spec['question']}]: doc_id '{doc_id}' is not present in parsed repo doc surfaces"
                )


def validate_selection_navigation_specs(records: list[TechniqueRecord], repo_root: Path) -> None:
    records_by_id = {record.id: record for record in records}
    reviews_by_path = {
        review.review_path: review for review in parse_semantic_reviews(repo_root)
    }
    canonical_domains = {
        record.domain for record in records if record.status == "canonical"
    }

    if len(DOMAIN_START_SPECS) != len(DOMAIN_ORDER):
        fail("DOMAIN_START_SPECS must contain exactly one spec per domain")

    seen_domains: set[str] = set()
    domain_start_targets: dict[str, str] = {}
    for spec in DOMAIN_START_SPECS:
        domain = spec["domain"]
        if domain not in DOMAIN_VALUES:
            fail(f"DOMAIN_START_SPECS: unsupported domain '{domain}'")
        if domain in seen_domains:
            fail(f"DOMAIN_START_SPECS: duplicate domain '{domain}'")
        seen_domains.add(domain)

        lead_ids = tuple(spec["lead_ids"])
        if not lead_ids:
            fail(f"DOMAIN_START_SPECS[{domain}]: lead_ids must not be empty")
        domain_start_targets[domain] = lead_ids[0]

        for review_doc in spec.get("review_docs", ()):
            if review_doc not in reviews_by_path:
                fail(
                    f"DOMAIN_START_SPECS[{domain}]: review doc '{review_doc}' does not exist"
                )

        for technique_id in lead_ids:
            record = records_by_id.get(technique_id)
            if record is None:
                fail(f"DOMAIN_START_SPECS[{domain}]: unknown technique id '{technique_id}'")
            if domain in canonical_domains:
                if record.status != "canonical":
                    fail(
                        f"DOMAIN_START_SPECS[{domain}]: lead_id '{technique_id}' must be canonical because domain '{domain}' already has canonical techniques"
                    )
            elif record.status not in {"canonical", "promoted"}:
                fail(
                    f"DOMAIN_START_SPECS[{domain}]: lead_id '{technique_id}' must be canonical or promoted"
                )
            if record.domain != domain:
                fail(
                    f"DOMAIN_START_SPECS[{domain}]: lead_id '{technique_id}' must belong to domain '{domain}'"
                )

    if set(domain_start_targets) != set(DOMAIN_ORDER):
        fail("DOMAIN_START_SPECS must cover every domain exactly once")

    for spec in COMMON_MOVE_SPECS:
        target_id = spec["target_id"]
        record = records_by_id.get(target_id)
        if record is None:
            fail(f"COMMON_MOVE_SPECS: unknown target_id '{target_id}'")
        if record.status != "canonical":
            fail(f"COMMON_MOVE_SPECS: target_id '{target_id}' must be canonical")

        basis_type = spec["basis_type"]
        if basis_type == COMMON_MOVE_BASIS_DIRECT_RELATION:
            anchor_ids = tuple(spec.get("anchor_ids", ()))
            if not anchor_ids:
                fail(
                    f"COMMON_MOVE_SPECS[{target_id}]: direct_relation moves require non-empty anchor_ids"
                )
            for anchor_id in anchor_ids:
                anchor = records_by_id.get(anchor_id)
                if anchor is None:
                    fail(f"COMMON_MOVE_SPECS[{target_id}]: unknown anchor_id '{anchor_id}'")
                direct_relation_found = any(
                    relation["target"] == target_id for relation in anchor.frontmatter["relations"]
                ) or any(
                    relation["target"] == anchor_id for relation in record.frontmatter["relations"]
                )
                if not direct_relation_found:
                    fail(
                        f"COMMON_MOVE_SPECS[{target_id}]: anchor_id '{anchor_id}' must have a direct relation with '{target_id}'"
                    )
            continue

        if basis_type == COMMON_MOVE_BASIS_DOMAIN_START:
            domain = spec.get("domain")
            if domain not in domain_start_targets:
                fail(
                    f"COMMON_MOVE_SPECS[{target_id}]: domain_start move requires a valid domain"
                )
            expected_target = domain_start_targets[domain]
            if target_id != expected_target:
                fail(
                    f"COMMON_MOVE_SPECS[{target_id}]: domain_start move for '{domain}' must point to '{expected_target}'"
                )
            continue

        fail(
            f"COMMON_MOVE_SPECS[{target_id}]: unsupported basis_type '{basis_type}'"
        )



def validate_stage1_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_STAGE1_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required Stage 1 file '{relative_path}'")


def validate_selection_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_SELECTION_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required selection file '{relative_path}'")


def validate_semantic_review_guide_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_SEMANTIC_REVIEW_GUIDE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required semantic review guide '{relative_path}'")


def validate_kag_source_reader_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KAG_SOURCE_READER_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required KAG source reader file '{relative_path}'")


def validate_capsule_surface_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_CAPSULE_SURFACE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required capsule surface file '{relative_path}'")


def validate_repo_doc_surface_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_REPO_DOC_SURFACE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required repo doc surface file '{relative_path}'")


def validate_kag_export_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KAG_EXPORT_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required KAG export file '{relative_path}'")


def validate_kind_doctrine_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KIND_DOCTRINE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required kind doctrine file '{relative_path}'")


def validate_kind_data_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KIND_DATA_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required kind data file '{relative_path}'")


def validate_kind_surface_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KIND_SURFACE_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required kind surface file '{relative_path}'")


def validate_kind_report_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_KIND_REPORT_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required kind scout report '{relative_path}'")


def validate_tree_report_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_TREE_REPORT_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required tree projection report '{relative_path}'")


def validate_technique_bundle(
    repo_root: Path, technique_dir: Path, expected_domain: str | None, schema_store: dict[str, Any]
) -> TechniqueRecord:
    technique_path = technique_dir / "TECHNIQUE.md"
    if not technique_path.is_file():
        fail(f"{technique_dir}: missing TECHNIQUE.md")

    validate_support_dirs(technique_dir)

    frontmatter_text, body = split_frontmatter(technique_path)
    frontmatter = parse_frontmatter(frontmatter_text, technique_path)
    validate_frontmatter_schema(frontmatter, technique_path, schema_store)
    sections = validate_sections(body, technique_path)
    checklists = parse_checklists(repo_root, technique_dir)
    examples = parse_examples(repo_root, technique_dir)
    notes = parse_notes(repo_root, technique_dir)
    validate_support_references(body, technique_dir, technique_path)

    if expected_domain is not None and frontmatter["domain"] != expected_domain:
        fail(
            f"{technique_path}: frontmatter domain '{frontmatter['domain']}' does not match parent directory '{expected_domain}'"
        )

    return TechniqueRecord(
        technique_dir=technique_dir,
        technique_path=technique_path,
        id=frontmatter["id"],
        name=frontmatter["name"],
        domain=frontmatter["domain"],
        kind=frontmatter["kind"],
        status=frontmatter["status"],
        summary=frontmatter["summary"],
        frontmatter=frontmatter,
        body=body,
        sections=sections,
        checklists=checklists,
        examples=examples,
        notes=notes,
    )


def expected_parent_domain_for_technique(repo_root: Path, technique_dir: Path) -> str | None:
    techniques_dir = repo_root / "techniques"
    try:
        relative_parts = technique_dir.relative_to(techniques_dir).parts
    except ValueError:
        fail(f"{technique_dir}: technique bundle must live under techniques/")

    if len(relative_parts) == 2:
        domain, _slug = relative_parts
        if domain not in DOMAIN_VALUES:
            fail(f"{technique_dir}: unsupported domain directory '{domain}'")
        return domain

    if len(relative_parts) == 3:
        trunk, shelf, _slug = relative_parts
        if trunk not in TREE_TRUNK_VALUES:
            fail(f"{technique_dir}: unsupported tree trunk directory '{trunk}'")
        if not shelf:
            fail(f"{technique_dir}: tree technique path must include a shelf directory")
        return None

    fail(
        f"{technique_dir}: technique bundle path must match "
        "techniques/<domain>/<slug>/ or techniques/<trunk>/<shelf>/<slug>/"
    )


def collect_techniques(repo_root: Path, schema_store: dict[str, Any]) -> list[TechniqueRecord]:
    techniques_dir = repo_root / "techniques"
    if not techniques_dir.is_dir():
        fail(f"{repo_root}: missing techniques/ directory")

    records: list[TechniqueRecord] = []
    seen_ids: set[str] = set()

    for top_level_dir in sorted(path for path in techniques_dir.iterdir() if path.is_dir()):
        if top_level_dir.name not in DOMAIN_VALUES and top_level_dir.name not in TREE_TRUNK_VALUES:
            fail(f"{top_level_dir}: unsupported technique root directory '{top_level_dir.name}'")

    for technique_path in sorted(techniques_dir.rglob("TECHNIQUE.md")):
        technique_dir = technique_path.parent
        expected_domain = expected_parent_domain_for_technique(repo_root, technique_dir)
        record = validate_technique_bundle(repo_root, technique_dir, expected_domain, schema_store)
        if record.id in seen_ids:
            fail(f"duplicate technique id '{record.id}' at {record.technique_dir}")
        seen_ids.add(record.id)
        records.append(record)

    if not records:
        fail(f"{repo_root}: no technique bundles found under techniques/")

    return records


def parse_index_rows(index_path: Path) -> dict[str, list[IndexRow]]:
    rows_by_id: dict[str, list[IndexRow]] = {}
    current_section = ""

    for line in read_text(index_path).splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue

        if current_section not in SECTION_STATUS or not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        if not cells:
            continue
        if cells[0] == "id":
            continue
        if all(re.fullmatch(r"-+", cell) for cell in cells):
            continue
        if all(cell == "-" for cell in cells):
            continue

        if current_section == "Deprecated techniques":
            if len(cells) != 4:
                fail(f"{index_path}: malformed row in deprecated table: {line}")
            row_id, name, _replacement, _note = cells
            if row_id == "-":
                continue
            row = IndexRow(
                section=current_section,
                id=row_id,
                name=name,
                domain="",
                status="deprecated",
                summary="",
            )
        else:
            if len(cells) != 5:
                fail(f"{index_path}: malformed row in {current_section}: {line}")
            row_id, name, domain, status, summary = cells
            if row_id == "-":
                continue
            row = IndexRow(
                section=current_section,
                id=row_id,
                name=name,
                domain=domain,
                status=status,
                summary=summary,
            )

        rows_by_id.setdefault(row.id, []).append(row)

    return rows_by_id


def validate_index(repo_root: Path, records: list[TechniqueRecord]) -> None:
    index_path = repo_root / "TECHNIQUE_INDEX.md"
    if not index_path.is_file():
        fail(f"{repo_root}: missing TECHNIQUE_INDEX.md")

    rows_by_id = parse_index_rows(index_path)
    records_by_id = {record.id: record for record in records}

    for row_id in rows_by_id:
        if row_id not in records_by_id:
            fail(f"{index_path}: index contains unknown technique id '{row_id}'")

    for record in records:
        rows = rows_by_id.get(record.id)
        if not rows:
            fail(f"{index_path}: missing row for technique '{record.id}'")
        if len(rows) != 1:
            fail(f"{index_path}: technique '{record.id}' appears more than once in the index")

        row = rows[0]
        expected_section = STATUS_SECTION[record.status]
        if row.section != expected_section:
            fail(
                f"{index_path}: technique '{record.id}' is in '{row.section}' but should be in '{expected_section}'"
            )

        if row.name != record.name:
            fail(
                f"{index_path}: technique '{record.id}' name mismatch: index='{row.name}' technique='{record.name}'"
            )

        if record.status in {"canonical", "promoted"}:
            if row.domain != record.domain:
                fail(
                    f"{index_path}: technique '{record.id}' domain mismatch: index='{row.domain}' technique='{record.domain}'"
                )
            if row.status != record.status:
                fail(
                    f"{index_path}: technique '{record.id}' status mismatch: index='{row.status}' technique='{record.status}'"
                )
            if row.summary != record.summary:
                fail(
                    f"{index_path}: technique '{record.id}' summary mismatch between index and frontmatter"
                )


def expected_evidence_kind(relative_path: str) -> str:
    return EVIDENCE_KIND_BY_NAME.get(Path(relative_path).name, "support_note")


def validate_evidence(records: list[TechniqueRecord]) -> None:
    for record in records:
        notes_dir = record.technique_dir / "notes"
        actual_note_paths = sorted(
            path.relative_to(record.technique_dir).as_posix()
            for path in notes_dir.rglob("*.md")
        )
        evidence_items = record.frontmatter["evidence"]
        evidence_paths = [item["path"] for item in evidence_items]

        if sorted(evidence_paths) != actual_note_paths:
            fail(
                f"{record.technique_path}: evidence paths do not match notes/ contents: "
                f"frontmatter={sorted(evidence_paths)} notes={actual_note_paths}"
            )

        if len(set(evidence_paths)) != len(evidence_paths):
            fail(f"{record.technique_path}: evidence paths must be unique")

        has_adverse_effects_review = ADVERSE_EFFECTS_REVIEW_PATH in actual_note_paths
        if record.status == "canonical":
            if not has_adverse_effects_review:
                fail(
                    f"{record.technique_path}: canonical techniques must include "
                    f"'{ADVERSE_EFFECTS_REVIEW_PATH}'"
                )
        elif has_adverse_effects_review:
            fail(
                f"{record.technique_path}: only canonical techniques may include "
                f"'{ADVERSE_EFFECTS_REVIEW_PATH}'"
            )

        for item in evidence_items:
            expected_kind = expected_evidence_kind(item["path"])
            if item["kind"] != expected_kind:
                fail(
                    f"{record.technique_path}: evidence '{item['path']}' must use kind '{expected_kind}', "
                    f"found '{item['kind']}'"
                )


def validate_relations(records: list[TechniqueRecord]) -> None:
    known_ids = {record.id for record in records}
    for record in records:
        seen_pairs: set[tuple[str, str]] = set()
        for relation in record.frontmatter["relations"]:
            pair = (relation["type"], relation["target"])
            if relation["target"] == record.id:
                fail(f"{record.technique_path}: relation '{relation['type']}' cannot target itself")
            if relation["target"] not in known_ids:
                fail(
                    f"{record.technique_path}: relation target '{relation['target']}' does not exist"
                )
            if pair in seen_pairs:
                fail(
                    f"{record.technique_path}: duplicate relation '{relation['type']}' -> '{relation['target']}'"
                )
            seen_pairs.add(pair)


def validate_technique_source_contracts(repo_root: Path) -> list[TechniqueRecord]:
    validate_source_fast_required_files(repo_root)
    validate_memo_agents_portable_validation_route(repo_root)
    schema_store = load_schema_store(repo_root)
    validate_kind_axis_alignment(repo_root, schema_store)
    records = collect_techniques(repo_root, schema_store)
    validate_family_scout_alignment(repo_root)
    validate_topology_axes_registry(repo_root)
    validate_kind_overlay(repo_root, records)
    validate_repo_doc_surface_specs(repo_root)
    validate_selection_working_set_specs(repo_root)
    validate_shadow_working_set_specs(records, repo_root)
    validate_shadow_question_specs(records)
    validate_selection_navigation_specs(records, repo_root)
    validate_repo_doc_navigation_specs(repo_root)
    validate_index(repo_root, records)
    validate_evidence(records)
    validate_relations(records)
    return records
