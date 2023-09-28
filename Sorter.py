import unittest
from BinarySearchTree import *


class Sorter:
    """
    Sorter class containing methods for different sorting algorithms.
    Based on https://www.bigocheatsheet.com/
    """


    @staticmethod
    def quick_sort(array: list) -> list:
        # quick sort algorithm implementation

        if len(array) <= 1:
            return array

        # take pivot halfway. Some other implementation take first or last element, but these run
        # into worse case scenario when array is already sorted
        pivot = array[len(array) // 2]

        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]

        return Sorter.quick_sort(left) + middle + Sorter.quick_sort(right)

    @staticmethod
    def merge_sort(array: list) -> list:
        """ merge sort algorithm """
        length = len(array)
        if length <= 1:
            return array
        left = array[:length // 2]
        right = array[length // 2:]

        # recursively sort left and right
        right = Sorter.merge_sort(right)
        left = Sorter.merge_sort(left)

        return Sorter._merge(left, right)

    @staticmethod
    def _merge(left: list, right: list) -> list:
        """Merges two arrays - left and right - into a sorted array"""
        array = []

        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                array.append(left[left_idx])
                left_idx += 1
            else:
                array.append(right[right_idx])
                right_idx += 1

        array.extend(left[left_idx:])
        array.extend(right[right_idx:])

        return array

    @staticmethod
    def heapify(array: list, n: int, i: int) -> None:
        """"Heapifies a subtree rooted in index i"""

        largest = i
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        # check if heap properties are satisfied
        if left_idx < n and array[left_idx] > array[largest]:
            largest = left_idx
        if right_idx < n and array[right_idx] > array[largest]:
            largest = right_idx

        # if not satisfied, heapify again
        if largest != i:
            array[largest], array[i] = array[i], array[largest]
            Sorter.heapify(array, n, largest)

    @staticmethod
    def heap_sort(array: list) -> list:
        """ heap sort algorithm"""
        array_length = len(array)

        # heapify the entire array, turning it into a heap
        for i in range(array_length // 2 - 1, -1, -1):
            Sorter.heapify(array, array_length, i)

        # Next element is at root of tree
        for i in range(array_length - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            Sorter.heapify(array, i, 0)
        return array

    @staticmethod
    def bubble_sort(array: list) -> list:
        """Sorts an array according to the Bubble Sort algorithm"""

        n = len(array)

        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True

            if swapped is False:
                break

        return array

    @staticmethod
    def insertion_sort(array: list) -> list:
        """Sorts an array according to the insertion sort algorithm"""

        n = len(array)

        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:

                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    @staticmethod
    def selection_sort(array: list) -> list:
        """Sorts an array ascending order according to Selection Sort algorithm"""
        n = len(array)
        if n <= 1:
            return array

        for i in range(n - 1):

            # find index that contains the minimum in the remaining part of the array
            min_index = i
            for j in range(i + 1, n):
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

        return array

    @staticmethod
    def tree_sort(array: list) -> list:
        binary_search_tree = BinarySearchTree()
        binary_search_tree.add_elements(array)
        return binary_search_tree.return_in_order()

    @staticmethod
    def shell_sort(array: list) -> list:
        """ Sorts an array according to the Shell Sort algorithm."""
        n = len(array)
        gap = n // 2

        while gap > 0:

            for i in range(gap, n):

                temp = array[i]
                j = i
                while j >= gap and temp < array[j - gap]:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp

            gap //= 2

        return array

    @staticmethod
    def bucket_sort(array: list) -> list:
        """Sorts an array according to Bucket Sort algorithm"""

        # step 1 : define buckets
        num_buckets = len(array)
        if num_buckets <= 1:
            return array
        min_value = min(array)
        max_value = max(array)
        if min_value == max_value:
            return array
        bucket_width = (max_value - min_value) / num_buckets

        buckets = [[] for _ in range(num_buckets)]

        # step 2 : put elements in buckets
        for element in array:
            index = int((element - min_value) / bucket_width)
            if index == num_buckets:
                index = -1
            buckets[index].append(element)

        # step 3 : sort buckets. Either recursively, or using insertion_sort or so
        for bucket in buckets:
            bucket = Sorter.bucket_sort(bucket)
            # bucket = Sorter.insertion_sort(bucket)

        # step 4 : combine buckets into final array
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    @staticmethod
    def radix_sort(array: list, base: int = 10) -> list:
        assert base > 1, ValueError("base has to be an integer > 1")

        def counting_sort(array, exp, base) -> None:

            # step 1 : create intermediary variables
            n = len(array)
            output = [0] * n
            count = [0] * base

            # step 2: loop over elements and count
            for i in range(n):
                index = array[i] // exp
                count[index % base] += 1

            # step 3: loop over count
            for i in range(1, base):
                count[i] += count[i - 1]

            # step 4: loop over elements
            for i in range(n - 1, -1, -1):
                index = array[i] // exp
                output[count[index % base] - 1] = array[i]
                count[index % base] -= 1

            # step 5 : copy result to array
            for i in range(n):
                array[i] = output[i]

        max_num = max(array)
        exp = 1

        while max_num // exp > 0:
            counting_sort(array, exp, base)
            exp *= base
        return array

    @staticmethod
    def tim_sort(array: list) -> list:
        """ very approximate tim_sort implementation"""

        MAX_INSERTION_SORT_SIZE = 32

        n = len(array)
        if n <= MAX_INSERTION_SORT_SIZE:  # insertion_sort
            return Sorter.insertion_sort(array)
        else:  # merge_sort
            left = array[:n // 2]
            right = array[n // 2:]

            # recursively sort left and right
            right = Sorter.tim_sort(right)
            left = Sorter.tim_sort(left)

            return Sorter._merge(left, right)


class SorterTest(unittest.TestCase):

    def test_quick_sort_num(self):
        test_array = [1, 5, 7, 8, 4, 4, 3, 2]
        sorted_array = Sorter.quick_sort(test_array)
        solution = [1, 2, 3, 4, 4, 5, 7, 8]
        self.assertEqual(sorted_array, solution)

    def test_quick_sort_string(self):
        test_array = ["1", "5", "ab", "aa", "test_word"]
        sorted_array = Sorter.quick_sort(test_array)
        solution = ["1", "5", "aa", "ab", "test_word"]
        self.assertEqual(sorted_array, solution)

    def test_quick_sort_range(self):
        n = 100
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.quick_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_merge_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.merge_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_heap_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.heap_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_bubble_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.bubble_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_insertion_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.insertion_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_selection_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.selection_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_tree_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.tree_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_shell_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.shell_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_bucket_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.bucket_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)

    def test_radix_sort_range(self):
        n = 10
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.radix_sort(test_array, base=10)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)


    def test_tim_sort_range(self):
        n = 100
        test_array = [x for x in range(n, -1, -1)]
        sorted_array = Sorter.tim_sort(test_array)
        solution = [x for x in range(n + 1)]
        self.assertEqual(sorted_array, solution)
