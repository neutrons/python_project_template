import pytest
from packaging import version as py_version

from packagenamepy import __version__


def test_version():
    assert __version__, "empty version"
    # conda env will default to "unknown" if not set
    # pixi will default to the default tag in pryproject.toml
    if __version__ != "unknown":
        try:
            version = py_version.parse(__version__)
            assert version.major >= 0
            assert version.minor >= 0
        except py_version.InvalidVersion:
            pytest.fail(f"Failed to parse version {__version__}")
