from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_topology_scout_markdown,
    build_topology_scout_payload,
    load_topology_axes_registry,
    load_kind_overlay,
    read_json,
    write_json_file,
    write_text_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    reports_dir = repo_root / "reports"
    reports_dir.mkdir(exist_ok=True)

    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    axis_registry = load_topology_axes_registry(repo_root)
    kind_overlay = load_kind_overlay(repo_root)

    report = build_topology_scout_payload(catalog, axis_registry, kind_overlay)
    markdown = build_topology_scout_markdown(report)

    json_path = reports_dir / "technique_topology_scout.json"
    markdown_path = reports_dir / "technique_topology_scout.md"

    write_json_file(json_path, report, compact=False)
    write_text_file(markdown_path, markdown)

    print(f"[ok] wrote {json_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {markdown_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
