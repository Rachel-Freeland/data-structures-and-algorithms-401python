
from dataclasses import dataclass


class Node:
    def __init__(self, data, next = "None"):
        self.data = data
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        # method body here
        return

    def includes(self, value):
        # method body here... Returns a boolean
        return

    def to_string(self):
        # method body here... Returns a string representing all values in list
        return


class TargetError:
    pass
