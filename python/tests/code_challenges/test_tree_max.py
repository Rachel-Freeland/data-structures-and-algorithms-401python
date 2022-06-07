import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

# threw in an extra test to ensure that this worked with a starting negative number
# and a slightly larger tree with larger values in unexpected places


def test_max_val_two():
    tree = BinaryTree()
    tree.root = Node(-7)
    tree.root.left = Node(-15)
    tree.root.right = Node(30)
    tree.root.right.right = Node(50)
    tree.root.left.left = Node(20)
    tree.root.left.left.left = Node(100)
    actual = tree.find_maximum_value()
    expected = 100

    assert actual == expected
