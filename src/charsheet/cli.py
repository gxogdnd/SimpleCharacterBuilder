"""Command-line entry point for SimpleCharacterBuilder.

Built with `click <https://click.palletsprojects.com/>`_. Each command is a
small function decorated with ``@main.command()``. Adding a new command is a
great first contribution — copy the shape of ``show`` and go from there.
"""

from __future__ import annotations

import click

from charsheet import __version__, rules
from charsheet.models import AbilityScores, Character
from charsheet.storage import load_character, save_character


@click.group()
@click.version_option(__version__, prog_name="charsheet")
def main() -> None:
    """Build and manage D&D 5e character sheets from the command line."""


def _ability_options(command):
    """Attach a ``--strength``/``--dexterity``/... option for each ability.

    Defined once as a decorator factory so we don't repeat six near-identical
    option definitions by hand.
    """
    for ability in reversed(rules.ABILITIES):
        command = click.option(
            f"--{ability}",
            type=click.IntRange(1, 30),
            default=10,
            show_default=True,
            help=f"{ability.capitalize()} score.",
        )(command)
    return command


@main.command()
@click.option("--name", required=True, help="The character's name.")
@click.option(
    "--race",
    default="Human",
    show_default=True,
    help="The character's race.",
)
@click.option(
    "--class",
    "char_class",
    default="Fighter",
    show_default=True,
    help="The character's class.",
)
@click.option(
    "--level",
    type=click.IntRange(min=1),
    default=1,
    show_default=True,
    help="The character's level.",
)
@_ability_options
@click.option(
    "--output",
    "-o",
    type=click.Path(dir_okay=False, writable=True),
    help="Where to save the character file. Defaults to <name>.character.json.",
)
def create(
    name: str,
    race: str,
    char_class: str,
    level: int,
    output: str | None,
    **ability_scores: int,
) -> None:
    """Create a new character and save it to a JSON file."""
    character = Character(
        name=name,
        race=race,
        char_class=char_class,
        level=level,
        abilities=AbilityScores(**ability_scores),
    )
    destination = output or f"{name.lower().replace(' ', '_')}.character.json"
    path = save_character(character, destination)
    click.echo(f"Created {character.name} and saved to {path}")


@main.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def show(path: str) -> None:
    """Display the character stored in PATH."""
    character = load_character(path)
    _print_character(character)


def _print_character(character: Character) -> None:
    """Print a simple, readable character sheet to the terminal."""
    click.echo(f"{character.name}")
    click.echo(f"Level {character.level} {character.race} {character.char_class}")
    click.echo("")
    click.echo("Ability Scores")
    click.echo("--------------")
    for ability in rules.ABILITIES:
        score = getattr(character.abilities, ability)
        modifier = character.abilities.modifier(ability)
        sign = "+" if modifier >= 0 else ""
        abbreviation = rules.ABILITY_ABBREVIATIONS[ability]
        click.echo(f"{abbreviation}  {score:>2}  ({sign}{modifier})")


if __name__ == "__main__":
    main()
