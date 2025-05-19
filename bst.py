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
    new_tree = insert_helper(bst.x, value, bst.y)
    return BinarySearchTree(new_tree, bst.y)


class TestBST(unittest.TestCase):
    def test_insert(self):
        tree = BinarySearchTree(None, comes_before)
        tree = insert(tree, 10)
        self.assertEqual(tree, BinarySearchTree)
