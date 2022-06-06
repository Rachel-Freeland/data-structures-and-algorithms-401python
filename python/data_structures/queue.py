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
<<<<<<< HEAD
        if self.rear:  # if a self.rear exists then,
=======
        
        if self.rear: # if a self.rear exists then,
>>>>>>> 4e8d246a4c0dfd9210e06b5c84ee0e84221695c8
            self.rear.next = Node(value, self.rear)  # add a node with the new value to the spot behind the current
            # self.rear
        else:
            self.rear = Node(value, self.rear)  # if there is no self. rear, create one and label it as the rear
            self.front = self.rear

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
        self.front = old_front.next_
        old_front.next = None
        return old_front.value

    def peek(self):
        """
<<<<<<< HEAD
        Arguments: none -->
        Returns: The value of the node located at the front of the queue.
        Will raise an exception when called on an empty queue.
        """

=======
        Argument(s): none -->
        Returns: value of the node located at the front of the queue -->
        Will raise an exception when called on an empty queue.
        """
        
>>>>>>> 4e8d246a4c0dfd9210e06b5c84ee0e84221695c8
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        """
        Arguments: none -->
        Returns: a boolean -->
        Takes 0 arguments and returns a bool indicating whether the queue is empty.
        """
<<<<<<< HEAD

=======
        
>>>>>>> 4e8d246a4c0dfd9210e06b5c84ee0e84221695c8
        if not self.front:
            return not self.front
