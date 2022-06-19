from data_structures.queue import Queue
from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(tree):
    """
    Argument:
        tree: as a k-ary tree
    Return:
        a *new* k-ary tree
    Returns a new tree with new values for: any number divisible by 3 will now be 'fizz', any number divisible by 5
    will now be 'buzz', and any number divisible by both 3 and 5 will now be 'fizzbuzz'
    """
    new_tree = KaryTree(tree.root)
    queue = Queue()

    if not tree and not tree.root:
        return new_tree

    queue.enqueue(new_tree.root)
    while queue.front:
        node = queue.dequeue()
        new_node = fizz_buzz(node.value)
        for child in node.children:
            queue.enqueue(child)
    return new_tree


def fizz_buzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    else:
        return str(value)
