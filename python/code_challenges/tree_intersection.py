from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1: BinaryTree, tree2: BinaryTree):
    """
    Argument:
        tree1: binary tree

        tree2: binary tree
    Return:
        collection of values found in both trees
    This function takes in 2 trees and returns the values found in both trees.
    """
    intersections = []
    ht = Hashtable()

    for val in tree1.in_order():
        ht.set(str(val), val)

    for val in tree2.in_order():
        if ht.contains(str(val)):
            if val not in intersections:
                intersections.append(val)
    return intersections
