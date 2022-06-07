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
        """This method takes in a value as an argument and adds a new node with
        that value to the `top` of the stack with an O(1) Time performance."""
        self.top = Node(value, self.top)

    def pop(self):
        """This method takes 0 arguments and returns the value of the node from the
        top of the stack. If the stack is empty, an exception will be raised."""
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            old_top = self.top
            self.top = self.top.next
            old_top.next = None
            return old_top.value

    def peek(self):
        """
        This method takes 0 arguments and returns the value of the node located
        at the top of the stack. An exception is raised when called on an empty stack.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        """
        This method takes 0 arguments and returns a boolean value denoting whether a stack is empty
        """
        if not self.top:
            return True
        else:
            return False
