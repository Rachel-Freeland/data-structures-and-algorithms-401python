from data_structures.hashtable import Hashtable
import re


def first_repeated_word(text):
    """
    Argument:
        text: as a string
    Return:
        string
    Takes in a string and finds the first word to occur more than once in the string.
    """
    pattern = r"\W+(?!\S*[a-z])|(?<!\S)\W+"
    new_string = re.sub(pattern, " ", text).lower().split()
    print(new_string)
    dic = {}

    for word in new_string:
        if word not in dic:
            dic[word] = word
        else:
            return word

    return None
