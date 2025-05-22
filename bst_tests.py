import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

class BSTTests(unittest.TestCase):

    def test_is_empty(self):
        tree = BinarySearchTree(None, compare)
        check = is_empty(tree)
        self.assertEqual(True, check)

    def test_insert(self):
        tree = BinarySearchTree(None, compare)
        tree = insert(tree, 10)
        expected = BinarySearchTree(Node(10, None, None),compare)
        self.assertEqual(tree, expected)

    def test_look_up(self):
        tree = BinarySearchTree(Node(5, Node( 10, None, None), None), compare)


    def test_delete(self):
        tree= BinarySearchTree(Node(5, Node(3, None, None), Node(7, None,None)), compare)
        result = delete(tree, 3)
        expected = BinarySearchTree(Node(5, None, Node(7, None, None)), compare)
        self.assertEqual(result, expected)

if (__name__ == '__main__'):
    unittest.main()
