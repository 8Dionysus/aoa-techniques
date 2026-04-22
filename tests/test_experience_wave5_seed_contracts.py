from __future__ import annotations

import copy
from datetime import datetime, timedelta
import json
from pathlib import Path
import re
import unittest

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
ESCAPE_VALUE = "__wave5_not_allowed__"
FORMAT_CHECKER = FormatChecker()
RFC3339_DATETIME = re.compile(
    r"^(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})"
    r"[Tt](?P<hour>[0-9]{2}):(?P<minute>[0-9]{2}):(?P<second>[0-9]{2})"
    r"(?:\.[0-9]+)?(?P<zone>[Zz]|(?P<offset_sign>[+-])(?P<offset_hour>[0-9]{2}):(?P<offset_minute>[0-9]{2}))$"
)
RFC3339_UTC_LEAP_SECOND_DATES = frozenset(
    (
        (1972, 6, 30),
        (1972, 12, 31),
        (1973, 12, 31),
        (1974, 12, 31),
        (1975, 12, 31),
        (1976, 12, 31),
        (1977, 12, 31),
        (1978, 12, 31),
        (1979, 12, 31),
        (1981, 6, 30),
        (1982, 6, 30),
        (1983, 6, 30),
        (1985, 6, 30),
        (1987, 12, 31),
        (1989, 12, 31),
        (1990, 12, 31),
        (1992, 6, 30),
        (1993, 6, 30),
        (1994, 6, 30),
        (1995, 12, 31),
        (1997, 6, 30),
        (1998, 12, 31),
        (2005, 12, 31),
        (2008, 12, 31),
        (2012, 6, 30),
        (2015, 6, 30),
        (2016, 12, 31),
    )
)


def is_rfc3339_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_rfc3339_date(year: int, month: int, day: int) -> bool:
    month_lengths = [31, 29 if is_rfc3339_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= month <= 12 and 1 <= day <= month_lengths[month - 1]


def is_rfc3339_leap_second(match: re.Match[str], year: int, month: int, day: int, hour: int, minute: int) -> bool:
    if minute != 59 or year == 0:
        return False
    if match["zone"] in ("Z", "z"):
        return hour == 23 and (year, month, day) in RFC3339_UTC_LEAP_SECOND_DATES
    offset_minutes = int(match["offset_hour"]) * 60 + int(match["offset_minute"])
    if match["offset_sign"] == "-":
        offset_minutes = -offset_minutes
    try:
        local_second = datetime(year, month, day, hour, minute, 59)
    except ValueError:
        return False
    utc_second = local_second - timedelta(minutes=offset_minutes)
    return (
        utc_second.hour == 23
        and utc_second.minute == 59
        and (utc_second.year, utc_second.month, utc_second.day) in RFC3339_UTC_LEAP_SECOND_DATES
    )


@FORMAT_CHECKER.checks("date-time")
def is_rfc3339_datetime(value: object) -> bool:
    if not isinstance(value, str):
        return True
    match = RFC3339_DATETIME.fullmatch(value)
    if not match:
        return False
    if not is_rfc3339_date(int(match["year"]), int(match["month"]), int(match["day"])):
        return False
    hour = int(match["hour"])
    minute = int(match["minute"])
    second = int(match["second"])
    if hour > 23 or minute > 59 or second > 60:
        return False
    if second == 60 and not is_rfc3339_leap_second(match, int(match["year"]), int(match["month"]), int(match["day"]), hour, minute):
        return False
    if match["offset_hour"] is not None:
        if int(match["offset_hour"]) > 23 or int(match["offset_minute"]) > 59:
            return False
    return True

WAVE5_CONTRACTS = (
    ('handoff_compression_technique_note_v1', 'handoff_compression_technique_note_v1.json'),
    ('installation_technique_note_v1', 'installation_technique_note_v1.json'),
    ('scope_boundary_technique_note_v1', 'scope_boundary_technique_note_v1.json'),
    ('service_clarity_technique_note_v1', 'service_clarity_technique_note_v1.json'),
    ('sovereign_release_technique_note_v1', 'sovereign_release_technique_note_v1.json'),
)


def load_contract(stem: str, schema_file: str) -> tuple[dict[str, object], dict[str, object]]:
    schema_path = ROOT / "schemas" / schema_file
    example_path = ROOT / "examples" / f"{stem}.example.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    example = json.loads(example_path.read_text(encoding="utf-8"))
    return schema, example


def validation_errors(schema: dict[str, object], value: object) -> list[object]:
    return sorted(
        Draft202012Validator(schema, format_checker=FORMAT_CHECKER).iter_errors(value),
        key=lambda error: list(error.path),
    )


def effective_schema(schema: object, value: object) -> object:
    if not isinstance(schema, dict):
        return schema
    variants = schema.get("oneOf")
    if isinstance(variants, list):
        for variant in variants:
            if isinstance(variant, dict) and not validation_errors(variant, value):
                return variant
    return schema


def schema_properties(schema: object, value: object | None = None) -> dict[str, object]:
    if value is not None:
        schema = effective_schema(schema, value)
    if not isinstance(schema, dict):
        return {}
    props = schema.get("properties")
    return props if isinstance(props, dict) else {}


def child_schema(schema: object, value: object, key: object) -> object:
    schema = effective_schema(schema, value)
    if isinstance(key, str) and isinstance(value, dict):
        return schema_properties(schema, value).get(key, {})
    if isinstance(key, int) and isinstance(value, list) and isinstance(schema, dict):
        return effective_schema(schema.get("items", {}), value[key])
    return {}


def wrong_type_value(value: object) -> object:
    if isinstance(value, bool):
        return "not-a-boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "not-an-integer"
    if isinstance(value, float):
        return "not-a-number"
    if isinstance(value, str):
        return 12345
    if isinstance(value, list):
        return {"not": "an array"}
    if isinstance(value, dict):
        return "not-an-object"
    return "not-null"


def escape_value(value: object) -> object:
    if isinstance(value, bool):
        return not value
    if isinstance(value, int) and not isinstance(value, bool):
        return value + 1
    if isinstance(value, float):
        return value + 1.0
    if isinstance(value, str):
        return f"{value}{ESCAPE_VALUE}"
    return ESCAPE_VALUE


def get_path(value: object, path: tuple[object, ...]) -> object:
    cursor = value
    for part in path:
        if isinstance(part, int):
            assert isinstance(cursor, list)
            cursor = cursor[part]
        else:
            assert isinstance(cursor, dict)
            cursor = cursor[part]
    return cursor


def set_path(value: object, path: tuple[object, ...], replacement: object) -> None:
    cursor = value
    for part in path[:-1]:
        if isinstance(part, int):
            assert isinstance(cursor, list)
            cursor = cursor[part]
        else:
            assert isinstance(cursor, dict)
            cursor = cursor[part]
    last = path[-1]
    if isinstance(last, int):
        assert isinstance(cursor, list)
        cursor[last] = replacement
    else:
        assert isinstance(cursor, dict)
        cursor[last] = replacement


def delete_path(value: object, path: tuple[object, ...]) -> None:
    cursor = value
    for part in path[:-1]:
        if isinstance(part, int):
            assert isinstance(cursor, list)
            cursor = cursor[part]
        else:
            assert isinstance(cursor, dict)
            cursor = cursor[part]
    last = path[-1]
    if isinstance(last, int):
        assert isinstance(cursor, list)
        del cursor[last]
    else:
        assert isinstance(cursor, dict)
        del cursor[last]


def walk_values(value: object, path: tuple[object, ...] = ()) -> list[tuple[tuple[object, ...], object]]:
    found: list[tuple[tuple[object, ...], object]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = (*path, key)
            found.append((child_path, child))
            found.extend(walk_values(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_path = (*path, index)
            found.append((child_path, child))
            found.extend(walk_values(child, child_path))
    return found


def object_paths(value: object, path: tuple[object, ...] = ()) -> list[tuple[object, ...]]:
    found: list[tuple[object, ...]] = []
    if isinstance(value, dict):
        found.append(path)
        for key, child in value.items():
            found.extend(object_paths(child, (*path, key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(object_paths(child, (*path, index)))
    return found


def array_paths(value: object, path: tuple[object, ...] = ()) -> list[tuple[object, ...]]:
    found: list[tuple[object, ...]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            found.extend(array_paths(child, (*path, key)))
    elif isinstance(value, list):
        found.append(path)
        for index, child in enumerate(value):
            found.extend(array_paths(child, (*path, index)))
    return found


def string_paths(value: object, path: tuple[object, ...] = ()) -> list[tuple[object, ...]]:
    found: list[tuple[object, ...]] = []
    if isinstance(value, str):
        found.append(path)
    elif isinstance(value, dict):
        for key, child in value.items():
            found.extend(string_paths(child, (*path, key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(string_paths(child, (*path, index)))
    return found


def schema_for_path(schema: object, example: object, path: tuple[object, ...]) -> object:
    cursor_schema = schema
    cursor_value = example
    for part in path:
        cursor_schema = child_schema(cursor_schema, cursor_value, part)
        if isinstance(part, int):
            assert isinstance(cursor_value, list)
            cursor_value = cursor_value[part]
        else:
            assert isinstance(cursor_value, dict)
            cursor_value = cursor_value[part]
    return effective_schema(cursor_schema, cursor_value)


def required_paths(schema: object, example: object, path: tuple[object, ...] = ()) -> list[tuple[object, ...]]:
    schema = effective_schema(schema, example)
    found: list[tuple[object, ...]] = []
    if isinstance(schema, dict) and schema.get("type") == "object" and isinstance(example, dict):
        required = schema.get("required")
        if isinstance(required, list):
            for key in required:
                if isinstance(key, str) and key in example:
                    found.append((*path, key))
        for key, prop in schema_properties(schema, example).items():
            if key in example:
                found.extend(required_paths(prop, example[key], (*path, key)))
    if isinstance(schema, dict) and schema.get("type") == "array" and isinstance(example, list) and example:
        found.extend(required_paths(schema.get("items"), example[0], (*path, 0)))
    return found


def constrained_paths(schema: object, example: object, keyword: str, path: tuple[object, ...] = ()) -> list[tuple[tuple[object, ...], object]]:
    schema = effective_schema(schema, example)
    found: list[tuple[tuple[object, ...], object]] = []
    if not isinstance(schema, dict):
        return found
    if keyword in schema:
        found.append((path, schema[keyword]))
    if schema.get("type") == "object" and isinstance(example, dict):
        for key, prop in schema_properties(schema, example).items():
            if key in example:
                found.extend(constrained_paths(prop, example[key], keyword, (*path, key)))
    if schema.get("type") == "array" and isinstance(example, list) and example:
        found.extend(constrained_paths(schema.get("items"), example[0], keyword, (*path, 0)))
    return found


class ExperienceWave5SeedContractTests(unittest.TestCase):
    def assert_invalid(self, schema: dict[str, object], value: object, label: str) -> None:
        errors = validation_errors(schema, value)
        self.assertTrue(errors, f"{label} unexpectedly validated")

    def test_experience_wave5_examples_match_schemas(self) -> None:
        self.assertTrue(WAVE5_CONTRACTS)
        missing_pairs: list[str] = []
        for stem, schema_file in WAVE5_CONTRACTS:
            schema_path = ROOT / "schemas" / schema_file
            example_path = ROOT / "examples" / f"{stem}.example.json"
            if not schema_path.exists():
                missing_pairs.append(f"{example_path.relative_to(ROOT)} -> {schema_path.relative_to(ROOT)}")
            if not example_path.exists():
                missing_pairs.append(f"{schema_path.relative_to(ROOT)} -> {example_path.relative_to(ROOT)}")
        self.assertFalse(missing_pairs, "missing wave5 contract pair(s): " + ", ".join(missing_pairs))

        for stem, schema_file in WAVE5_CONTRACTS:
            with self.subTest(stem=stem):
                schema, example = load_contract(stem, schema_file)
                Draft202012Validator.check_schema(schema)
                errors = validation_errors(schema, example)
                self.assertFalse(errors, f"{stem}: {errors[0].message}" if errors else stem)

    def test_experience_wave5_schemas_reject_unknown_fields(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path in object_paths(example):
                with self.subTest(stem=stem, path=path):
                    mutated = copy.deepcopy(example)
                    target = get_path(mutated, path) if path else mutated
                    self.assertIsInstance(target, dict)
                    target["contract_escape"] = "loose-field"
                    self.assert_invalid(schema, mutated, f"{stem} unknown field at {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_wrong_types_for_every_field(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path, value in walk_values(example):
                with self.subTest(stem=stem, path=path):
                    mutated = copy.deepcopy(example)
                    set_path(mutated, path, wrong_type_value(value))
                    self.assert_invalid(schema, mutated, f"{stem} wrong type at {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_missing_required_fields(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path in required_paths(schema, example):
                with self.subTest(stem=stem, path=path):
                    mutated = copy.deepcopy(example)
                    delete_path(mutated, path)
                    self.assert_invalid(schema, mutated, f"{stem} missing required {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_bad_array_items(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path in array_paths(example):
                with self.subTest(stem=stem, path=path):
                    mutated = copy.deepcopy(example)
                    array_value = get_path(mutated, path)
                    self.assertIsInstance(array_value, list)
                    if array_value:
                        array_value[0] = wrong_type_value(array_value[0])
                    else:
                        array_value.append({"not": "a valid array item"})
                    self.assert_invalid(schema, mutated, f"{stem} bad array item at {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_empty_strings(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path in string_paths(example):
                with self.subTest(stem=stem, path=path):
                    mutated = copy.deepcopy(example)
                    set_path(mutated, path, "")
                    self.assert_invalid(schema, mutated, f"{stem} empty string at {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_const_escapes(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path, _constraint in constrained_paths(schema, example, "const"):
                with self.subTest(stem=stem, path=path):
                    value = get_path(example, path)
                    mutated = copy.deepcopy(example)
                    set_path(mutated, path, escape_value(value))
                    self.assert_invalid(schema, mutated, f"{stem} const escape at {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_enum_escapes(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path, _constraint in constrained_paths(schema, example, "enum"):
                with self.subTest(stem=stem, path=path):
                    value = get_path(example, path)
                    mutated = copy.deepcopy(example)
                    set_path(mutated, path, escape_value(value))
                    self.assert_invalid(schema, mutated, f"{stem} enum escape at {path}")
                    exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_bad_datetime_formats(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path, constraint in constrained_paths(schema, example, "format"):
                if constraint != "date-time":
                    continue
                for bad_value in (
                    "not-a-date",
                    "2026-02-30T00:00:00Z",
                    "2026-04-22T24:00:00Z",
                    "2026-04-22T00:00:60Z",
                    "2026-04-22T00:00:00+24:00",
                    "\u0662\u0660\u0662\u0666-04-22T00:00:00Z",
                ):
                    with self.subTest(stem=stem, path=path, value=bad_value):
                        mutated = copy.deepcopy(example)
                        set_path(mutated, path, bad_value)
                        self.assert_invalid(schema, mutated, f"{stem} bad date-time at {path}")
                        exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_accept_rfc3339_datetime_variants(self) -> None:
        exercised = 0
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path, constraint in constrained_paths(schema, example, "format"):
                if constraint != "date-time":
                    continue
                for valid_value in (
                    "2026-04-22t00:00:00.123456789z",
                    "0000-02-29T00:00:00Z",
                    "2016-12-31T23:59:60Z",
                    "2017-01-01T00:59:60+01:00",
                ):
                    with self.subTest(stem=stem, path=path, value=valid_value):
                        mutated = copy.deepcopy(example)
                        set_path(mutated, path, valid_value)
                        errors = validation_errors(schema, mutated)
                        self.assertFalse(errors, f"{stem}: {errors[0].message}" if errors else stem)
                        exercised += 1
        self.assertGreater(exercised, 0)

    def test_experience_wave5_schemas_reject_numeric_bound_escapes(self) -> None:
        for stem, schema_file in WAVE5_CONTRACTS:
            schema, example = load_contract(stem, schema_file)
            for path, value in walk_values(example):
                if not isinstance(value, (int, float)) or isinstance(value, bool):
                    continue
                field_schema = schema_for_path(schema, example, path)
                if not isinstance(field_schema, dict):
                    continue
                if "minimum" in field_schema:
                    with self.subTest(stem=stem, path=path, bound="minimum"):
                        mutated = copy.deepcopy(example)
                        set_path(mutated, path, field_schema["minimum"] - 1)
                        self.assert_invalid(schema, mutated, f"{stem} below minimum at {path}")
                if "maximum" in field_schema:
                    with self.subTest(stem=stem, path=path, bound="maximum"):
                        mutated = copy.deepcopy(example)
                        set_path(mutated, path, field_schema["maximum"] + 1)
                        self.assert_invalid(schema, mutated, f"{stem} above maximum at {path}")
