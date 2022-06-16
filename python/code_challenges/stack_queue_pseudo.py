from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        """
        Argument:
            value
        Attribute:
            BigO Time Complexity: O(1)
        Returns:
            nothing
        Inserts the `value` into the PseudoQueue using FIFO
        """
        self.inbox.push(value)

    def dequeue(self):
        """
        Argument:
            none
        Attribute:
            BigO Time Complexity: O(n)
        Return:
            nothing
        Extracts a value from PseudoQueue using FIFO
        """
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                temp_node = self.inbox.pop()
                self.outbox.push(temp_node)
        return self.outbox.pop()
