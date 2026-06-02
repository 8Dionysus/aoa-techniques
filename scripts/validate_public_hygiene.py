from __future__ import annotations

import sys
from pathlib import Path

try:
    from scripts.validators import ValidationError, validate_public_hygiene
except ImportError:  # pragma: no cover - direct script execution
    from validators import ValidationError, validate_public_hygiene  # type: ignore


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    try:
        validate_public_hygiene(repo_root)
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    print("[ok] public hygiene validates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
