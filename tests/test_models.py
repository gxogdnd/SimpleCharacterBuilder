"""Tests for the data model in :mod:`charsheet.models`."""

import pytest

from charsheet.models import AbilityScores, Character


def test_ability_scores_default_to_ten() -> None:
    scores = AbilityScores()
    assert scores.strength == 10
    assert scores.modifier("strength") == 0


def test_ability_scores_modifier() -> None:
    scores = AbilityScores(dexterity=16)
    assert scores.modifier("dexterity") == 3


def test_ability_scores_reject_out_of_range() -> None:
    with pytest.raises(ValueError):
        AbilityScores(strength=31)


def test_ability_scores_reject_unknown_ability() -> None:
    with pytest.raises(ValueError):
        AbilityScores().modifier("luck")


def test_ability_scores_reject_below_minimum() -> None:
    with pytest.raises(ValueError):
        AbilityScores(strength=0)


@pytest.mark.parametrize("score", [1, 30])
def test_ability_score_boundary_value(score: int) -> None:
    ability_scores = AbilityScores(strength=score)
    assert ability_scores.strength == score


def test_ability_scores_reject_non_integer_value() -> None:
    with pytest.raises(TypeError):
        AbilityScores("twelve")


def test_character_requires_a_name() -> None:
    with pytest.raises(ValueError):
        Character(name="  ")


def test_character_round_trips_through_a_dict() -> None:
    original = Character(
        name="Bruenor",
        race="Dwarf",
        char_class="Fighter",
        level=3,
        abilities=AbilityScores(strength=16, constitution=15),
    )
    restored = Character.from_dict(original.to_dict())
    assert restored == original
