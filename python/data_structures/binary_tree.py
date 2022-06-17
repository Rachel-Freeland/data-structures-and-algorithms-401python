from data_structures.queue import Queue


class Node:
    """
    Attribute:
        self.left: refers to the left child node, if there is one
        self.right: refers to the right child node, if there is one
        self.value: the data stored in the node
    An object that has properties for the value stored in the Node of a tree.
    """

    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        pass


class BinaryTree:
    """
    Attribute:
        self.root: the uppermost node in the tree
    Methods:
        pre_order()
        in_order()
        post_order()
        find_maximum_value()
        add(value)
    A node-based data structure where each node can have links to multiple nodes. The tree has a 'root' node that is
    located at the top level of the tree.
    """

    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)

    def pre_order(self):
        """
        Argument:
            self
        Attribute:
            BigO Time Complexity: O(n)
        Return:
            list of values in correct order
        Traverses the tree from the root in a "pre-order" fashion.
        """

        def walk(root, values):
            """
            Argument:
                root: at that moment in time
                values: the values to be carried
            Return:
                nothing
            This method takes in the root at that moment in time and recursively traverses the tree until the
            "base case" is reached.
            """
            if not root:
                return
            # Task 1: Do something
            values.append(root.value)
            # Task 2: Go left
            walk(root.left, values)
            # Task 3: Go right
            walk(root.right, values)
            pass

        ordered_values = []
        walk(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        Argument:
            self
        Attribute:
            BigO Time Complexity: O(n)
        Return:
            A list of values in correct order
        Traverses the tree from the left in an "in-order" fashion.
        """

        def walk(root, values):
            """
            Argument:
                root: at that moment in time
                values: the values to be carried
            Return:
                nothing
            This method takes in the root at that moment in time and recursively traverses the tree until the
            "base case" is reached.
            """
            if not root:
                return

            # Task 1: Go left
            walk(root.left, values)

            # Task 2: Do something
            values.append(root.value)

            # Task 3: Go right
            walk(root.right, values)

        ordered_values = []
        walk(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        """
        Argument:
            self
        Attribute:
            BigO Time Complexity: O(n)
        Return: A list of values in correct order
        Traverses the tree from the root in a "post-order" fashion.
        """

        def walk(root, values):
            """
            Argument:
                root: at that moment in time
                values: the values to be carried
            Return:
                nothing
            This method takes in the root at that moment in time and recursively traverses the tree until the
            "base case" is reached.
            """
            if not root:
                return
            # Task 1: Go left
            walk(root.left, values)

            # Task 2: Go right
            walk(root.right, values)

            # Task 3: Do something
            values.append(root.value)

        ordered_values = []
        walk(self.root, ordered_values)

        return ordered_values

    def find_maximum_value(self):
        """
        Argument:
            self
        Attribute:
            BigO Time Complexity: O(n)
        Return:
            the max value found in the tree
        Traverses the tree in an "in-order" fashion and returns the largest value found in the tree
        """
        # Credit here goes to Dwight Lindquist, I couldn't figure out where I was going wrong until I realized that I
        # was trying to re-invent the wheel so-to-speak. His approach made way more sense to me than the approach I was
        # trying to take.

        if self.root:
            values = self.in_order()
            max_value = 0

            for num in values:
                if num > max_value:
                    max_value = num
            return max_value
        else:
            return "The tree is empty"

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            front = queue.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                queue.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                queue.enqueue(front.right)
