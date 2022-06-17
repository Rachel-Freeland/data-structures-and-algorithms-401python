from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Method:
        add()
        contains()
    Creates a subclass of the Binary tree that has additional methods and abides by certain rules:
    - Each node must have one "left" and one "right" child.
    - A node's left descendants can only contain values that are less than the node itself
    - A node's right descendants can only contain values that are greater than the node itself
    """

    def add(self, value):
        """
        Argument:
            value
        Return:
            Nothing
        Adds a new node with that value in the correct location in the binary tree search
        """

        def walk(root, new_node):
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

            if new_node.value < root.value:
                # go left
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node
                pass

        node_to_add = Node(value)  # local variable outside walk fx

        if not self.root:
            self.root = node_to_add
            return

        walk(self.root, node_to_add)

    def contains(self, value):
        """
        Argument:
            value
        Attribute:
            BigO Time Complexity: O(n)
        Return:
            boolean
        Indicates whether a value is in the tree
        """

        def walk(root, value):
            """
            Argument:
                root: at that moment in time
                values: the values to be carried
            Return:
                nothing
            This method takes in the root at that moment in time and recursively traverses the tree until the
            "base case" is reached.
            """
            if root is None:
                return False

            if root.value == value:
                return True
            elif root.value > value:
                return walk(root.left, value)
            elif root.value < value:
                return walk(root.right, value)
            else:
                return False

        return walk(self.root, value)

