from data_structures.stack import Stack


class PseudoQueue:

    def __init__(s):
        s.inbox = Stack()
        s.outbox = Stack()

    def enqueue(s, value):
        """Arguments: value -->
        Inserts the `value` into the PseudoQueue using FIFO"""
        s.inbox.push(value)

    def dequeue(s):
        """Arguments: none -->
        Extracts a value from PseudoQueue using FIFO"""
