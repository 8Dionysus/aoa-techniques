from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
READINESS_PATH = REPO_ROOT / "generated" / "technique_promotion_readiness.min.json"
PACKET_PATH = REPO_ROOT / (
    "stats/packets/published-promotion-readiness-pass-ratio.reference.json"
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def readiness_census() -> tuple[int, int]:
    records = load_json(READINESS_PATH)["techniques"]
    passed = sum(record["readiness_passed"] is True for record in records)
    return passed, len(records)


def assert_packet_matches_owner_readiness(packet: dict) -> None:
    passed, population_size = readiness_census()

    assert population_size > 0, "owner readiness population must not be empty"
    assert packet["population"]["size"] == population_size
    assert packet["sample"]["size"] == population_size
    assert packet["value"]["numerator"] == passed, (
        "packet numerator must match readiness_passed records"
    )
    assert packet["value"]["denominator"] == population_size
    assert packet["value"]["number"] == passed / population_size
    assert packet["progress"] == {
        "state": "terminal",
        "completed": population_size,
        "total": population_size,
    }


class LocalStatsPortTests(unittest.TestCase):
    def test_reference_ratio_matches_current_owner_readiness_projection(self) -> None:
        assert_packet_matches_owner_readiness(load_json(PACKET_PATH))

    def test_false_readiness_numerator_is_rejected(self) -> None:
        false_packet = deepcopy(load_json(PACKET_PATH))
        passed, population_size = readiness_census()
        false_numerator = (passed + 1) % (population_size + 1)
        false_packet["value"]["numerator"] = false_numerator
        false_packet["value"]["number"] = false_numerator / population_size

        with self.assertRaisesRegex(
            AssertionError,
            "packet numerator must match readiness_passed records",
        ):
            assert_packet_matches_owner_readiness(false_packet)


if __name__ == "__main__":
    unittest.main()
