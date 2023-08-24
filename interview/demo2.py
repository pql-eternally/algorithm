"""
给定一个树的根节点root，编写函数求树的最大深度
"""
from typing import Any
from __future__ import annotations  # noqa


class Node:

    def __init__(self, data: Any, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left
        self.right = right


def max_depth(root: Node) -> int:
    pass
