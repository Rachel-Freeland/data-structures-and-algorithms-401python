class Node:
    """Creates and initializes each node after the head node for the LinkedList"""

    def __init__(self, value, next_="None"):
        self.value = value  # assigns the value of the node
        self.next_ = next_  # assigns the location of the next node


class LinkedList:
    """
    This class creates and initializes a LinkedList. This class also includes methods to work with a linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        """Arguments: None -->
        Returns: A string representation of all values of the linked list"""
        string_rep = ""
        current = self.head

        while current:
            string_rep += f'{{ {current.value} }} -> '
            current = current.next_
        return string_rep + "NULL"

    def insert(self, value):
        """Arguments: value -->
        Inserts a new node with that value at the head of the list"""
        self.head = Node(value, self.head)

    def includes(self, target_value):
        """Arguments: value -->
        Returns: boolean -->
        Takes in a value and returns a boolean denoting if the value is present or not in the LinkedList"""
        current_node = self.head

        while current_node:
            if current_node.value == target_value:
                return True
            current_node = current_node.next_
        return False

    def append(self, value):
        """Arguments: value -->
        Returns: nothing -->
        Adds a new node with the given `value` to the end of the list"""

        new_node = Node(value, None)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next_:
            current = current.next_
        current.next_ = new_node

    def insert_before(self, target, value):
        """Arguments: the value to look for and a new value -->
        Adds a new node with the given new value immediately before the first
        node that has the value specified."""

        if not self.head:
            raise TargetError

        try:
            if self.head.value == target:
                self.insert(value)
                return

            current = self.head
            while current.next_:
                if current.next_.value == target:
                    previous = current.next_
                    current.next_ = Node(value, previous)
                    return
                else:
                    current = current.next_
            else:
                raise TargetError
        except:
            raise TargetError

    def insert_after(self, target, value):
        """Arguments: the node_value to look for and a new value -->
        Returns: The list with a new node containing the new_value inserted
        after the given node_value"""
        if not self.head:
            raise TargetError

        current = self.head
        while current:
            if current.value == target:
                current.next_ = Node(value, current.next_)
                break

            if not current.next_:
                raise TargetError
            else:
                current = current.next_

    def kth_from_end(self, num):
        """
        Argument: num, as an integer -->
        Return: the node's value from the kth place from the tail of the linked list
        """
        length = 0
        current = self.head

        while current is not None:
            # Calculate length of the list
            length += 1
            current = current.next_

        # Check for TargetError situations
        if num < 0 or num > (length -1):
            raise TargetError

        # find the kth value from the tail
        current = self.head
        for i in range(length - num - 1):
            current = current.next_
        return current.value


class TargetError(Exception):
    pass
