import pytest

from pycausalwhy.dag import Node

@pytest.mark.unit
def test_node_1():
    """Test Node()
    """
    node = Node(name="A", x=1, y=1)

    assert node.name == "A"
    assert node.pos.x == 1
    assert node.pos.y == 1

@pytest.mark.unit
def test_node_2():
    """Test Node()
    """
    node = Node(name="B", x=1, y=1.4)

    assert node.name == "B"
    assert node.pos.x == 1
    assert node.pos.y == 1.4

@pytest.mark.unit
def test_node_3():
    """Test Node()
    """
    node = Node(name="C", x=7.3, y=1.4)

    assert node.name == "C"
    assert node.pos.x == 7.3
    assert node.pos.y == 1.4
