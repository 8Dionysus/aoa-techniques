from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_kag_export_payloads,
    collect_techniques,
    load_schema_store,
    write_json_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    schema_store = load_schema_store(repo_root)
    records = collect_techniques(repo_root, schema_store)
    full_payload, min_payload = build_kag_export_payloads(repo_root, records)

    generated_dir = repo_root / "generated"
    generated_dir.mkdir(exist_ok=True)

    full_path = generated_dir / "kag_export.json"
    min_path = generated_dir / "kag_export.min.json"
    write_json_file(full_path, full_payload, compact=False)
    write_json_file(min_path, min_payload, compact=True)

    print(f"[ok] wrote {full_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {min_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
