"""
二叉树基本操作
"""
from __future__ import annotations
from data_structures.binary_tree import Node


def inorder_traversal(root: Node | None) -> None:
    """
    二查询中序遍历
    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> root.left.left = Node(4)
    >>> root.left.right = Node(5)
    >>> inorder_traversal(root)
    4
    2
    5
    1
    3
    """
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)


def depth_of_tree(tree: Node | None) -> int:
    """
    二叉树的深度
    Recursive function that returns the depth of a binary tree.

    >>> root = Node(1)
    >>> depth_of_tree(root)
    1
    >>> root.left = Node(2)
    >>> depth_of_tree(root)
    2
    >>> root.right = Node(3)
    >>> depth_of_tree(root)
    2
    >>> root.left.right = Node(4)
    >>> depth_of_tree(root)
    3
    >>> depth_of_tree(root.left)
    2
    """
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right)) if tree else 0


def is_full_binary_tree(tree: Node | None) -> bool:
    """
    判断是否是满二叉树
    Returns True if this is a full binary tree

    >>> root = Node(1)
    >>> is_full_binary_tree(root)
    True
    >>> root.left = Node(2)
    >>> is_full_binary_tree(root)
    False
    >>> root.right = Node(3)
    >>> is_full_binary_tree(root)
    True
    >>> root.left.left = Node(4)
    >>> is_full_binary_tree(root)
    False
    >>> root.right.right = Node(5)
    >>> is_full_binary_tree(root)
    False
    """
    if not tree:
        return True

    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    return not tree.left and not tree.right
