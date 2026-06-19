"""Read-only access to the bundled 5e SRD reference data.

The actual content lives in JSON files under ``charsheet/data/`` so that adding
a race, class, or skill is a small, friendly data change — no Python required.
This module just loads those files and hands back plain Python lists of dicts.

We read the files with :mod:`importlib.resources`, which finds them whether the
project is run from a source checkout or installed as a package.
"""

from __future__ import annotations

import json
from importlib import resources
from typing import Any


def _load(filename: str) -> list[dict[str, Any]]:
    """Load and parse one JSON file from the ``charsheet/data`` directory."""
    source = resources.files("charsheet").joinpath("data").joinpath(filename)
    return json.loads(source.read_text(encoding="utf-8"))


def load_races() -> list[dict[str, Any]]:
    """Return the list of playable races from the SRD."""
    return _load("races.json")


def load_classes() -> list[dict[str, Any]]:
    """Return the list of character classes from the SRD."""
    return _load("classes.json")


def load_skills() -> list[dict[str, Any]]:
    """Return the list of skills (each with its governing ability)."""
    return _load("skills.json")
