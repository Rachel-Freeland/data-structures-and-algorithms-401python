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
        '''Arguments: value  -->
        Adds a new node with the value passed to the \`head\` of the list with an O(1) Time Performance'''
        # method body here
        return

    def includes(self, value):
        '''Arguments: value  -->  Return: Boolean  -->
        Indicates whether the value exists as a Node's value somewhere in the list'''
        # method body here... Returns a boolean
        return

    def to_string(self):
        '''Arguments: None  -->  Return: String  -->
        Returns a string representing all the values in the Linked List'''
        # method body here... Returns a string representing all values in list
        return

    def append(self, new_value):
        '''Arguments: new_value  -->
        Adds a new node with the given \`value\` to the end of the list'''
        pass

    def insert_before(self, value, new_value):
        '''Arguements: value, new_value -->
        Adds a new node with the given new value immediately before the first node that has the specified value'''
        pass

    def insert_after(self, value, new_value):
        '''Arguments: value, new_value -->
        Adds a new node with the given new value immediately after the first node that has the value specified'''
        pass

    def kth_from_end(self, k):
        '''Argument: a number\'k\', as a parameter  -->
        Returns the node's value that is \'k\' places from the tail of the linked list'''
        pass


class TargetError:
    pass
