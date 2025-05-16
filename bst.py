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
    y: Callable[]
    #
    # def comes_before(self):
    #     if l < v:
    #
    #     v < r

def example_fun(x : int) -> bool:
    return x < 142
