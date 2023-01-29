"""
@Author : long
Date : 2023/1/29 14:03

"""
from typing import Any
from data_structures.linked_list import Node
from data_structures.linked_list.make_linked_list import make_linked_list


def swap_nodes(head: Node, node1_data: Any, node2_data: Any) -> Node:
    """
    交换两个节点的值
    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> result = swap_nodes(head_node, 2, 4)
    >>> print(result)
    1 --> 4 --> 3 --> 2 --> 5

    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> result = swap_nodes(head_node, 2, 6)
    >>> print(result)
    1 --> 2 --> 3 --> 4 --> 5
    """
    if node1_data == node2_data:
        return head
    node = head
    node1 = node2 = None
    while node and not (node1 and node2):
        if node1_data == node.data:
            node1 = node
        elif node2_data == node.data:
            node2 = node
        node = node.next
    if node1 is None or node2 is None:
        return head
    node1.data, node2.data = node2.data, node1.data
    return head
