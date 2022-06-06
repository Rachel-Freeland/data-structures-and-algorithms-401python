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
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                temp_node = self.inbox.pop()
                self.outbox.push(temp_node)
        return self.outbox.pop()

