import unittest


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity: int):
        assert capacity >= 0, ValueError("capacity has to be positive integer")
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:  # no collision case
            self.table[index] = new_node
        else:  # collision case
            current = self.table[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_node.next = self.table[index]
            self.table[index] = new_node
        return

    def remove(self, key):

        index = self._hash(key)
        previous = None
        current = self.table[index]
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        return

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False

    def __str__(self):
        result = ""
        for i in range(self.capacity):
            current = self.table[i]
            while current is not None:
                result += "key: " + str(current.key) + " - value: " + str(current.value) + " // "
                current = current.next
            result += "\n"
        return result


class TestHashTable(unittest.TestCase):
    def test_hash_table(self):
        hash_table = HashTable(capacity=4)
        hash_table.insert("apple", 5)
        hash_table.insert("pear", 3)
        hash_table.insert("apple", 1)
        hash_table.insert("tree", 1)
        hash_table.insert("book", 1)
        self.assertTrue(hash_table.search("book"))
        hash_table.remove("book")
        self.assertFalse(hash_table.search("book"))

