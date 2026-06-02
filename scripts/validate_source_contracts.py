from __future__ import annotations

import sys
from pathlib import Path

try:  # Supports package imports and direct `python scripts/validate_source_contracts.py`.
    from scripts.validators import ValidationError, validate_technique_source_contracts
except ImportError:  # pragma: no cover - exercised by direct script execution
    from validators import ValidationError, validate_technique_source_contracts  # type: ignore


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    try:
        records = validate_technique_source_contracts(repo_root)
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    canonical_count = sum(1 for record in records if record.status == "canonical")
    promoted_count = sum(1 for record in records if record.status == "promoted")
    deprecated_count = sum(1 for record in records if record.status == "deprecated")
    print(
        f"[ok] validated source contracts for {len(records)} technique bundles "
        f"({canonical_count} canonical, {promoted_count} promoted, {deprecated_count} deprecated)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
