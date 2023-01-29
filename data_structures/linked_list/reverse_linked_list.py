"""
@Author : long
Date : 2023/1/29 11:06

反转单链表
"""
from data_structures.linked_list import Node
from data_structures.linked_list.make_linked_list import make_linked_list


def reverse_linked_list(head: Node) -> Node:
    """
    反转单链表
    >>> linked_list = make_linked_list([1, 2, 3, 4, 5])
    >>> print(reverse_linked_list(linked_list))
    5 --> 4 --> 3 --> 2 --> 1
    """
    current = head
    pre_node = None
    while current:
        next_node = current.next
        current.next = pre_node
        pre_node = current
        current = next_node
    return pre_node


def print_reverse(head: Node) -> None:
    """
    反转输出单链表
    >>> linked_list = make_linked_list([1, 2, 3, 4, 5])
    >>> print_reverse(linked_list)
    5
    4
    3
    2
    1
    """
    print_reverse(head.next)
    print(str(head.data))
