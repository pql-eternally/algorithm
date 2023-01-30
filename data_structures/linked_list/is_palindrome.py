"""
@Author : long
Date : 2023/1/29 17:36

是否回文链表
"""

from data_structures.linked_list import Node
from data_structures.linked_list.middle_linked_list import get_down_middle_node, get_up_middle_node
from data_structures.linked_list.reverse_linked_list import reverse_linked_list
from data_structures.linked_list.make_linked_list import make_linked_list


def is_palindrome(head: Node) -> bool:
    """
    使用快慢指针实现是否是回文链表
    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    False
    >>> head_node = make_linked_list([1, 2, 3, 2, 1])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    True
    >>> head_node = make_linked_list([1, 2, 3, 3, 2, 1])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    True
    """
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


def is_palindrome_stack(head: Node) -> bool:
    """
    使用栈实现是否是回文链表
    >>> head_node = make_linked_list([1, 2, 3, 4, 5])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    False
    >>> head_node = make_linked_list([1, 2, 3, 2, 1])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    True
    >>> head_node = make_linked_list([1, 2, 3, 3, 2, 1])
    >>> result = is_palindrome(head_node)
    >>> print(result)
    True
    """
    # 1、使用快慢指针寻找链表下中间节点作为第二个链表
    second = get_down_middle_node(head)

    # 2、使用栈存储第二部分
    stack = []
    current = second
    while current:
        stack.append(current.data)
        current = current.next

    # 3、弹出栈中元素和原链表相比较
    current = head
    while stack:
        if stack.pop() != current.data:
            return False
        current = current.next
    return True
