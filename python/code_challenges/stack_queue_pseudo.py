from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.stack import Stack

class PseudoQueue:

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        """Arguments: value -->
        Inserts the `value` into the PseudoQueue using FIFO"""
        self.inbox.push(value)

    def dequeue(self):
        """Arguments: none -->
        Extracts a value from PseudoQueue using FIFO"""
        while self.outbox.is_empty:
            if self.inbox.is_empty:
                self.outbox.push(self.inbox.pop())
                return self.outbox.pop()
            else:
                raise InvalidOperationError
