"""Saving and loading characters as JSON files.

We keep all the file handling in one place so the rest of the code never has to
think about paths or the ``json`` module. A character is stored as a small,
human-readable JSON file you can open and inspect.
"""

from __future__ import annotations

import json
from pathlib import Path

from charsheet.models import Character


def save_character(character: Character, path: str | Path) -> Path:
    """Write ``character`` to ``path`` as formatted JSON and return the path."""
    path = Path(path)
    path.write_text(
        json.dumps(character.to_dict(), indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def load_character(path: str | Path) -> Character:
    """Read a character previously written by :func:`save_character`."""
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    return Character.from_dict(data)
