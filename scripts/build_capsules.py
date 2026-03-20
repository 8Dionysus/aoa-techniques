from __future__ import annotations

from pathlib import Path

from validate_repo import (
    build_capsule_payload,
    collect_techniques,
    load_schema_store,
    write_json_file,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    schema_store = load_schema_store(repo_root)
    records = collect_techniques(repo_root, schema_store)
    payload = build_capsule_payload(repo_root, records)

    generated_dir = repo_root / "generated"
    generated_dir.mkdir(exist_ok=True)

    path = generated_dir / "technique_capsules.json"
    write_json_file(path, payload, compact=False)

    print(f"[ok] wrote {path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
