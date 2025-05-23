import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

class BSTTests(unittest.TestCase):

    def test_compare(self):
        self.assertTrue(compare(3, 5))
        self.assertFalse(compare(4, 4))
        self.assertFalse(compare(6, 2))

    def test_is_empty(self):
        tree = BinarySearchTree(None, compare)
        check = is_empty(tree)
        self.assertEqual(True, check)

    def test_insert_helper(self):
        result = insert_helper(None, 10, compare)
        expected = Node(10, None, None)
        self.assertEqual(result, expected)

        tree = Node(20, None, None)
        result = insert_helper(tree, 10, compare)
        expected = Node(20, Node(10, None, None), None)
        self.assertEqual(result, expected)

    def test_insert(self):
        tree = BinarySearchTree(None, compare)
        tree = insert(tree, 10)
        expected = BinarySearchTree(Node(10, None, None),compare)
        self.assertEqual(tree, expected)

    def test_look_up_helper(self):
        self.assertFalse(look_up_helper(None, 5, compare))
        
        tree = Node(10, None, None)
        self.assertTrue(look_up_helper(tree, 10, compare))
        
        tree = Node(10, Node(5, None, None), None)
        self.assertTrue(look_up_helper(tree, 5, compare))

    def test_look_up(self):
        tree = BinarySearchTree(Node(5, Node( 10, None, None), None), compare)
   
    def test_delete_helper(self):
        self.assertIsNone(delete_helper(None, 10, compare))
        
        tree = Node(10, None, None)
        result = delete_helper(tree, 10, compare)
        self.assertIsNone(result)

    def test_find_min(self):
        self.assertIsNone(find_min(None))
        
        tree = Node(10, None, None)
        self.assertEqual(find_min(tree), 10)
        
        tree = Node(20,Node(10, Node(5, None, None), Node(15, None, None)),Node(30, None, None))
        self.assertEqual(find_min(tree), 5)
        
    def test_delete(self):
        tree= BinarySearchTree(Node(5, Node(3, None, None), Node(7, None,None)), compare)
        result = delete(tree, 3)
        expected = BinarySearchTree(Node(5, None, Node(7, None, None)), compare)
        self.assertEqual(result, expected)

if (__name__ == '__main__'):
    unittest.main()
