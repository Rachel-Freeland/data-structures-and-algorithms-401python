from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Queue:
    """
    Creates a Queue class that has a front property. It creates an empty Queue when instantiated.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Arguments: a value  -->
        Adds a new node with that value to the `back` of the queue with an
        O(1) Time performance."""

        if self.front is None:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next_ = Node(value)
            self.rear = self.rear.next_

    def dequeue(self):
        """
        Arguments: none -->
        Returns: value of the node that was removed from the front of the queue -->
        Removes and returns the value from the node at the front of the queue. Will raise an exception when called
        on an empty queue
        """

        if not self.front:
            raise InvalidOperationError

        old_front = self.front
        self.front = self.front.next_
        old_front.next_ = None
        return old_front.value

    def peek(self):
        """
        Argument(s): none -->
        Returns: value of the node located at the front of the queue -->
        Will raise an exception when called on an empty queue.
        """

        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        """
        Arguments: none -->
        Returns: a boolean -->
        Takes 0 arguments and returns a bool indicating whether the queue is empty.
        """

        if self.front is None:
            return True
        else:
            return False
