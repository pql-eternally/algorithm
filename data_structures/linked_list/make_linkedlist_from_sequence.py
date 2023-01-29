"""
@Author : long
Date : 2023/1/29 10:43

从序列生成链表
"""
from typing import Any, List
from data_structures.linked_list import Node


def make_linked_list(data: List[Any]):
    """
    列表生成单链表
    >>> list_data = range(1, 6)
    >>> head_node = make_linked_list(list_data)
    >>> print(head_node)
    1 --> 2 --> 3 --> 4 --> 5
    """
    if not data:
        return None

    head = Node(data[0])
    current = head
    for item in data[1:]:
        node = Node(item)
        current.next = node
        current = node
    return head
