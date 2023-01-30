"""
@Author : long
Date : 2023/1/29 17:36

是否回文链表
"""

from data_structures.linked_list import Node
from data_structures.linked_list.middle_linked_list import get_down_middle_node
from data_structures.linked_list.reverse_linked_list import reverse_linked_list
from data_structures.linked_list.make_linked_list import make_linked_list


def is_palindrome(head: Node) -> bool:
    """
    使用快慢指针实现是否是回文链表
    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    False
    """
    if not head:
        return True

    # 1、使用快慢指针寻找链表下中间节点作为第二个链表
    second = get_down_middle_node(head)
    # 2、反转第二个链表
    node = reverse_linked_list(second)
    # 3、依次比较两个链表的值
    while node:
        if node.data != head.data:
            return False
        node = node.next
        head = head.next
    return True
