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

# Function 1
# Return True if the tree is empty, False otherwise.
def is_empty(bst: BinarySearchTree) -> bool:
    return bst.bt is None

# Helper function for insert
def insert_helper(bt: BinTree, value: any, comes_before: Callable[[any, any], bool]) -> BinTree:
    match bt:
        case None:
            return Node(value, None, None)
        case Node(v, l, r):
            if comes_before(value, v):
                return Node(v, insert_helper(l, value, comes_before), r)
            else:
                return Node(v, l, insert_helper(r, value, comes_before))

# Function 2
# Adds the value to the binary search tree.
def insert(bst: BinarySearchTree, value: any) -> BinarySearchTree:
    new_tree = insert_helper(bst.bt, value, bst.comes_before)
    return BinarySearchTree(new_tree, bst.comes_before)

# Function 3
# Returns True if the value is stored in the tree and False otherwise.
def look_up(bst: BinarySearchTree, a: any) -> bool:
    return BinarySearchTree(Node(10, None, None),)

# Helper function for delete
def delete_helper(bt: BinTree, value: any, comes_before: Callable[[any, any], bool]) -> BinTree:
    match bt:
        case None:
            return None
        case Node(v, l, r):
            # going through left subtree
            if comes_before(value, v):
                return Node(v, delete_helper(l, value, comes_before), r)
            # going through right subtree
            elif comes_before(v, value):
                return Node(v, l, delete_helper(r, value, comes_before))
            # matches the current node
            else:
                # no children
                if l is None and r is None:
                    return None
                # only right child
                elif l is None:
                    return r
                # only left child
                elif r is None:
                    return l
                else:
                # two children, return the smallest on the right subtree and delete that smallest
                    smallest = find_min(r)
                    return Node(smallest, l, delete_helper(r, smallest, comes_before))

# find the leftmost node in the Binary Search Tree
def find_min(bt: BinTree):
    match bt:
        case None:
            return None
        case Node(v, None, r):
            return v
        case Node(v, l, r):
            return find_min(l)

# Function 4
# Removes the value from the tree
def delete(bst:BinarySearchTree, value: any) -> BinarySearchTree:
    new_tree = delete_helper(bst.bt, value, bst.comes_before)
    return BinarySearchTree(new_tree, bst.comes_before)
