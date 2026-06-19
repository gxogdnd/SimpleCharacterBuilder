"""Tests for the bundled SRD reference data and its loader.

As well as checking the loader works, these tests guard the *data* itself: if
someone adds a race or skill with a typo'd ability name, a test fails. That is
a friendly safety net for data-only contributions.
"""

from charsheet import reference, rules


def test_skills_load_and_use_known_abilities() -> None:
    skills = reference.load_skills()
    assert len(skills) == 18
    for skill in skills:
        assert skill["name"]
        assert skill["ability"] in rules.ABILITIES


def test_classes_load_with_sensible_fields() -> None:
    classes = reference.load_classes()
    assert len(classes) == 12
    for char_class in classes:
        assert char_class["hit_die"] in {6, 8, 10, 12}
        assert char_class["primary_abilities"]
        for ability in char_class["primary_abilities"]:
            assert ability in rules.ABILITIES
        # Every class has exactly two saving-throw proficiencies in 5e.
        saves = char_class["saving_throw_proficiencies"]
        assert len(saves) == 2
        for ability in saves:
            assert ability in rules.ABILITIES


def test_races_load_with_valid_ability_increases() -> None:
    races = reference.load_races()
    assert len(races) == 9
    for race in races:
        assert race["name"]
        assert race["size"] in {"Small", "Medium"}
        assert isinstance(race["speed"], int)
        for ability, bonus in race["ability_score_increases"].items():
            assert ability in rules.ABILITIES
            assert isinstance(bonus, int)


def test_class_names_are_unique() -> None:
    names = [c["name"] for c in reference.load_classes()]
    assert len(names) == len(set(names))
