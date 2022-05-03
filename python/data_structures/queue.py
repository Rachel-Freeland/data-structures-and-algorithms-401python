from xml.dom import InvalidAccessErr
from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node

class Queue:
    """
    Create a Queue class that has a front property. It creates an empty Queue
    when instantiated.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        '''Arguments: value  -->
        Adds a new node with that value to the `back` of the queue with an
        O(1) Time performance.'''
        self.rear = Node(value, self.rear)
        if not self.front:
            self.front = self.rear


    def dequeue(self):
        '''Arguments: none -->
        Removes and returns the value from node at the front of the queue.
        Will raise an exception when called on an empty queue'''
        if not self.front:
            raise InvalidOperationError

        old_front = self.front
        self.front = old_front.next
        old_front.next = None
        return old_front.value

    def peek(self):
        '''Arguments: none -->
        Returns: Value of the node located at the front of the queue.
        Will raise an exception when called on an empty queue.'''
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        '''Arguments: none -->
        Returns: Boolean indicating whether or not the queue is empty.'''
        if not self.front:
            return True
        else:
            return False
