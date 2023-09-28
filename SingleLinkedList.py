import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        value = self.head.data
        self.head = self.head.next
        return value

    def search(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                return True
            node = node.next
        return False

    def __str__(self):
        result = ""
        node = self.head
        while node is not None:
            result += str(node.data) + " "
            node = node.next
        return result


class TestSingleLinkedList(unittest.TestCase):
    def test_linked_list(self):
        llist = SingleLinkedList()
        llist.push(5)
        llist.push(4)
        llist.push(2)
        llist.push(0)
        llist.pop()
        self.assertEqual(llist.pop(), 2)
        self.assertTrue(llist.search(5))
        self.assertFalse(llist.search(2))
