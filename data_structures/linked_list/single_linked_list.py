"""
@Author : long
Date : 2023/1/29 10:15

单链表相关案例
"""
from typing import Any, List
from data_structures.linked_list import Node


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
