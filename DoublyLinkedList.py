import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # inserts at tail
    def insert(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def delete(self, element):

        node = self.head
        while node is not None:
            if node.value == element:
                if node.previous is not None:
                    node.previous.next = node.next
                    if node.previous.next is None:
                        self.tail = node.previous

                if node.next is not None:
                    node.next.previous = node.previous
                    if node.next.previous is None:
                        self.head = node.next

                node.value = None
                node.next = None
                node.previous = None

                return

            else:
                node = node.next

    def __str__(self):
        result = ""
        node = self.head
        while node is not None:
            result += str(node.value) + " "
            node = node.next
        return result

    def search(self, element):

        node = self.head
        while node is not None:
            if node.value == element:
                return True
            else:
                node = node.next

        return False


class TestDoublyLinkedList(unittest.TestCase):

    def test_llinked_list(self):
        llist = DoublyLinkedList()
        array_to_insert = [1, 2, 5, 6, 0]
        for num in array_to_insert:
            llist.insert(num)
        self.assertTrue(llist.search(5))
        llist.delete(5)
        self.assertFalse(llist.search(5))
        self.assertTrue(llist.search(1))
        llist.delete(1)
        self.assertFalse(llist.search(1))
        self.assertTrue(llist.search(0))
        llist.delete(0)
        self.assertFalse(llist.search(0))
