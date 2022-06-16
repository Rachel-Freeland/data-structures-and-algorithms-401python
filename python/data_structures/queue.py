from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Queue:
    """
    Creates a Queue class that has a front property. It creates an empty Queue when instantiated.
    Method:
        enqueue(value)
        dequeue()
        peek()
        is_empty()
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Argument:
            value: a new value
        Attribute:
            BigO Time Complexity: O(1)
        Return:
            nothing
        Adds a new node with that value to the `back` of the queue
        """

        if self.front is None:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next_node = Node(value)
            self.rear = self.rear.next_node

    def dequeue(self):
        """
        Argument:
            none
        Attribute:
            BigO Time Complexity: O(1)
        Raises:
            InvalidOperationError: if no node at front of queue
        Return:
            The value of the node that was removed from the front of the queue
        Removes and returns the value from the node at the front of the queue. Will raise an exception when called
        on an empty queue
        """

        if not self.front:
            raise InvalidOperationError

        old_front = self.front
        self.front = self.front.next_node
        old_front.next_node = None
        return old_front.value

    def peek(self):
        """
        Arguments:
            self
        Attribute:
            BigO Time Complexity: O(1)
        Return:
            value of the node located at the front of the queue
        Will raise an exception when called on an empty queue.
        """

        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        """
        Argument:
            self
        Attribute;
            BigO Time Complexity: O(1)
        Return:
            bool
        Indicates if queue is empty.
        """
        return self.front is None
