from packagenamepy import __version__


def test_version():
    assert __version__ == "unknown" or "dev" in __version__ or "0.1.0" in __version__
    #      ^ conda env will default to "unknown" if not set
    #                                  ^ pixi will default to the default tag in pryproject.toml
    #                                    if not set, it will default to "0.0.1" + "devxxx" on local dev builds
    #                                                          ^ this is the default version on runner
