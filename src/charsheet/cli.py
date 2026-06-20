"""Command-line entry point for SimpleCharacterBuilder.

Built with `click <https://click.palletsprojects.com/>`_. Each command is a
small function decorated with ``@main.command()``. Adding a new command is a
great first contribution — copy the shape of ``show`` and go from there.

Most commands delegate their real work to a plain ``_helper`` function. That way
the interactive ``menu`` can reuse exactly the same behaviour as the individual
commands, with no duplication.
"""

from __future__ import annotations

import click

from charsheet import __version__, reference, rules
from charsheet.models import AbilityScores, Character
from charsheet.storage import load_character, save_character


def _abbr(ability: str) -> str:
    """Short, upper-case form of an ability name, e.g. ``"dexterity"`` -> ``"DEX"``."""
    return rules.ABILITY_ABBREVIATIONS[ability]


def _default_character_path(name: str) -> str:
    """The default file name for a character, derived from their name."""
    return f"{name.lower().replace(' ', '_')}.character.json"


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
    destination = output or _default_character_path(name)
    path = save_character(character, destination)
    click.echo(f"Created {character.name} and saved to {path}")


@main.command()
@click.option(
    "--output",
    "-o",
    type=click.Path(dir_okay=False, writable=True),
    help="Where to save the character file. Defaults to <name>.character.json.",
)
def new(output: str | None) -> None:
    """Create a character interactively, one question at a time.

    A friendlier alternative to ``create`` and its many flags: you'll be asked
    for each value in turn, choosing race and class from the SRD lists. Press
    Enter to accept the value shown in [brackets].
    """
    _interactive_new(output)


def _interactive_new(output: str | None = None) -> None:
    """Prompt for each field and save a new character (shared by ``new``/``menu``)."""
    click.echo("Let's build a character. Press Enter to accept each [default].\n")

    name = click.prompt("Name")

    race_names = [r["name"] for r in reference.load_races()]
    race = click.prompt(
        "Race",
        type=click.Choice(race_names, case_sensitive=False),
        default="Human",
        show_choices=True,
    )

    class_names = [c["name"] for c in reference.load_classes()]
    char_class = click.prompt(
        "Class",
        type=click.Choice(class_names, case_sensitive=False),
        default="Fighter",
        show_choices=True,
    )

    level = click.prompt("Level", type=click.IntRange(min=1), default=1)

    click.echo("\nAbility scores (1-30):")
    scores = {
        ability: click.prompt(
            f"  {ability.capitalize()}",
            type=click.IntRange(1, 30),
            default=10,
        )
        for ability in rules.ABILITIES
    }

    character = Character(
        name=name,
        race=race,
        char_class=char_class,
        level=level,
        abilities=AbilityScores(**scores),
    )
    destination = output or _default_character_path(name)
    path = save_character(character, destination)
    click.echo(f"\nCreated {character.name} and saved to {path}\n")
    _print_character(character)


@main.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def show(path: str) -> None:
    """Display the character stored in PATH."""
    _print_character(load_character(path))


def _interactive_show() -> None:
    """Ask for a character file and display it (shared by ``menu``)."""
    path = click.prompt(
        "Path to character file",
        type=click.Path(exists=True, dir_okay=False),
    )
    _print_character(load_character(path))


@main.command()
def races() -> None:
    """List the playable races from the SRD."""
    _list_races()


def _list_races() -> None:
    for race in reference.load_races():
        increases = ", ".join(
            f"{_abbr(ability)} +{bonus}"
            for ability, bonus in race["ability_score_increases"].items()
        )
        click.echo(f"{race['name']} — {increases}")


@main.command()
def classes() -> None:
    """List the character classes from the SRD."""
    _list_classes()


def _list_classes() -> None:
    for char_class in reference.load_classes():
        saves = ", ".join(_abbr(a) for a in char_class["saving_throw_proficiencies"])
        click.echo(f"{char_class['name']} (d{char_class['hit_die']}) — saves: {saves}")


@main.command()
def skills() -> None:
    """List the skills and the ability each one uses."""
    _list_skills()


def _list_skills() -> None:
    for skill in reference.load_skills():
        click.echo(f"{skill['name']} ({_abbr(skill['ability'])})")


@main.command()
def menu() -> None:
    """Launch an interactive menu — no flags needed.

    Pick an action by number; the menu loops until you choose Quit.
    """
    # Each entry maps a choice to a (label, handler) pair. A handler of None
    # means "quit". The handlers are the same helpers the other commands use.
    actions: dict[str, tuple[str, object]] = {
        "1": ("Create a new character", _interactive_new),
        "2": ("Show a saved character", _interactive_show),
        "3": ("Browse races", _list_races),
        "4": ("Browse classes", _list_classes),
        "5": ("Browse skills", _list_skills),
        "6": ("Quit", None),
    }

    while True:
        click.echo("\n=== SimpleCharacterBuilder ===")
        for key, (label, _handler) in actions.items():
            click.echo(f"  {key}) {label}")

        choice = click.prompt(
            "Choose",
            type=click.Choice(list(actions)),
            show_choices=True,
        )
        label, handler = actions[choice]
        if handler is None:
            click.echo("Goodbye! 🎲")
            break
        click.echo("")
        handler()


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
