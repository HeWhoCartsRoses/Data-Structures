"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import unittest
import io
import sys
import random


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, val):
        if self is None:
            self = val
        else:
            if self.value <= val:
                if self.right is None:
                    self.right = BSTNode(val)
                else:
                    return self.right.insert(val)
            else:
                if self.left is None:
                    self.left = BSTNode(val)
                else:
                    return self.left.insert(val)

    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        arr = []
        def fn(x): return arr.append(x)
        self.node = node
        self.node.for_each(fn)
        arr.sort()
        print(*arr, sep='\n')
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def inorder(self, root, fn):
        if root:

            fn(root.value),
            root.inorder(root.right, fn)
            root.inorder(root.left, fn)

    def bft_print(self, node):
        arr = []
        def fn(x): return arr.append(x)
        self.node = node
        self.node.inorder(node, fn)
        print(*arr, sep='\n')
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        arr = []
        def fn(x): return arr.append(x)
        self.node = node
        self.node.for_each(fn)
        print(*arr, sep='\n')

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


class BinarySearchTreeTests(unittest.TestCase):

    def test_print_traversals(self):
        # WARNING:  Tests are for Print()
        # Debug calls to Print() in functions will cause failure

        self.bst = BSTNode(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)

        self.bst.bft_print(self.bst)

        stdout_ = sys.stdout  # Keep previous value
        sys.stdout = io.StringIO()
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n3\n7\n2\n4\n6\n" or
                        output == "1\n8\n5\n7\n3\n6\n4\n2\n")

        sys.stdout = io.StringIO()
        self.bst.dft_print(self.bst)
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n7\n6\n3\n4\n2\n" or
                        output == "1\n8\n5\n3\n2\n4\n7\n6\n")

        # sys.stdout = io.StringIO()
        # self.bst.pre_order_dft(self.bst)
        # output = sys.stdout.getvalue()
        # self.assertEqual(output, "1\n8\n5\n3\n2\n4\n7\n6\n")

        # sys.stdout = io.StringIO()
        # self.bst.post_order_dft(self.bst)
        # output = sys.stdout.getvalue()
        # self.assertEqual(output, "2\n4\n3\n6\n7\n5\n8\n1\n")

        sys.stdout = stdout_  # Restore stdout


if __name__ == '__main__':
    unittest.main()
