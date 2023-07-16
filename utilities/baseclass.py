import pytest


@pytest.mark.usefixtures("setup", "eyes")
class BaseClass:
    pass
