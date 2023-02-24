"""
二叉搜索树
"""
from __future__ import annotations
from typing import Generic, TypeVar, Iterable, List

from data_structures.binary_tree import SearchNode

T = TypeVar("T")


class BinarySearchTree(Generic[T]):

    def __init__(self, root: SearchNode | None = None) -> None:
        self.root = root

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, *values) -> None:
        pass

    def search(self, value: T) -> SearchNode | None:
        pass

    def get_max_value(self, node: SearchNode | None) -> T | None:
        pass

    def get_min_value(self, node: SearchNode | None) -> T | None:
        pass

    def remove(self, value: T) -> None:
        pass

    def preorder(self, node: SearchNode | None) -> Iterable:
        pass

    def inorder(self, node: SearchNode | None) -> Iterable:
        pass

    def postorder(self, node: SearchNode | None) -> Iterable:
        pass

    def find_kth_smallest(self, k: int, node: SearchNode) -> List:
        """
        返回二叉树中k小的值
        """
        pass
