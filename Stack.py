import unittest


class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        self.check_if_empty()
        return self.items[-1]

    def pop(self):
        self.check_if_empty()
        value = self.items[-1]
        del self.items[-1]
        return value

    def __str__(self):
        self.check_if_empty()

        result = ""
        for item in self.items:
            result += str(item) + " "
        return result

    def check_if_empty(self):
        if self.is_empty():
            raise EmptyStackError


class TestStack(unittest.TestCase):

    def test_stack_creation_and_popping(self):
        stack = Stack()
        stack.push(10)
        stack.push(5)
        stack.push(2)
        stack.push(7)
        stack.pop()
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 5)
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())
