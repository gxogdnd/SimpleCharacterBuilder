"""Tests for saving and loading characters.

``tmp_path`` is a pytest fixture that gives each test its own temporary
directory, so these tests never touch your real files.
"""

from charsheet.models import AbilityScores, Character
from charsheet.storage import load_character, save_character


def test_save_then_load_returns_an_equal_character(tmp_path) -> None:
    character = Character(
        name="Tika",
        race="Human",
        char_class="Rogue",
        level=2,
        abilities=AbilityScores(dexterity=17),
    )
    path = tmp_path / "tika.character.json"

    save_character(character, path)
    loaded = load_character(path)

    assert loaded == character


def test_saved_file_is_human_readable_json(tmp_path) -> None:
    path = save_character(Character(name="Raistlin"), tmp_path / "r.json")
    contents = path.read_text(encoding="utf-8")
    assert '"name": "Raistlin"' in contents
