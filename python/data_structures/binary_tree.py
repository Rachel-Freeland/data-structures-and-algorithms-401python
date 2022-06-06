class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        pass


class BinaryTree:
    """
    Creates a tree class and defines the methods that work with it.
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Traverses the tree from the root in a pre-order fashion.
        Return: A list of values in correct order
        """

        def walk(root, values):  # The root at that moment. root = Node or None. Recursive Fx
            # Every recursive fx needs to know when to stop, aka a "base case"
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
        Traverses the tree from the left in an "in-order" fashion.
        Return: A list of values in correct order
        """

        def walk(root, values):  # The root at that moment. root = Node or None. Recursive Fx
            # Every recursive fx needs to know when to stop, aka a "base case"
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
        Traverses the tree from the root in a post-order fashion.
        Return: A list of values in correct order
        """

        def walk(root, values):  # The root at that moment. root = Node or None. Recursive Fx
            # Every recursive fx needs to know when to stop, aka a "base case"
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
        Arguments: none -->
        Returns --> the max value found in the tree
        """
        # Credit here goes to Dwight Lindquist, I couldn't figure out where I was going wrong until I realized that I
        # was trying to re-invent the wheel so-to-speak. His approach made way more sense to me than the approach I was
        # trying to take.

        if self.root:
            values = self.in_order()
            # Set the starting max_value to 0 for a clean slate
            max_value = 0

            for num in values:
                if num > max_value:
                    max_value = num
            return max_value
        else:
            return "The tree is empty"






