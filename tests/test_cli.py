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


def test_create_rejects_an_out_of_range_score(tmp_path) -> None:
    runner = CliRunner()
    output = tmp_path / "x.json"
    result = runner.invoke(
        main,
        ["create", "--name", "Hero", "--strength", "99", "--output", str(output)],
    )
    assert result.exit_code != 0
