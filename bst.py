import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree: TypeAlias = Union["Node", None]

@dataclass(frozen=True)
class Node:
    v: any
    l: BinTree
    r: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    bt: BinTree
    comes_before: Callable[[any, any], bool]

def compare(x: int ,y: int) -> bool:
    return x < y

# extree: BinarySearchTree(None, compare)

def is_empty(bst: BinarySearchTree) -> bool:
    return bst.x is None


def insert_helper(bt: BinTree, value: any, comes_before: Callable[[any, any], bool]) -> BinTree:
    match bt:
        case None:
            return Node(value, None, None)
        case Node(v, l, r):
            if comes_before(value, v):
                return Node(v, insert_helper(l, value, comes_before), r)
            else:
                return Node(v, l, insert_helper(r, value, comes_before))


def insert(bst: BinarySearchTree, value: any) -> BinarySearchTree:
    new_tree = insert_helper(bst.bt, value, bst.comes_before)
    return BinarySearchTree(new_tree, bst.comes_before)

def look_up(bst: BinarySearchTree, a: any) -> bool:
    return BinarySearchTree(Node(10, None, None),)

class TestBST(unittest.TestCase):
    def test_insert(self):
        tree = BinarySearchTree(None, compare)
        tree = insert(tree, 10)
        expected = BinarySearchTree(Node(10, None, None),compare)
        self.assertEqual(tree, expected)
