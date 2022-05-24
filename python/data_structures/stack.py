from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Stack:
    """
    Creates a Stack that has a top property and creates an empty Stack
    when instantiated.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Argument(s): value -->
        Return: nothing -->
        This method takes in a value as an argument and adds a new node with
        that value to the 'top' of the stack with an O(1) Time performance."""
        self.top = Node(value, self.top)

    def pop(self):
        """
        Argument(s): none -->
        Returns: The value from the top of the stack -->
        This method takes 0 arguments and removes and returns the node from the
        top of the stack. If the stack is empty, an exception will be raised."""
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:  # Thanks to Eden Brekke for helping me to figure out where I was going wrong.
            old_top = self.top
            self.top = self.top.next_
            old_top.next_ = None
            return old_top.value

    def peek(self):
        """
        Argument(s): none -->
        Returns: the value at the top of the stack -->
        This method takes 0 arguments and returns the value of the node located
        at the top of the stack. An exception is raised when called on an empty stack."""
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        """
        Argument(s): none -->
        Returns: a boolean value -->
        This method takes 0 arguments and returns a boolean value denoting whether a stack is empty"""
        if not self.top:
            return True
        else:
            return False
