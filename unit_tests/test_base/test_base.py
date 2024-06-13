import pytest

from ghtestpackage.common import BaseLearner # pylint: disable=wrong-import-position, disable=import-error

@pytest.mark.unit
def test_base():
    """Unit test for the BaseLearner class
    """
    print("test_base")

    base = BaseLearner()
    assert base.test() == "test"
