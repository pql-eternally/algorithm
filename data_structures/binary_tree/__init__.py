from __future__ import annotations

from typing import TypeVar, Generic

T = TypeVar("T")


# 二叉树节点
class Node(Generic[T]):
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: T) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class SearchNode(Generic[T]):
    """
    搜索树节点
    """

    def __init__(self, data: T) -> None:
        self.data = data
        self.parent: Node | None = None
        self.left: Node | None = None
        self.right: Node | None = None
