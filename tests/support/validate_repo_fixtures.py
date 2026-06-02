from __future__ import annotations

import builtins
import importlib.util
import json
import re
import shutil
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from jsonschema import Draft202012Validator

from scripts import release_check, validate_repo, validation_lanes
from scripts.validators import source_contracts


REPO_ROOT = Path(__file__).resolve().parents[2]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_required_section_body(
    headings: tuple[str, ...] = validate_repo.REQUIRED_SECTIONS,
) -> str:
    chunks: list[str] = []
    for heading in headings:
        if heading == "Risks":
            markdown = """### Failure modes

- misses the main failure

### Negative effects

- adds avoidable friction

### Misuse patterns

- expands the pattern casually

### Detection signals

- drift shows up in review

### Mitigations

- narrow the contract again"""
        else:
            markdown = f"Bounded content for {heading.lower()}."
        chunks.append(f"## {heading}\n\n{markdown}")
    return "\n\n".join(chunks)
