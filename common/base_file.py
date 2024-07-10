"""Contains base classes
"""
#from typing import Union, Any
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

# class BaseCollection():
#     """Base Collection class
#     """

#     def __init__(self, items: dict):
#         ic("BaseCollection.init")
#         self.collection = items

#     def __getitem__(self, key: Union[int|str|slice]) -> Any:
#         """Gets an item from Nodes referenced by the key

#             Args:
#                 key (int or str): The key to retrieve - int = literal position, str = named key

#             Raises:
#                 TypeError: Raised if the key is not one of int, str

#             Returns:
#                 Node: The Node object referenced by the key
#             """
#         ic("BaseCollection.__getitem__")

#         if isinstance(key, int):
#             return list(self.collection.items())[key]
#         elif isinstance(key, str):
#             return self.collection[key]
#         elif isinstance(key, slice):
#             # region comments
#             # This section will replicate list slicing on a dictionary.
#             # Remembering that key will contain a slice (e.g. [1:2]) the first line will extract the set of keys that match the slice.
#             # The second line then uses list comprehension to return  a list of the items in the item dictionary where the key matches one of the sliced keys.
#             # endregion
#             sliced_keys = list(self.collection.keys())[key]
#             return [item[1] for item in self.collection.items() if item[0] in sliced_keys]
#         else:
#             raise TypeError(f"Unsupported index type: {type(key)}")

#     def keys(self) -> list:
#         """Returns the keys of the collection

#             Returns:
#                 list: The collection keys
#             """
#         return list(self.collection.keys())

#     def values(self) -> list:
#         """Returns the values of the collection

#             Returns:
#                 list: The collection values
#             """
#         return list(self.collection.values())

#     @property
#     def item_names(self) -> set:
#         """Returns the set of node names

#             Returns:
#                 set: The node names

#             Example:
#                 >>> nodes.node_names
#                 >>> {'W', 'X', 'Y', 'Z1', 'Z2', 'Z3'}
#             """
#         return set(self.collection.keys())
