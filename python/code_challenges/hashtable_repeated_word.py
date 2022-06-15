from data_structures.hashtable import Hashtable
import re


def first_repeated_word(str):
    """
    Arguments: string -->
    Returns: string -->
    Takes in a string and finds the first word to occur more than once in the string.
    """
    lower = str.lower()
    string_split = lower.split(' ')
    stripped_str = []

    for word in string_split:
        string_ = re.sub(r"[?!,;.-]", " ", word)

        if word in stripped_str:
            return string_
        else:
            stripped_str.append(string_)
