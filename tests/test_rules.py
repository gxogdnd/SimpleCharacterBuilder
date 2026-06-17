"""Tests for the pure rules helpers in :mod:`charsheet.rules`.

Note how easy these are to write: the functions take numbers and return
numbers, so each test is just "given this input, expect this output".
"""

import pytest

from charsheet import rules


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (1, -5),
        (8, -1),
        (9, -1),
        (10, 0),
        (11, 0),
        (12, 1),
        (16, 3),
        (20, 5),
    ],
)
def test_ability_modifier(score: int, expected: int) -> None:
    assert rules.ability_modifier(score) == expected


def test_there_are_six_abilities() -> None:
    assert len(rules.ABILITIES) == 6
    assert "strength" in rules.ABILITIES
