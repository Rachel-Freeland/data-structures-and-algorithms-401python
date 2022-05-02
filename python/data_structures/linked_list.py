from dataclasses import dataclass


class Node:
    '''This class creates the individual nodes linked in a LinkedList'''
    def __init__(self, data, next = "None"):
        self.data = data
        self.next = next

class LinkedList:
    """
    This class creates and initializes a LinkedList. It also includes some of
    the more common methods associated with working with a LinkedList
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        pass

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
