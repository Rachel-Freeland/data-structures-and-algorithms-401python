from data_structures.hashtable import Hashtable


def left_join(ht1: Hashtable, ht2: Hashtable):
    """
    Arguments:
        ht1: as a hashtable
        ht2: as a hashtable
    Return:
        a collection of the keys with their respective synonyms and antonyms
    This method left-joins ht2 to ht1.
    """
    collection = []

    for key in ht1.keys():
        joined = [key, ht1.get(key), ht2.get(key)]
        collection.append(joined)
    return collection
