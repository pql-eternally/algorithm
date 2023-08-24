"""
@Author : long
Date : 2023/1/28 17:33

链表是一堆节点的组合
Linked Lists consists of Nodes.
Nodes contain data and also may link to other nodes:
    - Head Node: First node, the address of the
                 head node gives us access of the complete list
    - Last node: points to null

各个py说明

单链表：
from_sequence：从序列生成链表
print_reverse：链表反转输出
middle_element_of_linked_list：取链表中间元素
swap_nodes：链表交换节点
circular_linked_list：环形链表
has_loop：链表是否有环
is_palindrome：是否回文链表
singly_linked_list：单链表
merge_two_lists：合并两个链表变成有序链表

双链表：
doubly_linked_list：双链表
doubly_linked_list_two：双链表
deque_doubly：双端队列

其它：
skip_list：跳表，参考自 https://epaperpress.com/sortsearch/download/skiplist.pdf
"""
from __future__ import annotations
from typing import Any, List


class Node:

    def __init__(self, data: Any, next: Node = None) -> None:
        self.data = data
        self.next = next

    def __str__(self):
        """
        输出当前节点及后续所有节点
        """
        data_list: List[str] = []
        node = self
        while node:
            data_list.append(str(node.data))
            node = node.next
        return " --> ".join(data_list)


class DoubleNode:

    def __init__(self, data: Any, pre: Any = None, next: Any = None):
        self.data = data
        self.pre = pre
        self.next = next
