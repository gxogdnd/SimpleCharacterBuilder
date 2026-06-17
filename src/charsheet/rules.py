"""Pure D&D 5e rules helpers.

Everything in this module is a plain function with no side effects: give it
numbers, get numbers back. That makes these rules very easy to test, which is
exactly why we keep them separate from the data model and the CLI.

Only the most fundamental rule lives here for now — the ability modifier.
Other rules (proficiency bonus, hit points, skill bonuses, ...) are introduced
through the project's issues as learning exercises.
"""

#: The six ability scores every D&D character has, in their conventional order.
ABILITIES: tuple[str, ...] = (
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
)

#: Common short forms, handy for display and for accepting user input.
ABILITY_ABBREVIATIONS: dict[str, str] = {
    "strength": "STR",
    "dexterity": "DEX",
    "constitution": "CON",
    "intelligence": "INT",
    "wisdom": "WIS",
    "charisma": "CHA",
}


def ability_modifier(score: int) -> int:
    """Return the modifier for an ability score.

    In 5e the modifier is ``(score - 10)`` halved and rounded *down*, so a
    score of 10-11 gives +0, 12-13 gives +1, 8-9 gives -1, and so on.

    >>> ability_modifier(10)
    0
    >>> ability_modifier(16)
    3
    >>> ability_modifier(7)
    -2
    """
    # Floor division in Python already rounds toward negative infinity, which
    # is the behaviour we want for negative modifiers too.
    return (score - 10) // 2
