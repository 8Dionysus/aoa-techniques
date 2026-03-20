from __future__ import annotations

from pathlib import Path

from validate_repo import build_shadow_review_manifest_payloads, write_json_file


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    full_manifest, min_manifest = build_shadow_review_manifest_payloads(repo_root)

    generated_dir = repo_root / "generated"
    generated_dir.mkdir(exist_ok=True)

    full_path = generated_dir / "shadow_review_manifest.json"
    min_path = generated_dir / "shadow_review_manifest.min.json"

    write_json_file(full_path, full_manifest, compact=False)
    write_json_file(min_path, min_manifest, compact=True)

    print(f"[ok] wrote {full_path.relative_to(repo_root).as_posix()}")
    print(f"[ok] wrote {min_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
