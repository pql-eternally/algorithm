"""
@Author : long
Date : 2023/1/28 17:33

链表是一堆节点的组合
Linked Lists consists of Nodes.
Nodes contain data and also may link to other nodes:
    - Head Node: First node, the address of the
                 head node gives us access of the complete list
    - Last node: points to null
"""
from typing import Any, List


class Node:
    def __init__(self, item: Any, next: Any) -> None:
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def add(self, item: Any) -> None:
        """
        往链表头部添加元素
        """
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self) -> Any:
        """
        移除链表头部元素
        """
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

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
            item_list.append(str(node.item))
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
