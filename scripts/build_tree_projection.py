from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_tree_projection_markdown,
    build_tree_projection_payload,
    load_wave1_kind_overlay,
    read_json,
    write_json_file,
    write_text_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    reports_dir = repo_root / "reports"
    reports_dir.mkdir(exist_ok=True)

    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    wave1_overlay = load_wave1_kind_overlay(repo_root)

    report = build_tree_projection_payload(catalog, wave1_overlay)
    markdown = build_tree_projection_markdown(report)

    json_path = reports_dir / "technique_tree_projection.json"
    markdown_path = reports_dir / "technique_tree_projection.md"

    write_json_file(json_path, report, compact=False)
    write_text_file(markdown_path, markdown)

    print(f"[ok] wrote {json_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {markdown_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
