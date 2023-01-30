"""
@Author : long
Date : 2023/1/29 13:35

取链表中间节点
"""
from data_structures.linked_list import Node
from data_structures.linked_list.make_linked_list import make_linked_list


def get_up_middle_node(head: Node) -> Node:
    """
    取链表上中间节点
    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> middle_node = get_up_middle_node(head_node)
    >>> print(middle_node.data)
    3
    >>> head_node = make_linked_list([1, 2, 3, 4, 5, 6])
    >>> middle_node = get_up_middle_node(head_node)
    >>> print(middle_node.data)
    3
    """
    slow_pointer = fast_pointer = head
    while fast_pointer and fast_pointer.next and fast_pointer.next.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer


def get_down_middle_node(head: Node) -> Node:
    """
    取链表下中间节点
    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> middle_node = get_down_middle_node(head_node)
    >>> print(middle_node.data)
    3
    >>> head_node = make_linked_list([1, 2, 3, 4, 5, 6])
    >>> middle_node = get_down_middle_node(head_node)
    >>> print(middle_node.data)
    4
    """
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer
