from __future__ import annotations

from pathlib import Path

from technique_intelligence_surface import (
    DAG_MIN_PATH,
    DAG_PATH,
    READER_PATH,
    REGISTRY_MIN_PATH,
    REGISTRY_PATH,
    build_all_outputs,
    write_all_outputs,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    write_all_outputs(repo_root)
    outputs = build_all_outputs(repo_root)

    print(f"[ok] wrote {REGISTRY_PATH.as_posix()}")
    print(f"[ok] wrote {REGISTRY_MIN_PATH.as_posix()}")
    print(f"[ok] wrote {DAG_PATH.as_posix()}")
    print(f"[ok] wrote {DAG_MIN_PATH.as_posix()}")
    print(f"[ok] wrote {READER_PATH.as_posix()}")
    print(f"[ok] indexed {outputs['registry']['technique_count']} technique moves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
