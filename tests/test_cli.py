"""Tests for the command-line interface.

click ships a ``CliRunner`` that invokes commands in-process and captures their
output, so we can test the CLI without spawning a real subprocess.
"""

from click.testing import CliRunner

from charsheet.cli import main
from charsheet.storage import load_character


def test_create_writes_a_character_file(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "hero.json"

    result = runner.invoke(
        main,
        ["create", "--name", "Hero", "--strength", "16", "--output", str(output)],
    )

    assert result.exit_code == 0
    assert output.exists()
    character = load_character(output)
    assert character.name == "Hero"
    assert character.abilities.strength == 16


def test_show_displays_scores_and_modifiers(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "hero.json"
    runner.invoke(
        main,
        ["create", "--name", "Hero", "--dexterity", "16", "--output", str(output)],
    )

    result = runner.invoke(main, ["show", str(output)])

    assert result.exit_code == 0
    assert "Hero" in result.output
    assert "DEX  16  (+3)" in result.output


def test_new_creates_a_character_from_answers(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "aria.json"
    # Answers in prompt order: name, race, class, level, then STR DEX CON INT WIS CHA.
    answers = "\n".join(
        ["Aria", "Elf", "Wizard", "1", "10", "14", "12", "16", "10", "8"]
    )

    result = runner.invoke(main, ["new", "-o", str(output)], input=answers + "\n")

    assert result.exit_code == 0, result.output
    character = load_character(output)
    assert character.name == "Aria"
    assert character.race == "Elf"
    assert character.char_class == "Wizard"
    assert character.abilities.dexterity == 14
    assert character.abilities.intelligence == 16


def test_new_accepts_defaults_with_blank_answers(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "bob.json"
    # Give a name, then press Enter for race, class, level, and all six abilities.
    answers = "Bob" + "\n" * 10

    result = runner.invoke(main, ["new", "-o", str(output)], input=answers)

    assert result.exit_code == 0, result.output
    character = load_character(output)
    assert character.race == "Human"
    assert character.char_class == "Fighter"
    assert character.level == 1
    assert character.abilities.strength == 10


def test_new_reprompts_on_an_unknown_race(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "x.json"
    # "Goblin" isn't in the SRD list; click should reprompt, so a valid answer
    # follows and the character ends up with the valid race.
    answers = "\n".join(
        ["Grizz", "Goblin", "Dwarf", "Fighter", "1", "10", "10", "10", "10", "10", "10"]
    )

    result = runner.invoke(main, ["new", "-o", str(output)], input=answers + "\n")

    assert result.exit_code == 0, result.output
    assert load_character(output).race == "Dwarf"


def test_races_command_lists_known_races() -> None:
    result = CliRunner().invoke(main, ["races"])
    assert result.exit_code == 0
    assert "Human" in result.output
    assert "Elf" in result.output


def test_classes_command_shows_hit_die() -> None:
    result = CliRunner().invoke(main, ["classes"])
    assert result.exit_code == 0
    assert "Wizard (d6)" in result.output


def test_skills_command_shows_governing_ability() -> None:
    result = CliRunner().invoke(main, ["skills"])
    assert result.exit_code == 0
    assert "Stealth (DEX)" in result.output


def test_create_rejects_an_out_of_range_score(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "x.json"
    result = runner.invoke(
        main,
        ["create", "--name", "Hero", "--strength", "99", "--output", str(output)],
    )
    assert result.exit_code != 0
