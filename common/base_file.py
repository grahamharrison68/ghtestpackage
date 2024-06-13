"""Contains base classes
"""

from icecream import ic

class BaseLearner():
    """Base Learner class
    """

    def __init__(self):
        ic("BaseLearner.init")

    def test(self) -> str:
        """Test method

        Returns:
            str: returns value "test"
        """
        ic("BaseLearner.test")
        return "test"
