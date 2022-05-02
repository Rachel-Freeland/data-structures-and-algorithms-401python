from dataclasses import dataclass
import string


class Node:
    '''Creates and initializes each node after the head node for the LinkedList'''
    def __init__(self, value, next = "None"):
        self.value = value #assigns the value of the node
        self.next = next #assigns the location of the next node

class LinkedList:
    """
    This class creates and initializes a LinkedList. This class also includes methods to work with a linked list
    """

    def __init__(self):
        self.head = None


    # Returns a string representation of the LinkedList followed by an appended "NULL" to signal the end of the list
    def __str__(self):
        '''Takes no arguments and returns a string representation of all values of the linked list'''
        string_representation = ""
        current_node = self.head

        while current_node:
            string_representation += f'\u007b {current_node.value} \u007d -> '
            current_node = current_node.next
        string_representation += "NULL"
        return string_representation


    # Inserts a new node with the given value at the beginning of the list
    def insert(self, value):
        '''Takes in a value and inserts a new node with that value at the head of the list'''
        self.head = Node(value, self.head)


    # Determines if a value is included in a LinkedList and returns True if present and False if not in the LinkedList
    def includes(self, value):
        '''Takes in a value and returns a boolean value denoting if the value is present or not in the LinkedList'''
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

class TargetError:
    pass
