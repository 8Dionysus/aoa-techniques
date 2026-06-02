from __future__ import annotations

try:  # Supports package imports and direct `python scripts/validate_repo.py`.
    from scripts.validators import *
except ImportError:  # pragma: no cover - exercised by direct script execution
    from validators import *  # type: ignore

if __name__ == "__main__":
    raise SystemExit(main())
