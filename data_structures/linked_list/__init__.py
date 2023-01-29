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
from typing import Any, List


class Node:

    def __init__(self, data: Any, next: Any = None) -> None:
        self.data = data
        self.next = next


class DoubleNode:

    def __init__(self, data: Any, pre: Any = None, next: Any = None):
        self.data = data
        self.pre = pre
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def add(self, data: Any) -> None:
        """
        往链表头部添加元素
        """
        self.head = Node(data, self.head)
        self.size += 1

    def remove(self) -> Any:
        """
        移除链表头部元素
        """
        if self.is_empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        """
        >>> linked_list = LinkedList()
        >>> linked_list.add(1)
        >>> linked_list.add(2)
        >>> linked_list.add(3)
        >>> print(linked_list)
        3 --> 2 --> 1
        """
        if self.is_empty():
            return ""

        item_list: List[str] = []
        node = self.head
        while node:
            item_list.append(str(node.data))
            node = node.next
        return " --> ".join(item_list)

    def __len__(self) -> int:
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> node = linked_list.remove()
        >>> node
        'b'
        >>> len(linked_list)
        1
        >>> node = linked_list.remove()
        >>> node
        'a'
        >>> len(linked_list)
        0
        >>> node = linked_list.remove()
        >>> node
        """
        return self.size
