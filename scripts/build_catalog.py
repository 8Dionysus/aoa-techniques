from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_selection_surface_markdown,
    build_selection_patterns_markdown,
    build_catalog_payloads,
    collect_techniques,
    load_schema_store,
    write_json_file,
    write_text_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    schema_store = load_schema_store(repo_root)
    records = collect_techniques(repo_root, schema_store)
    full_catalog, min_catalog = build_catalog_payloads(repo_root, records)

    generated_dir = repo_root / "generated"
    generated_dir.mkdir(exist_ok=True)
    docs_dir = repo_root / "docs"
    docs_dir.mkdir(exist_ok=True)

    full_path = generated_dir / "technique_catalog.json"
    min_path = generated_dir / "technique_catalog.min.json"
    selection_path = docs_dir / "TECHNIQUE_SELECTION.md"
    selection_patterns_path = docs_dir / "SELECTION_PATTERNS.md"

    write_json_file(full_path, full_catalog, compact=False)
    write_json_file(min_path, min_catalog, compact=True)
    write_text_file(selection_path, build_selection_surface_markdown(full_catalog))
    write_text_file(selection_patterns_path, build_selection_patterns_markdown(full_catalog))

    print(f"[ok] wrote {full_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {min_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {selection_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {selection_patterns_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
