"""A tiny first test, so the test suite and CI are green from day one.

If you are new here: this file shows the shape of every test in the project —
a function named ``test_*`` that ``assert``s something is true. Run the whole
suite with ``pytest`` from the project root.
"""

from charsheet import __version__


def test_version_is_a_nonempty_string() -> None:
    assert isinstance(__version__, str)
    assert __version__
