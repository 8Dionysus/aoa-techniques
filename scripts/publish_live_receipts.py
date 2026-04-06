#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG_PATH = REPO_ROOT / ".aoa" / "live_receipts" / "technique-receipts.jsonl"
ALLOWED_EVENT_KINDS = {
    "technique_promotion_receipt",
    "technique_publication_receipt",
}


class ReceiptPublishError(ValueError):
    pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append bounded technique-layer receipts to the owner-local live JSONL log."
    )
    parser.add_argument(
        "--input",
        action="append",
        default=[],
        help="Path to a JSON or JSONL file containing one receipt, an array of receipts, or one receipt per line.",
    )
    parser.add_argument(
        "--log-path",
        default=str(DEFAULT_LOG_PATH),
        help="Owner-local JSONL log that should receive newly published technique receipts.",
    )
    return parser.parse_args(argv)


def validate_receipt(receipt: dict[str, Any], *, location: str) -> None:
    required_fields = (
        "event_kind",
        "event_id",
        "observed_at",
        "run_ref",
        "session_ref",
        "actor_ref",
        "object_ref",
        "evidence_refs",
        "payload",
    )
    for field in required_fields:
        if field not in receipt:
            raise ReceiptPublishError(f"{location}: missing field {field!r}")
    event_kind = receipt["event_kind"]
    if event_kind not in ALLOWED_EVENT_KINDS:
        raise ReceiptPublishError(
            f"{location}.event_kind: unsupported technique receipt kind {event_kind!r}"
        )
    if not isinstance(receipt["event_id"], str) or not receipt["event_id"]:
        raise ReceiptPublishError(f"{location}.event_id: must be a non-empty string")
    if not isinstance(receipt["object_ref"], dict):
        raise ReceiptPublishError(f"{location}.object_ref: must be an object")
    if not isinstance(receipt["evidence_refs"], list):
        raise ReceiptPublishError(f"{location}.evidence_refs: must be a list")
    if not isinstance(receipt["payload"], dict):
        raise ReceiptPublishError(f"{location}.payload: must be an object")


def load_receipts(paths: list[Path]) -> list[dict[str, Any]]:
    receipts: list[dict[str, Any]] = []
    for path in paths:
        if path.suffix == ".jsonl":
            for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                line = raw_line.strip()
                if not line:
                    continue
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ReceiptPublishError(f"{path}:{line_number}: receipt must be an object")
                validate_receipt(item, location=f"{path}:{line_number}")
                receipts.append(item)
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            validate_receipt(payload, location=str(path))
            receipts.append(payload)
            continue
        if not isinstance(payload, list):
            raise ReceiptPublishError(f"{path}: receipt payload must be an object or list")
        for index, item in enumerate(payload):
            if not isinstance(item, dict):
                raise ReceiptPublishError(f"{path}[{index}]: receipt must be an object")
            validate_receipt(item, location=f"{path}[{index}]")
            receipts.append(item)
    return receipts


def load_existing_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    event_ids: set[str] = set()
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        item = json.loads(line)
        if not isinstance(item, dict):
            raise ReceiptPublishError(f"{path}:{line_number}: existing log line must be an object")
        event_id = item.get("event_id")
        if isinstance(event_id, str) and event_id:
            event_ids.add(event_id)
    return event_ids


def append_new_receipts(*, log_path: Path, receipts: list[dict[str, Any]]) -> tuple[int, int]:
    existing_ids = load_existing_ids(log_path)
    appended = 0
    skipped = 0
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        for receipt in receipts:
            event_id = receipt["event_id"]
            if event_id in existing_ids:
                skipped += 1
                continue
            handle.write(json.dumps(receipt, sort_keys=True, ensure_ascii=False) + "\n")
            existing_ids.add(event_id)
            appended += 1
    return appended, skipped


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    input_paths = [Path(path).expanduser().resolve() for path in args.input]
    if not input_paths:
        raise SystemExit("no receipt input files were provided")
    log_path = Path(args.log_path).expanduser().resolve()
    receipts = load_receipts(input_paths)
    appended, skipped = append_new_receipts(log_path=log_path, receipts=receipts)
    print(f"[ok] appended {appended} technique receipts to {log_path}")
    print(f"[skip] duplicate event ids skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
