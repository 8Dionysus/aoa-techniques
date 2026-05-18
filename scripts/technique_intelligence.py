from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from technique_intelligence_surface import (
    DAG_MIN_PATH,
    DAG_PATH,
    READER_PATH,
    REGISTRY_MIN_PATH,
    REGISTRY_PATH,
    build_all_outputs,
    explain_candidate,
    load_registry,
    pack_candidate,
    search_registry,
    status_payload,
    write_all_outputs,
)


def print_json(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=True, indent=2))


def check_outputs(repo_root: Path) -> int:
    status = status_payload(repo_root)
    print_json(status)
    return 0 if status["status"] == "ok" else 1


def build_command(args: argparse.Namespace) -> int:
    repo_root = args.repo_root
    if args.check:
        return check_outputs(repo_root)

    write_all_outputs(repo_root)
    outputs = build_all_outputs(repo_root)
    print(f"[ok] wrote {REGISTRY_PATH.as_posix()}")
    print(f"[ok] wrote {REGISTRY_MIN_PATH.as_posix()}")
    print(f"[ok] wrote {DAG_PATH.as_posix()}")
    print(f"[ok] wrote {DAG_MIN_PATH.as_posix()}")
    print(f"[ok] wrote {READER_PATH.as_posix()}")
    print(f"[ok] indexed {outputs['registry']['technique_count']} technique moves")
    return 0


def query_command(args: argparse.Namespace) -> int:
    registry = load_registry(args.repo_root)
    print_json(
        search_registry(
            registry,
            args.intent,
            limit=args.limit,
            filters={
                "status": args.status,
                "domain": args.domain,
                "kind": args.kind,
                "execution_profile": args.execution_profile,
                "risk_posture": args.risk_posture,
            },
        )
    )
    return 0


def explain_command(args: argparse.Namespace) -> int:
    registry = load_registry(args.repo_root)
    print_json(explain_candidate(registry, args.technique_id, intent=args.intent))
    return 0


def pack_command(args: argparse.Namespace) -> int:
    registry = load_registry(args.repo_root)
    print_json(pack_candidate(registry, args.technique_id, profile=args.profile))
    return 0


def status_command(args: argparse.Namespace) -> int:
    print_json(status_payload(args.repo_root))
    return 0


def build_parser() -> argparse.ArgumentParser:
    repo_default = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Build and query the source-derived Technique Intelligence layer."
    )
    parser.add_argument("--repo-root", type=Path, default=repo_default)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="write or check generated intelligence outputs")
    build.add_argument("--check", action="store_true", help="fail if outputs are not up to date")
    build.set_defaults(func=build_command)

    query = subparsers.add_parser("query", help="search for technique moves by intent")
    query.add_argument("intent")
    query.add_argument("--limit", type=int, default=5)
    query.add_argument("--status")
    query.add_argument("--domain")
    query.add_argument("--kind")
    query.add_argument("--execution-profile")
    query.add_argument("--risk-posture")
    query.set_defaults(func=query_command)

    explain = subparsers.add_parser("explain", help="explain why one technique fits an intent")
    explain.add_argument("technique_id")
    explain.add_argument("--intent", required=True)
    explain.set_defaults(func=explain_command)

    pack = subparsers.add_parser("pack", help="emit a bounded packet for one selected technique")
    pack.add_argument("technique_id")
    pack.add_argument(
        "--profile",
        choices=("capsule", "small-agent", "orchestrator", "workflow-handoff", "eval-fixture"),
        default="capsule",
    )
    pack.set_defaults(func=pack_command)

    status = subparsers.add_parser("status", help="report generated output freshness")
    status.set_defaults(func=status_command)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.repo_root = args.repo_root.resolve()
    try:
        return args.func(args)
    except (KeyError, ValueError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
