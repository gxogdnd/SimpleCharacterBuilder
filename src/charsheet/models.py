"""The data model for a character.

We use :mod:`dataclasses`, which give us a tidy place to hold data plus free
``__init__`` and ``__repr__`` methods. The classes here also know how to turn
themselves into plain dictionaries (and back), which is all the save/load code
in :mod:`charsheet.storage` needs.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from charsheet import rules

#: Ability scores must fall within this inclusive range in the 5e SRD.
MIN_ABILITY_SCORE = 1
MAX_ABILITY_SCORE = 30


@dataclass
class AbilityScores:
    """The six ability scores, defaulting to the "average" value of 10."""

    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10

    def __post_init__(self) -> None:
        for ability in rules.ABILITIES:
            score = getattr(self, ability)
            if not isinstance(score, int):
                raise TypeError(f"{ability} score must be an int, got {score!r}")
            if not MIN_ABILITY_SCORE <= score <= MAX_ABILITY_SCORE:
                raise ValueError(
                    f"{ability} score {score} is outside the allowed range "
                    f"{MIN_ABILITY_SCORE}-{MAX_ABILITY_SCORE}"
                )

    def modifier(self, ability: str) -> int:
        """Return the modifier for the named ability (e.g. ``"dexterity"``)."""
        if ability not in rules.ABILITIES:
            raise ValueError(f"unknown ability: {ability!r}")
        return rules.ability_modifier(getattr(self, ability))

    def to_dict(self) -> dict[str, int]:
        return {ability: getattr(self, ability) for ability in rules.ABILITIES}

    @classmethod
    def from_dict(cls, data: dict[str, int]) -> AbilityScores:
        return cls(**{ability: data[ability] for ability in rules.ABILITIES})


@dataclass
class Character:
    """A single D&D character.

    Race and class are kept as free-form strings for now. Validating them
    against the official SRD lists is a planned contributor exercise.
    """

    name: str
    race: str = "Human"
    char_class: str = "Fighter"
    level: int = 1
    abilities: AbilityScores = field(default_factory=AbilityScores)

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("character name must not be empty")
        if self.level < 1:
            raise ValueError(f"level must be at least 1, got {self.level}")

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary describing the character."""
        return {
            "name": self.name,
            "race": self.race,
            "char_class": self.char_class,
            "level": self.level,
            "abilities": self.abilities.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> Character:
        """Rebuild a :class:`Character` from a dictionary produced by ``to_dict``."""
        return cls(
            name=data["name"],
            race=data.get("race", "Human"),
            char_class=data.get("char_class", "Fighter"),
            level=data.get("level", 1),
            abilities=AbilityScores.from_dict(data["abilities"]),
        )
