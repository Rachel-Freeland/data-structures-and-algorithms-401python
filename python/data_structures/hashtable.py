from data_structures.linked_list import LinkedList


class Hashtable:
    """
    A data structure that uses key/value pairs. Every `Node` or `bucket` has both a key and a value.
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        """
        Arguments: key as a string -->
        Returns: index in the collection for the key-->
        This method returns a hashed key for the index of the array where the key/value pair should be placed.
        """
        chars_sum = 0

        for char in key:
            chars_sum += ord(char)

        chars_primed = chars_sum * 599
        index = chars_primed % self.size

        return index

    def set(self, key, value):
        """
        Arguments: a key as a string, and a value -->
        Returns: nothing -->
        This method hashes the key and sets the key/value pair in the table, handles collisions as needed,
        and should a given key already exist, the value will be replaced with the value argument given in the method
        call.
        """
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is None:
            bucket = LinkedList()
            self.buckets[index] = bucket

        # TODO: update vs insert
        bucket.insert((key, value))

    def get(self, key):
        """
        Arguments: a key as a string -->
        Returns: value associated with that key -->
        This method takes in a key, hashes it, and retrieves the value associated with that index.
        """
        index = self.hash(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next_

        return None

    def contains(self, key):
        """
        Arguments: a key as a string -->
        Returns: a boolean value -->
        This method takes in a key and returns a boolean value indicating if the key exists in the table.
        """
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is None:
            return False
        else:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next_
            return False

    def keys(self):
        key_list = []

        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    pair = current.value
                    key_list.append(pair[0])
                    current = current.next_
        return key_list
