from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_family_scout_markdown,
    build_family_scout_payload,
    build_kind_ambiguity_audit_markdown,
    build_kind_manifest_payloads,
    build_kind_reader_markdown,
    load_family_seed,
    load_kind_registry,
    load_wave1_kind_overlay,
    read_json,
    write_json_file,
    write_text_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    generated_dir = repo_root / "generated"
    docs_dir = repo_root / "docs"
    reports_dir = repo_root / "reports"
    generated_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)

    catalog = read_json(generated_dir / "technique_catalog.json")
    registry = load_kind_registry(repo_root)
    family_seed = load_family_seed(repo_root)
    wave1_overlay = load_wave1_kind_overlay(repo_root)

    full_manifest, min_manifest = build_kind_manifest_payloads(catalog, registry)
    family_report = build_family_scout_payload(catalog, family_seed, wave1_overlay)
    kind_reader = build_kind_reader_markdown(full_manifest)
    family_markdown = build_family_scout_markdown(family_report)
    ambiguity_markdown = build_kind_ambiguity_audit_markdown(
        catalog, registry, family_seed, wave1_overlay
    )

    full_path = generated_dir / "technique_kind_manifest.json"
    min_path = generated_dir / "technique_kind_manifest.min.json"
    reader_path = docs_dir / "TECHNIQUE_KINDS.md"
    family_markdown_path = reports_dir / "technique_family_scout.md"
    family_json_path = reports_dir / "technique_family_scout.json"
    ambiguity_path = reports_dir / "kind_ambiguity_audit.md"

    write_json_file(full_path, full_manifest, compact=False)
    write_json_file(min_path, min_manifest, compact=True)
    write_text_file(reader_path, kind_reader)
    write_text_file(family_markdown_path, family_markdown)
    write_json_file(family_json_path, family_report, compact=False)
    write_text_file(ambiguity_path, ambiguity_markdown)

    print(f"[ok] wrote {full_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {min_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {reader_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {family_markdown_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {family_json_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {ambiguity_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
