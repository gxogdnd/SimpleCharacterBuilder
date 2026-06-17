"""Command-line entry point for SimpleCharacterBuilder.

Right now this only knows how to report its version. The rest of the commands
(``create``, ``show``, ``roll-abilities`` ...) are built up through the seeded
issues in the learning path — that is the whole point of the project.
"""

import click

from charsheet import __version__


@click.group()
@click.version_option(__version__, prog_name="charsheet")
def main() -> None:
    """Build and manage D&D 5e character sheets from the command line."""


if __name__ == "__main__":
    main()
