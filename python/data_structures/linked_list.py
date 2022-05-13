class Node:
    """Creates and initializes each node after the head node for the LinkedList"""

    def __init__(self, value, next="None"):

        self.value = value  # assigns the value of the node
        self.next = next  # assigns the location of the next node


class LinkedList:
    """
    This class creates and initializes a LinkedList. This class also includes methods to work with a linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        """Arguments: None -->
        Returns: A string representation of all values of the linked list"""

        string_representation = ""
        current_node = self.head

        while current_node:
            string_representation += f'\u007b {current_node.value} \u007d -> '
            current_node = current_node.next
        string_representation += "NULL"
        return string_representation

    def insert(self, value):
        """Argument: value -->
        Returns: nothing -->
        Takes in a value and inserts a new node with that value at the head of the list"""
        self.head = Node(value, self.head)

    def includes(self, value):
        """Arguments: value -->
        Returns: boolean -->
        Takes in a value and returns a boolean denoting if the value is present or not in the LinkedList"""
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False


    def append(self, value):
        """Arguments: a new value  -->
        Adds a new node with the given `value` to the end of the list"""
        current_node = self.head

        while current_node:
            if self.head is None:
                self.head = Node(value)
            elif current_node.next is None:
                current_node = Node(value)
            else:
                current_node = current_node.next

    def insert_before(self, node_value, new_value):
        """Arguments: the value to look for and a new value -->
        Adds a new node with the given new value immediately before the first
        node that has the value specified."""
        raise TargetError

    def insert_after(self, node_value, new_value):
        """Arguments: the node_value to look for and a new value -->
        Returns: The list with a new node containing the new_value inserted
        after the given node_value"""
        # new_node = Node(new_value)
        # current_node = self.head
        # if node_value is None:
        #     raise TargetError("Node not found")
        # else:
        #     if current_node.next.value == node_value:
        #         new_node = Node(new_value)
        #         new_node.next = current_node
        raise TargetError


class TargetError(Exception):
    pass

