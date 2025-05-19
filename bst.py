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
    x: BinTree
    y: Callable[[any, any], bool]

def comes_before(x, y):
    return x < y

def example_fun(x : int) -> bool:
    return x < 142

def is_empty(bst: BinarySearchTree) -> bool:
    return bst.x is None
