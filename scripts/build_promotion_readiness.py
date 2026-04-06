from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_promotion_readiness_payload,
    collect_techniques,
    load_schema_store,
    write_json_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    schema_store = load_schema_store(repo_root)
    records = collect_techniques(repo_root, schema_store)
    payload = build_promotion_readiness_payload(repo_root, records)

    generated_dir = repo_root / "generated"
    generated_dir.mkdir(exist_ok=True)
    output_path = generated_dir / "technique_promotion_readiness.min.json"
    write_json_file(output_path, payload, compact=True)
    print(f"[ok] wrote {output_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
