import unittest


class Array:

    def __init__(self, size: int):
        if size < 0:
            raise ValueError("Size of array has to be a positive integer")
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index: int):
        self.check_if_index_exists(index)
        return self.data[index]

    def __setitem__(self, value, index: int):
        self.check_if_index_exists(index)
        self.data[index] = value

    def _resize(self):
        new_data = [None] * self.size * 2
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.size *= 2
        self.data = new_data

    def _is_full(self):
        return self.data[self.size - 1] is not None

    def insert(self, element, index):
        self.check_if_index_exists(index)
        if self._is_full():
            self._resize()
        for i in range(self.size - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element

    def check_if_index_exists(self, index):
        if index + 1 > self.size or index < 0:
            raise IndexError
        return True

    def delete(self, index):
        self.check_if_index_exists(index)
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None

    def search(self, element):
        for i in range(self.size):
            if self.data[i] == element:
                return i
        return None

    def print(self):
        result = []
        for i in range(self.size):
            result.append(self.data[i])

        print(result)
        return result


class TestArray(unittest.TestCase):

    def test_array_creation(self):
        test_array = Array(2)
        test_array.insert(1, 0)
        test_array.insert(2, 1)
        test_array.insert(3, 1)

        # size
        self.assertEqual(test_array.size, 4)
        # access
        self.assertEqual(test_array[2], 2)
        # insert
        test_array.insert(5, 3)
        self.assertEqual(test_array[3], 5)
        # delete
        test_array.delete(0)
        self.assertEqual(test_array[0], 3)
        # delete
        self.assertFalse(test_array.search(1))
        self.assertEqual(test_array.search(5), 2)
