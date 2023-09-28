import random
import unittest


class Node:
    def __init__(self, height: int, value=None):
        self.value = value
        self.next = [None] * height
        self.height = height

    def get_height(self):
        return self.height


class SkipList:

    def __init__(self, max_height: int, probability=0.25):

        assert 0 <= probability <= 1, ValueError("probability has to be between 0 and 1")
        assert 0 < max_height, ValueError("max_height has to be higher than 0")
        self.probability = probability
        self.max_height = max_height
        self.head = Node(max_height)

    def _random_height(self):
        height = 1
        while height < self.max_height and random.random() < self.probability:
            height += 1
        return height

    def insert(self, value):

        height = self._random_height()
        new_node = Node(height, value)
        update_list = self._update_list(value)
        for level in range(height):
            new_node.next[level] = update_list[level].next[level]
            update_list[level].next[level] = new_node

    def _update_list(self, value):

        update_list = [None] * self.max_height
        node = self.head
        for level in range(self.max_height - 1, -1, -1):

            while node.next[level] is not None and node.next[level].value < value:
                node = node.next[level]
            update_list[level] = node

        return update_list

    def display(self):

        for i in range(self.max_height):
            print("\nlvl : {}".format(i))
            current = self.head.next[i]
            while current is not None:
                print(current.value, end=" ")
                current = current.next[i]

    def search(self, value):
        node = self.head
        for level in range(self.max_height - 1, -1, -1):
            while node.next[level] is not None and node.next[level].value < value:
                node = node.next[level]

        if node.next[0] is not None and node.next[0].value == value:
            return True
        return False

    def delete(self, value):

        update_list = self._update_list(value)
        if update_list[0].next[0] is not None and update_list[0].next[0].value == value:
            for level in range(update_list[0].next[0].get_height()):
                if update_list[level].next[level] is not None:
                    update_list[level].next[level] = update_list[level].next[level].next[level]


class TestSkipList(unittest.TestCase):
    def test_skip_list(self):
        skip_list = SkipList(max_height=4, probability=0.5)
        array = [1, 2, 5, 7, 4, 4, 6, 0, 10, 50, -10, -5]
        for num in array:
            skip_list.insert(num)

        self.assertTrue(skip_list.search(6))
        skip_list.delete(50)
        self.assertFalse(skip_list.search(50))
        skip_list.delete(-10)
        self.assertFalse(skip_list.search(-10))
        self.assertTrue(skip_list.search(10))

