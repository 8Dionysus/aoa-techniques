from __future__ import annotations

import subprocess
import sys
from pathlib import Path


TEST_DIRS = (
    Path("tests"),
    Path("mechanics/tests"),
    Path("mechanics/agon/tests"),
    Path("mechanics/antifragility/tests"),
    Path("mechanics/audit/tests"),
    Path("mechanics/boundary-bridge/tests"),
    Path("mechanics/checkpoint/tests"),
    Path("mechanics/distillation/tests"),
    Path("mechanics/experience/tests"),
    Path("mechanics/growth-cycle/tests"),
    Path("mechanics/method-growth/tests"),
    Path("mechanics/questbook/tests"),
    Path("mechanics/recurrence/tests"),
    Path("mechanics/release-support/tests"),
    Path("mechanics/rpg/tests"),
)


def has_unittest_files(test_dir: Path) -> bool:
    return test_dir.is_dir() and any(test_dir.glob("test*.py"))


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    ran = 0

    for test_dir in TEST_DIRS:
        if not has_unittest_files(repo_root / test_dir):
            continue
        command = (
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(test_dir),
            "-p",
            "test*.py",
        )
        print(f"[run] {' '.join(command)}", flush=True)
        subprocess.run(command, cwd=repo_root, check=True)
        ran += 1

    if ran == 0:
        print("[error] no unittest directories were discovered", file=sys.stderr)
        return 1

    print(f"[ok] completed unittest discovery across {ran} test directories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
