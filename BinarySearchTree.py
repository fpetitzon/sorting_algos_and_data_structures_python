import unittest


class BinarySearchTree1:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add_elements(self, elements):
        for element in elements:
            self.add(element)

    def add(self, element):
        if self.value is None:
            self.value = element
        elif element < self.value:
            if self.left is None:
                self.left = BinarySearchTree(element)
            else:
                self.left.add(element)
        else:
            if self.right is None:
                self.right = BinarySearchTree(element)
            else:
                self.right.add(element)

    def return_in_order(self):
        if self.value is None:
            return
        result = []

        if self.left is not None:
            result = self.left.return_in_order()

        result.append(self.value)

        if self.right is not None:
            result += self.right.return_in_order()

        return result

    def search(self, value):
        if self.value is None:
            return False
        elif self.value == value:
            return True
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        return False

    def delete(self, value):

        current = self
        parent = None

        while current is not None:

            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right

            elif current.value == value:
                current.value = None

                # case 1 no children
                if current.left is None and current.right is None:
                    if parent is None:
                        return
                    elif parent.left == current:
                        parent.left = None
                    elif parent.right == current:
                        parent.right = None

                # case 2 1 child
                elif current.left is None:
                    if parent is None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    elif parent.left == current:
                        parent.left = current.right
                    elif parent.right == current:
                        parent.right = current.right

                elif current.right is None:
                    if parent is None:
                        current.value = current.left.value
                        current.left = current.left.left
                        current.right = current.left.right
                    elif parent.left == current:
                        parent.left = current.left
                    elif parent.right == current:
                        parent.right = current.left

                # case 3: 2 children
                # Find the minimum value in the right subtree
                else:
                    successor = current.right
                    while successor.left is not None:
                        successor = successor.left

                    current.value = successor.value
                    current.right.delete(successor.value)

                return

        return


class TestBinarySearchTree(unittest.TestCase):
    def test_bstree(self):
        bst = BinarySearchTree()
        test_array = [1, 2, 5, -5, 9, 7, 10, -5]
        bst.add_elements(test_array)
        self.assertTrue(bst.search(7))
        bst.delete(7)
        self.assertFalse(bst.search(7))
        self.assertEqual(bst.return_in_order(), [-5, -5, 1, 2, 5, 9, 10])
