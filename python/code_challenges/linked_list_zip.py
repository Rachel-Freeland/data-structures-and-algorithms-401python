from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    """
    Arguments: 2 linked list -->
    Return: A new linked list of both a and b "zipped" together in an alternating fashion. Should list_a run short, it
    will finish appending with list_b and vice versa.
    """
    # set the head of the lists
    list_a = a.head
    list_b = b.head

    # check to make sure that neither list is empty
    if list_a is None:
        return b
    if list_b is None:
        return a

    # create a new container for the newly zipped list to be returned
    new_list = LinkedList()

    # while there is a list_a and a list_b...
    while list_a and list_b:
        new_list.append(list_a.value)  # append the node to the list
        list_a = list_a.next_node  # move the pointer for the list_a
        new_list.append(list_b.value)  # append list b... beginning of alternating sequence
        list_b = list_b.next_node  # move the pointer for the list_b

    # while there is a list_a and not a list_b, finish appending with the remainder of list_a
    while list_a and not list_b:
        new_list.append(list_a.value)
        list_a = list_a.next_node

    # while there is a list_b and not a list_a, finish appending with the remainder of list_b
    while list_b and not list_a:
        new_list.append(list_b.value)
        list_b = list_b.next_node

    return new_list









