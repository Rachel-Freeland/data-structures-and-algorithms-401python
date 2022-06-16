class Node:
    """
    An object that has properties for the value stored in the Node and a pointer to the next Node.

    Attribute:
        value: Data stored in the node
        next_node: Reference to the next node in the linked list
    """

    def __init__(self, value, next_node=None):
        """
        Creates an instance of a Node
        """
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "%s ->" % self.value


class LinkedList:
    """
    A data structure that represents a list of items. The list maintains a reference to the first node, also called
    the head. Each node points to the next node in the list.

    Attribute:
        head: The head node of the list
    Method:
        insert(value)
        includes(value)
        append(value)
        insert_before(target_value, new_value)
        insert_after(target_value, new_value)
        kth_from_end(k)
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        string_rep = ""
        current_node = self.head

        while current_node:
            string_rep += f'{{ {current_node.value} }} -> '
            current_node = current_node.next_node
        return string_rep + "NULL"

    def insert(self, value):
        """
        Parameters:
            value: new value to be added
        Return:
            nothing
        Attribute:
            BigO Time Complexity: O(1)
        Adds a new node with the given value to the "head" of the list.
        """
        self.head = Node(value, self.head)
        self.count += 1

    def includes(self, value):
        """
        Parameters:
            value: value to look for
        Returns:
            bool
        Attribute:
            BigO Time Complexity: O(n)
        Takes in a value and returns a bool indicating if the value exists as a Node's value somewhere within the list.
        """
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def append(self, value):
        """
        Arguments:
            value: new value to be added
        Return:
            nothing
        Attribute:
            BigO Time Complexity: O(n)
        Takes in a new value and adds a new node with the given value to the end of the linked list.
        """
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.count += 1
            return

        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        self.count += 1

    def insert_before(self, target_value, new_value):
        """
        Arguments:
            target_value: the value to look for
            new_value: the new value to be inserted before the target value
        Return:
            nothing
        Attribute:
            BigO Time Complexity: O(n)
        Raises:
            TargetError: if there is no self.head
        Adds the new_value immediately before the first node with the given target_value in a linked list.
        """
        if not self.head:
            raise TargetError

        if self.head.value == target_value:
            self.insert(new_value)
            return

        current_node = self.head
        while current_node.next_node:
            if current_node.next_node.value == target_value:
                previous_node = current_node.next_node
                current_node.next_node = Node(new_value, previous_node)
                self.count += 1
                break
            else:
                current_node = current_node.next_node

    def insert_after(self, target_value, new_value):
        """
        Arguments:
            target_value: the value to look for
            new_value: the new value to be inserted
        Return:
            nothing
        Raises:
            TargetError: if there is no node with the target value and the end of the list is reached OR if there is no self.head
        """
        if not self.head:
            raise TargetError

        current_node = self.head
        while current_node:
            if current_node.value == target_value:
                current_node.next_node = Node(new_value, current_node.next_node)
                self.count += 1
                break

            if not current_node.next_node:
                raise TargetError
            else:
                current_node = current_node.next_node

    def kth_from_end(self, k):
        """
        Arguments:
            k: the k<sup>th</sup> position from the end
        Return:
            value: the Node's value that is located at the position
        """
        # Credit here to be given to Dwight Lindquist
        if k < 0 or k >= self.count:
            raise TargetError
        else:
            current_node = self.head
            position = self.count - k

            for i in range(position - 1):
                current_node = current_node.next_node
            return current_node.value


class TargetError(Exception):
    pass
