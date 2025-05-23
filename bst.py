import sys
import unittest
from typing import *
from dataclasses import dataclass
import time
import random

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
    return look_up_helper(bst.bt, a, bst.comes_before)

def look_up_helper(bt:BinTree, value:any, comes_before:Callable[[any, any], bool]) -> bool:
    match bt:
        case None:
            return False
        case Node(v, l, r):
            if comes_before(value, v):
                return look_up_helper(l, value, comes_before)
            elif comes_before(v, value):
                return look_up_helper(r, value, comes_before)
            else:
                return True

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


# Performance measurement
def time_bst_insertion(size: int) -> float:
    values = [random.random() for _ in range(size)]
    tree = BinarySearchTree(None, compare)
    start = time.perf_counter()
    for v in values:
        tree = insert(tree, v)
    end = time.perf_counter()
    return end - start

def time_bst_look_up(size: int) -> float:
    values = [random.random() for _ in range(size)]
    tree = BinarySearchTree(None, compare)
    for v in values:
        tree = insert(tree, v)
    start = time.perf_counter()
    search_values = [random.random() for _ in range(size)]
    for v in search_values:
        look_up(tree, v)
    end = time.perf_counter()
    return end - start

for size in [100000 * i for i in range(1, 11)]:
    total = 0
    for _ in range(1):
        total += time_bst_look_up(size)
    print(f"{total:.6f}")
