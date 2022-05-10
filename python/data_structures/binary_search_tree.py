from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Creates a subclass of the Binary tree that has additional methods
    """

    def add(self, value):
        """
        Arguments: value ->
        Returns: Nothing
        Adds a new node with that value in the correct location in the binary tree search
        """

        def walk(root, new_node):

            # base case
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
        Arguments: value ->
        Returns: boolean
        Indicates whether a value is in the tree
        """

        def walk(root, value):
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

