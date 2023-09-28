import unittest


class FullQueue(Exception):
    pass


class DynamicQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def size(self):
        len(self.items)

    def dequeue(self):
        value = self.items[0]
        del self.items[0]
        return value

    def peek_front(self):
        return self.data[0]

    def peek_back(self):
        return self.data[-1]


class FixedSizedQueue:
    """Fixed sized queue"""

    def __init__(self, max_size: int):
        if max_size <= 0:
            raise ValueError("max_size should be a positive integer")
        self.data = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.back = 0

    def size(self):
        return self.back - self.front

    def check_if_is_full(self):
        if self.is_full():
            raise FullQueue("Queue is filled at max capacity")

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.max_size

    def enqueue(self, element):
        self.check_if_is_full()
        self.data[self.back % self.max_size] = element
        self.back = self.back + 1

    def dequeue(self):
        if self.is_empty():
            return
        self.front = self.front + 1
        return self.data[(self.front - 1) % self.max_size]

    def peek_front(self):
        if self.is_empty():
            return
        return self.data[self.front % self.max_size]

    def peek_back(self):
        if self.is_empty():
            return
        return self.data[( self.back - 1) % self.max_size]

    def __str__(self):
        result = ""
        for i in range(self.size()):
            index = (self.front + i) % self.max_size
            result += str(self.data[index]) + " "

        return result


class TestQueue(unittest.TestCase):
    def test_fixed_sized_queue(self):
        queue = FixedSizedQueue(4)
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(4)
        queue.enqueue(0)
        self.assertEqual(queue.size(), 4)
        self.assertEqual(queue.peek_front(), 5)
        self.assertEqual(queue.peek_back(), 0)
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 4)

    def test_dynamic_queue(self):
        queue = DynamicQueue()
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(4)
        queue.enqueue(0)
        self.assertEqual(queue.size(), 4)
        self.assertEqual(queue.peek_front(), 5)
        self.assertEqual(queue.peek_back(), 0)
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 4)
