from data_structures.queue import Queue


def breadth_first(tree):
    """
    Argument:
        tree: as a data structure
    Return:
        a collection of tree values
    """
    tree_values = []
    queue = Queue()

    if not tree or not tree.root:
        return tree_values

    queue.enqueue(tree.root)

    while queue.front:
        front = queue.dequeue()
        tree_values.append(front.value)

        if front.left:
            queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

    return tree_values
